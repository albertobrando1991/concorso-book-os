import { parseMarkdownTables } from "../../server/wiki/markdown-table"
import type { GateIssue, GateResult } from "../state/types"

export interface ReviewReportInput {
  report: string
  reportPath: string
  requireJudgment?: boolean
}

export const SEVERE_LEVELS = ["grave", "critico", "bloccante"]
export const CLOSED_STATES = ["applicato", "applicata", "chiuso", "chiusa", "risolto", "risolta", "corretto", "corretta"]
export const ASSIGNED_STATES = ["review umana", "in review", "assegnato", "assegnata", "attesa review"]

const PUBLISHABLE = /pubblicabile con correzioni minori/i
const OTHER_JUDGMENTS = [/pubblicabile dopo intervento medio/i, /non pubblicabile allo stato attuale/i]

interface ErrorRow {
  id: string
  position: string
  severity: string
  description: string
  state: string
}

export function runReviewReportGate(input: ReviewReportInput): GateResult {
  const at = (code: string, message: string): GateIssue => ({ code, message, location: input.reportPath })

  if (!input.report.trim()) {
    return { passed: false, blockers: [at("missing-report", `Report di revisione assente o vuoto: ${input.reportPath}.`)], warnings: [] }
  }

  const rows = errorRows(input.report)

  if (!rows.length) {
    return {
      passed: false,
      blockers: [
        at(
          "missing-error-table",
          `Il report ${input.reportPath} non contiene la tabella errori del template fisso (ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato).`
        )
      ],
      warnings: []
    }
  }

  const blockers = rows
    .filter(isOpenSevere)
    .map((row) =>
      at(
        "open-severe-error",
        `Errore grave aperto ${row.id || "(senza ID)"} in ${row.position || "posizione non indicata"}: ${row.description || row.state}.`
      )
    )
  const warnings = rows
    .filter(isOpenMinor)
    .map((row) => at("open-minor-error", `Errore non grave ancora aperto ${row.id || "(senza ID)"}: stato "${row.state || "non indicato"}".`))

  if (!input.requireJudgment) {
    return { passed: blockers.length === 0, blockers, warnings }
  }

  const judgment = judgmentOf(input.report)
  const judgmentBlockers = !judgment
    ? [at("missing-judgment", `Il report ${input.reportPath} non dichiara il giudizio di pubblicabilità previsto dal template.`)]
    : PUBLISHABLE.test(judgment)
      ? []
      : [at("judgment-not-publishable", `Giudizio di pubblicabilità non sufficiente: "${judgment}".`)]

  return { passed: blockers.length + judgmentBlockers.length === 0, blockers: [...blockers, ...judgmentBlockers], warnings }
}

export function errorRows(report: string): ErrorRow[] {
  return parseMarkdownTables(report)
    .filter((table) => table.headers.some((header) => /^stato$/i.test(header.trim())) && table.headers.some((header) => /gravit/i.test(header)))
    .flatMap((table) =>
      table.rows.map((row) => ({
        id: row.id ?? "",
        position: row.posizione ?? "",
        severity: (row["gravità"] ?? row.gravita ?? "").toLowerCase(),
        description: row.descrizione ?? "",
        state: (row.stato ?? "").toLowerCase()
      }))
    )
}

function isOpenSevere(row: ErrorRow) {
  return SEVERE_LEVELS.some((level) => row.severity.includes(level)) && !isClosed(row)
}

function isOpenMinor(row: ErrorRow) {
  return !SEVERE_LEVELS.some((level) => row.severity.includes(level)) && !isClosed(row) && !isAssigned(row)
}

function isClosed(row: ErrorRow) {
  return CLOSED_STATES.some((state) => row.state.includes(state))
}

function isAssigned(row: ErrorRow) {
  return ASSIGNED_STATES.some((state) => row.state.includes(state))
}

function judgmentOf(report: string) {
  return [PUBLISHABLE, ...OTHER_JUDGMENTS].map((pattern) => pattern.exec(report)).find(Boolean)?.[0] ?? ""
}
