import { describe, expect, it } from "vitest"
import { canBackfillBlock } from "@/src/book/pagination"

describe("Book Studio backfill stability", () => {
  it("does not rebalance ordinary small gaps", () => {
    expect(canBackfillBlock({
      availableHeight: 100,
      candidateHeight: 50
    })).toBe(false)
  })
})
