import { describe, expect, it } from "vitest"
import { backfillCandidateCount, canBackfillBlock } from "@/src/book/pagination"

describe("Book Studio measured backfill", () => {
  it("moves the final continued-table fragments together when both fit", () => {
    expect(backfillCandidateCount({
      availableHeight: 508,
      candidates: [
        { type: "table", continued: true, height: 165 },
        { type: "table", continued: true, height: 40 }
      ]
    })).toBe(2)

    expect(backfillCandidateCount({
      availableHeight: 200,
      candidates: [
        { type: "table", continued: true, height: 165 },
        { type: "table", continued: true, height: 40 }
      ]
    })).toBe(0)
  })

  it("keeps ordinary backfill limited to the first fitting block", () => {
    expect(backfillCandidateCount({
      availableHeight: 260,
      candidates: [
        { type: "paragraph", height: 100 },
        { type: "paragraph", height: 100 }
      ]
    })).toBe(1)
  })

  it("moves a complete block back only when it fits the measured free space", () => {
    expect(canBackfillBlock({ availableHeight: 246, candidateHeight: 110 })).toBe(true)
    expect(canBackfillBlock({ availableHeight: 209, candidateHeight: 246 })).toBe(false)
    expect(canBackfillBlock({ availableHeight: 214, candidateHeight: 217 })).toBe(false)
  })

  it("leaves headings to the dedicated keep-with-next rule", () => {
    expect(canBackfillBlock({
      availableHeight: 180,
      candidateHeight: 25,
      candidateType: "heading",
      followingBlockHeight: 120
    })).toBe(false)
    expect(canBackfillBlock({
      availableHeight: 120,
      candidateHeight: 25,
      candidateType: "heading",
      followingBlockHeight: 120
    })).toBe(false)
  })
})
