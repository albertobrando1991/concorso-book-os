import { describe, expect, it } from "vitest"

import { auditCoverageRows, parseCoverageMatrix } from "../src/server/editorial/didactic-coverage"

const header = `| Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |`

function matrix(row: string) {
  return `${header}\n${row}`
}

describe("didactic coverage matrix", () => {
  it("accepts and counts a complete row", () => {
    const rows = parseCoverageMatrix(matrix(
      "| M-FC02 / funzionario | Diritto tributario | Obbligazione tributaria; presupposto | alta | [[sources/diritto-tributario]] | cap. 4, § 2 | definizione, funzione e disciplina | caso guidato | quiz e orale | domanda di controllo | completo | fonte vigente 2026; review umana | |"
    ))

    expect(rows).toHaveLength(1)
    expect(rows[0]).toMatchObject({
      familyProfile: "M-FC02 / funzionario",
      subject: "Diritto tributario",
      status: "completo"
    })
    expect(auditCoverageRows(rows)).toEqual({ blockers: [], warnings: [], complete: 1 })
  })

  it("blocks a solo-nominato row", () => {
    const rows = parseCoverageMatrix(matrix(
      "| M-FC02 | Tributario | Interpello | alta | [[sources/interpello]] | cap. 5 | cenno | | quiz | | solo-nominato | da revisionare | |"
    ))

    expect(auditCoverageRows(rows).blockers).toEqual(
      expect.arrayContaining([expect.objectContaining({ code: "blocking-status", row: 1 })])
    )
  })

  it("blocks a referral without a precise destination", () => {
    const rows = parseCoverageMatrix(matrix(
      "| M-FC02 | Diritto amministrativo | Accesso | media | [[sources/accesso]] | rinvio | contesto minimo | esempio | quiz | checkpoint | rinviato | verificata | |"
    ))

    expect(auditCoverageRows(rows).blockers).toEqual(
      expect.arrayContaining([expect.objectContaining({ code: "missing-referral-destination", row: 1 })])
    )
  })

  it("warns when a consolidated source is missing", () => {
    const rows = parseCoverageMatrix(matrix(
      "| M-FC02 | Tributario | Imposta | alta | | cap. 4 | definizione | caso | quiz | domanda | completo | review richiesta | |"
    ))

    expect(auditCoverageRows(rows).warnings).toEqual(
      expect.arrayContaining([expect.objectContaining({ code: "missing-source", row: 1 })])
    )
  })

  it("blocks an invalid status", () => {
    const rows = parseCoverageMatrix(matrix(
      "| M-FC02 | Tributario | Imposta | alta | [[sources/imposta]] | cap. 4 | definizione | caso | quiz | domanda | pronto | review | |"
    ))

    expect(auditCoverageRows(rows).blockers).toEqual(
      expect.arrayContaining([expect.objectContaining({ code: "invalid-status", row: 1 })])
    )
  })

  it("blocks a complete row with empty theoretical, application, or verification coverage", () => {
    const rows = parseCoverageMatrix(matrix(
      "| M-FC02 | Tributario | Imposta | alta | [[sources/imposta]] | cap. 4 | | | quiz | | completo | review | |"
    ))

    expect(auditCoverageRows(rows).blockers).toEqual(
      expect.arrayContaining([expect.objectContaining({ code: "incomplete-complete-row", row: 1 })])
    )
  })
})
