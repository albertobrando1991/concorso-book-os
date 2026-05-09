import OpenAI from "openai"
import { getOpenAiConfig } from "../config"

export interface LlmMessage {
  role: "system" | "user" | "assistant"
  content: string
}

export interface LlmClient {
  complete(messages: LlmMessage[]): Promise<string>
}

export class OpenAiLlmClient implements LlmClient {
  private readonly client: OpenAI | null
  private readonly model: string

  constructor() {
    const config = getOpenAiConfig()
    this.model = config.model
    this.client = config.apiKey ? new OpenAI({ apiKey: config.apiKey }) : null
  }

  async complete(messages: LlmMessage[]) {
    if (!this.client) {
      return deterministicCompletion(messages)
    }

    const response = await this.client.chat.completions.create({
      model: this.model,
      messages
    })

    return response.choices[0]?.message.content || ""
  }
}

export function deterministicCompletion(messages: LlmMessage[]) {
  const lastMessage = messages[messages.length - 1]?.content || ""
  const compact = lastMessage.replace(/\s+/g, " ").trim()

  return compact.length > 500 ? `${compact.slice(0, 497)}...` : compact
}

