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

## 2026-05-10 struttura madre libro
- The user's long outline is now the canonical operational guide for developing the manual.
- Canonical guide file: `wiki/books/il-metodo-bando/struttura-madre.md`.
- Source summary: `wiki/sources/struttura-madre-il-metodo-bando.md`.
- Book index now lists introduction, 24 chapters and 6 appendices.
- Manual Writer Agent must start from `books/il-metodo-bando/struttura-madre.md`, then the selected chapter note and its `Specifica struttura madre`, then use consolidated wiki knowledge for the actual content.

## 2026-05-10 constitutional source ingest
- New local raw PDF detected: `wiki/raw/manuals/Diritto Costituzionale (Pitruzzella G. R.Bin) (z-library.sk, 1lib.sk, z-lib.sk).pdf`.
- The PDF is ignored from GitHub because rights are unverified and the filename references z-library/z-lib.
- Created metadata-only source note: `wiki/sources/diritto-costituzionale-bin-pitruzzella.md`.
- New primary source detected: `wiki/raw/decrees/Costituzione_ITALIANa.pdf`.
- Created official/primary source note: `wiki/sources/costituzione-repubblica-italiana-testo-vigente.md`.
- Created topics: `diritto-costituzionale`, `ordinamento-dello-stato`, `principi-costituzionali-pa`.
- Created constitutional entity stubs and impacted chapter `costituzione-e-ordinamento-dello-stato`.
- Rule: do not extract or summarize the manual PDF until rights are verified; use the Constitution source and official primary sources for publishable chapter text.

## 2026-05-10 constitutional manual rights confirmed
- User confirmed they own/hold the rights for the Bin/Pitruzzella constitutional manual.
- Created clean raw copy: `wiki/raw/manuals/diritto-costituzionale-bin-pitruzzella-authorized.pdf`.
- Original z-library-named file remains ignored by Git.
- Source note `wiki/sources/diritto-costituzionale-bin-pitruzzella.md` is now `processed` with policy `summaries_and_conceptual_extraction_allowed_no_long_verbatim`.
- Added topics: `forme-di-stato`, `forme-di-governo`, `fonti-dell-ordinamento-italiano`, `giustizia-costituzionale`, `diritti-e-liberta-costituzionali`, `regioni-e-governo-locale`.
- Chapter `costituzione-e-ordinamento-dello-stato` is now `knowledge-ready`.

## 2026-05-10 Book Studio preview
- Added dashboard section `Book Studio` for visual review of `Il Metodo BANDO`.
- The preview is generated from `wiki/books/il-metodo-bando/chapters/*.md`, sorted by `outline_section`.
- The UI supports chapter view and full-book view, with a formatted book page for review.
- The selected chapter can be sent to Manual Writer Agent/Codex directly from the preview.
- Image upload stores assets in `wiki/raw/assets/books/il-metodo-bando/` and appends an Obsidian embed under `## Immagini e layout`.
- API routes added: `GET /api/book-studio`, `POST /api/book-studio/assets`, `GET /api/book-studio/assets/file`.
- Verification passed: typecheck, tests, build, screenshot, dashboard HTTP 200 on ports 3000 and 3001, Book Studio API HTTP 200.

## 2026-05-10 editorial formatting standard
- Canonical file: `wiki/books/il-metodo-bando/design-system-editoriale.md`.
- Research source note: `wiki/sources/book-layout-typography-standards.md`.
- Decision: professional manual-workbook, not novel or dense legal compendium.
- Primary format: 17 x 24 cm circa, KDP equivalent `6.69 x 9.61 in`; alternative workbook format `7 x 10 in`.
- Typography: Source Serif 4 for body, Source Sans 3 for headings, boxes, captions and tables; fallback serif/sans stacks defined.
- Layout: single-column explanation, recurring operational boxes, short paragraphs, readable tables, didactic images only.
- Book Studio preview now reflects the design system with manual typography and page styling.

## 2026-05-10 Manual Writer actual-chapter correction
- User correctly identified that Manual Writer fallback was writing meta summaries, not real chapters.
- Manual Writer Agent now rejects outputs containing meta markers such as `Aggiornamento generato`, `Istruzione ricevuta`, `Knowledge consolidata`, or `questo blocco sviluppa`.
- Default dashboard prompts now instruct the writer to produce actual reader-facing chapter text.
- Rule clarified: the wiki brain is mandatory and comes first; web research is used only for updates/verification and must be consolidated into source notes before becoming stable knowledge.
- Rewrote `books/il-metodo-bando/chapters/introduzione.md` and `books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md` as real editorial drafts.
- Book Studio preview now renders markdown tables, so workbook grids display properly.
