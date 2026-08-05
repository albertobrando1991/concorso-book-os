import fs from "node:fs/promises"
import path from "node:path"
import { chromium } from "@playwright/test"
import {
  buildContactSheetRanges,
  classifyPageDiagnostic,
  flaggedPageNumbers,
  renderPageAuditMarkdown,
  resolvePageAuditOptions,
  validatePageAuditMarkdown
} from "./book-studio-page-audit-core.mjs"

const options = resolvePageAuditOptions(process.env)
const {
  artifactPrefix,
  baseUrl,
  bookId,
  contactSheetSize,
  expectedPageCount,
  explicitScreenshotPages,
  reportMode,
  reportPath
} = options
const url = `${baseUrl}/?bookId=${encodeURIComponent(bookId)}#studio`

await fs.mkdir("artifacts", { recursive: true })
await fs.mkdir(path.dirname(reportPath), { recursive: true })

const browser = await launchBrowser()
const page = await browser.newPage({ viewport: { width: 1500, height: 1050 } })

try {
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 180_000 })
  await page.locator("#studio").waitFor({ state: "visible", timeout: 120_000 })
  await page.locator("#studio").scrollIntoViewIfNeeded()
  await page.getByRole("button", { name: "Libro", exact: true }).click()
  await page.locator(".bookPages .bookPage").first().waitFor({ state: "visible", timeout: 120_000 })
  await page.evaluate(() => document.fonts.ready)
  await waitForBookImages(page)
  const stableSignature = await waitForStablePagination(page)
  const diagnostics = await collectDiagnostics(page)

  if (diagnostics.length !== expectedPageCount) {
    throw new Error(`Conteggio pagine inatteso: ${diagnostics.length}, atteso ${expectedPageCount}`)
  }

  const expectedSequence = Array.from({ length: diagnostics.length }, (_, index) => index + 1)
  if (JSON.stringify(diagnostics.map((item) => item.printedNumber)) !== JSON.stringify(expectedSequence)) {
    throw new Error("Numerazione pagine non progressiva")
  }

  const confirmationSignature = await pageSignature(page)
  if (confirmationSignature !== stableSignature) {
    throw new Error("Paginazione cambiata durante la raccolta diagnostica")
  }

  const eligibleFreeSpace = diagnostics
    .filter((item) => !item.isSectionTerminal && item.sectionType !== "front_matter")
    .map((item) => item.freeSpace)
  const context = {
    pageCount: diagnostics.length,
    medianFreeSpace: median(eligibleFreeSpace),
    expectedWidth: 6.69 * 96,
    expectedHeight: 9.61 * 96
  }
  const issues = diagnostics.flatMap((item) => classifyPageDiagnostic(item, context))
  const ranges = buildContactSheetRanges(diagnostics.length, contactSheetSize)

  for (const range of ranges) {
    await captureContactSheet(page, range, artifactPrefix)
  }

  const screenshotPages = flaggedPageNumbers(issues, explicitScreenshotPages)
  for (const pageNumber of screenshotPages) {
    if (pageNumber > diagnostics.length) {
      throw new Error(`Pagina screenshot fuori intervallo: ${pageNumber}/${diagnostics.length}`)
    }
    await page.locator(".bookPages .bookPage").nth(pageNumber - 1).screenshot({
      path: `artifacts/${artifactPrefix}-page-${pad(pageNumber, 3)}.png`
    })
  }

  const generatedAt = new Date().toISOString()
  const failures = []

  if (reportMode === "write") {
    await fs.writeFile(
      reportPath,
      renderPageAuditMarkdown({ generatedAt, bookId, diagnostics, issues }),
      "utf8"
    )
  } else {
    const markdown = await fs.readFile(reportPath, "utf8")
    failures.push(...validatePageAuditMarkdown(markdown, diagnostics.length))
    failures.push(...issues.map(
      (issue) => `pagina ${issue.page}: ${issue.problemType} - ${issue.element} (${issue.severity})`
    ))
  }

  const summary = {
    bookId,
    pageCount: diagnostics.length,
    contactSheets: ranges.length,
    screenshotPages,
    blocking: issues.filter((issue) => issue.severity === "bloccante").length,
    significant: issues.filter((issue) => issue.severity === "media").length,
    medianFreeSpace: context.medianFreeSpace,
    reportMode
  }

  console.log(JSON.stringify(summary, null, 2))

  if (failures.length > 0) {
    console.error(failures.join("\n"))
    process.exitCode = 1
  }
} finally {
  await browser.close()
}

async function collectDiagnostics(page) {
  return page.$$eval(".bookPages .bookPage", (bookPages) => {
    const lastHeadingLevelByChapter = new Map()

    return bookPages.map((bookPage, index) => {
      const nextPage = bookPages[index + 1]
      const pageRect = bookPage.getBoundingClientRect()
      const pageStyle = getComputedStyle(bookPage)
      const paddingTop = numberStyle(pageStyle.paddingTop)
      const paddingRight = numberStyle(pageStyle.paddingRight)
      const paddingBottom = numberStyle(pageStyle.paddingBottom)
      const paddingLeft = numberStyle(pageStyle.paddingLeft)
      const footer = bookPage.querySelector(".pageFooter")
      const footerRect = footer?.getBoundingClientRect()
      const safeBottom = footerRect?.top ?? pageRect.bottom - paddingBottom
      const contentLeft = pageRect.left + paddingLeft
      const contentRight = pageRect.right - paddingRight
      const visibleBlocks = Array.from(bookPage.querySelectorAll(
        ":scope > .previewBlocks > [data-block-type], :scope > .digitalServicesHero [data-block-type]"
      )).filter(isVisible)
      const blockRects = visibleBlocks.map((element) => element.getBoundingClientRect())
      const contentTop = blockRects.length > 0
        ? Math.min(...blockRects.map((rect) => rect.top))
        : pageRect.top + paddingTop
      const contentBottom = blockRects.length > 0
        ? Math.max(...blockRects.map((rect) => rect.bottom))
        : contentTop
      const usableHeight = Math.max(0, safeBottom - contentTop)
      const usedHeight = Math.max(0, Math.min(safeBottom, contentBottom) - contentTop)
      const chapterPath = bookPage.getAttribute("data-chapter-path") || ""
      const sectionType = bookPage.getAttribute("data-section-type") || ""
      const frontMatterLayout = bookPage.getAttribute("data-front-matter-layout") || ""
      const collisions = collectCollisions(visibleBlocks, footer)
      const tables = Array.from(bookPage.querySelectorAll(".previewTableWrap")).filter(isVisible).map(
        (wrapper, tableIndex) => {
          const rect = wrapper.getBoundingClientRect()
          return {
            label: `table ${tableIndex + 1}`,
            continued: wrapper.getAttribute("data-block-continued") === "true",
            hasHeader: Boolean(wrapper.querySelector("thead th")),
            contained: rect.left >= contentLeft - 1
              && rect.right <= contentRight + 1
              && rect.top >= pageRect.top
              && rect.bottom <= safeBottom + 1
          }
        }
      )
      const images = Array.from(bookPage.querySelectorAll("figure")).filter(isVisible).map(
        (figure, imageIndex) => {
          const image = figure.querySelector("img")
          const caption = figure.querySelector("figcaption")
          const rects = [figure, image, caption]
            .filter(Boolean)
            .map((element) => element.getBoundingClientRect())
          return {
            label: `figure ${imageIndex + 1}`,
            loaded: Boolean(image?.complete && image.naturalWidth > 0),
            hasCaption: Boolean(caption?.textContent?.trim()),
            contained: rects.every((rect) =>
              rect.left >= contentLeft - 1
              && rect.right <= contentRight + 1
              && rect.top >= pageRect.top
              && rect.bottom <= safeBottom + 1
            )
          }
        }
      )
      for (const [missingIndex] of Array.from(bookPage.querySelectorAll(".missingAsset")).entries()) {
        images.push({
          label: `missing asset ${missingIndex + 1}`,
          loaded: false,
          hasCaption: true,
          contained: true
        })
      }
      const rawMarkdown = Array.from(bookPage.querySelectorAll(
        '[data-block-type="paragraph"], [data-block-type="list"] li'
      )).filter(isVisible).map((element) => element.textContent?.trim() || "").filter(
        (text) => /^\s*\|.*\|\s*$/.test(text) || /^\s*\|?\s*:?-{3,}/.test(text)
      )
      const headingFailures = []
      let previousHeadingLevel = lastHeadingLevelByChapter.get(chapterPath) || 2
      for (const heading of Array.from(bookPage.querySelectorAll(
        '.chapterPreviewHeader h2, [data-block-type="heading"]'
      )).filter(isVisible)) {
        const level = Number(heading.tagName.slice(1))
        if (level - previousHeadingLevel > 1) {
          headingFailures.push(`${heading.tagName.toLowerCase()} dopo h${previousHeadingLevel}`)
        }
        previousHeadingLevel = level
      }
      lastHeadingLevelByChapter.set(chapterPath, previousHeadingLevel)

      return {
        page: index + 1,
        domIndex: index + 1,
        printedNumber: Number(bookPage.getAttribute("data-page-number") || 0),
        title: bookPage.querySelector(
          ".chapterPreviewHeader h2, .runningHeader span, .frontMatterBlocks h3"
        )?.textContent?.trim() || "Front matter",
        chapterPath,
        sectionType,
        frontMatterLayout,
        side: bookPage.classList.contains("bookPageVerso") ? "verso" : "recto",
        width: pageRect.width,
        height: pageRect.height,
        paddingTop,
        paddingRight,
        paddingBottom,
        paddingLeft,
        freeSpace: Math.max(0, Math.round(safeBottom - contentBottom)),
        fillRatio: usableHeight > 0 ? Math.max(0, Math.min(1, usedHeight / usableHeight)) : 0,
        overflow: Math.max(0, Math.round(contentBottom - safeBottom)),
        collisions,
        firstBlock: blockDiagnostic(visibleBlocks[0]),
        lastBlock: blockDiagnostic(visibleBlocks.at(-1)),
        tables,
        images,
        rawMarkdown,
        typographyFailures: collectTypographyFailures(bookPage, frontMatterLayout),
        headingFailures,
        unjustifiedProse: collectUnjustifiedProse(bookPage, frontMatterLayout),
        consecutiveImages: visibleBlocks.some(
          (block, blockIndex) => block.getAttribute("data-block-type") === "image"
            && visibleBlocks[blockIndex + 1]?.getAttribute("data-block-type") === "image"
        ),
        detachedBlocks: [],
        isSectionTerminal: !nextPage
          || nextPage.getAttribute("data-chapter-path") !== chapterPath
      }
    })

    function numberStyle(value) {
      return Number.parseFloat(value) || 0
    }

    function isVisible(element) {
      const rect = element.getBoundingClientRect()
      return rect.width > 0 && rect.height > 0
    }

    function blockDiagnostic(element) {
      if (!element) return undefined
      const rect = element.getBoundingClientRect()
      const style = getComputedStyle(element)
      const lineHeight = Number.parseFloat(style.lineHeight)
        || Number.parseFloat(style.fontSize) * 1.2
      return {
        type: element.getAttribute("data-block-type") || element.tagName.toLowerCase(),
        continued: element.getAttribute("data-block-continued") === "true",
        lines: Math.max(1, Math.round(rect.height / lineHeight))
      }
    }

    function collectCollisions(blocks, footer) {
      const failures = []

      for (let index = 0; index < blocks.length - 1; index += 1) {
        const left = blocks[index]
        const right = blocks[index + 1]
        if (overlap(left, right)) {
          failures.push(`${blockLabel(left, index)} / ${blockLabel(right, index + 1)}`)
        }
      }

      if (footer) {
        blocks.forEach((block, index) => {
          if (overlap(block, footer)) failures.push(`${blockLabel(block, index)} / footer`)
        })
      }

      return failures
    }

    function overlap(leftElement, rightElement) {
      const left = leftElement.getBoundingClientRect()
      const right = rightElement.getBoundingClientRect()
      const horizontal = Math.min(left.right, right.right) - Math.max(left.left, right.left)
      const vertical = Math.min(left.bottom, right.bottom) - Math.max(left.top, right.top)
      return horizontal > 4 && vertical > 4
    }

    function blockLabel(element, index) {
      return `${element.getAttribute("data-block-type") || element.tagName.toLowerCase()} ${index + 1}`
    }

    function collectTypographyFailures(bookPage, frontMatterLayout) {
      const failures = []
      const checks = [
        [".chapterPreviewHeader h2", "chapter heading", "arial", [26.67], true],
        ['[data-block-type="heading"]', "content heading", "arial", [], true],
        ['[data-block-type="paragraph"]:not(.previewCaption):not(.missingAsset)', "body", "garamond", [14.67], false],
        ['[data-block-type="list"] > li', "list", "garamond", [14.67], false],
        [".previewTable", "table", "arial", [12.67], false],
        [".previewCallout p", "callout", "arial", [12.67], false],
        [".previewCaption, figcaption", "caption", "arial", [12], false]
      ]

      for (const [selector, label, family, sizes, bold] of checks) {
        const elements = Array.from(bookPage.querySelectorAll(selector)).filter(isVisible)
        for (const [elementIndex, element] of elements.entries()) {
          const style = getComputedStyle(element)
          const expectedSizes = label === "content heading"
            ? headingSizes(element, bookPage, frontMatterLayout)
            : sizes
          const actualSize = Number.parseFloat(style.fontSize)
          const actualWeight = Number.parseInt(style.fontWeight, 10)

          if (!style.fontFamily.toLowerCase().includes(family)) {
            failures.push(`${label} ${elementIndex + 1}: font ${style.fontFamily}`)
          }
          if (expectedSizes.length > 0 && !expectedSizes.some(
            (expected) => Math.abs(actualSize - expected) <= 0.25
          )) {
            failures.push(`${label} ${elementIndex + 1}: size ${actualSize}px`)
          }
          if (bold && (!Number.isFinite(actualWeight) || actualWeight < 700)) {
            failures.push(`${label} ${elementIndex + 1}: weight ${style.fontWeight}`)
          }
        }
      }

      return failures
    }

    function headingSizes(element, bookPage, frontMatterLayout) {
      if (element.tagName === "H4") return [16]
      if (element.tagName === "H5") return [14.67]
      if (
        frontMatterLayout === "analytical-index"
        && element.matches(".frontMatterBlocks > h3:first-child")
      ) return [24]
      if (
        frontMatterLayout === "title-page"
        && element.matches(".frontMatterBlocks h3:not(:first-child)")
      ) return [16]
      if (bookPage.classList.contains("frontMatterPage")) return [18.67, 24]
      return [18.67]
    }

    function collectUnjustifiedProse(bookPage, frontMatterLayout) {
      if (frontMatterLayout === "title-page" || frontMatterLayout === "module-opening") return []

      return Array.from(bookPage.querySelectorAll(
        ':scope > .previewBlocks > [data-block-type="paragraph"]'
      )).filter(isVisible).filter(
        (element) => !element.classList.contains("previewCaption")
          && !element.classList.contains("missingAsset")
          && !element.closest(".digitalServicesHero")
      ).flatMap((element, index) => {
        const style = getComputedStyle(element)
        const orphans = Number.parseInt(style.orphans, 10)
        const widows = Number.parseInt(style.widows, 10)
        return style.textAlign !== "justify" || orphans < 3 || widows < 3
          ? [`paragraph ${index + 1}: align=${style.textAlign}, orphans=${style.orphans}, widows=${style.widows}`]
          : []
      })
    }
  })
}

async function captureContactSheet(page, range, prefix) {
  const clonedPages = await page.evaluate(({ pages }) => {
    document.querySelector("#bookAuditContactSheet")?.remove()
    const sourcePages = Array.from(document.querySelectorAll(".bookPages .bookPage"))
    const firstRect = sourcePages[0]?.getBoundingClientRect()
    if (!firstRect) throw new Error("Nessuna pagina disponibile per la tavola-contatto")

    const scale = 0.205
    const labelHeight = 18
    const root = document.createElement("section")
    root.id = "bookAuditContactSheet"
    Object.assign(root.style, {
      position: "absolute",
      top: `${document.documentElement.scrollHeight + 100}px`,
      left: "0",
      display: "grid",
      gridTemplateColumns: "repeat(4, max-content)",
      gap: "12px",
      padding: "20px",
      background: "#d1d5db",
      zIndex: "2147483647"
    })

    for (const pageNumber of pages) {
      const source = sourcePages[pageNumber - 1]
      if (!source) throw new Error(`Pagina ${pageNumber} assente dalla tavola-contatto`)
      const wrapper = document.createElement("div")
      const label = document.createElement("div")
      const clone = source.cloneNode(true)
      wrapper.setAttribute("data-contact-page", String(pageNumber))
      Object.assign(wrapper.style, {
        position: "relative",
        width: `${firstRect.width * scale}px`,
        height: `${firstRect.height * scale + labelHeight}px`,
        overflow: "hidden",
        background: "#ffffff"
      })
      label.textContent = `Pagina ${pageNumber}`
      Object.assign(label.style, {
        position: "absolute",
        inset: "0 0 auto 0",
        height: `${labelHeight}px`,
        padding: "2px 4px",
        color: "#111827",
        background: "#f9fafb",
        font: "700 11px Arial, sans-serif",
        lineHeight: "14px",
        zIndex: "2"
      })
      Object.assign(clone.style, {
        position: "absolute",
        top: `${labelHeight}px`,
        left: "0",
        margin: "0",
        transform: `scale(${scale})`,
        transformOrigin: "top left"
      })
      wrapper.append(label, clone)
      root.append(wrapper)
    }

    document.body.append(root)
    return Array.from(root.querySelectorAll("[data-contact-page]"))
      .map((item) => Number(item.getAttribute("data-contact-page")))
  }, { pages: range.pages })

  if (JSON.stringify(clonedPages) !== JSON.stringify(range.pages)) {
    throw new Error(`Sequenza tavola-contatto errata: ${range.start}-${range.end}`)
  }

  try {
    const sheet = page.locator("#bookAuditContactSheet")
    await sheet.scrollIntoViewIfNeeded()
    await sheet.screenshot({
      path: `artifacts/${prefix}-contact-${pad(range.index, 2)}-pages-${pad(range.start, 3)}-${pad(range.end, 3)}.png`
    })
  } finally {
    await page.evaluate(() => document.querySelector("#bookAuditContactSheet")?.remove())
  }
}

async function waitForStablePagination(page) {
  let previous = ""
  let stableChecks = 0

  for (let attempt = 0; attempt < 60; attempt += 1) {
    const current = await pageSignature(page)
    if (current === previous && current.length > 0) stableChecks += 1
    else stableChecks = 0

    if (stableChecks >= 4) {
      await page.waitForTimeout(1_500)
      const confirmation = await pageSignature(page)
      if (confirmation === current) return confirmation
      previous = confirmation
      stableChecks = 0
      continue
    }

    previous = current
    await page.waitForTimeout(750)
  }

  throw new Error("Paginazione non stabilizzata entro il timeout")
}

async function pageSignature(page) {
  return page.$$eval(".bookPages .bookPage", (pages) => pages.map((bookPage) => {
    const text = bookPage.textContent?.replace(/\s+/g, " ").trim() || ""
    return `${bookPage.getAttribute("data-page-number")}:${text.length}:${text.slice(-80)}`
  }).join("|"))
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

function median(values) {
  if (values.length === 0) return 0
  const sorted = [...values].sort((left, right) => left - right)
  const middle = Math.floor(sorted.length / 2)
  return sorted.length % 2 === 0
    ? Math.round((sorted[middle - 1] + sorted[middle]) / 2)
    : sorted[middle]
}

function pad(value, width) {
  return String(value).padStart(width, "0")
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
