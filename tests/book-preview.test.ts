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

  it("loads front matter before chapters and generates the analytical index", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-front-matter-"))

    try {
      await mkdir(path.join(root, "books/il-metodo-bando/front-matter"), { recursive: true })
      await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/il-metodo-bando/index.md"),
        "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/front-matter/01-servizi.md"),
        [
          "---",
          "title: Servizi digitali inclusi",
          "type: front_matter",
          "outline_section: FM1",
          "front_matter_layout: digital-services",
          "---",
          "# Accedi ai servizi digitali",
          "",
          "Un testo sufficiente per la preview editoriale delle prime pagine del libro.",
          "",
          "![QR](../assets/front-matter/qr.png)"
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/front-matter/06-indice.md"),
        [
          "---",
          "title: Indice",
          "type: front_matter",
          "outline_section: FM6",
          "front_matter_layout: analytical-index",
          "---",
          "# Indice",
          "",
          "Indice generato."
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/anatomia-del-bando.md"),
        [
          "---",
          "title: Anatomia del bando",
          "outline_section: 2",
          "---",
          "# Anatomia del bando",
          "",
          "Questo capitolo contiene testo sufficiente per essere incluso nella preview del libro.",
          "",
          "## Lettura del bando",
          "",
          "Paragrafo operativo.",
          "",
          "### Requisiti e prove",
          "",
          "Sottosezione reale."
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const index = data.chapters.find((chapter) => chapter.frontMatterLayout === "analytical-index")

      expect(data.chapters[0].sectionType).toBe("front_matter")
      expect(data.chapters[0].title).toBe("Servizi digitali inclusi")
      expect(data.chapters[2].title).toBe("Anatomia del bando")
      const indexPart = index?.blocks.find((block) => block.type === "index-part" && block.number === "Parte I")
      const chapterLine = index?.blocks.find((block) => block.type === "index-chapter" && block.text === "Anatomia del bando")
      const row = index?.blocks.find((block) => block.type === "index-row" && block.text === "Lettura del bando")

      expect(indexPart?.text).toBe("Capire il concorso prima di studiare")
      expect(chapterLine?.number).toBe("Capitolo 2")
      expect(chapterLine?.pageNumber).toBe(1)
      expect(row?.number).toBe("2.1")
      expect(row?.pageNumber).toBe(1)
      expect(index?.blocks.some((block) => block.type === "index-row" && block.text === "Requisiti e prove")).toBe(false)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })
})
