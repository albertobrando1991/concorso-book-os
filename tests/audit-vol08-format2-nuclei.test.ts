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

  it("rejects the former chapter-level evidence placeholders in a matrix row", () => {
    const root = fixtureRoot()
    const matrix = join(root, moduleRelative, "planning", "02-matrice-copertura-didattica.md")
    writeFileSync(matrix, readFileSync(matrix, "utf8").replace("quesito del nucleo:", "verifica, caso o esercizio del capitolo"), "utf8")
    expect(audit(root).status).not.toBe(0)
  })
  it("ignores a nucleus-looking heading inside a fenced code block", () => {
    const root = fixtureRoot()
    const chapter = join(root, moduleRelative, "chapters", "01-lavorare-ict-pa-ruoli-enti-prove.md")
    writeFileSync(chapter, `${readFileSync(chapter, "utf8")}\n\`\`\`md\n## N-TR01-99-99 · esempio non didattico\n\`\`\`\n`, "utf8")

    expect(audit(root).status).toBe(0)
  })
})
