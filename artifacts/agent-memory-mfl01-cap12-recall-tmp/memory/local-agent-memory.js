"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.LocalAgentMemory = void 0;
exports.withLocalMemoryContext = withLocalMemoryContext;
const promises_1 = __importDefault(require("node:fs/promises"));
const node_path_1 = __importDefault(require("node:path"));
const config_1 = require("../config");
const DEFAULT_SCOPE = "global";
const ATOMS_PATH = node_path_1.default.join("l1", "atoms.jsonl");
const CONVERSATIONS_INDEX_PATH = node_path_1.default.join("l0", "conversations.jsonl");
const SCENARIOS_PATH = node_path_1.default.join("l2", "scenarios.md");
const PERSONA_PATH = node_path_1.default.join("l3", "persona.md");
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
]);
class LocalAgentMemory {
    constructor(config = {}) {
        this.config = {
            ...(0, config_1.getAgentMemoryConfig)(),
            ...config
        };
    }
    static fromConfig() {
        return new LocalAgentMemory();
    }
    async recall(input) {
        if (!this.config.enabled)
            return emptyRecall();
        const queryTerms = tokenize(input.query);
        if (queryTerms.length === 0)
            return emptyRecall();
        const records = await this.readJsonl(ATOMS_PATH);
        const scored = records
            .map((memory) => ({ memory, score: scoreMemory(memory, queryTerms, input.scope || DEFAULT_SCOPE) }))
            .filter((item) => item.score > 0)
            .sort((left, right) => right.score - left.score || right.memory.createdAt.localeCompare(left.memory.createdAt));
        const maxResults = input.maxResults || this.config.recallMaxResults;
        const maxTotalChars = input.maxTotalChars || this.config.recallMaxTotalChars;
        const selected = fitMemoryBudget(scored.slice(0, maxResults * 2), maxResults, maxTotalChars);
        return {
            memories: selected,
            totalChars: selected.reduce((count, memory) => count + memory.text.length, 0),
            context: renderMemoryContext(selected)
        };
    }
    async recallForMessages(messages, scope) {
        return this.recall({
            scope,
            query: messages
                .slice(-8)
                .map((message) => `${message.role}: ${message.content}`)
                .join("\n")
        });
    }
    async captureConversation(input) {
        if (!this.config.enabled)
            return { conversationId: "", atoms: [] };
        await this.ensureDirectories();
        const now = new Date().toISOString();
        const conversation = {
            id: `conv-${toDateSlug(now)}-${shortHash(`${input.route}\n${input.messages.map((message) => message.content).join("\n")}\n${input.reply || ""}`)}`,
            createdAt: now,
            scope: input.scope || DEFAULT_SCOPE,
            route: input.route,
            messages: input.messages.slice(-this.config.maxMessagesPerConversation).map((message) => ({
                role: message.role,
                content: trimChars(message.content, this.config.maxCharsPerMessage)
            })),
            reply: trimChars(input.reply || "", this.config.maxCharsPerMessage),
            metadata: cleanMetadata(input.metadata || {})
        };
        const l0Path = node_path_1.default.join("l0", `${conversation.id}.md`);
        await this.writeText(l0Path, renderConversationMarkdown(conversation));
        await this.appendJsonl(CONVERSATIONS_INDEX_PATH, {
            id: conversation.id,
            createdAt: conversation.createdAt,
            scope: conversation.scope,
            route: conversation.route,
            l0Path,
            messageCount: conversation.messages.length,
            replyChars: conversation.reply.length
        });
        const atoms = await this.extractAtoms(conversation, l0Path);
        if (atoms.length > 0) {
            for (const atom of atoms) {
                await this.appendJsonl(ATOMS_PATH, atom);
            }
            await this.appendScenario(conversation, atoms);
            await this.refreshPersona();
        }
        return { conversationId: conversation.id, atoms };
    }
    async stats() {
        if (!this.config.enabled) {
            return {
                enabled: false,
                root: this.config.root,
                conversations: 0,
                atoms: 0,
                lastUpdatedAt: "",
                personaPath: PERSONA_PATH
            };
        }
        const [conversations, atoms] = await Promise.all([
            this.readJsonl(CONVERSATIONS_INDEX_PATH),
            this.readJsonl(ATOMS_PATH)
        ]);
        const lastUpdatedAt = [...conversations.map((item) => item.createdAt || ""), ...atoms.map((item) => item.createdAt)]
            .filter(Boolean)
            .sort()
            .at(-1) || "";
        return {
            enabled: true,
            root: this.config.root,
            conversations: conversations.length,
            atoms: atoms.length,
            lastUpdatedAt,
            personaPath: PERSONA_PATH
        };
    }
    async extractAtoms(conversation, l0Path) {
        const existing = new Set((await this.readJsonl(ATOMS_PATH)).map((memory) => normalizeMemoryText(memory.text)));
        const candidates = [];
        for (const message of conversation.messages) {
            if (message.role !== "user")
                continue;
            candidates.push(...extractUserAtoms(message.content));
        }
        if (conversation.reply) {
            const result = summarizeResult(conversation);
            if (result) {
                candidates.push({
                    kind: "result",
                    text: result,
                    weight: 0.7
                });
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
            const normalized = normalizeMemoryText(memory.text);
            if (existing.has(normalized))
                return false;
            existing.add(normalized);
            return true;
        })
            .slice(0, this.config.maxAtomsPerConversation);
    }
    async appendScenario(conversation, atoms) {
        const block = [
            "",
            `## ${conversation.createdAt} - ${conversation.scope}`,
            "",
            `- conversation_id: ${conversation.id}`,
            `- route: ${conversation.route}`,
            `- l0: ${node_path_1.default.join("l0", `${conversation.id}.md`).replace(/\\/g, "/")}`,
            "- atoms:",
            ...atoms.map((atom) => `  - ${atom.id} | ${atom.kind} | ${atom.text}`)
        ].join("\n");
        await this.appendText(SCENARIOS_PATH, `${block}\n`);
    }
    async refreshPersona() {
        const atoms = await this.readJsonl(ATOMS_PATH);
        const stable = atoms
            .filter((atom) => atom.kind === "preference" || atom.kind === "instruction" || atom.kind === "workflow")
            .slice(-80)
            .reverse();
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
        ].join("\n");
        await this.writeText(PERSONA_PATH, content);
    }
    async ensureDirectories() {
        await Promise.all([
            promises_1.default.mkdir(node_path_1.default.join(this.config.root, "l0"), { recursive: true }),
            promises_1.default.mkdir(node_path_1.default.join(this.config.root, "l1"), { recursive: true }),
            promises_1.default.mkdir(node_path_1.default.join(this.config.root, "l2"), { recursive: true }),
            promises_1.default.mkdir(node_path_1.default.join(this.config.root, "l3"), { recursive: true })
        ]);
    }
    async readJsonl(relativePath) {
        try {
            const content = await promises_1.default.readFile(node_path_1.default.join(this.config.root, relativePath), "utf8");
            return content
                .split("\n")
                .map((line) => line.trim())
                .filter(Boolean)
                .map((line) => JSON.parse(line));
        }
        catch {
            return [];
        }
    }
    async appendJsonl(relativePath, value) {
        await this.ensureDirectories();
        const absolutePath = node_path_1.default.join(this.config.root, relativePath);
        await promises_1.default.mkdir(node_path_1.default.dirname(absolutePath), { recursive: true });
        await promises_1.default.appendFile(absolutePath, `${JSON.stringify(value)}\n`, "utf8");
    }
    async writeText(relativePath, content) {
        const absolutePath = node_path_1.default.join(this.config.root, relativePath);
        await promises_1.default.mkdir(node_path_1.default.dirname(absolutePath), { recursive: true });
        await promises_1.default.writeFile(absolutePath, content, "utf8");
    }
    async appendText(relativePath, content) {
        const absolutePath = node_path_1.default.join(this.config.root, relativePath);
        await promises_1.default.mkdir(node_path_1.default.dirname(absolutePath), { recursive: true });
        await promises_1.default.appendFile(absolutePath, content, "utf8");
    }
}
exports.LocalAgentMemory = LocalAgentMemory;
function withLocalMemoryContext(messages, recall) {
    if (!recall.context)
        return messages;
    return [
        {
            role: "system",
            content: recall.context
        },
        ...messages
    ];
}
function emptyRecall() {
    return { context: "", memories: [], totalChars: 0 };
}
function scoreMemory(memory, queryTerms, scope) {
    const memoryTerms = new Set(memory.keywords.length > 0 ? memory.keywords : tokenize(memory.text));
    const overlap = queryTerms.filter((term) => memoryTerms.has(term)).length;
    if (overlap === 0)
        return 0;
    const overlapScore = overlap / Math.max(queryTerms.length, 1);
    const scopeBoost = memory.scope === scope ? 0.2 : memory.scope === DEFAULT_SCOPE ? 0.08 : 0;
    const kindBoost = memory.kind === "preference" || memory.kind === "instruction" ? 0.12 : 0;
    return (overlapScore + scopeBoost + kindBoost) * memory.weight;
}
function fitMemoryBudget(scored, maxResults, maxTotalChars) {
    const selected = [];
    let usedChars = 0;
    for (const item of scored) {
        const nextChars = usedChars + item.memory.text.length;
        if (selected.length >= maxResults)
            break;
        if (selected.length > 0 && nextChars > maxTotalChars)
            continue;
        selected.push(item.memory);
        usedChars = nextChars;
    }
    return selected;
}
function renderMemoryContext(memories) {
    if (memories.length === 0)
        return "";
    return [
        "Memoria locale ConcorsoBook OS richiamata automaticamente.",
        "Usa queste note solo se pertinenti. Per norme, date e claim editoriali resta vincolante il wiki consolidato.",
        "",
        ...memories.map((memory) => `- [${memory.id}] ${memory.kind}: ${memory.text} (trace: ${memory.sourceRef})`)
    ].join("\n");
}
function extractUserAtoms(content) {
    const units = content
        .replace(/\r\n/g, "\n")
        .split(/\n+|(?<=[.!?])\s+/)
        .map((line) => line.trim())
        .filter((line) => line.length >= 18);
    const atoms = [];
    for (const unit of units) {
        const normalized = normalizeForSearch(unit);
        if (/(ricorda|preferisco|voglio che|non voglio|mi serve|per me|d'ora in poi|da ora in poi)/.test(normalized)) {
            atoms.push({ kind: "preference", text: unit, weight: 1 });
            continue;
        }
        if (/(devi|non devi|sempre|mai|evita|usa|mantieni|formato|stile|quando|prima di|obbligatorio)/.test(normalized)) {
            atoms.push({ kind: "instruction", text: unit, weight: 0.95 });
            continue;
        }
        if (/(workflow|procedura|pipeline|telegram|hermes|manual writer|codex|claude|kimi|openai|dashboard|api|endpoint)/.test(normalized)) {
            atoms.push({ kind: "workflow", text: unit, weight: 0.85 });
            continue;
        }
        if (/(capitolo|fonte|wiki|source|topic|entity|metodo bando|concorso|manuale|libro)/.test(normalized)) {
            atoms.push({ kind: "project_fact", text: unit, weight: 0.75 });
        }
    }
    return atoms;
}
function summarizeResult(conversation) {
    const userText = conversation.messages
        .filter((message) => message.role === "user")
        .map((message) => message.content)
        .join(" ");
    const userSummary = firstSentence(userText);
    const replySummary = firstSentence(conversation.reply);
    if (!userSummary && !replySummary)
        return "";
    return `Esito ${conversation.route}: ${trimChars([userSummary, replySummary].filter(Boolean).join(" -> "), 420)}`;
}
function renderConversationMarkdown(conversation) {
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
    ].join("\n");
}
function tokenize(value) {
    return Array.from(new Set(normalizeForSearch(value)
        .split(/[^a-z0-9]+/)
        .map((word) => word.trim())
        .filter((word) => word.length >= 3 && !STOPWORDS.has(word))));
}
function normalizeForSearch(value) {
    return value
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase();
}
function normalizeMemoryText(value) {
    return normalizeForSearch(value).replace(/[^a-z0-9]+/g, " ").trim();
}
function cleanMetadata(value) {
    return Object.fromEntries(Object.entries(value).filter(([, item]) => item !== undefined));
}
function firstSentence(value) {
    return trimChars(value.replace(/\s+/g, " ").trim().split(/(?<=[.!?])\s+/)[0] || "", 220);
}
function trimChars(value, limit) {
    const compact = value.replace(/\s+\n/g, "\n").trim();
    return compact.length > limit ? `${compact.slice(0, limit - 3)}...` : compact;
}
function toDateSlug(value) {
    return value.replace(/[-:.TZ]/g, "").slice(0, 14);
}
function shortHash(value) {
    let hash = 2166136261;
    for (let index = 0; index < value.length; index += 1) {
        hash ^= value.charCodeAt(index);
        hash = Math.imul(hash, 16777619);
    }
    return (hash >>> 0).toString(36);
}
