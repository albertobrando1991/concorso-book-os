# ConcorsoBook OS

ConcorsoBook OS is an agentic LLM Wiki platform for building, maintaining, and using a persistent Obsidian-backed knowledge base for Italian public competition books.

GitHub repository: https://github.com/albertobrando1991/concorso-book-os

The book is not treated as a detached document. It is an editorial projection of the consolidated wiki:

- `wiki/raw/` stores immutable source material.
- `wiki/sources/` stores source summaries.
- `wiki/topics/` and `wiki/entities/` store cumulative knowledge.
- `wiki/books/` stores book master notes, outlines, chapters, and revisions.
- `wiki/AGENTS.md` defines operating rules for agents.
- `wiki/index.md` is the catalog.
- `wiki/log.md` is append-only operational history.

## Quick Start

```powershell
npm install
npm run dev
```

Open `http://localhost:3000`.

For live Obsidian operations, install and enable the Obsidian Local REST API plugin, then copy `.env.example` to `.env.local` and set:

```text
OBSIDIAN_BASE_URL=https://127.0.0.1:27124
OBSIDIAN_API_KEY=your-plugin-key
OPENAI_API_KEY=your-openai-key
```

Without Obsidian credentials, the app uses the local `wiki/` directory as the canonical development vault.

## Work From Another PC

Use the same GitHub account to clone the repository and continue work from any PC:

```powershell
git clone https://github.com/albertobrando1991/concorso-book-os.git
cd concorso-book-os
npm install
npm run dev
```

Detailed setup: [docs/WORK_FROM_ANOTHER_PC.md](docs/WORK_FROM_ANOTHER_PC.md).

## Commands

```powershell
npm run typecheck
npm test
npm run build
```

## Delivered Milestone Artifacts

Artifacts live in `artifacts/`:

- task list
- implementation plan
- information architecture map
- vault schema
- dashboard wireframe
- screenshot placeholder/notes
- test report
- diff summary
- final readiness report
- Antigravity Knowledge summary

## Obsidian Local REST API

The integration layer targets the plugin API documented at:

- https://github.com/coddingtonbear/obsidian-local-rest-api
- https://coddingtonbear.github.io/obsidian-local-rest-api/

The client supports note creation, reading, append, search, frontmatter patching, heading patching, and metadata/document-map requests where the plugin exposes them.
