import { describe, expect, it } from "vitest"
import {
  reconcileIndexPageNumbers,
  type BookStudioPageLike
} from "@/app/components/book-studio-index-pages"
import type { BookStudioChapter, MarkdownBlock } from "@/src/server/book/book-preview"

const chapter = (input: Partial<BookStudioChapter>): BookStudioChapter => ({
  path: "books/volumi/vol-07/front-matter/fm6-indice-completo.md",
  title: "Indice completo",
  outlineSection: "FM6",
  bookScope: "main",
  sectionType: "front_matter",
  frontMatterLayout: "analytical-index",
  indexDetail: "volume-modules",
  status: "generated",
  draftStage: "generated-volume-layout",
  reviewRequired: false,
  topics: [],
  sourceRefs: [],
  wordCount: 0,
  contentState: "written",
  blocks: [],
  ...input
})

describe("Book Studio analytical index pages", () => {
  it("reconciles chapter and nucleus rows against measured pages without mutation", () => {
    const pilotPath = "books/moduli/m-sa02-professioni-sanitarie/chapters/05-pilota.md"
    const indexBlocks: MarkdownBlock[] = [
      { type: "index-chapter", text: "Capitolo pilota", path: pilotPath, pageNumber: 1 },
      {
        type: "index-row",
        text: "Team e sicurezza",
        path: pilotPath,
        nucleusId: "N-SA02-05-04",
        number: "9.4",
        pageNumber: 1
      }
    ]
    const pages: BookStudioPageLike[] = [
      {
        chapter: chapter({ blocks: indexBlocks }),
        blocks: indexBlocks,
        pageNumber: 6
      },
      {
        chapter: chapter({
          path: pilotPath,
          title: "Capitolo pilota",
          outlineSection: "9",
          sectionType: "chapter",
          frontMatterLayout: "",
          blocks: []
        }),
        blocks: [{ type: "paragraph", text: "Apertura" }],
        pageNumber: 41
      },
      {
        chapter: chapter({
          path: pilotPath,
          title: "Capitolo pilota",
          outlineSection: "9",
          sectionType: "chapter",
          frontMatterLayout: "",
          blocks: []
        }),
        blocks: [
          {
            type: "heading",
            text: "Team e sicurezza",
            number: "9.4",
            nucleusId: "N-SA02-05-04"
          }
        ],
        pageNumber: 43
      }
    ]
    const original = structuredClone(pages)
    const reconciled = reconcileIndexPageNumbers(pages)
    const blocks = reconciled[0].blocks

    expect(blocks[0].pageNumber).toBe(41)
    expect(blocks[1].pageNumber).toBe(43)
    expect(pages).toEqual(original)
  })

  it("reconciles legacy numbered headings when no nucleus id exists", () => {
    const legacyPath = "books/il-metodo-bando/chapters/introduzione.md"
    const indexBlocks: MarkdownBlock[] = [
      {
        type: "index-row",
        text: "La promessa del libro",
        path: legacyPath,
        number: "2",
        pageNumber: 1
      }
    ]
    const pages: BookStudioPageLike[] = [
      {
        chapter: chapter({ blocks: indexBlocks }),
        blocks: indexBlocks,
        pageNumber: 6
      },
      {
        chapter: chapter({
          path: legacyPath,
          title: "Perche questo libro e diverso",
          outlineSection: "INTRODUZIONE",
          sectionType: "chapter",
          frontMatterLayout: "",
          blocks: []
        }),
        blocks: [{ type: "heading", text: "La promessa del libro", number: "2" }],
        pageNumber: 557
      }
    ]

    expect(reconcileIndexPageNumbers(pages)[0].blocks[0].pageNumber).toBe(557)
  })

  it("reconciles unnumbered source headings by their text", () => {
    const legacyPath = "books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md"
    const indexBlocks: MarkdownBlock[] = [
      {
        type: "index-row",
        text: "Perché partire dal candidato",
        path: legacyPath,
        number: "1.1",
        pageNumber: 1
      },
      {
        type: "index-row",
        text: "Pubblica amministrazione e attività amministrativa",
        path: legacyPath,
        number: "1.2",
        pageNumber: 2
      }
    ]
    const pages: BookStudioPageLike[] = [
      {
        chapter: chapter({ blocks: indexBlocks }),
        blocks: indexBlocks,
        pageNumber: 8
      },
      {
        chapter: chapter({
          path: legacyPath,
          title: "Il nuovo candidato pubblico",
          outlineSection: "1",
          sectionType: "chapter",
          frontMatterLayout: "",
          blocks: []
        }),
        blocks: [{ type: "heading", text: "Perché partire dal candidato" }],
        pageNumber: 16
      },
      {
        chapter: chapter({
          path: legacyPath,
          title: "Il nuovo candidato pubblico",
          outlineSection: "1",
          sectionType: "chapter",
          frontMatterLayout: "",
          blocks: []
        }),
        blocks: [{ type: "heading", text: "1. Pubblica amministrazione e attività amministrativa" }],
        pageNumber: 17
      }
    ]

    expect(reconcileIndexPageNumbers(pages)[0].blocks[0].pageNumber).toBe(16)
    expect(reconcileIndexPageNumbers(pages)[0].blocks[1].pageNumber).toBe(17)
  })
})
