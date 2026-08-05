export interface PdfExportContract {
  pageCss: string
  pdfOptions: {
    path: string
    width: "6.69in"
    height: "9.61in"
    printBackground: true
    preferCSSPageSize: true
    margin: { top: "0"; right: "0"; bottom: "0"; left: "0" }
  }
}

export interface BookReadiness {
  pageCount: number
  expectedPageCount: number
  fontsReady: boolean
  missingImages: number
}

export function createPdfExportContract(outputPath: string): PdfExportContract
export function assertBookReady(input: BookReadiness): void
