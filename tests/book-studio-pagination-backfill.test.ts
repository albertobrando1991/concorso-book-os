import { describe, expect, it } from "vitest"
import { canBackfillBlock } from "@/src/book/pagination"

describe("Book Studio measured backfill", () => {
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
