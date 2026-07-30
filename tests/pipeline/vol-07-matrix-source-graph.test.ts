import { createHash } from "node:crypto"
import { execFileSync } from "node:child_process"
import fs from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { parseFrontmatter } from "../../src/server/wiki/frontmatter"

const repositoryRoot = process.cwd()
const wikiRoot = path.join(repositoryRoot, "wiki")

const matrixPaths = [
  "books/moduli/m-sa01-sanita-amministrativa/planning/02-matrice-copertura-didattica.md",
  "books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md",
  "books/moduli/m-sa03-dirigenza-medica-sanitaria/planning/02-matrice-copertura-didattica.md",
  "books/moduli/m-sa04-tecnici-sanitari-prevenzione/planning/02-matrice-copertura-didattica.md"
]

const rawCorpusRoots = [
  "raw/m-sa01-sanita-amministrativa",
  "raw/m-sa02-professioni-sanitarie",
  "raw/m-sa03-dirigenza-medica-sanitaria",
  "raw/m-sa04-tecnici-sanitari-prevenzione"
]

interface RawManifestItem {
  file: string
  bytes: number
  sha256: string
  url?: string
  status?: string
  valid_corpus?: boolean
  failure?: string
  note?: string
}

describe("VOL-07 matrix source graph package", () => {
  it("packages every source note declared or linked by the four matrices", async () => {
    const tracked = trackedFiles()
    const queuedRefs: string[] = []
    const visitedRefs = new Set<string>()
    const issues: string[] = []

    for (const matrixPath of matrixPaths) {
      const content = await fs.readFile(path.join(wikiRoot, matrixPath), "utf8")
      const directRefs = new Set([
        ...declaredSourceRefs(content),
        ...sourceWikilinks(content)
      ])

      expect(directRefs.size, matrixPath).toBeGreaterThan(0)
      queuedRefs.push(...directRefs)
    }

    while (queuedRefs.length > 0) {
      const sourceRef = normalizeSourceRef(queuedRefs.shift() ?? "")
      if (!sourceRef || visitedRefs.has(sourceRef)) continue
      visitedRefs.add(sourceRef)

      const relativePath = `wiki/${sourceRef}.md`
      const absolutePath = path.join(repositoryRoot, relativePath)

      if (!tracked.has(relativePath)) {
        issues.push(`${sourceRef}: source note not packaged`)
      }

      let content: string
      try {
        content = await fs.readFile(absolutePath, "utf8")
      } catch {
        issues.push(`${sourceRef}: source note missing`)
        continue
      }

      const source = parseFrontmatter(content)
      if (source.data.status !== "processed") {
        issues.push(`${sourceRef}: status is not processed`)
      }
      if (typeof source.data.canonical !== "boolean") {
        issues.push(`${sourceRef}: canonical flag is missing`)
      }

      queuedRefs.push(...declaredSourceRefs(content))
    }

    expect(issues).toEqual([])
  })

  it("matches every raw item and excludes Gcore captures from active sources", async () => {
    const tracked = trackedFiles()
    const issues: string[] = []
    const blockedOrChallengeUrls = new Set<string>()

    for (const corpusRoot of rawCorpusRoots) {
      const absoluteCorpusRoot = path.join(wikiRoot, corpusRoot)
      const corpusFiles = await listFiles(absoluteCorpusRoot)
      const manifestPaths = corpusFiles.filter((file) => path.basename(file) === "download-log.json")
      const declaredFiles = new Set<string>()

      expect(manifestPaths.length, corpusRoot).toBeGreaterThan(0)

      for (const manifestPath of manifestPaths) {
        const manifestRelativePath = repositoryRelative(manifestPath)
        if (!tracked.has(manifestRelativePath)) {
          issues.push(`${manifestRelativePath}: manifest not packaged`)
        }

        const items = await readRawManifestItems(manifestPath)
        expect(items.length, manifestRelativePath).toBeGreaterThan(0)

        for (const item of items) {
          const label = `${manifestRelativePath} -> ${item.file || "<missing path>"}`
          const status = item.status ?? "captured"

          if (!item.file) issues.push(`${label}: path missing`)
          if (!Number.isInteger(item.bytes) || item.bytes < 0) {
            issues.push(`${label}: bytes invalid`)
          }
          if (!/^[a-f0-9]{64}$/i.test(item.sha256 ?? "")) {
            issues.push(`${label}: SHA-256 invalid`)
          }
          if (!new Set(["captured", "verified", "blocked"]).has(status)) {
            issues.push(`${label}: status ${status} invalid`)
          }
          if (status === "verified" && item.valid_corpus !== true) {
            issues.push(`${label}: verified item is not valid_corpus`)
          }
          if (status === "blocked" && (item.valid_corpus !== false || !item.failure)) {
            issues.push(`${label}: blocked item lacks failure metadata`)
          }
          if (!item.file) continue

          const rawPath = path.resolve(path.dirname(manifestPath), item.file)
          const manifestDirectory = `${path.resolve(path.dirname(manifestPath))}${path.sep}`
          if (!rawPath.startsWith(manifestDirectory)) {
            issues.push(`${label}: path escapes manifest directory`)
            continue
          }

          const rawRelativePath = repositoryRelative(rawPath)
          declaredFiles.add(rawRelativePath)
          if (!tracked.has(rawRelativePath)) {
            issues.push(`${rawRelativePath}: raw file not packaged`)
          }

          let raw: Buffer
          try {
            raw = await fs.readFile(rawPath)
          } catch {
            issues.push(`${rawRelativePath}: raw file missing`)
            continue
          }

          const sha256 = createHash("sha256").update(raw).digest("hex").toUpperCase()
          if (raw.byteLength !== item.bytes) {
            issues.push(`${rawRelativePath}: bytes ${raw.byteLength} != ${item.bytes}`)
          }
          if (sha256 !== item.sha256.toUpperCase()) {
            issues.push(`${rawRelativePath}: SHA-256 mismatch`)
          }

          const isGcoreChallenge = raw
            .subarray(0, 65_536)
            .toString("utf8")
            .includes("<title>Gcore</title>")

          if ((isGcoreChallenge || status === "blocked") && item.url) {
            blockedOrChallengeUrls.add(item.url)
          }
          if (isGcoreChallenge && status !== "blocked") {
            issues.push(`${label}: Gcore payload is not blocked`)
          }
          if (
            isGcoreChallenge &&
            (item.valid_corpus !== false || item.failure !== "gcore_challenge")
          ) {
            issues.push(`${label}: Gcore payload lacks exclusion metadata`)
          }
          if (isGcoreChallenge && !/Gcore/i.test(item.note ?? "")) {
            issues.push(`${label}: Gcore payload lacks an audit note`)
          }
          if (status === "blocked" && !isGcoreChallenge) {
            issues.push(`${label}: blocked metadata does not match a Gcore payload`)
          }
        }
      }

      const manifestFiles = new Set(manifestPaths.map(repositoryRelative))
      for (const corpusFile of corpusFiles) {
        const relativePath = repositoryRelative(corpusFile)
        if (!tracked.has(relativePath)) {
          issues.push(`${relativePath}: corpus file not packaged`)
        }
        if (!manifestFiles.has(relativePath) && !declaredFiles.has(relativePath)) {
          issues.push(`${relativePath}: corpus file not declared by a manifest`)
        }
      }
    }

    for (const sourceRef of await reachableMatrixSourceRefs()) {
      const sourcePath = path.join(wikiRoot, `${sourceRef}.md`)
      const source = parseFrontmatter(await fs.readFile(sourcePath, "utf8"))
      if (source.data.status !== "processed") continue

      const sourceUrl = String(source.data.source_url ?? "")
      if (sourceUrl && blockedOrChallengeUrls.has(sourceUrl)) {
        issues.push(`${sourceRef}: active source_url points to a blocked capture`)
      }
    }

    expect(issues).toEqual([])
  })
})

function declaredSourceRefs(content: string) {
  const normalized = content.replace(/^\uFEFF/, "").replace(/\r\n/g, "\n")
  if (!normalized.startsWith("---\n")) return []

  const closingIndex = normalized.indexOf("\n---\n", 4)
  if (closingIndex === -1) return []

  const lines = normalized.slice(4, closingIndex).split("\n")
  const sourceRefsIndex = lines.findIndex((line) => line.startsWith("source_refs:"))
  if (sourceRefsIndex === -1) return []

  const inlineValue = lines[sourceRefsIndex].slice("source_refs:".length).trim()
  if (inlineValue.startsWith("[")) {
    return [...inlineValue.matchAll(/["'](sources\/[^"']+)["']/g)].map((match) =>
      normalizeSourceRef(match[1])
    )
  }

  const refs: string[] = []
  for (let index = sourceRefsIndex + 1; index < lines.length; index += 1) {
    const match = lines[index].match(/^\s+-\s+["']?([^"']+?)["']?\s*$/)
    if (!match) break
    refs.push(normalizeSourceRef(match[1]))
  }
  return refs
}

function sourceWikilinks(content: string) {
  return [...content.matchAll(/\[\[(sources\/[^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]/g)].map(
    (match) => normalizeSourceRef(match[1])
  )
}

function normalizeSourceRef(sourceRef: string) {
  return sourceRef.trim().replace(/^wiki\//, "").replace(/\.md$/i, "")
}

async function reachableMatrixSourceRefs() {
  const queuedRefs: string[] = []
  const visitedRefs = new Set<string>()

  for (const matrixPath of matrixPaths) {
    const content = await fs.readFile(path.join(wikiRoot, matrixPath), "utf8")
    queuedRefs.push(...declaredSourceRefs(content), ...sourceWikilinks(content))
  }

  while (queuedRefs.length > 0) {
    const sourceRef = normalizeSourceRef(queuedRefs.shift() ?? "")
    if (!sourceRef || visitedRefs.has(sourceRef)) continue
    visitedRefs.add(sourceRef)

    const content = await fs.readFile(path.join(wikiRoot, `${sourceRef}.md`), "utf8")
    queuedRefs.push(...declaredSourceRefs(content))
  }

  return visitedRefs
}

async function readRawManifestItems(manifestPath: string) {
  const parsed = JSON.parse(
    (await fs.readFile(manifestPath, "utf8")).replace(/^\uFEFF/, "")
  ) as Record<string, unknown>[] | { items: Record<string, unknown>[] }
  const items = Array.isArray(parsed) ? parsed : parsed.items

  return items.map((item) => {
    const normalized = Object.fromEntries(
      Object.entries(item).map(([key, value]) => [key.toLowerCase(), value])
    )
    return normalized as unknown as RawManifestItem
  })
}

async function listFiles(directory: string): Promise<string[]> {
  const entries = await fs.readdir(directory, { withFileTypes: true })
  const nested = await Promise.all(
    entries.map((entry) => {
      const entryPath = path.join(directory, entry.name)
      return entry.isDirectory() ? listFiles(entryPath) : [entryPath]
    })
  )
  return nested.flat()
}

function trackedFiles() {
  const output = execFileSync("git", ["ls-files", "-z", "--", "wiki/sources", "wiki/raw"], {
    cwd: repositoryRoot,
    encoding: "utf8"
  })
  return new Set(output.split("\0").filter(Boolean).map(normalizePath))
}

function repositoryRelative(absolutePath: string) {
  return normalizePath(path.relative(repositoryRoot, absolutePath))
}

function normalizePath(filePath: string) {
  return filePath.replace(/\\/g, "/")
}
