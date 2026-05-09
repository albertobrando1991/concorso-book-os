import { describe, expect, it } from "vitest"
import { encodeVaultPath } from "@/src/server/obsidian/client"

describe("obsidian client helpers", () => {
  it("encodes path segments without losing folder separators", () => {
    expect(encodeVaultPath("books/il metodo bando/index.md")).toBe(
      "books/il%20metodo%20bando/index.md"
    )
  })
})

