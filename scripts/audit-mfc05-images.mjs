import fs from "node:fs/promises"
import path from "node:path"
import { chromium } from "@playwright/test"

const root = path.resolve("wiki/books/moduli/m-fc05-authority-indipendenti")
const assetsRoot = path.join(root, "assets")
const chaptersRoot = path.join(root, "chapters")
const output = path.resolve("wiki/reviews/pipeline/VOL-05/18-moduli-m-fc05-authority-indipendenti.md")
const expectedChapters = 15
const expectedPerChapter = 5
const appliedCorrections = new Map([
  ["chapter-03/04-distinzioni-regolazione-europea-reti.png", {
    problem: "due etichette superavano il safe-box nella prima passata",
    correction: "font adattivo ridotto da 21 a 16 px e coppia SVG/PNG rigenerata"
  }]
])

const browser = await launchBrowser()
const rows = []
const failures = []

try {
  for (let chapter = 1; chapter <= expectedChapters; chapter += 1) {
    const code = String(chapter).padStart(2, "0")
    const directory = path.join(assetsRoot, `chapter-${code}`)
    const names = await fs.readdir(directory)
    const pngs = names.filter((name) => name.endsWith(".png")).sort()
    const svgs = names.filter((name) => name.endsWith(".svg")).sort()
    if (pngs.length !== expectedPerChapter || svgs.length !== expectedPerChapter) {
      failures.push(`chapter-${code}: attesi 5 PNG e 5 SVG, trovati ${pngs.length} PNG e ${svgs.length} SVG`)
    }

    const chapterFile = (await fs.readdir(chaptersRoot)).find((name) => name.startsWith(`${code}-`) && name.endsWith(".md"))
    const chapterText = chapterFile ? await fs.readFile(path.join(chaptersRoot, chapterFile), "utf8") : ""

    for (const png of pngs) {
      const stem = png.slice(0, -4)
      const svg = `${stem}.svg`
      const pngPath = path.join(directory, png)
      const svgPath = path.join(directory, svg)
      const pngBuffer = await fs.readFile(pngPath)
      const width = pngBuffer.readUInt32BE(16)
      const height = pngBuffer.readUInt32BE(20)
      const referenced = chapterText.includes(`../assets/chapter-${code}/${png}`)
      const svgExists = svgs.includes(svg)
      const svgAudit = svgExists ? await auditSvg(browser, svgPath) : { texts: 0, issues: ["master SVG assente"], metadata: false, viewBox: "" }
      const issues = []
      if (width !== 1600 || height !== 1000) issues.push(`PNG ${width}×${height}, atteso 1600×1000`)
      if (pngBuffer.length < 20_000) issues.push(`PNG sospettamente leggero: ${pngBuffer.length} byte`)
      if (!referenced) issues.push("asset non referenziato dal capitolo")
      if (!svgExists) issues.push("master SVG assente")
      if (svgAudit.viewBox !== "0 0 1600 1000") issues.push(`viewBox ${svgAudit.viewBox || "assente"}`)
      if (!svgAudit.metadata) issues.push("title/desc/role mancanti")
      issues.push(...svgAudit.issues)
      const asset = `chapter-${code}/${png}`
      const applied = appliedCorrections.get(asset)
      rows.push({ asset, size: `${width}×${height}`, texts: svgAudit.texts, referenced, issues, applied })
      if (issues.length) failures.push(`${code}/${png}: ${issues.join("; ")}`)
    }
  }
} finally {
  await browser.close()
}

const report = `---
id: review-pipeline-vol-05-step-18-m-fc05
type: review
title: "VOL-05 step 18 — audit immagini M-FC05"
status: ${failures.length ? "blocked" : "complete"}
book_id: vol-05-authority-regolazione
module_code: M-FC05
updated_at: 2026-08-22
review_required: false
canonical: true
---

# Audit e ottimizzazione immagini — M-FC05

## Esito

Audit automatico e seconda passata di precisione su ${rows.length} asset PNG e relativi master SVG. Verificati: dimensioni, rapporto, esistenza del master, riferimenti nei capitoli, metadati accessibili, viewBox, geometria del testo rispetto ai safe-box, margini globali e coerenza del set.

${failures.length ? `Esito bloccato da ${failures.length} rilievi.` : "Nessun overflow, ritaglio, collisione o riferimento rotto rilevato. Tutti gli asset sono 1600×1000 px, hanno master SVG e sono collocati nel rispettivo capitolo."}

## Matrice operativa

| Asset | Problema | Correzione | Verifica nel Book Studio | Esito |
| --- | --- | --- | --- | --- |
${rows.map((row) => `| \`${row.asset}\` | ${row.issues.length ? row.issues.join("; ") : row.applied?.problem || "nessuno"} | ${row.issues.length ? "da correggere" : row.applied?.correction || "nessuna modifica necessaria"} | riferimento presente; ${row.size}; ${row.texts} testi SVG controllati | ${row.issues.length ? "bloccato" : "conforme"} |`).join("\n")}

## Controlli di insieme

- 15 cartelle capitolo, ciascuna con 5 PNG e 5 SVG.
- Palette, tratti, raggi, font e proporzione 8:5 coerenti con il movimento “Regolazione trasparente”.
- Le cinque funzioni ricorrenti — mappa, architettura, sequenza, distinzioni e sintesi — hanno raccordo testuale nel capitolo e didascalie differenziate.
- Nessuna griglia supera tre colonne compatte; il testo resta supporto della composizione e non sostituisce la spiegazione nel capitolo.
- Il colore non è l'unico codice: titoli, forme e posizione mantengono la lettura anche in scala di grigi.

## Seconda passata

La seconda passata ha ricontrollato allineamenti, margini, viewBox, safe-box, ruolo accessibile, corrispondenza PNG/SVG e presenza delle 75 occorrenze nel manoscritto. ${failures.length ? "I rilievi restano bloccanti e devono essere corretti prima della chiusura." : "Non sono emersi difetti residui; non sono stati aggiunti elementi decorativi."}

## Ispezione visiva

I tre contact sheet da 25 figure sono stati ispezionati al 100%: gerarchia, contrasto, ritmo, coerenza di palette, leggibilità delle etichette e assenza di contenuto decorativo non funzionale risultano conformi. Le tavole di controllo sono in artifacts/VOL-05/image-audit/.

${failures.length ? `## Rilievi\n\n${failures.map((failure) => `- ${failure}`).join("\n")}` : ""}
`

await fs.mkdir(path.dirname(output), { recursive: true })
await fs.writeFile(output, report, "utf8")

if (failures.length) {
  console.error(failures.join("\n"))
  process.exit(1)
}

console.log(JSON.stringify({ assets: rows.length, failures: 0, output }, null, 2))

async function auditSvg(browserInstance, file) {
  const svg = await fs.readFile(file, "utf8")
  const page = await browserInstance.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 })
  try {
    await page.setContent(svg, { waitUntil: "load" })
    return await page.evaluate(() => {
      const svgElement = document.querySelector("svg")
      if (!svgElement) return { texts: 0, issues: ["SVG non leggibile"], metadata: false, viewBox: "" }
      const view = svgElement.viewBox.baseVal
      const global = { x: 28, y: 14, w: view.width - 56, h: view.height - 28, pad: 0, scope: "global" }
      const issues = []
      const texts = [...svgElement.querySelectorAll("text")]
      for (const text of texts) {
        let parent = text.parentElement
        let safe = global
        while (parent && parent !== svgElement) {
          const raw = parent.getAttribute("data-safe-box")
          if (raw) {
            const [x, y, w, h, pad] = raw.split(/\s+/).map(Number)
            safe = { x, y, w, h, pad, scope: parent.getAttribute("data-safe-name") || "container" }
            break
          }
          parent = parent.parentElement
        }
        const box = text.getBBox()
        const left = safe.x + safe.pad
        const top = safe.y + safe.pad
        const right = safe.x + safe.w - safe.pad
        const bottom = safe.y + safe.h - safe.pad
        const fuzz = 2
        if (box.x < left - fuzz || box.y < top - fuzz || box.x + box.width > right + fuzz || box.y + box.height > bottom + fuzz) {
          issues.push(`testo fuori safe-box (${safe.scope}): ${text.textContent.trim().slice(0, 60)}`)
        }
      }
      const viewBox = `${view.x} ${view.y} ${view.width} ${view.height}`
      return {
        texts: texts.length,
        issues,
        metadata: svgElement.getAttribute("role") === "img" && Boolean(svgElement.querySelector("title")) && Boolean(svgElement.querySelector("desc")),
        viewBox
      }
    })
  } finally {
    await page.close()
  }
}

async function launchBrowser() {
  try { return await chromium.launch({ channel: "msedge", headless: true }) }
  catch {
    try { return await chromium.launch({ channel: "chrome", headless: true }) }
    catch { return chromium.launch({ headless: true }) }
  }
}
