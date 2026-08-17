export const COVERAGE_STATUSES = ["completo", "parziale", "solo-nominato", "rinviato", "mancante"] as const
export type CoverageStatus = (typeof COVERAGE_STATUSES)[number]

export const COVERAGE_DIMENSIONS = [
  "definition",
  "function",
  "framing",
  "elements",
  "distinctions",
  "consequences",
  "exampleCase",
  "typicalError",
  "verification",
  "sources"
] as const
export type CoverageDimension = (typeof COVERAGE_DIMENSIONS)[number]

export interface VerificationCounts {
  quizzes: number
  cases: number
  exercises: number
}

export type CoverageDimensions = Record<CoverageDimension, string>

export interface CoverageRow {
  familyProfile: string
  subject: string
  concepts: string
  frequencyWeight: string
  sources: string
  location: string
  theoreticalCoverage: string
  application: string
  competitionOutput: string
  verification: string
  status: string
  normativeReview: string
  referralDestination: string
  nucleusId: string
  schemaVersion: 1 | 2
  verificationCounts?: VerificationCounts
  dimensions: CoverageDimensions
  hasDimensionChecklist: boolean
}

export interface CoverageIssue {
  row: number
  code:
    | "blocking-status"
    | "missing-referral-destination"
    | "missing-source"
    | "invalid-status"
    | "incomplete-complete-row"
    | "invalid-nucleus-id"
    | "invalid-verification"
    | "dimensione-mancante"
  message: string
}

const NUCLEUS_ID = /^N-[A-Z]{2}\d{2}-\d{2}-\d{2}$/
const PRIMARY_FIELDS: Record<string, keyof CoverageRow> = {
  "nucleo id": "nucleusId",
  "famiglia/profilo": "familyProfile",
  "famiglia e profilo": "familyProfile",
  materia: "subject",
  "concetto/sotto-concetti": "concepts",
  "concetto e sotto-concetti": "concepts",
  "frequenza/peso": "frequencyWeight",
  "fonti consolidate": "sources",
  fonti: "sources",
  collocazione: "location",
  "copertura teorica": "theoreticalCoverage",
  applicazione: "application",
  "output concorsuale": "competitionOutput",
  "verifica apprendimento": "verification",
  verifica: "verification",
  stato: "status",
  "review normativa": "normativeReview",
  "destinazione rinvio": "referralDestination"
}
const DIMENSION_FIELDS: Record<string, CoverageDimension> = {
  definizione: "definition",
  funzione: "function",
  inquadramento: "framing",
  elementi: "elements",
  distinzioni: "distinctions",
  conseguenze: "consequences",
  "esempio/caso": "exampleCase",
  "errore tipico": "typicalError",
  verifica: "verification",
  fonti: "sources"
}

export function parseCoverageMatrix(markdown: string): CoverageRow[] {
  const tables = markdownTables(markdown)
  const rows: CoverageRow[] = []
  const dimensionalRows = new Map<string, CoverageDimensions>()

  for (const table of tables) {
    const normalizedHeaders = table.headers.map(normalizeHeader)
    const isPrimary = normalizedHeaders.includes("stato")
    const isDimensional = normalizedHeaders.includes("nucleo id") && normalizedHeaders.includes("definizione") && !isPrimary

    if (isPrimary) {
      const fields = normalizedHeaders.map((header) => PRIMARY_FIELDS[header])
      const schemaVersion = fields.includes("nucleusId") ? 2 : 1

      for (const cells of table.rows) {
        const row = emptyRow(schemaVersion)
        fields.forEach((field, index) => {
          if (!field || field === "schemaVersion" || field === "dimensions" || field === "hasDimensionChecklist" || field === "verificationCounts") return
          row[field] = (cells[index] || "").trim() as never
        })
        row.verificationCounts = schemaVersion === 2 ? parseVerificationCounts(row.verification) : undefined
        rows.push(row)
      }
    } else if (isDimensional) {
      const nucleusIndex = normalizedHeaders.indexOf("nucleo id")
      const fields = normalizedHeaders.map((header) => DIMENSION_FIELDS[header])

      for (const cells of table.rows) {
        const nucleusId = (cells[nucleusIndex] || "").trim()
        if (!nucleusId) continue
        const dimensions = emptyDimensions()
        fields.forEach((field, index) => {
          if (field) dimensions[field] = (cells[index] || "").trim()
        })
        dimensionalRows.set(nucleusId, dimensions)
      }
    }
  }

  return rows.map((row) => {
    const dimensions = dimensionalRows.get(row.nucleusId)
    return dimensions ? { ...row, dimensions, hasDimensionChecklist: true } : row
  })
}

export function parseVerificationCounts(value: string): VerificationCounts | undefined {
  const match = /(?:^|\s)Q\s*:\s*(\d+)\s+C\s*:\s*(\d+)\s+E\s*:\s*(\d+)(?=\s|$)/i.exec(value)
  if (!match) return undefined

  return {
    quizzes: Number.parseInt(match[1], 10),
    cases: Number.parseInt(match[2], 10),
    exercises: Number.parseInt(match[3], 10)
  }
}

export function auditCoverageRows(rows: CoverageRow[]) {
  const blockers: CoverageIssue[] = []
  const warnings: CoverageIssue[] = []
  let complete = 0

  rows.forEach((row, index) => {
    const number = index + 1
    const status = row.status.trim().toLowerCase()
    const rowBlockersBefore = blockers.length

    if (!COVERAGE_STATUSES.includes(status as CoverageStatus)) {
      blockers.push(issue(number, "invalid-status", `Stato non valido: ${row.status || "(vuoto)"}.`))
    } else if (["solo-nominato", "mancante", "parziale"].includes(status)) {
      blockers.push(issue(number, "blocking-status", `Lo stato ${status} non supera il gate editoriale.`))
    }

    if (status === "rinviato" && !isPreciseReferral(row.referralDestination)) {
      blockers.push(issue(number, "missing-referral-destination", "Il rinvio non indica una destinazione precisa."))
    }

    if (!row.sources.trim()) warnings.push(issue(number, "missing-source", "Manca una fonte consolidata."))

    if (status === "completo") {
      if (!row.theoreticalCoverage.trim() || !row.application.trim() || !row.verification.trim()) {
        blockers.push(issue(number, "incomplete-complete-row", "Una riga completa richiede teoria, applicazione e verifica."))
      }

      if (row.schemaVersion === 2) {
        if (!NUCLEUS_ID.test(row.nucleusId)) {
          blockers.push(issue(number, "invalid-nucleus-id", `Nucleo ID non valido: ${row.nucleusId || "(vuoto)"}.`))
        }
        if (!row.verificationCounts) {
          blockers.push(issue(number, "invalid-verification", "La verifica v2 deve iniziare con il formato strutturato Q:<n> C:<n> E:<n>."))
        }
        const missingDimensions = COVERAGE_DIMENSIONS.filter((dimension) => !isCoveredDimension(row.dimensions[dimension]))
        if (!row.hasDimensionChecklist || missingDimensions.length) {
          blockers.push(issue(number, "dimensione-mancante", `Checklist dimensionale incompleta: ${missingDimensions.join(", ") || "tabella assente"}.`))
        }
      }

      if (blockers.length === rowBlockersBefore) complete += 1
    }
  })

  return { blockers, warnings, complete }
}

export function isPreciseReferral(destination: string): boolean {
  const value = destination.trim()
  if (!value || /^(?:volume base|altrove|vedi sopra)$/i.test(value)) return false
  if (/\[\[[^\]]+#[^\]]+\]\]/.test(value)) return true
  const hasPathTarget = /\[\[[^\]]+\]\]/.test(value) || /(?:^|\s)(?:\.{0,2}\/)?[\w./-]+\.md\b/i.test(value)
  const hasHumanTarget = /(?:\bVOL-\d+\b|\bM-[A-Z]{2}\d+\b|\bvolume\s+\d+\b)/i.test(value)
  const hasChapter = /\bcap(?:itolo)?\.?\s*[\w-]+/i.test(value)
  const hasParagraph = /(?:§|\bpar(?:agrafo)?\.?)\s*[\w-]+/i.test(value)
  return (hasPathTarget && (hasChapter || hasParagraph)) || (hasHumanTarget && hasChapter && hasParagraph)
}

function isCoveredDimension(value: string) {
  const normalized = value.trim().toLowerCase()
  return normalized.startsWith("✓") || /^n\/?a(?:\b|\s|:|—|-)/i.test(normalized)
}

function emptyRow(schemaVersion: 1 | 2): CoverageRow {
  return {
    familyProfile: "",
    subject: "",
    concepts: "",
    frequencyWeight: "",
    sources: "",
    location: "",
    theoreticalCoverage: "",
    application: "",
    competitionOutput: "",
    verification: "",
    status: "",
    normativeReview: "",
    referralDestination: "",
    nucleusId: "",
    schemaVersion,
    dimensions: emptyDimensions(),
    hasDimensionChecklist: false
  }
}

function emptyDimensions(): CoverageDimensions {
  return {
    definition: "",
    function: "",
    framing: "",
    elements: "",
    distinctions: "",
    consequences: "",
    exampleCase: "",
    typicalError: "",
    verification: "",
    sources: ""
  }
}

function markdownTables(markdown: string) {
  const lines = markdown.split(/\r?\n/)
  const tables: Array<{ headers: string[]; rows: string[][] }> = []

  for (let index = 0; index < lines.length - 1; index += 1) {
    const headers = tableLine(lines[index])
    if (!headers || !separator(lines[index + 1])) continue
    const rows: string[][] = []
    for (let rowIndex = index + 2; rowIndex < lines.length; rowIndex += 1) {
      const cells = tableLine(lines[rowIndex])
      if (!cells) break
      rows.push(cells)
    }
    tables.push({ headers, rows })
  }

  return tables
}

function normalizeHeader(value: string) {
  return value.toLowerCase().replace(/\s+/g, " ").trim()
}

function tableLine(line: string) {
  const value = line.trim()
  return value.startsWith("|") && value.endsWith("|") ? tokenize(value.slice(1, -1)) : null
}

function tokenize(value: string) {
  const cells: string[] = []
  let cell = ""
  let codeDelimiterLength = 0
  let inWikilink = false

  for (let index = 0; index < value.length; index += 1) {
    const char = value[index]
    const next = value[index + 1]
    if (char === "\\" && next === "|") {
      cell += "|"
      index += 1
      continue
    }
    if (!codeDelimiterLength && char === "[" && next === "[") {
      inWikilink = true
      cell += "[["
      index += 1
      continue
    }
    if (!codeDelimiterLength && inWikilink && char === "]" && next === "]") {
      inWikilink = false
      cell += "]]"
      index += 1
      continue
    }
    if (!inWikilink && char === "`") {
      let run = 1
      while (value[index + run] === "`") run += 1
      if (!codeDelimiterLength) codeDelimiterLength = run
      else if (run === codeDelimiterLength) codeDelimiterLength = 0
      cell += "`".repeat(run)
      index += run - 1
      continue
    }
    if (char === "|" && !codeDelimiterLength && !inWikilink) {
      cells.push(cell.trim())
      cell = ""
    } else {
      cell += char
    }
  }

  cells.push(cell.trim())
  return cells
}

function separator(line: string) {
  const cells = tableLine(line)
  return Boolean(cells?.length && cells.every((cell) => /^:?-{3,}:?$/.test(cell)))
}

function issue(row: number, code: CoverageIssue["code"], message: string): CoverageIssue {
  return { row, code, message }
}
