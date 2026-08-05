import fs from "node:fs/promises"
import path from "node:path"
import { chromium } from "@playwright/test"
import { assertBookReady, createPdfExportContract } from "./book-studio-pdf-export-core.mjs"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3010"
const bookId = process.env.BOOK_STUDIO_BOOK_ID || "volumi/vol-07"
const expectedPageCount = Number.parseInt(process.env.BOOK_STUDIO_EXPECTED_PAGES || "394", 10)
const outputPath = path.resolve(
  process.env.BOOK_STUDIO_PDF_PATH || "delivery/VOL-07/candidate/vol-07-interior-kdp.pdf"
)
const url = `${baseUrl}/?bookId=${encodeURIComponent(bookId)}#studio`
const contract = createPdfExportContract(outputPath)

await fs.mkdir(path.dirname(outputPath), { recursive: true })

let browser
try {
  browser = await chromium.launch({ channel: "msedge" })
} catch {
  try {
    browser = await chromium.launch({ channel: "chrome" })
  } catch {
    browser = await chromium.launch()
  }
}

const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })

try {
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 180_000 })
  await page.locator("#studio").waitFor({ state: "visible", timeout: 120_000 })
  await page.getByRole("button", { name: "Libro", exact: true }).click()
  await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 120_000 })
  await page.evaluate(() => document.fonts.ready)
  await page.$$eval(".bookPages img", async (images) => {
    for (const image of images) image.loading = "eager"
    await Promise.all(images.map(async (image) => {
      if (!image.complete) {
        await new Promise((resolve) => {
          image.addEventListener("load", resolve, { once: true })
          image.addEventListener("error", resolve, { once: true })
        })
      }
      await image.decode?.().catch(() => undefined)
    }))
  })
  await page.waitForFunction(
    (expected) => document.querySelectorAll(".bookPages .bookPage").length === expected,
    expectedPageCount,
    { timeout: 120_000 }
  )
  await page.waitForTimeout(2_000)

  const readiness = await page.evaluate(() => ({
    pageCount: document.querySelectorAll(".bookPages .bookPage").length,
    fontsReady: document.fonts.status === "loaded",
    missingImages: Array.from(document.querySelectorAll(".bookPages img"))
      .filter((image) => !image.complete || image.naturalWidth < 1).length
      + document.querySelectorAll(".bookPages .missingAsset").length
  }))
  assertBookReady({ ...readiness, expectedPageCount })

  await page.evaluate(() => {
    const pages = document.querySelector(".bookPages")
    if (!pages) throw new Error("Contenitore .bookPages assente.")
    document.body.replaceChildren(pages)
  })
  await page.addStyleTag({ content: contract.pageCss })
  await page.emulateMedia({ media: "print" })
  await page.pdf(contract.pdfOptions)

  const stat = await fs.stat(outputPath)
  console.log(JSON.stringify({
    ok: true,
    bookId,
    outputPath,
    pageCount: readiness.pageCount,
    bytes: stat.size
  }, null, 2))
} finally {
  await browser.close()
}
