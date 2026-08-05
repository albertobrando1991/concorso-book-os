import fs from "node:fs"
import path from "node:path"

const args = parseArgs(process.argv.slice(2))
if (!args.output) {
  console.error("Uso: node scripts/aggregate-coverage-matrices.mjs --modules-root <dir> --output <file>")
  process.exit(2)
}

const modulesRoot = path.resolve(args.modulesRoot || path.join(process.cwd(), "wiki", "books", "moduli"))
const output = path.resolve(args.output)
const matrices = findMatrices(modulesRoot)
const generated = [
  "---",
  "type: didactic_coverage_matrix",
  "generated: true",
  `generated_at: ${new Date().toISOString()}`,
  "---",
  "",
  "# Matrice di copertura didattica aggregata",
  "",
  "> File generato dalle matrici autoritative dei moduli. Non modificare a mano.",
  "",
  ...matrices.flatMap((file) => {
    const moduleName = moduleNameOf(file)
    return [`## Fonte modulo: \`${moduleName}\``, "", fs.readFileSync(file, "utf8").trim(), ""]
  })
].join("\n")

fs.mkdirSync(path.dirname(output), { recursive: true })
fs.writeFileSync(output, `${generated.trim()}\n`, "utf8")
console.log(`Aggregate ${matrices.length} matrici in ${output}.`)

function findMatrices(directory) {
  if (!fs.existsSync(directory)) return []
  const found = []
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const target = path.join(directory, entry.name)
    if (entry.isDirectory()) found.push(...findMatrices(target))
    else if (entry.name === "02-matrice-copertura-didattica.md") found.push(target)
  }
  return found.sort()
}

function moduleNameOf(file) {
  const parts = file.split(path.sep)
  const planning = parts.lastIndexOf("planning")
  return planning > 0 ? parts[planning - 1] : path.basename(path.dirname(file))
}

function parseArgs(values) {
  const parsed = {}
  for (let index = 0; index < values.length; index += 1) {
    if (values[index] === "--modules-root") parsed.modulesRoot = values[++index]
    else if (values[index] === "--output") parsed.output = values[++index]
  }
  return parsed
}
