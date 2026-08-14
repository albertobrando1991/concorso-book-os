import { describe, expect, it } from "vitest"

type CoverGeometry = {
  pageCount: number
  trimWidthIn: number
  trimHeightIn: number
  bleedIn: number
  spineIn: number
  widthIn: number
  heightIn: number
}

type CoverCore = {
  calculateCoverGeometry?: (pageCount: number) => CoverGeometry
  buildVol08CoverHtml?: (input: { pageCount: number }) => string
}

async function loadCoverCore(): Promise<CoverCore> {
  return import("../scripts/vol08-kdp-cover-core.mjs").catch(() => ({}))
}

describe("VOL-08 KDP cover", () => {
  it("derives the KDP wrap geometry from the final page count", async () => {
    const { calculateCoverGeometry } = await loadCoverCore()

    expect(calculateCoverGeometry, "implementare il calcolo geometrico della copertina").toBeTypeOf("function")
    expect(calculateCoverGeometry!(231)).toEqual({
      pageCount: 231,
      trimWidthIn: 6.69,
      trimHeightIn: 9.61,
      bleedIn: 0.125,
      spineIn: 0.520212,
      widthIn: 14.150212,
      heightIn: 9.86
    })
    expect(calculateCoverGeometry!(250).spineIn).toBeCloseTo(0.563, 9)
    expect(calculateCoverGeometry!(250).widthIn).toBeCloseTo(14.193, 9)
  })

  it("rejects page counts that cannot define this paperback cover", async () => {
    const { calculateCoverGeometry } = await loadCoverCore()

    expect(calculateCoverGeometry, "implementare la validazione del conteggio pagine").toBeTypeOf("function")
    expect(() => calculateCoverGeometry!(23)).toThrow("pageCount must be an integer >= 24")
    expect(() => calculateCoverGeometry!(231.5)).toThrow("pageCount must be an integer >= 24")
  })

  it("renders the approved Circuito Civico copy without an embedded ISBN", async () => {
    const { buildVol08CoverHtml } = await loadCoverCore()

    expect(buildVol08CoverHtml, "implementare il canvas HTML della copertina").toBeTypeOf("function")
    const html = buildVol08CoverHtml!({ pageCount: 231 })

    expect(html).toContain("ICT, digitale,")
    expect(html).toContain("cybersecurity")
    expect(html).toContain("e dati")
    expect(html).toContain(
      "Manuale specialistico per concorsi pubblici — informatica, cloud, cybersecurity, dati e intelligenza artificiale"
    )
    expect(html).toContain("Capitale Personale")
    expect(html).toContain("13 capitoli · 82 nuclei · casi applicativi · quiz commentati · laboratorio prove")
    expect(html).toContain("class=\"barcode-safe\"")
    expect(html).not.toMatch(/ISBN\s*[:0-9]/i)
    expect(html).not.toMatch(/crop-mark|template-overlay/i)
  })
})
