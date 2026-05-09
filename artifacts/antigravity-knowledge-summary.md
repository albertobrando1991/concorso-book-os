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
