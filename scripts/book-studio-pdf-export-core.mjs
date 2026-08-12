export function createPdfExportContract(outputPath) {
  return {
    pageCss: [
      "@page { size: 481.68pt 691.92pt; margin: 0; }",
      "html, body { margin: 0 !important; padding: 0 !important; background: #fff !important; }",
      ".bookPages { display: block !important; margin: 0 !important; padding: 0 !important; gap: 0 !important; }",
      ".bookPage { margin: 0 !important; box-shadow: none !important; border: 0 !important; break-after: page; page-break-after: always; }",
      ".bookPage:last-child { break-after: auto; page-break-after: auto; }"
    ].join("\n"),
    pdfOptions: {
      path: outputPath,
      width: "6.69in",
      height: "9.61in",
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: "0", right: "0", bottom: "0", left: "0" }
    }
  }
}

export function assertBookReady({ pageCount, expectedPageCount, fontsReady, missingImages }) {
  if (pageCount !== expectedPageCount) {
    throw new Error(`Paginazione instabile: attese ${expectedPageCount} pagine, rilevate ${pageCount}.`)
  }
  if (!fontsReady) throw new Error("Font non pronti.")
  if (missingImages) throw new Error(`Immagini non caricate: ${missingImages}.`)
}

export function normalizeKdpTrimBoxes(input) {
  const source = input.toString("latin1")
  let replacements = 0
  const normalized = source.replace(
    /\/(MediaBox|CropBox)\s*\[0 0 481\.91998 691\.91998\]/g,
    (_match, boxType) => {
      replacements += 1
      return `/${boxType} [0 0 481.68000 691.92000]`
    }
  )
  const buffer = Buffer.from(normalized, "latin1")
  if (buffer.length !== input.length) {
    throw new Error("La normalizzazione del trim modificherebbe gli offset del PDF.")
  }
  return { buffer, replacements }
}
