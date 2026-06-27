import { NextResponse } from "next/server"
import { getWikiRoot } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import { slugify } from "@/src/server/wiki/slug"
import { baseFrontmatter, bookNotePath, chapterNotePath } from "@/src/server/wiki/templates"
import { withFrontmatter } from "@/src/server/wiki/frontmatter"
import { KnowledgeMaintainer } from "@/src/server/agents/knowledge-maintainer"

export async function POST(request: Request) {
  try {
    const { bookId: rawBookId, title, structureSource } = await request.json()

    if (!rawBookId || !title || !structureSource) {
      return NextResponse.json(
        { error: "bookId, title and structureSource are required" },
        { status: 400 }
      )
    }

    const bookId = slugify(rawBookId)
    if (!/^[a-z0-9-]+$/.test(bookId)) {
      return NextResponse.json(
        { error: "bookId must contain only letters, numbers and hyphens" },
        { status: 400 }
      )
    }

    const store = new FileWikiStore(getWikiRoot())
    const masterPath = bookNotePath(bookId)

    if (await store.exists(masterPath)) {
      return NextResponse.json(
        { error: `Il libro con ID "${bookId}" esiste già.` },
        { status: 400 }
      )
    }

    // Parse structureSource
    const lines = structureSource.replace(/\r\n/g, "\n").split("\n")
    const parsedChapters: Array<{
      title: string
      slug: string
      path: string
      section: string
      type: "front_matter" | "chapter"
    }> = []

    let fmIndex = 1
    let chIndex = 1

    for (const rawLine of lines) {
      const line = rawLine.trim()
      if (!line) continue

      const listMatch =
        /^(FM\d+|FM|\d+)\.?\s+(.+)$/i.exec(line) ||
        /^\s*[-*]\s+(.+)$/.exec(line) ||
        /^\s*(.+)$/.exec(line)

      if (listMatch) {
        const prefix = listMatch[1]
        let itemTitle = listMatch[2] || listMatch[1]
        itemTitle = itemTitle.trim()

        if (!itemTitle || itemTitle.startsWith("#")) continue

        const isFM =
          prefix?.toUpperCase().startsWith("FM") ||
          itemTitle.toLowerCase().includes("front-matter") ||
          itemTitle.toLowerCase().includes("premessa") ||
          itemTitle.toLowerCase().includes("sommario") ||
          itemTitle.toLowerCase().includes("sommario") ||
          itemTitle.toLowerCase().includes("colophon")

        const slug = slugify(itemTitle)
        if (isFM) {
          const section = prefix?.toUpperCase().startsWith("FM") ? prefix.toUpperCase() : `FM${fmIndex++}`
          parsedChapters.push({
            title: itemTitle,
            slug,
            path: `books/${bookId}/front-matter/${slug}.md`,
            section,
            type: "front_matter"
          })
        } else {
          const sectionNum = /^\d+$/.test(prefix) ? prefix : String(chIndex++)
          parsedChapters.push({
            title: itemTitle,
            slug,
            path: `books/${bookId}/chapters/${slug}.md`,
            section: sectionNum,
            type: "chapter"
          })
        }
      }
    }

    if (parsedChapters.length === 0) {
      return NextResponse.json(
        { error: "Nessun capitolo o sezione rilevata nella struttura inserita." },
        { status: 400 }
      )
    }

    const changedFiles: string[] = []
    const now = new Date().toISOString()

    // 1. Create each chapter note
    for (const ch of parsedChapters) {
      const frontmatter = baseFrontmatter({
        id: `${ch.type === "front_matter" ? "fm" : "chapter"}-${ch.slug}`,
        type: ch.type,
        title: ch.title,
        status: "draft",
        bookRefs: [bookId],
        confidence: 0.5,
        reviewRequired: true,
        tags: [ch.type === "front_matter" ? "front-matter" : "book-chapter"],
        extra: {
          book_id: bookId,
          outline_section: ch.section,
          draft_stage: "structure"
        }
      })

      const content = withFrontmatter(
        frontmatter,
        `# ${ch.title}

## Obiettivo didattico
Da definire.

## Specifica struttura madre
- Da definire.

## Testo editoriale

## Bozza agente

## Note editoriali
- Capitolo inizializzato da struttura di partenza.
`
      )

      await store.writeText(ch.path, content)
      changedFiles.push(ch.path)
    }

    // 2. Create the master book file index.md
    const bookFrontmatter = baseFrontmatter({
      id: bookId,
      type: "book",
      title,
      status: "draft",
      topics: [],
      entities: [],
      sourceRefs: [],
      bookRefs: [bookId],
      confidence: 0.7,
      reviewRequired: true,
      tags: ["book"]
    })

    const fmList = parsedChapters
      .filter((ch) => ch.type === "front_matter")
      .map((ch) => `${ch.section}. [[${ch.path.replace(".md", "")}|${ch.title}]]`)
      .join("\n")

    const chList = parsedChapters
      .filter((ch) => ch.type === "chapter")
      .map((ch) => `${ch.section}. [[${ch.path.replace(".md", "")}|${ch.title}]]`)
      .join("\n")

    const bookContent = withFrontmatter(
      bookFrontmatter,
      `# ${title}

## Obiettivo editoriale
Libro-workbook operativo inizializzato da struttura di partenza.

## Outline

### Prime pagine
${fmList || "- Nessuna sezione prime pagine inserita."}

### Capitoli del manuale
${chList || "- Nessun capitolo inserito."}

## Stato revisione
- Inizializzato il ${now}.
- Struttura iniziale pronta per la scrittura.
`
    )

    await store.writeText(masterPath, bookContent)
    changedFiles.push(masterPath)

    // 3. Append to log.md
    await store.appendText(
      "log.md",
      `\n- ${now} | book_create | ${bookId} | title=${title} | chapters=${parsedChapters.length}`
    )
    changedFiles.push("log.md")

    // 4. Update wiki/index.md
    const maintainer = new KnowledgeMaintainer(store)
    await maintainer.updateIndex()

    return NextResponse.json({
      status: "created",
      bookId,
      title,
      chaptersCreated: parsedChapters.length,
      changedFiles
    })
  } catch (error) {
    const message = error instanceof Error ? error.message : "Impossibile creare il libro"
    return NextResponse.json({ error: message }, { status: 500 })
  }
}
