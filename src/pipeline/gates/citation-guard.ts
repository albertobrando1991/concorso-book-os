import { parseFrontmatter } from "../../server/wiki/frontmatter"
import { extractWikiLinks } from "../../server/wiki/markdown"
import type { GateIssue, GateResult } from "../state/types"

export interface CitationGuardInput {
  before: string
  after: string
  chapterPath: string
}

const NORM_PATTERNS = [
  /\bart(?:t)?\.\s*\d+[a-z-]*(?:\s*(?:bis|ter|quater|quinquies))?/gi,
  /\bd\.?\s*lgs\.?\s*n?\.?\s*\d+\/\d{4}/gi,
  /\bd\.?\s*p\.?\s*r\.?\s*n?\.?\s*\d+\/\d{4}/gi,
  /\bl(?:egge)?\.?\s*n\.?\s*\d+\/\d{4}/gi,
  /\bd\.?\s*l\.?\s*n?\.?\s*\d+\/\d{4}/gi
]

export function runCitationGuard(input: CitationGuardInput): GateResult {
  const at = (code: string, message: string): GateIssue => ({ code, message, location: input.chapterPath })

  if (!input.before.trim()) {
    return {
      passed: false,
      blockers: [
        at(
          "missing-snapshot",
          `Nessuno snapshot pre-Humanizer per ${input.chapterPath}: esegui "pipeline next" sullo step 11 prima di modificare il capitolo, così la pipeline registra il testo di partenza.`
        )
      ],
      warnings: []
    }
  }

  const before = analyze(input.before)
  const after = analyze(input.after)
  const blockers = [
    ...missing(before.links, after.links).map((value) => at("lost-wikilink", `Wikilink perso nell'Humanizer: [[${value}]].`)),
    ...missing(before.sourceRefs, after.sourceRefs).map((value) => at("lost-source-ref", `source_refs perso dal frontmatter: ${value}.`)),
    ...missing(before.norms, after.norms).map((value) => at("lost-norm", `Riferimento normativo scomparso dal testo: ${value}.`))
  ]
  const warnings = [
    ...missing(after.links, before.links).map((value) =>
      at("new-wikilink", `Wikilink aggiunto durante l'Humanizer: [[${value}]]. Verificare che sia fondato.`)
    ),
    ...missing(after.norms, before.norms).map((value) =>
      at("new-norm", `Riferimento normativo introdotto durante l'Humanizer: ${value}. L'Humanizer non deve aggiungere norme.`)
    )
  ]

  return { passed: blockers.length === 0, blockers, warnings }
}

function analyze(content: string) {
  const { data, body } = parseFrontmatter(content.replace(/\r\n/g, "\n"))
  const frontmatter = data as Record<string, unknown>

  return {
    links: new Set(extractWikiLinks(body).map(normalizeValue)),
    sourceRefs: new Set(asList(frontmatter.source_refs).map(normalizeValue)),
    norms: new Set(NORM_PATTERNS.flatMap((pattern) => body.match(pattern) ?? []).map(normalizeNorm))
  }
}

function missing(source: Set<string>, target: Set<string>) {
  return [...source].filter((value) => !target.has(value))
}

function normalizeValue(value: string) {
  return value.trim().toLowerCase()
}

function normalizeNorm(value: string) {
  return value.replace(/\s+/g, " ").trim().toLowerCase()
}

function asList(value: unknown) {
  if (Array.isArray(value)) return value.map((item) => String(item).trim()).filter(Boolean)

  const single = value === undefined || value === null ? "" : String(value).trim()

  return single ? [single] : []
}
