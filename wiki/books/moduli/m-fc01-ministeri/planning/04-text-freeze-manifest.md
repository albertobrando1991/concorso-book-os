---
id: m-fc01-text-freeze-manifest
type: text_freeze_manifest
title: "Text freeze — M-FC01 Ministeri, PCM e Avvocatura dello Stato"
status: frozen
domain: "concorsi pubblici italiani"
book_id: m-fc01-ministeri
volume_code: VOL-03
module_code: M-FC01
freeze_date: 2026-08-22
reference_commit: fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a
updated_at: 2026-08-22T13:30:00+02:00
created_at: 2026-08-22T13:30:00+02:00
review_required: false
canonical: true
tags: ["text-freeze", "vol-03", "m-fc01", "pipeline-step-16"]
---

# Text freeze — M-FC01 Ministeri, PCM e Avvocatura dello Stato

## Esito

Il modulo entra in congelamento testuale il 22 agosto 2026. I quindici capitoli sono presenti; la matrice non contiene stati parziale, solo-nominato o mancante; gli errori obbligatori degli step 13-15 sono chiusi; indice editoriale, Bibbia, fonti e apparati risultano coerenti. Il gate `text-freeze`, non ancora automatizzato, è stato verificato manualmente prima dell'accettazione motivata.

Da questo manifest sono ammesse soltanto correzioni controllate. Ogni modifica sostanziale a teoria, fonti, casi, quiz, riferimenti o struttura riapre i gate 10-15.

## Riferimento di versione

- Commit di base: `fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a`.
- Stato congelato: modifiche correnti degli step 08-16, identificate dagli hash seguenti e destinate al successivo commit di pipeline.
- Algoritmo: SHA-256 sul contenuto dei file.
- Cut-off dell'audit specialistico: 22 agosto 2026.

## Verifica delle condizioni

| Condizione | Evidenza | Esito |
|---|---|---|
| Capitoli presenti | Quindici target e quindici file; un solo H1 per capitolo | superata |
| Copertura integrale | Tutti i nuclei della matrice hanno stato completo | superata |
| Rinvii | Slug, rinvii interni e riferimenti alle fonti controllati dai gate 09-12 | superata |
| Humanizer | Step 11 completato per tutti i capitoli; tono e strutture ripetitive ricontrollati nello step 13 | superata |
| Errori obbligatori | Step 14 chiuso; step 15 superato senza blocker o warning | superata |
| Audit specialistico | Ordinamento, CCNL, Avvocatura, PIAO, contabilità, contratti e digitale consolidati | superata |
| Indice | Piano editoriale, indice del modulo e sequenza dei quindici capitoli coerenti | superata |
| Fonti e cut-off | Source refs presenti; cut-off specialistico 22-08-2026 dichiarato | superata |
| Dati mobili | Nessun box `Dato operativo`; variabili di bando trattate come dati da verificare sulla procedura | superata |

## File congelati

| File | Stato | SHA-256 |
|---|---|---|
| `index.md` | frozen | `290678dc6770c2291bfe518c0ecd42e89f4f5a66b04c9f9815ae352593061748` |
| `planning/00-piano-editoriale.md` | frozen | `296e9157ec15d6d183021a6f917604e4597722a2357c7cafd07daa158cbba714` |
| `planning/02-matrice-copertura-didattica.md` | frozen | `6dd448534242422a12836f724739933fc3148227800555d697522d12a5610c15` |
| `planning/03-bibbia-del-modulo.md` | frozen | `290cdfc5302bcf73a15841ea3802958b4fd2d869b851ba6cff8f0ad6704a5153` |
| `chapters/01-lavorare-ministeri-funzioni-centrali.md` | frozen | `c934c085bc0620b87010d3cff4435ed6e182389323c012cf6391d78dbd9e0aa6` |
| `chapters/02-anatomia-bando-ministeriale-ripam.md` | frozen | `32f4fc591617b2abb6f9926a5aa4de894b541d45599677dc9fa2b66b41b3bf3b` |
| `chapters/03-profili-professionali-ccnl-mansioni.md` | frozen | `8cd049dcab554dfefc33f9015af95c67b18640476524816af74a96da50267589` |
| `chapters/04-governo-ministeri-amministrazione-centrale.md` | frozen | `d8ae9aa39a65fd6ecfe1d376cafabba59f98fd9c809fa7148ffaa9e2da9d573b` |
| `chapters/05-presidenza-consiglio-ministri.md` | frozen | `e0cb28a2063e989904a38ecebb816d04630e697a3520be827444c0db57fb2b2c` |
| `chapters/06-organizzazione-interna-ministeri.md` | frozen | `bb016ca6a61cc2b744ff8e024bc8e64fa6c4e851c392d113a641782d1182dc95` |
| `chapters/07-avvocatura-stato.md` | frozen | `9ea7e5f259e80b1ab417419da560d723c4c1be3011af53c4f031a8b318f35a9d` |
| `chapters/08-piao-performance-anticorruzione-valore-pubblico.md` | frozen | `f7e2a207b04a5aacc88b19db0cac418a80320c620d2890334e1bdfdf4d643511` |
| `chapters/09-contabilita-stato-bilancio-ministeriale.md` | frozen | `cba90db2d9f48d134b237f00f0000cfd542ea86df22c86b58fc472e6512eba7f` |
| `chapters/10-contratti-pubblici-pnrr-amministrazione-digitale.md` | frozen | `11acae6c16a002929ab44297bf81829a01ec1263fbda7541c897e6dc1104d481` |
| `chapters/11-casi-pratici-ministeriali.md` | frozen | `66989fdd6c143681b08ad434e2802ef22dc22b9ae8d9851e218ce43458b663ae` |
| `chapters/12-quesiti-situazionali-codice-comportamento.md` | frozen | `9ad75ed0658d38fd86625ecbcbb0b5a405f3c1fd19b3fdc7a0259bec7d2929a1` |
| `chapters/13-matrice-materie-piano-30-60-90.md` | frozen | `586898fba60a53a5367e396542152c093bb9962c8962d08776ad2f7ccdd5c264` |
| `chapters/14-simulazione-finale-diario-errori.md` | frozen | `c7b2ffa256cdff8af663d3ce15c437ced67e20ba5da4af2cfbc71120f396e2ff` |
| `chapters/15-appendici-operative.md` | frozen | `ba6716f1e0a55664f05301b99c36a57e74783fc02f86a1177e39e60946957eb4` |

## Regola successiva al freeze

Ogni modifica sostanziale successiva deve essere tracciata e sottoposta nuovamente a copertura, Humanizer, revisione trasversale e audit specialistico prima di un nuovo freeze.
