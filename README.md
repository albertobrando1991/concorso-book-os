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

On Windows, double-click:

```text
AVVIA_CONCORSOBOOK.bat
```

Keep the terminal window open, then open `http://127.0.0.1:3000`.

Manual start:

```powershell
npm install
npm run dev
```

Open `http://localhost:3000`.

For live Obsidian operations, install and enable the Obsidian Local REST API plugin, then copy `.env.example` to `.env.local` and set:

```text
OBSIDIAN_BASE_URL=https://127.0.0.1:27124
OBSIDIAN_API_KEY=your-plugin-key
WRITER_PROVIDER=codex
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

## Manual Writer Agent

The dashboard includes a specialized writing agent for book chapters. It reads consolidated wiki knowledge and writes managed chapter sections without using raw sources directly.

Default provider: local `codex exec`, so the Writer can use your Codex/Antigravity account instead of a separate OpenAI API key.
The writer is configured to call `gpt-5.5` with `model_reasoning_effort=xhigh`.
Run `codex login --device-auth` once on the PC if the launcher reports that Codex CLI is not authenticated.

Guide: [docs/WRITING_WITH_MANUAL_AGENT.md](docs/WRITING_WITH_MANUAL_AGENT.md).

## Hermes Agent

Hermes can be used as an internal writer/runtime by setting:

```text
WRITER_PROVIDER=hermes
HERMES_API_BASE=http://127.0.0.1:8642/v1
HERMES_API_KEY=your-hermes-api-key
HERMES_MODEL=hermes-agent
HERMES_WEBHOOK_SECRET=shared-secret-for-hermes-calls
```

Useful local endpoints:

- `GET /api/hermes/health` checks the Hermes API server.
- `POST /api/hermes/chat` sends server-side chat messages to Hermes.
- `POST /api/hermes/import-source` lets Hermes/Telegram import an official source URL into the wiki, link it to a chapter, and optionally run the writer.

For PDF imports, the Hermes import endpoint can call GLM-OCR before creating the source note:

```text
GLM_OCR_ENABLED=true
GLM_OCR_COMMAND=glmocr
GLM_OCR_TIMEOUT_MS=600000
```

Install the SDK separately with `pip install glmocr` and configure its own API/self-hosted backend as required by GLM-OCR.

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
