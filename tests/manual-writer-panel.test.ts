import { describe, expect, it } from "vitest"
import { groupChapterOptionsByBook } from "@/app/components/manual-writer-panel"
import type { ChapterOption } from "@/src/server/agents/manual-writer-agent"

describe("ManualWriterPanel chapter options", () => {
  it("groups chapter options by book so the writer select can show every module", () => {
    const chapters: ChapterOption[] = [
      chapter("books/moduli/m-fl03-camere-commercio/chapters/01-camere.md", "Camere", "moduli/m-fl03-camere-commercio", "1"),
      chapter("books/il-metodo-bando/chapters/01-metodo.md", "Metodo", "il-metodo-bando", "1"),
      chapter("books/moduli/m-fl01-comuni-unioni/chapters/02-statuto.md", "Statuto", "moduli/m-fl01-comuni-unioni", "2")
    ]

    expect(groupChapterOptionsByBook(chapters)).toEqual([
      {
        bookId: "il-metodo-bando",
        label: "Il Metodo Bando",
        chapters: [chapters[1]]
      },
      {
        bookId: "moduli/m-fl01-comuni-unioni",
        label: "M-FL01 - Comuni Unioni",
        chapters: [chapters[2]]
      },
      {
        bookId: "moduli/m-fl03-camere-commercio",
        label: "M-FL03 - Camere Commercio",
        chapters: [chapters[0]]
      }
    ])
  })
})

function chapter(path: string, title: string, bookId: string, outlineSection: string): ChapterOption {
  return {
    path,
    title,
    bookId,
    outlineSection,
    status: "revised_draft",
    reviewRequired: true
  }
}
