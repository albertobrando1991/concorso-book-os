import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { analyzeDidacticDensity } = await import("../src/pipeline/gates/didactic-density-gate.ts")
const { parseCoverageMatrix, auditCoverageRows } = await import("../src/server/editorial/didactic-coverage.ts")

const write = process.argv.includes("--write")
const rootArgument = process.argv.indexOf("--root")
const root = rootArgument >= 0 ? path.resolve(process.argv[rootArgument + 1]) : process.cwd()
const moduleRoot = path.join(root, "wiki", "books", "moduli", "m-tr01-ict-trasformazione-digitale")
const chaptersRoot = path.join(moduleRoot, "chapters")
const matrixPath = path.join(moduleRoot, "planning", "02-matrice-copertura-didattica.md")
const indexPath = path.join(moduleRoot, "index.md")
const reportPath = path.join(root, "wiki", "reviews", "pipeline", "VOL-08", "format-2-nucleus-reconciliation.md")
const matrixStart = "<!-- format-2-nucleus-reconciliation:start -->"
const matrixEnd = "<!-- format-2-nucleus-reconciliation:end -->"
const indexStart = "<!-- format-2-analytical-index:start -->"
const indexEnd = "<!-- format-2-analytical-index:end -->"

const manifest = JSON.parse(fs.readFileSync(path.join(moduleRoot, 'planning', '10-manifest-nuclei-format-2.json'), 'utf8'))
const expectedChapterFiles = manifest.chapters.map((chapter) => chapter.file)
const expectedIds = manifest.chapters.flatMap((chapter) => Array.from({ length: chapter.nuclei }, (_, index) => `N-TR01-${chapter.number}-${String(index + 1).padStart(2, '0')}`))
const chapters = expectedChapterFiles.filter((file) => fs.existsSync(path.join(chaptersRoot, file))).map((file) => inspectChapter(file))

if (write) {
  writeCanonicalMatrix(chapters)
  writeAnalyticalIndex(chapters)
}

const matrixRows = parseCoverageMatrix(extractBlock(fs.readFileSync(matrixPath, "utf8"), matrixStart, matrixEnd))
  .map((row) => ({ ...row, nucleusId: normalizeNucleusId(row.nucleusId) }))
  .filter((row) => row.schemaVersion === 2 && /^N-TR01-\d{2}-\d{2}$/.test(row.nucleusId))
const matrixIds = matrixRows.map((row) => row.nucleusId)
const chapterIds = chapters.flatMap((chapter) => chapter.nucleusIds)
const indexRows = parseIndexRows(extractBlock(fs.readFileSync(indexPath, 'utf8'), indexStart, indexEnd))
const indexIds = indexRows.map((row) => row.id)
const chapterSet = new Set(chapterIds)
const matrixSet = new Set(matrixIds)
const indexSet = new Set(indexIds)
const duplicateChapters = duplicates(chapterIds)
const duplicateMatrix = duplicates(matrixIds)
const duplicateIndex = duplicates(indexIds)
const missingFromMatrix = [...chapterSet].filter((id) => !matrixSet.has(id)).sort()
const missingFromChapters = [...matrixSet].filter((id) => !chapterSet.has(id)).sort()
const missingFromIndex = [...chapterSet].filter((id) => !indexSet.has(id)).sort()
const extraInIndex = [...indexSet].filter((id) => !chapterSet.has(id)).sort()
const missingExpected = expectedIds.filter((id) => !chapterSet.has(id)).sort()
const unexpectedChapterIds = [...chapterSet].filter((id) => !expectedIds.includes(id)).sort()
const invalidIndexLinks = indexRows.filter((row) => {
  const file = path.join(chaptersRoot, row.file)
  return !fs.existsSync(file) || row.heading !== row.id.toLowerCase() || !stripFenced(fs.readFileSync(file, 'utf8')).includes(`## ${row.id} ·`)
}).map((row) => `${row.id}: ${row.destination}`)
const malformed = chapters.flatMap((chapter) => chapter.malformed)
const prefixMismatches = chapters.flatMap((chapter) => chapter.nucleusIds.filter((id) => id.split("-")[2] !== chapter.number).map((id) => `${chapter.file}: ${id}`))
const coverage = auditCoverageRows(matrixRows.filter((row) => row.status === 'completo'))
const incompleteRows = matrixRows.filter((row) => !row.sources || !row.theoreticalCoverage || !row.application || !row.competitionOutput || !row.verification || !row.status || !row.normativeReview)
const genericEvidenceRows = matrixRows.filter((row) => /source_refs del capitolo|esempio, caso o applicazione nel nucleo|output tecnico o concorsuale del nucleo|verifica, caso o esercizio del capitolo/i.test(`${row.sources} ${row.application} ${row.competitionOutput} ${row.verification}`))
const failures = [
  chapters.length !== manifest.chapters.length ? `capitoli del manifest mancanti: ${expectedChapterFiles.filter((file) => !fs.existsSync(path.join(chaptersRoot, file))).join(', ')}` : '',
  expectedIds.length !== 82 ? `manifest incoerente: attesi 82 nuclei, dichiarati ${expectedIds.length}` : '',
  chapterSet.size !== expectedIds.length ? `cardinalità nuclei errata: attesi ${expectedIds.length}, trovati ${chapterSet.size}` : '',
  extraInIndex.length ? `ID extra nell'indice: ${extraInIndex.join(', ')}` : '',
  missingExpected.length ? `nuclei attesi dal manifest mancanti: ${missingExpected.join(', ')}` : '',
  unexpectedChapterIds.length ? `nuclei non dichiarati dal manifest: ${unexpectedChapterIds.join(', ')}` : '',
  invalidIndexLinks.length ? `destinazioni indice non valide: ${invalidIndexLinks.join(', ')}` : '',  chapters.length !== 13 ? `attesi 13 capitoli, trovati ${chapters.length}` : "",
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
  genericEvidenceRows.length ? `evidenze non atomiche nella matrice: ${genericEvidenceRows.map((row) => row.nucleusId).join(", ")}` : "",
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
  const content = stripFenced(fs.readFileSync(path.join(chaptersRoot, file), 'utf8'))
  const number = file.slice(0, 2)
  const matches = [...content.matchAll(/^## (N-TR01-\d{2}-\d{2}) \u00b7 (.+)$/gm)]
  const nucleusIds = matches.map((match) => match[1])
  const titles = new Map(matches.map((match) => [match[1], match[2].trim()]))
  const sections = new Map(matches.map((match, index) => [match[1], content.slice(match.index + match[0].length, index + 1 < matches.length ? matches[index + 1].index : content.length).replace(/\s+/g, ' ').trim()]))
  const malformed = [...content.matchAll(/^## (N-[^\s\u00b7]+).*$/gm)].map((match) => match[1]).filter((id) => !/^N-TR01-\d{2}-\d{2}$/.test(id))
  const sourceRefs = [...((/^source_refs:\s*\[([^\]]*)\]/m.exec(content)?.[1] || '').matchAll(/["']([^"']+)["']/g))].map((match) => match[1])
  return { file, number, nucleusIds, titles, sections, sourceRefs, malformed, ...analyzeDidacticDensity(content) }
}
function writeCanonicalMatrix(chapterRows) {
  const rows = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => {
    const title = chapter.titles.get(id) || 'Nucleo didattico'
    const source = manifest.chapters.find((item) => item.file === chapter.file)?.sourceRef || 'fonte non dichiarata'
    const evidence = atomicEvidence(chapter.sections.get(id), id, title)
    const verificationCounts = countVerification(chapter.sections.get(id))
    const verification = `${stateEvidence(evidence.verification)}; Q:${verificationCounts.quiz} C:${verificationCounts.case} E:${verificationCounts.exercise}`
    return `| \`${id}\` | Tutti i profili ICT | Capitolo ${chapter.number} | ${escape(title)} | alta, da allineare al bando | ${escape(`open: ${source}; attribuzione al nucleo da riesaminare allo step 15`)} | cap. ${chapter.number}, ${id} | ${escape(stateEvidence(evidence.theory))} | ${escape(stateEvidence(evidence.application))} | ${escape(stateEvidence(evidence.output))} | ${escape(verification)} | parziale | attribuzione della fonte al nucleo e review normativa aperte allo step 15 |  n/a |`
  }))
  const dimensions = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => {
    const evidence = atomicEvidence(chapter.sections.get(id), id, chapter.titles.get(id))
    const source = manifest.chapters.find((item) => item.file === chapter.file)?.sourceRef || 'fonte non dichiarata'
    return `| \`${id}\` | ✓ ${escape(stateEvidence(evidence.theory))} | ✓ ${escape(stateEvidence(evidence.function))} | ✓ ${escape(stateEvidence(evidence.framing))} | ✓ ${escape(stateEvidence(evidence.elements))} | ✓ ${escape(stateEvidence(evidence.distinctions))} | ✓ ${escape(stateEvidence(evidence.consequences))} | ✓ ${escape(stateEvidence(evidence.application))} | ✓ ${escape(stateEvidence(evidence.output))} | ✓ ${escape(stateEvidence(evidence.error))} | ✓ ${escape(stateEvidence(evidence.verification))} | ✓ ${escape(`open: ${source}; attribuzione al nucleo da riesaminare allo step 15`)} |`
  }))
  const block = [matrixStart, '', '## Riconciliazione canonica Format 2 - VOL-08', '', 'Ogni riga conserva un riscontro testuale estratto dal nucleo corrispondente; questa riconciliazione non chiude gli audit specialistici degli step 13-18.', '', '| Nucleo ID | Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |', '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |', ...rows, '', '### Checklist dimensionale canonica Format 2', '', '| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Uso prova | Errore tipico | Verifica | Fonti |', '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |', ...dimensions, '', matrixEnd].join('\n')
  fs.writeFileSync(matrixPath, replaceBlock(fs.readFileSync(matrixPath, 'utf8'), matrixStart, matrixEnd, block), 'utf8')
}

function atomicEvidence(section, id, title) {
  const text = section || ''
  const sentence = (pattern) => { const found = text.match(new RegExp(`[^.]*${pattern}[^.]*\\.`, 'i'))?.[0]; const value = (found || '').replace(/[|\r\n]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 240); return value.length >= 20 ? value : '' }
  const verification = sentence('Come lo chiede la commissione|In prova|domanda|quesito')
  return {
    theory: sentence('definisce|è |sono |indica|consiste'),
    application: sentence('caso|esempio|applic|scenario|simul|commissione'),
    output: sentence('output|risposta|evidenza|In prova|decisione'),
    verification,
    function: sentence('funzione|serve|permette|assicura'),
    framing: sentence('contesto|ente|amministrazione|pubblico|PA'),
    elements: sentence('elementi|include|comprende|componenti'),
    distinctions: sentence('distingu|differen|non '),
    consequences: sentence('conseguen|quindi|deriva|effetto'),
    error: sentence('Errore da evitare|errore|evita')
  }
}

function stateEvidence(value) { return value ? `verified: ${value}` : 'open: evidenza non osservata; review step 15' }

function writeAnalyticalIndex(chapterRows) {  const rows = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => `- \`${id}\` - [${chapter.titles.get(id)}](chapters/${chapter.file}#${id.toLowerCase()})`))
  const block = [indexStart, "", "## Indice analitico dei nuclei Format 2", "", "L'indice tecnico conserva l'identità stabile dei nuclei e rimanda al capitolo che li sviluppa.", "", ...rows, "", indexEnd].join("\n")
  fs.writeFileSync(indexPath, replaceBlock(fs.readFileSync(indexPath, "utf8"), indexStart, indexEnd, block), "utf8")
}

function parseIndexRows(block) {
  return block.split(/\r?\n/).flatMap((line) => {
    const match = /^-\s+`(N-TR01-\d{2}-\d{2})`\s+-\s+\[[^\]]+\]\(chapters\/([^#)]+)#([^)]+)\)$/.exec(line.trim())
    return match ? [{ id: match[1], destination: `chapters/${match[2]}#${match[3]}`, file: match[2], heading: match[3] }] : []
  })
}

function stripFenced(content) { return content.replace(/^```[^\n]*\n[\s\S]*?^```\s*$/gm, '') }
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
function escape(value) { return value.replace(/[|`\r\n]+/g, " ").replace(/\s+/g, " ").trim() }
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
function countVerification(section) { const text = section || ''; return { quiz: (text.match(/\bquiz\b/gi) || []).length, case: (text.match(/\bcaso\b/gi) || []).length, exercise: (text.match(/\besercizio\b/gi) || []).length } }
