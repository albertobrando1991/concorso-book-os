import fs from "node:fs"
import path from "node:path"

const args = parseArgs(process.argv.slice(2))
const root = path.resolve(args.root || path.join(process.cwd(), "wiki", "books"))
const reviewsRoot = path.resolve(args.reviews || path.join(process.cwd(), "wiki", "reviews", "retrofit"))
const write = Boolean(args.write)
const changes = []

for (const file of findChapters(root)) {
  const original = fs.readFileSync(file, "utf8").replace(/\r\n/g, "\n")
  const transformed = cleanChapter(original)
  if (transformed.content === original && transformed.archived.length === 0) continue
  const moduleName = moduleNameOf(file)
  const archive = path.join(reviewsRoot, moduleName, path.basename(file))
  changes.push({ file, archive, ...transformed })

  if (write) {
    fs.writeFileSync(file, transformed.content, "utf8")
    fs.mkdirSync(path.dirname(archive), { recursive: true })
    fs.writeFileSync(
      archive,
      ["# Archivio contratto dello studente", "", `- Capitolo: \`${file.replace(/\\/g, "/")}\``, "", ...transformed.archived, ""].join("\n"),
      "utf8"
    )
  }
}

console.log(`${write ? "Puliti" : "Da pulire"}: ${changes.length} capitoli. ${write ? "Archivi creati" : "Usa --write per applicare"}.`)

export function cleanChapter(content) {
  let lines = content.split("\n")
  const archived = []

  ;({ lines, archived: archived.work } = removeSections(lines, /^##\s+Scheda di lavoro\s*$/i))
  ;({ lines, archived: archived.review } = removeSections(lines, /^###\s+Note di review editoriale\s*$/i))

  const wrapper = lines.findIndex((line) => /^##\s+Testo editoriale\s*$/i.test(line))
  if (wrapper >= 0) {
    const end = nextHeadingAtOrAbove(lines, wrapper + 1, 2)
    for (let index = wrapper + 1; index < end; index += 1) {
      lines[index] = lines[index].replace(/^###(\s+)/, "##$1")
    }
    lines.splice(wrapper, 1)
  }

  return {
    content: normalize(lines.join("\n")),
    archived: [archived.work, archived.review].flat().filter(Boolean)
  }
}

function removeSections(lines, headingPattern) {
  const archived = []
  let index = 0
  while (index < lines.length) {
    if (!headingPattern.test(lines[index])) {
      index += 1
      continue
    }
    const level = headingLevel(lines[index])
    const end = nextHeadingAtOrAbove(lines, index + 1, level)
    archived.push(lines.slice(index, end).join("\n").trim())
    lines.splice(index, end - index)
  }
  return { lines, archived }
}

function nextHeadingAtOrAbove(lines, start, level) {
  const found = lines.findIndex((line, offset) => offset >= start && headingLevel(line) > 0 && headingLevel(line) <= level)
  return found === -1 ? lines.length : found
}

function headingLevel(line) {
  return /^(#{1,6})\s+/.exec(line)?.[1].length ?? 0
}

function normalize(value) {
  return `${value.replace(/\n{3,}/g, "\n\n").trim()}\n`
}

function moduleNameOf(file) {
  const parts = file.split(path.sep)
  const chapters = parts.lastIndexOf("chapters")
  return chapters > 0 ? parts[chapters - 1] : "corpus"
}

function findChapters(directory) {
  if (!fs.existsSync(directory)) return []
  const found = []
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const target = path.join(directory, entry.name)
    if (entry.isDirectory()) found.push(...findChapters(target))
    else if (entry.name.endsWith(".md") && target.split(path.sep).includes("chapters")) found.push(target)
  }
  return found.sort()
}

function parseArgs(values) {
  const parsed = {}
  for (let index = 0; index < values.length; index += 1) {
    if (values[index] === "--root") parsed.root = values[++index]
    else if (values[index] === "--reviews") parsed.reviews = values[++index]
    else if (values[index] === "--write") parsed.write = true
  }
  return parsed
}
