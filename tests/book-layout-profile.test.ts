import { describe, expect, it } from "vitest"

import { bookLayoutClass } from "../src/server/book/book-layout-profile"

describe("bookLayoutClass", () => {
  it("compatta esclusivamente VOL-03", () => {
    expect(bookLayoutClass("volumi/vol-03")).toBe("bookLayoutVol03Compact")
    expect(bookLayoutClass("volumi/vol-07")).toBe("")
    expect(bookLayoutClass("il-metodo-bando")).toBe("")
  })
})
