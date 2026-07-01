import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3010"
const cases = [
  { id: "il-metodo-bando", label: "base", url: `${baseUrl}/?bookId=il-metodo-bando#studio` },
  { id: "moduli/m-fc01-ministeri", label: "m-fc01", url: `${baseUrl}/?bookId=${encodeURIComponent("moduli/m-fc01-ministeri")}#studio` }
]

await fs.mkdir("artifacts", { recursive: true })

const browser = await launchBrowser()
const report = []

try {
  for (const current of cases) {
    const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })
    await page.goto(current.url, { waitUntil: "networkidle" })
    await page.locator("#studio").scrollIntoViewIfNeeded()
    await page.getByRole("button", { name: "Libro", exact: true }).click()
    await page.waitForTimeout(900)
    await page.screenshot({ path: `artifacts/book-studio-${current.label}.png`, fullPage: true })

    const diagnostics = await page.$$eval(".bookPages .bookPage", (pages) => pages.map((bookPage, index) => {
      const pageRect = bookPage.getBoundingClientRect()
      const footer = bookPage.querySelector(".pageFooter")
      const footerRect = footer?.getBoundingClientRect()
      const content = bookPage.querySelector(".frontMatterBlocks, .digitalServicesContent, .previewBlocks")
      const contentRect = content?.getBoundingClientRect()
      const bottomLimit = footerRect ? footerRect.top - 4 : pageRect.bottom - 8
      const overflow = contentRect ? Math.max(0, Math.round(contentRect.bottom - bottomLimit)) : 0
      const elements = Array.from(bookPage.querySelectorAll(".frontMatterBlocks > *, .digitalServicesContent > *, .previewBlocks > *, .pageFooter, .titlePageWordmark, .runningHeader"))
        .filter((element) => {
          const rect = element.getBoundingClientRect()
          return rect.width > 0 && rect.height > 0
        })
        .map((element) => {
          const rect = element.getBoundingClientRect()
          return {
            label: element.className || element.tagName,
            top: rect.top,
            right: rect.right,
            bottom: rect.bottom,
            left: rect.left
          }
        })

      const overlaps = []
      for (let leftIndex = 0; leftIndex < elements.length; leftIndex += 1) {
        for (let rightIndex = leftIndex + 1; rightIndex < elements.length; rightIndex += 1) {
          const left = elements[leftIndex]
          const right = elements[rightIndex]
          const horizontal = Math.min(left.right, right.right) - Math.max(left.left, right.left)
          const vertical = Math.min(left.bottom, right.bottom) - Math.max(left.top, right.top)

          if (horizontal > 4 && vertical > 4) {
            overlaps.push(`${left.label} / ${right.label}`)
          }
        }
      }

      return {
        page: index + 1,
        overflow,
        overlaps
      }
    }))

    report.push({ ...current, diagnostics })
    await page.close()
  }
} finally {
  await browser.close()
}

await fs.writeFile("artifacts/book-studio-layout-report.json", JSON.stringify(report, null, 2), "utf8")

const failures = report.flatMap((entry) =>
  entry.diagnostics
    .filter((page) => page.overflow > 8 || page.overlaps.length > 0)
    .map((page) => `${entry.label} page ${page.page}: overflow=${page.overflow}, overlaps=${page.overlaps.join("; ")}`)
)

if (failures.length > 0) {
  console.error(failures.join("\n"))
  process.exit(1)
}

console.log(`Book Studio layout OK for ${report.map((entry) => entry.label).join(", ")}`)

async function launchBrowser() {
  try {
    return await chromium.launch({ channel: "msedge" })
  } catch {
    try {
      return await chromium.launch({ channel: "chrome" })
    } catch {
      return chromium.launch()
    }
  }
}
