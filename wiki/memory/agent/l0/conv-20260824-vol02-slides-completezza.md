---
id: conv-20260824-vol02-slides-completezza
type: agent_memory
created_at: 2026-08-24
tags: [slides, vol-02, completezza, images]
---

# VOL-02 slide decks: completezza + figure wiki

Preferenze confermate:
- Brand Ivory Luxe + Pearl Emerald, Navy/Gold, Playfair+Montserrat.
- Identità di capitolo solo in cartelle/`capitolo.json`, non in UI/anteprima.
- Testo solo dal wiki; niente path wiki visibili; niente stock; figure solo da `wiki/books/**/assets`.
- Standard: insegnare (che cos’è / come funziona / esempio / errore), 16–22 slide, `.lead` `.note` `.warn` `.map` `table.dense`.

Fatto:
- `scripts/sync-slide-images.mjs` copia PNG modulo da `source` del manifest (M-FL02 ch.01 → VOL-02/18; M-FL03 ch.01 → VOL-02/45).
- `scripts/inject-slide-images.py` opera su VOL-01 e VOL-02.
- 26 deck schematici (13–25, 39–51) espansi a 18–20 slide.
- Figure wiki usate tutte in cap. 18 e 45.
- Dual output: `slides/` repo + Desktop `slide-capitale-personale/` via `npm run slides:sync`.

Prossimo: VOL-03 se l’utente dice continua.
