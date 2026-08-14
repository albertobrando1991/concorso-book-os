import fs from "node:fs"
import { describe, expect, it } from "vitest"

import { bookLayoutClass } from "../src/server/book/book-layout-profile"

describe("bookLayoutClass", () => {
  it("compatta esclusivamente VOL-03", () => {
    expect(bookLayoutClass("volumi/vol-03")).toBe("bookLayoutVol03Compact")
    expect(bookLayoutClass("volumi/vol-07")).toBe("")
    expect(bookLayoutClass("il-metodo-bando")).toBe("")
  })
})

describe("profilo tipografico VOL-03", () => {
  it("mantiene corpo 11 pt e compatta soltanto il ritmo verticale", () => {
    const css = fs.readFileSync("app/globals.css", "utf8")
    const block = css.match(/\.bookLayoutVol03Compact \.previewBlocks \{([\s\S]*?)\}/)?.[1] || ""

    expect(block).toContain("font-size: 11pt")
    expect(block).toContain("line-height: 1.15")
    expect(css).toContain(".bookLayoutVol03Compact .previewBlocks p {\n  margin-bottom: 2pt;")
    expect(block).not.toContain("--book-padding")
  })
})