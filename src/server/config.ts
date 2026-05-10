import path from "node:path"

export const DEFAULT_DOMAIN = "concorsi pubblici italiani"
export const DEFAULT_BOOK_ID = "il-metodo-bando"

export function getProjectRoot() {
  return process.cwd()
}

export function getWikiRoot() {
  return path.resolve(getProjectRoot(), process.env.WIKI_ROOT || "wiki")
}

export function getArtifactsRoot() {
  return path.resolve(getProjectRoot(), "artifacts")
}

export function getObsidianConfig() {
  return {
    baseUrl: process.env.OBSIDIAN_BASE_URL || "https://127.0.0.1:27124",
    apiKey: process.env.OBSIDIAN_API_KEY || ""
  }
}

export function getOpenAiConfig() {
  return {
    apiKey: process.env.OPENAI_API_KEY || "",
    model: process.env.DEFAULT_LLM_MODEL || "gpt-4.1-mini"
  }
}

export type WriterProvider = "codex" | "openai" | "local"

export function getWriterConfig() {
  const requestedProvider = process.env.WRITER_PROVIDER || "codex"
  const provider: WriterProvider = ["codex", "openai", "local"].includes(requestedProvider)
    ? (requestedProvider as WriterProvider)
    : "codex"
  const timeoutMs = Number(process.env.CODEX_WRITER_TIMEOUT_MS || 240000)

  return {
    provider,
    codexCommand: process.env.CODEX_CLI_PATH || "codex",
    codexModel: process.env.CODEX_WRITER_MODEL || "",
    codexTimeoutMs: Number.isFinite(timeoutMs) ? timeoutMs : 240000
  }
}
