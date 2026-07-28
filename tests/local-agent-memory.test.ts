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

  it("recalls legacy atoms without keywords and skips records without text", async () => {
    const root = await fs.mkdtemp(path.join(os.tmpdir(), "concorso-memory-legacy-"))
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
      await fs.mkdir(path.join(root, "l1"), { recursive: true })
      await fs.writeFile(
        path.join(root, "l1", "atoms.jsonl"),
        [
          JSON.stringify({
            id: "legacy-without-keywords",
            createdAt: "2026-07-01T00:00:00.000Z",
            scope: "editorial-reviewer",
            kind: "instruction",
            text: "Revisionare integralmente il volume uno prima della pubblicazione.",
            sourceConversationId: "legacy-conversation",
            sourceRef: "l0/legacy.md",
            weight: 1
          }),
          JSON.stringify({
            id: "legacy-without-text",
            createdAt: "2026-07-01T00:00:00.000Z",
            scope: "editorial-reviewer",
            kind: "instruction",
            sourceConversationId: "legacy-conversation",
            sourceRef: "l0/legacy.md",
            weight: 1
          })
        ].join("\n") + "\n",
        "utf8"
      )

      const recall = await memory.recall({
        scope: "editorial-reviewer",
        query: "revisione integrale volume uno"
      })

      expect(recall.memories).toHaveLength(1)
      expect(recall.memories[0].id).toBe("legacy-without-keywords")
      expect(recall.context).toContain("prima della pubblicazione")
    } finally {
      await fs.rm(root, { recursive: true, force: true })
    }
  })
})
