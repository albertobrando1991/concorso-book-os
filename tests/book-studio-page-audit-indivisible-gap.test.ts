import { describe, expect, it } from "vitest"
import { classifyPageDiagnostic } from "@/scripts/book-studio-page-audit-core.mjs"

const pxPerMm = 96 / 25.4
const context = { pageCount: 459, medianFreeSpace: 78, expectedWidth: 6.69 * 96, expectedHeight: 9.61 * 96 }

function diagnostic(nextFirstBlockHeight: number, nextBackfillCandidateHeight?: number) {
  return {
    page: 104,
    domIndex: 104,
    title: "Pagina di test",
    chapterPath: "books/moduli/test/chapters/01.md",
    printedNumber: 104,
    sectionType: "chapter",
    frontMatterLayout: "",
    side: "verso" as const,
    width: 6.69 * 96,
    height: 9.61 * 96,
    paddingTop: 18 * pxPerMm,
    paddingRight: 23 * pxPerMm,
    paddingBottom: 18 * pxPerMm,
    paddingLeft: 13 * pxPerMm,
    freeSpace: 209,
    fillRatio: 0.6,
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
    nextFirstBlockHeight,
    nextBackfillCandidateHeight,
    isFrontMatterContinuation: false,
    isSectionTerminal: false
  }
}

describe("page-fill with indivisible next block", () => {
  it("does not flag whitespace when the next complete block cannot fit", () => {
    const issues = classifyPageDiagnostic(diagnostic(246), context)
    expect(issues.some((issue) => issue.problemType === "page-fill")).toBe(false)
  })

  it("still flags whitespace when the next complete block would fit", () => {
    const issues = classifyPageDiagnostic(diagnostic(110), context)
    expect(issues.some((issue) => issue.problemType === "page-fill")).toBe(true)
  })

  it("applies the same 22px guard used by rendered backfill", () => {
    expect(classifyPageDiagnostic(diagnostic(188), context)
      .some((issue) => issue.problemType === "page-fill")).toBe(false)
    expect(classifyPageDiagnostic(diagnostic(187), context)
      .some((issue) => issue.problemType === "page-fill")).toBe(true)
  })

  it("uses the atomic height of the final continued pair", () => {
    const issues = classifyPageDiagnostic(diagnostic(110, 230), context)
    expect(issues.some((issue) => issue.problemType === "page-fill")).toBe(false)
  })
})
