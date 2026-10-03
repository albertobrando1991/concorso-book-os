import { describe, expect, it } from "vitest"
import { extractOperationalDataReviewRows, renderOperationalDataReviewAppendix } from "../../src/pipeline/review/operational-data"

describe("operational data specialist audit package", () => {
  it("extracts frontmatter audit metadata while keeping the reader table outside staff boxes", () => {
    const content = `---
dati_operativi: ["DO-NEWS2"]
dati_operativi_audit: [{"id":"DO-NEWS2","title":"NEWS2: calcolo e limiti","heading":"NEWS2: calcolo e limiti","auditArea":"clinico-assistenziale","source":"RCP NEWS2","version":"2017","verifiedAt":"2026-10-03"}]
---
### NEWS2: calcolo e limiti

| Parametro | Punteggio |
| --- | --- |
| Ossigenoterapia | 2 |
`
    expect(extractOperationalDataReviewRows(content, "chapter.md")).toEqual([
      { id: "DO-NEWS2", title: "NEWS2: calcolo e limiti", file: "chapter.md", line: 5,
        auditArea: "clinico-assistenziale", source: "RCP NEWS2", version: "2017", verifiedAt: "2026-10-03" }
    ])
  })

  it("preserves missing audit fields as explicit unresolved values", () => {
    const content = '---\ndati_operativi_audit: [{"id":"DO-X","heading":"Missing heading"}]\n---\n# Chapter\n'
    expect(extractOperationalDataReviewRows(content, "chapter.md")[0]).toMatchObject({
      id: "DO-X", source: "NON INDICATA", version: "NON INDICATA", verifiedAt: "NON INDICATA", line: 2
    })
  })

  const chapter = `---
title: Prevenzione delle cadute
dati_operativi: ["DO-SA02-05-CONLEY"]
---
# Prevenzione delle cadute

> **Dato operativo · Scala di Conley**
> Ambito: prevenzione cadute, adulto ospedalizzato · Livello: nazionale
> Fonte: Linea guida ufficiale · Versione: 2 · Verificata al: 2026-08-01
> Contenuto verificato.
> Audit automatico: clinico-assistenziale
`

  it("extracts one mandatory specialist row for each Dato operativo box", () => {
    expect(extractOperationalDataReviewRows(chapter, "books/moduli/m-sa02/chapters/05-cadute.md")).toEqual([
      expect.objectContaining({
        id: "DO-SA02-05-CONLEY",
        title: "Scala di Conley",
        line: 7,
        auditArea: "clinico-assistenziale",
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
    expect(appendix).toContain("Area di audit automatico")
    expect(appendix).toContain("clinico-assistenziale")
    expect(appendix).not.toMatch(/revisore|NON ASSEGNATO|REV-INF/i)
    expect(appendix).toContain("05-cadute.md:7")
  })
})
