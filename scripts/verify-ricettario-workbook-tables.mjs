import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3411"
const outputDir = "artifacts/ricettario-layout-audit"
const data = await fetch(`${baseUrl}/api/book-studio?bookId=il-metodo-bando`).then(async (response) => {
  if (!response.ok) throw new Error(`Book Studio API: ${response.status}`)
  return response.json()
})
const chapters = data.chapters.filter((chapter) => chapter.bookScope === "ricettario")
const sourceIssues = []
let tableBlocks = 0
let blankWorkbookRows = 0

for (const chapter of chapters) {
  for (const block of chapter.blocks) {
    if (block.type === "paragraph" && /\|\s*:?-{3,}:?\s*\|/.test(block.text || "")) {
      sourceIssues.push({
        module: `R${Number(chapter.outlineSection) - 24}`,
        title: chapter.title,
        text: block.text
      })
    }

    if (block.type === "table") {
      tableBlocks += 1
      blankWorkbookRows += (block.rows || []).filter((row) => row.every((cell) => !cell)).length
    }
  }
}

const browser = await chromium.launch({ headless: true })
const page = await browser.newPage({ viewport: { width: 1500, height: 1100 } })
const visualIssues = []
let renderedTables = 0
let screenshotSaved = false

try {
  await fs.mkdir(outputDir, { recursive: true })

  for (const chapter of chapters) {
    const url = `${baseUrl}/?bookId=il-metodo-bando&chapterPath=${encodeURIComponent(chapter.path)}#studio`
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 180_000 })
    await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 180_000 })
    await page.evaluate(() => document.fonts.ready)
    await page.waitForFunction(() =>
      Array.from(document.querySelectorAll(".bookPages img")).every(
        (image) => image.complete && image.naturalWidth > 0 && image.naturalHeight > 0
      )
    )
    await page.waitForTimeout(1200)

    const result = await page.evaluate(() => {
      const rawMarkdownParagraphs = Array.from(document.querySelectorAll(".bookPages p"))
        .map((node) => node.textContent || "")
        .filter((text) => /\|\s*:?-{3,}:?\s*\|/.test(text))
      const tables = Array.from(document.querySelectorAll(".bookPages .previewTable"))
      const tableGeometryIssues = tables.flatMap((table, index) => {
        const rect = table.getBoundingClientRect()
        const pageElement = table.closest(".bookPage")
        const pageRect = pageElement?.getBoundingClientRect()
        const footerRect = pageElement?.querySelector(".pageFooter")?.getBoundingClientRect()
        if (
          !pageRect ||
          rect.left < pageRect.left - 2 ||
          rect.right > pageRect.right + 2 ||
          (footerRect && rect.bottom > footerRect.top + 2)
        ) {
          return [{ index, left: rect.left, right: rect.right, bottom: rect.bottom }]
        }
        return []
      })

      return {
        rawMarkdownParagraphs,
        tableCount: tables.length,
        tableGeometryIssues
      }
    })

    renderedTables += result.tableCount
    if (result.rawMarkdownParagraphs.length > 0 || result.tableGeometryIssues.length > 0) {
      visualIssues.push({
        module: `R${Number(chapter.outlineSection) - 24}`,
        title: chapter.title,
        ...result
      })
    }

    if (!screenshotSaved) {
      const header = page.getByRole("columnheader", { name: "Fonte controllata", exact: true })
      if ((await header.count()) > 0) {
        const tablePage = header
          .first()
          .locator(
            "xpath=ancestor::*[contains(concat(' ', normalize-space(@class), ' '), ' bookPage ')]"
          )
          .first()
        await tablePage.screenshot({ path: `${outputDir}/registro-fonti-formattato.png` })
        screenshotSaved = true
      }
    }
  }
} finally {
  await browser.close()
}

const report = {
  generatedAt: new Date().toISOString(),
  chapters: chapters.length,
  tableBlocks,
  blankWorkbookRows,
  renderedTables,
  sourceIssues,
  visualIssues,
  screenshotSaved
}

await fs.writeFile(
  `${outputDir}/workbook-table-report.json`,
  `${JSON.stringify(report, null, 2)}\n`,
  "utf8"
)
console.log(JSON.stringify(report, null, 2))

if (sourceIssues.length > 0 || visualIssues.length > 0 || !screenshotSaved) {
  process.exitCode = 1
}
