export interface ObsidianClientOptions {
  baseUrl: string
  apiKey: string
}

export interface ObsidianPatchOptions {
  operation: "append" | "prepend" | "replace"
  targetType: "heading" | "block" | "frontmatter"
  target: string
  content: string
}

export class ObsidianLocalRestClient {
  constructor(private readonly options: ObsidianClientOptions) {}

  isConfigured() {
    return Boolean(this.options.baseUrl && this.options.apiKey)
  }

  async health() {
    if (!this.isConfigured()) {
      return { ok: false, message: "Obsidian API key is not configured" }
    }

    try {
      await this.request("/")
      return { ok: true, message: "Obsidian Local REST API is reachable" }
    } catch (error) {
      return {
        ok: false,
        message: error instanceof Error ? error.message : "Unknown Obsidian connection error"
      }
    }
  }

  async readNote(path: string) {
    return this.request(`/vault/${encodeVaultPath(path)}`)
  }

  async createOrReplaceNote(path: string, content: string) {
    return this.request(`/vault/${encodeVaultPath(path)}`, {
      method: "PUT",
      body: content,
      headers: {
        "Content-Type": "text/markdown"
      }
    })
  }

  async appendNote(path: string, content: string) {
    return this.request(`/vault/${encodeVaultPath(path)}`, {
      method: "POST",
      body: content,
      headers: {
        "Content-Type": "text/markdown"
      }
    })
  }

  async patchNote(path: string, options: ObsidianPatchOptions) {
    return this.request(`/vault/${encodeVaultPath(path)}`, {
      method: "PATCH",
      body: options.content,
      headers: {
        "Content-Type": "text/markdown",
        Operation: options.operation,
        "Target-Type": options.targetType,
        Target: options.target
      }
    })
  }

  async patchFrontmatter(path: string, yamlPatch: string) {
    return this.patchNote(path, {
      operation: "replace",
      targetType: "frontmatter",
      target: "",
      content: yamlPatch
    })
  }

  async patchHeading(path: string, heading: string, content: string) {
    return this.patchNote(path, {
      operation: "replace",
      targetType: "heading",
      target: heading,
      content
    })
  }

  async appendHeading(path: string, heading: string, content: string) {
    return this.patchNote(path, {
      operation: "append",
      targetType: "heading",
      target: heading,
      content
    })
  }

  async search(query: string) {
    return this.request("/search/simple/", {
      method: "POST",
      body: JSON.stringify({ query }),
      headers: {
        "Content-Type": "application/json"
      }
    })
  }

  async getMetadata(path: string) {
    return this.request(`/vault/${encodeVaultPath(path)}/metadata`)
  }

  private async request(endpoint: string, init: RequestInit = {}) {
    const response = await fetch(`${this.options.baseUrl}${endpoint}`, {
      ...init,
      headers: {
        Authorization: `Bearer ${this.options.apiKey}`,
        ...(init.headers || {})
      }
    })

    if (!response.ok) {
      const detail = await response.text()
      throw new Error(`Obsidian request failed ${response.status}: ${detail}`)
    }

    const text = await response.text()
    const contentType = response.headers.get("content-type") || ""

    if (contentType.includes("application/json")) {
      return JSON.parse(text)
    }

    return text
  }
}

export function encodeVaultPath(path: string) {
  return path
    .split("/")
    .map((segment) => encodeURIComponent(segment))
    .join("/")
}

