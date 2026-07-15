import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3000"
const outputPath = "artifacts/volume01-page-fill-report.json"

const browser = await launchBrowser()
const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })

try {
  await page.goto(`${baseUrl}/?bookId=il-metodo-bando#studio`, { waitUntil: "domcontentloaded", timeout: 120_000 })
  await page.locator("#studio").scrollIntoViewIfNeeded()
  await page.getByRole("button", { name: "Libro", exact: true }).click()
  await page.waitForSelector(".bookPages .bookPage", { timeout: 120_000 })
  await waitForStablePagination(page)

  const pages = await page.$$eval(".bookPages .bookPage", (elements) => {
    const diagnostics = elements.map((element, index) => {
      const pageRect = element.getBoundingClientRect()
      const footer = element.querySelector(".pageFooter")
      const footerRect = footer?.getBoundingClientRect()
      const content = element.querySelector(".previewBlocks, .frontMatterBlocks, .digitalServicesContent")
      const visibleChildren = Array.from(content?.children || []).filter((child) => {
        const rect = child.getBoundingClientRect()
        return rect.width > 0 && rect.height > 0
      })
      const lastChild = visibleChildren.at(-1)
      const lastRect = lastChild?.getBoundingClientRect()
      const firstTitle = element.querySelector(".chapterPreviewHeader h2")?.textContent?.trim()
      const runningTitle = element.querySelector(".runningHeader span")?.textContent?.trim()
      const title = firstTitle || runningTitle || "Front matter"
      const safeBottom = footerRect?.top ?? pageRect.bottom
      const contentBottom = lastRect?.bottom ?? content?.getBoundingClientRect().bottom ?? pageRect.top

      return {
        page: index + 1,
        title,
        isFirstPage: Boolean(firstTitle),
        freeSpace: Math.max(0, Math.round(safeBottom - contentBottom)),
        overflow: Math.max(0, Math.round(contentBottom - safeBottom)),
        lastBlock: lastChild?.tagName || "none",
        lastBlockClass: typeof lastChild?.className === "string" ? lastChild.className : ""
      }
    })

    return diagnostics.map((item, index) => ({
      ...item,
      isLastChapterPage: index === diagnostics.length - 1 || diagnostics[index + 1].title !== item.title
    }))
  })

  const nonFinalPages = pages.filter((item) => !item.isLastChapterPage)
  const report = {
    generatedAt: new Date().toISOString(),
    pageCount: pages.length,
    overflowPages: pages.filter((item) => item.overflow > 8).length,
    nonFinalPages: nonFinalPages.length,
    nonFinalOver120: nonFinalPages.filter((item) => item.freeSpace > 120).length,
    averageNonFinalFreeSpace: average(nonFinalPages.map((item) => item.freeSpace)),
    medianNonFinalFreeSpace: median(nonFinalPages.map((item) => item.freeSpace)),
    worstNonFinalPages: [...nonFinalPages].sort((a, b) => b.freeSpace - a.freeSpace).slice(0, 30),
    pages
  }

  const screenshotTargets = [...nonFinalPages]
    .filter((item) => item.title !== "Front matter" && item.title !== "Indice")
    .sort((a, b) => b.freeSpace - a.freeSpace)
    .slice(0, 3)

  for (const target of screenshotTargets) {
    await page.locator(".bookPages .bookPage").nth(target.page - 1).screenshot({
      path: `artifacts/volume01-page-fill-page-${String(target.page).padStart(3, "0")}.png`
    })
  }

  await fs.writeFile(outputPath, JSON.stringify(report, null, 2), "utf8")
  console.log(JSON.stringify({
    pageCount: report.pageCount,
    overflowPages: report.overflowPages,
    nonFinalOver120: report.nonFinalOver120,
    averageNonFinalFreeSpace: report.averageNonFinalFreeSpace,
    medianNonFinalFreeSpace: report.medianNonFinalFreeSpace,
    worst: report.worstNonFinalPages.slice(0, 10)
  }, null, 2))
} finally {
  await browser.close()
}

function average(values) {
  if (values.length === 0) return 0
  return Math.round(values.reduce((sum, value) => sum + value, 0) / values.length)
}

function median(values) {
  if (values.length === 0) return 0
  const sorted = [...values].sort((a, b) => a - b)
  const middle = Math.floor(sorted.length / 2)
  return sorted.length % 2 === 0 ? Math.round((sorted[middle - 1] + sorted[middle]) / 2) : sorted[middle]
}

async function waitForStablePagination(page) {
  let previous = -1
  let stableChecks = 0

  for (let attempt = 0; attempt < 30; attempt += 1) {
    const current = await page.locator(".bookPages .bookPage").count()
    if (current === previous && current > 0) stableChecks += 1
    else stableChecks = 0
    if (stableChecks >= 3) return
    previous = current
    await page.waitForTimeout(500)
  }
}

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
