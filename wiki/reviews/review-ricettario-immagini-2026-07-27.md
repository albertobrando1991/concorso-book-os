---
id: review-ricettario-immagini-2026-07-27
type: review
title: Revisione professionale delle immagini del Ricettario digitale
status: completed
domain: editoriale-visivo
topics:
  - ricettario-digitale
  - immagini-editoriali
  - book-studio
entities: []
source_refs: []
book_refs:
  - il-metodo-bando
confidence: high
updated_at: 2026-07-27
created_at: 2026-07-27
review_required: false
canonical: false
tags:
  - canvas-design
  - image-audit
  - kdp
---

# Revisione professionale delle immagini del Ricettario digitale

## Esito

Il gate visivo delle immagini del Ricettario è superato. Sono state controllate tutte le 161 immagini dei moduli R1–R23, sia come file sia nella paginazione reale del Book Studio.

## Interventi

- Adottata la filosofia visiva [[books/il-metodo-bando/filosofia-visiva-precisione-civica]].
- Verificati i 63 master SVG di R1–R9: nessun testo fuori area sicura, nessuna collisione testo-testo e nessuna voce a contatto con il proprio rettangolo.
- Sostituite le 98 tavole raster di R10–R23 con immagini deterministiche a griglia controllata.
- Eliminati microsegni pseudo-tipografici, moduli casuali, rettangoli disallineati e sovrapposizioni non verificabili.
- Conservati tutti i nomi file e tutti i riferimenti Markdown esistenti.
- Uniformati fondo avorio, palette blu notte/bordeaux/verde/teal/oro, spessori, margini, titoli e gerarchia.
- Ridotto il peso complessivo delle immagini R10–R23 a circa 5 MB, migliorando il caricamento senza ridurre le dimensioni native di 1536 × 1024 px.

## Verifiche

| Controllo | Esito |
|---|---:|
| Moduli verificati | 23/23 |
| PNG presenti | 161/161 |
| Immagini per modulo | 7/7 |
| Master SVG R1–R9 | 63/63 |
| Collisioni geometriche SVG | 0 |
| Immagini caricate nel Book Studio | 161/161 |
| Immagini fuori pagina o sul piè di pagina | 0 |
| Pagine con overflow nel Ricettario | 0 |

## Strumenti di controllo

- `scripts/audit-ricettario-images.cjs`
- `scripts/generate-ricettario-r10-r23-assets.cjs`
- `scripts/verify-ricettario-images-in-book-studio.mjs`
- `scripts/verify-ricettario-layout.mjs`

Il presente report riguarda il gate delle immagini e della loro resa in pagina. Non sostituisce gli altri gate editoriali, normativi o di copertura didattica.
