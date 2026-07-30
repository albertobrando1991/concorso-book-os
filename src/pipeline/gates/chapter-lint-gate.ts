import { parseFrontmatter } from "../../server/wiki/frontmatter"
import { extractWikiLinks } from "../../server/wiki/markdown"
import type { GateIssue, GateResult } from "../state/types"
import { isInternalKnowledgeLink } from "./reader-contract"

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

const EDITORIAL_DEPENDENCIES = [
  /\bsource notes?\b/i,
  /\bfont(?:e|i) consolidat(?:a|e)\b/i,
  /\bcorpus\s+(?:m-[a-z0-9-]+|auditato|interno|editoriale|dei bandi)\b/i,
  /\b(?:consulta|consultare|consultate|consulti|vedi|si\s+veda|si\s+consulti|rinvia|si\s+rinvia|accedi|fare\s+riferimento|fai\s+riferimento)\b[^.!?\n]{0,120}\b(?:wiki|dashboard|report\s+intern[oaie])\b/i,
  /\b(?:nel(?:la|le|lo)?|nell['’]|sul(?:la|le|lo)?|sull['’]|al(?:la|le|lo)?|all['’]|dal(?:la|le|lo)?|dall['’]|in)\s+(?:wiki|dashboard|report(?:\s+intern[oaie])?)\b/i,
  /\breport\s+intern[oaie]\b/i
]

const DIDACTIC_SECTIONS = [
  { label: "obiettivo didattico", pattern: /\b(?:obiettiv[oi]|risultati? di apprendimento)\b/i },
  { label: "Mappa BANDO", pattern: /\b(?:mappa bando|metodo bando|bando in pratica)\b/i },
  {
    label: "spiegazione teorica",
    pattern: /\b(?:spiegazione|inquadramento|quadro|fondament[oi]|principi?|disciplin[ae]|profil[oi]|requisiti?|prove?|autonomia|responsabilit[aà]|deontologia)\b/i
  },
  { label: "applicazione o caso", pattern: /\b(?:cas[oi]|esempi?|applicazione|come lo chiede|domanda da commissario)\b/i },
  { label: "errore o trappola", pattern: /\b(?:error[ei]|trappola|attenzione)\b/i },
  { label: "verifica dell'apprendimento", pattern: /\b(?:eserciz(?:io|i)|quiz|verifica|checklist|domanda da commissario)\b/i }
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

  const internalLinks = extractWikiLinks(body).filter(isInternalKnowledgeLink)

  if (internalLinks.length) {
    blockers.push(
      at(
        "internal-knowledge-link",
        `Il corpo del capitolo contiene link interni non disponibili allo studente: ${internalLinks.map((link) => `[[${link}]]`).join(", ")}. Sposta la tracciabilità nel frontmatter o nel report di review.`
      )
    )
  }

  const editorialDependency = EDITORIAL_DEPENDENCIES.find((pattern) => pattern.test(body))

  if (editorialDependency) {
    blockers.push(
      at(
        "editorial-dependency",
        "Il testo dipende da note, corpus o strumenti editoriali interni: insegna direttamente il contenuto necessario allo studente."
      )
    )
  }

  const headingText = headings.map((heading) => heading.text).join("\n")

  DIDACTIC_SECTIONS.filter((section) => !section.pattern.test(headingText)).forEach((section) => {
    blockers.push(
      at(
        "missing-didactic-section",
        `Manca un'evidenza strutturale per ${section.label}: il capitolo deve accompagnare lo studente dalla teoria alla prova.`
      )
    )
  })

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
