import { describe, expect, it } from "vitest"
import {
  buildContactSheetRanges,
  buildPageRegistryRows,
  classifyPageDiagnostic,
  flaggedPageNumbers,
  renderPageAuditMarkdown,
  resolvePageAuditOptions,
  validatePageAuditMarkdown
} from "@/scripts/book-studio-page-audit-core.mjs"
import type {
  PageAuditIssue,
  PageDiagnostic
} from "@/scripts/book-studio-page-audit-core.mjs"

const context = {
  pageCount: 381,
  medianFreeSpace: 60,
  expectedWidth: 6.69 * 96,
  expectedHeight: 9.61 * 96
}

function basePage(overrides: Partial<PageDiagnostic> = {}): PageDiagnostic {
  return {
    page: 1,
    domIndex: 1,
    printedNumber: 1,
    title: "Capitolo",
    chapterPath: "moduli/m-sa01-sanita-amministrativa/chapters/01.md",
    sectionType: "chapter",
    frontMatterLayout: "",
    side: "recto",
    width: 6.69 * 96,
    height: 9.61 * 96,
    paddingTop: 18 * 96 / 25.4,
    paddingRight: 13 * 96 / 25.4,
    paddingBottom: 18 * 96 / 25.4,
    paddingLeft: 23 * 96 / 25.4,
    freeSpace: 70,
    fillRatio: 0.8,
    overflow: 0,
    collisions: [],
    firstBlock: { type: "paragraph", continued: false, lines: 8 },
    lastBlock: { type: "paragraph", continued: false, lines: 8 },
    tables: [],
    images: [],
    rawMarkdown: [],
    typographyFailures: [],
    headingFailures: [],
    unjustifiedProse: [],
    consecutiveImages: false,
    detachedBlocks: [],
    isSectionTerminal: false,
    ...overrides
  }
}

describe("VOL-07 page audit options", () => {
  it("resolves stable VOL-07 defaults and explicit verification pages", () => {
    expect(resolvePageAuditOptions({
      BOOK_STUDIO_URL: "http://127.0.0.1:3010",
      BOOK_STUDIO_AUDIT_PAGES: "381,7,19,7",
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

  it("rejects unsupported report modes", () => {
    expect(() => resolvePageAuditOptions({
      BOOK_STUDIO_AUDIT_REPORT_MODE: "append"
    })).toThrow("Modalita report non valida: append")
  })
})

describe("contact sheet coverage", () => {
  it("covers 381 pages with 20 gapless, non-overlapping sheets", () => {
    const ranges = buildContactSheetRanges(381, 20)

    expect(ranges).toHaveLength(20)
    expect(ranges[0]).toEqual({
      index: 1,
      start: 1,
      end: 20,
      pages: Array.from({ length: 20 }, (_, index) => index + 1)
    })
    expect(ranges.at(-1)).toEqual({
      index: 20,
      start: 381,
      end: 381,
      pages: [381]
    })
    expect(ranges.flatMap((range) => range.pages)).toEqual(
      Array.from({ length: 381 }, (_, index) => index + 1)
    )
  })

  it("deduplicates automatic and explicit screenshot pages", () => {
    expect(flaggedPageNumbers([
      { page: 9 },
      { page: 2 },
      { page: 9 }
    ], [7, 2])).toEqual([2, 7, 9])
  })
})

describe("page diagnostic classification", () => {
  it.each([
    ["page-number", { printedNumber: 2 }],
    ["page-size", { width: 620 }],
    ["margins", { paddingLeft: 40 }],
    ["overflow", { overflow: 9 }],
    ["collision", { collisions: ["paragraph/footer"] }],
    ["raw-markdown", { rawMarkdown: ["| --- | --- |"] }],
    ["typography", { typographyFailures: ["body 12pt"] }],
    ["heading-hierarchy", { headingFailures: ["h3 -> h5"] }],
    ["justification", { unjustifiedProse: ["paragraph 1"] }],
    ["orphan-heading", { lastBlock: { type: "heading", continued: false, lines: 1 } }],
    ["broken-image", { images: [{ label: "figure 1", loaded: false, contained: true, hasCaption: true }] }],
    ["image-caption", { images: [{ label: "figure 1", loaded: true, contained: true, hasCaption: false }] }],
    ["table-header", { tables: [{ label: "table 1", continued: true, hasHeader: false, contained: true }] }],
    ["consecutive-images", { consecutiveImages: true }]
  ])("classifies %s as blocking", (problemType, overrides) => {
    const issues = classifyPageDiagnostic(basePage(overrides), context)

    expect(issues).toEqual(expect.arrayContaining([
      expect.objectContaining({
        problemType,
        severity: "bloccante",
        outcome: "aperto"
      })
    ]))
  })

  it("flags a short continued edge fragment as significant", () => {
    const issues = classifyPageDiagnostic(basePage({
      firstBlock: { type: "paragraph", continued: true, lines: 2 }
    }), context)

    expect(issues).toEqual(expect.arrayContaining([
      expect.objectContaining({
        problemType: "widow-orphan",
        severity: "media"
      })
    ]))
  })

  it("flags a detached box as significant", () => {
    const issues = classifyPageDiagnostic(basePage({
      detachedBlocks: ["callout 2"]
    }), context)

    expect(issues).toEqual(expect.arrayContaining([
      expect.objectContaining({
        problemType: "detached-box",
        severity: "media"
      })
    ]))
  })

  it("flags abnormal whitespace only on nonterminal content pages", () => {
    expect(classifyPageDiagnostic(basePage({
      freeSpace: 181,
      fillRatio: 0.34
    }), context)).toEqual(expect.arrayContaining([
      expect.objectContaining({
        problemType: "page-fill",
        severity: "media"
      })
    ]))

    expect(classifyPageDiagnostic(basePage({
      freeSpace: 181,
      fillRatio: 0.34,
      isSectionTerminal: true
    }), context).some((issue: { problemType: string }) => issue.problemType === "page-fill")).toBe(false)

    expect(classifyPageDiagnostic(basePage({
      freeSpace: 181,
      fillRatio: 0.34,
      sectionType: "front_matter",
      frontMatterLayout: "title-page"
    }), context).some((issue: { problemType: string }) => issue.problemType === "page-fill")).toBe(false)
  })

  it("returns no issue for a compliant page", () => {
    expect(classifyPageDiagnostic(basePage(), context)).toEqual([])
  })
})

describe("page registry and Markdown report", () => {
  it("emits exactly one aggregated row for each diagnostic page", () => {
    const diagnostics = [
      basePage(),
      basePage({ page: 2, domIndex: 2, printedNumber: 2, side: "verso", paddingLeft: 13 * 96 / 25.4, paddingRight: 23 * 96 / 25.4 })
    ]
    const issues: PageAuditIssue[] = [
      { page: 2, problemType: "overflow", element: "body", severity: "bloccante", correction: "ripaginare", outcome: "aperto" },
      { page: 2, problemType: "page-fill", element: "area utile", severity: "media", correction: "riequilibrare", outcome: "aperto" }
    ]

    expect(buildPageRegistryRows(diagnostics, issues)).toEqual([
      {
        page: 1,
        problemType: "nessuno",
        element: "pagina",
        severity: "nessuna",
        correction: "nessuna",
        outcome: "conforme"
      },
      {
        page: 2,
        problemType: "overflow<br>page-fill",
        element: "body<br>area utile",
        severity: "bloccante",
        correction: "ripaginare<br>riequilibrare",
        outcome: "aperto"
      }
    ])
  })

  it("renders canonical frontmatter and a marked full-page registry", () => {
    const markdown = renderPageAuditMarkdown({
      generatedAt: "2026-08-04T18:00:00+02:00",
      bookId: "volumi/vol-07",
      diagnostics: [basePage()],
      issues: []
    })

    expect(markdown).toContain("id: review-vol-07-step-20-page-audit")
    expect(markdown).toContain("status: in-progress")
    expect(markdown).toContain("<!-- page-audit-registry:start -->")
    expect(markdown).toContain("| 1 | nessuno | pagina | nessuna | nessuna | conforme |")
    expect(markdown).toContain("<!-- page-audit-registry:end -->")
  })

  it("rejects missing pages, open outcomes, and missing execution evidence", () => {
    const markdown = [
      "<!-- page-audit-registry:start -->",
      "| pagina | tipo di problema | elemento | gravita | correzione | esito |",
      "| ---: | --- | --- | --- | --- | --- |",
      "| 1 | overflow | body | bloccante | ripaginare | aperto |",
      "<!-- page-audit-registry:end -->"
    ].join("\n")

    expect(validatePageAuditMarkdown(markdown, 2)).toEqual([
      "registro pagine non completo: 1/2",
      "registro con esiti aperti",
      "riesecuzione finale non registrata come conforme",
      "ispezione tavole-contatto non registrata"
    ])
  })

  it("accepts a complete resolved registry with recorded visual and final checks", () => {
    const markdown = [
      "Tavole-contatto ispezionate: 1/1",
      "Riesecuzione finale: conforme; 2/2 pagine registrate.",
      "<!-- page-audit-registry:start -->",
      "| pagina | tipo di problema | elemento | gravita | correzione | esito |",
      "| ---: | --- | --- | --- | --- | --- |",
      "| 1 | nessuno | pagina | nessuna | nessuna | conforme |",
      "| 2 | overflow | body | bloccante | ripaginato | risolto - ricontrollato |",
      "<!-- page-audit-registry:end -->"
    ].join("\n")

    expect(validatePageAuditMarkdown(markdown, 2)).toEqual([])
  })
})
