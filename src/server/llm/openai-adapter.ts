import OpenAI from "openai"
import { getOpenAiConfig } from "../config"

export interface LlmMessage {
  role: "system" | "user" | "assistant"
  content: string
}

export interface LlmClient {
  complete(messages: LlmMessage[]): Promise<string>
}

interface OpenAiClientOptions {
  apiKey?: string
  baseURL?: string
  model?: string
}

export class OpenAiLlmClient implements LlmClient {
  private readonly client: OpenAI | null
  private readonly model: string

  constructor(options: OpenAiClientOptions = {}) {
    const config = getOpenAiConfig()
    const apiKey = options.apiKey ?? config.apiKey

    this.model = options.model || config.model
    this.client = apiKey
      ? new OpenAI({
          apiKey,
          baseURL: options.baseURL
        })
      : null
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
