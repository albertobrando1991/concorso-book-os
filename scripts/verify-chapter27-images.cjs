const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const CHAPTER_27_ASSETS = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-27"
)

const EXPECTED_IMAGE_COUNT = 7
const DASHBOARD_URL = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3000"

async function main() {
  const browser = await chromium.launch({ headless: true })

  try {
    const svgAudit = await auditSvgTextGeometry(browser)
    const page = await browser.newPage({
      viewport: { width: 1440, height: 1800 },
      deviceScaleFactor: 1
    })

    await page.goto(DASHBOARD_URL, {
      waitUntil: "domcontentloaded",
      timeout: 60000
    })

    await page
      .locator("button.chapterButton")
      .filter({ hasText: "Gestire concorsi paralleli senza disperdersi" })
      .first()
      .click()
    await page.waitForTimeout(2500)

    const pages = page.locator(".bookPages > .bookPage")
    const count = await pages.count()
    if (count < 10) {
      throw new Error("Meno di 10 pagine nella preview del capitolo 27")
    }

    await pages.nth(0).screenshot({ path: "artifacts/chapter27-page1-preview.png" })

    const diag = await page.evaluate(() => {
      const pageEls = Array.from(document.querySelectorAll(".bookPages > .bookPage"))
      const images = Array.from(document.querySelectorAll(".bookPages img"))
      const chapter27Images = images.filter((image) => (image.getAttribute("src") || "").includes("chapter-27"))
      const visibleChapter27Images = chapter27Images.map((image) => image.getAttribute("src") || "")
      const imageLayouts = chapter27Images.map((image, index) => {
        const imageRect = image.getBoundingClientRect()
        const pageEl = image.closest(".bookPage")
        const pageRect = pageEl ? pageEl.getBoundingClientRect() : null
        const footer = pageEl ? pageEl.querySelector(".pageFooter") : null
        const footerRect = footer ? footer.getBoundingClientRect() : null
        const pageIndex = pageEl ? pageEls.indexOf(pageEl) + 1 : null
        const fuzz = 2
        const aspectRatio = imageRect.height > 0 ? Number((imageRect.width / imageRect.height).toFixed(3)) : 0

        return {
          index: index + 1,
          page: pageIndex,
          source: image.getAttribute("src") || "",
          naturalWidth: image.naturalWidth,
          naturalHeight: image.naturalHeight,
          renderedWidth: Math.round(imageRect.width),
          renderedHeight: Math.round(imageRect.height),
          withinPage:
            Boolean(pageRect) &&
            imageRect.left >= pageRect.left - fuzz &&
            imageRect.right <= pageRect.right + fuzz &&
            imageRect.top >= pageRect.top - fuzz &&
            (!footerRect || imageRect.bottom <= footerRect.top - fuzz),
          hasExpectedNaturalSize: image.naturalWidth === 1600 && image.naturalHeight === 900,
          hasExpectedRenderedSize: imageRect.width >= 390 && imageRect.height >= 215,
          hasExpectedAspectRatio: aspectRatio >= 1.75 && aspectRatio <= 1.79,
          aspectRatio
        }
      })

      return {
        pages: pageEls.length,
        chapter27Images: visibleChapter27Images.length,
        allImagesLoaded: images.every((image) => image.complete && image.naturalWidth > 0 && image.naturalHeight > 0),
        sources: visibleChapter27Images,
        imageLayouts,
        imageLayoutIssues: imageLayouts.filter((entry) =>
          !entry.withinPage ||
          !entry.hasExpectedNaturalSize ||
          !entry.hasExpectedRenderedSize ||
          !entry.hasExpectedAspectRatio
        ),
        overlapPages: pageEls
          .map((el, index) => {
            const footer = el.querySelector(".pageFooter")
            const blocks = Array.from(el.children).filter((node) => !node.classList.contains("pageFooter"))
            const contentBottom = blocks.reduce(
              (max, node) => Math.max(max, node.offsetTop + node.offsetHeight),
              0
            )
            const footerTop = footer ? footer.offsetTop : null

            return {
              page: index + 1,
              overlapsFooter: footerTop ? contentBottom > footerTop - 2 : false
            }
          })
          .filter((entry) => entry.overlapsFooter)
      }
    })

    if (diag.chapter27Images !== EXPECTED_IMAGE_COUNT) {
      throw new Error(`Attese ${EXPECTED_IMAGE_COUNT} immagini chapter-27, trovate ${diag.chapter27Images}`)
    }
    if (!diag.allImagesLoaded) {
      throw new Error("Almeno una immagine della preview non risulta caricata")
    }
    if (diag.imageLayoutIssues.length > 0) {
      throw new Error(`Immagini chapter-27 non conformi nella pagina: ${JSON.stringify(diag.imageLayoutIssues)}`)
    }
    if (diag.overlapPages.length > 0) {
      throw new Error(`Contenuto sovrapposto al footer: ${JSON.stringify(diag.overlapPages)}`)
    }

    console.log(JSON.stringify({ ...diag, svgAudit }, null, 2))

    await page.close()
  } finally {
    await browser.close()
  }
}

async function auditSvgTextGeometry(browser) {
  const files = (await fs.readdir(CHAPTER_27_ASSETS))
    .filter((file) => file.endsWith(".svg"))
    .sort()

  if (files.length !== EXPECTED_IMAGE_COUNT) {
    throw new Error(`Attesi ${EXPECTED_IMAGE_COUNT} SVG chapter-27, trovati ${files.length}`)
  }

  const results = []
  const failures = []

  for (const file of files) {
    const svg = await fs.readFile(path.join(CHAPTER_27_ASSETS, file), "utf8")
    const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 })

    await page.setContent(svg, { waitUntil: "load" })

    const audit = await page.evaluate(() => {
      const svgEl = document.querySelector("svg")
      if (!svgEl) throw new Error("SVG non trovato")

      const viewBox = svgEl.viewBox.baseVal
      const globalBox = {
        x: 28,
        y: 14,
        w: viewBox.width - 56,
        h: viewBox.height - 28,
        pad: 0,
        scope: "global"
      }
      const issues = []
      const texts = Array.from(svgEl.querySelectorAll("text"))

      function nearestSafeBox(text) {
        let parent = text.parentElement

        while (parent && parent !== svgEl) {
          const attr = parent.getAttribute("data-safe-box")
          if (attr) {
            const [x, y, w, h, pad] = attr.split(/\s+/).map(Number)
            return { x, y, w, h, pad, scope: parent.getAttribute("data-safe-name") || "container" }
          }

          parent = parent.parentElement
        }

        return globalBox
      }

      for (const text of texts) {
        const bbox = text.getBBox()
        const safe = nearestSafeBox(text)
        const left = safe.x + safe.pad
        const top = safe.y + safe.pad
        const right = safe.x + safe.w - safe.pad
        const bottom = safe.y + safe.h - safe.pad
        const fuzz = 2

        if (
          bbox.x < left - fuzz ||
          bbox.y < top - fuzz ||
          bbox.x + bbox.width > right + fuzz ||
          bbox.y + bbox.height > bottom + fuzz
        ) {
          issues.push({
            text: text.textContent.trim(),
            scope: safe.scope,
            box: {
              x: Number(bbox.x.toFixed(2)),
              y: Number(bbox.y.toFixed(2)),
              w: Number(bbox.width.toFixed(2)),
              h: Number(bbox.height.toFixed(2))
            },
            safe: {
              x: Number(left.toFixed(2)),
              y: Number(top.toFixed(2)),
              w: Number((right - left).toFixed(2)),
              h: Number((bottom - top).toFixed(2))
            }
          })
        }
      }

      return {
        texts: texts.length,
        issues
      }
    })

    await page.close()

    results.push({ file, texts: audit.texts, issues: audit.issues.length })

    if (audit.issues.length > 0) {
      failures.push({ file, issues: audit.issues })
    }
  }

  if (failures.length > 0) {
    throw new Error(`Testi fuori margine negli SVG: ${JSON.stringify(failures, null, 2)}`)
  }

  return results
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
