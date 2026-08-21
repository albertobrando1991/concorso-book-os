---
id: review-vol-01-pdf-recovery-2026-08-21
type: review
title: VOL-01 — Recupero del candidato PDF e preflight tecnico
status: candidate_technical_preflight_passed_visual_verification_blocked
domain: editorial
book_refs:
  - il-metodo-bando
confidence: high
created_at: 2026-08-21
updated_at: 2026-08-21
review_required: true
canonical: false
tags:
  - vol-01
  - pdf
  - kdp
  - preflight
---

# VOL-01 — Recupero del candidato PDF e preflight tecnico

## Scopo e perimetro

Il controllo riguarda l'export cartaceo KDP di `Il Metodo BANDO`. Non sostituisce la revisione editoriale, normativa o umana del libro. Il PDF legacy in `output/pdf/vol-01-il-metodo-bando-layout-corretto.pdf` è stato conservato e non modificato.

## Difetto riscontrato nel PDF legacy

Il file legacy, pur contenendo il volume completo in 593 pagine, termina con quattro pagine dell'introduzione dopo l'Appendice F (pagine 590-593). La sequenza non è pubblicabile perché interrompe la chiusura del volume e duplica materiale già presente nelle prime pagine.

## Verifica del Book Studio corrente

- Libro controllato: `il-metodo-bando`.
- Render stabilizzato: 593 pagine.
- Sezioni nel Book Studio: 6 prime pagine, 32 sezioni cartacee, nessun modulo del Ricettario nel corpo del libro.
- Diagnostica layout: nessun overflow e nessuna sovrapposizione rilevati dallo script.
- Contenuto delle pagine 590-593: Appendice F — Matrice materie/profili; non introduzione.

Il difetto appartiene quindi all'export legacy, non al manoscritto o alla sequenza finale del renderer corrente.

## Candidato rigenerato

- Percorso: `delivery/VOL-01/candidate/vol-01-interior-kdp.pdf`.
- Esportazione: 2026-08-21, Book Studio locale, libro `il-metodo-bando`.
- Pagine attese/rilevate: 593/593.
- Dimensione: 12.178.323 byte.
- SHA-256: `0823749737804E58369C15ABB2046112A047879E1A38980BE9A5A078730AB553`.

## Esiti del preflight tecnico

| Controllo | Esito | Evidenza |
| --- | --- | --- |
| Paginazione stabilizzata | Superato | 593 pagine attese e 593 rilevate dall'export. |
| Sequenza finale | Superato | Dopo l'Appendice F non compare l'introduzione; le pagine 590-593 proseguono e chiudono l'Appendice F. |
| Font | Superato | Arial Bold, Garamond, Arial Black, Arial e Consolas risultano incorporati e subset. |
| Sicurezza/form | Superato | Nessuna cifratura, JavaScript o modulo PDF. |
| Immagini | Superato | Export con immagini mancanti pari a zero. |
| Formato | Superato | MediaBox, CropBox, TrimBox e BleedBox normalizzati a 481,68 × 691,92 pt: 6,69 × 9,61 in senza bleed. Il contenuto è stato scalato uniformemente di 0,999502. |
| Metadata | Superato | Titolo `Il Metodo BANDO`, autore `Capitale Personale`, soggetto e parole chiave coerenti con il volume. |
| Ispezione visiva PNG | Bloccata | Le pagine 1, 297 e 593 sono state renderizzate, ma l'helper visivo locale non le apre per l'errore Windows `CreateProcessWithLogonW failed: 2`. Nessuna dichiarazione di resa visiva è formulata in assenza di ispezione. |

## Criticità residue e decisione

1. **Importante — preflight KDP esterno:** caricare il candidato nel Print Previewer del portale KDP e confermare margini, font e nessun avviso di impaginazione. Kindle Previewer non verifica gli interni PDF cartacei.
2. **Importante — ispezione visiva:** verificare i PNG campione non appena il visualizzatore locale torna disponibile, oppure nel Print Previewer KDP.
3. **Critico per la pubblicazione, esterno a questo recupero:** l'indice del libro conserva `status: draft` e `review_required: true`; questo candidato non sostituisce la revisione editoriale/normativa e il sign-off umano pre-pubblicazione.

## Giudizio

Il candidato PDF corregge il difetto oggettivo del legacy, ha trim esatto e metadati editoriali, e supera il preflight tecnico automatico. È **utilizzabile per il successivo proof KDP**, ma non è dichiarato pronto alla pubblicazione finché non siano eseguiti il controllo visivo/Print Previewer e i gate editoriali e umani ancora aperti.
