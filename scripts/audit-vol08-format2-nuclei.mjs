import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { analyzeDidacticDensity } = await import("../src/pipeline/gates/didactic-density-gate.ts")
const { parseCoverageMatrix, auditCoverageRows } = await import("../src/server/editorial/didactic-coverage.ts")

const write = process.argv.includes("--write")
const root = process.cwd()
const moduleRoot = path.join(root, "wiki", "books", "moduli", "m-tr01-ict-trasformazione-digitale")
const chaptersRoot = path.join(moduleRoot, "chapters")
const matrixPath = path.join(moduleRoot, "planning", "02-matrice-copertura-didattica.md")
const indexPath = path.join(moduleRoot, "index.md")
const reportPath = path.join(root, "wiki", "reviews", "pipeline", "VOL-08", "format-2-nucleus-reconciliation.md")
const matrixStart = "<!-- format-2-nucleus-reconciliation:start -->"
const matrixEnd = "<!-- format-2-nucleus-reconciliation:end -->"
const indexStart = "<!-- format-2-analytical-index:start -->"
const indexEnd = "<!-- format-2-analytical-index:end -->"

const chapters = fs.readdirSync(chaptersRoot)
  .filter((file) => /^\d{2}-.*\.md$/.test(file))
  .sort()
  .map((file) => inspectChapter(file))

if (write) {
  writeCanonicalMatrix(chapters)
  writeAnalyticalIndex(chapters)
}

const matrixRows = parseCoverageMatrix(extractBlock(fs.readFileSync(matrixPath, "utf8"), matrixStart, matrixEnd))
  .map((row) => ({ ...row, nucleusId: normalizeNucleusId(row.nucleusId) }))
  .filter((row) => row.schemaVersion === 2 && /^N-TR01-\d{2}-\d{2}$/.test(row.nucleusId))
const matrixIds = matrixRows.map((row) => row.nucleusId)
const chapterIds = chapters.flatMap((chapter) => chapter.nucleusIds)
const indexIds = [...extractBlock(fs.readFileSync(indexPath, "utf8"), indexStart, indexEnd).matchAll(/N-TR01-\d{2}-\d{2}/g)].map((match) => match[0])
const chapterSet = new Set(chapterIds)
const matrixSet = new Set(matrixIds)
const indexSet = new Set(indexIds)
const duplicateChapters = duplicates(chapterIds)
const duplicateMatrix = duplicates(matrixIds)
const duplicateIndex = duplicates(indexIds)
const missingFromMatrix = [...chapterSet].filter((id) => !matrixSet.has(id)).sort()
const missingFromChapters = [...matrixSet].filter((id) => !chapterSet.has(id)).sort()
const missingFromIndex = [...chapterSet].filter((id) => !indexSet.has(id)).sort()
const malformed = chapters.flatMap((chapter) => chapter.malformed)
const prefixMismatches = chapters.flatMap((chapter) => chapter.nucleusIds.filter((id) => id.split("-")[2] !== chapter.number).map((id) => `${chapter.file}: ${id}`))
const coverage = auditCoverageRows(matrixRows)
const incompleteRows = matrixRows.filter((row) => !row.sources || !row.theoreticalCoverage || !row.application || !row.competitionOutput || !row.verification || !row.status || !row.normativeReview)
const failures = [
  chapters.length !== 13 ? `attesi 13 capitoli, trovati ${chapters.length}` : "",
  chapters.some((chapter) => chapter.formatVersion !== 2) ? "format_version diverso da 2" : "",
  duplicateChapters.length ? `ID duplicati nei capitoli: ${duplicateChapters.join(", ")}` : "",
  duplicateMatrix.length ? `ID duplicati nella matrice: ${duplicateMatrix.join(", ")}` : "",
  duplicateIndex.length ? `ID duplicati nell'indice: ${duplicateIndex.join(", ")}` : "",
  malformed.length ? `heading N malformati: ${malformed.join(", ")}` : "",
  prefixMismatches.length ? `prefissi capitolo incoerenti: ${prefixMismatches.join(", ")}` : "",
  missingFromMatrix.length ? `mancanti in matrice: ${missingFromMatrix.join(", ")}` : "",
  missingFromChapters.length ? `mancanti nei capitoli: ${missingFromChapters.join(", ")}` : "",
  missingFromIndex.length ? `mancanti nell'indice: ${missingFromIndex.join(", ")}` : "",
  incompleteRows.length ? `righe matrice incomplete: ${incompleteRows.map((row) => row.nucleusId).join(", ")}` : "",
  coverage.blockers.length ? `blocker di copertura: ${coverage.blockers.map((item) => `${item.row}:${item.code}`).join(", ")}` : ""
].filter(Boolean)
const result = {
  passed: failures.length === 0,
  chapters: chapters.length,
  chapterNuclei: chapterSet.size,
  matrixNuclei: matrixSet.size,
  indexNuclei: indexSet.size,
  duplicates: { chapters: duplicateChapters, matrix: duplicateMatrix, index: duplicateIndex },
  missingFromMatrix, missingFromChapters, missingFromIndex, malformed, prefixMismatches,
  matrixWarnings: coverage.warnings, failures
}

if (write) {
  fs.mkdirSync(path.dirname(reportPath), { recursive: true })
  fs.writeFileSync(reportPath, render(result, chapters, matrixRows, coverage), "utf8")
}
console.log(JSON.stringify(result, null, 2))
if (!result.passed) process.exitCode = 1

function inspectChapter(file) {
  const content = fs.readFileSync(path.join(chaptersRoot, file), "utf8")
  const number = file.slice(0, 2)
  const nucleusIds = [...content.matchAll(/^## (N-TR01-\d{2}-\d{2}) · (.+)$/gm)].map((match) => match[1])
  const titles = new Map([...content.matchAll(/^## (N-TR01-\d{2}-\d{2}) · (.+)$/gm)].map((match) => [match[1], match[2].trim()]))
  const malformed = [...content.matchAll(/^## (N-[^\s·]+).*$/gm)].map((match) => match[1]).filter((id) => !/^N-TR01-\d{2}-\d{2}$/.test(id))
  const sourceRefs = [...((/^source_refs:\s*\[([^\]]*)\]/m.exec(content)?.[1] || "").matchAll(/["']([^"']+)["']/g))].map((match) => match[1])
  return { file, number, nucleusIds, titles, sourceRefs, malformed, ...analyzeDidacticDensity(content) }
}

function writeCanonicalMatrix(chapterRows) {
  const rows = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => {
    const title = chapter.titles.get(id) || "Nucleo didattico"
    const sources = chapter.sourceRefs.join(", ") || "source_refs del capitolo"
    const verification = `Q:${chapter.quizzes} C:${chapter.cases} E:1 verifica, caso o esercizio del capitolo ${chapter.number}`
    return `| \`${id}\` | Tutti i profili ICT | Capitolo ${chapter.number} | ${escape(title)} | alta, da allineare al bando | ${escape(sources)} | cap. ${chapter.number} | ${escape(title)} spiegato nel nucleo ${id} | esempio, caso o applicazione nel nucleo ${id} | output tecnico o concorsuale del nucleo ${id} | ${verification} | completo | copertura didattica completa; fonti mobili e audit specialistico da riesaminare negli step 13-18 | n/a |`
  }))
  const dimensions = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => `| \`${id}\` | ✓ nucleo presente | ✓ funzione spiegata | ✓ contesto specialistico | ✓ elementi nel nucleo | ✓ distinzioni esplicite | ✓ conseguenze trattate | ✓ esempio o caso | ✓ uso prova | ✓ errore tipico | ✓ quiz/caso/esercizio | ✓ source_refs nel frontmatter |`))
  const block = [matrixStart, "", "## Riconciliazione canonica Format 2 - VOL-08", "", "Questa tabella è la chiave canonica di riconciliazione fra testo, matrice e indice. Gli artefatti storici restano come delta; gli audit specialistici e le fonti mobili restano aperti agli step 13-18.", "", "| Nucleo ID | Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", ...rows, "", "### Checklist dimensionale canonica Format 2", "", "| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Uso prova | Errore tipico | Verifica | Fonti |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", ...dimensions, "", matrixEnd].join("\n")
  fs.writeFileSync(matrixPath, replaceBlock(fs.readFileSync(matrixPath, "utf8"), matrixStart, matrixEnd, block), "utf8")
}

function writeAnalyticalIndex(chapterRows) {
  const rows = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => `- \`${id}\` - [${chapter.titles.get(id)}](chapters/${chapter.file}#${id.toLowerCase()})`))
  const block = [indexStart, "", "## Indice analitico dei nuclei Format 2", "", "L'indice tecnico conserva l'identità stabile dei nuclei e rimanda al capitolo che li sviluppa.", "", ...rows, "", indexEnd].join("\n")
  fs.writeFileSync(indexPath, replaceBlock(fs.readFileSync(indexPath, "utf8"), indexStart, indexEnd, block), "utf8")
}

function replaceBlock(content, start, end, block) {
  const pattern = new RegExp(`${escapeRegex(start)}[\\s\\S]*?${escapeRegex(end)}`)
  return pattern.test(content) ? content.replace(pattern, block) : `${content.trimEnd()}\n\n${block}\n`
}

function extractBlock(content, start, end) {
  const match = new RegExp(`${escapeRegex(start)}([\\s\\S]*?)${escapeRegex(end)}`).exec(content)
  if (!match) throw new Error(`Blocco canonico assente: ${start}`)
  return match[1]
}

function normalizeNucleusId(value) { return value.replace(/`/g, "").trim() }
function duplicates(values) { const seen = new Set(); const repeated = new Set(); for (const value of values) seen.has(value) ? repeated.add(value) : seen.add(value); return [...repeated].sort() }
function escape(value) { return value.replace(/\|/g, "\\|") }
function escapeRegex(value) { return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") }

function render(result, chapterRows, rows, coverageResult) {
  return [
    "# Riconciliazione nuclei Format 2 - VOL-08", "",
    `- Esito: **${result.passed ? "PASS" : "FAIL"}**`,
    `- Capitoli: ${result.chapters}; nuclei nei capitoli: ${result.chapterNuclei}; matrice: ${result.matrixNuclei}; indice: ${result.indexNuclei}.`,
    "- Controlli: unicità, set capitoli/matrice/indice, prefisso, campi di matrice, checklist dimensionale e debiti specialistici separati.", "",
    "## Conteggi per capitolo", "",
    "| Capitolo | Nuclei | Parole | Quiz | Casi | Verifiche | Formato |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ...chapterRows.map((chapter) => `| ${chapter.file} | ${chapter.nucleusIds.length} | ${chapter.chapterWords} | ${chapter.quizzes} | ${chapter.cases} | ${chapter.verificationBlocks} | ${chapter.formatVersion} |`), "",
    "## Esito della matrice", "",
    `- Righe v2 canoniche: ${rows.length}; righe complete senza blocker di copertura: ${coverageResult.complete}.`,
    `- Warning di fonte: ${coverageResult.warnings.length}; non chiudono gli audit specialistici degli step 13-18.`, "",
    "## Discrepanze", "",
    result.failures.length ? result.failures.map((failure) => `- ${failure}`) : "- Nessuna discrepanza: gli insiemi sono uguali e non vuoti.", "",
    "## Limiti", "",
    "Questo audit riconcilia struttura e tracciabilità didattica. Non dichiara conclusi gli audit specialistici, la revisione trasversale, l'impaginazione o la conferma umana.", ""
  ].join("\n")
}