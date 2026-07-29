import { existsSync, statSync } from "node:fs"
import path from "node:path"
import { describe, expect, it } from "vitest"

const root = path.resolve(process.cwd(), "wiki/books/moduli/m-fc05-authority-indipendenti/assets/chapter-01")
const figures = [
  "01-mappa-bando-authority",
  "02-authority-settori-poteri",
  "03-percorsi-g-e-p",
  "04-nucleo-comune-delta-authority",
  "05-bando-decoder-authority"
]

describe("asset del capitolo M-FC05 1", () => {
  it("fornisce cinque master SVG e cinque PNG leggibili", () => {
    for (const figure of figures) {
      const svg = path.join(root, `${figure}.svg`)
      const png = path.join(root, `${figure}.png`)

      expect(existsSync(svg), `${figure}.svg`).toBe(true)
      expect(existsSync(png), `${figure}.png`).toBe(true)
      expect(statSync(svg).size, `${figure}.svg non deve essere vuoto`).toBeGreaterThan(1000)
      expect(statSync(png).size, `${figure}.png non deve essere vuoto`).toBeGreaterThan(10000)
    }
  })

  it("conserva una guida di lettura per le cinque figure", () => {
    const readme = path.join(root, "README.md")
    expect(existsSync(readme)).toBe(true)
    expect(statSync(readme).size).toBeGreaterThan(500)
  })
})
