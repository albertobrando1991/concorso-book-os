const INTERNAL_KNOWLEDGE_SEGMENTS = new Set([
  "sources",
  "topics",
  "entities",
  "quizzes",
  "reviews",
  "planning",
  "raw",
  "templates",
  "dashboards",
  "memory",
  "logs"
])
const INTERNAL_LOG_FILES = new Set(["log", "log.md"])

export function isInternalKnowledgeLink(value: string) {
  const segments = canonicalSegments(value)

  if (segments[0] === "wiki") segments.shift()

  if (segments[0] === "books") {
    const bookSegments = segments.slice(1)
    const chaptersIndex = bookSegments.indexOf("chapters")
    const internalIndex = bookSegments.findIndex(isInternalSegment)

    return internalIndex >= 0 && (chaptersIndex < 0 || internalIndex < chaptersIndex)
  }

  return segments.length > 0 && isInternalSegment(segments[0])
}

function canonicalSegments(value: string) {
  const segments: string[] = []
  const path = value.trim().replace(/\\/g, "/").split("#", 1)[0]

  for (const rawSegment of path.split("/")) {
    const segment = rawSegment.trim().toLowerCase()

    if (!segment || segment === ".") continue

    if (segment === "..") {
      segments.pop()
      continue
    }

    segments.push(segment)
  }

  return segments
}

function isInternalSegment(segment: string) {
  return INTERNAL_KNOWLEDGE_SEGMENTS.has(segment) || INTERNAL_LOG_FILES.has(segment)
}
