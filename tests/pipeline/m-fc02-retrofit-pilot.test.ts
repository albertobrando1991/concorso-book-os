import fs from "node:fs"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { runDidacticDensityGate } from "../../src/pipeline/gates/didactic-density-gate"
import { rowsForChapter, runCoverageGate } from "../../src/pipeline/gates/coverage-gate"
import { parseCoverageMatrix } from "../../src/server/editorial/didactic-coverage"

const root = process.cwd()
const chapterPath = path.join(root, "wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md")
const matrixPath = path.join(root, "wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md")

describe("M-FC02 level-A retrofit pilot", () => {
  it("converts chapter 04 to format 2 without rewriting its substantive content", () => {
    const content = fs.readFileSync(chapterPath, "utf8")
    const result = runDidacticDensityGate({ content, chapterPath })
    expect(content).toMatch(/^format_version:\s*2$/m)
    expect(result.blockers).toEqual([])
    expect(result.warnings.map((issue) => issue.code)).not.toContain("retrofit-dovuto")
  })

  it("maps the six stable nuclei through dimensional v2 rows", () => {
    const matrix = fs.readFileSync(matrixPath, "utf8")
    const rows = rowsForChapter(parseCoverageMatrix(matrix), "04")
    const result = runCoverageGate({ matrix, matrixPath, chapterNumber: "04" })
    expect(rows).toHaveLength(6)
    expect(rows.every((row) => row.schemaVersion === 2 && row.hasDimensionChecklist)).toBe(true)
    expect(result.blockers).toEqual([])
  })
})
