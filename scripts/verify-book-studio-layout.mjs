import fs from "node:fs/promises"
import { chromium } from "@playwright/test"
import {
  resolveBookStudioLayoutOptions,
  waitForStableBookPageCount
} from "./book-studio-layout-options.mjs"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3010"
const { cases: configuredCases, artifactPrefix, expectedCounts } = resolveBookStudioLayoutOptions(process.env)
const cases = configuredCases.map((current) => ({
  ...current,
  url: `${baseUrl}/?bookId=${encodeURIComponent(current.id)}#studio`
}))

await fs.mkdir("artifacts", { recursive: true })

const browser = await launchBrowser()
const report = []

try {
  for (const current of cases) {
    const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })
    await page.goto(current.url, { waitUntil: "domcontentloaded", timeout: 120_000 })
    await page.locator("#studio").waitFor({ state: "visible", timeout: 120_000 })
    await page.evaluate(() => document.querySelector("#studio")?.scrollIntoView({ block: "start" }))
    await page.getByRole("button", { name: "Libro", exact: true }).click()
    await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 120_000 })
    await page.evaluate(() => document.fonts.ready)
    await waitForBookImages(page)
    await page.waitForTimeout(Number(process.env.BOOK_STUDIO_RENDER_SETTLE_MS || 25_000))
    await waitForStableBookPageCount(page)
    await page.screenshot({ path: `artifacts/${artifactPrefix}-${current.label}.png`, fullPage: true })

    await waitForStableBookPageCount(page)

    const studio = await page.evaluate(() => {
      const getRect = (selector) => {
        const element = document.querySelector(selector)
        if (!element) return null
        const rect = element.getBoundingClientRect()

        return {
          top: rect.top,
          right: rect.right,
          bottom: rect.bottom,
          left: rect.left,
          width: rect.width,
          height: rect.height
        }
      }
      const overlapArea = (left, right) => {
        if (!left || !right) return 0
        const width = Math.max(0, Math.min(left.right, right.right) - Math.max(left.left, right.left))
        const height = Math.max(0, Math.min(left.bottom, right.bottom) - Math.max(left.top, right.top))

        return Math.round(width * height)
      }
      const getTypography = (selector) => {
        const element = document.querySelector(selector)
        if (!element) return null
        const style = getComputedStyle(element)

        return {
          fontFamily: style.fontFamily,
          fontSize: Number.parseFloat(style.fontSize),
          lineHeight: Number.parseFloat(style.lineHeight),
          fontWeight: style.fontWeight
        }
      }
      const preview = getRect(".bookPreviewShell")
      const assets = getRect(".assetStrip")

      return {
        gridTemplateColumns: getComputedStyle(document.querySelector(".bookStudioLayout")).gridTemplateColumns,
        preview,
        assets,
        assetPreviewOverlap: overlapArea(preview, assets),
        typography: {
          chapter: getTypography(".bookPages .bookPage:not(.frontMatterPage) .chapterPreviewHeader h2"),
          section: getTypography(".bookPages .bookPage:not(.frontMatterPage) .previewBlocks h3"),
          subsection: getTypography(".bookPages .bookPage:not(.frontMatterPage) .previewBlocks h4"),
          body: getTypography(".bookPages .bookPage:not(.frontMatterPage) .previewBlocks > p"),
          table: getTypography(".bookPages .bookPage:not(.frontMatterPage) .previewTable"),
          callout: getTypography(".bookPages .bookPage:not(.frontMatterPage) .previewCallout p"),
          digitalSection: getTypography(".bookPages .digitalServicesContent h3"),
          digitalCallout: getTypography(".bookPages .digitalServicesContent .previewCallout p")
        }
      }
    })

    const structure = await page.evaluate(() => {
      const pages = Array.from(document.querySelectorAll(".bookPages .bookPage"))
      const unique = (values) => new Set(values.filter(Boolean)).size

      return {
        pageCount: pages.length,
        pageNumbers: pages.map((item) => Number(item.getAttribute("data-page-number") || 0)),
        frontMatter: unique(
          pages
            .filter((item) => item.getAttribute("data-front-matter-layout") !== "module-opening")
            .map((item) => item.getAttribute("data-front-matter-layout"))
        ),
        moduleOpenings: unique(
          pages
            .filter((item) => item.getAttribute("data-front-matter-layout") === "module-opening")
            .map((item) => item.getAttribute("data-chapter-path"))
        ),
        chapters: unique(
          pages
            .filter((item) => item.getAttribute("data-section-type") === "chapter")
            .map((item) => item.getAttribute("data-chapter-path"))
        ),
        nuclei: unique(
          Array.from(document.querySelectorAll(".bookPages [data-nucleus-id]"))
            .map((item) => item.getAttribute("data-nucleus-id"))
        ),
        indexNuclei: unique(
          Array.from(document.querySelectorAll(".bookPages .indexSubLine[data-nucleus-id]"))
            .map((item) => item.getAttribute("data-nucleus-id"))
        ),
        verificationHeadings: document.querySelectorAll(".bookPages .verificationHeading").length
      }
    })

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

    report.push({ ...current, studio, structure, diagnostics })
    await page.close()
  }
} finally {
  await browser.close()
}

await fs.writeFile(`artifacts/${artifactPrefix}-layout-report.json`, JSON.stringify(report, null, 2), "utf8")

const failures = report.flatMap((entry) =>
  [
    ...(entry.studio.assetPreviewOverlap > 0
      ? [`${entry.label}: asset strip overlaps preview by ${entry.studio.assetPreviewOverlap}px2`]
      : []),
    ...structureFailures(entry, expectedCounts),
    ...typographyFailures(entry),
    ...entry.diagnostics
      .filter((page) => page.overflow > 8 || page.overlaps.length > 0)
      .map((page) => `${entry.label} page ${page.page}: overflow=${page.overflow}, overlaps=${page.overlaps.join("; ")}`)
  ]
)

if (failures.length > 0) {
  console.error(failures.join("\n"))
  process.exit(1)
}

console.log(`Book Studio layout OK for ${report.map((entry) => entry.label).join(", ")}`)

function structureFailures(entry, expectedCounts) {
  const failures = []
  const expectedSequence = Array.from(
    { length: entry.structure.pageCount },
    (_, index) => index + 1
  )

  if (entry.structure.pageCount < 1) {
    failures.push(`${entry.label}: nessuna pagina renderizzata`)
  }

  if (JSON.stringify(entry.structure.pageNumbers) !== JSON.stringify(expectedSequence)) {
    failures.push(`${entry.label}: numerazione pagine non progressiva`)
  }

  if (entry.structure.nuclei !== entry.structure.indexNuclei) {
    failures.push(
      `${entry.label}: nuclei testo=${entry.structure.nuclei}, indice=${entry.structure.indexNuclei}`
    )
  }

  if (expectedCounts) {
    for (const [key, expected] of Object.entries(expectedCounts)) {
      if (entry.structure[key] !== expected) {
        failures.push(`${entry.label}: ${key}=${entry.structure[key]}, atteso=${expected}`)
      }
    }
  }

  return failures
}

function typographyFailures(entry) {
  const checks = [
    ["chapter", "Arial", 26.67, true],
    ["section", "Arial", 18.67, true],
    ["subsection", "Arial", 16, true],
    ["body", "Garamond", 14.67, false],
    ["table", "Arial", 12.67, false],
    ["callout", "Arial", 12.67, false],
    ["digitalSection", "Arial", 18.67, true],
    ["digitalCallout", "Arial", 12.67, false]
  ]

  return checks.flatMap(([key, family, size, bold]) => {
    const actual = entry.studio.typography[key]
    if (!actual) return [`${entry.label}: typography sample missing for ${key}`]
    const errors = []
    if (!actual.fontFamily.toLowerCase().includes(family.toLowerCase())) {
      errors.push(`${entry.label}: ${key} uses ${actual.fontFamily}, expected ${family}`)
    }
    if (Math.abs(actual.fontSize - size) > 0.25) {
      errors.push(`${entry.label}: ${key} size ${actual.fontSize}px, expected ${size}px`)
    }
    if (bold && Number.parseInt(actual.fontWeight, 10) < 700) {
      errors.push(`${entry.label}: ${key} weight ${actual.fontWeight}, expected bold`)
    }
    return errors
  })
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
