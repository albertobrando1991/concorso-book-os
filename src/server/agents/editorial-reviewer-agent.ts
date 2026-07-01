import { readFile } from "node:fs/promises"
import path from "node:path"
import {
  getHermesConfig,
  getKimiConfig,
  getOpenAiConfig,
  getWriterConfig,
  type WriterProvider
} from "../config"
import { completeWithClaudeCode } from "../llm/claude-code-adapter"
import { completeWithCodexCli } from "../llm/codex-cli-adapter"
import { HermesLlmClient } from "../llm/hermes-adapter"
import { OpenAiLlmClient } from "../llm/openai-adapter"
import { LocalAgentMemory } from "../memory/local-agent-memory"
import { FileWikiStore } from "../wiki/file-store"
import { parseFrontmatter } from "../wiki/frontmatter"

// ── Types ──────────────────────────────────────────────────────────────────────

export type ReviewScope = "full" | "chapter" | "aspect"

export type PublishabilityJudgment = "publishable_minor" | "publishable_medium" | "not_publishable"

export interface EditorialReviewInput {
  bookId: string
  scope: ReviewScope
  chapterPath?: string
  aspect?: string
  provider?: WriterProvider
}

export interface ReviewErrorRow {
  id: string
  position: string
  category: string
  severity: "grave" | "media" | "lieve"
  description: string
  proposedFix: string
  status: string
}

export interface ChapterObservation {
  chapter: string
  strengths: string
  issues: string
}

export interface EditorialReviewResult {
  status: "completed"
  bookId: string
  scope: ReviewScope
  provider: WriterProvider
  editorialSummary: string
  errorTable: ReviewErrorRow[]
  publishabilityJudgment: PublishabilityJudgment
  publishabilityReason: string
  chapterObservations: ChapterObservation[]
  verificationItems: string[]
  optionalSuggestions: string[]
  priorityOrder: string[]
  limitations: string[]
  warnings: string[]
  rawReport: string
}

// ── Agent ──────────────────────────────────────────────────────────────────────

export class EditorialReviewerAgent {
  constructor(private readonly store: FileWikiStore) {}

  async runReview(input: EditorialReviewInput): Promise<EditorialReviewResult> {
    const [skillText, checklistText, templateText] = await Promise.all([
      loadSkillFile("SKILL.md"),
      loadSkillFile("references/checklist-30-punti.md"),
      loadSkillFile("references/template-report.md")
    ])

    const chapterContents = await this.loadChapterContents(input)
    if (chapterContents.length === 0) {
      throw new Error("Nessun capitolo trovato per il libro o il perimetro richiesto.")
    }

    const memory = LocalAgentMemory.fromConfig()
    const memoryRecall = await memory.recall({
      scope: "editorial-reviewer",
      query: [
        `Revisione editoriale libro ${input.bookId}`,
        `scope=${input.scope}`,
        input.chapterPath || "",
        input.aspect || ""
      ].join("\n")
    })

    const prompt = buildReviewPrompt({
      skillText,
      checklistText,
      templateText,
      chapterContents,
      scope: input.scope,
      aspect: input.aspect,
      memoryContext: memoryRecall.context
    })

    const writerConfig = getWriterConfig()
    const provider = input.provider || writerConfig.provider
    const generation = await this.callProvider(provider, prompt)

    const parsed = parseReviewResponse(generation.text)
    const now = new Date().toISOString()

    // Save review report to wiki/reviews/
    const reviewPath = `reviews/editorial-review-${input.bookId}-${now.replace(/[:.]/g, "-")}.md`
    const reportContent = [
      "---",
      `id: review-editorial-${input.bookId}-${Date.now()}`,
      "type: review",
      `title: "Revisione editoriale - ${input.bookId}"`,
      `status: completed`,
      "issue_type: editorial_review",
      `severity: ${parsed.publishabilityJudgment === "not_publishable" ? "high" : parsed.publishabilityJudgment === "publishable_medium" ? "medium" : "low"}`,
      `affected_pages: []`,
      `created_at: ${now}`,
      `updated_at: ${now}`,
      `review_required: false`,
      `canonical: true`,
      "tags: [revisione-editoriale, pubblicabilita]",
      "---",
      "",
      generation.text
    ].join("\n")

    await this.store.writeText(reviewPath, reportContent).catch(() => undefined)
    await this.store.appendText(
      "log.md",
      `\n- ${now} | editorial_review | ${input.bookId} | scope=${input.scope} | provider=${generation.provider} | chapters=${chapterContents.length} | judgment=${parsed.publishabilityJudgment}`
    ).catch(() => undefined)

    await memory.captureConversation({
      scope: "editorial-reviewer",
      route: "EditorialReviewerAgent.runReview",
      messages: [
        {
          role: "user",
          content: `bookId=${input.bookId}\nscope=${input.scope}\naspect=${input.aspect || "full"}`
        }
      ],
      reply: [
        `Revisione editoriale completata su ${input.bookId}.`,
        `Giudizio: ${parsed.publishabilityJudgment}.`,
        `Errori trovati: ${parsed.errorTable.length}.`,
        `Provider: ${generation.provider}.`
      ].join("\n"),
      metadata: {
        bookId: input.bookId,
        scope: input.scope,
        provider: generation.provider,
        judgment: parsed.publishabilityJudgment,
        errorCount: parsed.errorTable.length
      }
    }).catch(() => undefined)

    return {
      status: "completed",
      bookId: input.bookId,
      scope: input.scope,
      provider: generation.provider,
      ...parsed,
      warnings: generation.warnings,
      rawReport: generation.text
    }
  }

  // ── Chapter loading ────────────────────────────────────────────────────────

  private async loadChapterContents(input: EditorialReviewInput) {
    const files = await this.store.listMarkdown("books")
    const chapterFiles = files.filter((file) => file.includes("/chapters/"))
    const results: Array<{ path: string; title: string; body: string }> = []

    for (const file of chapterFiles) {
      const bookId = bookIdFromPath(file)
      if (bookId !== input.bookId) continue
      if (input.scope === "chapter" && input.chapterPath && file !== input.chapterPath) continue

      const content = await this.store.readText(file)
      const parsed = parseFrontmatter(content)
      const title = String(parsed.data.title || file)
      const body = content.replace(/^---[\s\S]*?---/, "").trim()

      results.push({ path: file, title, body })
    }

    return results.sort((a, b) => a.path.localeCompare(b.path))
  }

  // ── Provider dispatch ──────────────────────────────────────────────────────

  private async callProvider(provider: WriterProvider, prompt: string) {
    if (provider === "codex") {
      try {
        const response = await completeWithCodexCli(prompt)
        if (response.text.trim()) {
          return {
            text: response.text.trim(),
            provider: "codex" as const,
            warnings: response.stderr.trim() ? [`Codex CLI stderr: ${response.stderr.slice(0, 200)}`] : []
          }
        }
      } catch (error) {
        return {
          text: buildLocalFallbackReport(),
          provider: "local" as const,
          warnings: [`Codex CLI non disponibile: ${error instanceof Error ? error.message : "errore sconosciuto"}`]
        }
      }
    }

    if (provider === "claude") {
      try {
        const response = await completeWithClaudeCode(prompt)
        if (response.text.trim()) {
          return {
            text: response.text.trim(),
            provider: "claude" as const,
            warnings: response.stderr.trim() ? [`Claude Code stderr: ${response.stderr.slice(0, 200)}`] : []
          }
        }
      } catch (error) {
        return {
          text: buildLocalFallbackReport(),
          provider: "local" as const,
          warnings: [`Claude Code non disponibile: ${error instanceof Error ? error.message : "errore sconosciuto"}`]
        }
      }
    }

    if (provider === "hermes") {
      const config = getHermesConfig()
      if (!config.apiKey) {
        return { text: buildLocalFallbackReport(), provider: "local" as const, warnings: ["HERMES_API_KEY non configurata."] }
      }
      const llm = new HermesLlmClient()
      const response = await llm.complete([
        { role: "system", content: REVIEWER_SYSTEM_PROMPT },
        { role: "user", content: prompt }
      ])
      return { text: response.trim() || buildLocalFallbackReport(), provider: response.trim() ? "hermes" as const : "local" as const, warnings: [] }
    }

    if (provider === "kimi") {
      const config = getKimiConfig()
      if (!config.apiKey) {
        return { text: buildLocalFallbackReport(), provider: "local" as const, warnings: ["KIMI_API_KEY non configurata."] }
      }
      const llm = new OpenAiLlmClient({ apiKey: config.apiKey, baseURL: config.baseUrl, model: config.model })
      const response = await llm.complete([
        { role: "system", content: REVIEWER_SYSTEM_PROMPT },
        { role: "user", content: prompt }
      ])
      return { text: response.trim() || buildLocalFallbackReport(), provider: response.trim() ? "kimi" as const : "local" as const, warnings: [] }
    }

    if (provider === "openai") {
      const config = getOpenAiConfig()
      if (!config.apiKey) {
        return { text: buildLocalFallbackReport(), provider: "local" as const, warnings: ["OPENAI_API_KEY non configurata."] }
      }
      const llm = new OpenAiLlmClient()
      const response = await llm.complete([
        { role: "system", content: REVIEWER_SYSTEM_PROMPT },
        { role: "user", content: prompt }
      ])
      return { text: response.trim() || buildLocalFallbackReport(), provider: response.trim() ? "openai" as const : "local" as const, warnings: [] }
    }

    // local fallback
    return { text: buildLocalFallbackReport(), provider: "local" as const, warnings: [] }
  }
}

// ── Prompt building ────────────────────────────────────────────────────────────

const REVIEWER_SYSTEM_PROMPT = [
  "Sei il Revisore Editoriale Totale di ConcorsoBook OS.",
  "Agisci come un team editoriale completo: capo-redattore, copy editor, editor di sviluppo, revisore contenutistico, correttore di bozze e responsabile di produzione editoriale.",
  "Produci sempre il risultato nel formato strutturato del template-report fornito.",
  "Non riscrivere il testo al posto dell'autore: segnala, spiega il motivo, proponi una correzione concreta.",
  "Scrivi in italiano."
].join(" ")

function buildReviewPrompt(input: {
  skillText: string
  checklistText: string
  templateText: string
  chapterContents: Array<{ path: string; title: string; body: string }>
  scope: ReviewScope
  aspect?: string
  memoryContext: string
}) {
  const chapterSection = input.chapterContents.map((chapter) => [
    `\n### Capitolo: ${chapter.title}`,
    `Path: ${chapter.path}`,
    trimWords(chapter.body, 1800)
  ].join("\n")).join("\n\n")

  const scopeLabel = input.scope === "full"
    ? "Revisione completa dell'intero libro"
    : input.scope === "chapter"
      ? "Revisione del singolo capitolo selezionato"
      : `Revisione aspetto specifico: ${input.aspect || "non specificato"}`

  const memorySection = input.memoryContext
    ? `\n## Memoria operativa richiamata\n${input.memoryContext}\n`
    : ""

  return [
    "## Skill: Revisore Editoriale Totale",
    trimWords(input.skillText, 3000),
    "",
    "## Checklist a 30 punti",
    input.checklistText,
    "",
    "## Template di report (formato obbligatorio)",
    input.templateText,
    "",
    `## Perimetro: ${scopeLabel}`,
    memorySection,
    "## Capitoli da revisionare",
    chapterSection,
    "",
    "## Istruzioni finali",
    "Produci ora il report editoriale completo seguendo esattamente il template fornito.",
    "La tabella errori deve usare il formato markdown con colonne: ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato.",
    "Ordina gli errori per gravita decrescente poi per posizione.",
    "Alla fine esprimi il giudizio di pubblicabilita con una delle tre formule esatte:",
    "- 'Pubblicabile con correzioni minori'",
    "- 'Pubblicabile dopo intervento medio'",
    "- 'Non pubblicabile allo stato attuale'",
    "Motiva il giudizio con riferimento alla tabella errori."
  ].join("\n")
}

// ── Response parsing ───────────────────────────────────────────────────────────

function parseReviewResponse(raw: string): Omit<EditorialReviewResult, "status" | "bookId" | "scope" | "provider" | "warnings" | "rawReport"> {
  const editorialSummary = extractReportSection(raw, "1. Sintesi editoriale") || extractReportSection(raw, "Sintesi editoriale") || "Revisione completata."
  const errorTableRaw = extractReportSection(raw, "3. Tabella errori") || extractReportSection(raw, "Tabella errori") || ""
  const errorTable = parseErrorTable(errorTableRaw)
  const judgment = detectJudgment(raw)
  const publishabilityReason = extractReportSection(raw, "9. Giudizio di pubblicabilita") || extractReportSection(raw, "Giudizio di pubblicabilita") || ""
  const chapterObservations = parseChapterObservations(raw)
  const verificationItems = parseBulletSection(extractReportSection(raw, "6. Contenuto da verificare") || extractReportSection(raw, "Contenuto da verificare") || "")
  const optionalSuggestions = parseBulletSection(extractReportSection(raw, "7. Suggerimenti facoltativi") || extractReportSection(raw, "Suggerimenti facoltativi") || "")
  const priorityOrder = parseBulletSection(extractReportSection(raw, "8. Priorita degli interventi") || extractReportSection(raw, "Priorita degli interventi") || "")
  const limitations = parseBulletSection(extractReportSection(raw, "10. Limiti di questa revisione") || extractReportSection(raw, "Limiti di questa revisione") || "")

  return {
    editorialSummary,
    errorTable,
    publishabilityJudgment: judgment,
    publishabilityReason,
    chapterObservations,
    verificationItems,
    optionalSuggestions,
    priorityOrder,
    limitations
  }
}

function detectJudgment(raw: string): PublishabilityJudgment {
  const lower = raw.toLowerCase()
  if (lower.includes("non pubblicabile")) return "not_publishable"
  if (lower.includes("pubblicabile dopo intervento medio") || lower.includes("intervento medio")) return "publishable_medium"
  if (lower.includes("pubblicabile con correzioni minori") || lower.includes("correzioni minori")) return "publishable_minor"

  return "publishable_medium"
}

function parseErrorTable(raw: string): ReviewErrorRow[] {
  const rows: ReviewErrorRow[] = []
  const lines = raw.split("\n").filter((line) => line.trim().startsWith("|") && !line.includes("---"))

  for (const line of lines) {
    const cells = line.split("|").map((cell) => cell.trim()).filter(Boolean)
    if (cells.length < 6) continue
    if (cells[0].toLowerCase() === "id") continue // header row

    rows.push({
      id: cells[0] || `E${rows.length + 1}`,
      position: cells[1] || "",
      category: cells[2] || "",
      severity: parseSeverity(cells[3]),
      description: cells[4] || "",
      proposedFix: cells[5] || "",
      status: cells[6] || "Aperto"
    })
  }

  return rows
}

function parseSeverity(value: string): "grave" | "media" | "lieve" {
  const lower = value.toLowerCase().trim()
  if (lower.includes("grave") || lower.includes("grav")) return "grave"
  if (lower.includes("lieve") || lower.includes("liev")) return "lieve"

  return "media"
}

function parseChapterObservations(raw: string): ChapterObservation[] {
  const section = extractReportSection(raw, "4. Osservazioni per capitolo") || extractReportSection(raw, "Osservazioni per capitolo") || ""
  if (!section.trim()) return []

  const observations: ChapterObservation[] = []
  const chapterBlocks = section.split(/###\s+/).filter(Boolean)

  for (const block of chapterBlocks) {
    const titleMatch = block.match(/^(.+?)[\n\r]/)
    const title = titleMatch?.[1]?.trim() || "Capitolo"
    const strengths = extractBullet(block, "Punti di forza")
    const issues = extractBullet(block, "Criticita") || extractBullet(block, "Criticità")

    observations.push({
      chapter: title,
      strengths: strengths || "Non specificati.",
      issues: issues || "Non specificati."
    })
  }

  return observations
}

function extractBullet(text: string, label: string) {
  const match = text.match(new RegExp(`[-*]\\s*${label}\\s*:?\\s*(.+?)(?=\\n[-*]|$)`, "is"))
  return match?.[1]?.trim() || ""
}

function parseBulletSection(raw: string): string[] {
  return raw.split("\n")
    .map((line) => line.replace(/^[-*\d.]+\s*/, "").trim())
    .filter(Boolean)
}

function extractReportSection(content: string, heading: string) {
  const lines = content.replace(/\r\n/g, "\n").split("\n")
  const normalizedHeading = heading.toLowerCase().replace(/[àáâã]/g, "a").replace(/[èéêë]/g, "e").replace(/[ìíîï]/g, "i").replace(/[òóôõ]/g, "o").replace(/[ùúûü]/g, "u")

  let start = -1
  for (let i = 0; i < lines.length; i++) {
    const lineLower = lines[i].toLowerCase()
      .replace(/^#+\s*/, "")
      .replace(/[àáâã]/g, "a")
      .replace(/[èéêë]/g, "e")
      .replace(/[ìíîï]/g, "i")
      .replace(/[òóôõ]/g, "o")
      .replace(/[ùúûü]/g, "u")
      .trim()
    if (lineLower.includes(normalizedHeading)) {
      start = i
      break
    }
  }

  if (start === -1) return ""

  let end = lines.length
  for (let i = start + 1; i < lines.length; i++) {
    if (/^#{1,2}\s+/.test(lines[i])) {
      end = i
      break
    }
  }

  return lines.slice(start + 1, end).join("\n").trim()
}

// ── Helpers ────────────────────────────────────────────────────────────────────

async function loadSkillFile(relativePath: string) {
  const fullPath = path.join(process.cwd(), ".agents", "skills", "revisore-editoriale-totale", relativePath)
  return readFile(fullPath, "utf8").catch(() => "")
}

function bookIdFromPath(filePath: string) {
  const normalized = filePath.replace(/\\/g, "/")
  const match = normalized.match(/^books\/(.+?)\/chapters\//)
  return match?.[1] || ""
}

function trimWords(value: string, limit: number) {
  const words = value.replace(/\s+/g, " ").trim().split(" ").filter(Boolean)
  if (words.length <= limit) return words.join(" ")
  return `${words.slice(0, limit).join(" ")}...`
}

function buildLocalFallbackReport() {
  return [
    "# Report editoriale — Revisione locale",
    "",
    "## 1. Sintesi editoriale",
    "- Genere editoriale: manuale per concorsi pubblici",
    "- Pubblico target: candidati a concorsi pubblici italiani",
    "- Perimetro di questa revisione: revisione locale (nessun provider AI disponibile)",
    "- Stato generale: revisione automatica non disponibile, necessario provider AI configurato",
    "",
    "## 3. Tabella errori",
    "| ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato |",
    "|----|-----------|-----------|---------|-------------|----------------------|-------|",
    "| L01 | Intero libro | Revisione AI | Media | Provider AI non disponibile per revisione completa | Configurare un provider (Codex, Claude, Kimi, OpenAI, Hermes) | Aperto |",
    "",
    "## 9. Giudizio di pubblicabilita",
    "Pubblicabile dopo intervento medio",
    "Motivazione: la revisione locale non ha potuto eseguire i 30 controlli della checklist. Configurare un provider AI per una revisione completa.",
    "",
    "## 10. Limiti di questa revisione",
    "- Nessun provider AI era disponibile. Questa è una revisione placeholder.",
    "- Configurare almeno un provider (OPENAI_API_KEY, KIMI_API_KEY, o Codex/Claude CLI) per ottenere una revisione editoriale reale."
  ].join("\n")
}
