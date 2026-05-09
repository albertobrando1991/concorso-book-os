import { describe, expect, it } from "vitest"
import { classifySource } from "@/src/server/agents/classifier"

describe("source classifier", () => {
  it("recognizes Metodo BANDO product references", () => {
    const source = classifySource({
      title: "Metodo BANDO progetto editoriale",
      sourceType: "manual",
      content: "Bando Decoder, Moduli Profilo, Piano 30/60/90 giorni e Diario errori sono il cuore del libro."
    })

    expect(source.topics).toContain("metodo bando")
    expect(source.topics).toContain("bando decoder")
    expect(source.entities).toContain("Metodo BANDO")
    expect(source.entities).toContain("Bando Decoder")
  })
})

