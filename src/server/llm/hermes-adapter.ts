import { getHermesConfig } from "../config"
import { deterministicCompletion, type LlmClient, type LlmMessage } from "./openai-adapter"

interface HermesChatCompletionResponse {
  choices?: Array<{
    message?: {
      content?: string
    }
  }>
}

export class HermesLlmClient implements LlmClient {
  private readonly baseUrl: string
  private readonly apiKey: string
  private readonly model: string
  private readonly timeoutMs: number

  constructor() {
    const config = getHermesConfig()
    this.baseUrl = config.baseUrl
    this.apiKey = config.apiKey
    this.model = config.model
    this.timeoutMs = config.timeoutMs
  }

  isConfigured() {
    return Boolean(this.baseUrl && this.apiKey)
  }

  async health() {
    if (!this.isConfigured()) {
      return { ok: false, message: "Hermes API key is not configured" }
    }

    try {
      await this.request("/models", { method: "GET" })
      return { ok: true, message: "Hermes API server is reachable" }
    } catch (error) {
      return {
        ok: false,
        message: error instanceof Error ? error.message : "Unknown Hermes connection error"
      }
    }
  }

  async complete(messages: LlmMessage[]) {
    if (!this.isConfigured()) {
      return deterministicCompletion(messages)
    }

    const response = await this.request<HermesChatCompletionResponse>("/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: this.model,
        messages,
        stream: false
      })
    })

    return response.choices?.[0]?.message?.content || ""
  }

  private async request<T>(endpoint: string, init: RequestInit) {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), this.timeoutMs)

    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, {
        ...init,
        signal: controller.signal,
        headers: {
          Authorization: `Bearer ${this.apiKey}`,
          ...(init.headers || {})
        }
      })

      if (!response.ok) {
        const detail = await response.text()
        throw new Error(`Hermes request failed ${response.status}: ${trim(detail, 800)}`)
      }

      return (await response.json()) as T
    } finally {
      clearTimeout(timer)
    }
  }
}

function trim(value: string, limit: number) {
  return value.length > limit ? `${value.slice(0, limit)}...` : value
}
