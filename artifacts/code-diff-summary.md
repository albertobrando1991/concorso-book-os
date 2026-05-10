# Code diff summary

## Added
- Next.js dashboard and API routes.
- Obsidian Local REST API client.
- Local wiki file store.
- Agent modules for ingest, maintenance, book writing, quiz, lint and review.
- Obsidian vault with LLM Wiki structure.
- Canonical Metodo BANDO product source integration.
- Demo book `Il Metodo BANDO` with four chapters.
- Unit tests and artifact documents.

## Changed
- Active book changed from a generic enti locali demo to `Il Metodo BANDO`.
- Default book ID changed to `il-metodo-bando`.
- Classifier expanded with Metodo BANDO, Bando Decoder, Moduli Profilo, Piano 30/60/90 and Diario Errori.
- 2026-05-10 ingest: added source notes and wiki graph updates for `MANUALE DIRITTO AMMINISTRATIVO.pdf` and the article on responsabilità dirigenziale, performance and risk governance.
- Added Manual Writer Agent with dashboard interaction and managed chapter writing sections.
- Added dashboard writer provider status indicator so the user can see whether Codex, OpenAI, or local fallback writing is active.
- Added Codex CLI writer provider so chapter writing can use the local Codex account instead of requiring an OpenAI API key.
- Pinned the Codex writer provider to `gpt-5.5` with `model_reasoning_effort=xhigh`.
- Added project skill `.agents/skills/concorso-book-professional-writer/SKILL.md` and inject it into Manual Writer Agent prompts.
- Updated Windows launcher to warn when Codex CLI is missing or not authenticated.
- Added interactive dashboard Knowledge Graph for sources, topics, entities, books, chapters and reviews.
- Added skills research artifact with current web findings and project skill recommendations.
- Added canonical `Il Metodo BANDO` structure guide with introduction, 24 chapters and 6 appendices.
- Updated Manual Writer rules so every chapter starts from `struttura-madre.md` and the chapter `Specifica struttura madre`.
- Manual Writer now injects the canonical structure guide directly into Codex/OpenAI prompts for `Il Metodo BANDO` chapters.
- Manual Writer chapter menu now follows outline order instead of alphabetical order.
