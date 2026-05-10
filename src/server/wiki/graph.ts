import { parseFrontmatter } from "./frontmatter"
import { FileWikiStore } from "./file-store"
import { extractWikiLinks } from "./markdown"

export interface GraphNode {
  id: string
  label: string
  type: "source" | "topic" | "entity" | "book" | "chapter" | "review" | "wiki" | "other"
  path: string
}

export interface GraphLink {
  source: string
  target: string
  kind: "wikilink" | "frontmatter"
}

export interface KnowledgeGraph {
  nodes: GraphNode[]
  links: GraphLink[]
}

export async function buildKnowledgeGraph(store: FileWikiStore): Promise<KnowledgeGraph> {
  const files = (await store.listMarkdown(""))
    .filter((file) => !file.startsWith("raw/"))
    .filter((file) => !file.startsWith("templates/"))
  const nodes = new Map<string, GraphNode>()
  const links: GraphLink[] = []

  for (const file of files) {
    const content = await store.readText(file)
    const parsed = parseFrontmatter(content)
    const id = toNodeId(file)
    const type = inferNodeType(file, String(parsed.data.type || ""))

    nodes.set(id, {
      id,
      label: String(parsed.data.title || file.replace(".md", "")),
      type,
      path: file
    })
  }

  for (const file of files) {
    const content = await store.readText(file)
    const parsed = parseFrontmatter(content)
    const source = toNodeId(file)

    for (const rawTarget of extractWikiLinks(content)) {
      const target = resolveTargetId(rawTarget, nodes)
      if (target && target !== source) {
        links.push({ source, target, kind: "wikilink" })
      }
    }

    for (const target of frontmatterTargets(parsed.data)) {
      if (nodes.has(target) && target !== source) {
        links.push({ source, target, kind: "frontmatter" })
      }
    }
  }

  return {
    nodes: Array.from(nodes.values()).sort((left, right) => left.label.localeCompare(right.label)),
    links: dedupeLinks(links)
  }
}

function frontmatterTargets(data: Record<string, unknown>) {
  return [
    ...asStringArray(data.source_refs),
    ...asStringArray(data.book_refs),
    ...asStringArray(data.chapter_refs)
  ]
    .filter((value) => value.endsWith(".md"))
    .map(toNodeId)
}

function inferNodeType(path: string, frontmatterType: string): GraphNode["type"] {
  if (path.startsWith("sources/")) return "source"
  if (path.startsWith("topics/")) return "topic"
  if (path.startsWith("entities/")) return "entity"
  if (path.includes("/chapters/")) return "chapter"
  if (path.startsWith("books/")) return "book"
  if (path.startsWith("reviews/")) return "review"
  if (path === "index.md" || path === "AGENTS.md" || path === "log.md") return "wiki"

  if (["source", "topic", "entity", "book", "chapter", "review"].includes(frontmatterType)) {
    return frontmatterType as GraphNode["type"]
  }

  return "other"
}

function resolveTargetId(target: string, nodes: Map<string, GraphNode>) {
  const normalized = toNodeId(target.endsWith(".md") ? target : `${target}.md`)

  if (nodes.has(normalized)) return normalized

  if (normalized.includes("/")) return ""

  const matchingNode = Array.from(nodes.keys()).find((id) => id.endsWith(`/${normalized}`) || id === normalized)

  return matchingNode || ""
}

function toNodeId(path: string) {
  return path.replace(/\\/g, "/").replace(/\.md$/, "")
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map(String) : []
}

function dedupeLinks(links: GraphLink[]) {
  const seen = new Set<string>()
  return links.filter((link) => {
    const key = `${link.source}->${link.target}:${link.kind}`
    if (seen.has(key)) return false
    seen.add(key)
    return true
  })
}
