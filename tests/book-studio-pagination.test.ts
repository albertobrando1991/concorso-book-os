import { describe, expect, it } from "vitest"
import { moveTrailingHeadingToNextPage } from "../src/book/pagination"

describe("Book Studio pagination", () => {
  it("moves a trailing heading to the following page of the same chapter", () => {
    const paragraph = { type: "paragraph" }
    const heading = { type: "heading" }
    const nextParagraph = { type: "paragraph" }
    const pages = [
      { chapter: { path: "chapter.md" }, blocks: [paragraph, heading] },
      { chapter: { path: "chapter.md" }, blocks: [nextParagraph] }
    ]

    expect(moveTrailingHeadingToNextPage(pages)).toEqual([
      { chapter: { path: "chapter.md" }, blocks: [paragraph] },
      { chapter: { path: "chapter.md" }, blocks: [heading, nextParagraph] }
    ])
  })

  it("does not move a heading across a chapter boundary", () => {
    const heading = { type: "heading" }
    const pages = [
      { chapter: { path: "first.md" }, blocks: [heading] },
      { chapter: { path: "second.md" }, blocks: [{ type: "paragraph" }] }
    ]

    expect(moveTrailingHeadingToNextPage(pages)).toEqual(pages)
  })
})
