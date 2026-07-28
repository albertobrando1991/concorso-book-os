import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3411"
const outputDir = "artifacts/ricettario-image-audit"
const data = await fetch(`${baseUrl}/api/book-studio?bookId=il-metodo-bando`).then(async (response) => {
  if (!response.ok) throw new Error(`Book Studio API: ${response.status}`)
  return response.json()
})
const chapters = data.chapters.filter((chapter) => chapter.bookScope === "ricettario")
const browser = await chromium.launch({ headless: true })
const page = await browser.newPage({ viewport: { width: 1500, height: 1100 } })
const report = []

try {
  await fs.mkdir(outputDir, { recursive: true })

  for (const [chapterIndex, chapter] of chapters.entries()) {
    const url = `${baseUrl}/?bookId=il-metodo-bando&chapterPath=${encodeURIComponent(chapter.path)}#studio`
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 180_000 })
    await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 180_000 })
    await page.evaluate(() => document.fonts.ready)
    await page.waitForFunction(() =>
      Array.from(document.querySelectorAll(".bookPages img")).every(
        (image) => image.complete && image.naturalWidth > 0 && image.naturalHeight > 0
      )
    )
    await page.waitForTimeout(1000)

    const result = await page.evaluate(() => {
      const pageElements = Array.from(document.querySelectorAll(".bookPages .bookPage"))
      const images = Array.from(document.querySelectorAll(".bookPages img")).filter((image) =>
        /chapter-(2[5-9]|3[0-9]|4[0-7])/.test(image.getAttribute("src") || "")
      )
      const geometry = images.map((image) => {
        const rect = image.getBoundingClientRect()
        const pageElement = image.closest(".bookPage")
        const pageRect = pageElement?.getBoundingClientRect()
        const footer = pageElement?.querySelector(".pageFooter")
        const footerRect = footer?.getBoundingClientRect()
        return {
          src: image.getAttribute("src") || "",
          page: pageElement ? pageElements.indexOf(pageElement) + 1 : null,
          loaded: image.complete && image.naturalWidth > 0 && image.naturalHeight > 0,
          naturalWidth: image.naturalWidth,
          naturalHeight: image.naturalHeight,
          renderedWidth: Math.round(rect.width),
          renderedHeight: Math.round(rect.height),
          pageLeftGap: pageRect ? Math.round(rect.left - pageRect.left) : null,
          pageRightGap: pageRect ? Math.round(pageRect.right - rect.right) : null,
          pageTopGap: pageRect ? Math.round(rect.top - pageRect.top) : null,
          footerGap: footerRect ? Math.round(footerRect.top - rect.bottom) : null,
          insidePage:
            Boolean(pageRect) &&
            rect.left >= pageRect.left - 2 &&
            rect.right <= pageRect.right + 2 &&
            rect.top >= pageRect.top - 2 &&
            (!footerRect || rect.bottom <= footerRect.top - 2)
        }
      })

      return {
        imageCount: images.length,
        geometry,
        issues: geometry.filter(
          (image) =>
            !image.loaded ||
            !image.insidePage ||
            image.renderedWidth < 320 ||
            image.renderedHeight < 175
        )
      }
    })

    for (const issue of result.issues) {
      const filename = decodeURIComponent(issue.src).split("/").at(-1)
      const image = page.locator(`.bookPages img[src*="${filename}"]`).first()
      const imagePage = image.locator("xpath=ancestor::*[contains(@class,'bookPage')]").first()
      await imagePage.screenshot({
        path: `${outputDir}/book-studio-${chapter.outlineSection}-${filename.replace(/\.png$/i, "")}.png`
      })
    }

    report.push({
      module: `R${Number(chapter.outlineSection) - 24}`,
      outlineSection: chapter.outlineSection,
      title: chapter.title,
      chapterIndex: chapterIndex + 1,
      ...result
    })
  }
} finally {
  await browser.close()
}

const failures = report.flatMap((chapter) => {
  const issues = []
  if (chapter.imageCount !== 7) {
    issues.push(`${chapter.module}: attese 7 immagini, trovate ${chapter.imageCount}`)
  }
  for (const image of chapter.issues) {
    issues.push(`${chapter.module}: ${image.src} non conforme`)
  }
  return issues
})

await fs.writeFile(
  `${outputDir}/book-studio-image-report.json`,
  `${JSON.stringify({ generatedAt: new Date().toISOString(), report, failures }, null, 2)}\n`,
  "utf8"
)

console.log(
  JSON.stringify(
    {
      chapterCount: report.length,
      imageCount: report.reduce((sum, chapter) => sum + chapter.imageCount, 0),
      failures
    },
    null,
    2
  )
)

if (failures.length > 0) process.exitCode = 1
