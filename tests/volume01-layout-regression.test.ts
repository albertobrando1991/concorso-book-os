import { readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { renderedPageGuard } from "../src/book/pagination"

const readProjectFile = (relativePath: string) =>
  readFile(path.join(process.cwd(), relativePath), "utf8")

describe("Volume 1 closing chapter and index layout", () => {
  it("keeps long chapter labels in their own header column", async () => {
    const css = await readProjectFile("app/globals.css")
    const component = await readProjectFile("app/components/book-studio-panel.tsx")

    expect(css).toMatch(
      /\.chapterPreviewHeader\s*\{[^}]*grid-template-columns:\s*minmax\(42px,\s*max-content\)\s+minmax\(0,\s*1fr\);/
    )
    expect(css).toMatch(
      /\.chapterNumber\s*\{[^}]*max-width:\s*96px;[^}]*overflow-wrap:\s*anywhere;/
    )
    expect(css).toMatch(
      /\.chapterNumber\[data-long-label="true"\]\s*\{[^}]*font-size:\s*8pt;[^}]*white-space:\s*nowrap;/
    )
    expect(component).toContain(
      "data-long-label={chapter.outlineSection.length > 4 || undefined}"
    )
  })

  it("reserves a print-safe footer gap for analytical index pages", () => {
    expect(renderedPageGuard({
      bookScope: "main",
      frontMatterLayout: "analytical-index"
    })).toBe(24)
  })

  it("keeps long analytical index labels separate from chapter titles", async () => {
    const css = await readProjectFile("app/globals.css")

    expect(css).toMatch(
      /\.indexLine\s*\{[^}]*grid-template-columns:\s*60px\s+minmax\(0,\s*1fr\)\s+minmax\(16px,\s*0\.24fr\)\s+24px;/
    )
    expect(css).toMatch(
      /\.indexChapterLabel\s*\{[^}]*white-space:\s*nowrap;/
    )
  })

  it("does not overlap adjacent fragments of a continued table", async () => {
    const css = await readProjectFile("app/globals.css")

    expect(css).toMatch(
      /\.previewTableWrap\.continuedTable\s*\{[^}]*margin-top:\s*0;/
    )
  })
})
