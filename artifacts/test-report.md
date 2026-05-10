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

## Notes
- First typecheck exposed Node 24 `fs.readdir` typing issues; fixed by using explicit UTF-8 dirent reads.
- First markdown append test exposed excessive blank lines; fixed in section append logic.
- `npm audit` could not complete because npm attempted to write logs under the user cache directory outside the workspace. It is not a release blocker for this local milestone.
