import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises"
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

  it("applies a local humanizer revision without flattening multiline frontmatter", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "manual-writer-humanizer-"))
    const previousMemoryRoot = process.env.AGENT_MEMORY_ROOT
    const previousMemoryEnabled = process.env.AGENT_MEMORY_ENABLED

    try {
      process.env.AGENT_MEMORY_ROOT = path.join(root, "memory", "agent")
      process.env.AGENT_MEMORY_ENABLED = "true"

      await mkdir(path.join(root, "books/test-book/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/test-book/chapters/capitolo.md"),
        [
          "---",
          "title: Capitolo test",
          "book_id: test-book",
          "status: draft",
          "review_required: true",
          "source_refs: [",
          "  \"sources/test-one.md\",",
          "  \"sources/test-two.md\"",
          "]",
          "---",
          "",
          "# Capitolo test",
          "",
          "## Apertura editoriale",
          "",
          "E' importante sottolineare che questo passaggio serve come un elemento cruciale del percorso.",
          "",
          "## Riferimenti consolidati",
          "",
          "- [[sources/test-one]]"
        ].join("\n"),
        "utf8"
      )

      const result = await new ManualWriterAgent(new FileWikiStore(root)).reviseChapter({
        chapterPath: "books/test-book/chapters/capitolo.md",
        provider: "local"
      })
      const updated = await readFile(path.join(root, "books/test-book/chapters/capitolo.md"), "utf8")

      expect(result.writerProvider).toBe("local")
      expect(result.revisionDiff?.changed).toBe(true)
      expect(result.revisionDiff?.additions).toBeGreaterThan(0)
      expect(result.revisionDiff?.deletions).toBeGreaterThan(0)
      expect(result.revisionDiff?.previewLines.some((line) => line.type === "removed" && line.text.includes("serve come"))).toBe(true)
      expect(result.revisionDiff?.previewLines.some((line) => line.type === "added" && line.text.includes("serve da"))).toBe(true)
      expect(updated).toContain("status: revised_draft")
      expect(updated).toContain("draft_stage: humanized-editorial-revision")
      expect(updated).toContain("source_refs: [")
      expect(updated).toContain("\"sources/test-one.md\",")
      expect(updated).toContain("# Capitolo test")
      expect(updated).toContain("questo passaggio serve da un elemento importante")
      expect(updated).not.toContain("serve come")
      expect(updated).not.toContain("cruciale")
    } finally {
      if (previousMemoryRoot === undefined) {
        delete process.env.AGENT_MEMORY_ROOT
      } else {
        process.env.AGENT_MEMORY_ROOT = previousMemoryRoot
      }

      if (previousMemoryEnabled === undefined) {
        delete process.env.AGENT_MEMORY_ENABLED
      } else {
        process.env.AGENT_MEMORY_ENABLED = previousMemoryEnabled
      }

      await rm(root, { recursive: true, force: true })
    }
  })
})
