import { describe, expect, it } from "vitest"

describe("Book Studio PDF export contract", () => {
  it("locks the KDP trim size and removes browser print margins", async () => {
    const module = await import("../scripts/book-studio-pdf-export-core.mjs").catch(() => ({} as Record<string, unknown>))
    const createPdfExportContract = module.createPdfExportContract as undefined | ((outputPath: string) => {
      pageCss: string
      pdfOptions: Record<string, unknown>
    })

    expect(createPdfExportContract, "implementare il contratto di export PDF").toBeTypeOf("function")

    const contract = createPdfExportContract!("delivery/VOL-07/candidate/vol-07-interior-kdp.pdf")
    expect(contract.pageCss).toContain("@page { size: 6.69in 9.61in; margin: 0; }")
    expect(contract.pdfOptions).toEqual({
      path: "delivery/VOL-07/candidate/vol-07-interior-kdp.pdf",
      width: "6.69in",
      height: "9.61in",
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: "0", right: "0", bottom: "0", left: "0" }
    })
  })

  it("blocks export when pagination, fonts, or images are not stable", async () => {
    const module = await import("../scripts/book-studio-pdf-export-core.mjs")
    const assertBookReady = module.assertBookReady as undefined | ((input: {
      pageCount: number
      expectedPageCount: number
      fontsReady: boolean
      missingImages: number
    }) => void)

    expect(assertBookReady, "implementare il gate di stabilità pre-export").toBeTypeOf("function")
    expect(() => assertBookReady!({ pageCount: 394, expectedPageCount: 394, fontsReady: true, missingImages: 0 })).not.toThrow()
    expect(() => assertBookReady!({ pageCount: 393, expectedPageCount: 394, fontsReady: true, missingImages: 0 })).toThrow(
      "Paginazione instabile: attese 394 pagine, rilevate 393."
    )
    expect(() => assertBookReady!({ pageCount: 394, expectedPageCount: 394, fontsReady: false, missingImages: 0 })).toThrow(
      "Font non pronti."
    )
    expect(() => assertBookReady!({ pageCount: 394, expectedPageCount: 394, fontsReady: true, missingImages: 2 })).toThrow(
      "Immagini non caricate: 2."
    )
  })
})
