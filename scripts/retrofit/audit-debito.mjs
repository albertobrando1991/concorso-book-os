import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { analyzeDidacticDensity, DEFAULT_DIDACTIC_THRESHOLDS } = await import("../../src/pipeline/gates/didactic-density-gate.ts")
const { parseCoverageMatrix, auditCoverageRows } = await import("../../src/server/editorial/didactic-coverage.ts")

const args = parseArgs(process.argv.slice(2))
const root = path.resolve(args.root || path.join(process.cwd(), "wiki", "books"))
const output = path.resolve(args.output || path.join(process.cwd(), "wiki", "reviews", "retrofit", "00-debito-didattico.md"))
const chapters = findChapters(root)
const records = chapters.map((file) => inspect(file, root))

fs.mkdirSync(path.dirname(output), { recursive: true })
fs.writeFileSync(output, render(records, root), "utf8")

const withoutQuiz = records.filter((record) => record.quizzes === 0).length
const belowWords = records.filter((record) => record.words < DEFAULT_DIDACTIC_THRESHOLDS.minChapterWords).length
console.log(
  `Audit debito didattico: ${records.length} capitoli, ${withoutQuiz} senza quiz, ${belowWords} sotto ${DEFAULT_DIDACTIC_THRESHOLDS.minChapterWords} parole. Report: ${output}`
)

function inspect(file, rootDirectory) {
  const content = fs.readFileSync(file, "utf8")
  const metrics = analyzeDidacticDensity(content)
  const dimensionSample = inspectDimensions(file)
  const a0 = /^## Scheda di lavoro\s*$/m.test(content) || /^### Note di review editoriale\s*$/m.test(content) || /^## Testo editoriale\s*$/m.test(content)
  const a = metrics.formatVersion < 2 || metrics.nuclei.length < DEFAULT_DIDACTIC_THRESHOLDS.minNuclei || metrics.quizzes < DEFAULT_DIDACTIC_THRESHOLDS.minQuizzes
  const b = metrics.chapterWords < DEFAULT_DIDACTIC_THRESHOLDS.minChapterWords || dimensionSample.missing
  const levels = [a0 ? "A0" : "", a ? "A" : "", b ? "B" : ""].filter(Boolean)

  return {
    file: path.relative(rootDirectory, file).replace(/\\/g, "/"),
    words: metrics.chapterWords,
    nuclei: metrics.nuclei.length,
    quizzes: metrics.quizzes,
    cases: metrics.cases,
    dimensions: `${metrics.formatVersion >= 2 ? "checklist v2" : "campionamento richiesto"} · ${dimensionSample.label}`,
    level: levels.join("+") || "conforme"
  }
}

function inspectDimensions(file) {
  const moduleRoot = path.dirname(path.dirname(file))
  const matrix = path.join(moduleRoot, "planning", "02-matrice-copertura-didattica.md")
  if (!fs.existsSync(matrix)) return { label: "matrice assente", missing: false }

  const chapterNumber = /^(\d{2})/.exec(path.basename(file))?.[1]
  const candidates = parseCoverageMatrix(fs.readFileSync(matrix, "utf8"))
    .filter((row) => row.schemaVersion === 2 && (!chapterNumber || row.nucleusId.split("-")[2] === chapterNumber))
    .slice(0, 3)

  if (!candidates.length) return { label: "matrice legacy o capitolo non mappato", missing: false }

  const complete = candidates.filter((row) =>
    !auditCoverageRows([row]).blockers.some((issue) => issue.code === "dimensione-mancante")
  ).length

  return {
    label: `${complete}/${candidates.length} completi`,
    missing: complete < candidates.length
  }
}

function render(records, rootDirectory) {
  const totals = {
    words: records.reduce((sum, record) => sum + record.words, 0),
    withoutQuiz: records.filter((record) => record.quizzes === 0).length,
    belowWords: records.filter((record) => record.words < DEFAULT_DIDACTIC_THRESHOLDS.minChapterWords).length
  }

  return [
    "# Debito didattico del corpus",
    "",
    `- Root analizzata: \`${rootDirectory.replace(/\\/g, "/")}\``,
    `- Capitoli: ${records.length}`,
    `- Parole: ${totals.words}`,
    `- Senza quiz: ${totals.withoutQuiz}`,
    `- Sotto ${DEFAULT_DIDACTIC_THRESHOLDS.minChapterWords} parole: ${totals.belowWords}`,
    "",
    "| Capitolo | Parole | Nuclei | Quiz | Casi | Campione dimensionale | Intervento |",
    "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ...records.map(
      (record) =>
        `| \`${record.file}\` | ${record.words} | ${record.nuclei} | ${record.quizzes} | ${record.cases} | ${record.dimensions} | ${record.level} |`
    ),
    ""
  ].join("\n")
}

function findChapters(rootDirectory) {
  if (!fs.existsSync(rootDirectory)) return []
  const found = []
  for (const entry of fs.readdirSync(rootDirectory, { withFileTypes: true })) {
    const target = path.join(rootDirectory, entry.name)
    if (entry.isDirectory()) found.push(...findChapters(target))
    else if (entry.name.endsWith(".md") && target.split(path.sep).includes("chapters")) found.push(target)
  }
  return found.sort()
}

function parseArgs(values) {
  const parsed = {}
  for (let index = 0; index < values.length; index += 1) {
    if (values[index] === "--root") parsed.root = values[++index]
    else if (values[index] === "--output") parsed.output = values[++index]
  }
  return parsed
}
