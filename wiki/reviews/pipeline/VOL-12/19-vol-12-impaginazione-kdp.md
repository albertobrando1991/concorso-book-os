---
id: review-vol-12-step-19-kdp-layout
type: review
title: Impaginazione KDP - VOL-12
status: complete
domain: concorsi pubblici italiani
topics:
  - impaginazione KDP
  - Book Studio
entities:
  - Amazon KDP
source_refs: []
book_refs:
  - vol-12-carriere-speciali-premium
confidence: 1
updated_at: 2026-08-14T16:15:00+02:00
created_at: 2026-08-14T16:15:00+02:00
review_required: false
canonical: false
tags:
  - pipeline-step-19
  - kdp-layout
  - vol-12
issue_type: kdp_layout
severity: none
affected_pages:
  - books/volumi/vol-12-carriere-speciali-premium/index.md
---

# Impaginazione KDP — VOL-12

## Esito

VOL-12 è stato renderizzato integralmente nel Book Studio con il master paperback KDP 6,69 × 9,61 pollici, bianco e nero, senza bleed e a colonna singola. La verifica automatizzata ha prodotto **459 pagine** con numerazione progressiva continua.

Esito complessivo: **conforme per lo step 19**. Il PDF candidato e l'audit visivo pagina per pagina appartengono allo step 20.

## Evidenze misurate

| Controllo | Valore | Esito |
| --- | ---: | --- |
| Pagine renderizzate | 459 | Conforme |
| Numerazione progressiva | 1–459 | Conforme |
| Sezioni di front matter | 6 | Conforme |
| Aperture di modulo | 4 | Conforme |
| Capitoli | 32 | Conforme |
| Nuclei identificati nel testo | 162 | Conforme |
| Righe-nucleo nell'indice | 162 | Conforme |
| Intestazioni `▣ Verifica` con stile dedicato | 46 | Conforme |
| Pagine con overflow oltre soglia | 0 | Conforme |
| Pagine con sovrapposizioni | 0 | Conforme |

L'indice analitico conserva la chiave tecnica `path + nucleusId`, mostra la numerazione globale dei nuclei nel volume composito e usa le pagine misurate dal paginator.

## Master applicato

- pagina 6,69 × 9,61 pollici;
- margini speculari con gutter interno di 23 mm, margine esterno di 13 mm e margini superiore/inferiore di 18 mm;
- corpo Garamond 11 pt con interlinea 1,18;
- titoli Arial Bold sulla scala 20/14/12 pt;
- tabelle, quiz, callout e strumenti in Arial 9,5–10 pt;
- blocchi `▣ Verifica` distinti e leggibili in scala di grigi;
- nessun overflow strutturale o collisione con il footer rilevato.

## Evidenze tecniche

- `artifacts/vol-12-step-19-layout-report.json`;
- `artifacts/vol-12-step-19-vol-12.png`;
- test mirato `tests/book-preview-index-nucleus-regression.test.ts`;
- suite correlata: 18 test superati in `book-preview`, `book-studio-index-pages` e regressione indice.

## Anomalia corretta

Il primo rendering esponeva 159 nuclei nell'indice a fronte di 162 nel testo. Il filtro lessicale ometteva i nuclei canonici il cui titolo iniziava con «Checklist». La composizione ora fa prevalere la presenza del `Nucleo ID`; le checklist prive di ID restano escluse. Il secondo rendering espone 162/162 nuclei.

## Passaggio successivo

Lo step 20 genera il PDF candidato e verifica tutte le 459 pagine per vedove, orfani, spazi bianchi, tabelle, box, immagini, equilibrio e coerenza recto/verso.
