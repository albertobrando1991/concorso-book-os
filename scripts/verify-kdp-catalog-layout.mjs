import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3010"
const volumeIds = Array.from({ length: 12 }, (_, index) => `volumi/vol-${String(index + 1).padStart(2, "0")}`)
const report = []

const browser = await launchBrowser()

try {
  for (const bookId of volumeIds) {
    const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })
    const url = `${baseUrl}/?bookId=${encodeURIComponent(bookId)}#studio`

    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 180_000 })
    await page.locator("#studio").scrollIntoViewIfNeeded()
    await page.getByRole("button", { name: "Libro", exact: true }).click()
    await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 180_000 })
    await page.evaluate(() => document.fonts.ready)
    await page.waitForTimeout(1_200)

    const result = await page.$$eval(".bookPages .bookPage", (pages) => pages.map((bookPage, index) => {
      const footer = bookPage.querySelector(".pageFooter")
      const content = bookPage.querySelector(".previewBlocks, .frontMatterBlocks, .digitalServicesContent")
      const footerTop = footer?.getBoundingClientRect().top ?? bookPage.getBoundingClientRect().bottom
      const contentBottom = content?.getBoundingClientRect().bottom ?? bookPage.getBoundingClientRect().top

      return {
        page: index + 1,
        overflow: Math.max(0, Math.round(contentBottom - footerTop))
      }
    }))

    report.push({ bookId, pages: result.length, overflowPages: result.filter((item) => item.overflow > 8) })
    await page.close()
  }
} finally {
  await browser.close()
}

await fs.mkdir("artifacts", { recursive: true })
await fs.writeFile("artifacts/kdp-catalog-layout-report.json", JSON.stringify(report, null, 2), "utf8")

const failures = report.flatMap((entry) => entry.overflowPages.map((page) => `${entry.bookId} page ${page.page}: overflow ${page.overflow}px`))

if (failures.length > 0) {
  console.error(failures.join("\n"))
  process.exit(1)
}

console.log(JSON.stringify(report.map(({ bookId, pages }) => ({ bookId, pages })), null, 2))

async function launchBrowser() {
  try {
    return await chromium.launch({ channel: "msedge" })
  } catch {
    return chromium.launch()
  }
}
