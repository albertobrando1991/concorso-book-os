import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3010"
const data = await fetch(`${baseUrl}/api/book-studio?bookId=il-metodo-bando`).then(async (response) => {
  if (!response.ok) throw new Error(`Book Studio API: ${response.status}`)
  return response.json()
})
const chapters = data.chapters.filter((chapter) => chapter.bookScope === "ricettario")
const startIndex = Number.parseInt(process.env.RICETTARIO_START || "0", 10) || 0
const endIndex = Number.parseInt(process.env.RICETTARIO_END || `${chapters.length}`, 10) || chapters.length
const selectedChapters = chapters.slice(startIndex, endIndex)
const outputPath = `artifacts/ricettario-layout-audit/report-${startIndex}-${Math.min(endIndex, chapters.length)}.json`
const report = []

const browser = await launchBrowser()
const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })

try {
  for (const chapter of selectedChapters) {
    const url = `${baseUrl}/?bookId=il-metodo-bando&chapterPath=${encodeURIComponent(chapter.path)}#studio`

    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 180_000 })
    await page.locator("#studio").scrollIntoViewIfNeeded()
    await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 180_000 })
    await page.evaluate(() => document.fonts.ready)
    await page.waitForTimeout(700)

    const pages = await page.$$eval(".bookPages .bookPage", (elements) => elements.map((element, index) => {
      const pageRect = element.getBoundingClientRect()
      const footer = element.querySelector(".pageFooter")
      const content = element.querySelector(".previewBlocks, .frontMatterBlocks, .digitalServicesContent")
      const footerTop = footer?.getBoundingClientRect().top ?? pageRect.bottom
      const children = Array.from(content?.children || []).filter((child) => {
        const rect = child.getBoundingClientRect()
        return rect.width > 0 && rect.height > 0
      })
      const contentBottom = Math.max(content?.getBoundingClientRect().bottom ?? pageRect.top, ...children.map((child) => child.getBoundingClientRect().bottom))
      const lastChild = children.at(-1)

      return {
        page: index + 1,
        freeSpace: Math.max(0, Math.round(footerTop - contentBottom)),
        overflow: Math.max(0, Math.round(contentBottom - footerTop)),
        lastBlock: lastChild?.tagName || "none",
        lastBlockClass: typeof lastChild?.className === "string" ? lastChild.className : ""
      }
    }))

    for (const pageResult of pages.filter((item) => item.overflow > 8)) {
      await page.locator(".bookPages .bookPage").nth(pageResult.page - 1).screenshot({
        path: `artifacts/ricettario-layout-audit/${chapter.outlineSection}-page-${String(pageResult.page).padStart(2, "0")}-overflow.png`
      })
    }

    report.push({ path: chapter.path, title: chapter.title, pages })
    await fs.mkdir("artifacts/ricettario-layout-audit", { recursive: true })
    await fs.writeFile(outputPath, JSON.stringify({ partial: true, chapters: report }, null, 2), "utf8")
  }
} finally {
  await browser.close()
}

const allPages = report.flatMap((chapter) => chapter.pages.map((page) => ({ ...page, chapter: chapter.title, path: chapter.path })))
const nonFinalPages = allPages.filter((page) => page.page < report.find((chapter) => chapter.path === page.path).pages.length)
const result = {
  generatedAt: new Date().toISOString(),
  chapters: report,
  summary: {
    chapterCount: report.length,
    range: `${startIndex}-${Math.min(endIndex, chapters.length)}`,
    pageCount: allPages.length,
    overflowPages: allPages.filter((page) => page.overflow > 8).length,
    nonFinalOver120: nonFinalPages.filter((page) => page.freeSpace > 120).length,
    worst: [...nonFinalPages].sort((left, right) => right.freeSpace - left.freeSpace).slice(0, 20)
  }
}

await fs.mkdir("artifacts/ricettario-layout-audit", { recursive: true })
await fs.writeFile(outputPath, JSON.stringify(result, null, 2), "utf8")
console.log(JSON.stringify(result.summary, null, 2))

async function launchBrowser() {
  try {
    return await chromium.launch({ channel: "msedge" })
  } catch {
    return chromium.launch()
  }
}
