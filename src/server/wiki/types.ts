export type NoteStatus =
  | "raw"
  | "new"
  | "processed"
  | "draft"
  | "consolidated"
  | "review_required"
  | "to_expand"
  | "archived"

export type NoteType =
  | "source"
  | "topic"
  | "entity"
  | "book"
  | "chapter"
  | "quiz"
  | "review"
  | "dashboard"
  | "template"
  | "log"

export interface BaseFrontmatter {
  id: string
  type: NoteType | string
  title: string
  status: NoteStatus | string
  domain: string
  topics: string[]
  entities: string[]
  source_refs: string[]
  book_refs: string[]
  confidence: number
  updated_at: string
  created_at: string
  review_required: boolean
  canonical: boolean
  tags: string[]
  [key: string]: unknown
}

export interface SourceInput {
  title: string
  content: string
  sourceType: "law" | "decree" | "manual" | "article" | "website" | "transcript"
  sourceUrl?: string
  sourceDate?: string
  authorityLevel?: "alta" | "media" | "bassa"
  domain?: string
}

export interface ClassifiedSource {
  id: string
  title: string
  slug: string
  topics: string[]
  entities: string[]
  summary: string
  authorityLevel: "alta" | "media" | "bassa"
  sourceType: SourceInput["sourceType"]
}

export interface AgentArtifact {
  title: string
  path: string
  kind: "task-list" | "plan" | "wireframe" | "report" | "summary" | "screenshot"
}

export interface AgentRunResult {
  runId: string
  status: "completed" | "failed"
  changedFiles: string[]
  impactedBooks: string[]
  artifacts: AgentArtifact[]
  messages: string[]
}

export interface DashboardSource {
  title: string
  path: string
  status: string
  sourceType: string
  authorityLevel: string
  topics: string[]
  updatedAt: string
}

export interface DashboardTopic {
  title: string
  path: string
  status: string
  sourceRefs: string[]
  chapterRefs: string[]
  confidence: number
  updatedAt: string
}

export interface DashboardBook {
  title: string
  path: string
  status: string
  chapters: number
  reviewRequired: boolean
  updatedAt: string
}

export interface QualityIssue {
  id: string
  title: string
  severity: "low" | "medium" | "high"
  issueType: string
  affectedPages: string[]
  recommendation: string
}

export interface DashboardData {
  metrics: {
    totalSources: number
    unprocessedSources: number
    recentTopics: number
    draftChapters: number
    consolidatedChapters: number
    openConflicts: number
    memoryConversations: number
    memoryAtoms: number
  }
  sources: DashboardSource[]
  topics: DashboardTopic[]
  books: DashboardBook[]
  qualityIssues: QualityIssue[]
  logEntries: string[]
  agentRuns: string[]
  artifacts: AgentArtifact[]
}
