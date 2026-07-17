export const COVERAGE_STATUSES = ["completo", "parziale", "solo-nominato", "rinviato", "mancante"] as const
export type CoverageStatus = (typeof COVERAGE_STATUSES)[number]
export interface CoverageRow { familyProfile: string; subject: string; concepts: string; frequencyWeight: string; sources: string; location: string; theoreticalCoverage: string; application: string; competitionOutput: string; verification: string; status: string; normativeReview: string; referralDestination: string }
export interface CoverageIssue { row: number; code: "blocking-status" | "missing-referral-destination" | "missing-source" | "invalid-status" | "incomplete-complete-row"; message: string }
const FIELDS: Record<string, keyof CoverageRow> = { "famiglia/profilo": "familyProfile", "famiglia e profilo": "familyProfile", materia: "subject", "concetto/sotto-concetti": "concepts", "concetto e sotto-concetti": "concepts", "frequenza/peso": "frequencyWeight", "fonti consolidate": "sources", fonti: "sources", collocazione: "location", "copertura teorica": "theoreticalCoverage", applicazione: "application", "output concorsuale": "competitionOutput", "verifica apprendimento": "verification", verifica: "verification", stato: "status", "review normativa": "normativeReview", "destinazione rinvio": "referralDestination" }
export function parseCoverageMatrix(markdown: string): CoverageRow[] {
  const lines = markdown.split(/\r?\n/), rows: CoverageRow[] = []
  for (let i = 0; i < lines.length - 1; i += 1) {
    const headers = tableLine(lines[i]); if (!headers || !separator(lines[i + 1])) continue
    const fields = headers.map((header) => FIELDS[header.toLowerCase().replace(/\s+/g, " ")]); if (!fields.includes("status")) continue
    for (let j = i + 2; j < lines.length; j += 1) {
      const cells = tableLine(lines[j]); if (!cells) break
      const row = emptyRow(); fields.forEach((field, index) => { if (field) row[field] = (cells[index] || "").trim() }); rows.push(row)
    }
  }
  return rows
}
export function auditCoverageRows(rows: CoverageRow[]) {
  const blockers: CoverageIssue[] = [], warnings: CoverageIssue[] = []; let complete = 0
  rows.forEach((row, index) => {
    const number = index + 1, status = row.status.trim().toLowerCase()
    if (!COVERAGE_STATUSES.includes(status as CoverageStatus)) blockers.push(issue(number, "invalid-status", `Stato non valido: ${row.status || "(vuoto)"}.`))
    else if (["solo-nominato", "mancante", "parziale"].includes(status)) blockers.push(issue(number, "blocking-status", `Lo stato ${status} non supera il gate editoriale.`))
    if (status === "rinviato" && !row.referralDestination.trim()) blockers.push(issue(number, "missing-referral-destination", "Il rinvio non indica una destinazione precisa."))
    if (!row.sources.trim()) warnings.push(issue(number, "missing-source", "Manca una fonte consolidata."))
    if (status === "completo") {
      if (!row.theoreticalCoverage.trim() || !row.application.trim() || !row.verification.trim()) blockers.push(issue(number, "incomplete-complete-row", "Una riga completa richiede teoria, applicazione e verifica."))
      else complete += 1
    }
  })
  return { blockers, warnings, complete }
}
function emptyRow(): CoverageRow { return { familyProfile: "", subject: "", concepts: "", frequencyWeight: "", sources: "", location: "", theoreticalCoverage: "", application: "", competitionOutput: "", verification: "", status: "", normativeReview: "", referralDestination: "" } }
function tableLine(line: string) { const value = line.trim(); return value.startsWith("|") && value.endsWith("|") ? value.slice(1, -1).split("|").map((cell) => cell.trim()) : null }
function separator(line: string) { const cells = tableLine(line); return Boolean(cells?.length && cells.every((cell) => /^:?-{3,}:?$/.test(cell))) }
function issue(row: number, code: CoverageIssue["code"], message: string): CoverageIssue { return { row, code, message } }
