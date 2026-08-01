import { spawnSync } from "node:child_process"
import { existsSync, mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { join, resolve } from "node:path"
import { afterEach, describe, expect, it } from "vitest"

const directories: string[] = []
afterEach(() => directories.splice(0).forEach((directory) => rmSync(directory, { recursive: true, force: true })))

describe("retrofit debt audit", () => {
  it("classifies A0, A and B using the same density thresholds as the gate", () => {
    const cwd = temporaryDirectory()
    const root = join(cwd, "wiki", "books")
    const chapter = join(root, "moduli", "m-test", "chapters", "01-breve.md")
    const matrix = join(root, "moduli", "m-test", "planning", "02-matrice-copertura-didattica.md")
    const output = join(cwd, "wiki", "reviews", "retrofit", "00-debito-didattico.md")
    mkdirSync(join(root, "moduli", "m-test", "chapters"), { recursive: true })
    mkdirSync(join(root, "moduli", "m-test", "planning"), { recursive: true })
    writeFileSync(
      chapter,
      `---\nformat_version: 1\n---\n\n# Breve\n\n## Scheda di lavoro\n\nInterna.\n\n## Testo editoriale\n\n### Nucleo\n\nTesto.\n\n### Note di review editoriale\n\nInterna.`
    )
    writeFileSync(
      matrix,
      [
        "| Nucleo ID | Famiglia/Profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
        "| N-TE01-01-01 | test | test | test | alta | [[sources/test]] | Cap. 01 | teoria | caso | quiz | Q:6 C:1 E:1 | completo | review | |",
        "",
        "| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Errore tipico | Verifica | Fonti |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
        "| N-TE01-01-01 | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |"
      ].join("\n")
    )

    const result = spawnSync(process.execPath, [resolve("scripts/retrofit/audit-debito.mjs"), "--root", root, "--output", output], {
      cwd: resolve("."),
      encoding: "utf8"
    })

    expect(result.status).toBe(0)
    expect(result.stdout).toContain("1 capitoli")
    expect(readFileSync(output, "utf8")).toContain("A0+A+B")
    expect(readFileSync(output, "utf8")).toContain("campionamento richiesto")
    expect(readFileSync(output, "utf8")).toContain("1/1 completi")
  })
})

describe("retrofit contract cleanup", () => {
  it("archives internal sections and flattens the reader-facing editorial wrapper only with --write", () => {
    const cwd = temporaryDirectory()
    const root = join(cwd, "wiki", "books", "moduli", "m-test")
    const chapter = join(root, "chapters", "01-capitolo.md")
    const reviews = join(cwd, "wiki", "reviews", "retrofit")
    mkdirSync(join(root, "chapters"), { recursive: true })
    writeFileSync(
      chapter,
      "# Titolo\n\n## Scheda di lavoro\n\nNota interna.\n\n## Testo editoriale\n\n### Apertura editoriale\n\nTesto lettore.\n\n### Note di review editoriale\n\nReview interna.\n\n### Riferimenti consolidati\n\nFonti."
    )

    const result = spawnSync(
      process.execPath,
      [resolve("scripts/retrofit/pulisci-contratto.mjs"), "--root", root, "--reviews", reviews, "--write"],
      { cwd: resolve("."), encoding: "utf8" }
    )

    expect(result.status).toBe(0)
    const cleaned = readFileSync(chapter, "utf8")
    expect(cleaned).not.toContain("Scheda di lavoro")
    expect(cleaned).not.toContain("Note di review editoriale")
    expect(cleaned).not.toContain("Testo editoriale")
    expect(cleaned).toContain("## Apertura editoriale")
    expect(cleaned).toContain("## Riferimenti consolidati")
    const archive = join(reviews, "m-test", "01-capitolo.md")
    expect(readFileSync(archive, "utf8")).toContain("Nota interna")
    expect(readFileSync(archive, "utf8")).toContain("Review interna")
  })
})

describe("retrofit nucleus proposal", () => {
  it("proposes stable IDs without modifying the chapter", () => {
    const cwd = temporaryDirectory()
    const chapter = join(cwd, "05-triage.md")
    const matrix = join(cwd, "matrice.md")
    writeFileSync(chapter, "# Triage\n\n## Obiettivo del capitolo\n\nTesto.\n\n## Valutazione iniziale\n\nTesto.\n\n## Rivalutazione\n\nTesto.\n\n## Errori e trappole ricorrenti\n\nTesto.")
    writeFileSync(
      matrix,
      "| Famiglia/Profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| sanitario | triage | Valutazione iniziale e priorità | alta | [[sources/triage]] | Cap. 05 | teoria | caso | quiz | test | completo | REV-INF | |"
    )
    const before = readFileSync(chapter, "utf8")
    const result = spawnSync(
      process.execPath,
      [resolve("scripts/retrofit/proponi-nuclei.mjs"), "--chapter", chapter, "--module-code", "M-SA02", "--matrix", matrix],
      { cwd: resolve("."), encoding: "utf8" }
    )

    expect(result.status).toBe(0)
    expect(result.stdout).toContain("N-SA02-05-01")
    expect(result.stdout).toContain("Valutazione iniziale")
    expect(result.stdout).toContain("N-SA02-05-02")
    expect(result.stdout).toContain("Valutazione iniziale e priorità")
    expect(readFileSync(chapter, "utf8")).toBe(before)
  })
})

describe("retrofit item extraction", () => {
  it("creates structured quiz items tagged with their source nucleus", () => {
    const cwd = temporaryDirectory()
    const root = join(cwd, "wiki", "books", "moduli", "m-fc02", "chapters")
    const output = join(cwd, "items.json")
    mkdirSync(root, { recursive: true })
    writeFileSync(
      join(root, "04-imposta.md"),
      "# Imposta\n\n## N-FC02-04-01 · Obbligazione\n\n### Quiz 1\n\nQuale risposta?\n\nA. Uno\nB. Due\n\nRisposta corretta: A. Perché è uno."
    )

    const result = spawnSync(
      process.execPath,
      [resolve("scripts/retrofit/estrai-item.mjs"), "--root", join(cwd, "wiki", "books"), "--output", output],
      { cwd: resolve("."), encoding: "utf8" }
    )

    expect(result.status).toBe(0)
    const items = JSON.parse(readFileSync(output, "utf8"))
    expect(items).toEqual([
      expect.objectContaining({ id: "Q-FC02-04-01", nucleusId: "N-FC02-04-01", correctAnswer: "A. Perché è uno." })
    ])
  })
})

describe("coverage matrix aggregation", () => {
  it("generates a volume matrix from module matrices without changing the sources", () => {
    const cwd = temporaryDirectory()
    const modulesRoot = join(cwd, "wiki", "books", "moduli")
    const source = join(modulesRoot, "m-a", "planning", "02-matrice-copertura-didattica.md")
    const output = join(cwd, "wiki", "books", "volumi", "vol-test", "planning", "02-matrice-copertura-didattica.md")
    mkdirSync(join(modulesRoot, "m-a", "planning"), { recursive: true })
    writeFileSync(source, "# Matrice M-A\n\n| Stato |\n| --- |\n| completo |")
    const before = readFileSync(source, "utf8")

    const result = spawnSync(
      process.execPath,
      [resolve("scripts/aggregate-coverage-matrices.mjs"), "--modules-root", modulesRoot, "--output", output],
      { cwd: resolve("."), encoding: "utf8" }
    )

    expect(result.status).toBe(0)
    expect(readFileSync(output, "utf8")).toContain("Fonte modulo: `m-a`")
    expect(readFileSync(output, "utf8")).toContain("| completo |")
    expect(readFileSync(source, "utf8")).toBe(before)
  })
})

function temporaryDirectory() {
  const directory = mkdtempSync(join(tmpdir(), "retrofit-tools-"))
  directories.push(directory)
  return directory
}
