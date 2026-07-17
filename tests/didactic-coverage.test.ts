import { execFileSync, spawnSync } from "node:child_process"
import { mkdtempSync, mkdirSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { join, resolve } from "node:path"
import { afterEach, describe, expect, it } from "vitest"
import { auditCoverageRows, parseCoverageMatrix } from "../src/server/editorial/didactic-coverage"

const header = `| Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |`
const matrix = (row: string) => `${header}\n${row}`
const directories: string[] = []
afterEach(() => directories.splice(0).forEach((directory) => rmSync(directory, { recursive: true, force: true })))

describe("didactic coverage matrix", () => {
  it("accepts and counts a complete row", () => {
    const rows = parseCoverageMatrix(matrix("| M-FC02 / funzionario | Tributario | Obbligazione | alta | [[sources/tributario]] | cap. 4 | definizione | caso | quiz | domanda | completo | review | |"))
    expect(rows[0]).toMatchObject({ familyProfile: "M-FC02 / funzionario", subject: "Tributario", status: "completo" })
    expect(auditCoverageRows(rows)).toEqual({ blockers: [], warnings: [], complete: 1 })
  })
  it.each(["solo-nominato", "parziale", "mancante"])("blocks the %s status", (status) => {
    const rows = parseCoverageMatrix(matrix(`| M-FC02 | Tributario | Imposta | alta | [[sources/imposta]] | cap. 4 | cenno | caso | quiz | domanda | ${status} | review | |`))
    expect(auditCoverageRows(rows).blockers).toEqual(expect.arrayContaining([expect.objectContaining({ code: "blocking-status" })]))
  })
  it.each(["", "volume base", "altrove", "vedi sopra"])("blocks the imprecise referral '%s'", (destination) => {
    const rows = parseCoverageMatrix(matrix(`| M-FC02 | Amministrativo | Accesso | media | [[sources/accesso]] | rinvio | contesto | esempio | quiz | checkpoint | rinviato | review | ${destination} |`))
    expect(auditCoverageRows(rows).blockers).toEqual(expect.arrayContaining([expect.objectContaining({ code: "missing-referral-destination" })]))
  })
  it.each(["[[books/base#accesso-documentale]]", "books/base.md, capitolo 4, paragrafo 2"])("accepts the precise referral %s", (destination) => {
    const rows = parseCoverageMatrix(matrix(`| M-FC02 | Amministrativo | Accesso | media | [[sources/accesso]] | rinvio | contesto | esempio | quiz | checkpoint | rinviato | review | ${destination} |`))
    expect(auditCoverageRows(rows).blockers).toEqual([])
  })
  it("warns when a consolidated source is missing", () => {
    const rows = parseCoverageMatrix(matrix("| M-FC02 | Tributario | Imposta | alta | | cap. 4 | definizione | caso | quiz | domanda | completo | review | |"))
    expect(auditCoverageRows(rows).warnings).toEqual(expect.arrayContaining([expect.objectContaining({ code: "missing-source" })]))
  })
  it("blocks an invalid status", () => {
    const rows = parseCoverageMatrix(matrix("| M-FC02 | Tributario | Imposta | alta | [[sources/imposta]] | cap. 4 | definizione | caso | quiz | domanda | pronto | review | |"))
    expect(auditCoverageRows(rows).blockers).toEqual(expect.arrayContaining([expect.objectContaining({ code: "invalid-status" })]))
  })
  it("blocks a complete row with empty theoretical, application, or verification coverage", () => {
    const rows = parseCoverageMatrix(matrix("| M-FC02 | Tributario | Imposta | alta | [[sources/imposta]] | cap. 4 | | | quiz | | completo | review | |"))
    expect(auditCoverageRows(rows).blockers).toEqual(expect.arrayContaining([expect.objectContaining({ code: "incomplete-complete-row" })]))
  })
  it("does not split escaped pipes, aliased wikilinks, or inline code", () => {
    const rows = parseCoverageMatrix(matrix("| M-FC02 | Tributario | A \\| B; [[topics/imposta|imposta]]; `x | y` | alta | [[sources/imposta|fonte]] | cap. 4 | definizione | caso | quiz | domanda | completo | review | |"))
    expect(rows).toHaveLength(1)
    expect(rows[0]).toMatchObject({ concepts: "A | B; [[topics/imposta|imposta]]; `x | y`", sources: "[[sources/imposta|fonte]]", status: "completo" })
  })
})

describe("didactic coverage CLI", () => {
  const script = resolve("scripts/audit-didactic-coverage.mjs")
  it("exits zero with an explicit message when no matrix exists", () => {
    expect(execFileSync(process.execPath, [script], { cwd: temporaryDirectory(), encoding: "utf8" })).toContain("nessuna matrice")
  })
  it("scans recursively, prints a summary, and exits one for blockers", () => {
    const cwd = temporaryDirectory(), nested = join(cwd, "wiki", "books", "module", "planning")
    mkdirSync(nested, { recursive: true })
    writeFileSync(join(nested, "02-matrice-copertura-didattica.md"), matrix("| M-FC02 | Tributario | Imposta | alta | [[sources/imposta]] | cap. 4 | cenno | caso | quiz | domanda | parziale | review | |"))
    const result = spawnSync(process.execPath, [script], { cwd, encoding: "utf8" })
    expect(result.status).toBe(1)
    expect(result.stdout).toContain("02-matrice-copertura-didattica.md")
    expect(result.stdout).toContain("1 blocker")
    expect(result.stdout).toContain("Totale: 1 matrici")
  })
})

function temporaryDirectory() { const directory = mkdtempSync(join(tmpdir(), "coverage-audit-")); directories.push(directory); return directory }
