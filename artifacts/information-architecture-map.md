# Information architecture map

## Knowledge layers
- Layer 1 raw immutable: `wiki/raw/**`
- Layer 2 generated wiki: `wiki/sources`, `wiki/topics`, `wiki/entities`, `wiki/books`, `wiki/quizzes`, `wiki/reviews`
- Layer 3 schema: `wiki/AGENTS.md`
- Catalog: `wiki/index.md`
- Append-only operations: `wiki/log.md`

## Product graph
- Canonical source: `sources/metodo-bando-progetto-editoriale`
- Core topics: `metodo-bando`, `anatomia-del-bando`, `bando-decoder`, `moduli-profilo`, `piano-30-60-90-giorni`, `diario-errori`
- Active book: `books/il-metodo-bando/index`
- Demo chapters: `anatomia-del-bando`, `il-metodo-bando`, `diritto-amministrativo-per-candidati`, `sistema-adattabile`

## App map
- Dashboard: `app/page.tsx`
- API routes: `app/api/**`
- Agents: `src/server/agents/**`
- Obsidian client: `src/server/obsidian/client.ts`
- Wiki utilities: `src/server/wiki/**`

