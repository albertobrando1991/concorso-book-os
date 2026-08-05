export function createPdfExportContract(outputPath) {
  return {
    pageCss: [
      "@page { size: 6.69in 9.61in; margin: 0; }",
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
