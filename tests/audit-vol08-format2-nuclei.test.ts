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
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", `verified: ${quote}`), "utf8")
    expect(audit(root).status).not.toBe(0)
  })

  it("requires a complete curated attestation before a verified ledger record can pass", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    const manifestPath = join(root, moduleRelative, "planning", "10-manifest-nuclei-format-2.json")
    const quote = "La scelta deve restare tracciabile tramite un controllo verificabile e una fonte dichiarata."
    writeFileSync(chapter, readFileSync(chapter, "utf8").replace("## N-TR01-01-02", `${quote}\n\n## N-TR01-01-02`), "utf8")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("open: attestazione strutturata richiesta allo step 15", `verified: ${quote}`), "utf8")
    const manifest = JSON.parse(readFileSync(manifestPath, "utf8"))
    manifest.attestations = [{ nucleusId: "N-TR01-01-01", evidenceQuote: quote, sourceLocation: "chapters/01-lavorare-ict-pa-ruoli-enti-prove.md#n-tr01-01-01", reviewer: "revisore-specialistico", gateId: "step-15" }]
    writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf8")
    expect(audit(root).status).toBe(0)
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
  it("generates an all-open baseline ledger", () => {
    const root = fixtureRoot()
    const matrix = readFileSync(join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md"), "utf8")
    const ledger = matrix.split("<!-- format-2-nucleus-reconciliation:start -->")[1].split("<!-- format-2-nucleus-reconciliation:end -->")[0]
    expect(ledger).not.toContain("verified:")
  })
  it("ignores a nucleus-looking heading inside a fenced code block", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, `${readFileSync(chapter, "utf8")}\n\`\`\`md\n## N-TR01-99-99 · esempio non didattico\n\`\`\`\n`, "utf8")

    expect(audit(root).status).toBe(0)
  })
})
