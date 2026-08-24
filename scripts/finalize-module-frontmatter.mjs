import { readdir, readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'

const [moduleSlug, freezeDate] = process.argv.slice(2)

if (!moduleSlug || !/^m-[a-z0-9-]+$/.test(moduleSlug)) {
  throw new Error('Uso: node scripts/finalize-module-frontmatter.mjs <module-slug> <YYYY-MM-DD>')
}

if (!freezeDate || !/^\d{4}-\d{2}-\d{2}$/.test(freezeDate)) {
  throw new Error('La data di freeze deve avere formato YYYY-MM-DD')
}

const moduleRoot = path.resolve('wiki', 'books', 'moduli', moduleSlug)

async function markdownFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true })
  const nested = await Promise.all(entries.map(async (entry) => {
    const absolute = path.join(directory, entry.name)
    if (entry.isDirectory()) return markdownFiles(absolute)
    return entry.isFile() && entry.name.endsWith('.md') ? [absolute] : []
  }))
  return nested.flat()
}

function replaceField(frontmatter, field, value) {
  const expression = new RegExp(`^${field}:.*$`, 'm')
  return expression.test(frontmatter)
    ? frontmatter.replace(expression, `${field}: ${value}`)
    : `${frontmatter.trimEnd()}\n${field}: ${value}\n`
}

for (const file of await markdownFiles(moduleRoot)) {
  const original = await readFile(file, 'utf8')
  const match = original.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/)
  if (!match) continue

  const relative = path.relative(moduleRoot, file).replaceAll('\\', '/')
  let frontmatter = match[1]
  frontmatter = replaceField(frontmatter, 'review_required', 'false')
  frontmatter = replaceField(frontmatter, 'updated_at', freezeDate)

  if (relative === 'index.md' || relative.startsWith('chapters/')) {
    frontmatter = replaceField(frontmatter, 'status', 'final')
    frontmatter = replaceField(frontmatter, 'draft_stage', 'text_frozen')
  }

  if (relative === 'index.md') {
    frontmatter = replaceField(frontmatter, 'module_status', 'text_freeze')
  }

  const replacement = `---\n${frontmatter.trimEnd()}\n---\n`
  const updated = replacement + original.slice(match[0].length)
  if (updated !== original) {
    await writeFile(file, updated, 'utf8')
    process.stdout.write(`${relative}\n`)
  }
}
