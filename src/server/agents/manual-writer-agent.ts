import { getOpenAiConfig, getWriterConfig } from "../config"
import { completeWithCodexCli } from "../llm/codex-cli-adapter"
import { OpenAiLlmClient } from "../llm/openai-adapter"
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
}

export interface ManualWriterResult {
  status: "completed"
  chapterPath: string
  changedFiles: string[]
  knowledgeUsed: string[]
  draft: string
  writerProvider: "codex" | "openai" | "local"
  warnings: string[]
}

interface KnowledgeItem {
  path: string
  title: string
  summary: string
}

export class ManualWriterAgent {
  constructor(private readonly store: FileWikiStore) {}

  async listChapters(): Promise<ChapterOption[]> {
    const files = await this.store.listMarkdown("books")
    const chapters: ChapterOption[] = []

    for (const file of files.filter((item) => item.includes("/chapters/"))) {
      const content = await this.store.readText(file)
      const parsed = parseFrontmatter(content)

      chapters.push({
        path: file,
        title: String(parsed.data.title || file),
        bookId: String(parsed.data.book_id || file.split("/")[1] || "unknown"),
        outlineSection: String(parsed.data.outline_section || ""),
        status: String(parsed.data.status || "draft"),
        reviewRequired: Boolean(parsed.data.review_required)
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
    const generation = await this.generateDraft({
      title: String(chapter.data.title || input.chapterPath),
      instruction: input.instruction,
      mode: input.mode,
      chapterContent,
      structureGuide,
      knowledge
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
      `\n- ${now} | manual_writer | ${input.chapterPath} | mode=${input.mode} | target_heading=${targetHeading} | knowledge=${knowledge.length}`
    )

    return {
      status: "completed",
      chapterPath: input.chapterPath,
      changedFiles: [input.chapterPath, "log.md"],
      knowledgeUsed: knowledge.map((item) => item.path),
      draft,
      writerProvider: generation.provider,
      warnings: generation.warnings
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
    if (!chapterPath.startsWith("books/il-metodo-bando/")) return ""

    const path = "books/il-metodo-bando/struttura-madre.md"
    if (!(await this.store.exists(path))) return ""

    return this.store.readText(path)
  }

  private async generateDraft(input: {
    title: string
    instruction: string
    mode: ManualWriterMode
    chapterContent: string
    structureGuide: string
    knowledge: KnowledgeItem[]
  }) {
    const writerConfig = getWriterConfig()

    if (writerConfig.provider === "codex") {
      try {
        const skill = await loadProfessionalWriterSkill()
        const response = await completeWithCodexCli(renderCodexPrompt(input, skill))
        const text = response.text.trim()

        if (text) {
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

    if (writerConfig.provider === "local") {
      return {
        text: renderDeterministicDraft(input),
        provider: "local" as const,
        warnings: []
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
        content:
          "Sei Manual Writer Agent di ConcorsoBook OS. Scrivi manuali e libri operativi per concorsi pubblici. Usa solo knowledge consolidata fornita: source notes, topic pages, entity pages. Non citare o usare raw sources direttamente. Scrivi in italiano, stile workbook professionale, chiaro e didattico."
      },
      {
        role: "user",
        content: [
          `Capitolo target: ${input.title}`,
          `Modalita: ${input.mode}`,
          `Istruzione utente: ${input.instruction || "Scrivi una bozza editoriale migliorata."}`,
          "Knowledge consolidata disponibile:",
          ...input.knowledge.map((item) => `\n### ${item.title}\nPath: ${item.path}\n${item.summary}`),
          "\nGuida operativa canonica del manuale:",
          trimWords(input.structureGuide.replace(/^---[\s\S]*?---/, ""), 1000),
          "\nCapitolo esistente e struttura editoriale da rispettare:",
          trimWords(input.chapterContent.replace(/^---[\s\S]*?---/, ""), 900),
          "\nProduci testo pronto per un manuale-workbook professionale. Formato obbligatorio: apertura editoriale, obiettivo, mappa BANDO, spiegazione strutturata, box da sapere in 5 righe, caso guidato, domanda da commissario, domanda-trappola, mini-esercizio, errore tipico, riferimenti consolidati, note di review. Integra la richiesta dell'utente e la conoscenza nuova senza cancellare tracciabilità."
        ].join("\n")
      }
    ])

    return {
      text: response.trim() || renderDeterministicDraft(input),
      provider: response.trim() ? ("openai" as const) : ("local" as const),
      warnings: response.trim() ? [] : ["Risposta OpenAI vuota: usata bozza locale strutturata."]
    }
  }
}

function renderCodexPrompt(input: {
  title: string
  instruction: string
  mode: ManualWriterMode
  chapterContent: string
  structureGuide: string
  knowledge: KnowledgeItem[]
}, skill: string) {
  return [
    "Sei Manual Writer Agent di ConcorsoBook OS, eseguito tramite Codex CLI locale.",
    "",
    "## Skill di progetto caricata",
    skill || "Skill non trovata: applica comunque le regole di AGENTS.md e del Metodo BANDO.",
    "",
    "Devi generare SOLO il markdown da inserire nel capitolo. Non modificare file, non eseguire comandi, non leggere raw sources.",
    "Usa esclusivamente la knowledge consolidata fornita qui sotto: source notes, topic pages, entity pages.",
    "Scrivi in italiano, stile manuale-workbook professionale per concorsi pubblici, seguendo il Metodo BANDO.",
    "",
    `Capitolo target: ${input.title}`,
    `Modalita: ${input.mode}`,
    `Istruzione utente: ${input.instruction || "Scrivi una bozza editoriale migliorata."}`,
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
    "## Capitolo esistente e struttura editoriale da rispettare",
    trimWords(input.chapterContent.replace(/^---[\s\S]*?---/, ""), 1200),
    "",
    "Restituisci solo markdown del capitolo, senza premesse operative."
  ].join("\n")
}

async function loadProfessionalWriterSkill() {
  const skillPath = path.join(process.cwd(), ".agents", "skills", "concorso-book-professional-writer", "SKILL.md")

  return readFile(skillPath, "utf8").catch(() => "")
}

function renderDeterministicDraft(input: {
  title: string
  instruction: string
  mode: ManualWriterMode
  chapterContent: string
  structureGuide: string
  knowledge: KnowledgeItem[]
}) {
  const primary = input.knowledge.slice(0, 6)
  const references = primary.map((item) => `- [[${item.path.replace(".md", "")}]]`).join("\n")
  const bullets = primary
    .map((item) => `- ${item.title}: ${firstSentence(item.summary)}`)
    .join("\n")

  return `Aggiornamento generato da Manual Writer Agent.

### Istruzione ricevuta
${input.instruction || "Scrivere una bozza editoriale usando la conoscenza consolidata."}

### Apertura editoriale
Questo blocco sviluppa il capitolo "${input.title}" in stile Metodo BANDO: non come trattazione enciclopedica, ma come unità operativa che aiuta il candidato a capire, ricordare e usare il tema in prova. La scrittura deve restare autonoma su carta e potenziabile dal digitale solo come supporto.

### Obiettivo del blocco
Trasformare la conoscenza consolidata in testo da manuale: chiaro, progressivo, utilizzabile per studio, ripasso, prova scritta e orale.

### Mappa BANDO
- **Bando**: individuare come il tema compare nelle materie e nelle prove.
- **Aree**: collegare il tema alle aree comuni e specifiche.
- **Nuclei**: selezionare i concetti ad alta probabilità.
- **Diario**: trasformare il tema in ripassi e controllo errori.
- **Output**: produrre risposta, caso, domanda orale o mini-esercizio.

### Spiegazione
${bullets || "- Knowledge consolidata insufficiente: aggiungere source notes e topic pages prima di consolidare il capitolo."}

### Da sapere in 5 righe
1. Parti dal concetto centrale e collegalo alla funzione pratica.
2. Distingui definizione, norma, effetto operativo e caso d'esame.
3. Usa esempi di ufficio pubblico, non solo formule astratte.
4. Evidenzia rischi, errori frequenti e parole chiave.
5. Chiudi sempre con un output: quiz, risposta orale, mini-caso o checklist.

### Caso guidato
Un candidato legge un bando che richiede conoscenza del tema trattato nel capitolo. Deve trasformare il contenuto in tre output: mappa dei nuclei, risposta sintetica da prova scritta e spiegazione orale con esempio.

### Domanda da commissario
Spiega il tema collegando definizione, funzione, riferimento essenziale e ricaduta pratica nell'organizzazione amministrativa.

### Domanda-trappola
Questo argomento va studiato come definizione da memorizzare?

Risposta guidata: no. Nel Metodo BANDO il tema deve diventare uno strumento: definizione, funzione, collegamento normativo, caso pratico e controllo dell'errore.

### Errore tipico
Scrivere una risposta corretta ma generica, senza mostrare perché il concetto serve nella pratica amministrativa o nella prova concorsuale.

### Mini-esercizio
Compila una tabella con tre colonne: concetto, applicazione pratica, rischio di errore. Usa almeno un riferimento consolidato tra quelli sotto.

### Riferimenti consolidati
${references || "- Nessun riferimento consolidato disponibile."}

### Note di review
- Bozza da revisionare prima della pubblicazione.
- Non sono state lette raw sources direttamente.
- Modalità richiesta: ${input.mode}.`
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
