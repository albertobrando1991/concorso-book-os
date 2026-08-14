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
          "![Scala profilo](../assets/chapter-01/04-scala-profondita-profilo.png)",
          "",
          "## Note di review",
          "Questa nota è riservata allo staff editoriale e non deve comparire nella preview pubblica."
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/assets/chapter-01/04-scala-profondita-profilo.png"),
        "png"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const volumeOneAlias = await buildBookStudioData(new FileWikiStore(root), "volumi/vol-01")
      const imageBlock = data.chapters[0].blocks.find((block) => block.type === "image")
      const calloutBlock = data.chapters[0].blocks.find((block) => block.type === "callout")

      expect(imageBlock?.path).toBe("books/il-metodo-bando/assets/chapter-01/04-scala-profondita-profilo.png")
      expect(calloutBlock?.calloutType).toBe("warning")
      expect(calloutBlock?.title).toBe("Errore tipico")
      expect(calloutBlock?.text).toContain("priorita operative")
      expect(JSON.stringify(data.chapters[0].blocks)).not.toContain("riservata allo staff editoriale")
      expect(data.assets.map((asset) => asset.path)).toContain(
        "books/il-metodo-bando/assets/chapter-01/04-scala-profondita-profilo.png"
      )
      expect(volumeOneAlias.bookId).toBe("il-metodo-bando")
      expect(volumeOneAlias.chapters.some((chapter) => chapter.isGenerated)).toBe(false)
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
    expect(normalizeAssetPath("raw/assets/books/moduli/m-fl01-comuni-unioni/schema.png")).toBe(
      "raw/assets/books/moduli/m-fl01-comuni-unioni/schema.png"
    )
    expect(normalizeAssetPath("books/moduli/m-fc02-agenzie-fiscali/assets/chapter-01/schema.png")).toBe(
      "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-01/schema.png"
    )
    expect(() => normalizeAssetPath("books/il-metodo-bando/chapters/schema.png")).toThrow("Asset path non valido")
  })

  it("splits long tables as visual continuations without repeating the header", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-table-"))
    const tableRows = Array.from({ length: 15 }, (_, index) => `| Fase ${index + 1} | Azione operativa ${index + 1} | Esito ${index + 1} |`)

    try {
      await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/il-metodo-bando/index.md"),
        "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/tabella-operativa.md"),
        [
          "---",
          "title: Tabella operativa",
          "outline_section: 1",
          "---",
          "# Tabella operativa",
          "",
          "| Fase | Azione | Esito |",
          "| --- | --- | --- |",
          ...tableRows
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const tableBlocks = data.chapters[0].blocks.filter((block) => block.type === "table")

      expect(tableBlocks.length).toBeGreaterThan(1)
      expect(tableBlocks[0].continued).toBeFalsy()
      expect(tableBlocks.slice(1).every((block) => block.continued)).toBe(true)
      expect(tableBlocks.flatMap((block) => block.rows || [])).toHaveLength(15)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("preserves blank workbook rows as real table fields", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-workbook-table-"))

    try {
      await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/il-metodo-bando/index.md"),
        "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/registro-fonti.md"),
        [
          "---",
          "title: Registro fonti",
          "outline_section: 25",
          "---",
          "# Registro fonti",
          "",
          "| Fonte controllata | Ultimo controllo | Azione se cambia |",
          "|---|---|---|",
          "| | | |",
          "| | | |",
          "| | | |"
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const tableBlocks = data.chapters[0].blocks.filter((block) => block.type === "table")
      const rawParagraphs = data.chapters[0].blocks.filter(
        (block) => block.type === "paragraph" && block.text?.includes("|---|")
      )

      expect(tableBlocks).toHaveLength(1)
      expect(tableBlocks[0].headers).toEqual([
        "Fonte controllata",
        "Ultimo controllo",
        "Azione se cambia"
      ])
      expect(tableBlocks[0].rows).toEqual([
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
      ])
      expect(rawParagraphs).toHaveLength(0)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("groups verbose table rows instead of creating sparse one-row pages", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-verbose-table-"))
    const verboseRows = Array.from(
      { length: 8 },
      (_, index) =>
        `| Passaggio ${index + 1} | Descrizione operativa abbastanza articolata da richiedere più righe senza diventare una tabella a una riga per blocco | Esito verificabile ${index + 1} |`
    )

    try {
      await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/il-metodo-bando/index.md"),
        "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/tabella-verbosa.md"),
        [
          "---",
          "title: Tabella verbosa",
          "outline_section: 1",
          "---",
          "# Tabella verbosa",
          "",
          "| Fase | Descrizione | Esito |",
          "| --- | --- | --- |",
          ...verboseRows
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const tableBlocks = data.chapters[0].blocks.filter((block) => block.type === "table")

      expect(tableBlocks).toHaveLength(4)
      expect(tableBlocks.every((block) => block.rows?.length === 2)).toBe(true)
      expect(tableBlocks.flatMap((block) => block.rows || [])).toHaveLength(8)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("splits exceptionally tall table rows to avoid moving an oversized fragment to the next page", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-very-verbose-table-"))
    const veryVerboseRows = Array.from(
      { length: 4 },
      (_, index) =>
        `| Passaggio ${index + 1} | ${"Descrizione operativa molto estesa ".repeat(7)}| Esito verificabile ${index + 1} |`
    )

    try {
      await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/il-metodo-bando/index.md"),
        "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/tabella-molto-verbosa.md"),
        [
          "---",
          "title: Tabella molto verbosa",
          "outline_section: 1",
          "---",
          "# Tabella molto verbosa",
          "",
          "| Fase | Descrizione | Esito |",
          "| --- | --- | --- |",
          ...veryVerboseRows
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const tableBlocks = data.chapters[0].blocks.filter((block) => block.type === "table")

      expect(tableBlocks).toHaveLength(4)
      expect(tableBlocks.every((block) => block.rows?.length === 1)).toBe(true)
      expect(tableBlocks.flatMap((block) => block.rows || [])).toHaveLength(4)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("splits long paragraphs into smaller preview blocks for tighter pagination", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-paragraph-"))
    const longParagraph = Array.from(
      { length: 18 },
      (_, index) =>
        `Periodo ${index + 1} con contenuto editoriale operativo per verificare che la preview A4 possa riempire lo spazio senza spostare un intero blocco alla pagina successiva.`
    ).join(" ")

    try {
      await mkdir(path.join(root, "books/il-metodo-bando/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/il-metodo-bando/index.md"),
        "---\ntitle: Il Metodo BANDO\n---\n# Il Metodo BANDO",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/paragrafo-lungo.md"),
        [
          "---",
          "title: Paragrafo lungo",
          "outline_section: 1",
          "---",
          "# Paragrafo lungo",
          "",
          longParagraph
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const paragraphBlocks = data.chapters[0].blocks.filter((block) => block.type === "paragraph")

      expect(paragraphBlocks.length).toBeGreaterThan(1)
      expect(paragraphBlocks.slice(1).every((block) => block.continued)).toBe(true)
      expect(new Set(paragraphBlocks.map((block) => block.continuationKey)).size).toBe(1)
      expect(paragraphBlocks.map((block) => block.text).join(" ")).toBe(longParagraph)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("keeps M-SA02 quiz questions, options and solutions as separate preview blocks", async () => {
    const data = await buildBookStudioData(
      new FileWikiStore(path.resolve(process.cwd(), "wiki")),
      "moduli/m-sa02-professioni-sanitarie"
    )
    const chapter = data.chapters.find((item) => item.path.endsWith("03-discipline-professionali-autonomia-responsabilita.md"))
    const quizIndex = chapter?.blocks.findIndex((block) => block.type === "heading" && block.text === "Quiz") ?? -1
    const quizBlocks = chapter?.blocks.slice(quizIndex, quizIndex + 10) || []

    expect(quizIndex).toBeGreaterThanOrEqual(0)
    expect(quizBlocks.map((block) => block.type)).toEqual([
      "heading",
      "paragraph",
      "list",
      "paragraph",
      "paragraph",
      "list",
      "paragraph",
      "paragraph",
      "list",
      "paragraph"
    ])
    expect(quizBlocks[1]?.text).toBe("1. Quale coppia è corretta?")
    expect(quizBlocks[2]?.items).toEqual([
      "A. OSS — albo professionale ordinistico.",
      "B. TPALL — prevenzione, vigilanza e controllo nei limiti delle attribuzioni.",
      "C. Fisioterapista — competenza generale su ogni bisogno assistenziale.",
      "D. Ostetrica — profilo privo di autonomia."
    ])
    expect(quizBlocks[3]?.text).toMatch(/^Soluzione ragionata: B\./)
  })

  it("loads nested specialist module books", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-module-"))

    try {
      await mkdir(path.join(root, "books/moduli/m-fl01-comuni-unioni/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/moduli/m-fl01-comuni-unioni/index.md"),
        "---\ntitle: M-FL01 - Comuni e Unioni\n---\n# M-FL01",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fl01-comuni-unioni/chapters/00-piano-editoriale.md"),
        [
          "---",
          "title: Piano editoriale - M-FL01 Comuni e Unioni",
          "outline_section: 0",
          "---",
          "# Piano editoriale",
          "",
          "Questo modulo contiene testo sufficiente per essere caricato come libro annidato nel Book Studio."
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fl01-comuni-unioni/chapters/01-capitolo.md"),
        [
          "---",
          "title: Capitolo destinato al lettore",
          "type: book_chapter",
          "outline_section: 1",
          "status: draft",
          "---",
          "# Capitolo destinato al lettore",
          "",
          "Questo testo reale deve essere caricato nel Book Studio senza il piano editoriale interno."
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "moduli/m-fl01-comuni-unioni")

      expect(data.bookId).toBe("moduli/m-fl01-comuni-unioni")
      expect(data.title).toBe("M-FL01 - Comuni e Unioni")
      expect(data.chapters.map((chapter) => chapter.path)).toEqual([
        "books/moduli/m-fl01-comuni-unioni/chapters/01-capitolo.md"
      ])
      expect(data.summary.structure).toBe(0)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("generates a chapter-only analytical index for specialist modules", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-module-index-"))

    try {
      await mkdir(path.join(root, "books/moduli/m-fc01-ministeri/front-matter"), { recursive: true })
      await mkdir(path.join(root, "books/moduli/m-fc01-ministeri/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/moduli/m-fc01-ministeri/index.md"),
        "---\ntitle: M-FC01 - Ministeri\n---\n# M-FC01",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc01-ministeri/front-matter/06-indice.md"),
        [
          "---",
          "title: Indice",
          "type: front_matter",
          "outline_section: FM6",
          "front_matter_layout: analytical-index",
          "index_detail: chapters-only",
          "---",
          "# Indice"
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc01-ministeri/chapters/01-lavorare-ministeri.md"),
        [
          "---",
          "title: Lavorare nei Ministeri",
          "outline_section: 1",
          "---",
          "# Lavorare nei Ministeri",
          "",
          "Questo capitolo contiene testo sufficiente per essere incluso nell'indice del modulo.",
          "",
          "## N-FC01-01-01 · Competenze e struttura",
          "",
          "Il nucleo in formato 2 deve comparire nell'indice analitico anche quando il front matter conserva il dettaglio chapters-only.",
          "",
          "## Sottosezione da non mostrare",
          "",
          "Questa intestazione non deve produrre una riga 1.1 nell'indice del modulo."
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc01-ministeri/chapters/15-appendici.md"),
        [
          "---",
          "title: Appendici operative",
          "outline_section: A",
          "---",
          "# Appendici operative",
          "",
          "Strumenti finali del modulo con checklist, matrice di lavoro, glossario operativo e materiali da usare durante la revisione del bando."
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "moduli/m-fc01-ministeri")
      const index = data.chapters.find((chapter) => chapter.frontMatterLayout === "analytical-index")
      const chapterLine = index?.blocks.find((block) => block.type === "index-chapter" && block.text === "Lavorare nei Ministeri")
      const appendixLine = index?.blocks.find((block) => block.type === "index-chapter" && block.text === "Appendici operative")
      const nucleusLine = index?.blocks.find((block) => block.type === "index-row" && block.text === "Competenze e struttura")
      const nucleusHeading = data.chapters.find((chapter) => chapter.title === "Lavorare nei Ministeri")
        ?.blocks.find((block) => block.type === "heading" && block.text === "Competenze e struttura")

      expect(nucleusLine?.number).toBe("1.1")
      expect(nucleusHeading?.number).toBe("1.1")
      expect(index?.blocks.some((block) => block.type === "index-row" && block.text === "Sottosezione da non mostrare")).toBe(false)
      expect(chapterLine?.number).toBe("Capitolo 1")
      expect(chapterLine?.path).toBe("books/moduli/m-fc01-ministeri/chapters/01-lavorare-ministeri.md")
      expect(appendixLine?.number).toBe("Appendice A")
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("builds commercial volume previews as one book over internal modules", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-volume-"))

    try {
      await mkdir(path.join(root, "books/moduli/m-fc01-ministeri/front-matter"), { recursive: true })
      await mkdir(path.join(root, "books/moduli/m-fc01-ministeri/chapters"), { recursive: true })
      await mkdir(path.join(root, "books/moduli/m-fc02-agenzie-fiscali/front-matter"), { recursive: true })
      await mkdir(path.join(root, "books/moduli/m-fc02-agenzie-fiscali/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/moduli/m-fc01-ministeri/index.md"),
        "---\ntitle: M-FC01 - Ministeri\n---\n# M-FC01",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc01-ministeri/front-matter/01-servizi.md"),
        [
          "---",
          "title: Servizi digitali inclusi",
          "type: front_matter",
          "outline_section: FM1",
          "---",
          "# Servizi digitali interni da non duplicare nel volume"
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc01-ministeri/chapters/01-ministeri.md"),
        [
          "---",
          "title: Lavorare nei Ministeri",
          "outline_section: 1",
          "status: publication-ready",
          "---",
          "# Lavorare nei Ministeri",
          "",
          "Questo capitolo contiene testo sufficiente per entrare nel volume commerciale completo."
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc02-agenzie-fiscali/index.md"),
        "---\ntitle: M-FC02 - Agenzie fiscali\n---\n# M-FC02",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc02-agenzie-fiscali/front-matter/03-copyright.md"),
        [
          "---",
          "title: Copyright interno",
          "type: front_matter",
          "outline_section: FM3",
          "---",
          "# Copyright interno da non duplicare nel volume"
        ].join("\n"),
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-fc02-agenzie-fiscali/chapters/01-fisco.md"),
        [
          "---",
          "title: Agenzie fiscali e profili",
          "outline_section: 1",
          "status: publication-ready",
          "---",
          "# Agenzie fiscali e profili",
          "",
          "Questo capitolo contiene testo sufficiente per essere mostrato dopo l'apertura modulo."
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "volumi/vol-03")
      const generatedTitles = data.chapters.filter((chapter) => chapter.isGenerated).map((chapter) => chapter.title)
      const index = data.chapters.find((chapter) => chapter.title === "Indice completo")
      const moduleOpening = data.chapters.find((chapter) => chapter.frontMatterLayout === "module-opening")
      const readerChapters = data.chapters.filter((chapter) => chapter.sectionType === "chapter" && !chapter.isGenerated)

      expect(data.bookId).toBe("volumi/vol-03")
      expect(data.title).toBe("VOL-03 — Funzioni centrali, Fisco, Previdenza e Ispettivo")
      expect(generatedTitles.slice(0, 6)).toEqual([
        "Servizi digitali inclusi",
        "Frontespizio",
        "Copyright e note editoriali",
        "Sommario",
        "Premessa",
        "Indice completo"
      ])
      expect(data.chapters.some((chapter) => chapter.path.includes("/front-matter/01-servizi.md"))).toBe(false)
      expect(data.chapters.some((chapter) => chapter.path.includes("/front-matter/03-copyright.md"))).toBe(false)
      expect(index?.blocks.some((block) => block.type === "index-part" && block.number === "M-FC01")).toBe(true)
      expect(index?.blocks.some((block) => block.type === "index-part" && block.number === "M-FC02")).toBe(true)
      expect(moduleOpening?.title).toContain("M-FC01")
      expect(data.chapters.some((chapter) => chapter.title === "Lavorare nei Ministeri")).toBe(true)
      expect(data.chapters.find((chapter) => chapter.title === "Agenzie fiscali e profili")?.volumeModuleCode).toBe("M-FC02")
      expect(readerChapters.map((chapter) => chapter.outlineSection)).toEqual(["1", "2"])
      expect(readerChapters.map((chapter) => chapter.moduleOutlineSection)).toEqual(["1", "1"])
      expect(readerChapters.map((chapter) => chapter.contentState)).toEqual(["written", "written"])
      expect(new Set(readerChapters.map((chapter) => chapter.path)).size).toBe(2)

      const digitalServicesText = data.chapters
        .find((chapter) => chapter.title === "Servizi digitali inclusi")
        ?.blocks.flatMap((block) => [
          block.text || "",
          ...(block.items || []),
          ...(block.headers || []),
          ...(block.rows?.flat() || [])
        ]).join(" ")
      const copyrightText = data.chapters
        .find((chapter) => chapter.title === "Copyright e note editoriali")
        ?.blocks.flatMap((block) => [
          block.text || "",
          ...(block.items || []),
          ...(block.headers || []),
          ...(block.rows?.flat() || [])
        ]).join(" ")
      const prefaceText = data.chapters
        .find((chapter) => chapter.title === "Premessa")
        ?.blocks.flatMap((block) => [
          block.text || "",
          ...(block.items || []),
          ...(block.headers || []),
          ...(block.rows?.flat() || [])
        ]).join(" ")

      expect(digitalServicesText).toContain("è collegato")
      expect(digitalServicesText).toContain("priorità")
      expect(digitalServicesText).not.toContain("prima della pubblicazione")
      expect(copyrightText).toContain("ed è costruito")
      expect(copyrightText).toContain("né aggiornamento automatico")
      expect(copyrightText).not.toContain("pubblicazione definitiva")
      expect(copyrightText).toContain("prima di applicarle a un bando")
      expect(prefaceText).toContain("Percorso specialistico per funzioni centrali generaliste")
      expect(prefaceText).toContain("Usa il bando come selettore")
      expect(prefaceText).not.toContain("La struttura segue una regola precisa")
      expect(prefaceText).not.toContain("senza incontrare di nuovo")
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("renders the approved VOL-08 commercial identity in generated front matter", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-vol-08-identity-"))

    try {
      await mkdir(path.join(root, "books/moduli/m-tr01-ict-trasformazione-digitale/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/moduli/m-tr01-ict-trasformazione-digitale/index.md"),
        "---\ntitle: M-TR01 — ICT e trasformazione digitale\n---\n# M-TR01",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-tr01-ict-trasformazione-digitale/chapters/01-profilo.md"),
        [
          "---",
          "title: Profili ICT nella PA",
          "outline_section: 1",
          "status: publication-ready",
          "---",
          "# Profili ICT nella PA",
          "",
          "Questo capitolo rende disponibile il modulo nel volume commerciale."
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "volumi/vol-08")
      const flattenGeneratedText = (title: string) => data.chapters
        .find((chapter) => chapter.title === title)
        ?.blocks.flatMap((block) => [
          block.text || "",
          ...(block.items || []),
          ...(block.headers || []),
          ...(block.rows?.flat() || [])
        ]).join(" ") || ""
      const titlePageText = flattenGeneratedText("Frontespizio")
      const copyrightText = flattenGeneratedText("Copyright e note editoriali")

      expect(titlePageText).toContain(
        "Manuale specialistico per concorsi pubblici — informatica, cloud, cybersecurity, dati e intelligenza artificiale"
      )
      expect(titlePageText).toContain("Capitale Personale")
      expect(copyrightText).toContain("© 2026 Capitale Personale. Tutti i diritti riservati.")
      expect(copyrightText).toContain("Prima edizione, 2026.")
      expect(`${titlePageText} ${copyrightText}`).not.toMatch(/ISBN\s*[:0-9]/i)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
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
      await writeFile(
        path.join(root, "books/il-metodo-bando/chapters/aggiornare-il-metodo-dopo-il-libro.md"),
        [
          "---",
          "title: Aggiornare il metodo dopo il libro",
          "outline_section: 25",
          "---",
          "# Aggiornare il metodo dopo il libro",
          "",
          "Questo modulo appartiene al ricettario digitale e non deve entrare nella preview del volume principale."
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(new FileWikiStore(root), "il-metodo-bando")
      const index = data.chapters.find((chapter) => chapter.frontMatterLayout === "analytical-index")

      expect(data.chapters[0].sectionType).toBe("front_matter")
      expect(data.chapters[0].title).toBe("Servizi digitali inclusi")
      expect(data.chapters[2].title).toBe("Anatomia del bando")
      const ricettarioChapter = data.chapters.find((chapter) => chapter.outlineSection === "25")

      expect(ricettarioChapter?.bookScope).toBe("ricettario")
      expect(index?.blocks.some((block) => block.type === "index-chapter" && block.text === "Aggiornare il metodo dopo il libro")).toBe(false)
      const indexPart = index?.blocks.find((block) => block.type === "index-part" && block.number === "Parte I")
      const chapterLine = index?.blocks.find((block) => block.type === "index-chapter" && block.text === "Anatomia del bando")
      const row = index?.blocks.find((block) => block.type === "index-row" && block.text === "Lettura del bando")

      expect(indexPart?.text).toBe("Capire il concorso prima di studiare")
      expect(chapterLine?.number).toBe("Capitolo 2")
      expect(chapterLine?.path).toBe("books/il-metodo-bando/chapters/anatomia-del-bando.md")
      expect(chapterLine?.pageNumber).toBe(1)
      expect(row?.number).toBe("2.1")
      expect(row?.pageNumber).toBe(1)
      expect(index?.blocks.some((block) => block.type === "index-row" && block.text === "Requisiti e prove")).toBe(false)
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("preserves nucleus identity and verification semantics", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-nucleus-meta-"))

    try {
      await mkdir(path.join(root, "books/moduli/m-sa02-professioni-sanitarie/chapters"), { recursive: true })
      await writeFile(
        path.join(root, "books/moduli/m-sa02-professioni-sanitarie/index.md"),
        "---\ntitle: M-SA02 - Professioni sanitarie\n---\n# M-SA02",
        "utf8"
      )
      await writeFile(
        path.join(root, "books/moduli/m-sa02-professioni-sanitarie/chapters/05-pilota.md"),
        [
          "---",
          "title: Capitolo pilota",
          "outline_section: 5",
          "---",
          "# Capitolo pilota",
          "",
          "## N-SA02-05-04 · Team e sicurezza",
          "",
          "Questo testo editoriale completo descrive il lavoro del team, la comunicazione professionale e la sicurezza operativa nelle attività sanitarie quotidiane.",
          "",
          "## ▣ Verifica",
          "",
          "1. Domanda di controllo."
        ].join("\n"),
        "utf8"
      )

      const data = await buildBookStudioData(
        new FileWikiStore(root),
        "moduli/m-sa02-professioni-sanitarie"
      )
      const headings = data.chapters[0].blocks.filter((block) => block.type === "heading")

      expect(headings.find((block) => block.nucleusId)?.nucleusId).toBe("N-SA02-05-04")
      expect(headings.find((block) => block.nucleusId)?.number).toBe("5.4")
      expect(headings.find((block) => block.verification)?.text).toBe("▣ Verifica")
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })

  it("maps local nucleus numbers to global volume chapters", async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-volume-nuclei-"))

    try {
      for (const moduleId of ["m-fc01-ministeri", "m-fc02-agenzie-fiscali"]) {
        await mkdir(path.join(root, `books/moduli/${moduleId}/chapters`), { recursive: true })
        await writeFile(
          path.join(root, `books/moduli/${moduleId}/index.md`),
          `---\ntitle: ${moduleId}\n---\n# ${moduleId}`,
          "utf8"
        )
      }

      for (let index = 1; index <= 8; index += 1) {
        const number = String(index).padStart(2, "0")
        await writeFile(
          path.join(root, `books/moduli/m-fc01-ministeri/chapters/${number}-base.md`),
          [
            "---",
            `title: Capitolo ${index}`,
            `outline_section: ${index}`,
            "---",
            `# Capitolo ${index}`,
            "",
            "Questo capitolo contiene materiale editoriale completo e sufficiente per entrare nella preview composita e stabilire la numerazione globale del volume."
          ].join("\n"),
          "utf8"
        )
      }

      const pilotPath = path.join(root, "books/moduli/m-fc02-agenzie-fiscali/chapters/05-pilota.md")
      await writeFile(
        pilotPath,
        [
          "---",
          "title: Capitolo pilota",
          "outline_section: 5",
          "---",
          "# Capitolo pilota",
          "",
          "## N-FC02-05-04 · Nucleo pilota",
          "",
          "Questo nucleo contiene materiale editoriale completo e sufficiente per entrare nella preview e verificare il mapping globale del volume composito."
        ].join("\n"),
        "utf8"
      )

      const store = new FileWikiStore(root)
      const volume = await buildBookStudioData(store, "volumi/vol-03")
      const standalone = await buildBookStudioData(store, "moduli/m-fc02-agenzie-fiscali")
      const volumePilot = volume.chapters.find((chapter) => chapter.title === "Capitolo pilota")
      const volumeNucleus = volumePilot?.blocks.find((block) => block.nucleusId === "N-FC02-05-04")
      const standaloneNucleus = standalone.chapters[0].blocks.find((block) => block.nucleusId === "N-FC02-05-04")
      const index = volume.chapters.find((chapter) => chapter.frontMatterLayout === "analytical-index")
      const row = index?.blocks.find((block) => block.nucleusId === "N-FC02-05-04")

      expect(volumePilot?.outlineSection).toBe("9")
      expect(volumePilot?.moduleOutlineSection).toBe("5")
      expect(volumeNucleus?.number).toBe("9.4")
      expect(standaloneNucleus?.number).toBe("5.4")
      expect(row).toMatchObject({
        type: "index-row",
        number: "9.4",
        nucleusId: "N-FC02-05-04",
        path: volumePilot?.path
      })
    } finally {
      await rm(root, { recursive: true, force: true })
    }
  })
})
