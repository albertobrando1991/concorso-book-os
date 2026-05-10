# Antigravity Knowledge summary

## Project
ConcorsoBook OS: agentic LLM Wiki platform backed by an Obsidian markdown vault for writing and maintaining books for Italian public competitions.

## Canonical product direction
All book generation starts from `Metodo_BANDO_Progetto_Editoriale.md`, imported as:
- raw: `wiki/raw/manuals/metodo-bando-progetto-editoriale.md`
- source note: `wiki/sources/metodo-bando-progetto-editoriale.md`

The active product is `Il Metodo BANDO`: a workbook-style book that teaches candidates to decode public competition notices, plan study, master common subjects and train on outputs. The book must be complete without the website; digital tools are optional optimizers.

## Conventions
- Raw sources are immutable.
- Agent-generated knowledge lives in `sources`, `topics`, `entities`, `books`, `quizzes`, `reviews`.
- `AGENTS.md` defines rules.
- `index.md` is regenerated/cataloged.
- `log.md` is append-only.
- Use surgical heading/frontmatter patches where possible.

## Implementation state
- Next.js/TypeScript app created.
- Dashboard v1 implemented.
- Agents implemented as modular services.
- Obsidian client implemented.
- Metodo BANDO book demo created with four chapters.
- Unit tests added.
- Verification passed: typecheck, unit tests, build and screenshot.
- GitHub remote created and pushed: `https://github.com/albertobrando1991/concorso-book-os`.
- Multi-PC workflow uses GitHub clone/pull/push. Supabase is not required for the current single-owner cross-PC requirement.

## Next tasks
- Re-authenticate GitHub CLI.
- Run install/typecheck/test/build.
- Capture dashboard screenshot.
- Add live Obsidian API smoke test.
- Expand official source base.

## 2026-05-10 source ingest
- New raw PDF: `wiki/raw/manuals/MANUALE DIRITTO AMMINISTRATIVO.pdf`.
- New raw web clipping: responsabilità dirigenziale, performance e governo del rischio.
- Created source notes, topic pages and entities for diritto amministrativo foundations, responsabilità dirigenziale, performance amministrativa, governo del rischio, contratti pubblici and PNRR.
- Impacted book: `Il Metodo BANDO`, especially chapters `diritto-amministrativo-per-candidati` and `sistema-adattabile`.

## 2026-05-10 Manual Writer and skills
- Added Manual Writer Agent for dashboard-driven chapter writing.
- Default writer provider is `WRITER_PROVIDER=codex`, using local `codex exec` instead of an OpenAI API key.
- Manual Writer Codex calls are pinned to `CODEX_WRITER_MODEL=gpt-5.5` and `CODEX_WRITER_REASONING_EFFORT=xhigh`.
- Added project skill `.agents/skills/concorso-book-professional-writer/SKILL.md`.
- Manual Writer Agent injects the project writer skill into Codex prompts and still uses only consolidated wiki knowledge, never raw sources.
- Added interactive knowledge graph for sources, topics, entities, books, chapters and reviews.
- Current blocker for true Codex-backed generation: local `codex login status` reports not logged in. After login, dashboard writing can use Codex CLI; until then it falls back to a structured local draft.
