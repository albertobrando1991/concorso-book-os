import { describe, expect, it } from "vitest"
import { findTableAfterHeading, parseMarkdownTables } from "../../src/server/wiki/markdown-table"

const table = `| Codice | Module id | Priorità |
| --- | --- | --- |
| M-FC02 | moduli/m-fc02-agenzie-fiscali | 1 |
| M-FC01 | moduli/m-fc01-ministeri | 2 |`

describe("parseMarkdownTables", () => {
  it("returns headers, rows, and the heading each table sits under", () => {
    const [parsed] = parseMarkdownTables(`## Moduli\n\n${table}\n`)
    expect(parsed.heading).toBe("Moduli")
    expect(parsed.headers).toEqual(["Codice", "Module id", "Priorità"])
    expect(parsed.rows).toEqual([
      { codice: "M-FC02", "module id": "moduli/m-fc02-agenzie-fiscali", priorità: "1" },
      { codice: "M-FC01", "module id": "moduli/m-fc01-ministeri", priorità: "2" }
    ])
  })
  it("records the source line of every row so errors can point at it", () => {
    const [parsed] = parseMarkdownTables(`## Moduli\n\n${table}\n`)
    expect(parsed.lines).toEqual([5, 6])
  })
  it("finds several tables and keeps their order", () => {
    const parsed = parseMarkdownTables(`## Moduli\n\n${table}\n\n## Capitoli M-FC02\n\n| # | File |\n| --- | --- |\n| 01 | chapters/01-a.md |\n`)
    expect(parsed.map((item) => item.heading)).toEqual(["Moduli", "Capitoli M-FC02"])
  })
  it("keeps escaped pipes, wikilinks with alias, and inline code intact", () => {
    const [parsed] = parseMarkdownTables("| A | B |\n| --- | --- |\n| x \\| y | [[topics/imposta|imposta]] `p | q` |\n")
    expect(parsed.rows[0]).toEqual({ a: "x | y", b: "[[topics/imposta|imposta]] `p | q`" })
  })
  it("pads short rows and drops cells beyond the header count", () => {
    const [parsed] = parseMarkdownTables("| A | B | C |\n| --- | --- | --- |\n| 1 | 2 |\n")
    expect(parsed.rows[0]).toEqual({ a: "1", b: "2", c: "" })
  })
  it("ignores a table without a separator row", () => {
    expect(parseMarkdownTables("| A | B |\n| 1 | 2 |\n")).toEqual([])
  })
  it("returns nothing for markdown without tables", () => {
    expect(parseMarkdownTables("# Titolo\n\nSolo prosa.\n")).toEqual([])
  })
})

describe("findTableAfterHeading", () => {
  const document = `## Moduli\n\n${table}\n\n## Capitoli M-FC02\n\n| # | File |\n| --- | --- |\n| 01 | chapters/01-a.md |\n`
  it("matches a heading exactly, ignoring case", () => {
    expect(findTableAfterHeading(document, "moduli")?.headers).toEqual(["Codice", "Module id", "Priorità"])
  })
  it("matches a heading by regular expression", () => {
    expect(findTableAfterHeading(document, /^capitoli\s+(.+)$/i)?.rows[0]).toEqual({ "#": "01", file: "chapters/01-a.md" })
  })
  it("returns undefined when no heading matches", () => {
    expect(findTableAfterHeading(document, "fonti")).toBeUndefined()
  })
})
