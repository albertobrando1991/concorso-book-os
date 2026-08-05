import { describe, expect, it } from "vitest"
import { LocalAgentMemory } from "@/src/server/memory/local-agent-memory"

describe("temporary IVA project memory capture", () => {
  it("records the completed M-FC02 IVA and filings block", async () => {
    const memory = LocalAgentMemory.fromConfig()
    const result = await memory.captureConversation({
      scope: "concorso-book-os",
      route: "codex-m-fc02-iva-adempimenti",
      messages: [
        {
          role: "user",
          content:
            "Regola globale: i capitoli dei manuali concorsuali devono garantire progressione logica, completezza teorica, definizioni funzionali, autonomia didattica, coerenza tra promessa e contenuto, esempi, casi e strumenti operativi. Per IVA e adempimenti usare struttura stabile e dati mobili solo se verificati e datati."
        }
      ],
      reply:
        "Blocco M-FC02 IVA e adempimenti completato: source ufficiali consolidate, capitoli 4 e 6 a Livello 3, matrice 80 nuclei con 66 completi e 14 blocker residui; modulo ancora non pubblicabile. Commit finale del blocco: 2968cf2."
    })

    expect(result.conversationId).toBeTruthy()
  })
})
