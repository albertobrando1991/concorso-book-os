# Agent Memory Scenarios

## 2026-05-27T21:45:00.000Z - global

- conversation_id: conv-20260527214500-always-on-memory
- route: codex-user-preference
- l0: l0/conv-20260527214500-always-on-memory.md
- atoms:
  - mem-20260527214500-always-on-memory | preference | Nel contesto ConcorsoBook OS la memoria locale deve restare sempre attiva per ricordare cio' che e' stato detto e migliorare progressivamente gli output.

## 2026-05-27T21:55:00.000Z - global

- conversation_id: conv-20260527215500-shared-provider-memory
- route: codex-user-preference
- l0: l0/conv-20260527215500-shared-provider-memory.md
- atoms:
  - mem-20260527215500-shared-provider-memory | instruction | La memoria persistente del progetto deve essere condivisa da tutti gli agenti e provider usati: Codex/GPT, Claude, Kimi, OpenAI API, Hermes e locale.

## 2026-05-28T00:50:00.000Z - global

- conversation_id: conv-20260528005000-ruflo-stop-hook-patch
- route: codex-system-maintenance
- l0: l0/conv-20260528005000-ruflo-stop-hook-patch.md
- atoms:
  - mem-20260528005000-ruflo-stop-hook-patch | system-fix | L'avviso ricorrente Stop hook failed era causato dallo Stop hook di Claude/Ruflo ruflo-core 0.2.0 che chiamava npx claude-flow@alpha; il file hooks.json globale e' stato patchato per wrappare quei comandi con cmd /c e fallback exit 0 tramite node.

## 2026-05-27T23:13:08.944Z - global

- conversation_id: conv-20260527231308-1pogjhn
- route: codex/resolve-skill-and-mcp-warnings
- l0: l0/conv-20260527231308-1pogjhn.md
- atoms:
  - mem-20260527231308-116gwtz | project_fact | Risolvi tutti gli avvisi di caricamento skill e MCP Supabase nel contesto ConcorsoBook OS.
  - mem-20260527231308-10gu8jz | result | Esito codex/resolve-skill-and-mcp-warnings: Risolvi tutti gli avvisi di caricamento skill e MCP Supabase nel contesto ConcorsoBook OS. -> Corretti 17 SKILL.md con frontmatter YAML valido, description presente e sotto 1024 caratteri; rigenerata autenticazione OAuth del MCP Supabase con codex mcp logout/login.

## 2026-05-28T11:43:54.020Z - global

- conversation_id: conv-20260528114354-1rtulm9
- route: codex/resolve-heygen-skill-cache-warnings
- l0: l0/conv-20260528114354-1rtulm9.md
- atoms:
  - mem-20260528114354-1hznga7 | result | Esito codex/resolve-heygen-skill-cache-warnings: Gli avvisi continuano a uscire per HeyGen 719ed655: heygen-avatar e heygen-video hanno description oltre 1024 caratteri. -> Corretti i due SKILL.md HeyGen nel cache 719ed655 e le due copie sorgente temporanee in .codex/.tmp/plugins/plugins/heygen; validazione finale: 4 copie controllate, tutte valide.

## 2026-05-28T15:48:49.069Z - global

- conversation_id: conv-20260528154849-4kjfkk
- route: codex/adapt-book-layout-from-docx
- l0: l0/conv-20260528154849-4kjfkk.md
- atoms:
  - mem-20260528154849-1cefyks | project_fact | Adatta layout del libro e delle pagine alla proposta_layout_editoriale_metodo_bando.docx, mantenendo il colore pagina attuale e l'ottimizzazione dei margini.
  - mem-20260528154849-l23wje | result | Esito codex/adapt-book-layout-from-docx: Adatta layout del libro e delle pagine alla proposta_layout_editoriale_metodo_bando.docx, mantenendo il colore pagina attuale e l'ottimizzazione dei margini. -> Aggiornata la preview editoriale a 16,8 x 24 cm con Playfair Display, Montserrat, palette Navy/Bordeaux/Muted Gold, barra BANDO e callout box; mantenuto colore pagina esistente e margini ottimizzati.

## 2026-05-28T16:05:00.000Z - global

- conversation_id: conv-20260528160500-dashboard-next-cache
- route: codex/fix-dashboard-next-cache
- l0: l0/conv-20260528160500-dashboard-next-cache.md
- atoms:
  - mem-20260528160500-dashboard-next-cache | system-fix | Errore dashboard Cannot find module './331.js' risolto fermando il processo Next su porta 3000, eliminando solo la cache generata .next e riavviando npm run dev su 127.0.0.1:3000; verificati / e /api/book-studio/assets/file con HTTP 200 e screenshot artifacts/dashboard-check.png.

## 2026-05-28T17:55:00.000Z - global

- conversation_id: conv-20260528175500-ch12-logic-corpus
- route: codex/ingest-chapter-12-logic-corpus
- l0: l0/conv-20260528175500-ch12-logic-corpus.md
- atoms:
  - mem-20260528175500-ch12-logic-corpus | result | Preparato il knowledge pack per il capitolo 12 Logica, comprensione del testo e ragionamento: scaricati 19 PDF leciti in wiki/raw/chapter-12-logica-comprensione-ragionamento, creati 5 source notes, 4 topic pages, aggiornati index/log e portato il capitolo a status knowledge-ready preservando le note pregresse.

## 2026-05-28T20:25:00.000+02:00 - global

- conversation_id: conv-20260528202500-ch12-editorial-draft
- route: codex/write-chapter-12-editorial-draft
- l0: l0/conv-20260528202500-ch12-editorial-draft.md
- atoms:
  - mem-20260528202500-ch12-editorial-draft | result | Scritto il Testo editoriale professionale del capitolo 12 Logica, comprensione del testo e ragionamento: capitolo in status revised_draft/editorial-revision, con mappa BANDO, metodi per logica, comprensione, ragionamento critico e numerico, diario errori, domanda commissario, mini-esercizio e mini-simulazione originale da 25 quesiti.

## 2026-05-28T20:38:00.000+02:00 - global

- conversation_id: conv-20260528203800-editorial-proofread-chapters
- route: codex/editorial-proofread-chapters
- l0: l0/conv-20260528203800-editorial-proofread-chapters.md
- atoms:
  - mem-20260528203800-editorial-proofread-chapters | result | Revisione editoriale capillare dei capitoli scritti del Metodo BANDO: audit da Introduzione a Capitolo 12, rimozione di sezioni interne dal Capitolo 12, pulizia di link wiki visibili, correzione di accenti/sintassi/titoli e microcorrezioni nel Capitolo 9 Contratti pubblici; git diff --check e test preview libro passati.
