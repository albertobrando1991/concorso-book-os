import crypto from "node:crypto"
import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { parseFrontmatter } = await import("../src/server/wiki/frontmatter.ts")

const projectRoot = process.cwd()
const wikiRoot = path.join(projectRoot, "wiki")
const moduleRoot = path.join(wikiRoot, "books", "moduli", "m-fc05-authority-indipendenti")
const files = markdownFiles(moduleRoot)
const chapters = files.filter((file) => file.includes(`${path.sep}chapters${path.sep}`)).sort()
const issues = []
const counts = { files: files.length, chapters: chapters.length, wikiLinks: 0, sourceRefs: 0, assetRefs: 0, markdownImages: 0, nuclei: 0, answers: 0, tables: 0 }
const imageHashes = new Map()

if (chapters.length !== 15) issues.push(`capitoli: trovati ${chapters.length}, attesi 15`)

for (const file of files) {
  const relative = path.relative(projectRoot, file).split(path.sep).join("/")
  const content = fs.readFileSync(file, "utf8")
  const parsed = parseFrontmatter(content)
  const publicationFile = relative.includes("/chapters/") || relative.endsWith("/index.md")

  if (!relative.includes("/assets/") && (!parsed.data.id || !parsed.data.type)) issues.push(`${relative}: frontmatter privo di id o type`)
  if (/[\u00c3\u00c2\ufffd]/u.test(content)) issues.push(`${relative}: carattere corrotto`)
  if (publicationFile && parsed.data.review_required === true) issues.push(`${relative}: review_required=true`)
  if (publicationFile && parsed.data.status !== "final") issues.push(`${relative}: status=${String(parsed.data.status || "assente")}`)

  const sourceRefs = array(parsed.data.source_refs)
  counts.sourceRefs += sourceRefs.length
  if (relative.includes("/chapters/") && sourceRefs.length === 0) issues.push(`${relative}: source_refs vuoto`)
  for (const ref of sourceRefs) if (!wikiTargetExists(ref)) issues.push(`${relative}: source_ref mancante ${ref}`)

  const assetRefs = array(parsed.data.asset_refs).length ? array(parsed.data.asset_refs) : yamlList(content, "asset_refs")
  for (const ref of assetRefs) {
    counts.assetRefs += 1
    const resolved = path.join(wikiRoot, stripWikiPrefix(ref))
    if (!fs.existsSync(resolved)) issues.push(`${relative}: asset_ref mancante ${ref}`)
    else registerImage(resolved, `${relative}:asset_ref`)
  }

  const seenImages = new Set()
  for (const match of content.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)) {
    const target = match[1].trim().split(/\s+["']/)[0]
    if (/^(?:https?:|data:)/i.test(target)) continue
    counts.markdownImages += 1
    const resolved = path.resolve(path.dirname(file), decodeURIComponent(target))
    if (!fs.existsSync(resolved)) issues.push(`${relative}: immagine mancante ${target}`)
    if (seenImages.has(resolved)) issues.push(`${relative}: immagine duplicata ${target}`)
    seenImages.add(resolved)
  }

  for (const match of content.matchAll(/\[\[([^\]]+)\]\]/g)) {
    const target = match[1].split("|")[0].split("#")[0].trim()
    if (!target) continue
    counts.wikiLinks += 1
    if (!wikiTargetExists(target)) issues.push(`${relative}: link wiki mancante ${target}`)
  }

  const tableIssues = auditTables(content)
  counts.tables += tableIssues.tables
  issues.push(...tableIssues.issues.map((issue) => `${relative}: ${issue}`))

  if (relative.includes("/chapters/")) {
    const body = content.replace(/^---[\s\S]*?---\s*/, "")
    const nuclei = body.match(/^## N-MF05-\d{2}-\d{2}\b/gm)?.length || 0
    const answers = body.match(/Risposta corretta:/g)?.length || 0
    const verify = body.match(/^### ▣ Verifica/gm)?.length || 0
    const h1 = body.match(/^# /gm)?.length || 0
    counts.nuclei += nuclei
    counts.answers += answers
    if (h1 !== 1 || nuclei !== 5 || answers < 6 || verify < 1) {
      issues.push(`${relative}: formato didattico h1=${h1}, nuclei=${nuclei}, risposte=${answers}, verifiche=${verify}`)
    }
  }
}

for (const [hash, refs] of imageHashes) {
  if (refs.length > 1) issues.push(`immagine binaria duplicata ${hash.slice(0, 12)}: ${refs.join(", ")}`)
}

if (counts.nuclei !== 75) issues.push(`nuclei totali ${counts.nuclei}, attesi 75`)
if (counts.assetRefs !== 75 || counts.markdownImages !== 75) {
  issues.push(`asset: frontmatter ${counts.assetRefs}, Markdown ${counts.markdownImages}, attesi 75/75`)
}

console.log(JSON.stringify({ ...counts, duplicateImageHashes: [...imageHashes.values()].filter((refs) => refs.length > 1).length, issues }, null, 2))
process.exitCode = issues.length ? 1 : 0

function array(value) { return Array.isArray(value) ? value.map(String) : [] }
function yamlList(content, key) {
  const frontmatter = content.match(/^---\s*\r?\n([\s\S]*?)\r?\n---/)?.[1] || ""
  const lines = frontmatter.split(/\r?\n/)
  const start = lines.findIndex((line) => line.trim() === `${key}:`)
  if (start < 0) return []
  const values = []
  for (let index = start + 1; index < lines.length && /^\s+-\s+/.test(lines[index]); index += 1) {
    values.push(lines[index].replace(/^\s+-\s+/, "").trim().replace(/^['"]|['"]$/g, ""))
  }
  return values
}
function stripWikiPrefix(value) { return String(value).replace(/^wiki[\\/]/, "").split(/[\\/]/).join(path.sep) }

function wikiTargetExists(value) {
  const clean = stripWikiPrefix(String(value).replace(/\.md$/i, ""))
  const candidates = [clean]
  if (!clean.includes(path.sep)) candidates.push(`sources${path.sep}${clean}`, `topics${path.sep}${clean}`, `entities${path.sep}${clean}`)
  return candidates.some((candidate) => fs.existsSync(path.join(wikiRoot, `${candidate}.md`)) || fs.existsSync(path.join(wikiRoot, candidate, "index.md")))
}

function registerImage(file, ref) {
  if (!file.toLowerCase().endsWith(".png")) return
  const hash = crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex")
  const refs = imageHashes.get(hash) || []
  refs.push(ref)
  imageHashes.set(hash, refs)
}

function auditTables(content) {
  const lines = content.split(/\r?\n/)
  const issues = []
  let tables = 0
  let index = 0
  while (index < lines.length) {
    if (!/^\s*\|.*\|\s*$/.test(lines[index])) { index += 1; continue }
    const start = index
    const group = []
    while (index < lines.length && /^\s*\|.*\|\s*$/.test(lines[index])) group.push(lines[index++])
    tables += 1
    const columns = group.map((line) => line.split("|").length - 2)
    if (group.length < 2 || !/^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$/.test(group[1])) issues.push(`tabella alla riga ${start + 1} priva di separatore valido`)
    if (new Set(columns).size !== 1) issues.push(`tabella alla riga ${start + 1} con colonne incoerenti: ${columns.join("/")}`)
  }
  return { tables, issues }
}

function markdownFiles(root) {
  const found = []
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    const target = path.join(root, entry.name)
    if (entry.isDirectory()) found.push(...markdownFiles(target))
    else if (entry.isFile() && entry.name.endsWith(".md")) found.push(target)
  }
  return found
}
