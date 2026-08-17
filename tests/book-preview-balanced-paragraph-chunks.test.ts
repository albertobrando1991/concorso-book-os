import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { buildBookStudioData } from "@/src/server/book/book-preview"
import { FileWikiStore } from "@/src/server/wiki/file-store"

async function paragraphBlocks(paragraph: string) {
  const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-balanced-paragraph-"))

  try {
    await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
    await writeFile(
      path.join(root, "books/il-metodo-bando/index.md"),
      "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
      "utf8"
    )
    await writeFile(
      path.join(root, "books/il-metodo-bando/chapters/paragrafo.md"),
      ["---", "title: Paragrafo", "outline_section: 1", "---", "# Paragrafo", "", paragraph].join("\n"),
      "utf8"
    )

    const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
    return data.chapters[0].blocks.filter((block) => block.type === "paragraph")
  } finally {
    await rm(root, { recursive: true, force: true })
  }
}

describe("book preview paragraph chunks", () => {
  it("keeps a short trailing sentence attached instead of splitting it mid-phrase", async () => {
    const first = [...Array.from({ length: 71 }, () => "parola"), "fine."].join(" ")
    const tail = Array.from({ length: 8 }, () => "coda").join(" ")
    const paragraph = `${first} ${tail}`

    const chunks = await paragraphBlocks(paragraph)

    // La coda non chiude un periodo: spezzarla produrrebbe un blocco che comincia a metà
    // frase, quindi resta unita al blocco precedente.
    expect(chunks).toHaveLength(1)
    expect(chunks.map((block) => block.text).join(" ")).toBe(paragraph)
  })

  it("splits long paragraphs only at sentence boundaries", async () => {
    const sentence = (index: number) =>
      `${Array.from({ length: 45 }, () => `parola${index}`).join(" ")} conclusione numero ${index}.`
    const paragraph = [sentence(1), sentence(2), sentence(3)].join(" ")

    const chunks = await paragraphBlocks(paragraph)

    expect(chunks.length).toBeGreaterThan(1)

    for (const block of chunks) {
      expect((block.text || "").trim()).toMatch(/[.!?]$/)
    }

    expect(chunks.map((block) => block.text).join(" ")).toBe(paragraph)
  })

  it("does not treat an abbreviation as the end of a sentence", async () => {
    const head = Array.from({ length: 70 }, () => "parola").join(" ")
    const paragraph = `${head} secondo il d.lgs. 217 del 2005 la disciplina resta quella indicata dal bando ufficiale della tornata corrente e non va dedotta per analogia.`

    const chunks = await paragraphBlocks(paragraph)

    for (const block of chunks) {
      expect((block.text || "").trim()).not.toMatch(/d\.lgs\.$/)
    }

    expect(chunks.map((block) => block.text).join(" ")).toBe(paragraph)
  })
})
