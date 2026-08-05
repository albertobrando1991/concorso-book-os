import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { join } from "node:path"
import { describe, expect, it } from "vitest"
import { runChapterLintGate } from "../../src/pipeline/gates/chapter-lint-gate"
import { runCitationGuard } from "../../src/pipeline/gates/citation-guard"
import { runCoverageGate } from "../../src/pipeline/gates/coverage-gate"
import { runDidacticDensityGate } from "../../src/pipeline/gates/didactic-density-gate"
import { runReviewReportGate } from "../../src/pipeline/gates/review-report-gate"
import { runGate } from "../../src/pipeline/gates"
import { runVerifiedReferralGate } from "../../src/pipeline/gates/verified-referral-gate"

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
    "Consulta la dashboard e il report interno.",
    "Consulta un report.",
    "La risposta si trova nella dashboard.",
    "La risposta si trova dentro la dashboard.",
    "I risultati sono in un report.",
    "La risposta è disponibile in una dashboard.",
    "I dati sono raccolti in una wiki.",
    "Gli esiti sono su una dashboard.",
    "I dettagli sono nella wiki.",
    "I dettagli sono nei report.",
    "Le risposte sono nelle wiki.",
    "La soluzione è descritta nel report.",
    "Il procedimento è illustrato sulla dashboard.",
    "Gli esiti sono sui report.",
    "La procedura rimanda alle dashboard.",
    "I dati provengono dai report.",
    "Il candidato accede ai dati attraverso la wiki.",
    "La verifica avviene tramite il report.",
    "Per la verifica si rimanda al report.",
    "Il report interno contiene i dati.",
    "La dashboard riporta i risultati.",
    "La wiki contiene le istruzioni.",
    "Il report fornisce le informazioni necessarie.",
    "Per la risposta, usa la dashboard.",
    "Apri la wiki per leggere i dettagli.",
    "La dashboard consente di trovare la soluzione.",
    "La definizione è nella wiki.",
    "Il criterio è spiegato nel report.",
    "La risposta si trova nella **dashboard**.",
    "Per la risposta, usa la **dashboard**.",
    "Apri la `wiki` per leggere i dettagli.",
    "Il criterio è spiegato nel **report**.",
    "La risposta si trova nella `dashboard`.",
    "La soluzione è nella [dashboard](https://example.test/cruscotto).",
    "Sulla dashboard sono disponibili le risposte.",
    "Nel report sono raccolti i dati.",
    "Dentro la dashboard sono presenti i dettagli.",
    "La dashboard interna contiene le istruzioni.",
    "Il report di revisione contiene i risultati.",
    "La dashboard rende disponibili i risultati.",
    "La wiki ospita le istruzioni.",
    "La risposta è disponibile qui:\n\n- nella dashboard.",
    "La dashboard seguente è lo strumento da usare.\n\nContiene le risposte."
  ])("blocks the editorial dependency %s from the reader body", (sentence) => {
    expect(codes(chapter(`${validBody}\n\n${sentence}`))).toContain("editorial-dependency")
  })
  it.each([
    "Una wiki è un sito collaborativo modificabile dagli utenti.",
    "La dashboard è uno strumento che sintetizza indicatori.",
    "La dashboard è uno strumento che riporta i risultati.",
    "La wiki è una raccolta di pagine collaborative.",
    "Il report è un documento che presenta risultati.",
    "Un report è un documento strutturato che presenta risultati.",
    "Una dashboard può sintetizzare gli indicatori.",
    "Un report confronta risultati di periodi diversi.",
    "Le wiki sono siti collaborativi.",
    "Le dashboard sono strumenti di visualizzazione.",
    "I report sono documenti strutturati.",
    "In una dashboard, i grafici possono sintetizzare gli indicatori.",
    "In una wiki, le voci possono essere collegate tra loro.",
    "Per dashboard si intende un pannello di visualizzazione.",
    "Con il termine report si indica un documento riepilogativo.",
    "Le dashboard consentono di sintetizzare gli indicatori.",
    "Un database consente di creare maschere e report.",
    "Un report contiene dati riepilogativi.",
    "Una dashboard mostra risultati aggregati.",
    "La wiki raccoglie informazioni collegate.",
    "Il referto e il report di laboratorio riportano i risultati.",
    "I risultati sono presentati di seguito\n\nUna dashboard è uno strumento che sintetizza indicatori.",
    "leggere testi, istruzioni, dashboard e documentazione",
    "gestire dati strutturati in tabelle, query, maschere e report"
  ])("does not treat the encyclopedic mention %s as an editorial dependency", (sentence) => {
    expect(chapter(`${validBody}\n\n${sentence}`).passed).toBe(true)
  })
  it.each([
    "wiki/books/il-metodo-bando/chapters/diario-degli-errori.md",
    "wiki/books/il-metodo-bando/chapters/prendere-servizio-nella-pa-dal-concorso-al-ruolo.md",
    "wiki/books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali.md"
  ])("does not add an editorial dependency to the real chapter %s", (chapterPath) => {
    const result = runChapterLintGate({ content: readFileSync(chapterPath, "utf8"), chapterPath })

    expect(codes(result)).not.toContain("editorial-dependency")
  })
  it.each([
    "wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali.md",
    "wiki/books/moduli/m-sa02-professioni-sanitarie/planning/00-piano-editoriale.md"
  ])("keeps blocking the real internal dependency in %s", (chapterPath) => {
    const result = runChapterLintGate({ content: readFileSync(chapterPath, "utf8"), chapterPath })

    expect(codes(result)).toContain("editorial-dependency")
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
  it("requires format_version 2 when the pipeline is completing step 09", () => {
    const content = `---\n${defaults}\n---\n\n${validBody}`
    const result = runChapterLintGate({ content, chapterPath: "chapters/01.md", requireFormatVersion2: true })

    expect(codes(result)).toContain("missing-format-version")
    expect(
      runChapterLintGate({ content: content.replace("---\n", "---\nformat_version: 2\n"), chapterPath: "chapters/01.md", requireFormatVersion2: true }).passed
    ).toBe(true)
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
  it("blocks every error deferred to human review before the final signoff", () => {
    const result = report("| E3 | cap. 3 | norma | media | soglia da verificare | chiedere al revisore | review umana |")
    expect(result.passed).toBe(false)
    expect(codes(result)).toContain("deferred-to-human")
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
  it("selects v2 rows by the chapter segment of Nucleo ID instead of free-form location prose", () => {
    const v2 = `| Nucleo ID | Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N-FC02-04-01 | M-FC02 | Tributi | Imposta | alta | [[sources/y]] | testo libero senza numero capitolo | definizione | caso | quiz | Q:6 C:1 E:1 | parziale | review | |`

    expect(codes(runCoverageGate({ matrix: v2, matrixPath: "m.md", chapterNumber: "04" }))).toContain("blocking-status")
    expect(codes(runCoverageGate({ matrix: v2, matrixPath: "m.md", chapterNumber: "03" }))).toContain("unassigned-chapter")
  })
})

describe("didactic density gate", () => {
  const words = (count: number, token = "parola") => Array.from({ length: count }, () => token).join(" ")
  const nucleus = (id: string, count = 600) => `## ${id} · Titolo del nucleo\n\n${words(count)}`
  const quiz = Array.from({ length: 6 }, (_, index) => `### Quiz ${index + 1}\n\nRisposta corretta: A. Commento.`).join("\n\n")
  const verification = `## ▣ Verifica 01.A\n\n${quiz}\n\n### Caso ragionato\n\nApplicazione commentata.`
  const body = (nuclei: string[], tail = verification) => `# Capitolo\n\n${nuclei.join("\n\n")}\n\n${tail}`
  const v2 = (chapterBody: string) =>
    runDidacticDensityGate({
      content: `---\nformat_version: 2\n---\n\n${chapterBody}`,
      chapterPath: "chapters/01.md"
    })

  it("accepts a format v2 chapter at every minimum threshold", () => {
    const result = v2(body(Array.from({ length: 5 }, (_, index) => nucleus(`N-FC02-01-0${index + 1}`))))

    expect(result).toMatchObject({ passed: true, blockers: [] })
  })
  it("turns every deficit into one retrofit warning for legacy chapters", () => {
    const result = runDidacticDensityGate({ content: "# Capitolo\n\nBreve.", chapterPath: "chapters/legacy.md" })

    expect(result).toMatchObject({ passed: true, blockers: [] })
    expect(result.warnings.map((issue) => issue.code)).toContain("retrofit-dovuto")
  })
  it("blocks fewer than five valid nuclei", () => {
    expect(codes(v2(body([nucleus("N-FC02-01-01")])))).toContain("nuclei-insufficienti")
  })
  it("blocks a heading that starts with N- but has a malformed ID", () => {
    const nuclei = [nucleus("N-FC02-01-01"), nucleus("N-FC02-01-02"), nucleus("N-FC02-01-03"), nucleus("N-FC02-01-04"), nucleus("N-FC02-1-5")]

    expect(codes(v2(body(nuclei)))).toContain("nucleo-id-malformato")
  })
  it("blocks a nucleus below 600 words", () => {
    const nuclei = Array.from({ length: 5 }, (_, index) => nucleus(`N-FC02-01-0${index + 1}`, index === 2 ? 599 : 600))

    expect(codes(v2(body(nuclei)))).toContain("nucleo-troppo-breve")
  })
  it("blocks a chapter without a verification heading", () => {
    const nuclei = Array.from({ length: 5 }, (_, index) => nucleus(`N-FC02-01-0${index + 1}`))

    expect(codes(v2(body(nuclei, `${quiz}\n\nCaso guidato`)))).toContain("verifica-assente")
  })
  it("blocks more than seven consecutive nuclei without an interposed verification", () => {
    const nuclei = Array.from({ length: 8 }, (_, index) => nucleus(`N-FC02-01-0${index + 1}`))

    expect(codes(v2(body(nuclei)))).toContain("verifica-troppo-distante")
  })
  it("blocks fewer than six commented quiz answers", () => {
    const nuclei = Array.from({ length: 5 }, (_, index) => nucleus(`N-FC02-01-0${index + 1}`))

    expect(codes(v2(body(nuclei, "## ▣ Verifica 01.A\n\nRisposta corretta: A.\n\nCaso guidato")))).toContain("quiz-insufficienti")
  })
  it("blocks a chapter without a guided or reasoned case", () => {
    const nuclei = Array.from({ length: 5 }, (_, index) => nucleus(`N-FC02-01-0${index + 1}`))

    expect(codes(v2(body(nuclei, `## ▣ Verifica 01.A\n\n${quiz}`)))).toContain("caso-assente")
  })
  it("blocks a chapter below 3000 body words even when structural counts pass", () => {
    const nuclei = Array.from({ length: 5 }, (_, index) => nucleus(`N-FC02-01-0${index + 1}`, 100))

    expect(codes(v2(body(nuclei)))).toContain("capitolo-troppo-breve")
  })
  it("ignores nucleus and verification headings inside code fences", () => {
    const fenced = `# Capitolo\n\n\`\`\`markdown\n## N-FC02-01-01 · Falso\n## ▣ Verifica 01.A\n\`\`\`\n\n${words(3000)}\n\n${quiz}\n\nCaso guidato`

    expect(codes(v2(fenced))).toEqual(expect.arrayContaining(["nuclei-insufficienti", "verifica-assente"]))
  })
})

describe("didactic density pipeline wiring", () => {
  it("combines matrix coverage blockers with chapter density warnings at step 10", async () => {
    const projectRoot = mkdtempSync(join(tmpdir(), "didactic-density-wiring-"))
    const wikiRoot = join(projectRoot, "wiki")
    const moduleId = "moduli/m-test"
    const chapterTarget = `${moduleId}/chapters/01.md`
    const matrixPath = join(wikiRoot, "books", moduleId, "planning", "02-matrice-copertura-didattica.md")
    const chapterPath = join(wikiRoot, "books", chapterTarget)
    mkdirSync(join(wikiRoot, "books", moduleId, "planning"), { recursive: true })
    mkdirSync(join(wikiRoot, "books", moduleId, "chapters"), { recursive: true })
    writeFileSync(chapterPath, "# Capitolo legacy\n\nBreve.")
    writeFileSync(
      matrixPath,
      `| Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M-TEST | Materia | Nucleo | alta | [[sources/x]] | cap. 1 | cenno | caso | quiz | domanda | parziale | review | |`
    )

    try {
      const module = {
        code: "M-TEST",
        moduleId,
        priority: 1,
        phases: ["C"],
        chapters: [{ number: "01", title: "Capitolo legacy", file: "chapters/01.md", matrix: "planning/02-matrice-copertura-didattica.md", expectedStatus: "completo", notes: "" }],
        chaptersSource: "declared" as const,
        line: 1,
        chapterLines: [1]
      }
      const result = await runGate("didactic-density", {
        projectRoot,
        wikiRoot,
        module,
        chapterNumber: "01",
        spec: {
          specPath: "spec.md",
          volumeCode: "VOL-99",
          volumeTitle: "Test",
          cutOffDate: "2026-08-01",
          writerProvider: "codex",
          phases: ["C"],
          modules: [module]
        },
        step: { key: "10:test", id: "10", phase: "C", scope: "chapter", target: chapterTarget, status: "in-progress", attempts: 0, evidence: [] }
      })

      expect(codes(result)).toContain("blocking-status")
      expect(result.warnings.map((issue) => issue.code)).toContain("retrofit-dovuto")
    } finally {
      rmSync(projectRoot, { recursive: true, force: true })
    }
  })
})

describe("verified VOL-01 referrals", () => {
  it("accepts an existing VOL-01 file and exact heading", async () => {
    const root = mkdtempSync(join(tmpdir(), "verified-referral-"))
    const target = join(root, "books", "il-metodo-bando", "chapters", "accesso.md")
    mkdirSync(join(root, "books", "il-metodo-bando", "chapters"), { recursive: true })
    writeFileSync(target, "# Accesso\n\n## Accesso documentale\n\nTesto.")

    try {
      const result = await runVerifiedReferralGate({
        content: "[[books/il-metodo-bando/chapters/accesso#Accesso documentale]]",
        wikiRoot: root,
        chapterPath: "wiki/books/moduli/test.md"
      })
      expect(result).toMatchObject({ passed: true, blockers: [] })
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })
  it.each([
    ["[[books/il-metodo-bando/chapters/assente#Accesso documentale]]", "file"],
    ["[[books/il-metodo-bando/chapters/accesso#Heading inesistente]]", "heading"]
  ])("blocks a VOL-01 referral with a missing %s", async (link) => {
    const root = mkdtempSync(join(tmpdir(), "verified-referral-"))
    const target = join(root, "books", "il-metodo-bando", "chapters", "accesso.md")
    mkdirSync(join(root, "books", "il-metodo-bando", "chapters"), { recursive: true })
    writeFileSync(target, "# Accesso\n\n## Accesso documentale\n\nTesto.")

    try {
      const result = await runVerifiedReferralGate({ content: link, wikiRoot: root, chapterPath: "chapter.md" })
      expect(codes(result)).toContain("rinvio-non-risolto")
    } finally {
      rmSync(root, { recursive: true, force: true })
    }
  })
})
