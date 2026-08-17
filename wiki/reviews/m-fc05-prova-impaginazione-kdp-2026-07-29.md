---
id: review-m-fc05-prova-impaginazione-kdp-2026-07-29
type: layout_proof_review
title: "VOL-05, M-FC05 - prova interna di impaginazione paperback KDP"
status: completed
domain: concorsi pubblici italiani
topics: ["impaginazione editoriale", "accessibilità", "authority", "regolazione"]
entities: ["Book Studio", "KDP"]
book_refs: ["vol-05-authority-regolazione", "m-fc05-authority-indipendenti"]
confidence: 0.94
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: true
canonical: false
tags: ["vol-05", "m-fc05", "kdp", "layout", "prova-impaginazione"]
---

# VOL-05, M-FC05 - prova interna di impaginazione paperback KDP

## Oggetto e metodo

La prova è stata eseguita sulla preview Book Studio del libro `volumi/vol-05`, in formato paperback 6,69 × 9,61 pollici. Il controllo automatico ha esaminato tutte le pagine generate e la verifica visiva ha campionato apertura, capitolo con figura, capitolo con tabella ed ultima pagina.

## Risultati misurati

| Controllo | Esito |
| --- | --- |
| Pagine della preview finale | 167 |
| Formato pagina | 642 × 923 px; rapporto 0,696, coerente con 6,69 ÷ 9,61 |
| Corpo testo | Garamond, 14,67 px |
| Titoli | Arial, 26,67 px |
| Overflow oltre il piè di pagina | 0 pagine |
| Immagini non caricate | 0 |
| Immagini fuori dai limiti della pagina | 0 |
| Campioni visivi | 4, inclusa l'ultima pagina del Capitolo 15 |

Le evidenze tecniche sono conservate in `artifacts/m-fc05-kdp-layout-report.json` e in `artifacts/m-fc05-kdp-layout/`.

## Rilievo e correzione applicata

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| L01 | Preview del volume, pagine finali | Struttura editoriale | Media | Il file di lavorazione `00-piano-editoriale.md` veniva aggregato alla preview destinata al lettore. | Conservare il piano nel modulo ma escludere dall'aggregazione dei volumi i capitoli con `outline_section: 0`; preservare correttamente il valore numerico zero nel parser. | Applicata e verificata |

## Giudizio

La prova interna di impaginazione è **superata**. La preview contiene il solo front matter previsto all'inizio del volume, l'apertura di modulo e i quindici capitoli destinati al lettore; il piano editoriale interno non compare più. Non risultano errori gravi aperti di layout. Resta esclusivamente la firma editoriale-normativa umana.
