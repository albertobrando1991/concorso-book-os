import { describe, expect, it } from "vitest"
import { canBackfillBlock } from "@/src/book/pagination"

describe("Book Studio heading stability", () => {
  it("leaves headings to the dedicated keep-with-next rule", () => {
    expect(canBackfillBlock({
      availableHeight: 300,
      candidateHeight: 25,
      candidateType: "heading",
      followingBlockHeight: 120
    })).toBe(false)
  })
})
