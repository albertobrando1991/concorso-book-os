import { describe, expect, it } from "vitest"
import { extractOperationalDataReviewRows, renderOperationalDataReviewAppendix } from "../../src/pipeline/review/operational-data"

describe("operational data specialist audit package", () => {
  const chapter = `---
title: Prevenzione delle cadute
dati_operativi: ["DO-SA02-05-CONLEY"]
---
# Prevenzione delle cadute

> **Dato operativo — Scala di Conley**
> Ambito: prevenzione cadute, adulto ospedalizzato · Livello: nazionale
> Fonte: Linea guida ufficiale · Versione: 2 · Verificata al: 2026-08-01
> Contenuto verificato.
> Review: REV-INF (professionista sanitario del profilo)
`

  it("extracts one mandatory specialist row for each Dato operativo box", () => {
    expect(extractOperationalDataReviewRows(chapter, "books/moduli/m-sa02/chapters/05-cadute.md")).toEqual([
      expect.objectContaining({
        id: "DO-SA02-05-CONLEY",
        title: "Scala di Conley",
        line: 7,
        reviewer: "REV-INF",
        source: "Linea guida ufficiale",
        version: "2",
        verifiedAt: "2026-08-01"
      })
    ])
  })

  it("renders the rows as a precise step-15 checklist", () => {
    const rows = extractOperationalDataReviewRows(chapter, "books/moduli/m-sa02/chapters/05-cadute.md")
    const appendix = renderOperationalDataReviewAppendix(rows)

    expect(appendix).toContain("## Dati operativi — righe obbligatorie generate dalla pipeline")
    expect(appendix).toContain("DO-SA02-05-CONLEY")
    expect(appendix).toContain("REV-INF")
    expect(appendix).toContain("05-cadute.md:7")
  })
})
