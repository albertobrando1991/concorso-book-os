---
id: review-vol-07-step-19-kdp-layout
type: review
title: Impaginazione KDP - VOL-07
status: complete
domain: concorsi pubblici italiani
topics:
  - impaginazione KDP
  - Book Studio
entities:
  - Amazon KDP
source_refs: []
book_refs:
  - vol-07-sanita-amministrativa-professioni-sanitarie
confidence: 1
updated_at: 2026-08-04T16:24:00+02:00
created_at: 2026-08-04T16:24:00+02:00
review_required: false
canonical: false
tags:
  - pipeline-step-19
  - kdp-layout
  - vol-07
issue_type: kdp_layout
severity: none
affected_pages:
  - books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md
---

# Impaginazione KDP — VOL-07

## Esito

Il volume composito VOL-07 è stato renderizzato integralmente nel Book Studio con il master paperback KDP 6,69 × 9,61 pollici, bianco e nero, senza bleed e a colonna singola. La verifica automatica ha prodotto **381 pagine** con numerazione progressiva continua.

Esito complessivo: **conforme per lo step 19**. Lo step non genera il PDF e non sostituisce l'audit visivo pagina per pagina previsto dallo step 20.

## Evidenze misurate

La struttura verificata comprende 6 sezioni di front matter, 4 aperture di modulo, 25 capitoli e 7 nuclei, tutti presenti anche nell'indice analitico.

| Controllo | Valore | Esito |
| --- | ---: | --- |
| Pagine renderizzate | 381 | Conforme |
| Numerazione progressiva | 1–381 | Conforme |
| Sezioni di front matter | 6 | Conforme |
| Aperture di modulo | 4 | Conforme |
| Capitoli | 25 | Conforme |
| Nuclei identificati nel testo | 7 | Conforme |
| Righe-nucleo nell'indice | 7 | Conforme |
| Intestazioni `▣ Verifica` con stile dedicato | 1 | Conforme |
| Pagine con overflow oltre soglia | 0 | Conforme |
| Pagine con sovrapposizioni | 0 | Conforme |

L'indice analitico conserva la chiave tecnica `path + nucleusId`, mostra la numerazione globale dei nuclei nel volume composito e usa le pagine effettivamente misurate dal paginator. Il capitolo pilota M-SA02 mantiene la numerazione locale `5.1–5.7` nello standalone e la espone come `9.1–9.7` nel volume.

## Master applicato

- pagina 6,69 × 9,61 pollici;
- margini speculari con gutter interno di 23 mm, margine esterno di 13 mm e margini superiore/inferiore di 18 mm;
- corpo Garamond 11 pt con interlinea 1,18;
- titoli Arial Bold sulla scala 20/14/12 pt;
- tabelle, quiz, callout e strumenti in Arial 9,5–10 pt;
- blocco `▣ Verifica` distinto con bordo scuro e fondo neutro leggibile in scala di grigi;
- nessun overflow strutturale o collisione con il footer rilevato.

## Comando di verifica

Il Book Studio è stato avviato localmente e verificato con:

```powershell
$env:BOOK_STUDIO_URL = 'http://127.0.0.1:3010'
$env:BOOK_STUDIO_BOOK_IDS = 'volumi/vol-07'
$env:BOOK_STUDIO_ARTIFACT_PREFIX = 'vol-07-step-19'
$env:BOOK_STUDIO_EXPECTED_COUNTS = '{"frontMatter":6,"moduleOpenings":4,"chapters":25,"nuclei":7}'
node scripts/verify-book-studio-layout.mjs
```

Evidenze diagnostiche:

- `artifacts/vol-07-step-19-layout-report.json`;
- `artifacts/vol-07-step-19-vol-07.png`.

## Anomalie corrette

- preservata l'identità tecnica dei nuclei nel parser Markdown;
- rinumerati i nuclei rispetto al capitolo globale del volume;
- aggiunte le righe-nucleo all'indice analitico composito;
- riconciliati capitoli e nuclei con la paginazione DOM misurata;
- portato il gutter interno del master condiviso a 23 mm;
- introdotta la resa semantica in bianco e nero per `▣ Verifica`;
- reso configurabile il verifier Playwright con conteggi strutturali bloccanti.

## Limiti e passaggio successivo

Nessun PDF è stato generato nello step 19. Lo step 20 deve svolgere l'audit visivo dettagliato di tutte le 381 pagine, con controllo di vedove, orfani, spazi bianchi, tabelle, box, immagini, equilibrio della pagina e coerenza recto/verso.
