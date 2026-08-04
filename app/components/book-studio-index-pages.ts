import type { BookStudioChapter, MarkdownBlock } from "@/src/server/book/book-preview"

export interface BookStudioPageLike {
  chapter: BookStudioChapter
  blocks: MarkdownBlock[]
  pageNumber: number
}

export function reconcileIndexPageNumbers<T extends BookStudioPageLike>(pages: T[]): T[] {
  const chapterPages = new Map<string, number>()
  const nucleusPages = new Map<string, number>()

  for (const page of pages) {
    if (page.chapter.sectionType === "chapter" && !chapterPages.has(page.chapter.path)) {
      chapterPages.set(page.chapter.path, page.pageNumber)
    }

    for (const block of page.blocks) {
      if (block.type === "heading" && block.nucleusId) {
        nucleusPages.set(`${page.chapter.path}\n${block.nucleusId}`, page.pageNumber)
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

        if (block.type === "index-row" && block.path && block.nucleusId) {
          const pageNumber = nucleusPages.get(`${block.path}\n${block.nucleusId}`)
          return pageNumber ? { ...block, pageNumber } : block
        }

        return block
      })
    }
  })
}
