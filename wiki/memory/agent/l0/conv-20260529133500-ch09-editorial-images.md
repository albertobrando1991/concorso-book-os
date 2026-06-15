---
id: conv-20260529133500-ch09-editorial-images
type: agent_memory_conversation
created_at: "2026-05-29T13:35:00+02:00"
scope: global
route: codex/illustrate-chapter-09-contracts
---

# Immagini editoriali Capitolo 9

Richiesta: individuare, elaborare, generare e inserire in modo professionale le immagini necessarie per il Capitolo 9 `Contratti pubblici essenziali`.

Esito: generate 6 figure didattiche in `wiki/books/il-metodo-bando/assets/chapter-09/` con master SVG e PNG per preview/export: mappa generale contratti pubblici, ciclo dal fabbisogno all'esecuzione, scala procedure/concorrenza, documenti gara-offerte-stipula, ecosistema digitale BDNCP/PCP/FVOE/CIG/piattaforme, sintesi portale-controlli-responsabilita. Le immagini sono state inserite nel capitolo nei punti didattici pertinenti.

Validazione: `npm test` passato con 19 test, `npm run typecheck` passato, `git diff --check` passato. Verifica Playwright su `127.0.0.1:3000`: 25 pagine preview Capitolo 9, 6 immagini chapter-09 caricate, nessuna sovrapposizione col footer.
