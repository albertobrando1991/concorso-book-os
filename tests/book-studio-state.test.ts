import { describe, expect, it } from "vitest"
import {
  getInitialBookStudioChapterPath,
  reconcileBookStudioPayloadState,
  reconcileSelectedChapterPath
} from "@/app/components/book-studio-state"

const chapters = [
  { path: "books/moduli/m-sa02/chapters/00-piano.md" },
  { path: "books/moduli/m-sa02/chapters/01-mappa.md" }
]

describe("reconcileSelectedChapterPath", () => {
  it("uses an explicit valid path before the current selection", () => {
    expect(reconcileSelectedChapterPath(chapters, chapters[0].path, chapters[1].path)).toBe(chapters[1].path)
  })

  it("preserves the current selection when it still exists", () => {
    expect(reconcileSelectedChapterPath(chapters, chapters[1].path)).toBe(chapters[1].path)
  })

  it("falls back to the first chapter when the selection disappeared", () => {
    expect(reconcileSelectedChapterPath(chapters, "books/removed.md")).toBe(chapters[0].path)
  })

  it("returns an empty path for an empty payload", () => {
    expect(reconcileSelectedChapterPath([], "books/removed.md")).toBe("")
  })

  it("replaces a same-book payload and reconciles a removed selection", () => {
    const originalData = {
      bookId: "volumi/vol-07",
      chapters: [
        { path: "books/volumi/vol-07/chapters/00-piano.md", title: "Piano editoriale" },
        { path: "books/volumi/vol-07/chapters/01-mappa.md", title: "Mappa precedente" }
      ]
    }
    const refreshedData = {
      bookId: "volumi/vol-07",
      chapters: [
        { path: "books/volumi/vol-07/chapters/01-mappa.md", title: "Mappa aggiornata" },
        { path: "books/volumi/vol-07/chapters/02-profili.md", title: "Profili e prove" }
      ]
    }

    const nextState = reconcileBookStudioPayloadState(
      { data: originalData, selectedPath: originalData.chapters[0].path },
      refreshedData
    )

    expect(nextState.data).toBe(refreshedData)
    expect(nextState.data.chapters.map((chapter) => chapter.title)).toEqual(["Mappa aggiornata", "Profili e prove"])
    expect(nextState.selectedPath).toBe(refreshedData.chapters[0].path)
  })
})

describe("getInitialBookStudioChapterPath", () => {
  it("opens a composite volume on its first editorial chapter", () => {
    const volumeChapters = [
      { path: "books/volumi/vol-07/front-matter/fm1.md", isGenerated: true, status: "generated" },
      { path: "books/moduli/m-sa01/chapters/00-piano.md", isGenerated: false, status: "structure" },
      { path: "books/moduli/m-sa02/chapters/01-profili.md", isGenerated: false, status: "editorial_draft" }
    ]

    expect(getInitialBookStudioChapterPath(volumeChapters)).toBe(volumeChapters[2].path)
    expect(getInitialBookStudioChapterPath(volumeChapters, volumeChapters[0].path)).toBe(volumeChapters[0].path)
  })

  it("falls back to a non-generated chapter and then to the first available item", () => {
    const structureOnly = [
      { path: "books/front-matter/fm1.md", isGenerated: true, status: "generated" },
      { path: "books/chapters/00-piano.md", isGenerated: false, status: "structure" }
    ]

    expect(getInitialBookStudioChapterPath(structureOnly)).toBe(structureOnly[1].path)
    expect(getInitialBookStudioChapterPath([structureOnly[0]])).toBe(structureOnly[0].path)
    expect(getInitialBookStudioChapterPath([])).toBe("")
  })
})
