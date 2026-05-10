# Test report

## Results

- `npm install`: passed.
- `npm run typecheck`: passed.
- `npm test`: passed, 4 test files and 7 tests.
- `npm run build`: passed, 11 app routes generated.
- `npm run screenshot`: passed, generated `artifacts/dashboard-screenshot.png`.
- 2026-05-10 post-ingest verification: `npm run typecheck`, `npm test`, and `npm run build` passed after adding the new raw sources and wiki notes.
- 2026-05-10 Manual Writer/Graph verification: `npm run typecheck`, `npm test`, `npm run build`, and `npm run screenshot` passed after adding dashboard writer, Codex provider status indicator, and knowledge graph routes.
- 2026-05-10 Codex Writer verification: `npm run typecheck`, `npm test`, `npm run build`, and `npm run screenshot` passed after adding `WRITER_PROVIDER=codex`, Codex CLI adapter, and project writer skill injection.
- 2026-05-10 final Codex Writer typecheck: `npm run typecheck` passed after launcher/docs updates.
- 2026-05-10 GPT-5.5 xhigh pin: `npm run typecheck`, `npm test`, `npm run build`, and `npm run screenshot` passed after pinning Manual Writer Codex calls to `gpt-5.5` and `model_reasoning_effort=xhigh`.
- 2026-05-10 structure guide update: `npm run typecheck`, `npm test`, `npm run build`, and `PORT=3011 npm run screenshot` passed after adding canonical book structure and chapter targets.
- 2026-05-10 structure guide injection: `npm run typecheck`, `npm test`, and `npm run build` passed after making Manual Writer load `books/il-metodo-bando/struttura-madre.md` directly.
- 2026-05-10 outline-ordered writer menu: `npm run typecheck`, `npm test`, and `npm run build` passed after adding `outlineSection` to chapter options.
- 2026-05-10 constitutional sources ingest: `npm run typecheck` and `npm test` passed after metadata-only manual registration and primary Constitution source registration.
- 2026-05-10 authorized constitutional manual processing: `npm run typecheck` and `npm test` passed after user confirmed rights and source note was upgraded from metadata-only to processed.
- 2026-05-10 Book Studio preview milestone: `npm run typecheck`, `npm test`, `npm run build`, `PORT=3011 npm run screenshot`, local dashboard HTTP checks on `http://127.0.0.1:3000` and `http://127.0.0.1:3001`, and `GET /api/book-studio` all passed.
- 2026-05-10 editorial formatting standard: `npm run typecheck`, `npm test`, `npm run build`, and `PORT=3011 npm run screenshot` passed after adding design system files, prompt injection and Book Studio typography update.
- 2026-05-10 Manual Writer actual-chapter correction: `npm run typecheck`, `npm test`, `npm run build`, `PORT=3011 npm run screenshot`, and meta-text grep passed after rejecting meta drafts, enforcing wiki-brain-first policy and rewriting introduction/chapter 1.
- 2026-05-10 A4 paginated preview correction: `npm run typecheck`, `npm test`, `npm run build`, and `$env:PORT='3011'; npm run screenshot` passed after making Book Studio render single A4 pages with justified body text, footer/page numbers, anti-orphan heading pagination and print CSS.
- 2026-05-10 measured pagination optimization: `npm run typecheck`, `npm test`, `npm run build`, and `$env:PORT='3012'; npm run screenshot` passed after replacing heuristic page breaks with measured A4 block pagination and compact manual tables.

## Notes
- First typecheck exposed Node 24 `fs.readdir` typing issues; fixed by using explicit UTF-8 dirent reads.
- First markdown append test exposed excessive blank lines; fixed in section append logic.
- `npm audit` could not complete because npm attempted to write logs under the user cache directory outside the workspace. It is not a release blocker for this local milestone.
