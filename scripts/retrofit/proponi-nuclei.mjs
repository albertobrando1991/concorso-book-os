import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { headingsOf } = await import("../../src/pipeline/gates/chapter-lint-gate.ts")
const { parseCoverageMatrix } = await import("../../src/server/editorial/didactic-coverage.ts")

const args = parseArgs(process.argv.slice(2))
if (!args.chapter || !args.moduleCode) {
  console.error("Uso: node scripts/retrofit/proponi-nuclei.mjs --chapter <file> --module-code M-SA02 [--matrix <file>] [--output <file>]")
  process.exit(2)
}

const chapter = path.resolve(args.chapter)
const content = fs.readFileSync(chapter, "utf8")
const chapterNumber = /^([0-9]{2})/.exec(path.basename(chapter))?.[1] || "00"
const moduleId = String(args.moduleCode).toUpperCase().replace(/^M-/, "")
const excluded = /^(?:obiettivo|mappa bando|errori|checklist|riferimenti|apertura|▣ verifica|domanda|caso|mini-esercizio)/i
const candidates = headingsOf(content).filter((heading) => heading.level === 2 && !excluded.test(heading.text) && !/^N-/.test(heading.text))
const matrixPath = args.matrix || defaultMatrixPath(chapter)
const matrixRows = matrixPath && fs.existsSync(matrixPath) ? parseCoverageMatrix(fs.readFileSync(matrixPath, "utf8")) : []
const proposals = candidates.map((heading, index) => {
  const match = closestMatrixRow(heading.text, matrixRows)
  return {
    heading: heading.text,
    nucleusId: match?.nucleusId || `N-${moduleId}-${chapterNumber}-${String(index + 1).padStart(2, "0")}`,
    matrix: match?.concepts || "nessuna corrispondenza"
  }
})
const lines = [
  `# Proposta nuclei — ${path.basename(chapter)}`,
  "",
  "| Heading esistente | Nucleo ID proposto | Riga matrice più vicina |",
  "| --- | --- | --- |",
  ...proposals.map((proposal) => `| ${escapeCell(proposal.heading)} | ${proposal.nucleusId} | ${escapeCell(proposal.matrix)} |`),
  "",
  "> Proposta automatica: non modifica il capitolo. Richiede approvazione umana e riconciliazione con la matrice.",
  ""
]
const output = lines.join("\n")

if (args.output) {
  fs.mkdirSync(path.dirname(path.resolve(args.output)), { recursive: true })
  fs.writeFileSync(path.resolve(args.output), output, "utf8")
} else {
  console.log(output)
}

function defaultMatrixPath(chapterPath) {
  const chaptersDirectory = path.dirname(chapterPath)
  if (path.basename(chaptersDirectory) !== "chapters") return ""
  return path.join(path.dirname(chaptersDirectory), "planning", "02-matrice-copertura-didattica.md")
}

function closestMatrixRow(heading, rows) {
  const headingTokens = tokens(heading)
  const ranked = rows.map((row) => ({
    row,
    score: [...tokens(`${row.concepts} ${row.theoreticalCoverage}`)].filter((token) => headingTokens.has(token)).length
  })).filter((candidate) => candidate.score > 0).sort((left, right) => right.score - left.score)
  return ranked[0]?.row
}

function tokens(value) {
  const ignored = new Set(["della", "delle", "degli", "alla", "alle", "nelle", "con", "per", "tra", "una", "uno", "gli", "le", "del", "dei", "e"])
  return new Set(String(value).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().split(/[^a-z0-9]+/).filter((token) => token.length > 2 && !ignored.has(token)))
}

function escapeCell(value) {
  return value.replace(/\|/g, "\\|")
}

function parseArgs(values) {
  const parsed = {}
  for (let index = 0; index < values.length; index += 1) {
    if (values[index] === "--chapter") parsed.chapter = values[++index]
    else if (values[index] === "--module-code") parsed.moduleCode = values[++index]
    else if (values[index] === "--matrix") parsed.matrix = values[++index]
    else if (values[index] === "--output") parsed.output = values[++index]
  }
  return parsed
}
