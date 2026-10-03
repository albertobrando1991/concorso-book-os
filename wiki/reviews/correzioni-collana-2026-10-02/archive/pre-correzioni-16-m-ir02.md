---
id: text-freeze-manifest-vol-06-m-ir02-step-16
type: text_freeze_manifest
title: "Manifest di text freeze - VOL-06 M-IR02 Università e AFAM"
status: frozen
domain: "istruzione superiore italiana e concorsi pubblici"
topics: ["università", "AFAM", "pipeline", "text freeze"]
entities: ["Ministero dell'Università e della Ricerca", "ANVUR"]
source_refs: ["sources/fonti-ufficiali-m-ir02-universita-afam-2026-07-24", "sources/bandi-rappresentativi-m-ir02-universita-afam-2025-2026"]
book_refs: ["m-ir02-universita-afam", "vol-06-scuola-universita-ricerca-cultura"]
confidence: 0.91
updated_at: 2026-08-22
created_at: 2026-08-22
review_required: false
canonical: false
tags: ["text-freeze", "pipeline-step-16", "module-code-m-ir02"]
---

# Manifest di text freeze - VOL-06 M-IR02 Università e AFAM

## Esito del controllo

Il modulo entra in text freeze il 22 agosto 2026. I dodici capitoli sono presenti e in Formato 2; la matrice non contiene stati parziali, solo nominati, rinviati o mancanti; i gate di copertura, densità, lint, citazioni, Humanizer e revisione editoriale risultano completati. L'audit specialistico ha verificato i richiami normativi puntuali e il dato mobile sul Bando PRIN 2026. Non restano errori gravi o medi, né rinvii a una futura revisione umana.

Riferimento Git di base: `fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a`. Gli hash sotto identificano esattamente i file del working tree congelati, incluse le modifiche editoriali non ancora committate.

## Condizioni verificate

| Condizione | Esito | Evidenza |
| --- | --- | --- |
| Capitoli presenti | superato | capitoli 01-12 nel modulo M-IR02 |
| Copertura | superato | matrice con dodici righe complete e gate 08-10 superati |
| Rinvii | superato | rinvii verificabili e distinzione esplicita tra fonte nazionale e atto locale |
| Humanizer | superato | step 11 completato per tutti i capitoli |
| Revisione editoriale | superato | step 12-14 completati; nessun errore obbligatorio aperto |
| Audit specialistico | superato | step 15; fonti ufficiali Normattiva e MUR verificate il 22 agosto 2026 |
| Metadati | superato | `status: final`, `draft_stage: text_frozen`, `review_required: false` |
| Indice e cut-off | superato | indice, matrice, Bibbia del modulo e fonti dichiarate |

## Elenco dei file congelati

| File | Stato | Data | SHA-256 |
| --- | --- | --- | --- |
| `wiki/books/moduli/m-ir02-universita-afam/index.md` | congelato | 2026-08-22 | `53d66f809c2b07d6a2366e66141118145fabe1c4a12cf50ec5694e3aa9029d41` |
| `wiki/books/moduli/m-ir02-universita-afam/planning/02-matrice-copertura-didattica.md` | congelato | 2026-08-22 | `42c6c5296b0a897f2887241a383f5aacf91a3e2ddca9da73c63590067e9be8e7` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/01-sistema-universitario-afam.md` | congelato | 2026-08-22 | `027dbb3955bb421c7456e7e86e33ee2eac12f4cd5d8a38ba4dfaf978a9cb426c` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/02-autonomia-statuti-organi.md` | congelato | 2026-08-22 | `b2f2999c3e5a119789769a26015e376d66175de7eb54fa03332966141f25b30d` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/03-ordinamenti-didattici-qualita.md` | congelato | 2026-08-22 | `54fd9da78b900b6a6ad6b817a81f17363c6078b0802aacad1a3c225ea8158df7` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/04-carriere-studenti-diritto-studio.md` | congelato | 2026-08-22 | `b9afcab845f9c745b88fc2293126a9cc55ff570109b86dc445388adf6abda007` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/05-atti-protocollo-accesso-digitale.md` | congelato | 2026-08-22 | `252435dd68534d6bd36f9a86e6a0e9427bfdfe8675fab713eb6467f813a3d777` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/06-bilancio-ateneo.md` | congelato | 2026-08-22 | `af897e34b08c9ddb9c2a1aa67b2c20444f440bff861ee2e3759f09b0ea7644f5` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/07-ricerca-grant-management.md` | congelato | 2026-08-22 | `53038c1a9bdd1ecac2659b7a5b9486376247c66958e35e5e92f13fa93d8ecc70` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/08-prin-horizon-pnrr-audit.md` | congelato | 2026-08-22 | `808c17a502c0412ef7148dd11d253fe52c2ba33e07ad38ee40ea1a7455c6d02d` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/09-biblioteche-cataloghi-open-access.md` | congelato | 2026-08-22 | `fb3fe850ad98da27e59407a353fd7e521178040333add0b99a3ce93661efd135` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/10-orientamento-placement-terza-missione.md` | congelato | 2026-08-22 | `e1083dd851a254c61a5ea9d7ab8710f2212f3e7b17f459ef576eb5d9c0aea535` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/11-afam-ordinamento-amministrazione.md` | congelato | 2026-08-22 | `ec2ede48bec3de62284223f2c838b63e70dbc1c0978c913ceaacd1ae067a48a2` |
| `wiki/books/moduli/m-ir02-universita-afam/chapters/12-laboratorio-quattro-profili.md` | congelato | 2026-08-22 | `d3abf0a7b16c349f7dc9235d0bc9a0f570dd77dbaa58924b7cfce5f4bed66564` |
| `wiki/reviews/pipeline/VOL-06/13-moduli-m-ir02-universita-afam.md` | congelato | 2026-08-22 | `1d1d5d8f3f2670c301537e36bc9a7553d49c6e50fe49ca632797b645f97cd3ff` |
| `wiki/reviews/pipeline/VOL-06/14-moduli-m-ir02-universita-afam.md` | congelato | 2026-08-22 | `f1d355bd7e3138d654cad3897d6965a1be4851b420807a243026994764c7a251` |
| `wiki/reviews/pipeline/VOL-06/15-moduli-m-ir02-universita-afam.md` | congelato | 2026-08-22 | `89d4e1935d98bfc61761d1bb52b7e1afce5fbe520c572f117f87a25d263dc462` |

## Regola di modifica dopo il freeze

Sono ammesse solo correzioni controllate di refusi, aggiornamenti di fonte o interventi di impaginazione. Ogni modifica sostanziale a concetti, esempi, casi, esercizi, rinvii o fonti riapre gli step 10-15 sul passaggio interessato e richiede l'aggiornamento degli hash.
