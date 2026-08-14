import { spawnSync } from "node:child_process"
import { existsSync } from "node:fs"
import { copyFile, mkdir, mkdtemp, readFile, rm } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import process from "node:process"
import { fileURLToPath } from "node:url"
import { chromium } from "@playwright/test"
import { buildVol08CoverHtml, calculateCoverGeometry } from "./vol08-kdp-cover-core.mjs"

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const OUTPUT_DIR = path.join(ROOT, "delivery", "VOL-08", "candidate")
const PDF_PATH = path.join(OUTPUT_DIR, "vol-08-cover-kdp.pdf")
const PREVIEW_PATH = path.join(OUTPUT_DIR, "vol-08-cover-kdp-preview.png")
const FONT_PATHS = Object.freeze({
  arial: "C:\\Windows\\Fonts\\arial.ttf",
  arialBold: "C:\\Windows\\Fonts\\arialbd.ttf",
  garamond: "C:\\Windows\\Fonts\\GARA.TTF"
})

function parsePageCount(argv) {
  const index = argv.indexOf("--page-count")
  if (index < 0) return 231
  const value = Number(argv[index + 1])
  if (!Number.isInteger(value)) throw new Error("--page-count requires an integer")
  return value
}

export function resolveMutoolPath() {
  const candidates = [
    process.env.MUTOOL_PATH,
    "C:\\Program Files (x86)\\bit4id\\namirialsign\\etc\\sign_engine\\mutool.exe"
  ].filter(Boolean)

  for (const candidate of candidates) {
    if (existsSync(candidate)) return candidate
  }

  const located = spawnSync("where.exe", ["mutool"], { encoding: "utf8" })
  if (located.status === 0) {
    const first = located.stdout.split(/\r?\n/).map((item) => item.trim()).find(Boolean)
    if (first && existsSync(first)) return first
  }

  throw new Error("MuPDF mutool not found. Set MUTOOL_PATH to the executable.")
}

function runMutool(mutoolPath, args) {
  const result = spawnSync(mutoolPath, args, { cwd: ROOT, encoding: "utf8" })
  if (result.status !== 0) {
    throw new Error(`mutool failed (${result.status}): ${result.stderr || result.stdout}`)
  }
}

async function loadFonts() {
  for (const fontPath of Object.values(FONT_PATHS)) {
    if (!existsSync(fontPath)) throw new Error(`Required cover font not found: ${fontPath}`)
  }

  const [arial, arialBold, garamond] = await Promise.all([
    readFile(FONT_PATHS.arial),
    readFile(FONT_PATHS.arialBold),
    readFile(FONT_PATHS.garamond)
  ])

  return {
    arial: arial.toString("base64"),
    arialBold: arialBold.toString("base64"),
    garamond: garamond.toString("base64")
  }
}

async function main() {
  const pageCount = parsePageCount(process.argv.slice(2))
  const geometry = calculateCoverGeometry(pageCount)
  const mutoolPath = resolveMutoolPath()
  const fonts = await loadFonts()
  const tempDirectory = await mkdtemp(path.join(os.tmpdir(), "vol08-kdp-cover-"))
  const rgbPdfPath = path.join(tempDirectory, "vol-08-cover-rgb.pdf")
  const cmykPdfPath = path.join(tempDirectory, "vol-08-cover-cmyk.pdf")
  let browser

  try {
    await mkdir(OUTPUT_DIR, { recursive: true })
    browser = await chromium.launch({ headless: true })
    const page = await browser.newPage({
      viewport: {
        width: Math.ceil(geometry.widthIn * 96),
        height: Math.ceil(geometry.heightIn * 96)
      },
      deviceScaleFactor: 1
    })
    await page.setContent(buildVol08CoverHtml({ pageCount, fonts }), { waitUntil: "load" })
    await page.evaluate(async () => {
      await document.fonts.ready
    })
    await page.pdf({
      path: rgbPdfPath,
      width: `${geometry.widthIn}in`,
      height: `${geometry.heightIn}in`,
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: "0", right: "0", bottom: "0", left: "0" }
    })
    await browser.close()
    browser = undefined

    runMutool(mutoolPath, ["draw", "-q", "-F", "pdf", "-c", "cmyk", "-o", cmykPdfPath, rgbPdfPath, "1"])
    await readFile(cmykPdfPath)
    await rm(PDF_PATH, { force: true })
    await rm(PREVIEW_PATH, { force: true })
    await copyFile(cmykPdfPath, PDF_PATH)
    runMutool(mutoolPath, ["draw", "-q", "-F", "png", "-c", "rgb", "-r", "300", "-o", PREVIEW_PATH, PDF_PATH, "1"])

    process.stdout.write(`${JSON.stringify({
      pageCount,
      geometry,
      pdf: path.relative(ROOT, PDF_PATH).replaceAll("\\", "/"),
      preview: path.relative(ROOT, PREVIEW_PATH).replaceAll("\\", "/"),
      mutool: mutoolPath
    }, null, 2)}\n`)
  } finally {
    if (browser) await browser.close()
    await rm(tempDirectory, { recursive: true, force: true })
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((error) => {
    process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`)
    process.exitCode = 1
  })
}
