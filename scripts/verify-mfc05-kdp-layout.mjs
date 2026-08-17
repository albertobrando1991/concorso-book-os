import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3003"
const bookId = "volumi/vol-05"
const reportPath = "artifacts/m-fc05-kdp-layout-report.json"
const screenshotDir = "artifacts/m-fc05-kdp-layout"

await fs.mkdir(screenshotDir, { recursive: true })

const browser = await launchBrowser()
const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })

try {
  await page.goto(`${baseUrl}/?bookId=${encodeURIComponent(bookId)}#studio`, { waitUntil: "domcontentloaded", timeout: 180_000 })
  await page.locator("#studio").scrollIntoViewIfNeeded()
  await page.getByRole("button", { name: "Libro", exact: true }).click()
  await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 180_000 })
  await page.evaluate(() => document.fonts.ready)
  await waitForBookImages(page)
  await page.waitForTimeout(1_200)

  const report = await page.evaluate(() => {
    const pages = Array.from(document.querySelectorAll(".bookPages .bookPage"))
    const bodyFont = document.querySelector(".bookPages .bookPage:not(.frontMatterPage) .previewBlocks > p")
    const headingFont = document.querySelector(".bookPages .bookPage:not(.frontMatterPage) .chapterPreviewHeader h2")
    const getStyle = (element) => element ? {
      fontFamily: getComputedStyle(element).fontFamily,
      fontSize: Number.parseFloat(getComputedStyle(element).fontSize),
      lineHeight: Number.parseFloat(getComputedStyle(element).lineHeight)
    } : null

    return {
      pageCount: pages.length,
      typography: { body: getStyle(bodyFont), heading: getStyle(headingFont) },
      pages: pages.map((bookPage, index) => {
        const pageRect = bookPage.getBoundingClientRect()
        const footerRect = bookPage.querySelector(".pageFooter")?.getBoundingClientRect()
        const contentRect = bookPage.querySelector(".frontMatterBlocks, .digitalServicesContent, .previewBlocks")?.getBoundingClientRect()
        const bottomLimit = footerRect ? footerRect.top - 4 : pageRect.bottom - 8
        const images = Array.from(bookPage.querySelectorAll("img")).map((image) => {
          const rect = image.getBoundingClientRect()
          return {
            complete: image.complete,
            naturalWidth: image.naturalWidth,
            naturalHeight: image.naturalHeight,
            outsidePage: rect.left < pageRect.left || rect.right > pageRect.right || rect.top < pageRect.top || rect.bottom > pageRect.bottom
          }
        })

        return {
          page: index + 1,
          title: bookPage.querySelector("h2")?.textContent?.trim() || bookPage.querySelector("h3")?.textContent?.trim() || "front matter",
          width: Math.round(pageRect.width),
          height: Math.round(pageRect.height),
          ratio: Number((pageRect.width / pageRect.height).toFixed(3)),
          overflow: contentRect ? Math.max(0, Math.round(contentRect.bottom - bottomLimit)) : 0,
          brokenImages: images.filter((image) => !image.complete || image.naturalWidth === 0 || image.naturalHeight === 0).length,
          outOfBoundsImages: images.filter((image) => image.outsidePage).length,
          imageCount: images.length
        }
      })
    }
  })

  const pageCount = await page.locator(".bookPages .bookPage").count()
  const sampleIndexes = [...new Set([0, Math.floor(pageCount / 3), Math.floor((pageCount * 2) / 3), pageCount - 1])]

  for (const [sample, index] of sampleIndexes.entries()) {
    await page.locator(".bookPages .bookPage").nth(index).screenshot({ path: `${screenshotDir}/page-${String(sample + 1).padStart(2, "0")}.png` })
  }

  await fs.writeFile(reportPath, JSON.stringify(report, null, 2), "utf8")

  const failures = [
    ...(Math.abs((report.pages[0]?.ratio || 0) - 6.69 / 9.61) > 0.02 ? [`page ratio ${report.pages[0]?.ratio} is not KDP paperback`] : []),
    ...report.pages.filter((item) => item.overflow > 8).map((item) => `page ${item.page}: overflow ${item.overflow}px`),
    ...report.pages.filter((item) => item.brokenImages > 0).map((item) => `page ${item.page}: ${item.brokenImages} broken image(s)`),
    ...report.pages.filter((item) => item.outOfBoundsImages > 0).map((item) => `page ${item.page}: ${item.outOfBoundsImages} out-of-bounds image(s)`),
    ...(report.typography.body?.fontFamily.toLowerCase().includes("garamond") ? [] : [`body font ${report.typography.body?.fontFamily || "missing"} is not Garamond`]),
    ...(report.typography.heading?.fontFamily.toLowerCase().includes("arial") ? [] : [`heading font ${report.typography.heading?.fontFamily || "missing"} is not Arial`])
  ]

  if (failures.length > 0) throw new Error(failures.join("\n"))

  console.log(JSON.stringify({ bookId, pageCount: report.pageCount, samples: sampleIndexes, result: "ok" }, null, 2))
} finally {
  await browser.close()
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
