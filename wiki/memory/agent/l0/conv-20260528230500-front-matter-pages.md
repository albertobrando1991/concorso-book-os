---
id: conv-20260528230500-front-matter-pages
type: agent_memory_conversation
created_at: "2026-05-28T23:05:00+02:00"
scope: global
route: codex/front-matter-pages
---

# Integrazione prime pagine Metodo BANDO

Richiesta: analizzare il DOCX `PER LIBRO.docx` e le immagini di riferimento EdiSES per implementare nel libro le sezioni mancanti: servizi digitali con QR, frontespizio, copyright/colophon, sommario, premessa e indice dettagliato.

Esito: create sei pagine in `wiki/books/il-metodo-bando/front-matter/`, copiato il QR in `wiki/books/il-metodo-bando/assets/front-matter/qr-capitale-personale.png`, verificato che il QR punta a `https://www.capitalepersonale.it/`, aggiornato Book Studio per caricare il front matter prima dei capitoli e renderizzarlo con layout dedicati. L'indice dettagliato viene generato dai titoli e sottotitoli effettivi dei capitoli.

Validazione: `npm test -- book-preview.test.ts` passato con 3 test; `npm run typecheck` passato; screenshot Playwright salvato in `artifacts/dashboard-screenshot.png`.
