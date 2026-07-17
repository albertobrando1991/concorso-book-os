import { describe, expect, it } from "vitest"
import { mergeFrontmatter, parseFrontmatter, withFrontmatter } from "@/src/server/wiki/frontmatter"

describe("frontmatter", () => {
  it("round trips base values", () => {
    const content = withFrontmatter(
      {
        id: "topic-metodo-bando",
        type: "topic",
        topics: ["metodo bando", "bando decoder"],
        review_required: false,
        confidence: 0.96
      },
      "# Metodo BANDO"
    )
    const parsed = parseFrontmatter(content)

    expect(parsed.data.id).toBe("topic-metodo-bando")
    expect(parsed.data.topics).toEqual(["metodo bando", "bando decoder"])
    expect(parsed.data.review_required).toBe(false)
    expect(parsed.data.confidence).toBe(0.96)
  })

  it("merges surgical frontmatter patches", () => {
    const merged = mergeFrontmatter(
      "---\nid: chapter-1\nstatus: draft\n---\n# Chapter",
      { status: "to_expand", review_required: true }
    )
    const parsed = parseFrontmatter(merged)

    expect(parsed.data.status).toBe("to_expand")
    expect(parsed.data.review_required).toBe(true)
    expect(parsed.body.trim()).toBe("# Chapter")
  })
  it("handles UTF-8 BOM before frontmatter", () => {
    const parsed = parseFrontmatter("\uFEFF---\nid: chapter-12\n---\n# Capitolo")

    expect(parsed.data.id).toBe("chapter-12")
    expect(parsed.body.trim()).toBe("# Capitolo")
  })
})

