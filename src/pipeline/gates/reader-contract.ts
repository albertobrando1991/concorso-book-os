const INTERNAL_KNOWLEDGE_PREFIXES = ["sources/", "topics/", "entities/", "quizzes/", "reviews/", "planning/", "raw/"]

export function isInternalKnowledgeLink(value: string) {
  const normalized = value.trim().replace(/\\/g, "/").replace(/^\/?wiki\//i, "").replace(/^\//, "").toLowerCase()

  return INTERNAL_KNOWLEDGE_PREFIXES.some((prefix) => normalized.startsWith(prefix))
}
