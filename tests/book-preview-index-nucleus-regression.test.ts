import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { buildBookStudioData } from "@/src/server/book/book-preview"
import { FileWikiStore } from "@/src/server/wiki/file-store"

describe("book preview analytical index", () => {
  it("keeps a canonical nucleus whose title starts with Checklist", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-index-checklist-"))

    try {
      await mkdir(path.join(root, "books/moduli/m-fc02-agenzie-fiscali/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/moduli/m-fc02-agenzie-fiscali/index.md"),
        "---\ntitle: M-FC02 - Agenzie fiscali\n---\n# M-FC02",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc02-agenzie-fiscali/chapters/01-checklist.md"),
        [
          "---",
          "title: Capitolo pilota",
          "outline_section: 1",
          "---",
          "# Capitolo pilota",
          "",
          "## N-FC02-01-01 · Checklist finale di prontezza",
          "",
          "Questo nucleo canonico deve comparire nell'indice anche se il suo titolo descrittivo inizia con la parola Checklist."
        ].join("\n"),
        "utf8"
      )

      const volume = await buildBookStudioData(new FileWikiStore(root), "volumi/vol-03")
      const index = volume.chapters.find((chapter) => chapter.frontMatterLayout === "analytical-index")
      const row = index?.blocks.find((block) => block.nucleusId === "N-FC02-01-01")

      expect(row).toMatchObject({
        type: "index-row",
        nucleusId: "N-FC02-01-01",
        text: "Checklist finale di prontezza"
      })
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })
})
