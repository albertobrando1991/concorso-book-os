"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.WRITER_PROVIDERS = exports.DEFAULT_BOOK_ID = exports.DEFAULT_DOMAIN = void 0;
exports.getProjectRoot = getProjectRoot;
exports.getWikiRoot = getWikiRoot;
exports.getArtifactsRoot = getArtifactsRoot;
exports.getAgentMemoryConfig = getAgentMemoryConfig;
exports.getObsidianConfig = getObsidianConfig;
exports.getOpenAiConfig = getOpenAiConfig;
exports.getKimiConfig = getKimiConfig;
exports.getHermesConfig = getHermesConfig;
exports.getGlmOcrConfig = getGlmOcrConfig;
exports.getWriterConfig = getWriterConfig;
const node_path_1 = __importDefault(require("node:path"));
exports.DEFAULT_DOMAIN = "concorsi pubblici italiani";
exports.DEFAULT_BOOK_ID = "il-metodo-bando";
function getProjectRoot() {
    return process.cwd();
}
function getWikiRoot() {
    return node_path_1.default.resolve(getProjectRoot(), process.env.WIKI_ROOT || "wiki");
}
function getArtifactsRoot() {
    return node_path_1.default.resolve(getProjectRoot(), "artifacts");
}
function getAgentMemoryConfig() {
    const root = process.env.AGENT_MEMORY_ROOT
        ? node_path_1.default.resolve(getProjectRoot(), process.env.AGENT_MEMORY_ROOT)
        : node_path_1.default.join(getWikiRoot(), "memory", "agent");
    return {
        enabled: process.env.AGENT_MEMORY_ENABLED !== "false",
        root,
        recallMaxResults: readPositiveInt("AGENT_MEMORY_RECALL_MAX_RESULTS", 5),
        recallMaxTotalChars: readPositiveInt("AGENT_MEMORY_RECALL_MAX_CHARS", 3500),
        maxCharsPerMessage: readPositiveInt("AGENT_MEMORY_MAX_CHARS_PER_MESSAGE", 6000),
        maxMessagesPerConversation: readPositiveInt("AGENT_MEMORY_MAX_MESSAGES_PER_CONVERSATION", 24),
        maxAtomsPerConversation: readPositiveInt("AGENT_MEMORY_MAX_ATOMS_PER_CONVERSATION", 8)
    };
}
function getObsidianConfig() {
    return {
        baseUrl: process.env.OBSIDIAN_BASE_URL || "https://127.0.0.1:27124",
        apiKey: process.env.OBSIDIAN_API_KEY || ""
    };
}
function getOpenAiConfig() {
    return {
        apiKey: process.env.OPENAI_API_KEY || "",
        model: process.env.DEFAULT_LLM_MODEL || "gpt-4.1-mini"
    };
}
function getKimiConfig() {
    return {
        apiKey: process.env.KIMI_API_KEY || "",
        baseUrl: normalizeBaseUrl(process.env.KIMI_API_BASE || "https://api.moonshot.ai/v1"),
        model: process.env.KIMI_MODEL || "kimi-k2.6"
    };
}
function getHermesConfig() {
    const timeoutMs = Number(process.env.HERMES_TIMEOUT_MS || 240000);
    return {
        baseUrl: normalizeBaseUrl(process.env.HERMES_API_BASE || "http://127.0.0.1:8642/v1"),
        apiKey: process.env.HERMES_API_KEY || "",
        model: process.env.HERMES_MODEL || "hermes-agent",
        timeoutMs: Number.isFinite(timeoutMs) ? timeoutMs : 240000
    };
}
function getGlmOcrConfig() {
    const timeoutMs = Number(process.env.GLM_OCR_TIMEOUT_MS || 600000);
    return {
        enabled: process.env.GLM_OCR_ENABLED === "true",
        command: process.env.GLM_OCR_COMMAND || "glmocr",
        configPath: process.env.GLM_OCR_CONFIG || "",
        layoutDevice: process.env.GLM_OCR_LAYOUT_DEVICE || "",
        timeoutMs: Number.isFinite(timeoutMs) ? timeoutMs : 600000
    };
}
exports.WRITER_PROVIDERS = ["codex", "claude", "kimi", "openai", "hermes", "local"];
function getWriterConfig() {
    const requestedProvider = process.env.WRITER_PROVIDER || "codex";
    const provider = exports.WRITER_PROVIDERS.includes(requestedProvider)
        ? requestedProvider
        : "codex";
    const timeoutMs = Number(process.env.CODEX_WRITER_TIMEOUT_MS || 240000);
    const claudeTimeoutMs = Number(process.env.CLAUDE_WRITER_TIMEOUT_MS || timeoutMs || 240000);
    const openAiConfig = getOpenAiConfig();
    const kimiConfig = getKimiConfig();
    const hermesConfig = getHermesConfig();
    const codexModel = process.env.CODEX_WRITER_MODEL || "gpt-5.5";
    const codexReasoningEffort = process.env.CODEX_WRITER_REASONING_EFFORT || "xhigh";
    const claudeModel = process.env.CLAUDE_WRITER_MODEL || "claude-opus-4-7";
    const claudeReasoningEffort = process.env.CLAUDE_WRITER_REASONING_EFFORT || "xhigh";
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
        kimiApiKey: kimiConfig.apiKey,
        kimiBaseUrl: kimiConfig.baseUrl,
        kimiModel: kimiConfig.model,
        hermesModel: hermesConfig.model,
        writerModel: provider === "hermes"
            ? hermesConfig.model
            : provider === "kimi"
                ? kimiConfig.model
                : provider === "openai"
                    ? openAiConfig.model
                    : provider === "codex"
                        ? codexModel
                        : provider === "claude"
                            ? claudeModel
                            : "local",
        writerReasoningEffort: provider === "codex" ? codexReasoningEffort : provider === "claude" ? claudeReasoningEffort : "n/a"
    };
}
function normalizeBaseUrl(value) {
    return value.replace(/\/+$/, "");
}
function readPositiveInt(name, fallback) {
    const parsed = Number(process.env[name] || fallback);
    return Number.isFinite(parsed) && parsed > 0 ? Math.floor(parsed) : fallback;
}
