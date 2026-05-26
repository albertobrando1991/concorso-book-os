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

export function getHermesConfig() {
  const timeoutMs = Number(process.env.HERMES_TIMEOUT_MS || 240000)

  return {
    baseUrl: normalizeBaseUrl(process.env.HERMES_API_BASE || "http://127.0.0.1:8642/v1"),
    apiKey: process.env.HERMES_API_KEY || "",
    model: process.env.HERMES_MODEL || "hermes-agent",
    timeoutMs: Number.isFinite(timeoutMs) ? timeoutMs : 240000
  }
}

export function getGlmOcrConfig() {
  const timeoutMs = Number(process.env.GLM_OCR_TIMEOUT_MS || 600000)

  return {
    enabled: process.env.GLM_OCR_ENABLED === "true",
    command: process.env.GLM_OCR_COMMAND || "glmocr",
    configPath: process.env.GLM_OCR_CONFIG || "",
    layoutDevice: process.env.GLM_OCR_LAYOUT_DEVICE || "",
    timeoutMs: Number.isFinite(timeoutMs) ? timeoutMs : 600000
  }
}

export type WriterProvider = "codex" | "claude" | "openai" | "hermes" | "local"

export function getWriterConfig() {
  const requestedProvider = process.env.WRITER_PROVIDER || "codex"
  const provider: WriterProvider = ["codex", "claude", "openai", "hermes", "local"].includes(requestedProvider)
    ? (requestedProvider as WriterProvider)
    : "codex"
  const timeoutMs = Number(process.env.CODEX_WRITER_TIMEOUT_MS || 240000)
  const claudeTimeoutMs = Number(process.env.CLAUDE_WRITER_TIMEOUT_MS || timeoutMs || 240000)
  const openAiConfig = getOpenAiConfig()
  const hermesConfig = getHermesConfig()
  const codexModel = process.env.CODEX_WRITER_MODEL || "gpt-5.5"
  const codexReasoningEffort = process.env.CODEX_WRITER_REASONING_EFFORT || "xhigh"
  const claudeModel = process.env.CLAUDE_WRITER_MODEL || "claude-opus-4-7"
  const claudeReasoningEffort = process.env.CLAUDE_WRITER_REASONING_EFFORT || "xhigh"

  return {
    provider,
    codexCommand: process.env.CODEX_CLI_PATH || "codex",
    codexModel,
    codexReasoningEffort,
    codexTimeoutMs: Number.isFinite(timeoutMs) ? timeoutMs : 240000,
    claudeCommand: process.env.CLAUDE_CODE_PATH || process.env.CLAUDE_CLI_PATH || "claude",
    claudeModel,
    claudeReasoningEffort,
    claudeTimeoutMs: Number.isFinite(claudeTimeoutMs) ? claudeTimeoutMs : 240000,
    hermesModel: hermesConfig.model,
    writerModel:
      provider === "hermes"
        ? hermesConfig.model
        : provider === "openai"
          ? openAiConfig.model
          : provider === "codex"
            ? codexModel
            : provider === "claude"
              ? claudeModel
              : "local",
    writerReasoningEffort:
      provider === "codex" ? codexReasoningEffort : provider === "claude" ? claudeReasoningEffort : "n/a"
  }
}

function normalizeBaseUrl(value: string) {
  return value.replace(/\/+$/, "")
}
