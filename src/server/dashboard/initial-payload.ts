import type { BookStudioData } from "../book/book-preview"
import type { KnowledgeGraph } from "../wiki/graph"

const DEFAULT_GRAPH_NODE_LIMIT = 160
const DEFAULT_GRAPH_LINK_LIMIT = 360

export function trimBookStudioInitialData(data: BookStudioData, _requestedChapterPath?: string): BookStudioData {
  return {
    ...data,
    chapters: data.chapters.map((chapter) => ({
      ...chapter,
      blocks: []
    }))
  }
}

export function shouldLoadSourceReader(sourcePath?: string) {
  return Boolean(sourcePath?.trim())
}

export function trimKnowledgeGraphInitialData(
  graph: KnowledgeGraph,
  limits: { nodeLimit?: number; linkLimit?: number } = {}
): KnowledgeGraph {
  const nodeLimit = Math.max(1, limits.nodeLimit ?? DEFAULT_GRAPH_NODE_LIMIT)
  const linkLimit = Math.max(0, limits.linkLimit ?? DEFAULT_GRAPH_LINK_LIMIT)
  const nodes = graph.nodes.slice(0, nodeLimit)
  const nodeIds = new Set(nodes.map((node) => node.id))
  const links = graph.links
    .filter((link) => nodeIds.has(link.source) && nodeIds.has(link.target))
    .slice(0, linkLimit)

  return {
    nodes,
    links
  }
}
