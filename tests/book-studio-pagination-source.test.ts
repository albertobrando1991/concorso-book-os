import { readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"

describe("Book Studio overflow refinement", () => {
  it("moves the preceding heading when overflow would leave it orphaned", async () => {
    const source = await readFile(
      path.join(process.cwd(), "app/components/book-studio-panel.tsx"),
      "utf8"
    )

    expect(source).toContain("let moveFromIndex = firstOverflowIndex")
    expect(source).toContain('nextPages[index].blocks[firstOverflowIndex - 1]?.type === "heading"')
    expect(source).toContain("moveFromIndex = firstOverflowIndex - 1")
    expect(source).toContain("splice(moveFromIndex)")
    expect(source).toContain("keepTrailingHeadingsWithNextPage(pages)")
    expect(source).toContain("function keepTrailingHeadingsWithNextPage")
    expect(source).toContain("nextPage.blocks.unshift(trailingHeading)")
    expect(source).toContain("return keepTrailingHeadingsWithNextPage(renumberPreviewPages(nextPages))")
  })
})
