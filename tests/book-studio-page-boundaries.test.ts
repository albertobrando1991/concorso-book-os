import { describe, expect, it } from "vitest"
import { normalizePageBoundaries } from "@/src/server/book/book-studio-page-boundaries"

const chapter = { path: "chapter.md" }
const page = (blocks: any[]) => ({ chapter, blocks, pageNumber: 0, chapterPageNumber: 0, isFirstPage: false })

describe("Book Studio page boundaries", () => {
  it("moves a trailing heading to the next page of the same chapter", () => {
    const heading = { type: "heading", content: "Titolo" }
    const paragraph = { type: "paragraph", content: "Testo" }
    const result = normalizePageBoundaries([page([{ type: "paragraph" }, heading]), page([paragraph])])
    expect(result[0].blocks.at(-1)?.type).not.toBe("heading")
    expect(result[1].blocks).toEqual([heading, paragraph])
  })

  it("keeps a lone continued final fragment with the preceding page", () => {
    const fragment = { type: "list", continued: true, content: "due righe" }
    const result = normalizePageBoundaries([page([{ type: "paragraph", content: "prima" }, { type: "list", content: "inizio" }]), page([fragment])])
    expect(result).toHaveLength(2)
    expect(result[0].blocks).toHaveLength(1)
    expect(result[1].blocks).toHaveLength(2)
    expect(result[1].pageNumber).toBe(2)
  })

  it("does not move blocks across chapter boundaries", () => {
    const other = { ...page([{ type: "paragraph" }]), chapter: { path: "other.md" } }
    const result = normalizePageBoundaries([page([{ type: "heading" }]), other])
    expect(result[0].blocks).toHaveLength(1)
  })
})
