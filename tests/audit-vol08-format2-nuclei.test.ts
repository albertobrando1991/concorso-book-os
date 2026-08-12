import { cpSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { join, resolve } from "node:path"
import { spawnSync } from "node:child_process"
import { afterEach, describe, expect, it } from "vitest"

const temporaryRoots: string[] = []
const repositoryRoot = resolve(".")
const script = resolve("scripts/audit-vol08-format2-nuclei.mjs")
const moduleRelative = join("wiki", "books", "moduli", "m-tr01-ict-trasformazione-digitale")

afterEach(() => {
  while (temporaryRoots.length) rmSync(temporaryRoots.pop()!, { recursive: true, force: true })
})

function fixtureRoot() {
  const root = mkdtempSync(join(tmpdir(), "vol08-nuclei-"))
  temporaryRoots.push(root)
  cpSync(join(repositoryRoot, moduleRelative), join(root, moduleRelative), { recursive: true })
  return root
}

function audit(root: string) {
  return spawnSync(process.execPath, [script, "--root", root], {
    cwd: repositoryRoot,
    encoding: "utf8"
  })
}

describe("audit-vol08-format2-nuclei", () => {
  it("rejects an extra valid nucleus ID in the analytical index", () => {
    const root = fixtureRoot()
    const index = join(root, moduleRelative, "index.md")
    writeFileSync(index, `${readFileSync(index, "utf8").replace("<!-- format-2-analytical-index:end -->", "- `N-TR01-99-99` - [intruso](chapters/01-lavorare-ict-pa-ruoli-enti-prove.md#n-tr01-01-01)\n\n<!-- format-2-analytical-index:end -->")}`, "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a nucleus omitted consistently from chapter, matrix, and index because the manifest remains authoritative", () => {
    const root = fixtureRoot()
    const id = "N-TR01-13-07"
    const chapter = join(root, moduleRelative, "chapters", "13-laboratorio-prove-ict.md")
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    const index = join(root, moduleRelative, "index.md")
    for (const file of [chapter, matrix, index]) writeFileSync(file, readFileSync(file, "utf8").replaceAll(id, ""), "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("rejects an analytical-index destination whose chapter or heading does not exist", () => {
    const root = fixtureRoot()
    const index = join(root, moduleRelative, "index.md")
    writeFileSync(index, readFileSync(index, "utf8").replace("chapters/01-lavorare-ict-pa-ruoli-enti-prove.md#n-tr01-01-01", "chapters/missing.md#n-tr01-01-01"), "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("rejects an analytical-index fragment that is not the nucleus anchor", () => {
    const root = fixtureRoot()
    const index = join(root, moduleRelative, "index.md")
    writeFileSync(index, readFileSync(index, "utf8").replace("#n-tr01-01-01", "#wrong-fragment"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a duplicate analytical-index row even when its link is valid", () => {
    const root = fixtureRoot()
    const index = join(root, moduleRelative, "index.md")
    const row = "- `N-TR01-01-01` - [Lavorare nell'ICT](chapters/01-lavorare-ict-pa-ruoli-enti-prove.md#n-tr01-01-01)"
    writeFileSync(index, readFileSync(index, "utf8").replace("<!-- format-2-analytical-index:end -->", `${row}\n<!-- format-2-analytical-index:end -->`), "utf8")
    expect(audit(root).status).not.toBe(0)
  })
  it("rejects the former chapter-level evidence placeholders in a matrix row", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", "source_refs del capitolo"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })
  it("rejects a verified evidence cell that is too short", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", "verified: breve"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("keeps chapter 01 and 13 Q/C/E open until a structured atomic mapping exists", () => {
    const root = fixtureRoot()
    const matrix = readFileSync(join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md"), "utf8")
    expect(matrix.match(/N-TR01-01-\d\d[\s\S]{0,900}Q:\d/g)).toBeNull()
    expect(matrix.match(/N-TR01-13-\d\d[\s\S]{0,900}Q:\d/g)).toBeNull()
  })

  it("rejects an impossible numeric Q/C/E distribution without an atomic mapping", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attivita Q/C/E non attribuita al nucleo; review step 15", "Q:99 C:99 E:99"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })
  it("rejects nonsense verified evidence even when it is long enough", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", "verified: abcdefghijklmnopqrstuvwx."), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a short verified dimensional cell", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: review step 15", "✓ verified: breve"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })
  it("rejects a verified phrase that is only a compressed tail of a sentence", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", "verified: decisione esplicita."), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a verified half-sentence beginning with a connector", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", "verified: e la decisione resta verificabile nel servizio pubblico."), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects evidence that appears only inside a Markdown table in the nucleus", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("## N-TR01-01-02", "| Campo | Nota |\n| --- | --- |\n| prova | La decisione artificiale è verificabile nel servizio pubblico. |\n\n## N-TR01-01-02"), "utf8")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", "verified: La decisione artificiale è verificabile nel servizio pubblico."), "utf8")
    expect(audit(root).status).not.toBe(0)
  })
  it("does not promote a generic sentence merely because it appears in a nucleus", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    const quote = "Questa frase descrive una decisione importante per il servizio pubblico."
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("## N-TR01-01-02", `${quote}\n\n## N-TR01-01-02`), "utf8")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace(/verified: [^|]+/, `verified: ${quote}`), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("accepts the complete curated attestations used by verified ledger records", () => {
    expect(audit(fixtureRoot()).status).toBe(0)
  })

  it("rejects a verified record whose curated attestation is incomplete", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    const manifestPath = join(root, moduleRelative, "planning", "10-manifest-nuclei-format-2.json")
    const quote = "La scelta deve restare tracciabile tramite un controllo verificabile e una fonte dichiarata."
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("## N-TR01-01-02", `${quote}\n\n## N-TR01-01-02`), "utf8")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", `verified: ${quote}`), "utf8")
    const manifest = JSON.parse(readFileSync(manifestPath, "utf8"))
    manifest.attestations = [{ nucleusId: "N-TR01-01-01", evidenceQuote: quote, sourceLocation: "chapters/01-lavorare-ict-pa-ruoli-enti-prove.md#n-tr01-01-01", gateId: "step-15" }]
    writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  for (const reviewer of ['   ', true]) {
    it(`rejects a verified attestation with reviewer ${String(reviewer)}`, () => {
      const root = fixtureRoot()
      const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
      const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
      const manifestPath = join(root, moduleRelative, "planning", "10-manifest-nuclei-format-2.json")
      const quote = "La scelta deve restare tracciabile tramite un controllo verificabile e una fonte dichiarata."
      writeFileSync(chapter, readFileSync(chapter, "utf8").replace("## N-TR01-01-02", `${quote}\n\n## N-TR01-01-02`), "utf8")
      writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", `verified: ${quote}`), "utf8")
      const manifest = JSON.parse(readFileSync(manifestPath, "utf8"))
      manifest.attestations = [{ nucleusId: "N-TR01-01-01", evidenceQuote: quote, sourceLocation: "chapters/01-lavorare-ict-pa-ruoli-enti-prove.md#n-tr01-01-01", reviewer, gateId: "step-15" }]
      writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf8")
      expect(audit(root).status).not.toBe(0)
    })
  }
  it("keeps application and output evidence open after theory attestation", () => {
    const root = fixtureRoot()
    const matrix = readFileSync(join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md"), "utf8")
    const ledger = matrix.split("<!-- format-2-nucleus-reconciliation:start -->")[1].split("<!-- format-2-nucleus-reconciliation:end -->")[0]
    expect(ledger).toContain("verified:")
    expect(ledger).toContain("open: attestazione strutturata richiesta allo step 15")
    expect(ledger).toContain("| parziale |")
  })
  it("accepts the baseline atomic verification mappings", () => {
    expect(audit(fixtureRoot()).status).toBe(0)
  })

  it("rejects a missing atomic verification mapping", () => {
    const root = fixtureRoot(); const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace(/\| `N-TR01-01-01` \| [^\n]+\n/, ""), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a duplicated atomic verification mapping", () => {
    const root = fixtureRoot(); const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace(/(## Apparato di verifica dei nuclei[\s\S]*?\| --- \| --- \|)/, "$1\n| `N-TR01-01-01` | Quiz 1 |"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects an empty or absent verification target", () => {
    const root = fixtureRoot(); const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace(/(\| `N-TR01-01-01` \| )[^\n]+/, "$1"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a target that exists only in a terminal apparatus table", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "10-data-governance-open-data-interoperabilita.md")
    const source = readFileSync(chapter, "utf8")
    const table = source.match(/^## Apparato di verifica dei nuclei[\s\S]*?(?=^## (?!Apparato di verifica dei nuclei))/m)?.[0]
    expect(table).toBeTruthy()
    const withoutTable = source.replace(table!, "").replace("**Quiz 1.** La governance del dato coincide con l'amministrazione tecnica del database?", "**Quiz sostitutivo.** La domanda è stata spostata.")
    writeFileSync(chapter, `${withoutTable.trimEnd()}\n\n${table}\n`, "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a duplicated entire apparatus table", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const source = readFileSync(chapter, "utf8")
    const table = source.match(/^## Apparato di verifica dei nuclei[\s\S]*?(?=^## (?!Apparato di verifica dei nuclei))/m)?.[0]
    expect(table).toBeTruthy()
    writeFileSync(chapter, source.replace(table!, `${table}\n\n${table}`), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("accepts bold labels and numbered group items after Markdown normalization", () => {
    const root = fixtureRoot()
    const cap10 = join(root, moduleRelative, "chapters", "10-data-governance-open-data-interoperabilita.md")
    const cap12 = join(root, moduleRelative, "chapters", "12-procurement-ict-gestione-fornitori.md")
    const cap13 = join(root, moduleRelative, "chapters", "13-laboratorio-prove-ict.md")
    writeFileSync(cap10, readFileSync(cap10, "utf8").replace("| `N-TR01-10-01` | Quiz 1. La governance del dato coincide con l'amministrazione tecnica del database? |", "| `N-TR01-10-01` | **Quiz 1.** La governance del dato coincide con l'amministrazione tecnica del database? |"), "utf8")
    writeFileSync(cap12, readFileSync(cap12, "utf8").replace("| `N-TR01-12-06` | Il fornitore propone una nuova versione il giorno prima del rilascio. Quali evidenze chiedere? |", "| `N-TR01-12-06` | **3.** Il fornitore propone una nuova versione il giorno prima del rilascio. Quali evidenze chiedere? |"), "utf8")
    writeFileSync(cap13, readFileSync(cap13, "utf8").replace("| `N-TR01-13-01` | Leggi la traccia |", "| `N-TR01-13-01` | **Leggi la traccia** |"), "utf8")
    expect(audit(root).status).toBe(0)
  })
  it("rejects a target that is only a prefix of a reader-visible unit", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Quiz |"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a target that contains a reader-visible unit as a substring", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Quiz 2 aggiuntivo |"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a second apparatus table under one heading", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const source = readFileSync(chapter, "utf8")
    const second = "| Nucleo ID | Apparato di verifica |\n| --- | --- |\n| `N-TR01-01-01` | Quiz 2 |"
    writeFileSync(chapter, source.replace("## ▣ Verifica — Profilo, bando e piano specialistico", `${second}\n\n## ▣ Verifica — Profilo, bando e piano specialistico`), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a malformed table-like apparatus row", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Quiz 2 |\n| invalid | Quiz 2 |"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })
  it("ignores apparatus-looking tables inside fenced code", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const fenced = "\n```md\n## Apparato di verifica dei nuclei\n| Nucleo ID | Apparato di verifica |\n| --- | --- |\n| `N-TR01-01-01` | Quiz 2 |\n```\n"
    writeFileSync(chapter, `${readFileSync(chapter, "utf8")}${fenced}`, "utf8")
    expect(audit(root).status).toBe(0)
  })
  it("ignores a nucleus-looking heading inside a fenced code block", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, `${readFileSync(chapter, "utf8")}\n\`\`\`md\n## N-TR01-99-99 · esempio non didattico\n\`\`\`\n`, "utf8")

    expect(audit(root).status).toBe(0)
  })

  it("rejects a target that appears only inside a tilde fenced block", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const source = readFileSync(chapter, "utf8")
      .replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Solo nel fence tilde |")
    writeFileSync(chapter, `${source}\n~~~md\nSolo nel fence tilde\n~~~\n`, "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a target that appears only inside a four-backtick fenced block", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const source = readFileSync(chapter, "utf8")
      .replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Solo nel fence quattro backtick |")
    writeFileSync(chapter, `${source}\n\`\`\`\`md\nSolo nel fence quattro backtick\n\`\`\`\`\n`, "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("does not count an apparatus table that exists only inside a tilde fenced block", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const source = readFileSync(chapter, "utf8")
    const table = source.match(/^## Apparato di verifica dei nuclei[\s\S]*?(?=^## (?!Apparato di verifica dei nuclei))/m)?.[0]
    expect(table).toBeTruthy()
    writeFileSync(chapter, `${source.replace(table!, "").trimEnd()}\n\n~~~md\n${table}\n~~~\n`, "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a target that appears only inside an HTML comment", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const source = readFileSync(chapter, "utf8")
      .replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Solo nel commento HTML |")
    writeFileSync(chapter, `${source}\n<!--\nSolo nel commento HTML\n-->\n`, "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("rejects a target that appears only inside an unclosed HTML comment", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const source = readFileSync(chapter, "utf8")
      .replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Solo nel commento HTML aperto |")
    writeFileSync(chapter, `${source}\n<!--\nSolo nel commento HTML aperto\n`, "utf8")

    expect(audit(root).status).not.toBe(0)
  })

  it("rejects an extra valid nucleus ID row in the verification apparatus", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("| `N-TR01-01-01` | Quiz 2 |", "| `N-TR01-01-01` | Quiz 2 |\n| `N-TR01-99-99` | Quiz 2 |"), "utf8")

    expect(audit(root).status).not.toBe(0)
  })
})
