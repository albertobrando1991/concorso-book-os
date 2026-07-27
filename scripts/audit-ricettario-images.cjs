const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const ROOT = process.cwd()
const ASSET_ROOT = path.join(ROOT, "wiki", "books", "il-metodo-bando", "assets")
const OUTPUT_ROOT = path.join(ROOT, "artifacts", "ricettario-image-audit")
const CHAPTERS = Array.from({ length: 23 }, (_, index) => index + 25)
const EXPECTED_PER_CHAPTER = 7

async function main() {
  await fs.mkdir(OUTPUT_ROOT, { recursive: true })
  const browser = await chromium.launch({ headless: true })

  try {
    const inventory = await collectInventory()
    const svgGeometry = await auditSvgGeometry(browser, inventory)
    const contactSheets = await createContactSheets(browser, inventory)
    const report = {
      generatedAt: new Date().toISOString(),
      expectedChapters: CHAPTERS.length,
      expectedPngTotal: CHAPTERS.length * EXPECTED_PER_CHAPTER,
      inventory,
      svgGeometry,
      contactSheets
    }

    await fs.writeFile(
      path.join(OUTPUT_ROOT, "audit-report.json"),
      `${JSON.stringify(report, null, 2)}\n`,
      "utf8"
    )

    const failures = [
      ...inventory.flatMap((chapter) => chapter.issues.map((issue) => `R${chapter.chapter - 24}: ${issue}`)),
      ...svgGeometry.flatMap((entry) =>
        entry.issues.map((issue) => `${entry.relativePath}: ${issue.type} ${issue.detail}`)
      )
    ]

    console.log(
      JSON.stringify(
        {
          chapters: inventory.length,
          pngTotal: inventory.reduce((sum, chapter) => sum + chapter.png.length, 0),
          svgTotal: inventory.reduce((sum, chapter) => sum + chapter.svg.length, 0),
          contactSheets,
          svgFilesWithIssues: svgGeometry.filter((entry) => entry.issues.length > 0),
          failures
        },
        null,
        2
      )
    )

    if (failures.length > 0) process.exitCode = 1
  } finally {
    await browser.close()
  }
}

async function collectInventory() {
  const inventory = []

  for (const chapter of CHAPTERS) {
    const chapterName = `chapter-${String(chapter).padStart(2, "0")}`
    const dir = path.join(ASSET_ROOT, chapterName)
    const names = (await fs.readdir(dir)).sort()
    const png = names.filter((name) => name.endsWith(".png"))
    const svg = names.filter((name) => name.endsWith(".svg"))
    const issues = []

    if (png.length !== EXPECTED_PER_CHAPTER) {
      issues.push(`attesi ${EXPECTED_PER_CHAPTER} PNG, trovati ${png.length}`)
    }
    if (chapter <= 33 && svg.length !== EXPECTED_PER_CHAPTER) {
      issues.push(`attesi ${EXPECTED_PER_CHAPTER} SVG master, trovati ${svg.length}`)
    }

    inventory.push({
      chapter,
      module: `R${chapter - 24}`,
      relativeDir: path.relative(ROOT, dir).replaceAll("\\", "/"),
      png,
      svg,
      issues
    })
  }

  return inventory
}

async function auditSvgGeometry(browser, inventory) {
  const results = []

  for (const chapter of inventory) {
    for (const file of chapter.svg) {
      const absolutePath = path.join(ROOT, chapter.relativeDir, file)
      const svg = await fs.readFile(absolutePath, "utf8")
      const page = await browser.newPage({
        viewport: { width: 1600, height: 900 },
        deviceScaleFactor: 1
      })

      try {
        await page.setContent(svg, { waitUntil: "load" })
        const audit = await page.evaluate(() => {
          const root = document.querySelector("svg")
          if (!root) throw new Error("SVG root assente")

          const viewBox = root.viewBox.baseVal
          const fuzz = 2
          const issues = []
          const textNodes = Array.from(root.querySelectorAll("text"))
          const rectNodes = Array.from(root.querySelectorAll("rect"))

          function round(value) {
            return Number(value.toFixed(2))
          }

          function boxOf(node) {
            const box = node.getBBox()
            return {
              x: box.x,
              y: box.y,
              width: box.width,
              height: box.height,
              right: box.x + box.width,
              bottom: box.y + box.height
            }
          }

          function serialise(box) {
            return {
              x: round(box.x),
              y: round(box.y),
              width: round(box.width),
              height: round(box.height)
            }
          }

          function textLabel(node) {
            return (node.textContent || "").replace(/\s+/g, " ").trim()
          }

          function safeBoxFor(node) {
            let parent = node.parentElement
            while (parent && parent !== root) {
              const value = parent.getAttribute("data-safe-box")
              if (value) {
                const [x, y, width, height, padding = 0] = value.split(/\s+/).map(Number)
                return {
                  x: x + padding,
                  y: y + padding,
                  right: x + width - padding,
                  bottom: y + height - padding,
                  name: parent.getAttribute("data-safe-name") || "container"
                }
              }
              parent = parent.parentElement
            }

            return {
              x: viewBox.x + 24,
              y: viewBox.y + 12,
              right: viewBox.x + viewBox.width - 24,
              bottom: viewBox.y + viewBox.height - 12,
              name: "viewBox"
            }
          }

          const textBoxes = textNodes.map((node) => ({
            node,
            label: textLabel(node),
            box: boxOf(node),
            screenBox: node.getBoundingClientRect()
          }))

          for (const entry of textBoxes) {
            const safe = safeBoxFor(entry.node)
            if (
              entry.box.x < safe.x - fuzz ||
              entry.box.y < safe.y - fuzz ||
              entry.box.right > safe.right + fuzz ||
              entry.box.bottom > safe.bottom + fuzz
            ) {
              issues.push({
                type: "text-outside-safe-box",
                detail: `"${entry.label}" esce da ${safe.name}`,
                box: serialise(entry.box)
              })
            }

            const centerX = entry.screenBox.left + entry.screenBox.width / 2
            const centerY = entry.screenBox.top + entry.screenBox.height / 2
            const containingRects = rectNodes
              .map((node) => ({ node, box: node.getBoundingClientRect() }))
              .filter(({ box }) => {
                const viewportArea = viewBox.width * viewBox.height
                const area = box.width * box.height
                return (
                  area < viewportArea * 0.92 &&
                  centerX >= box.left &&
                  centerX <= box.right &&
                  centerY >= box.top &&
                  centerY <= box.bottom &&
                  box.width >= entry.screenBox.width &&
                  box.height >= entry.screenBox.height
                )
              })
              .sort(
                (left, right) =>
                  left.box.width * left.box.height - right.box.width * right.box.height
              )

            if (containingRects.length > 0) {
              const container = containingRects[0].box
              const padding = 3
              if (
                entry.screenBox.left < container.left + padding ||
                entry.screenBox.top < container.top + padding ||
                entry.screenBox.right > container.right - padding ||
                entry.screenBox.bottom > container.bottom - padding
              ) {
                issues.push({
                  type: "text-rect-collision",
                  detail: `"${entry.label}" tocca o supera il rettangolo contenitore`,
                  box: {
                    x: round(entry.screenBox.left),
                    y: round(entry.screenBox.top),
                    width: round(entry.screenBox.width),
                    height: round(entry.screenBox.height)
                  }
                })
              }
            }
          }

          for (let leftIndex = 0; leftIndex < textBoxes.length; leftIndex += 1) {
            for (let rightIndex = leftIndex + 1; rightIndex < textBoxes.length; rightIndex += 1) {
              const left = textBoxes[leftIndex]
              const right = textBoxes[rightIndex]
              const overlapWidth =
                Math.min(left.box.right, right.box.right) - Math.max(left.box.x, right.box.x)
              const overlapHeight =
                Math.min(left.box.bottom, right.box.bottom) - Math.max(left.box.y, right.box.y)

              if (overlapWidth > fuzz && overlapHeight > fuzz) {
                issues.push({
                  type: "text-overlap",
                  detail: `"${left.label}" interseca "${right.label}"`,
                  box: {
                    x: round(Math.max(left.box.x, right.box.x)),
                    y: round(Math.max(left.box.y, right.box.y)),
                    width: round(overlapWidth),
                    height: round(overlapHeight)
                  }
                })
              }
            }
          }

          return {
            viewBox: {
              x: viewBox.x,
              y: viewBox.y,
              width: viewBox.width,
              height: viewBox.height
            },
            textCount: textNodes.length,
            issues
          }
        })

        results.push({
          chapter: chapter.chapter,
          module: chapter.module,
          file,
          relativePath: path.relative(ROOT, absolutePath).replaceAll("\\", "/"),
          ...audit
        })
      } finally {
        await page.close()
      }
    }
  }

  return results
}

async function createContactSheets(browser, inventory) {
  const groups = []
  for (let index = 0; index < inventory.length; index += 4) {
    groups.push(inventory.slice(index, index + 4))
  }

  const paths = []

  for (const group of groups) {
    const page = await browser.newPage({
      viewport: { width: 2240, height: 1200 },
      deviceScaleFactor: 1
    })

    await page.route("http://ricettario-assets/**", async (route) => {
      const url = new URL(route.request().url())
      const relative = decodeURIComponent(url.pathname.slice(1))
      const absolute = path.join(ASSET_ROOT, relative)
      const body = await fs.readFile(absolute)
      await route.fulfill({ status: 200, contentType: "image/png", body })
    })

    const rows = group
      .map((chapter) => {
        const cards = chapter.png
          .map(
            (file) => `
              <figure>
                <div class="image-frame">
                  <img src="http://ricettario-assets/chapter-${String(chapter.chapter).padStart(2, "0")}/${encodeURIComponent(file)}" alt="">
                </div>
                <figcaption>${escapeHtml(file.replace(/\.png$/i, ""))}</figcaption>
              </figure>`
          )
          .join("")

        return `
          <section>
            <h2>${chapter.module} · Capitolo ${chapter.chapter}</h2>
            <div class="grid">${cards}</div>
          </section>`
      })
      .join("")

    await page.setContent(
      `<!doctype html>
      <html lang="it">
        <head>
          <meta charset="utf-8">
          <style>
            * { box-sizing: border-box; }
            html, body { margin: 0; background: #ede8de; color: #152238; }
            body { font-family: Arial, Helvetica, sans-serif; padding: 34px; }
            header { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 24px; }
            h1 { margin: 0; font-size: 30px; letter-spacing: .03em; }
            header p { margin: 0; color: #6d2534; font-size: 16px; }
            section { margin: 0 0 28px; padding: 20px; background: #fffdf8; border: 1px solid #c9c0b1; border-radius: 18px; }
            h2 { margin: 0 0 14px; font-size: 20px; }
            .grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 12px; }
            figure { min-width: 0; margin: 0; }
            .image-frame { aspect-ratio: 16 / 10.66; display: grid; place-items: center; overflow: hidden; background: white; border: 1px solid #c8cdd4; border-radius: 8px; }
            img { display: block; width: 100%; height: 100%; object-fit: contain; }
            figcaption { min-height: 31px; padding-top: 6px; color: #4e5865; font-size: 10px; line-height: 1.25; overflow-wrap: anywhere; }
          </style>
        </head>
        <body>
          <header>
            <h1>Ricettario · audit immagini</h1>
            <p>Precisione Civica · allineamento, gerarchia, collisioni</p>
          </header>
          ${rows}
        </body>
      </html>`,
      { waitUntil: "networkidle" }
    )

    await page.waitForFunction(() =>
      Array.from(document.images).every(
        (image) => image.complete && image.naturalWidth > 0 && image.naturalHeight > 0
      )
    )

    const first = group[0].module.toLowerCase()
    const last = group[group.length - 1].module.toLowerCase()
    const output = path.join(OUTPUT_ROOT, `contact-${first}-${last}.png`)
    await page.screenshot({ path: output, fullPage: true })
    paths.push(path.relative(ROOT, output).replaceAll("\\", "/"))
    await page.close()
  }

  return paths
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
