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
  await page.evaluate(() => document.fonts.ready)
  await waitForBookImages(page)
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
      const firstTitle = element.querySelector(".chapterPreviewHeader h2")?.textContent?.trim()
      const runningTitle = element.querySelector(".runningHeader span")?.textContent?.trim()
      const title = firstTitle || runningTitle || "Front matter"
      const safeBottom = footerRect?.top ?? pageRect.bottom
      const contentBottom = Math.max(
        content?.getBoundingClientRect().bottom ?? pageRect.top,
        ...visibleChildren.map((child) => child.getBoundingClientRect().bottom)
      )

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

  const nonFinalPages = pages.filter(
    (item) => !item.isLastChapterPage && item.title !== "Front matter" && item.title !== "Indice"
  )
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
  let previous = ""
  let stableChecks = 0

  for (let attempt = 0; attempt < 60; attempt += 1) {
    const current = await page.$$eval(".bookPages .bookPage", (pages) =>
      pages.map((bookPage) => {
        const text = bookPage.textContent?.replace(/\s+/g, " ").trim() || ""
        return `${text.length}:${text.slice(-80)}`
      }).join("|")
    )
    if (current === previous && current.length > 0) stableChecks += 1
    else stableChecks = 0
    if (stableChecks >= 4) {
      await page.waitForTimeout(1_500)
      const confirmation = await page.$$eval(".bookPages .bookPage", (pages) =>
        pages.map((bookPage) => {
          const text = bookPage.textContent?.replace(/\s+/g, " ").trim() || ""
          return `${text.length}:${text.slice(-80)}`
        }).join("|")
      )
      if (confirmation === current) return
      previous = confirmation
      stableChecks = 0
      continue
    }
    previous = current
    await page.waitForTimeout(750)
  }
}

async function waitForBookImages(page) {
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
