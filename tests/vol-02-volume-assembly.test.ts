import path from "node:path"
import { describe, expect, it } from "vitest"
import { TEXT_VOLUME_CATALOG, textVolumeBookId } from "@/src/catalog/text-volumes"
import { buildBookStudioData } from "@/src/server/book/book-preview"
import { FileWikiStore } from "@/src/server/wiki/file-store"

const wikiRoot = path.resolve(process.cwd(), "wiki")

describe("VOL-02 volume assembly", () => {
  it("opens and closes the compiled volume with the authored orientation chapters", async () => {
    const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === "VOL-02")
    expect(volume?.orientationBookId).toBe("vol-02-enti-locali-polizia-locale")

    const store = new FileWikiStore(wikiRoot)
    const data = await buildBookStudioData(store, textVolumeBookId(volume!))
    const mainChapters = data.chapters.filter((chapter) => chapter.sectionType === "chapter")

    expect(mainChapters[0].title).toBe("Come usare VOL-02 insieme a VOL-01")
    expect(mainChapters[0].outlineSection).toBe("1")
    expect(mainChapters[1].title).toBe("Bando Decoder territoriale")
    expect(mainChapters[2].title).toBe("Piano 30/60/90 giorni per VOL-02")

    const lastChapter = mainChapters[mainChapters.length - 1]
    expect(lastChapter.title).toBe("Conclusione — Dal volume al bando")
    expect(Number.parseInt(lastChapter.outlineSection, 10)).toBe(mainChapters.length)
    expect(mainChapters[mainChapters.length - 2].title).toBe("Simulazione finale VOL-02")

    // module chapters sit between the opening and closing chapters, in order
    expect(mainChapters[3].title).toContain("TUEL operativo")
  })

  it("uses the authored preface instead of the generated placeholder", async () => {
    const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === "VOL-02")
    const store = new FileWikiStore(wikiRoot)
    const data = await buildBookStudioData(store, textVolumeBookId(volume!))
    const preface = data.chapters.find((chapter) => chapter.outlineSection === "FM5")
    const prefaceText = preface?.blocks.map((block) => block.text || "").join(" ") || ""

    expect(prefaceText).toContain("Prima di ogni prova confronta sempre questo volume")
    expect(prefaceText).not.toContain("non sono libri separati per il lettore")
  })

  it("lists the opening and closing chapters in the printed index", async () => {
    const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === "VOL-02")
    const store = new FileWikiStore(wikiRoot)
    const data = await buildBookStudioData(store, textVolumeBookId(volume!))
    const index = data.chapters.find((chapter) => chapter.outlineSection === "FM6")
    const indexTexts = index?.blocks.map((block) => block.text || "") || []

    expect(indexTexts).toContain("Apertura del volume")
    expect(indexTexts).toContain("Parte finale")
    expect(indexTexts).toContain("Come usare VOL-02 insieme a VOL-01")
    expect(indexTexts).toContain("Simulazione finale VOL-02")
    expect(indexTexts).toContain("Conclusione — Dal volume al bando")
  })
})
