import { auditCoverageRows, parseCoverageMatrix, type CoverageRow } from "../../server/editorial/didactic-coverage"
import type { GateIssue, GateResult } from "../state/types"

export interface CoverageGateInput {
  matrix: string
  matrixPath: string
  chapterNumber?: string
}

export function runCoverageGate(input: CoverageGateInput): GateResult {
  const all = parseCoverageMatrix(input.matrix)

  if (!all.length) {
    return {
      passed: false,
      blockers: [
        {
          code: "missing-matrix",
          message: `La matrice ${input.matrixPath} non contiene righe leggibili: il gate di copertura non può essere valutato.`,
          location: input.matrixPath
        }
      ],
      warnings: []
    }
  }

  const rows = input.chapterNumber ? rowsForChapter(all, input.chapterNumber) : all

  if (input.chapterNumber && !rows.length) {
    return {
      passed: false,
      blockers: [
        {
          code: "unassigned-chapter",
          message: `Nessuna riga della matrice ${input.matrixPath} è collocata nel capitolo ${input.chapterNumber}: assegna i nuclei prima di dichiarare il capitolo completo.`,
          location: input.matrixPath
        }
      ],
      warnings: []
    }
  }

  const audit = auditCoverageRows(rows)

  return {
    passed: audit.blockers.length === 0,
    blockers: audit.blockers.map((issue) => toGateIssue(issue, input.matrixPath)),
    warnings: audit.warnings.map((issue) => toGateIssue(issue, input.matrixPath))
  }
}

export function rowsForChapter(rows: CoverageRow[], chapterNumber: string) {
  const pattern = chapterPattern(chapterNumber)

  return rows.filter((row) => pattern.test(row.location))
}

function chapterPattern(chapterNumber: string) {
  const normalized = chapterNumber.trim().replace(/^0+(?=\d)/, "")
  const escaped = normalized.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")

  return new RegExp(`\\bcap(?:itolo)?\\.?\\s*0*${escaped}\\b`, "i")
}

function toGateIssue(issue: { row: number; code: string; message: string }, matrixPath: string): GateIssue {
  return { code: issue.code, message: `riga ${issue.row}: ${issue.message}`, location: `${matrixPath}:${issue.row}` }
}
