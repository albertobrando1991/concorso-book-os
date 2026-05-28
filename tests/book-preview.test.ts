import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { buildBookStudioData, normalizeAssetPath } from "@/src/server/book/book-preview"
import { FileWikiStore } from "@/src/server/wiki/file-store"

describe("book preview assets", () => {
  it("resolves chapter-relative image paths to book asset paths", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-"))

    try {
      await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
      await mkdir(path.join(root, "books/il-metodo-bando/assets/chapter-01"), { recursive: true })
      await writeFile(
        path.join(root, "books/il-metodo-bando/index.md"),
        "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md"),
        [
          "---",
          "title: Il nuovo candidato pubblico",
          "outline_section: 1",
          "---",
          "# Il nuovo candidato pubblico",
          "",
          "Questo capitolo contiene un testo editoriale sufficiente per essere mostrato nella preview visuale del Book Studio insieme alle immagini didattiche.",
          "",
          "> [!WARNING]",
          "> **Errore tipico**",
          "> Studiare in ordine di pagina senza trasformare il bando in priorita operative.",
          "",
          "![Scala profilo](../assets/chapter-01/04-scala-profondita-profilo.png)"
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/assets/chapter-01/04-scala-profondita-profilo.png"),
        "png"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const imageBlock = data.chapters[0].blocks.find((block) => block.type === "image")
      const calloutBlock = data.chapters[0].blocks.find((block) => block.type === "callout")

      expect(imageBlock?.path).toBe("books/il-metodo-bando/assets/chapter-01/04-scala-profondita-profilo.png")
      expect(calloutBlock?.calloutType).toBe("warning")
      expect(calloutBlock?.title).toBe("Errore tipico")
      expect(calloutBlock?.text).toContain("priorita operative")
      expect(data.assets.map((asset) => asset.path)).toContain(
        "books/il-metodo-bando/assets/chapter-01/04-scala-profondita-profilo.png"
      )
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("serves raw uploaded assets and editorial book assets only", () => {
    expect(normalizeAssetPath("raw/assets/books/il-metodo-bando/schema.png")).toBe(
      "raw/assets/books/il-metodo-bando/schema.png"
    )
    expect(normalizeAssetPath("books/il-metodo-bando/assets/chapter-01/schema.png")).toBe(
      "books/il-metodo-bando/assets/chapter-01/schema.png"
    )
    expect(() => normalizeAssetPath("books/il-metodo-bando/chapters/schema.png")).toThrow("Asset path non valido")
  })
})
