# VOL-07 Step 20 Page-by-Page Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and run a repeatable, exhaustive page auditor for the 381-page VOL-07 Book Studio master, correct every blocking or significant defect, and close pipeline step 20 with complete Markdown and PNG evidence.

**Architecture:** A small shared metadata helper makes continuation state observable and keeps repeated-table-header pagination costs consistent between server parsing and client fallback pagination. A pure JavaScript audit core owns configuration, deterministic classification, registry rendering, report validation, and contact-sheet ranges; a separate Playwright entry point owns browser I/O, DOM measurement, PNG capture, and report write/verify modes. The final workflow uses the generated register plus visual inspection of every contact sheet, reruns impacted pages and then all pages, and only accepts the manual pipeline gate after the CLI reports `gate-not-implemented`.

**Tech Stack:** TypeScript 5.7, React 19, Next.js 15, Node.js 20 ESM, Playwright 1.49, Vitest 2.1, Markdown, PowerShell, LocalAgentMemory, ConcorsoBook OS pipeline CLI.

## Global Constraints

- Work directly on `main`, preserve all pre-existing worktree changes, and stage only files named in the current task.
- Read and obey `wiki/AGENTS.md`; never edit `pipeline/VOL-07/run-state.json` by hand.
- Recall `LocalAgentMemory` before AI output and capture a concise VOL-07 step-20 trace after the important flow.
- Audit every rendered page, not a sample; expected baseline is 381 pages and final truth is the stable DOM count.
- Keep the approved `Precisione Vitale` visual system; do not introduce a new aesthetic or new editorial imagery.
- KDP master remains 6.69 x 9.61 inches, one column, no bleed, mirrored margins with 23 mm inside, 13 mm outside, and 18 mm top/bottom.
- Body copy remains Garamond 11 pt with 1.18 line height; headings remain Arial Bold at 20/14/12 pt; tables and tools remain Arial 9.5-10 pt.
- Overflow above 8 px, collisions, broken assets, raw Markdown, orphan headings, bad page numbering, wrong master geometry, missing repeated table headers, wrong typography, and unjustified prose are blocking.
- Continued paragraph fragments under three visual lines, unexplained near-empty internal pages, abnormal whitespace, detached boxes, and recto/verso inconsistency are significant.
- Title/front-matter pages, module openings, and terminal section pages retain the approved whitespace exceptions, but never bypass mechanical checks.
- Flag whitespace candidates at `max(180 px, median nonterminal free space + 120 px)` or when usable fill is below 35%; visual review decides whether a candidate is defective.
- Produce Markdown and PNG evidence only: no PDF and no JSON deliverable for step 20.
- Produce `ceil(pageCount / 20)` ordered contact sheets and individual original-resolution PNGs only for pages with automatic or visual findings.
- Finish with zero unresolved blocking or significant issues, complete page numbering, matching registry/DOM counts, passing typecheck/tests, and a clean `git diff --check` for scoped changes.

## File Structure

- Create `src/server/book/book-preview-block-metadata.ts`: shared, framework-free continuation/header metadata and table-header cost.
- Modify `src/server/book/book-preview.ts`: charge repeated table headers in server-side cost estimation.
- Modify `app/components/book-studio-panel.tsx`: expose block diagnostics on every rendered root and repeat `<thead>` for continued table fragments.
- Create `tests/book-studio-block-metadata.test.ts`: behavior tests for metadata and continued table headers.
- Create `scripts/book-studio-page-audit-core.mjs`: environment options, classification, registry/report rendering, report validation, and contact-sheet ranges; no browser or filesystem I/O.
- Create `tests/book-studio-page-audit-core.test.ts`: pure unit and contract tests for all blocking/significant rules and evidence counts.
- Create `scripts/verify-book-studio-page-audit.mjs`: Playwright orchestration, exhaustive DOM diagnostics, contact sheets, flagged-page screenshots, and report write/verify modes.
- Create `wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md`: canonical step-20 report and 381-row final registry.
- Generate `artifacts/vol-07-step-20-contact-01-pages-001-020.png` through the final contact sheet and `artifacts/vol-07-step-20-page-NNN.png` only for flagged pages; do not stage artifacts unless repository policy explicitly requires it.

---

### Task 1: Establish the pure audit contract

**Files:**
- Create: `scripts/book-studio-page-audit-core.mjs`
- Create: `tests/book-studio-page-audit-core.test.ts`

**Interfaces:**
- Produces: `resolvePageAuditOptions(env): PageAuditOptions`.
- Produces: `buildContactSheetRanges(pageCount, sheetSize): Array<{ index: number; start: number; end: number; pages: number[] }>`.
- Produces: `classifyPageDiagnostic(page, context): PageAuditIssue[]`.
- Produces: `buildPageRegistryRows(diagnostics, issues): PageRegistryRow[]`.
- Produces: `renderPageAuditMarkdown(input): string`.
- Produces: `validatePageAuditMarkdown(markdown, expectedPageCount): string[]`.
- Consumed by: Tasks 3, 4, and 5.

- [ ] **Step 1: Add failing option and contact-range tests**

```ts
import { describe, expect, it } from "vitest"
import {
  buildContactSheetRanges,
  resolvePageAuditOptions
} from "@/scripts/book-studio-page-audit-core.mjs"

describe("VOL-07 page audit options", () => {
  it("resolves stable VOL-07 defaults and explicit verification pages", () => {
    expect(resolvePageAuditOptions({
      BOOK_STUDIO_URL: "http://127.0.0.1:3010",
      BOOK_STUDIO_AUDIT_PAGES: "7,19,381",
      BOOK_STUDIO_AUDIT_REPORT_MODE: "verify"
    })).toEqual({
      baseUrl: "http://127.0.0.1:3010",
      bookId: "volumi/vol-07",
      artifactPrefix: "vol-07-step-20",
      reportPath: "wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md",
      expectedPageCount: 381,
      contactSheetSize: 20,
      reportMode: "verify",
      explicitScreenshotPages: [7, 19, 381]
    })
  })

  it("covers 381 pages with 20 gapless, non-overlapping sheets", () => {
    const ranges = buildContactSheetRanges(381, 20)
    expect(ranges).toHaveLength(20)
    expect(ranges[0]).toMatchObject({ index: 1, start: 1, end: 20 })
    expect(ranges.at(-1)).toMatchObject({ index: 20, start: 381, end: 381 })
    expect(ranges.flatMap((range) => range.pages)).toEqual(
      Array.from({ length: 381 }, (_, index) => index + 1)
    )
  })
})
```

- [ ] **Step 2: Run the focused test and confirm the missing-module failure**

Run: `npm test -- tests/book-studio-page-audit-core.test.ts`

Expected: FAIL because `scripts/book-studio-page-audit-core.mjs` does not exist.

- [ ] **Step 3: Implement strict options and contact-sheet ranges**

```js
const DEFAULT_REPORT = "wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md"

export function resolvePageAuditOptions(env = process.env) {
  const expectedPageCount = positiveInteger(env.BOOK_STUDIO_EXPECTED_PAGE_COUNT || "381", "expected page count")
  const contactSheetSize = positiveInteger(env.BOOK_STUDIO_CONTACT_SHEET_SIZE || "20", "contact sheet size")
  const reportMode = String(env.BOOK_STUDIO_AUDIT_REPORT_MODE || "write")
  if (!new Set(["write", "verify"]).has(reportMode)) {
    throw new Error(`Modalita report non valida: ${reportMode}`)
  }

  const explicitScreenshotPages = [...new Set(String(env.BOOK_STUDIO_AUDIT_PAGES || "")
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean)
    .map((value) => positiveInteger(value, "screenshot page")))]
    .sort((left, right) => left - right)

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

function positiveInteger(value, label) {
  const parsed = Number(value)
  if (!Number.isInteger(parsed) || parsed < 1) throw new Error(`${label} non valido: ${value}`)
  return parsed
}
```

- [ ] **Step 4: Run the focused tests and confirm they pass**

Run: `npm test -- tests/book-studio-page-audit-core.test.ts`

Expected: PASS, 2 tests.

- [ ] **Step 5: Add failing classification tests**

Create a complete `basePage(overrides)` fixture with compliant geometry and fields for page/DOM number, page side and padding, free space/fill, overflow/collisions, first/last block, tables, images, raw Markdown, typography, justification, consecutive images, detached blocks, and terminal status. Drive blocking cases with:

```ts
it.each([
  ["page-number", { printedNumber: 2 }],
  ["page-size", { width: 620 }],
  ["overflow", { overflow: 9 }],
  ["collision", { collisions: ["paragraph/footer"] }],
  ["raw-markdown", { rawMarkdown: ["| --- | --- |"] }],
  ["typography", { typographyFailures: ["body 12pt"] }],
  ["heading-hierarchy", { headingFailures: ["h3 -> h5"] }],
  ["justification", { unjustifiedProse: ["paragraph 1"] }],
  ["orphan-heading", { lastBlock: { type: "heading", continued: false, lines: 1 } }],
  ["broken-image", { images: [{ label: "figure 1", loaded: false, contained: true, hasCaption: true }] }],
  ["image-caption", { images: [{ label: "figure 1", loaded: true, contained: true, hasCaption: false }] }],
  ["table-header", { tables: [{ label: "table 1", continued: true, hasHeader: false, contained: true }] }]
])("classifies %s as blocking", (problemType, overrides) => {
  expect(classifyPageDiagnostic(basePage(overrides), context)).toEqual(expect.arrayContaining([
    expect.objectContaining({ problemType, severity: "bloccante", outcome: "aperto" })
  ]))
})
```

Add focused assertions that a continued two-line edge paragraph returns `widow-orphan / media`, a nonterminal page over the whitespace threshold returns `page-fill / media`, and the same whitespace on a terminal or title page is exempt.

- [ ] **Step 6: Run the test and confirm classification exports are missing**

Run: `npm test -- tests/book-studio-page-audit-core.test.ts`

Expected: FAIL because classification and report functions are not exported yet.

- [ ] **Step 7: Implement normalized classification and exceptions**

Use a single issue factory and deterministic rule order:

```js
export function classifyPageDiagnostic(page, context) {
  const issues = []
  const add = (problemType, element, severity, correction) => issues.push({
    page: page.page, problemType, element, severity, correction, outcome: "aperto"
  })
  const pxPerMm = 96 / 25.4
  const expectedLeft = page.side === "recto" ? 23 * pxPerMm : 13 * pxPerMm
  const expectedRight = page.side === "recto" ? 13 * pxPerMm : 23 * pxPerMm

  if (page.domIndex !== page.page || page.printedNumber !== page.page) add("page-number", "numero pagina", "bloccante", "riallineare sequenza DOM e footer")
  if (Math.abs(page.width - context.expectedWidth) > 1 || Math.abs(page.height - context.expectedHeight) > 1) add("page-size", "pagina", "bloccante", "ripristinare master 6.69 x 9.61 in")
  if (Math.abs(page.paddingLeft - expectedLeft) > 1 || Math.abs(page.paddingRight - expectedRight) > 1 || Math.abs(page.paddingTop - 18 * pxPerMm) > 1 || Math.abs(page.paddingBottom - 18 * pxPerMm) > 1) add("margins", "padding pagina", "bloccante", "ripristinare margini speculari 23/13/18 mm")
  if (page.overflow > 8) add("overflow", "area contenuto/footer", "bloccante", "ripaginare i blocchi oltre il limite utile")
  page.collisions.forEach((value) => add("collision", value, "bloccante", "separare gli elementi sovrapposti"))
  page.rawMarkdown.forEach((value) => add("raw-markdown", value, "bloccante", "renderizzare la sintassi Markdown"))
  page.typographyFailures.forEach((value) => add("typography", value, "bloccante", "ripristinare la scala tipografica canonica"))
  page.headingFailures.forEach((value) => add("heading-hierarchy", value, "bloccante", "ripristinare la gerarchia progressiva dei titoli"))
  page.unjustifiedProse.forEach((value) => add("justification", value, "bloccante", "applicare giustificazione e regole 3/3"))
  if (page.lastBlock?.type === "heading") add("orphan-heading", "ultimo heading", "bloccante", "tenere il titolo con il blocco successivo")
  page.tables.filter((value) => !value.contained || (value.continued && !value.hasHeader)).forEach((value) => add("table-header", value.label, "bloccante", "ripetere intestazione e contenere la tabella"))
  page.images.filter((value) => !value.loaded || !value.contained).forEach((value) => add("broken-image", value.label, "bloccante", "caricare e contenere immagine e didascalia"))
  page.images.filter((value) => !value.hasCaption).forEach((value) => add("image-caption", value.label, "bloccante", "ripristinare la didascalia associata"))
  if (page.consecutiveImages) add("consecutive-images", "figure consecutive", "bloccante", "separare le figure con contenuto motivante")
  for (const edge of [page.firstBlock, page.lastBlock]) if (edge?.type === "paragraph" && edge.continued && edge.lines < 3) add("widow-orphan", "frammento paragrafo", "media", "ripaginare almeno tre righe insieme")
  page.detachedBlocks.forEach((value) => add("detached-box", value, "media", "tenere box e primo contenuto insieme"))
  const whitespaceLimit = Math.max(180, context.medianFreeSpace + 120)
  const exempt = page.isSectionTerminal || page.sectionType === "front_matter" || page.frontMatterLayout === "module-opening"
  if (!exempt && (page.freeSpace > whitespaceLimit || page.fillRatio < 0.35)) add("page-fill", "area utile", "media", "verificare ritmo e ripaginare il vuoto anomalo")
  return issues
}
```

- [ ] **Step 8: Add and implement report/registry contracts**

Test that each diagnostic appears in the registry, a conforming page becomes:

```text
| 1 | nessuno | pagina | nessuna | nessuna | conforme |
```

Implement registry grouping without `Map.groupBy` so Node 20.11 remains supported:

```js
export function buildPageRegistryRows(diagnostics, issues) {
  const byPage = new Map()
  for (const issue of issues) byPage.set(issue.page, [...(byPage.get(issue.page) || []), issue])
  return diagnostics.map((page) => {
    const pageIssues = byPage.get(page.page) || []
    if (pageIssues.length === 0) return {
      page: page.page,
      problemType: "nessuno",
      element: "pagina",
      severity: "nessuna",
      correction: "nessuna",
      outcome: "conforme"
    }
    return {
      page: page.page,
      problemType: pageIssues.map((issue) => issue.problemType).join("<br>"),
      element: pageIssues.map((issue) => issue.element).join("<br>"),
      severity: pageIssues.some((issue) => issue.severity === "bloccante") ? "bloccante" : "media",
      correction: pageIssues.map((issue) => issue.correction).join("<br>"),
      outcome: pageIssues.every((issue) => issue.outcome !== "aperto") ? "risolto - ricontrollato" : "aperto"
    }
  })
}
```

The generated report must have canonical review frontmatter, anomaly counts, and markers `<!-- page-audit-registry:start -->` / `<!-- page-audit-registry:end -->`. Render exactly one pipe-table row per returned registry row, escaping literal pipes as `\|`. `validatePageAuditMarkdown()` extracts numeric rows only between those markers, compares the complete page array to `1..expectedPageCount`, rejects any `aperto` outcome, and requires `Tavole-contatto ispezionate: N/N` plus `Riesecuzione finale: conforme`. The write-mode report initially records concrete baseline counts and explicitly says contact-sheet review and final rerun are pending; verify mode rejects that execution state.

- [ ] **Step 9: Run focused checks and commit**

Run: `npm test -- tests/book-studio-page-audit-core.test.ts`

Run: `npm run typecheck`

Expected: both exit 0.

```powershell
git add scripts/book-studio-page-audit-core.mjs tests/book-studio-page-audit-core.test.ts
git commit -m "feat: define page audit contracts"
```

### Task 2: Make continuation semantics observable and correct

**Files:**
- Create: `src/server/book/book-preview-block-metadata.ts`
- Modify: `src/server/book/book-preview.ts:1-20,1273-1318,1370-1375`
- Modify: `app/components/book-studio-panel.tsx:15,969-1110,1531-1579`
- Create: `tests/book-studio-block-metadata.test.ts`

**Interfaces:**
- Produces: `getPreviewBlockMetadata(block): { blockType: string; continued: boolean; showTableHeader: boolean; tableHeaderCost: number }`.
- Consumed by: server table cost estimation, renderer roots, client fallback cost estimation, and Task 3 DOM diagnostics.

- [ ] **Step 1: Write the failing metadata behavior tests**

```ts
import { describe, expect, it } from "vitest"
import { getPreviewBlockMetadata } from "@/src/server/book/book-preview-block-metadata"

describe("Book Studio block metadata", () => {
  it("repeats and charges headers on continued table fragments", () => {
    expect(getPreviewBlockMetadata({
      type: "table",
      continued: true,
      headers: ["Voce", "Regola"]
    })).toEqual({
      blockType: "table",
      continued: true,
      showTableHeader: true,
      tableHeaderCost: 24
    })
  })

  it("exposes paragraph continuation without table presentation", () => {
    expect(getPreviewBlockMetadata({ type: "paragraph", continued: true })).toEqual({
      blockType: "paragraph",
      continued: true,
      showTableHeader: false,
      tableHeaderCost: 0
    })
  })
})
```

- [ ] **Step 2: Run the focused test and confirm the missing-module failure**

Run: `npm test -- tests/book-studio-block-metadata.test.ts`

Expected: FAIL because the metadata module does not exist.

- [ ] **Step 3: Implement the framework-free helper**

```ts
interface PreviewBlockMetadataInput {
  type: string
  continued?: boolean
  headers?: string[]
}

export function getPreviewBlockMetadata(block: PreviewBlockMetadataInput) {
  const showTableHeader = block.type === "table" && (block.headers?.length || 0) > 0

  return {
    blockType: block.type,
    continued: Boolean(block.continued),
    showTableHeader,
    tableHeaderCost: showTableHeader ? 24 : 0
  }
}
```

- [ ] **Step 4: Run the focused test and confirm it passes**

Run: `npm test -- tests/book-studio-block-metadata.test.ts`

Expected: PASS, 2 tests.

- [ ] **Step 5: Wire the helper into server and client pagination**

Import `getPreviewBlockMetadata` in both files. Replace both existing `const headerCost = block.continued ? 0 : 24` branches with:

```ts
const { tableHeaderCost } = getPreviewBlockMetadata(block)
return tableHeaderCost + (block.rows?.length || 0) * 22 + 8
```

This is required in `estimateTableBlockCost()` on the server and the table branch of `estimateBlockCost()` in the client so measured and fallback pagination share the same assumption.

- [ ] **Step 6: Render repeated headers and diagnostic attributes on every block root**

At the start of `PreviewBlock`, compute:

```tsx
const metadata = getPreviewBlockMetadata(block)
const auditAttributes = {
  "data-block-type": metadata.blockType,
  "data-block-continued": metadata.continued ? "true" : undefined
}
```

Spread `auditAttributes` onto the single root returned by every branch: heading, index part/chapter/row/entry, ordered/unordered list, missing-asset paragraph, figure, table wrapper, pre, caption paragraph, aside, and fallback paragraph. In the table branch use `metadata.showTableHeader` and always render `<thead>` when headers exist:

```tsx
<div {...auditAttributes} className={`previewTableWrap${metadata.continued ? " continuedTable" : ""}`}>
  <table className="previewTable">
    {metadata.showTableHeader ? (
      <thead>
        <tr>{(block.headers || []).map((header, index) => <th key={`${header}-${index}`}>{header}</th>)}</tr>
      </thead>
    ) : null}
    <tbody>
      {(block.rows || []).map((row, rowIndex) => (
        <tr key={`${row.join("-")}-${rowIndex}`}>
          {row.map((cell, cellIndex) => (
            <td key={`${cell}-${cellIndex}`}>{cell}</td>
          ))}
        </tr>
      ))}
    </tbody>
  </table>
</div>
```

Do not add wrapper elements; wrappers would change pagination measurements and invalidate direct-child diagnostics.

- [ ] **Step 7: Verify renderer behavior and commit**

Run: `npm test -- tests/book-studio-block-metadata.test.ts tests/book-studio-index-pages.test.ts`

Run: `npm run typecheck`

Expected: all commands exit 0.

```powershell
git add src/server/book/book-preview-block-metadata.ts src/server/book/book-preview.ts app/components/book-studio-panel.tsx tests/book-studio-block-metadata.test.ts
git commit -m "fix: repeat continued table headers"
```

### Task 3: Build the exhaustive Playwright auditor

**Files:**
- Create: `scripts/verify-book-studio-page-audit.mjs`
- Modify: `scripts/book-studio-page-audit-core.mjs`
- Modify: `tests/book-studio-page-audit-core.test.ts`

**Interfaces:**
- Consumes: every Task 1 pure export and Task 2 `data-block-type` / `data-block-continued` DOM attributes.
- Produces: one diagnostic per `.bookPages .bookPage`, ordered contact-sheet PNGs, flagged-page PNGs, and report write/verify behavior.

- [ ] **Step 1: Extend core tests for screenshot selection and report verification**

```ts
it("deduplicates automatic and explicit screenshot pages", () => {
  expect(flaggedPageNumbers([{ page: 9 }, { page: 2 }, { page: 9 }], [7, 2]))
    .toEqual([2, 7, 9])
})

it("rejects an incomplete or unresolved final report", () => {
  const markdown = renderPageAuditMarkdown({
    generatedAt: "2026-08-04T18:00:00+02:00",
    bookId: "volumi/vol-07",
    diagnostics: [basePage()],
    issues: [{
      page: 1,
      problemType: "overflow",
      element: "body",
      severity: "bloccante",
      correction: "ripaginare",
      outcome: "aperto"
    }]
  })
  expect(validatePageAuditMarkdown(markdown, 1)).toEqual(expect.arrayContaining([
    "registro con esiti aperti",
    "riesecuzione finale non registrata come conforme",
    "ispezione tavole-contatto non registrata"
  ]))
})
```

- [ ] **Step 2: Run red, implement selection, and return to green**

Run before implementation: `npm test -- tests/book-studio-page-audit-core.test.ts`

Expected: FAIL because `flaggedPageNumbers` is missing.

```js
export function flaggedPageNumbers(issues, explicitPages = []) {
  return [...new Set([...issues.map((issue) => issue.page), ...explicitPages])]
    .sort((left, right) => left - right)
}
```

Run after implementation: `npm test -- tests/book-studio-page-audit-core.test.ts`

Expected: PASS.

- [ ] **Step 3: Implement startup and stable pagination**

Import `fs/promises`, `chromium`, and all Task 1 functions. Resolve options, create `artifacts`, and open `/?bookId=${encodeURIComponent(bookId)}#studio`. Select the exact `Libro` button; await `.bookPages .bookPage`, `document.fonts.ready`, and every image load/decode outcome. Copy the proven launch fallback and stabilization behavior from `verify-volume01-page-fill.mjs`: Edge, then Chrome, then bundled Chromium; four equal signatures 750 ms apart and a 1.5 s confirmation. Always close the browser in `finally`.

- [ ] **Step 4: Collect one diagnostic for every page in one DOM pass**

Use `page.$$eval(".bookPages .bookPage", ...)`. For each page, inspect visible direct children of `.previewBlocks`, `.frontMatterBlocks`, or `.digitalServicesContent`, plus the footer. Compute:

```js
{
  page: index + 1,
  domIndex: index + 1,
  printedNumber: Number(bookPage.dataset.pageNumber || 0),
  title,
  chapterPath: bookPage.dataset.chapterPath || "",
  sectionType: bookPage.dataset.sectionType || "",
  frontMatterLayout: bookPage.dataset.frontMatterLayout || "",
  side: bookPage.classList.contains("bookPageVerso") ? "verso" : "recto",
  width: pageRect.width,
  height: pageRect.height,
  paddingTop: numberStyle(pageStyle.paddingTop),
  paddingRight: numberStyle(pageStyle.paddingRight),
  paddingBottom: numberStyle(pageStyle.paddingBottom),
  paddingLeft: numberStyle(pageStyle.paddingLeft),
  freeSpace: Math.max(0, Math.round(safeBottom - contentBottom)),
  fillRatio: usableHeight > 0 ? Math.max(0, Math.min(1, usedHeight / usableHeight)) : 0,
  overflow: Math.max(0, Math.round(contentBottom - safeBottom)),
  collisions,
  firstBlock: blockDiagnostic(visibleBlocks[0]),
  lastBlock: blockDiagnostic(visibleBlocks.at(-1)),
  tables,
  images,
  rawMarkdown,
  typographyFailures,
  headingFailures,
  unjustifiedProse,
  consecutiveImages,
  detachedBlocks,
  isSectionTerminal: !nextPage || nextPage.dataset.chapterPath !== bookPage.dataset.chapterPath
}
```

`blockDiagnostic()` returns `type`, `continued`, and visual line count, using `data-block-*` and `Math.max(1, Math.round(rect.height / parseFloat(style.lineHeight)))`. Compare visible body paragraphs, h3/h4/h5, tables, and callouts to the exact font rules in Global Constraints with 0.25 px tolerance. Build `headingFailures` by scanning heading levels across each chapter and flagging every downward jump greater than one level; reset only at a new `data-chapter-path`. Ordinary prose is invalid when `textAlign !== "justify"`, `orphans < 3`, or `widows < 3`; exclude captions, missing-asset messages, and deliberately centered front-matter copy.

Detect raw Markdown only outside `pre`, using paragraphs/list items and `/^\s*\|.*\|\s*$/` or `/^\s*\|?\s*:?-{3,}/`. A table is contained only when its wrapper stays inside the useful content rectangle and above the footer; a continued table has a header only when it contains `thead th`. An image is loaded only when `complete && naturalWidth > 0`; `hasCaption` requires a nonempty `figcaption`; figure/image/caption must all remain inside the useful rectangle. Build collisions only from visible sibling blocks and footer intersections greater than 4 px so nested table/figure elements do not create false positives.

- [ ] **Step 5: Classify and enforce stable structural invariants**

```js
if (diagnostics.length !== expectedPageCount) {
  throw new Error(`Conteggio pagine inatteso: ${diagnostics.length}, atteso ${expectedPageCount}`)
}
const expectedSequence = Array.from({ length: diagnostics.length }, (_, index) => index + 1)
if (JSON.stringify(diagnostics.map((item) => item.printedNumber)) !== JSON.stringify(expectedSequence)) {
  throw new Error("Numerazione pagine non progressiva")
}
const eligibleFreeSpace = diagnostics
  .filter((item) => !item.isSectionTerminal && item.sectionType !== "front_matter")
  .map((item) => item.freeSpace)
const context = {
  pageCount: diagnostics.length,
  medianFreeSpace: median(eligibleFreeSpace),
  expectedWidth: 6.69 * 96,
  expectedHeight: 9.61 * 96
}
const issues = diagnostics.flatMap((item) => classifyPageDiagnostic(item, context))
```

Before writing evidence, reread the page signatures and fail if they differ from the stable signature used for diagnostics.

- [ ] **Step 6: Implement ordered contact sheets without image dependencies**

For each `buildContactSheetRanges()` entry, clone the selected page nodes into a temporary `#bookAuditContactSheet` grid in the browser document. Use four columns, five rows, 12 px gaps, 20 px padding, neutral gray background, and a high z-index. Each wrapper shows `Pagina N`, has original dimensions times `0.205`, and contains a page clone transformed with `scale(0.205)` from top-left.

Assert cloned `data-page-number` values equal `range.pages`, screenshot only the temporary grid, and remove it in `finally`:

```js
const fileName = `${artifactPrefix}-contact-${pad(range.index, 2)}-pages-${pad(range.start, 3)}-${pad(range.end, 3)}.png`
await page.locator("#bookAuditContactSheet").screenshot({ path: `artifacts/${fileName}` })
```

- [ ] **Step 7: Implement flagged screenshots and report modes**

Capture every `flaggedPageNumbers(issues, explicitScreenshotPages)` page:

```js
await page.locator(".bookPages .bookPage").nth(pageNumber - 1).screenshot({
  path: `artifacts/${artifactPrefix}-page-${pad(pageNumber, 3)}.png`
})
```

In `write` mode, write `renderPageAuditMarkdown(...)` to `reportPath`. In `verify` mode, read the existing report and combine `validatePageAuditMarkdown(markdown, diagnostics.length)` with all current blocking/significant issues. Exit 1 and print every failure if either list is nonempty; otherwise print this stdout-only summary:

```js
console.log(JSON.stringify({
  bookId,
  pageCount: diagnostics.length,
  contactSheets: ranges.length,
  screenshotPages,
  blocking: issues.filter((issue) => issue.severity === "bloccante").length,
  significant: issues.filter((issue) => issue.severity === "media").length,
  reportMode
}, null, 2))
```

The entry point must never create a PDF or JSON file.

- [ ] **Step 8: Run static checks and commit**

Run: `node --check scripts/verify-book-studio-page-audit.mjs`

Run: `npm test -- tests/book-studio-page-audit-core.test.ts tests/book-studio-block-metadata.test.ts`

Run: `npm run typecheck`

Expected: all commands exit 0.

```powershell
git add scripts/book-studio-page-audit-core.mjs scripts/verify-book-studio-page-audit.mjs tests/book-studio-page-audit-core.test.ts
git commit -m "feat: add exhaustive Book Studio page audit"
```

### Task 4: Produce and visually review the baseline evidence

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md`
- Generate: `artifacts/vol-07-step-20-contact-*.png`
- Generate when flagged: `artifacts/vol-07-step-20-page-*.png`

**Interfaces:**
- Consumes: Task 3 CLI behavior.
- Produces: baseline registry, all-page visual evidence, and a concrete finding list for Task 5.

- [ ] **Step 1: Verify the repository baseline**

Run: `npm run typecheck`

Run: `npm test`

Expected baseline: typecheck exits 0 and the full suite is green. Record exact file/test counts in the report later.

- [ ] **Step 2: Start Book Studio on the dedicated port**

Run in a persistent terminal:

```powershell
$env:NEXT_TELEMETRY_DISABLED = '1'
npm run dev -- --hostname 127.0.0.1 --port 3010
```

Wait until `http://127.0.0.1:3010` responds and retain the process identifier so only this process is stopped in Task 6.

- [ ] **Step 3: Generate baseline Markdown and PNG evidence**

```powershell
$env:BOOK_STUDIO_URL = 'http://127.0.0.1:3010'
$env:BOOK_STUDIO_BOOK_ID = 'volumi/vol-07'
$env:BOOK_STUDIO_ARTIFACT_PREFIX = 'vol-07-step-20'
$env:BOOK_STUDIO_EXPECTED_PAGE_COUNT = '381'
$env:BOOK_STUDIO_CONTACT_SHEET_SIZE = '20'
$env:BOOK_STUDIO_AUDIT_REPORT_MODE = 'write'
node scripts/verify-book-studio-page-audit.mjs
```

Expected: 381 diagnostics, every page represented in the registry, 20 ordered contact sheets, and individual PNGs for automatically flagged pages. Write mode may report open findings, but it must still produce the complete baseline evidence.

- [ ] **Step 4: Validate artifact coverage mechanically**

```powershell
Get-ChildItem 'artifacts/vol-07-step-20-contact-*.png' | Sort-Object Name | Format-Table Name,Length
Select-String -Path 'wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md' -Pattern '^\|\s*\d+\s*\|' | Measure-Object
```

Expected: 20 nonempty sheets, at least 381 page rows, first sheet 001-020, last sheet 381-381.

- [ ] **Step 5: Inspect every contact sheet in order**

Open all 20 PNGs with the image viewer, in numeric order. For a clean sheet append:

```markdown
- Tavola 01, pagine 1-20: ispezionata; nessuna anomalia visiva aggiuntiva.
```

For a newly observed page, rerun with its number in `BOOK_STUDIO_AUDIT_PAGES`, inspect the original-resolution PNG, and record a concrete finding:

```markdown
- Tavola 07, pagine 121-140: ispezionata; pagina 133, box separato dal primo contenuto, gravita media.
```

Do not mark a sheet reviewed without opening it. The final summary must state `Tavole-contatto ispezionate: 20/20` if the page count remains 381.

- [ ] **Step 6: Apply approved whitespace exceptions explicitly**

Classify each whitespace candidate as terminal section page, title/front-matter page, module opening, or true internal anomaly. Mechanical failures remain open on every page type. Add each true anomaly to the anomaly section and its page registry row with `esito: aperto`.

### Task 5: Correct findings and prove the rerun

**Files:**
- Modify only files causally implicated by Task 4 evidence.
- Create when Task 4 exposes an additional defect: `tests/book-studio-page-audit-regressions.test.ts`
- Modify: `wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md`
- Regenerate: impacted and all-page PNG evidence.

**Interfaces:**
- Consumes: Task 4 automatic and visual findings.
- Produces: zero open blocking/significant issues and an evidence-backed final report.

- [ ] **Step 1: Debug and regression-test each finding**

For each finding, invoke `superpowers:systematic-debugging`, identify the smallest reproducible input, and add a failing Vitest case to the nearest focused test file. Run that single test and require a failure naming the observed behavior. Apply the minimum renderer, paginator, CSS, or content correction; do not refactor unrelated code or edit frozen chapters unless renderer-level correction cannot solve the defect.

The known continued-table defect is already covered by Task 2 and must not become an untested manual CSS change.

- [ ] **Step 2: Rerun each impacted page at original resolution**

Set the comma-separated page numbers in `BOOK_STUDIO_AUDIT_PAGES`, use `BOOK_STUDIO_AUDIT_REPORT_MODE=verify`, and inspect every resulting `page-NNN.png`. Before the report is finalized this run may exit 1 solely because the preserved baseline still contains open outcomes; current DOM findings remain authoritative. If a correction changes page count or chapter boundaries, discard page-specific assumptions and regenerate/reinspect all contact sheets.

- [ ] **Step 3: Commit each independently reviewable correction**

```powershell
git add app/components/book-studio-panel.tsx app/globals.css src/server/book/book-preview.ts tests/book-studio-page-audit-regressions.test.ts
git diff --cached --check
git commit -m "fix: correct VOL-07 page audit finding"
```

Paths with no changes are harmlessly ignored by Git; before committing, `git diff --cached --name-only` must show only the subset actually implicated by the observed finding. If Task 4 finds no additional defect, do not create the regression file and skip this correction commit. Never use `git add .`; never stage unrelated chapters, memory files, artifacts, or run-state changes.

- [ ] **Step 4: Run the complete audit again**

Run the Task 4 command with `BOOK_STUDIO_AUDIT_PAGES` cleared and `BOOK_STUDIO_AUDIT_REPORT_MODE=verify` so the baseline correction history is not overwritten. Before Step 5, a nonzero exit is expected only from still-open report rows; the current DOM portion must show a stable final page count (381 unless a justified pagination correction changes it), `ceil(pageCount / 20)` regenerated sheets, zero current blocking issues, and zero current significant issues.

- [ ] **Step 5: Preserve correction history and finalize the registry**

Edit the report with `apply_patch`. Preserve each baseline issue's original page/type/element/severity, replace the generic correction with the exact applied correction, and set `esito` to `risolto - ricontrollato`. Keep every conforming page's explicit row. Replace pending execution state with:

```markdown
- Tavole-contatto ispezionate: 20/20 (pagine 1-381, senza salti o duplicati).
- Riesecuzione finale: conforme; 381/381 pagine registrate, 0 bloccanti aperti, 0 significativi aperti.
```

If final counts differ, use the actual page and sheet counts.

- [ ] **Step 6: Verify the preserved report against the current DOM**

```powershell
$env:BOOK_STUDIO_AUDIT_REPORT_MODE = 'verify'
node scripts/verify-book-studio-page-audit.mjs
```

Expected: exit 0; registry count equals DOM count; page sequence is complete; automatic checks are green; no registry outcome is `aperto`; visual sheet review and final rerun are recorded.

### Task 6: Complete verification, pipeline gate, memory, and scoped documentation commit

**Files:**
- Modify via CLI only: `pipeline/VOL-07/run-state.json`
- Modify via LocalAgentMemory service only: `wiki/memory/agent/`
- Modify: `wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md`

**Interfaces:**
- Consumes: Task 5 final report and green audit.
- Produces: step 20 completed, next pipeline step 21, durable local-memory trace, and a scoped report commit.

- [ ] **Step 1: Run final repository verification**

Run: `npm run typecheck`

Run: `npm test`

Run:

```powershell
git diff --check -- app/components/book-studio-panel.tsx src/server/book/book-preview.ts src/server/book/book-preview-block-metadata.ts scripts/book-studio-page-audit-core.mjs scripts/verify-book-studio-page-audit.mjs tests/book-studio-block-metadata.test.ts tests/book-studio-page-audit-core.test.ts wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md
```

Expected: every command exits 0. Record exact suite counts and final audit summary in the report.

- [ ] **Step 2: Attempt normal pipeline completion first**

```powershell
npm run pipeline -- complete VOL-07 --step 20 --json
```

Expected documented result: JSON error with code/status `gate-not-implemented` for `page-fill`. Do not infer this from formatted prose and do not use `--accept` before observing the JSON result.

- [ ] **Step 3: Accept the manual gate only after the expected JSON response**

```powershell
npm run pipeline -- complete VOL-07 --step 20 --accept --note "Audit completo sul DOM finale: 381/381 pagine registrate; 20/20 tavole-contatto ispezionate; numerazione continua; zero overflow, collisioni, asset mancanti, residui Markdown, bloccanti o significativi aperti; typecheck e suite completa verdi." --json
```

If final page or sheet counts changed, use the actual counts. Expected: `20:VOL-07` becomes complete.

- [ ] **Step 4: Confirm the canonical next state**

```powershell
npm run pipeline -- status VOL-07 --json
```

Expected: done 165, pending 4, next step 21, unless the CLI reports a different canonical total. JSON is authoritative; never edit run-state manually.

- [ ] **Step 5: Capture the local-memory trace**

Use `LocalAgentMemory.capture` with scope `VOL-07` and route/tag `pipeline-step-20`. Record final page count, contact-sheet count, corrected findings, final issue counts, test/typecheck result, report path, pipeline completion, and next step 21. Do not stage pre-existing memory changes in scoped code/report commits.

- [ ] **Step 6: Commit only the final report**

```powershell
git add wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md
git diff --cached --check
git diff --cached --name-only
git commit -m "docs(vol-07): record page-by-page audit"
```

Expected staged path: only the step-20 report. Leave shared pre-existing changes, generated artifacts, memory files, and run-state untouched unless a separate explicit decision authorizes staging them.

- [ ] **Step 7: Stop the temporary server and hand off**

Stop only the process started in Task 4, using its recorded PID. Report implementation commits, final audit counts, evidence paths, exact test counts, pipeline status, and any remaining uncommitted generated evidence. Do not claim publication readiness: step 21 remains the total editorial review.
