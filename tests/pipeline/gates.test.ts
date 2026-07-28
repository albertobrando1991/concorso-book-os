import { describe, expect, it } from "vitest"
import { runChapterLintGate } from "../../src/pipeline/gates/chapter-lint-gate"
import { runCitationGuard } from "../../src/pipeline/gates/citation-guard"
import { runCoverageGate } from "../../src/pipeline/gates/coverage-gate"
import { runReviewReportGate } from "../../src/pipeline/gates/review-report-gate"

const codes = (result: { blockers: { code: string }[] }) => result.blockers.map((issue) => issue.code)

describe("chapter lint gate", () => {
  const defaults = 'source_refs: ["sources/agenzie-fiscali"]\ndraft_stage: editorial-draft\nupdated_at: 2026-07-27\nlast_compiled_from: ["sources/agenzie-fiscali"]'
  const chapter = (body: string, frontmatter = defaults) =>
    runChapterLintGate({ content: `---\n${frontmatter}\n---\n\n${body}\n`, chapterPath: "chapters/01-perimetro.md" })

  it("accepts a chapter with one H1, sources and a declared stage", () => {
    expect(chapter("# Il perimetro\n\n## Le tre porte\n\nTesto operativo.")).toMatchObject({ passed: true, blockers: [] })
  })
  it("blocks a chapter with more than one H1", () => {
    expect(codes(chapter("# Uno\n\nTesto.\n\n# Due\n\nAltro."))).toContain("heading-h1")
  })
  it("blocks a chapter with no H1", () => {
    expect(codes(chapter("## Solo una sezione\n\nTesto."))).toContain("heading-h1")
  })
  it("blocks a jump in the heading hierarchy", () => {
    expect(codes(chapter("# Titolo\n\n### Sotto-sotto\n\nTesto."))).toContain("heading-jump")
  })
  it.each(["TODO: completare", "Lorem ipsum dolor", "[da completare]"])("blocks the leftover placeholder %s", (placeholder) => {
    expect(codes(chapter(`# Titolo\n\n${placeholder}`))).toContain("placeholder")
  })
  it("blocks an agent meta-comment instead of the chapter text", () => {
    expect(codes(chapter("# Titolo\n\nAggiornamento generato: ho integrato la sezione."))).toContain("agent-meta")
  })
  it("blocks a chapter without source_refs", () => {
    expect(codes(chapter("# Titolo\n\nTesto.", "draft_stage: editorial-draft"))).toContain("missing-source-refs")
  })
  it("blocks a chapter without draft_stage", () => {
    expect(codes(chapter("# Titolo\n\nTesto.", 'source_refs: ["sources/x"]'))).toContain("missing-draft-stage")
  })
  it("blocks an empty chapter", () => {
    expect(codes(chapter(""))).toContain("empty-chapter")
  })
  it("ignores headings inside a code fence", () => {
    expect(chapter("# Titolo\n\n```\n# non è un titolo\n```\n\nTesto.").passed).toBe(true)
  })
  it("warns, without blocking, when updated_at is missing", () => {
    const result = chapter("# Titolo\n\nTesto.", 'source_refs: ["sources/x"]\ndraft_stage: editorial-draft\nlast_compiled_from: ["sources/x"]')
    expect(result.passed).toBe(true)
    expect(result.warnings.map((issue) => issue.code)).toContain("missing-updated-at")
  })
})

describe("review report gate", () => {
  const header =
    "| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n| --- | --- | --- | --- | --- | --- | --- |"
  const report = (rows: string, extra = "") =>
    runReviewReportGate({ report: `## Tabella errori\n\n${header}\n${rows}\n\n${extra}`, reportPath: "wiki/reviews/r.md" })

  it("accepts a report whose severe errors are all closed", () => {
    expect(report("| E1 | cap. 1 | contenuto | grave | manca la definizione | aggiungere | applicato |").passed).toBe(true)
  })
  it("blocks an open severe error", () => {
    expect(codes(report("| E1 | cap. 1 | contenuto | grave | manca la definizione | aggiungere | aperto |"))).toContain("open-severe-error")
  })
  it.each(["critico", "bloccante"])("treats %s as a severe level", (severity) => {
    expect(codes(report(`| E1 | cap. 1 | norma | ${severity} | soglia errata | verificare | aperto |`))).toContain("open-severe-error")
  })
  it("warns, without blocking, on an open minor error", () => {
    const result = report("| E2 | cap. 2 | stile | lieve | ripetizione | riformulare | aperto |")
    expect(result.passed).toBe(true)
    expect(result.warnings.map((issue) => issue.code)).toContain("open-minor-error")
  })
  it("accepts an error explicitly assigned to human review", () => {
    expect(report("| E3 | cap. 3 | norma | media | soglia da verificare | chiedere al revisore | review umana |").warnings).toEqual([])
  })
  it("blocks a report without the fixed error table", () => {
    expect(codes(runReviewReportGate({ report: "## Sintesi\n\nTutto bene.", reportPath: "wiki/reviews/r.md" }))).toContain("missing-error-table")
  })
  it("blocks a missing report", () => {
    expect(codes(runReviewReportGate({ report: "", reportPath: "wiki/reviews/r.md" }))).toContain("missing-report")
  })
  it("requires the publishability judgment on the final review", () => {
    const rows = "| E1 | cap. 1 | stile | lieve | refuso | correggere | applicato |"
    expect(codes(runReviewReportGate({ report: `${header}\n${rows}`, reportPath: "wiki/reviews/r.md", requireJudgment: true }))).toContain(
      "missing-judgment"
    )
  })
  it("blocks a final review that is not publishable with minor fixes", () => {
    const rows = "| E1 | cap. 1 | stile | lieve | refuso | correggere | applicato |"
    const result = runReviewReportGate({
      report: `${header}\n${rows}\n\n## Giudizio\n\nNon pubblicabile allo stato attuale.`,
      reportPath: "wiki/reviews/r.md",
      requireJudgment: true
    })
    expect(codes(result)).toContain("judgment-not-publishable")
  })
  it("accepts a final review judged publishable with minor fixes", () => {
    const rows = "| E1 | cap. 1 | stile | lieve | refuso | correggere | applicato |"
    const result = runReviewReportGate({
      report: `${header}\n${rows}\n\n## Giudizio\n\nPubblicabile con correzioni minori.`,
      reportPath: "wiki/reviews/r.md",
      requireJudgment: true
    })
    expect(result.passed).toBe(true)
  })
})

describe("citation guard", () => {
  const before = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso, come indicato in [[topics/imposta]].`
  const guard = (after: string, start = before) => runCitationGuard({ before: start, after, chapterPath: "chapters/01.md" })

  it("accepts a rewrite that keeps links, sources and norms", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nIl caso ricade nell'art. 3 del d.lgs. 546/1992; il quadro sta in [[topics/imposta]].`
    expect(guard(after)).toMatchObject({ passed: true, blockers: [] })
  })
  it("blocks a lost wikilink", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso.`
    expect(codes(guard(after))).toContain("lost-wikilink")
  })
  it("blocks a lost source ref", () => {
    const after = `---\nsource_refs: ["sources/tributi"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso, come in [[topics/imposta]].`
    expect(codes(guard(after))).toContain("lost-source-ref")
  })
  it("blocks a norm that disappeared from the text", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nLa disciplina copre il caso, come in [[topics/imposta]].`
    expect(codes(guard(after))).toContain("lost-norm")
  })
  it("warns when the Humanizer introduces a new norm", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 e l'art. 7 valgono, come in [[topics/imposta]].`
    expect(guard(after).warnings.map((issue) => issue.code)).toContain("new-norm")
  })
  it("blocks when the pre-Humanizer snapshot is missing", () => {
    expect(codes(guard(before, ""))).toContain("missing-snapshot")
  })
})

describe("coverage gate", () => {
  const header = `| Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |`
  const matrix = (rows: string) => `${header}\n${rows}`

  it("evaluates only the rows placed in the requested chapter", () => {
    const rows = [
      "| M-FC02 | Perimetro | Enti | alta | [[sources/x]] | cap. 1, `Le tre porte` | definizione | caso | quiz | domanda | completo | review | |",
      "| M-FC02 | Tributi | Imposta | alta | [[sources/y]] | cap. 4, `Teoria` | cenno | caso | quiz | domanda | parziale | review | |"
    ].join("\n")
    expect(runCoverageGate({ matrix: matrix(rows), matrixPath: "m.md", chapterNumber: "01" }).passed).toBe(true)
    expect(codes(runCoverageGate({ matrix: matrix(rows), matrixPath: "m.md", chapterNumber: "04" }))).toContain("blocking-status")
  })
  it("blocks a chapter with no row assigned to it", () => {
    const rows = "| M-FC02 | Perimetro | Enti | alta | [[sources/x]] | cap. 1 | definizione | caso | quiz | domanda | completo | review | |"
    expect(codes(runCoverageGate({ matrix: matrix(rows), matrixPath: "m.md", chapterNumber: "07" }))).toContain("unassigned-chapter")
  })
  it("blocks an unreadable matrix", () => {
    expect(codes(runCoverageGate({ matrix: "# Nessuna tabella", matrixPath: "m.md" }))).toContain("missing-matrix")
  })
})
