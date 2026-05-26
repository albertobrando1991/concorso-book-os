import { getHermesConfig, getOpenAiConfig, getWriterConfig, type WriterProvider } from "../config"
import { completeWithClaudeCode } from "../llm/claude-code-adapter"
import { completeWithCodexCli } from "../llm/codex-cli-adapter"
import { HermesLlmClient } from "../llm/hermes-adapter"
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
  provider?: WriterProvider
}

export interface ManualWriterResult {
  status: "completed"
  chapterPath: string
  changedFiles: string[]
  knowledgeUsed: string[]
  draft: string
  writerProvider: "codex" | "claude" | "openai" | "hermes" | "local"
  warnings: string[]
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
    const designGuide = await this.loadDesignGuide(input.chapterPath)
    const generation = await this.generateDraft({
      title: String(chapter.data.title || input.chapterPath),
      instruction: input.instruction,
      mode: input.mode,
      provider: input.provider,
      chapterContent,
      structureGuide,
      designGuide,
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

  private async loadDesignGuide(chapterPath: string) {
    if (!chapterPath.startsWith("books/il-metodo-bando/")) return ""

    const path = "books/il-metodo-bando/design-system-editoriale.md"
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
}

function renderManualWriterMessages(input: {
  title: string
  instruction: string
  mode: ManualWriterMode
  chapterContent: string
  structureGuide: string
  designGuide: string
  knowledge: KnowledgeItem[]
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
  designGuide: string
  knowledge: KnowledgeItem[]
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
- Applicare design system editoriale 17 x 24 cm con gerarchia manuale-workbook.
- Modalità richiesta: ${input.mode}.
- Lunghezza del capitolo da espandere in seconda revisione se serve maggiore profondità: ${countWords(chapterBody)} parole di struttura disponibili.`
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
