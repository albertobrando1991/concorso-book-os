import type { BookStudioChapter, MarkdownBlock } from "@/src/server/book/book-preview"

export interface BookStudioPageLike {
  chapter: BookStudioChapter
  blocks: MarkdownBlock[]
  pageNumber: number
}

function indexTextKey(value: string | undefined) {
  return (value || "")
    .replace(/^\d+\.\s+/, "")
    .trim()
    .replace(/\s+/g, " ")
    .toLocaleLowerCase("it")
}

export function reconcileIndexPageNumbers<T extends BookStudioPageLike>(pages: T[]): T[] {
  const chapterPages = new Map<string, number>()
  const nucleusPages = new Map<string, number>()
  const headingPages = new Map<string, number>()
  const headingTextPages = new Map<string, number>()

  for (const page of pages) {
    if (page.chapter.sectionType === "chapter" && !chapterPages.has(page.chapter.path)) {
      chapterPages.set(page.chapter.path, page.pageNumber)
    }

    for (const block of page.blocks) {
      if (block.type === "heading" && block.nucleusId) {
        nucleusPages.set(`${page.chapter.path}\n${block.nucleusId}`, page.pageNumber)
      }

      if (block.type === "heading" && block.number) {
        headingPages.set(`${page.chapter.path}\n${block.number}`, page.pageNumber)
      }

      if (block.type === "heading" && block.text) {
        const key = `${page.chapter.path}\n${indexTextKey(block.text)}`
        if (!headingTextPages.has(key)) headingTextPages.set(key, page.pageNumber)
      }
    }
  }

  return pages.map((page) => {
    if (page.chapter.frontMatterLayout !== "analytical-index") return page

    return {
      ...page,
      blocks: page.blocks.map((block) => {
        if (block.type === "index-chapter" && block.path) {
          const pageNumber = chapterPages.get(block.path)
          return pageNumber ? { ...block, pageNumber } : block
        }

        if (block.type === "index-row" && block.path) {
          const pageNumber = (
            block.nucleusId
              ? nucleusPages.get(`${block.path}\n${block.nucleusId}`)
              : undefined
          ) || (
            block.number
              ? headingPages.get(`${block.path}\n${block.number}`)
              : undefined
          ) || (
            block.text
              ? headingTextPages.get(`${block.path}\n${indexTextKey(block.text)}`)
              : undefined
          )
          return pageNumber ? { ...block, pageNumber } : block
        }

        return block
      })
    }
  })
}
