import { describe, expect, it } from "vitest"
import { classifyPageDiagnostic } from "@/scripts/book-studio-page-audit-core.mjs"

const context = {
  pageCount: 459,
  medianFreeSpace: 78,
  expectedWidth: 6.69 * 96,
  expectedHeight: 9.61 * 96
}

function page(overrides: Record<string, unknown> = {}) {
  return {
    page: 2,
    domIndex: 2,
    title: "Pagina di test",
    chapterPath: "books/moduli/test/chapters/01.md",
    printedNumber: 2,
    sectionType: "chapter",
    frontMatterLayout: "",
    side: "verso" as const,
    width: 6.69 * 96,
    height: 9.61 * 96,
    paddingTop: 18 * 96 / 25.4,
    paddingRight: 23 * 96 / 25.4,
    paddingBottom: 18 * 96 / 25.4,
    paddingLeft: 13 * 96 / 25.4,
    freeSpace: 78,
    fillRatio: 0.8,
    overflow: 0,
    collisions: [],
    tables: [],
    images: [],
    rawMarkdown: [],
    typographyFailures: [],
    headingFailures: [],
    unjustifiedProse: [],
    consecutiveImages: false,
    detachedBlocks: [],
    nextPageStartsWithProtectedHeading: false,
    isFrontMatterContinuation: false,
    isSectionTerminal: false,
    ...overrides
  }
}

describe("large-volume page audit regressions", () => {
  it("does not demand a repeated header on a same-page table fragment", () => {
    const issues = classifyPageDiagnostic(page({
      tables: [{
        label: "table 2",
        continued: true,
        hasHeader: false,
        contained: true,
        firstOnPage: false
      }]
    }), context)

    expect(issues.some((issue) => issue.problemType === "table-header")).toBe(false)
  })

  it("accepts a populated analytical index across multiple pages", () => {
    const issues = classifyPageDiagnostic(page({
      sectionType: "front_matter",
      frontMatterLayout: "analytical-index",
      isFrontMatterContinuation: true
    }), context)

    expect(issues.some((issue) => issue.problemType === "split-index")).toBe(false)
  })
})
