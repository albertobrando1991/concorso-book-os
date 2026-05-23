#!/usr/bin/env node

const args = parseArgs(process.argv.slice(2))
const baseUrl = normalizeBaseUrl(process.env.CONCORSOBOOK_BASE_URL || "http://127.0.0.1:3000")
const secret = process.env.CONCORSOBOOK_WEBHOOK_SECRET || process.env.HERMES_WEBHOOK_SECRET || ""

if (!args.url && !args.query) {
  fail("Missing --url or --query")
}

const payload = {
  url: args.url,
  query: args.query,
  title: args.title,
  sourceType: args.type || "law",
  chapterPath: normalizeChapterPath(args.chapter),
  runWriter: toBoolean(args.writer),
  writerMode: "integrate",
  instruction: args.instruction
}

if (args.contentFile) {
  payload.content = await readTextFile(args.contentFile)
}

for (const key of Object.keys(payload)) {
  if (payload[key] === undefined || payload[key] === "") {
    delete payload[key]
  }
}

const response = await fetch(`${baseUrl}/api/hermes/import-source`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    ...(secret ? { Authorization: `Bearer ${secret}` } : {})
  },
  body: JSON.stringify(payload)
})

const text = await response.text()
let data

try {
  data = JSON.parse(text)
} catch {
  data = { raw: text }
}

if (!response.ok) {
  fail(`Import failed ${response.status}: ${JSON.stringify(data, null, 2)}`)
}

console.log(formatResult(data))

function formatResult(data) {
  const changedFiles = data.ingest?.changedFiles || []
  const warnings = data.warnings || []

  return [
    `Fonte importata: ${data.sourceTitle || "senza titolo"}`,
    `URL: ${data.sourceUrl || payload.url}`,
    data.sourcePath ? `Fonte wiki: ${data.sourcePath}` : "Fonte wiki: non riportata",
    data.rawMarkdownPath ? `Markdown raw: ${data.rawMarkdownPath}` : "Markdown raw: non riportato",
    data.linkedChapterPath ? `Capitolo collegato: ${data.linkedChapterPath}` : "Capitolo collegato: nessuno",
    data.writerResult ? `Writer: eseguito (${data.writerResult.writerProvider})` : "Writer: non eseguito",
    "",
    "File aggiornati:",
    changedFiles.slice(0, 12).map((file) => `- ${file}`).join("\n") || "- nessun file riportato",
    warnings.length > 0 ? "\nAvvisi:\n" + warnings.map((warning) => `- ${warning}`).join("\n") : "",
    data.search ? `\nRicerca:\n- Query: ${data.search.query}\n- Selezionato: ${data.search.selected?.title || "n/d"} (${data.search.selected?.url || "n/d"})` : ""
  ]
    .filter(Boolean)
    .join("\n")
}

function parseArgs(values) {
  const parsed = {}

  for (let index = 0; index < values.length; index += 1) {
    const item = values[index]

    if (!item.startsWith("--")) continue

    const [rawKey, inlineValue] = item.slice(2).split("=", 2)
    const key = toCamelCase(rawKey)
    const next = values[index + 1]

    if (inlineValue !== undefined) {
      parsed[key] = inlineValue
      continue
    }

    if (next && !next.startsWith("--")) {
      parsed[key] = next
      index += 1
      continue
    }

    parsed[key] = "true"
  }

  return parsed
}

function normalizeChapterPath(value) {
  if (!value) return undefined

  const clean = value.trim().replace(/^"|"$/g, "")

  if (clean.startsWith("books/") && clean.endsWith(".md")) {
    return clean
  }

  const slug = clean
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")

  return `books/il-metodo-bando/chapters/${slug}.md`
}

function toBoolean(value) {
  return ["true", "1", "yes", "si", "sì"].includes(String(value || "").toLowerCase())
}

function toCamelCase(value) {
  return value.replace(/-([a-z])/g, (_, letter) => letter.toUpperCase())
}

function normalizeBaseUrl(value) {
  return value.replace(/\/+$/, "")
}

async function readTextFile(filePath) {
  const { readFile } = await import("node:fs/promises")
  return readFile(filePath, "utf8")
}

function fail(message) {
  console.error(message)
  process.exit(1)
}
