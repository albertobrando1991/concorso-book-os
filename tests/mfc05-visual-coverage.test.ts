import { existsSync, readFileSync, statSync } from "node:fs"
import path from "node:path"
import { describe, expect, it } from "vitest"

const moduleRoot = path.resolve(process.cwd(), "wiki/books/moduli/m-fc05-authority-indipendenti")

const chapters = [
  "02-indipendenza-governance-accountability-personale",
  "03-regolazione-europea-multilivello-reti-autorita",
  "04-ciclo-regolatorio-consultazione-air-vir",
  "05-vigilanza-istruttoria-ispezioni-dati-prova",
  "06-sanzioni-impegni-rimedi-controllo-giurisdizionale",
  "07-economia-industriale-regolazione-econometria-contabilita",
  "08-agcm-concorrenza-consumatore-pratiche-scorrette",
  "09-arera-energia-gas-acqua-rifiuti-tariffe",
  "10-agcom-comunicazioni-media-utenti-piattaforme",
  "11-consob-mercati-intermediari-tutela-investitore",
  "12-banca-italia-ivass-vigilanza-prudenziale",
  "13-garante-privacy-poteri-procedimenti-cooperazione",
  "14-anac-prevenzione-vigilanza-whistleblowing",
  "15-laboratorio-prove-authority"
]

describe("copertura visiva dei capitoli M-FC05 2-15", () => {
  it("collega cinque infografiche PNG e i relativi master SVG in ogni capitolo", () => {
    for (const [index, chapter] of chapters.entries()) {
      const number = String(index + 2).padStart(2, "0")
      const chapterPath = path.join(moduleRoot, "chapters", `${chapter}.md`)
      const content = readFileSync(chapterPath, "utf8")
      const assetDir = path.join(moduleRoot, "assets", `chapter-${number}`)
      const references = content.match(new RegExp(`!\\[[^\\]]*\\]\\(\.\\./assets/chapter-${number}/[^)]+\\.png\\)`, "g")) || []

      expect(references, `${chapter} deve avere cinque immagini nel corpo`).toHaveLength(5)
      expect((content.match(/asset_refs:/g) || []).length, `${chapter} deve dichiarare asset_refs`).toBe(1)

      for (let sequence = 1; sequence <= 5; sequence += 1) {
        const prefix = `${String(sequence).padStart(2, "0")}-`
        const files = [".svg", ".png"].map((extension) =>
          require("node:fs").readdirSync(assetDir).find((name: string) => name.startsWith(prefix) && name.endsWith(extension))
        )
        for (const file of files) {
          expect(file, `${chapter} figura ${sequence}`).toBeTruthy()
          expect(statSync(path.join(assetDir, file)).size).toBeGreaterThan(1000)
        }
      }
    }
  })
})
