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
  resolveCoverLayers?: () => { panels: number; circuit: number; content: number; spine: number; barcode: number }
  resolveCircuitBand?: () => { topIn: number; bottomIn: number }
  buildVol08CoverHtml?: (input: { pageCount: number }) => string
  parseCmykPam?: (input: Buffer) => { widthPx: number; heightPx: number; pixels: Buffer }
  buildCmykImagePdf?: (input: {
    widthPx: number
    heightPx: number
    widthIn: number
    heightIn: number
    pixels: Buffer
  }) => Buffer
}

async function loadCoverCore(): Promise<CoverCore> {
  return import("../scripts/vol08-kdp-cover-core.mjs").catch(() => ({}))
}

describe("VOL-08 KDP cover", () => {
  it("keeps the circuit visible above panels and below every text layer", async () => {
    const { resolveCoverLayers } = await loadCoverCore()

    expect(resolveCoverLayers, "implementare l'ordine dei livelli della copertina").toBeTypeOf("function")
    const layers = resolveCoverLayers!()

    expect(layers.circuit).toBeGreaterThan(layers.panels)
    expect(layers.content).toBeGreaterThan(layers.circuit)
    expect(layers.spine).toBeGreaterThan(layers.circuit)
    expect(layers.barcode).toBeGreaterThan(layers.content)
  })

  it("confines the circuit to the clear lower-middle band", async () => {
    const { resolveCircuitBand } = await loadCoverCore()

    expect(resolveCircuitBand, "implementare la fascia sicura del reticolo").toBeTypeOf("function")
    const band = resolveCircuitBand!()

    expect(band.topIn).toBeGreaterThanOrEqual(5)
    expect(band.bottomIn).toBeLessThanOrEqual(6.9)
    expect(band.bottomIn - band.topIn).toBeGreaterThanOrEqual(1.5)
  })

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

  it("wraps a CMYK raster in a one-page PDF with the exact physical size", async () => {
    const { parseCmykPam, buildCmykImagePdf } = await loadCoverCore()
    const pam = Buffer.concat([
      Buffer.from("P7\nWIDTH 2\nHEIGHT 1\nDEPTH 4\nMAXVAL 255\nTUPLTYPE CMYK\nENDHDR\n", "ascii"),
      Buffer.from([0, 10, 20, 30, 40, 50, 60, 70])
    ])

    expect(parseCmykPam, "implementare il parser PAM CMYK").toBeTypeOf("function")
    expect(buildCmykImagePdf, "implementare il wrapper PDF DeviceCMYK").toBeTypeOf("function")
    const image = parseCmykPam!(pam)
    const pdf = buildCmykImagePdf!({ ...image, widthIn: 2, heightIn: 1 })
    const structure = pdf.toString("latin1")

    expect(image).toEqual({
      widthPx: 2,
      heightPx: 1,
      pixels: Buffer.from([0, 10, 20, 30, 40, 50, 60, 70])
    })
    expect(pdf.subarray(0, 8).toString("ascii")).toBe("%PDF-1.4")
    expect(structure).toContain("/MediaBox [0 0 144 72]")
    expect(structure).toContain("/Width 2 /Height 1 /ColorSpace /DeviceCMYK")
    expect(structure).toContain("/Count 1")
  })
})
