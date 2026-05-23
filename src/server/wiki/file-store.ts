import fs from "node:fs/promises"
import path from "node:path"
import { mergeFrontmatter } from "./frontmatter"
import { appendToHeadingSection, replaceHeadingSection } from "./markdown"

export class FileWikiStore {
  constructor(private readonly root: string) {}

  getRoot() {
    return this.root
  }

  async exists(relativePath: string) {
    try {
      await fs.access(this.resolve(relativePath))
      return true
    } catch {
      return false
    }
  }

  async readText(relativePath: string) {
    return fs.readFile(this.resolve(relativePath), "utf8")
  }

  async writeText(relativePath: string, content: string) {
    const absolutePath = this.resolve(relativePath)
    await fs.mkdir(path.dirname(absolutePath), { recursive: true })
    await fs.writeFile(absolutePath, content, "utf8")
  }

  async writeBinary(relativePath: string, content: ArrayBuffer) {
    const absolutePath = this.resolve(relativePath)
    await fs.mkdir(path.dirname(absolutePath), { recursive: true })
    await fs.writeFile(absolutePath, Buffer.from(content))
  }

  async appendText(relativePath: string, content: string) {
    const absolutePath = this.resolve(relativePath)
    await fs.mkdir(path.dirname(absolutePath), { recursive: true })
    await fs.appendFile(absolutePath, content, "utf8")
  }

  async updateFrontmatter(relativePath: string, patch: Record<string, unknown>) {
    const current = await this.readText(relativePath)
    await this.writeText(relativePath, mergeFrontmatter(current, patch))
  }

  async patchHeading(relativePath: string, heading: string, content: string) {
    const current = await this.readText(relativePath)
    await this.writeText(relativePath, replaceHeadingSection(current, heading, content))
  }

  async appendHeading(relativePath: string, heading: string, content: string) {
    const current = await this.readText(relativePath)
    await this.writeText(relativePath, appendToHeadingSection(current, heading, content))
  }

  async listMarkdown(relativeDirectory = "") {
    const base = this.resolve(relativeDirectory)
    const files: string[] = []

    await walk(base)

    return files
      .map((file) => path.relative(this.root, file).replace(/\\/g, "/"))
      .sort()

    async function walk(directory: string) {
      try {
        const entries = await fs.readdir(directory, { withFileTypes: true, encoding: "utf8" })

        for (const entry of entries) {
          const absolutePath = path.join(directory, entry.name)

          if (entry.isDirectory()) {
            await walk(absolutePath)
            continue
          }

          if (entry.isFile() && entry.name.endsWith(".md")) {
            files.push(absolutePath)
          }
        }
      } catch {
        return
      }
    }
  }

  resolve(relativePath: string) {
    const absolutePath = path.resolve(this.root, relativePath)

    if (!absolutePath.startsWith(this.root)) {
      throw new Error(`Refusing to access path outside wiki root: ${relativePath}`)
    }

    return absolutePath
  }
}
