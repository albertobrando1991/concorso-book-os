const DEFAULT_REPORT = "wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md"
const PX_PER_MM = 96 / 25.4

export function resolvePageAuditOptions(env = process.env) {
  const expectedPageCount = positiveInteger(
    env.BOOK_STUDIO_EXPECTED_PAGE_COUNT || "381",
    "expected page count"
  )
  const contactSheetSize = positiveInteger(
    env.BOOK_STUDIO_CONTACT_SHEET_SIZE || "20",
    "contact sheet size"
  )
  const reportMode = String(env.BOOK_STUDIO_AUDIT_REPORT_MODE || "write")

  if (!new Set(["write", "verify"]).has(reportMode)) {
    throw new Error(`Modalita report non valida: ${reportMode}`)
  }

  const explicitScreenshotPages = [...new Set(
    String(env.BOOK_STUDIO_AUDIT_PAGES || "")
      .split(",")
      .map((value) => value.trim())
      .filter(Boolean)
      .map((value) => positiveInteger(value, "screenshot page"))
  )].sort((left, right) => left - right)

  return {
    baseUrl: String(env.BOOK_STUDIO_URL || "http://127.0.0.1:3010"),
    bookId: String(env.BOOK_STUDIO_BOOK_ID || "volumi/vol-07"),
    artifactPrefix: String(env.BOOK_STUDIO_ARTIFACT_PREFIX || "vol-07-step-20"),
    reportPath: String(env.BOOK_STUDIO_AUDIT_REPORT || DEFAULT_REPORT),
    expectedPageCount,
    contactSheetSize,
    reportMode,
    explicitScreenshotPages
  }
}

export function buildContactSheetRanges(pageCount, sheetSize = 20) {
  const count = positiveInteger(pageCount, "page count")
  const size = positiveInteger(sheetSize, "contact sheet size")
  const ranges = []

  for (let start = 1, index = 1; start <= count; start += size, index += 1) {
    const end = Math.min(count, start + size - 1)
    ranges.push({
      index,
      start,
      end,
      pages: Array.from({ length: end - start + 1 }, (_, offset) => start + offset)
    })
  }

  return ranges
}

export function flaggedPageNumbers(issues, explicitPages = []) {
  return [...new Set([
    ...issues.map((issue) => issue.page),
    ...explicitPages
  ])].sort((left, right) => left - right)
}

export function classifyPageDiagnostic(page, context) {
  const issues = []
  const add = (problemType, element, severity, correction) => {
    issues.push({
      page: page.page,
      problemType,
      element,
      severity,
      correction,
      outcome: "aperto"
    })
  }

  const expectedLeft = page.side === "recto" ? 23 * PX_PER_MM : 13 * PX_PER_MM
  const expectedRight = page.side === "recto" ? 13 * PX_PER_MM : 23 * PX_PER_MM

  if (page.domIndex !== page.page || page.printedNumber !== page.page) {
    add("page-number", "numero pagina", "bloccante", "riallineare sequenza DOM e footer")
  }
  if (
    Math.abs(page.width - context.expectedWidth) > 1
    || Math.abs(page.height - context.expectedHeight) > 1
  ) {
    add("page-size", "pagina", "bloccante", "ripristinare master 6.69 x 9.61 in")
  }
  if (
    Math.abs(page.paddingLeft - expectedLeft) > 1
    || Math.abs(page.paddingRight - expectedRight) > 1
    || Math.abs(page.paddingTop - 18 * PX_PER_MM) > 1
    || Math.abs(page.paddingBottom - 18 * PX_PER_MM) > 1
  ) {
    add("margins", "padding pagina", "bloccante", "ripristinare margini speculari 23/13/18 mm")
  }
  if (page.overflow > 8) {
    add("overflow", "area contenuto/footer", "bloccante", "ripaginare i blocchi oltre il limite utile")
  }
  for (const value of page.collisions) {
    add("collision", value, "bloccante", "separare gli elementi sovrapposti")
  }
  for (const value of page.rawMarkdown) {
    add("raw-markdown", value, "bloccante", "renderizzare la sintassi Markdown")
  }
  for (const value of page.typographyFailures) {
    add("typography", value, "bloccante", "ripristinare la scala tipografica canonica")
  }
  for (const value of page.headingFailures) {
    add("heading-hierarchy", value, "bloccante", "ripristinare la gerarchia progressiva dei titoli")
  }
  for (const value of page.unjustifiedProse) {
    add("justification", value, "bloccante", "applicare giustificazione e regole 3/3")
  }
  if (page.lastBlock?.type === "heading") {
    add("orphan-heading", "ultimo heading", "bloccante", "tenere il titolo con il blocco successivo")
  }
  for (const table of page.tables.filter(
    (value) => !value.contained || (value.continued && !value.hasHeader)
  )) {
    add("table-header", table.label, "bloccante", "ripetere intestazione e contenere la tabella")
  }
  for (const image of page.images.filter((value) => !value.loaded || !value.contained)) {
    add("broken-image", image.label, "bloccante", "caricare e contenere immagine e didascalia")
  }
  for (const image of page.images.filter((value) => !value.hasCaption)) {
    add("image-caption", image.label, "bloccante", "ripristinare la didascalia associata")
  }
  if (page.consecutiveImages) {
    add("consecutive-images", "figure consecutive", "bloccante", "separare le figure con contenuto motivante")
  }
  for (const edge of [page.firstBlock, page.lastBlock]) {
    if (edge?.type === "paragraph" && edge.continued && edge.lines < 3) {
      add("widow-orphan", "frammento paragrafo", "media", "ripaginare almeno tre righe insieme")
    }
  }
  for (const value of page.detachedBlocks) {
    add("detached-box", value, "media", "tenere box e primo contenuto insieme")
  }

  const whitespaceLimit = Math.max(180, context.medianFreeSpace + 120)
  const exemptWhitespace = page.isSectionTerminal
    || page.sectionType === "front_matter"
    || page.frontMatterLayout === "module-opening"

  if (!exemptWhitespace && (page.freeSpace > whitespaceLimit || page.fillRatio < 0.35)) {
    add("page-fill", "area utile", "media", "verificare ritmo e ripaginare il vuoto anomalo")
  }

  return issues
}

export function buildPageRegistryRows(diagnostics, issues) {
  const byPage = new Map()

  for (const issue of issues) {
    byPage.set(issue.page, [...(byPage.get(issue.page) || []), issue])
  }

  return diagnostics.map((page) => {
    const pageIssues = byPage.get(page.page) || []

    if (pageIssues.length === 0) {
      return {
        page: page.page,
        problemType: "nessuno",
        element: "pagina",
        severity: "nessuna",
        correction: "nessuna",
        outcome: "conforme"
      }
    }

    return {
      page: page.page,
      problemType: pageIssues.map((issue) => issue.problemType).join("<br>"),
      element: pageIssues.map((issue) => issue.element).join("<br>"),
      severity: pageIssues.some((issue) => issue.severity === "bloccante")
        ? "bloccante"
        : "media",
      correction: pageIssues.map((issue) => issue.correction).join("<br>"),
      outcome: pageIssues.every((issue) => issue.outcome !== "aperto")
        ? "risolto - ricontrollato"
        : "aperto"
    }
  })
}

export function renderPageAuditMarkdown({
  generatedAt,
  bookId,
  diagnostics,
  issues
}) {
  const registryRows = buildPageRegistryRows(diagnostics, issues)
  const blocking = issues.filter((issue) => issue.severity === "bloccante").length
  const significant = issues.filter((issue) => issue.severity === "media").length
  const rows = registryRows
    .map((row) => [
      row.page,
      row.problemType,
      row.element,
      row.severity,
      row.correction,
      row.outcome
    ].map(escapeCell))
    .map((cells) => `| ${cells.join(" | ")} |`)
    .join("\n")
  const anomalies = issues.length === 0
    ? "Nessuna anomalia automatica aperta."
    : issues.map(
      (issue) => `- Pagina ${issue.page}: ${issue.problemType} - ${issue.element} (${issue.severity}).`
    ).join("\n")

  return `---
id: review-vol-07-step-20-page-audit
type: review
title: Audit pagina per pagina - VOL-07
status: in-progress
domain: concorsi pubblici italiani
topics:
  - audit pagina per pagina
  - Book Studio
entities:
  - Amazon KDP
source_refs: []
book_refs:
  - vol-07-sanita-amministrativa-professioni-sanitarie
confidence: 1
updated_at: ${generatedAt}
created_at: ${generatedAt}
review_required: true
canonical: false
tags:
  - pipeline-step-20
  - page-fill
  - vol-07
issue_type: page_fill
severity: ${blocking > 0 ? "high" : significant > 0 ? "medium" : "none"}
affected_pages:
  - books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md
---

# Audit pagina per pagina - VOL-07

## Sintesi

- Book ID: \`${bookId}\`
- Pagine DOM: ${diagnostics.length}
- Problemi bloccanti aperti: ${blocking}
- Problemi significativi aperti: ${significant}

## Anomalie

${anomalies}

## Registro completo

<!-- page-audit-registry:start -->
| pagina | tipo di problema | elemento | gravita | correzione | esito |
| ---: | --- | --- | --- | --- | --- |
${rows}
<!-- page-audit-registry:end -->

## Correzioni e riesecuzioni

- Baseline automatica eseguita su ${diagnostics.length} pagine.
- Revisione delle tavole-contatto: in attesa di ispezione completa.
- Riesecuzione finale: in attesa delle correzioni e del controllo conclusivo.
`
}

export function validatePageAuditMarkdown(markdown, expectedPageCount) {
  const failures = []
  const registry = markdown.match(
    /<!-- page-audit-registry:start -->([\s\S]*?)<!-- page-audit-registry:end -->/
  )?.[1] || ""
  const pages = [...registry.matchAll(/^\|\s*(\d+)\s*\|/gm)]
    .map((match) => Number(match[1]))
  const expected = Array.from({ length: expectedPageCount }, (_, index) => index + 1)

  if (JSON.stringify(pages) !== JSON.stringify(expected)) {
    failures.push(`registro pagine non completo: ${pages.length}/${expectedPageCount}`)
  }
  if (/\|\s*aperto\s*\|/i.test(registry)) {
    failures.push("registro con esiti aperti")
  }
  if (!/Riesecuzione finale:\s*conforme/i.test(markdown)) {
    failures.push("riesecuzione finale non registrata come conforme")
  }
  if (!/Tavole-contatto ispezionate:\s*\d+\/\d+/i.test(markdown)) {
    failures.push("ispezione tavole-contatto non registrata")
  }

  return failures
}

function positiveInteger(value, label) {
  const parsed = Number(value)

  if (!Number.isInteger(parsed) || parsed < 1) {
    throw new Error(`${label} non valido: ${value}`)
  }

  return parsed
}

function escapeCell(value) {
  return String(value).replace(/\|/g, "\\|").replace(/\r?\n/g, "<br>")
}
