const { chromium } = require("playwright")

async function main() {
  const browser = await chromium.launch({ headless: true })
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1700 },
    deviceScaleFactor: 1
  })

  await page.goto("http://127.0.0.1:3001", {
    waitUntil: "networkidle",
    timeout: 60000
  })

  await page
    .getByRole("button", { name: /11\.\s*Inglese concorsuale essenziale/i })
    .click()
  await page.waitForTimeout(2500)

  const pages = page.locator(".bookPages > .bookPage")
  const count = await pages.count()
  if (count < 4) {
    throw new Error("Meno di 4 pagine nella preview del capitolo 11")
  }

  await pages.nth(3).screenshot({ path: "artifacts/chapter11-page4-preview.png" })

  const diag = await page.evaluate(() => {
    const pageEls = Array.from(document.querySelectorAll(".bookPages > .bookPage"))
    return pageEls.map((el, index) => {
      const footer = el.querySelector(".pageFooter")
      const blocks = Array.from(el.children).filter(
        (node) => !node.classList.contains("pageFooter")
      )
      const contentBottom = blocks.reduce(
        (max, node) => Math.max(max, node.offsetTop + node.offsetHeight),
        0
      )
      const footerTop = footer ? footer.offsetTop : null
      const text = (el.textContent || "").replace(/\s+/g, " ").trim()

      return {
        page: index + 1,
        hasCounts: /Domande rilevate|1\.789|926|651|540|158|125/.test(text),
        overlapsFooter: footerTop ? contentBottom > footerTop - 2 : false,
        bottomWhitespace: footerTop
          ? Math.round(footerTop - contentBottom)
          : Math.round(el.clientHeight - contentBottom),
        textStart: text.slice(0, 220)
      }
    })
  })

  console.log(
    JSON.stringify(
      {
        pages: count,
        page4: diag[3],
        overlapPages: diag.filter((entry) => entry.overlapsFooter),
        tightPages: diag.filter((entry) => entry.bottomWhitespace < 24),
        anyOverlap: diag.some((entry) => entry.overlapsFooter),
        anyCounts: diag.some((entry) => entry.hasCounts)
      },
      null,
      2
    )
  )

  await browser.close()
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
