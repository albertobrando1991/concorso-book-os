import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { auditCoverageRows, parseCoverageMatrix } = await import("../src/server/editorial/didactic-coverage.ts")
const { TEXT_VOLUME_CATALOG } = await import("../src/catalog/text-volumes.ts")

const volumeCode = argumentValue(process.argv.slice(2), "--volume")?.toUpperCase()
const roots = volumeCode ? rootsForVolume(process.cwd(), volumeCode) : [process.cwd()]
const files = roots.flatMap(find).sort()

if (!files.length) {
  console.log("Audit copertura didattica: nessuna matrice *-matrice-copertura-didattica.md trovata.")
  process.exit(0)
}

let blockers = 0
let warnings = 0
let complete = 0

for (const file of files) {
  const rows = parseCoverageMatrix(fs.readFileSync(file, "utf8"))
  const result = auditCoverageRows(rows)
  blockers += result.blockers.length
  warnings += result.warnings.length
  complete += result.complete
  console.log(
    `${path.relative(process.cwd(), file)}: ${rows.length} righe, ${result.complete} complete, ${result.blockers.length} blocker, ${result.warnings.length} warning`
  )
  for (const item of [...result.blockers, ...result.warnings]) {
    console.log(`  riga ${item.row}: ${item.message}`)
  }
}

console.log(`Totale: ${files.length} matrici, ${complete} righe complete, ${blockers} blocker, ${warnings} warning.`)
process.exitCode = blockers ? 1 : 0

function find(root) {
  const found = []
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    if ([".git", ".worktrees", "node_modules"].includes(entry.name)) continue
    const target = path.join(root, entry.name)
    if (entry.isDirectory()) found.push(...find(target))
    else if (entry.name.endsWith("-matrice-copertura-didattica.md")) found.push(target)
  }
  return found.sort()
}

function argumentValue(args, name) {
  const index = args.indexOf(name)
  return index >= 0 ? args[index + 1] : undefined
}

function rootsForVolume(cwd, code) {
  const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === code)
  if (!volume) {
    console.error(`Volume sconosciuto: ${code}`)
    process.exit(2)
  }

  return volume.bookIds
    .map((bookId) => path.join(cwd, "wiki", "books", bookId))
    .filter((directory) => fs.existsSync(directory))
}
