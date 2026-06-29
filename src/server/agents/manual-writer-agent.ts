import { DEFAULT_BOOK_ID, getHermesConfig, getKimiConfig, getOpenAiConfig, getWriterConfig, type WriterProvider } from "../config"
import { completeWithClaudeCode } from "../llm/claude-code-adapter"
import { completeWithCodexCli } from "../llm/codex-cli-adapter"
import { HermesLlmClient } from "../llm/hermes-adapter"
import { OpenAiLlmClient } from "../llm/openai-adapter"
import { LocalAgentMemory } from "../memory/local-agent-memory"
import { parseFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"
import { slugify } from "../wiki/slug"
import { readFile } from "node:fs/promises"
import path from "node:path"

export type ManualWriterMode = "draft" | "expand" | "improve" | "integrate" | "format"

export interface ChapterOption {
  path: string
  title: string
  bookId: string
  outlineSection: string
  status: string
  reviewRequired: boolean
}

export interface ManualWriterInput {
  chapterPath: string
  instruction: string
  mode: ManualWriterMode
  provider?: WriterProvider
}

export interface ManualRevisionInput {
  chapterPath: string
  instruction?: string
  provider?: WriterProvider
}

export interface ManualWriterResult {
  status: "completed"
  chapterPath: string
  changedFiles: string[]
  knowledgeUsed: string[]
  draft: string
  writerProvider: WriterProvider
  memoryUsed: string[]
  warnings: string[]
  revisionDiff?: RevisionDiffSummary
}

export interface RevisionDiffSummary {
  changed: boolean
  additions: number
  deletions: number
  beforeWordCount: number
  afterWordCount: number
  previewLines: RevisionDiffLine[]
}

export interface RevisionDiffLine {
  type: "added" | "removed"
  lineNumber: number
  text: string
}

interface KnowledgeItem {
  path: string
  title: string
  summary: string
}

const BASE_WRITER_SYSTEM_PROMPT =
  "Sei Manual Writer Agent di ConcorsoBook OS. Scrivi manuali e libri operativi per concorsi pubblici. Usa solo knowledge consolidata fornita: source notes, topic pages, entity pages. Non citare o usare raw sources direttamente. Scrivi in italiano, stile workbook professionale, chiaro e didattico."

const ITALIAN_EDITORIAL_QUALITY_RULES = [
  "Regole obbligatorie di qualita' linguistica: scrivi in italiano naturale, corretto e professionale.",
  "Ogni frase deve avere soggetto, verbo e punteggiatura compiuta; evita frammenti telegrafici e frasi nominali usate come spiegazione.",
  "Inserisci sempre articoli, preposizioni e connettivi quando l'italiano li richiede: scrivi 'il candidato', 'la commissione', 'un procedimento', 'l'amministrazione', non formule spezzate o appunti.",
  "Usa virgole, punti, due punti e punti e virgola in modo controllato; non concatenare periodi lunghi senza pause.",
  "Controlla accenti e apostrofi: e', perche', puo', piu', l'amministrazione, un'istanza. Non produrre testo con caratteri corrotti o parole tronche.",
  "Spiega prima il concetto, poi la funzione, poi l'uso in prova; il lettore deve capire senza conoscere gia' la materia.",
  "Prima di restituire il capitolo, fai una revisione interna di chiarezza, articoli, punteggiatura, coerenza e scorrevolezza, senza stampare la checklist."
].join("\n")

export class ManualWriterAgent {
  constructor(private readonly store: FileWikiStore) {}

  async listChapters(bookId?: string): Promise<ChapterOption[]> {
    const files = await this.store.listMarkdown("books")
    const chapters: ChapterOption[] = []

    for (const file of files.filter((item) => item.includes("/chapters/"))) {
      const content = await this.store.readText(file)
      const parsed = parseFrontmatter(content)
      const data = parsed.data as any
      const declaredBookId = String(data.book_id || data.extra?.book_id || "")
      const currentBookId = bookIdFromChapterPath(file) || declaredBookId || "unknown"

      if (bookId && currentBookId !== bookId && declaredBookId !== bookId) {
        continue
      }

      chapters.push({
        path: file,
        title: String(data.title || file),
        bookId: currentBookId,
        outlineSection: String(data.outline_section || data.extra?.outline_section || ""),
        status: String(data.status || "draft"),
        reviewRequired: Boolean(data.review_required)
      })
    }

    return chapters.sort(compareChapters)
  }

  async writeChapter(input: ManualWriterInput): Promise<ManualWriterResult> {
    if (!input.chapterPath.startsWith("books/") || !input.chapterPath.endsWith(".md")) {
      throw new Error("Manual Writer Agent can only write markdown files under books/")
    }

    if (!(await this.store.exists(input.chapterPath))) {
      throw new Error(`Chapter not found: ${input.chapterPath}`)
    }

    const chapterContent = await this.store.readText(input.chapterPath)
    const chapter = parseFrontmatter(chapterContent)
    const knowledge = await this.loadKnowledgePack(chapter.data)
    const structureGuide = await this.loadStructureGuide(input.chapterPath)
    const designGuide = await this.loadDesignGuide(input.chapterPath)
    const memory = LocalAgentMemory.fromConfig()
    const memoryRecall = await memory.recall({
      scope: "manual-writer",
      query: [
        String(chapter.data.title || input.chapterPath),
        input.chapterPath,
        input.mode,
        input.instruction,
        asStringArray(chapter.data.topics).join(" "),
        asStringArray(chapter.data.source_refs).join(" ")
      ].join("\n")
    })
    const generation = await this.generateDraft({
      title: String(chapter.data.title || input.chapterPath),
      instruction: input.instruction,
      mode: input.mode,
      provider: input.provider,
      chapterContent,
      structureGuide,
      designGuide,
      knowledge,
      memoryContext: memoryRecall.context
    })
    const draft = generation.text
    const now = new Date().toISOString()

    const targetHeading = input.mode === "draft" ? "Bozza agente" : "Testo editoriale"
    await this.store.patchHeading(input.chapterPath, targetHeading, draft)
    await this.store.updateFrontmatter(input.chapterPath, {
      status: input.mode === "draft" ? "draft" : "to_expand",
      review_required: true,
      updated_at: now,
      last_manual_writer_run: now
    })
    await this.store.appendText(
      "log.md",
      `\n- ${now} | manual_writer | ${input.chapterPath} | mode=${input.mode} | target_heading=${targetHeading} | knowledge=${knowledge.length} | memory=${memoryRecall.memories.length}`
    )
    await memory.captureConversation({
      scope: "manual-writer",
      route: "ManualWriterAgent.writeChapter",
      messages: [
        {
          role: "user",
          content: [
            `chapterPath=${input.chapterPath}`,
            `mode=${input.mode}`,
            `instruction=${input.instruction || "Scrivi una bozza editoriale migliorata."}`
          ].join("\n")
        }
      ],
      reply: [
        `Manual Writer completato su ${input.chapterPath}.`,
        `Provider: ${generation.provider}.`,
        `Knowledge consolidata usata: ${knowledge.map((item) => item.path).join(", ") || "none"}.`,
        generation.warnings.length > 0 ? `Warnings: ${generation.warnings.join(" | ")}` : ""
      ].filter(Boolean).join("\n"),
      metadata: {
        chapterPath: input.chapterPath,
        mode: input.mode,
        provider: generation.provider,
        recalledMemories: memoryRecall.memories.length
      }
    }).catch(() => undefined)

    return {
      status: "completed",
      chapterPath: input.chapterPath,
      changedFiles: [input.chapterPath, "log.md"],
      knowledgeUsed: knowledge.map((item) => item.path),
      draft,
      writerProvider: generation.provider,
      memoryUsed: memoryRecall.memories.map((item) => item.id),
      warnings: generation.warnings
    }
  }

  async reviseChapter(input: ManualRevisionInput): Promise<ManualWriterResult> {
    if (!input.chapterPath.startsWith("books/") || !input.chapterPath.endsWith(".md")) {
      throw new Error("Manual Writer Agent can only revise markdown files under books/")
    }

    if (!(await this.store.exists(input.chapterPath))) {
      throw new Error(`Chapter not found: ${input.chapterPath}`)
    }

    const chapterContent = await this.store.readText(input.chapterPath)
    const chapter = parseFrontmatter(chapterContent)
    const chapterBody = extractMarkdownBody(chapterContent)
    const knowledge = await this.loadKnowledgePack(chapter.data)
    const structureGuide = await this.loadStructureGuide(input.chapterPath)
    const designGuide = await this.loadDesignGuide(input.chapterPath)
    const memory = LocalAgentMemory.fromConfig()
    const memoryRecall = await memory.recall({
      scope: "manual-writer",
      query: [
        String(chapter.data.title || input.chapterPath),
        input.chapterPath,
        "humanizer revisione stile capitolo testo editoriale",
        input.instruction || "",
        asStringArray(chapter.data.topics).join(" "),
        asStringArray(chapter.data.source_refs).join(" ")
      ].join("\n")
    })
    const generation = await this.generateHumanizedRevision({
      title: String(chapter.data.title || input.chapterPath),
      instruction: input.instruction || "",
      provider: input.provider,
      chapterContent,
      chapterBody,
      structureGuide,
      designGuide,
      knowledge,
      memoryContext: memoryRecall.context
    })
    const draft = sanitizeRevisionBody(generation.text, chapterBody)
    const revisionDiff = buildRevisionDiff(chapterBody, draft)
    const now = new Date().toISOString()
    const nextContent = patchRawFrontmatter(
      replaceMarkdownBodyPreservingFrontmatter(chapterContent, draft),
      {
        status: "revised_draft",
        review_required: true,
        updated_at: now,
        draft_stage: "humanized-editorial-revision",
        last_humanizer_revision: now
      }
    )

    await this.store.writeText(input.chapterPath, nextContent)
    await this.store.appendText(
      "log.md",
      `\n- ${now} | humanizer_revision | ${input.chapterPath} | provider=${generation.provider} | knowledge=${knowledge.length} | memory=${memoryRecall.memories.length}`
    )
    await memory.captureConversation({
      scope: "manual-writer",
      route: "ManualWriterAgent.reviseChapter",
      messages: [
        {
          role: "user",
          content: [
            `chapterPath=${input.chapterPath}`,
            "mode=humanizer_revision",
            `instruction=${input.instruction || "Applica revisione humanizer al capitolo."}`
          ].join("\n")
        }
      ],
      reply: [
        `Revisione humanizer completata su ${input.chapterPath}.`,
        `Provider: ${generation.provider}.`,
        `Knowledge consolidata usata: ${knowledge.map((item) => item.path).join(", ") || "none"}.`,
        generation.warnings.length > 0 ? `Warnings: ${generation.warnings.join(" | ")}` : ""
      ].filter(Boolean).join("\n"),
      metadata: {
        chapterPath: input.chapterPath,
        mode: "humanizer_revision",
        provider: generation.provider,
        recalledMemories: memoryRecall.memories.length
      }
    }).catch(() => undefined)

    return {
      status: "completed",
      chapterPath: input.chapterPath,
      changedFiles: [input.chapterPath, "log.md"],
      knowledgeUsed: knowledge.map((item) => item.path),
      draft,
      writerProvider: generation.provider,
      memoryUsed: memoryRecall.memories.map((item) => item.id),
      warnings: generation.warnings,
      revisionDiff
    }
  }

  private async loadKnowledgePack(frontmatter: Record<string, unknown>) {
    const items: KnowledgeItem[] = []
    const sourceRefs = asStringArray(frontmatter.source_refs)
      .filter((ref) => ref.startsWith("sources/"))
      .slice(0, 12)
    const topicRefs = asStringArray(frontmatter.topics)
      .map((topic) => `topics/${slugify(topic)}.md`)
      .slice(0, 14)
    const entityRefs = asStringArray(frontmatter.entities)
      .map((entity) => `entities/${slugify(entity)}.md`)
      .slice(0, 10)

    for (const ref of [...sourceRefs, ...topicRefs, ...entityRefs]) {
      if (ref.startsWith("raw/")) continue
      if (!(await this.store.exists(ref))) continue

      const content = await this.store.readText(ref)
      const parsed = parseFrontmatter(content)
      items.push({
        path: ref,
        title: String(parsed.data.title || ref),
        summary: extractUsefulSummary(content)
      })
    }

    return dedupeByPath(items)
  }

  private async loadStructureGuide(chapterPath: string) {
    const bookId = bookIdFromChapterPath(chapterPath) || DEFAULT_BOOK_ID
    let path = `books/${bookId}/struttura-madre.md`
    if (!(await this.store.exists(path))) {
      path = `books/${DEFAULT_BOOK_ID}/struttura-madre.md`
    }
    if (!(await this.store.exists(path))) return ""

    return this.store.readText(path)
  }

  private async loadDesignGuide(chapterPath: string) {
    const bookId = bookIdFromChapterPath(chapterPath) || DEFAULT_BOOK_ID
    let path = `books/${bookId}/design-system-editoriale.md`
    if (!(await this.store.exists(path))) {
      path = `books/${DEFAULT_BOOK_ID}/design-system-editoriale.md`
    }
    if (!(await this.store.exists(path))) return ""

    return this.store.readText(path)
  }

  private async generateDraft(input: {
    title: string
    instruction: string
    mode: ManualWriterMode
    chapterContent: string
    structureGuide: string
    designGuide: string
    knowledge: KnowledgeItem[]
    memoryContext: string
    provider?: WriterProvider
  }) {
    const writerConfig = getWriterConfig()
    const provider = input.provider || writerConfig.provider

    if (provider === "codex") {
      try {
        const skill = await loadProfessionalWriterSkill()
        const response = await completeWithCodexCli(renderCodexPrompt(input, skill))
        const text = response.text.trim()

        if (text && !looksLikeMetaDraft(text)) {
          return {
            text,
            provider: "codex" as const,
            warnings: response.stderr.trim() ? [`Codex CLI stderr: ${trimWords(response.stderr, 40)}`] : []
          }
        }
      } catch (error) {
        return {
          text: renderDeterministicDraft(input),
          provider: "local" as const,
          warnings: [`Codex CLI non disponibile o non autenticato: ${error instanceof Error ? error.message : "errore sconosciuto"}`]
        }
      }
    }

    if (provider === "claude") {
      try {
        const skill = await loadProfessionalWriterSkill()
        const response = await completeWithClaudeCode(renderClaudePrompt(input, skill))
        const text = response.text.trim()

        if (text && !looksLikeMetaDraft(text)) {
          return {
            text,
            provider: "claude" as const,
            warnings: response.stderr.trim() ? [`Claude Code stderr: ${trimWords(response.stderr, 40)}`] : []
          }
        }
      } catch (error) {
        return {
          text: renderDeterministicDraft(input),
          provider: "local" as const,
          warnings: [`Claude Code non disponibile o non autenticato: ${error instanceof Error ? error.message : "errore sconosciuto"}`]
        }
      }
    }

    if (provider === "hermes") {
      const config = getHermesConfig()

      if (!config.apiKey) {
        return {
          text: renderDeterministicDraft(input),
          provider: "local" as const,
          warnings: ["HERMES_API_KEY non configurata: usata bozza locale strutturata."]
        }
      }

      const llm = new HermesLlmClient()
      const response = await llm.complete(renderManualWriterMessages(input))

      if (looksLikeMetaDraft(response)) {
        return {
          text: renderDeterministicDraft(input),
          provider: "local" as const,
          warnings: ["Risposta Hermes scartata perche conteneva testo meta invece di un capitolo editoriale."]
        }
      }

      return {
        text: response.trim() || renderDeterministicDraft(input),
        provider: response.trim() ? ("hermes" as const) : ("local" as const),
        warnings: response.trim() ? [] : ["Risposta Hermes vuota: usata bozza locale strutturata."]
      }
    }

    if (provider === "local") {
      return {
        text: renderDeterministicDraft(input),
        provider: "local" as const,
        warnings: []
      }
    }

    if (provider === "kimi") {
      const config = getKimiConfig()

      if (!config.apiKey) {
        return {
          text: renderDeterministicDraft(input),
          provider: "local" as const,
          warnings: ["KIMI_API_KEY non configurata: usata bozza locale strutturata."]
        }
      }

      const llm = new OpenAiLlmClient({
        apiKey: config.apiKey,
        baseURL: config.baseUrl,
        model: config.model
      })
      const response = await llm.complete(renderManualWriterMessages(input))

      if (looksLikeMetaDraft(response)) {
        return {
          text: renderDeterministicDraft(input),
          provider: "local" as const,
          warnings: ["Risposta Kimi scartata perche conteneva testo meta invece di un capitolo editoriale."]
        }
      }

      return {
        text: response.trim() || renderDeterministicDraft(input),
        provider: response.trim() ? ("kimi" as const) : ("local" as const),
        warnings: response.trim() ? [] : ["Risposta Kimi vuota: usata bozza locale strutturata."]
      }
    }

    const config = getOpenAiConfig()

    if (!config.apiKey) {
      return {
        text: renderDeterministicDraft(input),
        provider: "local" as const,
        warnings: ["OPENAI_API_KEY non configurata: usata bozza locale strutturata."]
      }
    }

    const llm = new OpenAiLlmClient()
    const response = await llm.complete([
      {
        role: "system",
        content: `${BASE_WRITER_SYSTEM_PROMPT}\n\n${ITALIAN_EDITORIAL_QUALITY_RULES}`
      },
      {
        role: "user",
        content: [
          `Capitolo target: ${input.title}`,
          `Modalita: ${input.mode}`,
          `Istruzione utente: ${input.instruction || "Scrivi una bozza editoriale migliorata."}`,
          ...renderMemoryPromptSection(input.memoryContext),
          "Knowledge consolidata disponibile:",
          ...input.knowledge.map((item) => `\n### ${item.title}\nPath: ${item.path}\n${item.summary}`),
          "\nGuida operativa canonica del manuale:",
          trimWords(input.structureGuide.replace(/^---[\s\S]*?---/, ""), 1000),
          "\nDesign system editoriale canonico:",
          trimWords(input.designGuide.replace(/^---[\s\S]*?---/, ""), 800),
          "\nCapitolo esistente e struttura editoriale da rispettare:",
          trimWords(input.chapterContent.replace(/^---[\s\S]*?---/, ""), 900),
          "\nProduci testo pronto per un manuale-workbook professionale. Formato obbligatorio: apertura editoriale, obiettivo, mappa BANDO, spiegazione strutturata, box da sapere in 5 righe, caso guidato, domanda da commissario, domanda-trappola, mini-esercizio, errore tipico, riferimenti consolidati, note di review. Integra la richiesta dell'utente e la conoscenza nuova senza cancellare tracciabilità.",
          "\nRegole obbligatorie di italiano editoriale:",
          ITALIAN_EDITORIAL_QUALITY_RULES,
          "Divieto assoluto: non scrivere sezioni meta come 'Aggiornamento generato', 'Istruzione ricevuta', 'Knowledge consolidata', 'questo blocco sviluppa'. Non riassumere le fonti. Scrivi direttamente il capitolo destinato al lettore.",
          "Se il capitolo richiede aggiornamenti web o verifica normativa corrente e le fonti consolidate non bastano, segnala in 'Note di review' quali ricerche web ufficiali servono. Non inventare dati non presenti."
        ].join("\n")
      }
    ])

    if (looksLikeMetaDraft(response)) {
      return {
        text: renderDeterministicDraft(input),
        provider: "local" as const,
        warnings: ["Risposta LLM scartata perché conteneva testo meta invece di un capitolo editoriale."]
      }
    }

    return {
      text: response.trim() || renderDeterministicDraft(input),
      provider: response.trim() ? ("openai" as const) : ("local" as const),
      warnings: response.trim() ? [] : ["Risposta OpenAI vuota: usata bozza locale strutturata."]
    }
  }

  private async generateHumanizedRevision(input: {
    title: string
    instruction: string
    chapterContent: string
    chapterBody: string
    structureGuide: string
    designGuide: string
    knowledge: KnowledgeItem[]
    memoryContext: string
    provider?: WriterProvider
  }) {
    const writerConfig = getWriterConfig()
    const provider = input.provider || writerConfig.provider
    const localRevision = () => renderDeterministicHumanizedRevision(input)

    if (provider === "local") {
      return {
        text: localRevision(),
        provider: "local" as const,
        warnings: []
      }
    }

    if (provider === "codex") {
      try {
        const [writerSkill, humanizerSkill] = await Promise.all([loadProfessionalWriterSkill(), loadHumanizerSkill()])
        const response = await completeWithCodexCli(renderHumanizerPrompt(input, writerSkill, humanizerSkill, "Codex CLI locale"))
        const text = response.text.trim()

        if (isUsableRevision(text, input.chapterBody)) {
          return {
            text,
            provider: "codex" as const,
            warnings: response.stderr.trim() ? [`Codex CLI stderr: ${trimWords(response.stderr, 40)}`] : []
          }
        }

        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: ["Risposta Codex scartata: non sembrava una revisione completa del capitolo."]
        }
      } catch (error) {
        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: [`Codex CLI non disponibile o non autenticato: ${error instanceof Error ? error.message : "errore sconosciuto"}`]
        }
      }
    }

    if (provider === "claude") {
      try {
        const [writerSkill, humanizerSkill] = await Promise.all([loadProfessionalWriterSkill(), loadHumanizerSkill()])
        const response = await completeWithClaudeCode(renderHumanizerPrompt(input, writerSkill, humanizerSkill, "Claude Code locale"))
        const text = response.text.trim()

        if (isUsableRevision(text, input.chapterBody)) {
          return {
            text,
            provider: "claude" as const,
            warnings: response.stderr.trim() ? [`Claude Code stderr: ${trimWords(response.stderr, 40)}`] : []
          }
        }

        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: ["Risposta Claude scartata: non sembrava una revisione completa del capitolo."]
        }
      } catch (error) {
        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: [`Claude Code non disponibile o non autenticato: ${error instanceof Error ? error.message : "errore sconosciuto"}`]
        }
      }
    }

    const humanizerSkill = await loadHumanizerSkill()

    if (provider === "hermes") {
      const config = getHermesConfig()

      if (!config.apiKey) {
        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: ["HERMES_API_KEY non configurata: usata revisione locale conservativa."]
        }
      }

      const llm = new HermesLlmClient()
      const response = await llm.complete(renderHumanizerMessages(input, humanizerSkill))

      if (!isUsableRevision(response, input.chapterBody)) {
        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: ["Risposta Hermes scartata: non sembrava una revisione completa del capitolo."]
        }
      }

      return { text: response.trim(), provider: "hermes" as const, warnings: [] }
    }

    if (provider === "kimi") {
      const config = getKimiConfig()

      if (!config.apiKey) {
        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: ["KIMI_API_KEY non configurata: usata revisione locale conservativa."]
        }
      }

      const llm = new OpenAiLlmClient({
        apiKey: config.apiKey,
        baseURL: config.baseUrl,
        model: config.model
      })
      const response = await llm.complete(renderHumanizerMessages(input, humanizerSkill))

      if (!isUsableRevision(response, input.chapterBody)) {
        return {
          text: localRevision(),
          provider: "local" as const,
          warnings: ["Risposta Kimi scartata: non sembrava una revisione completa del capitolo."]
        }
      }

      return { text: response.trim(), provider: "kimi" as const, warnings: [] }
    }

    const config = getOpenAiConfig()

    if (!config.apiKey) {
      return {
        text: localRevision(),
        provider: "local" as const,
        warnings: ["OPENAI_API_KEY non configurata: usata revisione locale conservativa."]
      }
    }

    const llm = new OpenAiLlmClient()
    const response = await llm.complete(renderHumanizerMessages(input, humanizerSkill))

    if (!isUsableRevision(response, input.chapterBody)) {
      return {
        text: localRevision(),
        provider: "local" as const,
        warnings: ["Risposta OpenAI scartata: non sembrava una revisione completa del capitolo."]
      }
    }

    return { text: response.trim(), provider: "openai" as const, warnings: [] }
  }
}

function renderManualWriterMessages(input: {
  title: string
  instruction: string
  mode: ManualWriterMode
  chapterContent: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
  memoryContext: string
}) {
  return [
    {
      role: "system" as const,
      content: `${BASE_WRITER_SYSTEM_PROMPT}\n\n${ITALIAN_EDITORIAL_QUALITY_RULES}`
    },
    {
      role: "user" as const,
      content: [
        `Capitolo target: ${input.title}`,
        `Modalita: ${input.mode}`,
        `Istruzione utente: ${input.instruction || "Scrivi una bozza editoriale migliorata."}`,
        ...renderMemoryPromptSection(input.memoryContext),
        "Knowledge consolidata disponibile:",
        ...input.knowledge.map((item) => `\n### ${item.title}\nPath: ${item.path}\n${item.summary}`),
        "\nGuida operativa canonica del manuale:",
        trimWords(input.structureGuide.replace(/^---[\s\S]*?---/, ""), 1000),
        "\nDesign system editoriale canonico:",
        trimWords(input.designGuide.replace(/^---[\s\S]*?---/, ""), 800),
        "\nCapitolo esistente e struttura editoriale da rispettare:",
        trimWords(input.chapterContent.replace(/^---[\s\S]*?---/, ""), 900),
        "\nProduci testo pronto per un manuale-workbook professionale. Formato obbligatorio: apertura editoriale, obiettivo, mappa BANDO, spiegazione strutturata, box da sapere in 5 righe, caso guidato, domanda da commissario, domanda-trappola, mini-esercizio, errore tipico, riferimenti consolidati, note di review. Integra la richiesta dell'utente e la conoscenza nuova senza cancellare tracciabilita.",
        "\nRegole obbligatorie di italiano editoriale:",
        ITALIAN_EDITORIAL_QUALITY_RULES,
        "Divieto assoluto: non scrivere sezioni meta come 'Aggiornamento generato', 'Istruzione ricevuta', 'Knowledge consolidata', 'questo blocco sviluppa'. Non riassumere le fonti. Scrivi direttamente il capitolo destinato al lettore.",
        "Se il capitolo richiede aggiornamenti web o verifica normativa corrente e le fonti consolidate non bastano, segnala in 'Note di review' quali ricerche web ufficiali servono. Non inventare dati non presenti."
      ].join("\n")
    }
  ]
}

function renderCodexPrompt(input: {
  title: string
  instruction: string
  mode: ManualWriterMode
  chapterContent: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
  memoryContext: string
}, skill: string) {
  return [
    "Sei Manual Writer Agent di ConcorsoBook OS, eseguito tramite Codex CLI locale.",
    "",
    "## Skill di progetto caricata",
    skill || "Skill non trovata: applica comunque le regole di AGENTS.md e del Metodo BANDO.",
    "",
    "Devi generare SOLO il markdown da inserire nel capitolo. Non modificare file, non eseguire comandi, non leggere raw sources.",
    "Usa esclusivamente la knowledge consolidata fornita qui sotto: source notes, topic pages, entity pages.",
    "La knowledge consolidata del wiki e' il cervello obbligatorio del sistema: struttura madre, source notes, topic pages, entity pages, capitoli esistenti e quiz vengono prima di qualsiasi altra cosa.",
    "Scrivi in italiano, stile manuale-workbook professionale per concorsi pubblici, seguendo il Metodo BANDO.",
    ITALIAN_EDITORIAL_QUALITY_RULES,
    "Non devi spiegare che cosa stai facendo. Non devi riassumere il pacchetto conoscenza. Non scrivere 'Aggiornamento generato', 'Istruzione ricevuta', 'Knowledge consolidata', 'questo blocco sviluppa' o formule simili.",
    "Il testo deve sembrare una pagina reale del libro, rivolta direttamente al lettore.",
    "La ricerca web serve solo quando il cervello wiki non basta o quando servono aggiornamenti correnti. Dopo la ricerca, i risultati devono diventare source notes consolidate prima di essere trattati come conoscenza stabile.",
    "Se servono aggiornamenti web, fonti ufficiali o verifica normativa corrente e non sono presenti nel pacchetto conoscenza, aggiungi in 'Note di review' una richiesta puntuale di ricerca web. Non inventare norme, date, soglie o aggiornamenti.",
    "",
    `Capitolo target: ${input.title}`,
    `Modalita: ${input.mode}`,
    `Istruzione utente: ${input.instruction || "Scrivi una bozza editoriale migliorata."}`,
    ...renderMemoryPromptSection(input.memoryContext),
    "",
    "Formato obbligatorio:",
    "- apertura editoriale;",
    "- obiettivo;",
    "- mappa BANDO;",
    "- spiegazione strutturata;",
    "- box da sapere in 5 righe;",
    "- caso guidato;",
    "- domanda da commissario;",
    "- domanda-trappola;",
    "- mini-esercizio;",
    "- errore tipico;",
    "- riferimenti consolidati;",
    "- note di review.",
    "",
    "Knowledge consolidata:",
    ...input.knowledge.map((item) => `\n### ${item.title}\nPath: ${item.path}\n${item.summary}`),
    "",
    "## Guida operativa canonica del manuale",
    trimWords(input.structureGuide.replace(/^---[\s\S]*?---/, ""), 1200),
    "",
    "## Design system editoriale canonico",
    trimWords(input.designGuide.replace(/^---[\s\S]*?---/, ""), 900),
    "",
    "## Capitolo esistente e struttura editoriale da rispettare",
    trimWords(input.chapterContent.replace(/^---[\s\S]*?---/, ""), 1200),
    "",
    "Restituisci solo markdown del capitolo, senza premesse operative e senza testo meta."
  ].join("\n")
}

function renderClaudePrompt(input: {
  title: string
  instruction: string
  mode: ManualWriterMode
  chapterContent: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
  memoryContext: string
}, skill: string) {
  return [
    "Sei Manual Writer Agent di ConcorsoBook OS, eseguito tramite Claude Code locale.",
    "",
    "## Skill di progetto caricata",
    skill || "Skill non trovata: applica comunque le regole di AGENTS.md e del Metodo BANDO.",
    "",
    "Devi generare SOLO il markdown da inserire nel capitolo. Non modificare file, non eseguire comandi, non leggere raw sources.",
    "Usa esclusivamente la knowledge consolidata fornita qui sotto: source notes, topic pages, entity pages.",
    "La knowledge consolidata del wiki e' il cervello obbligatorio del sistema: struttura madre, source notes, topic pages, entity pages, capitoli esistenti e quiz vengono prima di qualsiasi altra cosa.",
    "Scrivi in italiano, stile manuale-workbook professionale per concorsi pubblici, seguendo il Metodo BANDO.",
    ITALIAN_EDITORIAL_QUALITY_RULES,
    "Non devi spiegare che cosa stai facendo. Non devi riassumere il pacchetto conoscenza. Non scrivere 'Aggiornamento generato', 'Istruzione ricevuta', 'Knowledge consolidata', 'questo blocco sviluppa' o formule simili.",
    "Il testo deve sembrare una pagina reale del libro, rivolta direttamente al lettore.",
    "La ricerca web serve solo quando il cervello wiki non basta o quando servono aggiornamenti correnti. Dopo la ricerca, i risultati devono diventare source notes consolidate prima di essere trattati come conoscenza stabile.",
    "Se servono aggiornamenti web, fonti ufficiali o verifica normativa corrente e non sono presenti nel pacchetto conoscenza, aggiungi in 'Note di review' una richiesta puntuale di ricerca web. Non inventare norme, date, soglie o aggiornamenti.",
    "",
    `Capitolo target: ${input.title}`,
    `Modalita: ${input.mode}`,
    `Istruzione utente: ${input.instruction || "Scrivi una bozza editoriale migliorata."}`,
    ...renderMemoryPromptSection(input.memoryContext),
    "",
    "Formato obbligatorio:",
    "- apertura editoriale;",
    "- obiettivo;",
    "- mappa BANDO;",
    "- spiegazione strutturata;",
    "- box da sapere in 5 righe;",
    "- caso guidato;",
    "- domanda da commissario;",
    "- domanda-trappola;",
    "- mini-esercizio;",
    "- errore tipico;",
    "- riferimenti consolidati;",
    "- note di review.",
    "",
    "Knowledge consolidata:",
    ...input.knowledge.map((item) => `\n### ${item.title}\nPath: ${item.path}\n${item.summary}`),
    "",
    "## Guida operativa canonica del manuale",
    trimWords(input.structureGuide.replace(/^---[\s\S]*?---/, ""), 1200),
    "",
    "## Design system editoriale canonico",
    trimWords(input.designGuide.replace(/^---[\s\S]*?---/, ""), 900),
    "",
    "## Capitolo esistente e struttura editoriale da rispettare",
    trimWords(input.chapterContent.replace(/^---[\s\S]*?---/, ""), 1200),
    "",
    "Restituisci solo markdown del capitolo, senza premesse operative e senza testo meta."
  ].join("\n")
}

function renderHumanizerPrompt(input: {
  title: string
  instruction: string
  chapterContent: string
  chapterBody: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
  memoryContext: string
}, writerSkill: string, humanizerSkill: string, runtimeLabel: string) {
  return [
    `Sei Manual Writer Agent di ConcorsoBook OS, eseguito tramite ${runtimeLabel}.`,
    "",
    "## Skill di progetto caricata",
    writerSkill || "Skill writer non trovata: applica comunque AGENTS.md e Metodo BANDO.",
    "",
    "## Skill humanizer caricata",
    humanizerSkill || "Skill humanizer non trovata: applica comunque revisione anti-AI conservativa.",
    "",
    ...renderHumanizerTask(input)
  ].join("\n")
}

function renderHumanizerMessages(input: {
  title: string
  instruction: string
  chapterContent: string
  chapterBody: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
  memoryContext: string
}, humanizerSkill: string) {
  return [
    {
      role: "system" as const,
      content: [
        BASE_WRITER_SYSTEM_PROMPT,
        ITALIAN_EDITORIAL_QUALITY_RULES,
        "Applica revisione humanizer solo se migliora il testo. Conserva significato, struttura, riferimenti e voce professionale del manuale."
      ].join("\n\n")
    },
    {
      role: "user" as const,
      content: [
        "## Skill humanizer caricata",
        trimWords(humanizerSkill, 2400),
        "",
        ...renderHumanizerTask(input)
      ].join("\n")
    }
  ]
}

function renderHumanizerTask(input: {
  title: string
  instruction: string
  chapterContent: string
  chapterBody: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
  memoryContext: string
}) {
  return [
    "## Obiettivo",
    "Applica una revisione editoriale humanizer al capitolo selezionato: elimina segnali di testo generato da AI, riscrivi solo dove serve, rendi il ritmo piu naturale e conserva il taglio da manuale-workbook Metodo BANDO.",
    "",
    "## Vincoli non negoziabili",
    "- Restituisci solo il corpo markdown completo e revisionato del capitolo.",
    "- Non restituire frontmatter YAML.",
    "- Non includere sezioni tipo 'Draft rewrite', 'What makes the below...', 'Final rewrite', audit, spiegazioni o riepiloghi del lavoro svolto.",
    "- Mantieni titolo, gerarchia markdown, tabelle, checklist, callout, immagini, link wiki e riferimenti consolidati.",
    "- Non inventare norme, date, soglie, statistiche, enti o fonti.",
    "- Non cancellare note di review, riferimenti o avvisi di verifica normativa: puoi renderli piu chiari, non eliminarli.",
    "- Non trasformare il manuale in tono personale o colloquiale: niente prima persona se non gia presente nel capitolo.",
    "- Evita enfasi vuota, formule promozionali, triadi meccaniche, frasi meta, passivi inutili, conclusioni generiche e parole gonfiate.",
    "- Se una frase e' gia naturale e precisa, lasciala invariata.",
    "",
    `Capitolo target: ${input.title}`,
    `Istruzione aggiuntiva: ${input.instruction || "Revisione humanizer conservativa del capitolo."}`,
    ...renderMemoryPromptSection(input.memoryContext),
    "",
    "## Knowledge consolidata disponibile",
    ...input.knowledge.map((item) => `\n### ${item.title}\nPath: ${item.path}\n${item.summary}`),
    "",
    "## Guida operativa canonica del manuale",
    trimWords(input.structureGuide.replace(/^---[\s\S]*?---/, ""), 900),
    "",
    "## Design system editoriale canonico",
    trimWords(input.designGuide.replace(/^---[\s\S]*?---/, ""), 650),
    "",
    "## Corpo markdown attuale da revisionare",
    input.chapterBody.trim(),
    "",
    "Restituisci ora solo il corpo markdown completo revisionato."
  ]
}

async function loadProfessionalWriterSkill() {
  const skillPath = path.join(process.cwd(), ".agents", "skills", "concorso-book-professional-writer", "SKILL.md")

  return readFile(skillPath, "utf8").catch(() => "")
}

async function loadHumanizerSkill() {
  const skillPath = path.join(process.cwd(), ".agents", "skills", "humanizer", "SKILL.md")

  return readFile(skillPath, "utf8").catch(() => "")
}

function renderMemoryPromptSection(memoryContext: string) {
  if (!memoryContext) return []

  return [
    "",
    "Memoria operativa locale richiamata:",
    memoryContext,
    "Usa questa memoria solo per continuita di lavoro e preferenze operative; non sostituisce le source notes consolidate."
  ]
}

function renderDeterministicHumanizedRevision(input: {
  title: string
  instruction: string
  chapterBody: string
}) {
  return applyHumanizerCleanup(input.chapterBody)
}

function applyHumanizerCleanup(value: string) {
  return value
    .split(/(```[\s\S]*?```)/g)
    .map((part) => (part.startsWith("```") ? part : cleanupEditorialText(part)))
    .join("")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{4,}/g, "\n\n\n")
    .trim()
}

function cleanupEditorialText(value: string) {
  const replacements: Array<[RegExp, string]> = [
    [/[\u201c\u201d]/g, "\""],
    [/[\u2018\u2019]/g, "'"],
    [/\u2014/g, " - "],
    [/\bIn order to\b/gi, "To"],
    [/\bDue to the fact that\b/gi, "Because"],
    [/\bAt this point in time\b/gi, "Now"],
    [/\bIt is important to note that\s+/gi, ""],
    [/\bE['\u2019]? importante sottolineare che\s+/gi, ""],
    [/\bE['\u2019]? bene ricordare che\s+/gi, ""],
    [/\bIn questo contesto,\s+/gi, ""],
    [/\bIn conclusione,\s+/gi, ""],
    [/\bNel complesso,\s+/gi, ""],
    [/\bserve come\b/gi, "serve da"],
    [/\bsi configura come\b/gi, "e'"],
    [/\bsi pone come\b/gi, "e'"],
    [/\brappresenta un elemento cruciale\b/gi, "conta"],
    [/\brappresenta un elemento fondamentale\b/gi, "conta"],
    [/\bcostituisce un elemento cruciale\b/gi, "conta"],
    [/\bcostituisce un elemento fondamentale\b/gi, "conta"],
    [/\bcruciale\b/gi, "importante"],
    [/\bpivotal\b/gi, "importante"],
    [/\bsignificativo\b/gi, "rilevante"],
    [/\bdi fondamentale importanza\b/gi, "importante"],
    [/\bmettere in evidenza\b/gi, "mostrare"],
    [/\bevidenzia l'importanza di\b/gi, "mostra"],
    [/\bsottolinea l'importanza di\b/gi, "mostra"],
    [/\bnel panorama\b/gi, "nel contesto"],
    [/\btessuto\b/gi, "insieme"],
    [/\bdelve\b/gi, "analizzare"],
    [/\bshowcase\b/gi, "mostrare"],
    [/\bhighlight\b/gi, "mostrare"]
  ]

  let next = value

  for (const [pattern, replacement] of replacements) {
    next = next.replace(pattern, replacement)
  }

  return next
    .replace(/([.!?])\s+Questo capitolo non e' solo\b/gi, "$1 Questo capitolo non e' soltanto")
    .replace(/\s+-\s+/g, " - ")
    .replace(/ {2,}/g, " ")
}

function renderDeterministicDraft(input: {
  title: string
  instruction: string
  mode: ManualWriterMode
  chapterContent: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
  memoryContext: string
}) {
  const primary = input.knowledge.slice(0, 6)
  const references = primary.map((item) => `- [[${item.path.replace(".md", "")}]]`).join("\n")
  const chapterBody = input.chapterContent.replace(/^---[\s\S]*?---/, "")
  const objective = extractSection(input.chapterContent, "Obiettivo didattico") || `Rendere il tema "${input.title}" utilizzabile nello studio e nelle prove.`
  const structureItems = extractBulletItems(extractSection(input.chapterContent, "Specifica struttura madre"))
  const toolItems = extractBulletItems(extractSection(input.chapterContent, "Strumenti da inserire"))
  const note = extractSection(input.chapterContent, "Note editoriali")
  const opening = renderOpening(input.title, objective, structureItems)
  const explanation = renderChapterSpecificExplanation(input.title, structureItems, note)
  const bandoMap = renderBandoMap(input.title, structureItems)
  const toolBlock = toolItems.length > 0 ? renderToolBlock(toolItems) : renderDefaultToolBlock(input.title)
  const caseBlock = renderCaseBlock(input.title)
  const imageNotes = renderImageNotes(input.title)

  const memoryReviewNote = input.memoryContext ? "Memoria locale richiamata e usata solo se pertinente alle istruzioni editoriali." : ""

  return `### Apertura editoriale
${opening}

### Obiettivo del capitolo
${objective}

### Mappa BANDO
${bandoMap}

### Spiegazione
${explanation}

### Da sapere in 5 righe
1. Il candidato efficace non parte dai materiali: parte dal bando e dalle prove.
2. Le materie non hanno tutte lo stesso peso: vanno ordinate per priorità, frequenza e rischio.
3. Quiz, teoria, casi e orale sono output diversi e vanno allenati in modo diverso.
4. Ogni errore deve diventare un dato di lavoro, non una semplice correzione.
5. Il Metodo BANDO serve a riusare ciò che studi, invece di ricominciare da zero a ogni concorso.

### Strumenti operativi
${toolBlock}

### Caso guidato
${caseBlock}

### Domanda da commissario
Perché due candidati che studiano lo stesso numero di ore possono ottenere risultati molto diversi in un concorso pubblico?

Risposta guidata: perché non conta solo la quantità di studio, ma la capacità di leggere il bando, selezionare le priorità, allenare il tipo di prova e correggere gli errori in modo sistematico.

### Domanda-trappola
Per preparare bene un concorso basta comprare il manuale più completo?

Risposta guidata: no. Un manuale completo può aiutare, ma senza metodo rischia di aumentare la dispersione. Prima si capisce il bando, poi si scelgono materiali, priorità e allenamenti.

### Errore tipico
Iniziare dallo studio lineare del primo manuale disponibile, senza sapere quali prove si affronteranno, quali materie pesano di più e quali contenuti possono essere riusati in altri concorsi.

### Mini-esercizio
Prendi un concorso che ti interessa e compila quattro righe:

| Elemento | Risposta |
| --- | --- |
| Profilo richiesto | |
| Prove previste | |
| Tre materie prioritarie | |
| Primo output da allenare | |

### Note layout e immagini
${imageNotes}

### Riferimenti consolidati
${references || "- Nessun riferimento consolidato disponibile."}

### Note di review
- Bozza da revisionare prima della pubblicazione.
- Non sono state lette raw sources direttamente.
- ${memoryReviewNote || "Nessuna memoria locale rilevante richiamata."}
- Applicare design system editoriale 17 x 24 cm con gerarchia manuale-workbook.
- Modalità richiesta: ${input.mode}.
- Lunghezza del capitolo da espandere in seconda revisione se serve maggiore profondità: ${countWords(chapterBody)} parole di struttura disponibili.`
}

function isUsableRevision(value: string, originalBody: string) {
  const candidate = stripRevisionArtifacts(value)
  const originalWords = countWords(originalBody)
  const candidateWords = countWords(candidate)
  const minimumWords = originalWords > 120 ? Math.max(80, Math.floor(originalWords * 0.35)) : Math.max(8, Math.floor(originalWords * 0.25))

  if (!candidate.trim()) return false
  if (looksLikeMetaDraft(candidate)) return false
  if (/what makes the below so obviously ai generated/i.test(candidate)) return false
  if (/now make it not obviously ai generated/i.test(candidate)) return false

  return candidateWords >= minimumWords
}

function sanitizeRevisionBody(value: string, originalBody: string) {
  const candidate = stripRevisionArtifacts(value).trim()

  if (!isUsableRevision(candidate, originalBody)) {
    return applyHumanizerCleanup(originalBody)
  }

  return `${candidate}\n`
}

function stripRevisionArtifacts(value: string) {
  let next = value.trim()
  const finalRewriteMatch = next.match(/(?:^|\n)(?:#{1,4}\s*)?(?:final rewrite|versione finale|riscrittura finale)\s*:?\s*\n/i)

  if (finalRewriteMatch?.index !== undefined) {
    next = next.slice(finalRewriteMatch.index + finalRewriteMatch[0].length).trim()
  }

  next = next
    .replace(/^```(?:markdown|md)?\s*/i, "")
    .replace(/```\s*$/i, "")
    .trim()

  if (next.startsWith("---\n")) {
    const closingIndex = next.indexOf("\n---\n", 4)
    if (closingIndex !== -1) {
      next = next.slice(closingIndex + 5).trim()
    }
  }

  return next
}

function extractMarkdownBody(content: string) {
  const split = splitRawFrontmatter(content)

  return split ? split.body : content.replace(/\r\n/g, "\n")
}

function replaceMarkdownBodyPreservingFrontmatter(content: string, nextBody: string) {
  const split = splitRawFrontmatter(content)
  const body = `${nextBody.trim()}\n`

  if (!split) return body

  return `${split.frontmatter}${body}`
}

function buildRevisionDiff(before: string, after: string): RevisionDiffSummary {
  const beforeLines = normalizeDiffLines(before)
  const afterLines = normalizeDiffLines(after)
  const changes = diffLines(beforeLines, afterLines)
  const previewLines = changes.slice(0, 140)

  return {
    changed: changes.length > 0,
    additions: changes.filter((line) => line.type === "added").length,
    deletions: changes.filter((line) => line.type === "removed").length,
    beforeWordCount: countWords(before),
    afterWordCount: countWords(after),
    previewLines
  }
}

function normalizeDiffLines(value: string) {
  return value.replace(/\r\n/g, "\n").replace(/\s+$/g, "").split("\n")
}

function diffLines(beforeLines: string[], afterLines: string[]): RevisionDiffLine[] {
  const rows = beforeLines.length
  const columns = afterLines.length
  const table: number[][] = Array.from({ length: rows + 1 }, () => Array(columns + 1).fill(0))

  for (let row = rows - 1; row >= 0; row -= 1) {
    for (let column = columns - 1; column >= 0; column -= 1) {
      if (beforeLines[row] === afterLines[column]) {
        table[row][column] = table[row + 1][column + 1] + 1
      } else {
        table[row][column] = Math.max(table[row + 1][column], table[row][column + 1])
      }
    }
  }

  const changes: RevisionDiffLine[] = []
  let row = 0
  let column = 0

  while (row < rows && column < columns) {
    if (beforeLines[row] === afterLines[column]) {
      row += 1
      column += 1
    } else if (table[row + 1][column] >= table[row][column + 1]) {
      changes.push({ type: "removed", lineNumber: row + 1, text: beforeLines[row] })
      row += 1
    } else {
      changes.push({ type: "added", lineNumber: column + 1, text: afterLines[column] })
      column += 1
    }
  }

  while (row < rows) {
    changes.push({ type: "removed", lineNumber: row + 1, text: beforeLines[row] })
    row += 1
  }

  while (column < columns) {
    changes.push({ type: "added", lineNumber: column + 1, text: afterLines[column] })
    column += 1
  }

  return changes.filter((line) => line.text.trim())
}

function patchRawFrontmatter(content: string, patch: Record<string, unknown>) {
  const split = splitRawFrontmatter(content)

  if (!split) return content

  const yaml = split.frontmatter.slice(4, -5)
  const lines = yaml.split("\n")

  for (const [key, value] of Object.entries(patch)) {
    const lineIndex = lines.findIndex((line) => new RegExp(`^${escapeRegExp(key)}\\s*:`).test(line))
    const nextLine = `${key}: ${stringifyInlineYamlValue(value)}`

    if (lineIndex === -1) {
      lines.push(nextLine)
    } else {
      lines[lineIndex] = nextLine
    }
  }

  return `---\n${lines.join("\n")}\n---\n${split.body}`
}

function splitRawFrontmatter(content: string) {
  const normalized = content.replace(/\r\n/g, "\n")

  if (!normalized.startsWith("---\n")) return null

  const closingIndex = normalized.indexOf("\n---\n", 4)

  if (closingIndex === -1) return null

  const frontmatterEnd = closingIndex + 5

  return {
    frontmatter: normalized.slice(0, frontmatterEnd),
    body: normalized.slice(frontmatterEnd)
  }
}

function stringifyInlineYamlValue(value: unknown) {
  if (typeof value === "boolean" || typeof value === "number") return String(value)
  if (value === null) return "null"

  const text = String(value)

  if (text === "" || /[:#\[\]{},"\n]/.test(text) || text !== text.trim()) {
    return JSON.stringify(text)
  }

  return text
}

function escapeRegExp(value: string) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
}

function looksLikeMetaDraft(value: string) {
  const normalized = value.toLowerCase()
  const forbidden = [
    "aggiornamento generato",
    "istruzione ricevuta",
    "knowledge consolidata",
    "questo blocco sviluppa",
    "devo generare",
    "manual writer agent"
  ]

  return forbidden.some((item) => normalized.includes(item))
}

function extractBulletItems(value: string) {
  return value
    .split("\n")
    .map((line) => line.replace(/^\s*[-*]\s+/, "").trim())
    .filter(Boolean)
}

function renderOpening(title: string, objective: string, structureItems: string[]) {
  const normalized = title.toLowerCase()

  if (normalized.includes("perche questo libro")) {
    return [
      "Se stai preparando un concorso pubblico, probabilmente hai già incontrato il problema principale: non mancano i materiali, manca un criterio per usarli. Manuali, quiz, gruppi online, video, schemi e appunti possono diventare utili solo quando entrano in un piano. Senza piano, anche il materiale migliore rischia di trasformarsi in rumore.",
      "",
      "Questo libro nasce per una ragione precisa: aiutarti a preparare concorsi diversi senza ricominciare ogni volta da zero. Non promette scorciatoie e non sostituisce lo studio. Ti insegna invece a leggere il bando, capire che cosa conta, costruire priorità, allenare le prove e trasformare gli errori in indicazioni di lavoro.",
      "",
      "Il punto di partenza è semplice: ciò che studi per un concorso può diventare capitale riutilizzabile. Diritto amministrativo, Costituzione, pubblico impiego, trasparenza, contabilità di base, contratti, logica e metodo non appartengono a un solo bando. Se li studi con ordine, possono accompagnarti da un concorso comunale a un concorso ministeriale, da un profilo amministrativo a un profilo più specialistico."
    ].join("\n")
  }

  if (normalized.includes("nuovo candidato")) {
    return [
      "Il candidato pubblico di oggi non è più soltanto una persona che studia molte pagine. È una persona che sa orientarsi tra bandi, piattaforme digitali, materie trasversali, prove a tempo, quiz, casi pratici e colloqui orali. La differenza non sta solo nella memoria: sta nella capacità di scegliere cosa fare prima, cosa rinviare, cosa allenare e cosa tagliare.",
      "",
      "Molti candidati partono con energia, comprano manuali, scaricano quiz e aprono decine di schede nel browser. Dopo pochi giorni, però, non sanno più se stanno avanzando davvero. Studiano, ma senza una mappa. Ripetono, ma senza sapere quali errori stanno correggendo. Fanno quiz, ma senza capire se il problema è memoria, concetto, distrazione o strategia.",
      "",
      "Il nuovo candidato pubblico deve diventare più strategico. Non perché lo studio conti meno, ma perché il concorso misura anche metodo, lucidità, gestione del tempo e capacità di produrre una risposta adeguata alla prova."
    ].join("\n")
  }

  const focus = structureItems.slice(0, 3).join(", ").toLowerCase()

  return `Questo capitolo affronta "${title}" con un taglio operativo. L'obiettivo non è accumulare nozioni, ma trasformare il tema in uno strumento di preparazione: capire che cosa richiede il bando, selezionare i nuclei utili e allenare l'output che la prova chiederà davvero.${focus ? ` In particolare, il capitolo lavora su: ${focus}.` : ""}\n\n${objective}`
}

function renderBandoMap(title: string, structureItems: string[]) {
  const normalized = title.toLowerCase()

  if (normalized.includes("perche questo libro")) {
    return [
      "- **Bando**: ogni percorso parte dal documento ufficiale, non dai materiali acquistati a caso.",
      "- **Aree**: le materie vengono divise tra nucleo comune, contenuti specifici e moduli integrativi.",
      "- **Nuclei**: si studiano prima i concetti ad alta probabilità e ad alto riuso.",
      "- **Diario**: errori, ripassi e simulazioni diventano dati di lavoro.",
      "- **Output**: ogni capitolo deve portare a un risultato concreto: risposta, caso, quiz, schema, checklist o piano."
    ].join("\n")
  }

  if (normalized.includes("nuovo candidato")) {
    return [
      "- **Bando**: il candidato strategico legge requisiti, profilo, prove, materie, punteggi e scadenze prima di scegliere i materiali.",
      "- **Aree**: distingue concorsi comunali, ministeriali, fiscali, sanitari, tecnici, scolastici o di polizia locale senza confonderli in un unico programma indistinto.",
      "- **Nuclei**: individua ciò che ricorre spesso: metodo, Costituzione, amministrativo, pubblico impiego, trasparenza, quiz, casi e orale.",
      "- **Diario**: registra errori e debolezze per non ripetere sempre lo stesso tipo di studio.",
      "- **Output**: si allena sulla forma della prova: quiz a tempo, risposta sintetica, caso pratico, esposizione orale o quesito situazionale."
    ].join("\n")
  }

  const items = structureItems.slice(0, 5)

  return [
    `- **Bando**: capire dove "${title}" compare nel programma e con quale peso.`,
    `- **Aree**: collegare il tema alle materie vicine e ai profili concorsuali.`,
    `- **Nuclei**: selezionare i punti più probabili: ${items.length ? items.join("; ").toLowerCase() : "definizioni, funzioni, casi e rischi d'errore"}.`,
    "- **Diario**: trasformare dubbi ed errori in ripasso programmato.",
    "- **Output**: produrre una risposta, uno schema, un caso o una checklist."
  ].join("\n")
}

function renderChapterSpecificExplanation(title: string, structureItems: string[], note: string) {
  const normalized = title.toLowerCase()

  if (normalized.includes("perche questo libro")) {
    return [
      "La maggior parte dei candidati non fallisce perché non studia. Fallisce perché studia senza gerarchia. Apre un manuale, segue l'ordine delle pagine, prova qualche quiz, poi cambia concorso e ha l'impressione di dover ripartire da capo. Questo meccanismo produce fatica, dispersione e sfiducia.",
      "",
      "Il Metodo BANDO rovescia l'ordine. Prima viene il bando: cosa chiede davvero l'ente, quali prove sono previste, quali materie sono centrali, quali sono accessorie, quali contenuti possono essere lasciati a un modulo successivo. Dopo vengono le aree, cioè la divisione tra ciò che serve sempre e ciò che serve solo per quel profilo. Poi arrivano i nuclei, cioè i concetti che hanno più probabilità di tornare nelle prove.",
      "",
      "Il diario serve a non studiare al buio. Ogni errore in un quiz, in una risposta scritta o in una simulazione orale deve indicare un'azione: ripassare un concetto, correggere una definizione, allenare il tempo, migliorare l'esposizione, cambiare strategia. L'output è la parte finale: non basta leggere, bisogna produrre qualcosa di simile alla prova.",
      "",
      "Per questo il libro è completo anche su carta. Il digitale può accelerare alcune operazioni, come compilare una griglia o recuperare aggiornamenti, ma non deve essere indispensabile. Se hai solo il libro, devi poter leggere, sottolineare, compilare, pianificare e allenarti comunque."
    ].join("\n")
  }

  if (normalized.includes("nuovo candidato")) {
    return [
      "I concorsi pubblici sono diventati più vari e più selettivi nella forma. Alcuni prevedono una prova preselettiva a quiz, altri una prova scritta unica, altri ancora casi pratici, prove digitali, valutazione dei titoli o colloqui orali. In molti bandi le materie comuni si ripetono, ma cambiano il peso, il livello richiesto e il tipo di prova.",
      "",
      "Il candidato principiante tende a cercare sicurezza nella quantità: più manuali, più corsi, più quiz, più file. Il candidato strategico cerca prima la struttura: quale profilo sto preparando, quale prova devo affrontare, quali materie sono centrali, quali contenuti sono solo eventuali, quanto tempo ho e come misuro il miglioramento.",
      "",
      "Un concorso comunale, un concorso ministeriale, un concorso in un'agenzia fiscale, un profilo amministrativo sanitario o un concorso per polizia locale non richiedono la stessa profondità sulle stesse materie. Alcune basi restano comuni, ma il modo di usarle cambia. Il valore del metodo è proprio questo: costruire un nucleo che resta e poi aggiungere solo ciò che serve.",
      "",
      "Il nuovo candidato pubblico deve quindi imparare tre gesti: leggere il bando prima di studiare, distinguere materie centrali e accessorie, allenarsi sulle prove reali. Senza questi tre passaggi, anche molte ore di studio possono produrre un risultato fragile."
    ].join("\n")
  }

  const items = structureItems.length
    ? structureItems.map((item) => `- ${item}`).join("\n")
    : "- Individuare il tema nel bando.\n- Collegarlo alle prove.\n- Trasformarlo in esercizio e ripasso."

  return [
    `Il capitolo deve rendere operativo il tema "${title}". La spiegazione principale va costruita intorno ai punti previsti dalla struttura madre:`,
    "",
    items,
    "",
    note ? `Nota editoriale da rispettare: ${note}` : "Il testo deve restare orientato al candidato e non trasformarsi in trattazione enciclopedica."
  ].join("\n")
}

function renderToolBlock(toolItems: string[]) {
  return toolItems.map((item) => `- ${item}`).join("\n")
}

function renderDefaultToolBlock(title: string) {
  return [
    `- Scheda rapida: "${title} in una pagina".`,
    "- Mini-checklist: che cosa devo sapere, che cosa devo saper fare, che errore devo evitare.",
    "- Spazio diario: una riga per registrare il primo errore collegato al tema."
  ].join("\n")
}

function renderCaseBlock(title: string) {
  const normalized = title.toLowerCase()

  if (normalized.includes("perche questo libro")) {
    return "Anna prepara un concorso comunale e compra tre manuali. Dopo due settimane ha letto molte pagine, ma non sa quali materie pesano di più. Con il Metodo BANDO riparte dal bando: individua prove, materie, scadenza e soglia; separa nucleo comune e contenuti specifici; decide quali quiz fare subito e quali rimandare. Il suo studio diventa un piano, non una raccolta di tentativi."
  }

  if (normalized.includes("nuovo candidato")) {
    return "Marco vuole partecipare a due concorsi: uno per istruttore amministrativo comunale e uno per assistente in un ente centrale. Il candidato principiante comprerebbe due percorsi separati. Il candidato strategico individua prima il nucleo comune, poi aggiunge le differenze: enti locali per il primo, organizzazione ministeriale e profilo specifico per il secondo. In questo modo non raddoppia lo studio: lo organizza."
  }

  return `Un candidato incontra il tema "${title}" nel programma d'esame. Prima lo collega al bando, poi seleziona i nuclei da studiare, infine produce uno schema di risposta e un mini-caso per verificare se lo sa usare davvero.`
}

function renderImageNotes(title: string) {
  const normalized = title.toLowerCase()

  if (normalized.includes("perche questo libro")) {
    return [
      "- Inserire uno schema semplice: \"Materiali sparsi\" -> \"Metodo BANDO\" -> \"Piano riutilizzabile\".",
      "- Valutare una pagina visuale con le cinque lettere BANDO e una frase funzione per ciascuna."
    ].join("\n")
  }

  if (normalized.includes("nuovo candidato")) {
    return [
      "- Inserire tabella comparativa: candidato principiante vs candidato strategico.",
      "- Inserire mini-test visuale \"Che tipo di candidato sei?\" con punteggio."
    ].join("\n")
  }

  return "- Inserire solo immagini funzionali: schema, tabella, flowchart o griglia compilabile collegata al capitolo."
}

function extractUsefulSummary(content: string) {
  const summary = extractSection(content, "Sintesi")
  const notes = extractSection(content, "Note editoriali")
  const review = extractSection(content, "Stato revisione")
  const combined = [summary, notes, review].filter(Boolean).join("\n\n")

  return trimWords(combined || content.replace(/^---[\s\S]*?---/, ""), 180)
}

function extractSection(content: string, heading: string) {
  const lines = content.replace(/\r\n/g, "\n").split("\n")
  const target = `## ${heading.toLowerCase()}`
  const start = lines.findIndex((line) => line.trim().toLowerCase() === target)

  if (start === -1) return ""

  let end = lines.length

  for (let index = start + 1; index < lines.length; index += 1) {
    if (/^#{1,2}\s+/.test(lines[index])) {
      end = index
      break
    }
  }

  return lines.slice(start + 1, end).join("\n").trim()
}

function firstSentence(value: string) {
  return trimWords(value.split(/(?<=[.!?])\s+/)[0] || value, 34)
}

function trimWords(value: string, limit: number) {
  const words = value.replace(/\s+/g, " ").trim().split(" ").filter(Boolean)

  if (words.length <= limit) return words.join(" ")

  return `${words.slice(0, limit).join(" ")}...`
}

function countWords(value: string) {
  return value.split(/\s+/).filter(Boolean).length
}

function bookIdFromChapterPath(chapterPath: string) {
  const normalized = chapterPath.replace(/\\/g, "/")
  const match = normalized.match(/^books\/(.+)\/chapters\/[^/]+\.md$/)

  return match?.[1] || ""
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map(String) : []
}

function dedupeByPath(items: KnowledgeItem[]) {
  const seen = new Set<string>()
  return items.filter((item) => {
    if (seen.has(item.path)) return false
    seen.add(item.path)
    return true
  })
}

function compareChapters(left: ChapterOption, right: ChapterOption) {
  if (left.bookId !== right.bookId) return left.bookId.localeCompare(right.bookId)

  return outlineRank(left.outlineSection) - outlineRank(right.outlineSection) || left.title.localeCompare(right.title)
}

function outlineRank(value: string) {
  if (!value) return 999
  if (/^\d+$/.test(value)) return Number(value)
  if (/^[A-Z]$/i.test(value)) return 100 + value.toUpperCase().charCodeAt(0) - 64

  return 900
}
