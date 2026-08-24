import { describe, expect, it } from "vitest"
import { canBackfillBlock, paginationIsEquivalent } from "@/src/book/pagination"

describe("Book Studio backfill stability", () => {
  it("recognizes structurally identical pagination arrays", () => {
    const first = { type: "paragraph" }
    const second = { type: "table", continued: true }
    const baseline = [
      { chapter: { path: "chapter-a.md" }, blocks: [first] },
      { chapter: { path: "chapter-a.md" }, blocks: [second] }
    ]
    const cloned = baseline.map((page) => ({ ...page, blocks: [...page.blocks] }))

    expect(paginationIsEquivalent(cloned, baseline)).toBe(true)
    expect(paginationIsEquivalent([
      { chapter: { path: "chapter-a.md" }, blocks: [first, second] }
    ], baseline)).toBe(false)
  })

  it("does not rebalance ordinary small gaps", () => {
    expect(canBackfillBlock({
      availableHeight: 100,
      candidateHeight: 50
    })).toBe(false)
  })
})
