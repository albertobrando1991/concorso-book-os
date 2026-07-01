const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const CHAPTER_10_ASSETS = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-10"
)

async function main() {
  const browser = await chromium.launch({ headless: true })
  const svgAudit = await auditSvgTextGeometry(browser)
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1800 },
    deviceScaleFactor: 1
  })

  await page.goto("http://127.0.0.1:3000", {
    waitUntil: "networkidle",
    timeout: 60000
  })

  await page.getByRole("button", { name: /10\.\s*Informatica/i }).click()
  await page.waitForTimeout(2500)

  const pages = page.locator(".bookPages > .bookPage")
  const count = await pages.count()
  if (count < 8) {
    throw new Error("Meno di 8 pagine nella preview del capitolo 10")
  }

  await pages.nth(0).screenshot({ path: "artifacts/chapter10-page1-preview.png" })

  const diag = await page.evaluate(() => {
    const pageEls = Array.from(document.querySelectorAll(".bookPages > .bookPage"))
    const images = Array.from(document.querySelectorAll(".bookPages img"))
    const chapter10Images = images.filter((image) => (image.getAttribute("src") || "").includes("chapter-10"))
    const visibleChapter10Images = chapter10Images.map((image) => image.getAttribute("src") || "")
    const imageLayouts = chapter10Images.map((image, index) => {
      const imageRect = image.getBoundingClientRect()
      const pageEl = image.closest(".bookPage")
      const pageRect = pageEl ? pageEl.getBoundingClientRect() : null
      const footer = pageEl ? pageEl.querySelector(".pageFooter") : null
      const footerRect = footer ? footer.getBoundingClientRect() : null
      const pageIndex = pageEl ? pageEls.indexOf(pageEl) + 1 : null
      const fuzz = 2

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
        aspectRatio: Number((imageRect.width / imageRect.height).toFixed(3))
      }
    })

    return {
      pages: pageEls.length,
      chapter10Images: visibleChapter10Images.length,
      allImagesLoaded: images.every((image) => image.complete && image.naturalWidth > 0 && image.naturalHeight > 0),
      sources: visibleChapter10Images,
      imageLayouts,
      imageLayoutIssues: imageLayouts.filter((entry) => !entry.withinPage),
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

  if (diag.chapter10Images !== 7) {
    throw new Error(`Attese 7 immagini chapter-10, trovate ${diag.chapter10Images}`)
  }
  if (!diag.allImagesLoaded) {
    throw new Error("Almeno una immagine della preview non risulta caricata")
  }
  if (diag.imageLayoutIssues.length > 0) {
    throw new Error(`Immagini chapter-10 fuori dalla pagina A4: ${JSON.stringify(diag.imageLayoutIssues)}`)
  }
  if (diag.overlapPages.length > 0) {
    throw new Error(`Contenuto sovrapposto al footer: ${JSON.stringify(diag.overlapPages)}`)
  }

  console.log(JSON.stringify({ ...diag, svgAudit }, null, 2))

  await browser.close()
}

async function auditSvgTextGeometry(browser) {
  const files = (await fs.readdir(CHAPTER_10_ASSETS))
    .filter((file) => file.endsWith(".svg"))
    .sort()

  const results = []
  const failures = []

  for (const file of files) {
    const svg = await fs.readFile(path.join(CHAPTER_10_ASSETS, file), "utf8")
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
