import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { analyzeDidacticDensity } = await import("../src/pipeline/gates/didactic-density-gate.ts")
const { parseCoverageMatrix, parseVerificationCounts, auditCoverageRows } = await import("../src/server/editorial/didactic-coverage.ts")

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
const canonicalMatrix = extractBlock(fs.readFileSync(matrixPath, 'utf8'), matrixStart, matrixEnd)
const invalidAttestations = validateVerifiedAttestations(canonicalMatrix)
const invalidDimensionStates = [...canonicalMatrix.matchAll(/(?:✓|âœ“)\s*open:/g)].map((_, index) => `dimensione aperta con spunta alla riga ${index + 1}`)
const invalidNumericQce = matrixRows.filter((row) => /(?:^|\s)Q\s*:\s*\d+\s+C\s*:\s*\d+\s+E\s*:\s*\d+(?=\s|$)/i.test(row.verification || "") && !matchesAtomicVerificationCounts({ ...row, verificationCounts: parseVerificationCounts(row.verification) }))
const invalidOpenStates = matrixRows.flatMap((row) => [row.sources, row.theoreticalCoverage, row.application, row.competitionOutput, row.verification].some((value) => !/^(?:open:.*step 1[3-8]|verified:|Q:\d+\s+C:\d+\s+E:\d+)/i.test(value || '')) ? [row.nucleusId] : [])
const genericEvidenceRows = matrixRows.filter((row) => /source_refs del capitolo|esempio, caso o applicazione nel nucleo|output tecnico o concorsuale del nucleo|verifica, caso o esercizio del capitolo/i.test(`${row.sources} ${row.application} ${row.competitionOutput} ${row.verification}`))
const apparatusFailures = chapters.flatMap((chapter) => validateVerificationApparatus(chapter).map((failure) => `${chapter.file}: ${failure}`))
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
  invalidAttestations.length ? `attestazioni verified non valide: ${invalidAttestations.join(', ')}` : "",
  invalidDimensionStates.length ? `dimensioni aperte marcate con spunta: ${invalidDimensionStates.join(', ')}` : "",
  invalidNumericQce.length ? `Q/C/E non coerenti con il mapping atomico: ${invalidNumericQce.map((row) => row.nucleusId).join(', ')}` : "",
  invalidOpenStates.length ? `stati open senza reviewTarget: ${invalidOpenStates.join(', ')}` : "",
  genericEvidenceRows.length ? `evidenze non atomiche nella matrice: ${genericEvidenceRows.map((row) => row.nucleusId).join(', ')}` : "",
  apparatusFailures.length ? `apparati di verifica non validi: ${apparatusFailures.join(', ')}` : "",
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
  const sections = new Map(matches.map((match, index) => [match[1], content.slice(match.index + match[0].length, index + 1 < matches.length ? matches[index + 1].index : content.length)]))
  const malformed = [...content.matchAll(/^## (N-[^\s\u00b7]+).*$/gm)].map((match) => match[1]).filter((id) => !/^N-TR01-\d{2}-\d{2}$/.test(id))
  const sourceRefs = [...((/^source_refs:\s*\[([^\]]*)\]/m.exec(content)?.[1] || '').matchAll(/["']([^"']+)["']/g))].map((match) => match[1])
  return { file, number, nucleusIds, titles, sections, sourceRefs, content, apparatus: parseVerificationApparatus(content), malformed, ...analyzeDidacticDensity(content) }
}
function parseVerificationApparatus(content) {
  const markers = [...content.matchAll(/^## Apparato di verifica dei nuclei\s*$/gm)]
  const sections = markers.map((marker) => {
    const nextHeading = /^## (?!#)/gm
    nextHeading.lastIndex = (marker.index || 0) + marker[0].length
    const next = nextHeading.exec(content)
    return { start: marker.index || 0, end: next?.index ?? content.length, body: content.slice((marker.index || 0) + marker[0].length, next?.index ?? content.length) }
  })
  const searchable = sections.reduceRight((text, section) => text.slice(0, section.start) + text.slice(section.end), content)
  if (sections.length !== 1) return { rows: [], count: sections.length, rowErrors: [], units: readerVisibleUnits(searchable) }

  const lines = sections[0].body.split(/\r?\n/)
  const headerPattern = /^\|\s*Nucleo ID\s*\|\s*Apparato di verifica\s*\|\s*$/
  const headers = lines.map((line, index) => headerPattern.test(line.trim()) ? index : -1).filter((index) => index >= 0)
  if (headers.length !== 1 || !/^\|\s*---\s*\|\s*---\s*\|\s*$/.test(lines[headers[0] + 1]?.trim() || '')) return { rows: [], count: headers.length, rowErrors: [], units: readerVisibleUnits(searchable) }

  const rows = []
  const rowErrors = []
  for (const line of lines.slice(headers[0] + 2)) {
    if (!line.trim().startsWith('|')) break
    const match = /^\|\s*`(N-TR01-\d{2}-\d{2})`\s*\|\s*(.*?)\s*\|\s*$/.exec(line.trim())
    if (!match) rowErrors.push(line.trim())
    else rows.push({ id: match[1], target: match[2] })
  }
  return { rows, count: 1, rowErrors, units: readerVisibleUnits(searchable) }
}
function readerVisibleUnits(content) {
  const units = new Set()
  for (const rawLine of content.split(/\r?\n/)) {
    const line = rawLine.trim()
    if (!line || line.startsWith('|')) continue
    addReaderUnit(units, line)
    const withoutNumericPrefix = line.replace(/^(?:\*\*)?\d+\.?(?:\*\*)?\s+/, '')
    if (withoutNumericPrefix !== line) addReaderUnit(units, withoutNumericPrefix)
    for (const sentence of line.split(/(?<=[.!?])\s+/)) addReaderUnit(units, sentence)
    const plainLine = line.replace(/[*`]/g, '')
    for (const sentence of plainLine.split(/(?<=[.!?])\s+/)) addReaderUnit(units, sentence)
    for (const match of line.matchAll(/\*\*([^*]+)\*\*/g)) addReaderUnit(units, match[1])
  }
  return units
}
function addReaderUnit(units, value) {
  const normalized = normalizeApparatus(value)
  if (normalized) units.add(normalized)
}
function normalizeApparatus(value) {
  return value
    .replace(/^[#>\s]+/, '')
    .replace(/^[*+-]\s+/, '')
    .replace(/[*`]/g, '')
    .replace(/^(?:\d+\.)\s+/, '')
    .replace(/\\s+/g, ' ')
    .trim()
    .replace(/[.?!]+$/, '')
    .toLowerCase()
}
function validateVerificationApparatus(chapter) {
  const errors = []; const { rows, count, rowErrors, units } = chapter.apparatus
  if (count !== 1) errors.push('table missing or duplicated')
  if (rowErrors.length) errors.push('malformed table row')
  const ids = rows.map((row) => row.id); const expected = new Set(chapter.nucleusIds)
  for (const id of chapter.nucleusIds) if (!ids.includes(id)) errors.push(`missing ${id}`)
  for (const id of duplicates(ids)) errors.push(`duplicate ${id}`)
  for (const id of ids.filter((id) => !expected.has(id))) errors.push(`extra ${id}`)
  for (const row of rows) {
    const target = normalizeApparatus(row.target)
    if (!target) errors.push(`empty target ${row.id}`)
    else if (!units.has(target)) errors.push(`missing target ${row.id}`)
  }
  return errors
}
function writeCanonicalMatrix(chapterRows) {
  const rows = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => {
    const title = chapter.titles.get(id) || 'Nucleo didattico'
    const source = manifest.chapters.find((item) => item.file === chapter.file)?.sourceRef || 'fonte non dichiarata'
    const verification = 'open: attivita Q/C/E non attribuita al nucleo; review step 15'
    return `| \`${id}\` | Tutti i profili ICT | Capitolo ${chapter.number} | ${escape(title)} | alta, da allineare al bando | ${escape(`open: ${source}; attribuzione al nucleo da riesaminare allo step 15`)} | cap. ${chapter.number}, ${id} | ${escape(openEvidence())} | ${escape(openEvidence())} | ${escape(openEvidence())} | ${escape(verification)} | parziale | attribuzione della fonte al nucleo e review normativa aperte allo step 15 |  n/a |`
  }))
  const dimensions = chapterRows.flatMap((chapter) => chapter.nucleusIds.map((id) => {
    const source = manifest.chapters.find((item) => item.file === chapter.file)?.sourceRef || 'fonte non dichiarata'
    return `| \`${id}\` | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: review step 15 | ✗ open: attribuzione fonte step 15 |`
  }))
  const block = [matrixStart, '', '## Riconciliazione canonica Format 2 - VOL-08', '', 'Il ledger parte fail-closed: tutte le evidenze e dimensioni restano aperte finche uno step 13-18 non registra un attestazione strutturata nel manifest.', '', '| Nucleo ID | Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |', '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |', ...rows, '', '### Checklist dimensionale canonica Format 2', '', '| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Uso prova | Errore tipico | Verifica | Fonti |', '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |', ...dimensions, '', matrixEnd].join('\n')
  fs.writeFileSync(matrixPath, replaceBlock(fs.readFileSync(matrixPath, 'utf8'), matrixStart, matrixEnd, block), 'utf8')
}


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

function stripFenced(content) {
  const withoutComments = content.replace(/<!--[\s\S]*?(?:-->|$)/g, '')
  const visible = []
  let fence = null
  for (const line of withoutComments.split(/\r?\n/)) {
    if (!fence) {
      const opener = /^ {0,3}(`{3,}|~{3,})(.*)$/.exec(line)
      if (opener) {
        fence = { character: opener[1][0], length: opener[1].length }
        continue
      }
      visible.push(line)
      continue
    }
    const escaped = escapeRegex(fence.character)
    const closer = new RegExp('^ {0,3}' + escaped + '{' + fence.length + ',}\\s*$')
    if (closer.test(line)) fence = null
  }
  return visible.join('\n')
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

function openEvidence() { return 'open: attestazione strutturata richiesta allo step 15' }
function validateVerifiedAttestations(block) {
  const failures = []
  for (const line of block.split(/\r?\n/)) {
    const id = /`(N-TR01-\d{2}-\d{2})`/.exec(line)?.[1]
    if (!id) continue
    const chapter = chapters.find((item) => item.nucleusIds.includes(id))
    const section = chapter?.sections.get(id) || ''
    const primaryCells = line.split('|').slice(1, -1)
    for (const match of line.matchAll(/verified:\s*([^|]+)/g)) {
      const quote = match[1].trim()
      const cellIndex = primaryCells.findIndex((cell) => cell.includes(`verified: ${quote}`))
      const expectedDimension = primaryCells.length === 14 ? ({ 8: 'application', 9: 'competition-output' }[cellIndex]) : undefined
      const didacticRecord = (manifest.didacticAttestations || []).find((item) => item.nucleusId === id && item.dimension === expectedDimension && item.evidenceQuote === quote)
      if (didacticRecord) {
        if (!validDidacticAttestation(didacticRecord, chapter, section)) failures.push(id)
        continue
      }
      const verificationRecord = (manifest.verificationAttestations || []).find((item) => item.nucleusId === id && item.target === quote)
      if (verificationRecord) {
        if (!validVerificationAttestation(verificationRecord, chapter)) failures.push(id)
      } else {
        const record = (manifest.attestations || []).find((item) => item.nucleusId === id && item.evidenceQuote === quote)
        if (!record || !validAttestation(record, chapter, section)) failures.push(id)
      }
    }
  }
  return [...new Set(failures)]
}
function validAttestation(record, chapter, section) {
  return Boolean(record.evidenceQuote && record.sourceLocation && typeof record.reviewer === 'string' && record.reviewer.trim().length > 0 && /^step-(?:13|14|15|16|17|18)$/.test(record.gateId || '') && record.sourceLocation === `chapters/${chapter.file}#${record.nucleusId.toLowerCase()}` && section.includes(record.evidenceQuote))
}
function matchesAtomicVerificationCounts(row) {
  const chapter = chapters.find((item) => item.nucleusIds.includes(row.nucleusId))
  if (!chapter || !row.verificationCounts) return false
  const records = (manifest.verificationAttestations || []).filter((record) => record.nucleusId === row.nucleusId && validVerificationAttestation(record, chapter))
  if (!records.length) return false
  const actual = { quizzes: 0, cases: 0, exercises: 0 }
  for (const record of records) {
    const normalized = normalizeApparatus(record.target)
    if (/\bquiz\b/i.test(normalized)) actual.quizzes += 1
    else if (/\bcaso\b/i.test(normalized)) actual.cases += 1
    else actual.exercises += 1
  }
  return actual.quizzes === row.verificationCounts.quizzes && actual.cases === row.verificationCounts.cases && actual.exercises === row.verificationCounts.exercises
}
function validVerificationAttestation(record, chapter) {
  return Boolean(record.target && typeof record.reviewer === 'string' && record.reviewer.trim().length > 0 && record.gateId === 'step-15' && record.sourceLocation === `chapters/${chapter.file}#apparato-di-verifica-dei-nuclei` && chapter.apparatus.rows.some((row) => row.id === record.nucleusId && normalizeApparatus(row.target) === normalizeApparatus(record.target)))
}

function validDidacticAttestation(record, chapter, section) {
  return Boolean(['application', 'competition-output'].includes(record.dimension) && record.evidenceQuote && typeof record.reviewer === 'string' && record.reviewer.trim().length > 0 && record.gateId === 'step-15' && record.sourceLocation === `chapters/${chapter.file}#${record.nucleusId.toLowerCase()}` && section.includes(record.evidenceQuote))
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
