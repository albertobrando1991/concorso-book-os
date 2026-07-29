"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.OpenAiLlmClient = void 0;
exports.deterministicCompletion = deterministicCompletion;
const openai_1 = __importDefault(require("openai"));
const config_1 = require("../config");
class OpenAiLlmClient {
    constructor(options = {}) {
        const config = (0, config_1.getOpenAiConfig)();
        const apiKey = options.apiKey ?? config.apiKey;
        this.model = options.model || config.model;
        this.client = apiKey
            ? new openai_1.default({
                apiKey,
                baseURL: options.baseURL
            })
            : null;
    }
    async complete(messages) {
        if (!this.client) {
            return deterministicCompletion(messages);
        }
        const response = await this.client.chat.completions.create({
            model: this.model,
            messages
        });
        return response.choices[0]?.message.content || "";
    }
}
exports.OpenAiLlmClient = OpenAiLlmClient;
function deterministicCompletion(messages) {
    const lastMessage = messages[messages.length - 1]?.content || "";
    const compact = lastMessage.replace(/\s+/g, " ").trim();
    return compact.length > 500 ? `${compact.slice(0, 497)}...` : compact;
}
