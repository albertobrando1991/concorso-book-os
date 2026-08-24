import { createHash } from "node:crypto"
import { readdir, readFile, writeFile } from "node:fs/promises"
import path from "node:path"

const roots = [
  "wiki/books/moduli/m-fc01-ministeri",
  "wiki/books/moduli/m-fc02-agenzie-fiscali"
].map((value) => path.resolve(value))

for (const root of roots) {
  for (const file of await markdownFiles(root)) {
    if (file.endsWith("04-text-freeze-manifest.md")) continue
    const content = (await readFile(file, "utf8")).replace(/\r\n/g, "\n")
    const match = content.match(/^(---\n[\s\S]*?\n---\n)([\s\S]*)$/)
    if (!match) continue

    const header = match[1]
      .replace(/^status: .+$/m, "status: final")
      .replace(/^review_required: .+$/m, "review_required: false")
      .replace(/^draft_stage: .+$/m, "draft_stage: text_frozen")
      .replace(/^updated_at: .+$/m, "updated_at: 2026-08-22T14:30:00+02:00")
      .replace(/professional-draft/g, "text-frozen")
    const normalized = header + match[2].replace(/[ \t]+$/gm, "")
    if (normalized !== content) await writeFile(file, normalized, "utf8")
  }
}

await refreshManifest(
  path.resolve("wiki/books/moduli/m-fc01-ministeri"),
  path.resolve("wiki/books/moduli/m-fc01-ministeri/planning/04-text-freeze-manifest.md")
)

async function markdownFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true })
  const files = []
  for (const entry of entries) {
    const target = path.join(directory, entry.name)
    if (entry.isDirectory()) files.push(...await markdownFiles(target))
    else if (entry.isFile() && entry.name.endsWith(".md")) files.push(target)
  }
  return files
}

async function refreshManifest(root, manifestPath) {
  let manifest = await readFile(manifestPath, "utf8")
  const matches = [...manifest.matchAll(/^\| `([^`]+)` \| frozen \| `([a-f0-9]{64})` \|$/gm)]
  for (const match of matches) {
    const bytes = await readFile(path.join(root, match[1]))
    const hash = createHash("sha256").update(bytes).digest("hex")
    manifest = manifest.replace(match[0], `| \`${match[1]}\` | frozen | \`${hash}\` |`)
  }
  await writeFile(manifestPath, manifest, "utf8")
}
