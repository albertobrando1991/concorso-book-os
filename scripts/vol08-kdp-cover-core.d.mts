export type CoverGeometry = {
  pageCount: number
  trimWidthIn: number
  trimHeightIn: number
  bleedIn: number
  spineIn: number
  widthIn: number
  heightIn: number
}

export type CoverFonts = {
  arial?: string
  arialBold?: string
  garamond?: string
}

export const VOL08_COVER_SPEC: Readonly<{
  code: string
  title: string
  subtitle: string
  author: string
  series: string
  summary: string
  website: string
  palette: Readonly<Record<string, string>>
}>

export function calculateCoverGeometry(pageCount: number): CoverGeometry
export function resolveCoverLayers(): Readonly<{
  panels: number
  circuit: number
  content: number
  spine: number
  barcode: number
}>
export function resolveCircuitBand(): Readonly<{ topIn: number; bottomIn: number }>
export function buildVol08CoverHtml(input: { pageCount: number; fonts?: CoverFonts }): string
export function parseCmykPam(input: Buffer): { widthPx: number; heightPx: number; pixels: Buffer }
export function buildCmykImagePdf(input: {
  widthPx: number
  heightPx: number
  widthIn: number
  heightIn: number
  pixels: Buffer
}): Buffer
