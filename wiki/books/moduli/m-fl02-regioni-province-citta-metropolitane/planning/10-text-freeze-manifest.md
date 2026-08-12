---
id: m-fl02-text-freeze-manifest
type: text_freeze_manifest
title: "Text freeze — M-FL02 Regioni, Province e Città metropolitane"
status: frozen
domain: "concorsi pubblici italiani"
book_id: m-fl02-regioni-province-citta-metropolitane
module_code: M-FL02
freeze_date: 2026-08-07
reference_commit: 89538f40fd0b8fb98845f45e24279c712d47055e
updated_at: 2026-08-07T16:00:00+02:00
created_at: 2026-08-07T16:00:00+02:00
review_required: false
canonical: true
tags: ["text-freeze", "m-fl02", "pipeline-step-16"]
---

# Text freeze — M-FL02 Regioni, Province e Città metropolitane

## Esito

Il modulo entra in congelamento testuale il 7 agosto 2026. I capitoli 01-12 sono presenti; la matrice non contiene stati `parziale`, `solo-nominato` o `mancante`; gli errori degli step 13-15 sono chiusi; indice, Bibbia e piano sono coerenti. Il gate `text-freeze` non è ancora implementato e viene chiuso con accettazione manuale motivata dopo questa verifica.

Da questo manifest sono ammesse soltanto correzioni controllate. Una modifica sostanziale a teoria, fonti, casi, quiz, riferimenti o struttura riapre i gate 10-15.

## Riferimento di versione

- Commit di base: `89538f40fd0b8fb98845f45e24279c712d47055e`.
- Stato da congelare: modifiche correnti degli step 14-16, identificate dagli hash seguenti e destinate al successivo commit di pipeline.
- Algoritmo: SHA-256 sul contenuto dei file.
- Cut-off dell'audit specialistico: 7 agosto 2026, secondo le source note consolidate disponibili nel progetto.

## Verifica delle condizioni

| Condizione | Evidenza | Esito |
| --- | --- | --- |
| Capitoli presenti | Dodici target dichiarati e dodici file in `chapters/` | superata |
| Copertura integrale | Matrice completa; nessuno stato didattico bloccante | superata |
| Rinvii | Nessun link interno di conoscenza nel corpo dei capitoli; riferimenti leggibili e tracciabilità nel frontmatter | superata |
| Humanizer | Tutti i dodici step 11 risultano chiusi | superata |
| Errori obbligatori | Step 13-14 chiusi; E13-01/E13-03 risolti | superata |
| Audit specialistico | Step 15 verde, zero blocker e zero warning | superata |
| Indice | Dodici voci e dodici capitoli; piano staff separato | superata |
| Fonti e cut-off | `source_refs` presenti nei capitoli; varianti territoriali e dati mobili qualificati | superata |
| Dati operativi | Nessun box `Dato operativo` rilevato | superata |

## File congelati

| File | Stato | SHA-256 |
| --- | --- | --- |
| `index.md` | text-frozen | `d281abc265f8e7555870e2a70cc21682805d540f00ef5c8a6a3ab263b30dd4ed` |
| `planning/00-piano-editoriale.md` | text-frozen | `2e66c94bd30b7ae9e173ed5907bb7a973a5f7358e8b844bef212d30871034593` |
| `planning/02-matrice-copertura-didattica.md` | complete | `0d57479e51df34f0562cca97506efec3d5324275ff9b88ef6feffd2dac23f758` |
| `planning/09-bibbia-del-modulo.md` | frozen | `e1da739f55ec37df03446d8a1b86e2cbf2d3346f8fd5a064e76c7f95e8d6dcae` |
| `chapters/01-il-sistema-territoriale-multilivello.md` | frozen | `f7b62c3daa74983fc18664e3e5efbe78f392af2a7422987f452f9ce47967f76c` |
| `chapters/02-statuti-organi-organizzazione-regionale.md` | frozen | `a1b4c3705c182fe7b5c9734fb4674290563449729b0180e9225e7821af8614e8` |
| `chapters/03-funzioni-regionali-rapporti-stato-enti-locali.md` | frozen | `62dbc01a1e23c21b4ce4be741c6d639e8ef8c02810f02be871e8d036cbe120af` |
| `chapters/04-procedimenti-atti-organizzazione-amministrativa-regionale.md` | frozen | `1cfa3be88e96befb256f10f8a43a7194b97db52c62839c484e34e0bd991712ce` |
| `chapters/05-programmazione-bilancio-controlli-regionali.md` | frozen | `8a09dda252bb767e46f67784fad427e5c79f541e4f2449472f8ba43b8162c377` |
| `chapters/06-tecnica-legislativa-air-vir-drafting.md` | frozen | `fe89803292483eed63f70d439b14e1675c035b8d73068e053920809f2a6a5d45` |
| `chapters/07-politiche-coesione-fondi-ue.md` | frozen | `2926d01866e233567a8cc45571b7c6584a2f4adf8891169915a2e667c3639220` |
| `chapters/08-pnrr-territoriale-regis-dnsh-controlli.md` | frozen | `0f1156b0b6095aa94322ba80ada6bfdc8ab6d4b3f17377bcf5d4893336e11e00` |
| `chapters/09-province-citta-metropolitane-legge-56-2014.md` | frozen | `20857b383284e654b84348ce54f5117eb1b21dae6d3a8b9e09a0b440ad415863` |
| `chapters/10-viabilita-edilizia-scolastica-territorio-espropri.md` | frozen | `103b05a5dc0d46514b3ee39cee480e4ddd392e324be3225e4da1870db9d26688` |
| `chapters/11-contratti-servizi-pubblici-locali-societa-partecipate.md` | frozen | `e008343623524c484fe1d3ded9b8a6c171a4e3d11980bd2af7cedc62a667655a` |
| `chapters/12-laboratorio-profili-regionali-area-vasta.md` | frozen | `e054c2720b739839c487c60a748541b3e0f9faa9c1c19c8358594f424c24f633` |

## Regola successiva al freeze

Ogni modifica sostanziale successiva deve essere tracciata e sottoposta nuovamente a copertura, Humanizer, revisione trasversale e audit specialistico prima di un nuovo freeze.
