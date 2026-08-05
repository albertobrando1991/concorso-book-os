import fs from "node:fs"
import path from "node:path"

const args = parseArgs(process.argv.slice(2))
const root = path.resolve(args.root || path.join(process.cwd(), "wiki", "books"))
const items = findChapters(root).flatMap(extractItems)
const json = `${JSON.stringify(items, null, 2)}\n`

if (args.output) {
  const output = path.resolve(args.output)
  fs.mkdirSync(path.dirname(output), { recursive: true })
  fs.writeFileSync(output, json, "utf8")
} else {
  process.stdout.write(json)
}

console.error(`Estratti ${items.length} item da ${root}.`)

function extractItems(file) {
  const lines = fs.readFileSync(file, "utf8").replace(/\r\n/g, "\n").split("\n")
  const chapterNumber = /^([0-9]{2})/.exec(path.basename(file))?.[1] || "00"
  const items = []
  let nucleusId = ""
  let questionStart = 0

  for (let index = 0; index < lines.length; index += 1) {
    const nucleus = /^##\s+(N-[A-Z]{2}\d{2}-\d{2}-\d{2})\b/.exec(lines[index])
    if (nucleus) nucleusId = nucleus[1]
    if (/^#{2,6}\s+.*Quiz\b/i.test(lines[index])) questionStart = index + 1
    const answer = /^Risposta corretta\s*:\s*(.+)$/i.exec(lines[index])
    if (!answer) continue

    const moduleId = /^N-([A-Z]{2}\d{2})-/.exec(nucleusId)?.[1] || moduleIdFromPath(file)
    items.push({
      id: `Q-${moduleId}-${chapterNumber}-${String(items.length + 1).padStart(2, "0")}`,
      nucleusId,
      sourceFile: file.replace(/\\/g, "/"),
      question: lines.slice(questionStart, index).join("\n").trim(),
      correctAnswer: answer[1].trim()
    })
  }

  return items
}

function moduleIdFromPath(file) {
  const match = /(?:^|[\\/])m-([a-z]{2}\d{2})(?:[-\\/]|$)/i.exec(file)
  return match ? match[1].toUpperCase() : "UNKN"
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
    else if (values[index] === "--output") parsed.output = values[++index]
  }
  return parsed
}
