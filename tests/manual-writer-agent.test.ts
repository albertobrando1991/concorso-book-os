import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { ManualWriterAgent } from "@/src/server/agents/manual-writer-agent"
import { FileWikiStore } from "@/src/server/wiki/file-store"

describe("ManualWriterAgent", () => {
  it("filters chapters by nested specialist module book id", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "manual-writer-module-"))

    try {
      await mkdir(path.join(root, "books/moduli/m-fl01-comuni-unioni/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/moduli/m-fl01-comuni-unioni/chapters/00-piano-editoriale.md"),
        [
          "---",
          "title: Piano editoriale - M-FL01 Comuni e Unioni",
          "book_id: m-fl01-comuni-unioni",
          "outline_section: 0",
          "status: structure",
          "---",
          "# Piano editoriale",
          "",
          "Da sviluppare."
        ].join("\n"),
        "utf8"
      )

      const chapters = await new ManualWriterAgent(new FileWikiStore(root)).listChapters(
        "moduli/m-fl01-comuni-unioni"
      )

      expect(chapters).toHaveLength(1)
      expect(chapters[0].bookId).toBe("moduli/m-fl01-comuni-unioni")
      expect(chapters[0].path).toBe("books/moduli/m-fl01-comuni-unioni/chapters/00-piano-editoriale.md")
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })
})
