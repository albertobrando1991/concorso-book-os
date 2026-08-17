import { describe, expect, it } from "vitest"
import {
  shouldLoadSourceReader,
  trimBookStudioInitialData,
  trimKnowledgeGraphInitialData
} from "@/src/server/dashboard/initial-payload"
import type { BookStudioChapter, BookStudioData } from "@/src/server/book/book-preview"
import type { KnowledgeGraph } from "@/src/server/wiki/graph"

describe("dashboard initial payload", () => {
  it("keeps the full chapter list but defers preview blocks", () => {
    const data = bookStudioData([
      chapter("books/moduli/m-fl01-comuni-unioni/chapters/01.md", "Primo", ["a"]),
      chapter("books/moduli/m-fl01-comuni-unioni/chapters/02.md", "Secondo", ["b", "c"]),
      chapter("books/moduli/m-fl01-comuni-unioni/chapters/03.md", "Terzo", ["d"])
    ])

    const trimmed = trimBookStudioInitialData(
      data,
      "books/moduli/m-fl01-comuni-unioni/chapters/02.md"
    )

    expect(trimmed.chapters).toHaveLength(3)
    expect(trimmed.chapters[0].blocks).toEqual([])
    expect(trimmed.chapters[1].blocks).toEqual([])
    expect(trimmed.chapters[2].blocks).toEqual([])
  })

  it("does not load a full source reader until a source is explicitly selected", () => {
    expect(shouldLoadSourceReader(undefined)).toBe(false)
    expect(shouldLoadSourceReader("")).toBe(false)
    expect(shouldLoadSourceReader("sources/test.md")).toBe(true)
  })

  it("limits the initial knowledge graph to visible nodes and internal links", () => {
    const graph: KnowledgeGraph = {
      nodes: [
        { id: "book", label: "Book", path: "books/book.md", type: "book" },
        { id: "chapter-1", label: "Chapter 1", path: "books/book/chapters/01.md", type: "chapter" },
        { id: "chapter-2", label: "Chapter 2", path: "books/book/chapters/02.md", type: "chapter" },
        { id: "topic", label: "Topic", path: "topics/topic.md", type: "topic" }
      ],
      links: [
        { source: "book", target: "chapter-1", kind: "frontmatter" },
        { source: "chapter-1", target: "chapter-2", kind: "wikilink" },
        { source: "chapter-2", target: "topic", kind: "wikilink" }
      ]
    }

    const trimmed = trimKnowledgeGraphInitialData(graph, { nodeLimit: 3, linkLimit: 2 })
    const nodeIds = new Set(trimmed.nodes.map((node) => node.id))

    expect(trimmed.nodes).toHaveLength(3)
    expect(trimmed.links).toHaveLength(2)
    expect(trimmed.links.every((link) => nodeIds.has(link.source) && nodeIds.has(link.target))).toBe(true)
  })
})

function bookStudioData(chapters: BookStudioChapter[]): BookStudioData {
  return {
    bookId: "volumi/vol-02",
    title: "VOL-02",
    footerTitle: "VOL-02",
    updatedAt: "2026-07-21T00:00:00.000Z",
    summary: {
      chapters: chapters.length,
      mainChapters: chapters.length,
      ricettarioModules: 0,
      written: chapters.length,
      draft: 0,
      structure: 0,
      reviewRequired: 0,
      assets: 0
    },
    chapters,
    assets: [],
    editorialPlan: null
  }
}

function chapter(path: string, title: string, text: string[]): BookStudioChapter {
  return {
    path,
    title,
    outlineSection: "1",
    bookScope: "main",
    sectionType: "chapter",
    frontMatterLayout: "",
    indexDetail: "",
    status: "revised_draft",
    draftStage: "professional-draft",
    reviewRequired: false,
    topics: [],
    sourceRefs: [],
    wordCount: text.length,
    contentState: "written",
    blocks: text.map((item) => ({ type: "paragraph", text: item }))
  }
}
