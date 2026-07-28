import { parseFrontmatter } from "../../server/wiki/frontmatter"
import type { GateIssue, GateResult } from "../state/types"

export interface ChapterLintInput {
  content: string
  chapterPath: string
}

const AGENT_META = [
  /^\s*(?:#+\s*)?aggiornamento generato\b/im,
  /^\s*(?:#+\s*)?istruzione ricevuta\b/im,
  /^\s*(?:#+\s*)?ecco (?:il|la|una|un)\b/im,
  /\bcome (?:assistente|modello) (?:ai|linguistico)\b/i,
  /\bnon posso (?:accedere|verificare)\b/i
]

const PLACEHOLDERS = [
  /\bTODO\b/,
  /\bTBD\b/,
  /\bFIXME\b/,
  /\bXXX\b/,
  /\blorem ipsum\b/i,
  /\[da (?:completare|inserire|verificare in seguito)\]/i,
  /\bdescrizione da scrivere\b/i
]

export function runChapterLintGate(input: ChapterLintInput): GateResult {
  const { data, body } = parseFrontmatter(input.content.replace(/\r\n/g, "\n"))
  const frontmatter = data as Record<string, unknown>
  const blockers: GateIssue[] = []
  const warnings: GateIssue[] = []
  const at = (code: string, message: string): GateIssue => ({ code, message, location: input.chapterPath })

  if (!body.trim()) {
    return {
      passed: false,
      blockers: [at("empty-chapter", "Il capitolo è vuoto: lo step 09 deve produrre il testo destinato al lettore.")],
      warnings: []
    }
  }

  const headings = headingsOf(body)
  const titles = headings.filter((heading) => heading.level === 1)

  if (titles.length !== 1) {
    blockers.push(at("heading-h1", `Il capitolo deve avere un solo H1: trovati ${titles.length}.`))
  }

  const jumpIndex = headings.findIndex((heading, index) => index > 0 && heading.level - headings[index - 1].level > 1)

  if (jumpIndex > 0) {
    blockers.push(
      at(
        "heading-jump",
        `Salto di gerarchia al titolo "${headings[jumpIndex].text}": un H${headings[jumpIndex].level} non può seguire un H${headings[jumpIndex - 1].level}.`
      )
    )
  }

  PLACEHOLDERS.filter((pattern) => pattern.test(body)).forEach((pattern) => {
    blockers.push(at("placeholder", `Segnaposto residuo nel testo (${pattern.source}): il capitolo non è consegnabile al lettore.`))
  })

  if (AGENT_META.some((pattern) => pattern.test(body))) {
    blockers.push(at("agent-meta", "Meta-commento da agente nel testo: il capitolo deve contenere il manuale, non il resoconto del lavoro."))
  }

  if (!asList(frontmatter.source_refs).length) {
    blockers.push(at("missing-source-refs", "Frontmatter senza source_refs: ogni capitolo deve dichiarare le fonti consolidate da cui deriva."))
  }

  if (!text(frontmatter.draft_stage)) {
    blockers.push(at("missing-draft-stage", "Frontmatter senza draft_stage: lo stato del capitolo deve essere dichiarato in modo veritiero."))
  }

  if (!text(frontmatter.updated_at)) {
    warnings.push(at("missing-updated-at", "Frontmatter senza updated_at: la data di ultima lavorazione manca."))
  }

  if (!asList(frontmatter.last_compiled_from).length) {
    warnings.push(at("missing-last-compiled-from", "Frontmatter senza last_compiled_from: la tracciabilità della compilazione è incompleta."))
  }

  return { passed: blockers.length === 0, blockers, warnings }
}

function headingsOf(body: string) {
  const lines = body.split("\n")

  return lines.reduce<{ level: number; text: string }[]>((headings, line, index) => {
    if (isInsideFence(lines, index)) return headings

    const match = /^(#{1,6})\s+(.+?)\s*$/.exec(line)

    return match ? [...headings, { level: match[1].length, text: match[2] }] : headings
  }, [])
}

function isInsideFence(lines: string[], index: number) {
  return lines.slice(0, index).filter((line) => /^\s*```/.test(line)).length % 2 === 1
}

function asList(value: unknown) {
  if (Array.isArray(value)) return value.map((item) => String(item).trim()).filter(Boolean)

  return text(value) ? [text(value)] : []
}

function text(value: unknown) {
  return value === undefined || value === null ? "" : String(value).trim()
}
