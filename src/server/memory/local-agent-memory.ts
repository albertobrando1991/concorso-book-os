import fs from "node:fs/promises"
import path from "node:path"
import { getAgentMemoryConfig } from "../config"
import type { LlmMessage } from "../llm/openai-adapter"

export type MemoryKind = "preference" | "instruction" | "workflow" | "project_fact" | "result" | "warning"

export interface MemoryRecord {
  id: string
  createdAt: string
  scope: string
  kind: MemoryKind
  text: string
  keywords: string[]
  sourceConversationId: string
  sourceRef: string
  weight: number
}

export interface MemoryRecall {
  context: string
  memories: MemoryRecord[]
  totalChars: number
}

export interface MemoryStats {
  enabled: boolean
  root: string
  conversations: number
  atoms: number
  lastUpdatedAt: string
  personaPath: string
}

interface AgentMemoryConfig {
  enabled: boolean
  root: string
  recallMaxResults: number
  recallMaxTotalChars: number
  maxCharsPerMessage: number
  maxMessagesPerConversation: number
  maxAtomsPerConversation: number
}

interface ConversationRecord {
  id: string
  createdAt: string
  scope: string
  route: string
  messages: LlmMessage[]
  reply: string
  metadata: Record<string, string | number | boolean>
}

interface ScoredMemory {
  memory: MemoryRecord
  score: number
}

const DEFAULT_SCOPE = "global"
const ATOMS_PATH = path.join("l1", "atoms.jsonl")
const CONVERSATIONS_INDEX_PATH = path.join("l0", "conversations.jsonl")
const SCENARIOS_PATH = path.join("l2", "scenarios.md")
const PERSONA_PATH = path.join("l3", "persona.md")

const STOPWORDS = new Set([
  "allora",
  "anche",
  "avere",
  "come",
  "con",
  "cosa",
  "deve",
  "devi",
  "dopo",
  "dove",
  "essere",
  "fare",
  "gli",
  "hai",
  "il",
  "in",
  "io",
  "la",
  "le",
  "lo",
  "ma",
  "mi",
  "nel",
  "non",
  "per",
  "piu",
  "poi",
  "qui",
  "sei",
  "si",
  "su",
  "sul",
  "tra",
  "una",
  "uno",
  "usa",
  "uso"
])

export class LocalAgentMemory {
  private readonly config: AgentMemoryConfig

  constructor(config: Partial<AgentMemoryConfig> = {}) {
    this.config = {
      ...getAgentMemoryConfig(),
      ...config
    }
  }

  static fromConfig() {
    return new LocalAgentMemory()
  }

  async recall(input: {
    query: string
    scope?: string
    maxResults?: number
    maxTotalChars?: number
  }): Promise<MemoryRecall> {
    if (!this.config.enabled) return emptyRecall()

    const queryTerms = tokenize(input.query)
    if (queryTerms.length === 0) return emptyRecall()

    const records = normalizeMemoryRecords(await this.readJsonl<MemoryRecord>(ATOMS_PATH))
    const scored = records
      .map((memory) => ({ memory, score: scoreMemory(memory, queryTerms, input.scope || DEFAULT_SCOPE) }))
      .filter((item) => item.score > 0)
      .sort((left, right) => right.score - left.score || right.memory.createdAt.localeCompare(left.memory.createdAt))

    const maxResults = input.maxResults || this.config.recallMaxResults
    const maxTotalChars = input.maxTotalChars || this.config.recallMaxTotalChars
    const selected = fitMemoryBudget(scored.slice(0, maxResults * 2), maxResults, maxTotalChars)

    return {
      memories: selected,
      totalChars: selected.reduce((count, memory) => count + memory.text.length, 0),
      context: renderMemoryContext(selected)
    }
  }

  async recallForMessages(messages: LlmMessage[], scope?: string) {
    return this.recall({
      scope,
      query: messages
        .slice(-8)
        .map((message) => `${message.role}: ${message.content}`)
        .join("\n")
    })
  }

  async captureConversation(input: {
    scope?: string
    route: string
    messages: LlmMessage[]
    reply?: string
    metadata?: Record<string, string | number | boolean | undefined>
  }) {
    if (!this.config.enabled) return { conversationId: "", atoms: [] as MemoryRecord[] }

    await this.ensureDirectories()

    const now = new Date().toISOString()
    const conversation: ConversationRecord = {
      id: `conv-${toDateSlug(now)}-${shortHash(
        `${input.route}\n${input.messages.map((message) => message.content).join("\n")}\n${input.reply || ""}`
      )}`,
      createdAt: now,
      scope: input.scope || DEFAULT_SCOPE,
      route: input.route,
      messages: input.messages.slice(-this.config.maxMessagesPerConversation).map((message) => ({
        role: message.role,
        content: trimChars(message.content, this.config.maxCharsPerMessage)
      })),
      reply: trimChars(input.reply || "", this.config.maxCharsPerMessage),
      metadata: cleanMetadata(input.metadata || {})
    }

    const l0Path = path.join("l0", `${conversation.id}.md`)
    await this.writeText(l0Path, renderConversationMarkdown(conversation))
    await this.appendJsonl(CONVERSATIONS_INDEX_PATH, {
      id: conversation.id,
      createdAt: conversation.createdAt,
      scope: conversation.scope,
      route: conversation.route,
      l0Path,
      messageCount: conversation.messages.length,
      replyChars: conversation.reply.length
    })

    const atoms = await this.extractAtoms(conversation, l0Path)

    if (atoms.length > 0) {
      for (const atom of atoms) {
        await this.appendJsonl(ATOMS_PATH, atom)
      }

      await this.appendScenario(conversation, atoms)
      await this.refreshPersona()
    }

    return { conversationId: conversation.id, atoms }
  }

  async stats(): Promise<MemoryStats> {
    if (!this.config.enabled) {
      return {
        enabled: false,
        root: this.config.root,
        conversations: 0,
        atoms: 0,
        lastUpdatedAt: "",
        personaPath: PERSONA_PATH
      }
    }

    const [conversations, atoms] = await Promise.all([
      this.readJsonl<{ createdAt?: string }>(CONVERSATIONS_INDEX_PATH),
      this.readJsonl<MemoryRecord>(ATOMS_PATH)
    ])
    const lastUpdatedAt = [...conversations.map((item) => item.createdAt || ""), ...atoms.map((item) => item.createdAt)]
      .filter(Boolean)
      .sort()
      .at(-1) || ""

    return {
      enabled: true,
      root: this.config.root,
      conversations: conversations.length,
      atoms: atoms.length,
      lastUpdatedAt,
      personaPath: PERSONA_PATH
    }
  }

  private async extractAtoms(conversation: ConversationRecord, l0Path: string): Promise<MemoryRecord[]> {
    const existing = new Set(
      normalizeMemoryRecords(await this.readJsonl<MemoryRecord>(ATOMS_PATH))
        .map((memory) => normalizeMemoryText(memory.text))
    )
    const candidates: Array<{ kind: MemoryKind; text: string; weight: number }> = []

    for (const message of conversation.messages) {
      if (message.role !== "user") continue

      candidates.push(...extractUserAtoms(message.content))
    }

    if (conversation.reply) {
      const result = summarizeResult(conversation)

      if (result) {
        candidates.push({
          kind: "result",
          text: result,
          weight: 0.7
        })
      }
    }

    return candidates
      .map((candidate, index) => ({
        id: `mem-${toDateSlug(conversation.createdAt)}-${shortHash(`${conversation.id}-${index}-${candidate.text}`)}`,
        createdAt: conversation.createdAt,
        scope: conversation.scope,
        kind: candidate.kind,
        text: trimChars(candidate.text, 800),
        keywords: tokenize(candidate.text).slice(0, 18),
        sourceConversationId: conversation.id,
        sourceRef: l0Path,
        weight: candidate.weight
      }))
      .filter((memory) => memory.keywords.length >= 2)
      .filter((memory) => {
        const normalized = normalizeMemoryText(memory.text)
        if (existing.has(normalized)) return false
        existing.add(normalized)
        return true
      })
      .slice(0, this.config.maxAtomsPerConversation)
  }

  private async appendScenario(conversation: ConversationRecord, atoms: MemoryRecord[]) {
    const block = [
      "",
      `## ${conversation.createdAt} - ${conversation.scope}`,
      "",
      `- conversation_id: ${conversation.id}`,
      `- route: ${conversation.route}`,
      `- l0: ${path.join("l0", `${conversation.id}.md`).replace(/\\/g, "/")}`,
      "- atoms:",
      ...atoms.map((atom) => `  - ${atom.id} | ${atom.kind} | ${atom.text}`)
    ].join("\n")

    await this.appendText(SCENARIOS_PATH, `${block}\n`)
  }

  private async refreshPersona() {
    const atoms = normalizeMemoryRecords(await this.readJsonl<MemoryRecord>(ATOMS_PATH))
    const stable = atoms
      .filter((atom) => atom.kind === "preference" || atom.kind === "instruction" || atom.kind === "workflow")
      .slice(-80)
      .reverse()

    const content = [
      "# Local Agent Persona",
      "",
      "Memoria operativa generata automaticamente da ConcorsoBook OS.",
      "Usala come profilo di lavoro: le source notes e il wiki restano la base canonica per i contenuti normativi.",
      "",
      "## Preferenze e istruzioni recenti",
      "",
      stable.length === 0 ? "- Nessuna preferenza stabile ancora rilevata." : stable.map((atom) => `- ${atom.text} (${atom.id})`).join("\n"),
      ""
    ].join("\n")

    await this.writeText(PERSONA_PATH, content)
  }

  private async ensureDirectories() {
    await Promise.all([
      fs.mkdir(path.join(this.config.root, "l0"), { recursive: true }),
      fs.mkdir(path.join(this.config.root, "l1"), { recursive: true }),
      fs.mkdir(path.join(this.config.root, "l2"), { recursive: true }),
      fs.mkdir(path.join(this.config.root, "l3"), { recursive: true })
    ])
  }

  private async readJsonl<T>(relativePath: string): Promise<T[]> {
    try {
      const content = await fs.readFile(path.join(this.config.root, relativePath), "utf8")

      return content
        .split("\n")
        .map((line) => line.trim())
        .filter(Boolean)
        .map((line) => JSON.parse(line) as T)
    } catch {
      return []
    }
  }

  private async appendJsonl(relativePath: string, value: unknown) {
    await this.ensureDirectories()
    const absolutePath = path.join(this.config.root, relativePath)
    await fs.mkdir(path.dirname(absolutePath), { recursive: true })
    await fs.appendFile(absolutePath, `${JSON.stringify(value)}\n`, "utf8")
  }

  private async writeText(relativePath: string, content: string) {
    const absolutePath = path.join(this.config.root, relativePath)
    await fs.mkdir(path.dirname(absolutePath), { recursive: true })
    await fs.writeFile(absolutePath, content, "utf8")
  }

  private async appendText(relativePath: string, content: string) {
    const absolutePath = path.join(this.config.root, relativePath)
    await fs.mkdir(path.dirname(absolutePath), { recursive: true })
    await fs.appendFile(absolutePath, content, "utf8")
  }
}

export function withLocalMemoryContext(messages: LlmMessage[], recall: MemoryRecall) {
  if (!recall.context) return messages

  return [
    {
      role: "system" as const,
      content: recall.context
    },
    ...messages
  ]
}

function emptyRecall(): MemoryRecall {
  return { context: "", memories: [], totalChars: 0 }
}

function normalizeMemoryRecords(records: MemoryRecord[]): MemoryRecord[] {
  return records.flatMap((memory) => {
    if (!memory || typeof memory.text !== "string" || memory.text.trim().length === 0) return []

    return [{
      ...memory,
      keywords: Array.isArray(memory.keywords) ? memory.keywords : []
    }]
  })
}

function scoreMemory(memory: MemoryRecord, queryTerms: string[], scope: string) {
  const memoryTerms = new Set(memory.keywords.length > 0 ? memory.keywords : tokenize(memory.text))
  const overlap = queryTerms.filter((term) => memoryTerms.has(term)).length

  if (overlap === 0) return 0

  const overlapScore = overlap / Math.max(queryTerms.length, 1)
  const scopeBoost = memory.scope === scope ? 0.2 : memory.scope === DEFAULT_SCOPE ? 0.08 : 0
  const kindBoost = memory.kind === "preference" || memory.kind === "instruction" ? 0.12 : 0

  return (overlapScore + scopeBoost + kindBoost) * memory.weight
}

function fitMemoryBudget(scored: ScoredMemory[], maxResults: number, maxTotalChars: number) {
  const selected: MemoryRecord[] = []
  let usedChars = 0

  for (const item of scored) {
    const nextChars = usedChars + item.memory.text.length

    if (selected.length >= maxResults) break
    if (selected.length > 0 && nextChars > maxTotalChars) continue

    selected.push(item.memory)
    usedChars = nextChars
  }

  return selected
}

function renderMemoryContext(memories: MemoryRecord[]) {
  if (memories.length === 0) return ""

  return [
    "Memoria locale ConcorsoBook OS richiamata automaticamente.",
    "Usa queste note solo se pertinenti. Per norme, date e claim editoriali resta vincolante il wiki consolidato.",
    "",
    ...memories.map((memory) => `- [${memory.id}] ${memory.kind}: ${memory.text} (trace: ${memory.sourceRef})`)
  ].join("\n")
}

function extractUserAtoms(content: string) {
  const units = content
    .replace(/\r\n/g, "\n")
    .split(/\n+|(?<=[.!?])\s+/)
    .map((line) => line.trim())
    .filter((line) => line.length >= 18)

  const atoms: Array<{ kind: MemoryKind; text: string; weight: number }> = []

  for (const unit of units) {
    const normalized = normalizeForSearch(unit)

    if (/(ricorda|preferisco|voglio che|non voglio|mi serve|per me|d'ora in poi|da ora in poi)/.test(normalized)) {
      atoms.push({ kind: "preference", text: unit, weight: 1 })
      continue
    }

    if (/(devi|non devi|sempre|mai|evita|usa|mantieni|formato|stile|quando|prima di|obbligatorio)/.test(normalized)) {
      atoms.push({ kind: "instruction", text: unit, weight: 0.95 })
      continue
    }

    if (/(workflow|procedura|pipeline|telegram|hermes|manual writer|codex|claude|kimi|openai|dashboard|api|endpoint)/.test(normalized)) {
      atoms.push({ kind: "workflow", text: unit, weight: 0.85 })
      continue
    }

    if (/(capitolo|fonte|wiki|source|topic|entity|metodo bando|concorso|manuale|libro)/.test(normalized)) {
      atoms.push({ kind: "project_fact", text: unit, weight: 0.75 })
    }
  }

  return atoms
}

function summarizeResult(conversation: ConversationRecord) {
  const userText = conversation.messages
    .filter((message) => message.role === "user")
    .map((message) => message.content)
    .join(" ")
  const userSummary = firstSentence(userText)
  const replySummary = firstSentence(conversation.reply)

  if (!userSummary && !replySummary) return ""

  return `Esito ${conversation.route}: ${trimChars([userSummary, replySummary].filter(Boolean).join(" -> "), 420)}`
}

function renderConversationMarkdown(conversation: ConversationRecord) {
  return [
    "---",
    `id: ${conversation.id}`,
    "type: agent_memory_conversation",
    `created_at: ${conversation.createdAt}`,
    `scope: ${conversation.scope}`,
    `route: ${conversation.route}`,
    "---",
    "",
    `# ${conversation.id}`,
    "",
    "## Metadata",
    "",
    Object.entries(conversation.metadata).map(([key, value]) => `- ${key}: ${value}`).join("\n") || "- none",
    "",
    "## Messages",
    "",
    ...conversation.messages.map((message, index) => [
      `### ${index + 1}. ${message.role}`,
      "",
      message.content
    ].join("\n")),
    "",
    "## Reply",
    "",
    conversation.reply || "(empty)",
    ""
  ].join("\n")
}

function tokenize(value: string) {
  return Array.from(new Set(
    normalizeForSearch(value)
      .split(/[^a-z0-9]+/)
      .map((word) => word.trim())
      .filter((word) => word.length >= 3 && !STOPWORDS.has(word))
  ))
}

function normalizeForSearch(value: string) {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
}

function normalizeMemoryText(value: string) {
  return normalizeForSearch(value).replace(/[^a-z0-9]+/g, " ").trim()
}

function cleanMetadata(value: Record<string, string | number | boolean | undefined>) {
  return Object.fromEntries(
    Object.entries(value).filter(([, item]) => item !== undefined)
  ) as Record<string, string | number | boolean>
}

function firstSentence(value: string) {
  return trimChars(value.replace(/\s+/g, " ").trim().split(/(?<=[.!?])\s+/)[0] || "", 220)
}

function trimChars(value: string, limit: number) {
  const compact = value.replace(/\s+\n/g, "\n").trim()

  return compact.length > limit ? `${compact.slice(0, limit - 3)}...` : compact
}

function toDateSlug(value: string) {
  return value.replace(/[-:.TZ]/g, "").slice(0, 14)
}

function shortHash(value: string) {
  let hash = 2166136261

  for (let index = 0; index < value.length; index += 1) {
    hash ^= value.charCodeAt(index)
    hash = Math.imul(hash, 16777619)
  }

  return (hash >>> 0).toString(36)
}
