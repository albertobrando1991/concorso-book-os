import fs from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { LocalAgentMemory, withLocalMemoryContext } from "@/src/server/memory/local-agent-memory"
import type { LlmMessage } from "@/src/server/llm/openai-adapter"

describe("LocalAgentMemory", () => {
  it("captures conversations as layered memory and recalls relevant atoms", async () => {
    const root = await fs.mkdtemp(path.join(os.tmpdir(), "concorso-memory-"))
    const memory = new LocalAgentMemory({
      enabled: true,
      root,
      recallMaxResults: 3,
      recallMaxTotalChars: 1200,
      maxCharsPerMessage: 2000,
      maxMessagesPerConversation: 8,
      maxAtomsPerConversation: 5
    })

    try {
      await memory.captureConversation({
        scope: "manual-writer",
        route: "test",
        messages: [
          {
            role: "user",
            content:
              "Ricorda: preferisco che il Manual Writer usi sempre il formato workbook Metodo BANDO per il capitolo contabilita pubblica."
          }
        ],
        reply: "Preferenza registrata."
      })

      const recall = await memory.recall({
        scope: "manual-writer",
        query: "Scrivi il capitolo di contabilita pubblica con formato workbook Metodo BANDO."
      })
      const stats = await memory.stats()

      expect(recall.memories.length).toBeGreaterThan(0)
      expect(recall.context).toContain("Metodo BANDO")
      expect(stats.conversations).toBe(1)
      expect(stats.atoms).toBeGreaterThan(0)
      await expect(fs.stat(path.join(root, "l2", "scenarios.md"))).resolves.toBeTruthy()
      await expect(fs.stat(path.join(root, "l3", "persona.md"))).resolves.toBeTruthy()
    } finally {
      await fs.rm(root, { recursive: true, force: true })
    }
  })

  it("injects recalled memory as a system message", () => {
    const messages: LlmMessage[] = [{ role: "user", content: "ciao" }]
    const withMemory = withLocalMemoryContext(messages, {
      context: "Memoria locale richiamata.",
      memories: [],
      totalChars: 0
    })

    expect(withMemory).toHaveLength(2)
    expect(withMemory[0].role).toBe("system")
    expect(withMemory[1]).toBe(messages[0])
  })
})
