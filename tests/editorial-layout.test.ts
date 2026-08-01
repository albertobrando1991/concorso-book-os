import { access, readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"
import {
  TEXT_CATALOG_MODULE_COUNT,
  TEXT_VOLUME_CATALOG
} from "@/src/catalog/text-volumes"
import { parseFrontmatter } from "@/src/server/wiki/frontmatter"

const wikiRoot = path.resolve(process.cwd(), "wiki")

describe("specialist module editorial layout", () => {
  it("keeps every catalog module plan under planning and outside reader chapters", async () => {
    const moduleIds = [...new Set(TEXT_VOLUME_CATALOG.flatMap((volume) => volume.bookIds))]
      .filter((bookId) => bookId.startsWith("moduli/"))

    expect(moduleIds).toHaveLength(TEXT_CATALOG_MODULE_COUNT)

    for (const moduleId of moduleIds) {
      const legacyPath = path.join(wikiRoot, "books", moduleId, "chapters", "00-piano-editoriale.md")
      const planPath = path.join(wikiRoot, "books", moduleId, "planning", "00-piano-editoriale.md")

      expect(await exists(legacyPath), `${moduleId} still exposes its plan as a chapter`).toBe(false)
      expect(await exists(planPath), `${moduleId} has no canonical editorial plan`).toBe(true)

      const data = parseFrontmatter(await readFile(planPath, "utf8")).data

      expect(data.type, `${moduleId} has a non-canonical plan type`).toBe("editorial_plan")
      expect(data.tags, `${moduleId} is missing the staff-only plan tag`).toContain("specialist-module-plan")
      expect(data.outline_section, `${moduleId} still gives the plan a reader outline number`).toBeUndefined()
    }
  })
})

async function exists(file: string) {
  try {
    await access(file)
    return true
  } catch {
    return false
  }
}
