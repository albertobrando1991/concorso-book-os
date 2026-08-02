import fs from "node:fs"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { runDidacticDensityGate } from "../../src/pipeline/gates/didactic-density-gate"
import { rowsForChapter, runCoverageGate } from "../../src/pipeline/gates/coverage-gate"
import { extractOperationalDataReviewRows } from "../../src/pipeline/review/operational-data"
import { parseCoverageMatrix } from "../../src/server/editorial/didactic-coverage"

const projectRoot = process.cwd()
const chapterPath = path.join(
  projectRoot,
  "wiki",
  "books",
  "moduli",
  "m-sa02-professioni-sanitarie",
  "chapters",
  "05-valutazione-clinica-triage-urgenza-emergenza.md"
)
const matrixPath = path.join(
  projectRoot,
  "wiki",
  "books",
  "moduli",
  "m-sa02-professioni-sanitarie",
  "planning",
  "02-matrice-copertura-didattica.md"
)

describe("VOL-07 hybrid nucleus pilot", () => {
  it("publishes chapter M-SA02/05 as a conforming format 2 chapter", () => {
    const content = fs.readFileSync(chapterPath, "utf8")
    const nucleusIds = [...content.matchAll(/^## (N-SA02-05-\d{2}) · /gm)].map((match) => match[1])
    const result = runDidacticDensityGate({ content, chapterPath })

    expect(content).toMatch(/^format_version:\s*2$/m)
    expect(content).toMatch(/^review_required:\s*false$/m)
    expect(nucleusIds).toHaveLength(7)
    expect(new Set(nucleusIds).size).toBe(7)
    expect(result.blockers).toEqual([])
    expect(extractOperationalDataReviewRows(content, chapterPath)).toEqual([
      expect.objectContaining({
        id: "DO-SA02-05-NEWS2-ER-2024",
        auditArea: "clinico-assistenziale",
        source: "Regione Emilia-Romagna, NEWS2",
        version: "settembre 2024 (base RCP 2017)",
        verifiedAt: "2026-08-01"
      })
    ])
  })

  it("maps every pilot nucleus to an auditable v2 coverage row without early human review", () => {
    const matrix = fs.readFileSync(matrixPath, "utf8")
    const rows = rowsForChapter(parseCoverageMatrix(matrix), "05")
    const result = runCoverageGate({ matrix, matrixPath, chapterNumber: "05" })

    expect(rows).toHaveLength(7)
    expect(rows.every((row) => row.schemaVersion === 2 && row.hasDimensionChecklist)).toBe(true)
    expect(new Set(rows.map((row) => row.nucleusId)).size).toBe(7)
    expect(result.blockers).toEqual([])
    expect(matrix).not.toMatch(
      /revisore clinico|revisore indipendente|assegnare (?:a )?un revisore|review (?:clinica|professionale|umana).*step 15/i
    )
  })

  it("keeps every historical module out of human waiting before final signoff", () => {
    const runState = JSON.parse(
      fs.readFileSync(path.join(projectRoot, "pipeline", "VOL-07", "run-state.json"), "utf8")
    ) as { steps: Array<{ id: string; status: string }> }

    expect(runState.steps.filter((step) => step.status === "awaiting-human" && step.id !== "24")).toEqual([])
    expect(
      runState.steps
        .filter((step) => step.id === "15")
        .every((step) => step.status === "done" || step.status === "pending")
    ).toBe(true)
  })
})
