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
  const validBody = `# Il perimetro

## Obiettivo del capitolo

Il candidato comprende il perimetro e sa applicarlo in prova.

## Mappa BANDO

La mappa collega bando, aree, nuclei, diario e output.

## Spiegazione

Il perimetro definisce l'oggetto, la funzione e le conseguenze della disciplina.

## Caso guidato

Il candidato riconosce la regola applicabile in uno scenario d'esame.

## Errore tipico

Confondere il perimetro generale con la regola del singolo bando.

## Mini-esercizio

Spiega la distinzione in cinque righe.`

  it("accepts a chapter with one H1, sources and a declared stage", () => {
    expect(chapter(validBody)).toMatchObject({ passed: true, blockers: [] })
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
  it.each([
    "[[sources/agenzie-fiscali]]",
    "[[topics/imposta]]",
    "[[entities/agenzia-delle-entrate]]",
    "[[../sources/agenzie-fiscali]]",
    "[[templates/prompt-staff]]",
    "[[books/moduli/m-x/sources/fonte]]",
    "[[books/moduli/m-x/topics/tema]]",
    "[[books/moduli/m-x/entities/ente]]",
    "[[books/moduli/m-x/quizzes/verifica]]",
    "[[books/moduli/m-x/reviews/audit]]",
    "[[books/moduli/m-x/planning/02-matrice]]",
    "[[books/moduli/m-x/raw/corpus]]",
    "[[books/moduli/m-x/templates/prompt]]",
    "[[books/moduli/m-x/dashboards/stato]]",
    "[[books/moduli/m-x/memory/note]]",
    "[[books/moduli/m-x/logs/revisione]]",
    "[[log]]",
    "[[wiki/books/moduli/m-x/chapters/../reviews/audit]]",
    "[[books/moduli/m-x/planning/chapters/bypass]]"
  ])("blocks the internal knowledge link %s from the reader body", (link) => {
    expect(codes(chapter(`${validBody}\n\n${link}`))).toContain("internal-knowledge-link")
  })
  it("preserves a public chapter link after canonical dot-segment normalization", () => {
    expect(chapter(`${validBody}\n\n[[books/moduli/m-x/planning/../chapters/01-perimetro]]`).passed).toBe(true)
    expect(chapter(`${validBody}\n\n[[books/moduli/m-x/chapters/planning]]`).passed).toBe(true)
  })
  it.each([
    "Come spiegato nella source note consolidata, il perimetro e completo.",
    "Le fonti consolidate confermano questa distinzione.",
    "Il corpus M-FC02 mostra una ricorrenza.",
    "Consulta la dashboard e il report interno."
  ])("blocks the editorial dependency %s from the reader body", (sentence) => {
    expect(codes(chapter(`${validBody}\n\n${sentence}`))).toContain("editorial-dependency")
  })
  it("does not treat a non-dependent mention of a wiki as an editorial dependency", () => {
    expect(chapter(`${validBody}\n\nUna wiki e un sito collaborativo modificabile dagli utenti.`).passed).toBe(true)
  })
  it.each([
    ["obiettivo", "## Obiettivo del capitolo\n\nIl candidato comprende il perimetro e sa applicarlo in prova.\n\n"],
    ["mappa", "## Mappa BANDO\n\nLa mappa collega bando, aree, nuclei, diario e output.\n\n"],
    ["spiegazione", "## Spiegazione\n\nIl perimetro definisce l'oggetto, la funzione e le conseguenze della disciplina.\n\n"],
    ["applicazione", "## Caso guidato\n\nIl candidato riconosce la regola applicabile in uno scenario d'esame.\n\n"],
    ["errore", "## Errore tipico\n\nConfondere il perimetro generale con la regola del singolo bando.\n\n"],
    ["verifica", "## Mini-esercizio\n\nSpiega la distinzione in cinque righe."]
  ])("blocks a chapter without the %s didactic evidence", (_section, excerpt) => {
    expect(codes(chapter(validBody.replace(excerpt, "")))).toContain("missing-didactic-section")
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
    expect(chapter(`${validBody}\n\n\`\`\`\n# non e un titolo\n\`\`\``).passed).toBe(true)
  })
  it("warns, without blocking, when updated_at is missing", () => {
    const result = chapter(validBody, 'source_refs: ["sources/x"]\ndraft_stage: editorial-draft\nlast_compiled_from: ["sources/x"]')
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
  const before = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso; il metodo e approfondito in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
  const guard = (after: string, start = before) => runCitationGuard({ before: start, after, chapterPath: "chapters/01.md" })

  it("accepts a rewrite that keeps links, sources and norms", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nIl caso ricade nell'art. 3 del d.lgs. 546/1992; il metodo e in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    expect(guard(after)).toMatchObject({ passed: true, blockers: [] })
  })
  it("blocks a lost wikilink", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso.`
    expect(codes(guard(after))).toContain("lost-wikilink")
  })
  it("blocks a lost source ref", () => {
    const after = `---\nsource_refs: ["sources/tributi"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso, come in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    expect(codes(guard(after))).toContain("lost-source-ref")
  })
  it("blocks a norm that disappeared from the text", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nLa disciplina copre il caso, come in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    expect(codes(guard(after))).toContain("lost-norm")
  })
  it("warns when the Humanizer introduces a new norm", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 e l'art. 7 valgono, come in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    expect(guard(after).warnings.map((issue) => issue.code)).toContain("new-norm")
  })
  it("allows the Humanizer to remove internal knowledge links from the reader body", () => {
    const start = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso [[sources/tributi]] e il metodo e in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso e il metodo e in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    expect(guard(after, start)).toMatchObject({ passed: true, blockers: [] })
  })
  it("blocks an internal knowledge link introduced by the Humanizer", () => {
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso [[sources/tributi]] e il metodo e in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    expect(codes(guard(after))).toContain("new-internal-knowledge-link")
  })
  it("blocks every internal knowledge link retained by the Humanizer", () => {
    const start = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso [[books/moduli/m-x/planning/02-matrice]] e il metodo e in [[books/il-metodo-bando/chapters/anatomia-del-bando]].`
    expect(codes(guard(start, start))).toContain("new-internal-knowledge-link")
  })
  it("keeps protecting a public chapter link while internal paths are normalized", () => {
    const start = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso in [[books/moduli/m-x/planning/../chapters/01-perimetro]].`
    const after = `---\nsource_refs: ["sources/tributi", "sources/dogane"]\n---\n\n# Titolo\n\nL'art. 3 del d.lgs. 546/1992 disciplina il caso.`
    expect(codes(guard(after, start))).toContain("lost-wikilink")
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
