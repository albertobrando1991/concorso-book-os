import fs from "node:fs"
import path from "node:path"

await import("tsx/esm")
const { parseFrontmatter } = await import("../src/server/wiki/frontmatter.ts")

const projectRoot = process.cwd()
const wikiRoot = path.join(projectRoot, "wiki")
const bookIds = [
  "moduli/m-fc01-ministeri",
  "moduli/m-fc02-agenzie-fiscali",
  "moduli/m-fc03-enti-non-economici"
]
const files = bookIds.flatMap((bookId) => markdownFiles(path.join(wikiRoot, "books", bookId)))
const issues = []
let wikiLinks = 0
let sourceRefs = 0
let assets = 0

for (const file of files) {
  const relative = path.relative(projectRoot, file).split(path.sep).join("/")
  const bookRoot = bookIds
    .map((bookId) => path.join(wikiRoot, "books", bookId))
    .find((root) => file.startsWith(`${root}${path.sep}`) || file === root)
  const content = fs.readFileSync(file, "utf8")
  const parsed = parseFrontmatter(content)
  const publicationFile = relative.includes("/chapters/") || relative.includes("/front-matter/") || relative.endsWith("/index.md")

  if (/[\u00c3\u00c2\ufffd]/u.test(content)) issues.push(`${relative}: carattere corrotto`)
  if (publicationFile && parsed.data.review_required === true) issues.push(`${relative}: review_required=true`)
  if (publicationFile && !["final", "publication_candidate"].includes(String(parsed.data.status || ""))) {
    issues.push(`${relative}: status=${String(parsed.data.status || "assente")}`)
  }

  for (const ref of array(parsed.data.source_refs)) {
    sourceRefs += 1
    if (!wikiTargetExists(ref)) issues.push(`${relative}: source_ref mancante ${ref}`)
  }
  for (const ref of array(parsed.data.asset_refs)) {
    assets += 1
    const clean = stripWikiPrefix(ref)
    const resolved = clean.startsWith("assets/") && bookRoot
      ? path.join(bookRoot, clean)
      : path.join(wikiRoot, clean)
    if (!fs.existsSync(resolved)) issues.push(`${relative}: asset_ref mancante ${ref}`)
  }

  const seenImages = new Set()
  for (const match of content.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)) {
    const target = match[1].trim().split(/\s+["']/)[0]
    if (/^(?:https?:|data:)/i.test(target)) continue
    assets += 1
    const resolved = path.resolve(path.dirname(file), decodeURIComponent(target))
    if (!fs.existsSync(resolved)) issues.push(`${relative}: immagine mancante ${target}`)
    if (seenImages.has(resolved)) issues.push(`${relative}: immagine duplicata ${target}`)
    seenImages.add(resolved)
  }

  for (const match of content.matchAll(/\[\[([^\]]+)\]\]/g)) {
    const target = match[1].split("|")[0].split("#")[0].trim()
    if (!target) continue
    wikiLinks += 1
    if (!wikiTargetExists(target)) issues.push(`${relative}: link wiki mancante ${target}`)
  }
}

console.log(JSON.stringify({ files: files.length, wikiLinks, sourceRefs, assets, issues }, null, 2))
process.exitCode = issues.length ? 1 : 0

function array(value) {
  return Array.isArray(value) ? value.map(String) : []
}

function stripWikiPrefix(value) {
  return String(value).replace("wiki/", "").replace(`wiki${path.sep}`, "").split(path.sep).join("/")
}

function wikiTargetExists(value) {
  const clean = stripWikiPrefix(String(value).replace(/\.md$/i, ""))
  const candidates = [clean]
  if (!clean.includes("/")) candidates.push(`sources/${clean}`, `topics/${clean}`, `entities/${clean}`)
  return candidates.some((candidate) =>
    fs.existsSync(path.join(wikiRoot, `${candidate}.md`)) ||
    fs.existsSync(path.join(wikiRoot, candidate, "index.md"))
  )
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
