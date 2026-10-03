---
id: m-fl04-text-freeze-manifest
type: text_freeze_manifest
title: "Text freeze — M-FL04 Polizia locale"
status: frozen
domain: "concorsi pubblici italiani"
book_id: m-fl04-polizia-locale
module_code: M-FL04
freeze_date: 2026-08-08
reference_commit: 0ddef2c6d295cd77431cf76d2d63e6a5d1f25712
updated_at: 2026-08-08T22:20:00+02:00
created_at: 2026-08-08T22:20:00+02:00
review_required: false
canonical: true
tags: ["text-freeze", "m-fl04", "pipeline-step-16"]
---

# Text freeze — M-FL04 Polizia locale

## Esito

Il modulo entra in congelamento testuale l'8 agosto 2026. Sono presenti quindici capitoli e 75 nuclei completi; gli step 11, 13, 14 e 15 sono chiusi; indice, Bibbia e matrice sono coerenti. Da questo manifest sono ammesse soltanto correzioni controllate. Ogni modifica sostanziale riapre i gate 10-15.

## Riferimento di versione

- Commit di base: `0ddef2c6d295cd77431cf76d2d63e6a5d1f25712`.
- Stato da congelare: modifiche correnti degli step 13-16, identificate dagli hash seguenti.
- Algoritmo: SHA-256 sul contenuto dei file.
- Cut-off dell'audit specialistico: 8 agosto 2026.

## Verifica delle condizioni

| Condizione | Evidenza | Esito |
| --- | --- | --- |
| Capitoli presenti | Quindici target e quindici file | superata |
| Copertura integrale | 75 nuclei completi; nessuno stato bloccante | superata |
| Rinvii | Nessuna dipendenza interna nel corpo; riferimenti leggibili e frontmatter tracciabile | superata |
| Humanizer | Tutti i quindici step 11 chiusi | superata |
| Errori obbligatori | Step 13-14 chiusi; E13-01/E13-02 risolti | superata |
| Audit specialistico | Step 15 verde, zero warning e zero esiti aperti | superata |
| Indice | Quindici voci e quindici capitoli | superata |
| Fonti e cut-off | Normattiva e ARAN; cut-off dichiarato | superata |
| Dati operativi | Nessun box rilevato | superata |

## File congelati

| File | Stato | SHA-256 |
| --- | --- | --- |
| `index.md` | frozen | `bff4cc5d1a4d9fc8b2b566170f53cacd4fa805d630ce51e01b3967a945b94390` |
| `planning/00-piano-editoriale.md` | frozen | `a571292618142f453bcf374a41cc3e7a7e7381d0f763aa54dd25aab8a0e9cccb` |
| `planning/02-matrice-copertura-didattica.md` | frozen | `d5bc73880ac681bc2241fc2d573cbd7108132e99b4c3cb4a5bff32a74652c2ad` |
| `planning/09-bibbia-del-modulo.md` | frozen | `916710441fc08edef0e3b212ffe272d855d97c278085e76a0bcdec6daf9b43d9` |
| `chapters/01-diventare-agente-ufficiale-polizia-locale.md` | frozen | `a554a044c7ad42a5e3f2a16d495890c16bfc515cd218424fe70662051940d2a5` |
| `chapters/02-ordinamento-nazionale-regionale-polizia-locale.md` | frozen | `54f4fde6e21c3e937de623dece8ecb046fbc8eaad2a4581e17e22cbab9f93ed8` |
| `chapters/03-qualifiche-poteri-dipendenze-organizzazione-servizio.md` | frozen | `8f880b8090068e490138ca5d862ae9fa1d1245f1c92ba1d806726a721d58dcf5` |
| `chapters/04-servizi-polizia-stradale.md` | frozen | `1918d618a46903d7d02cd4bd2905ed1e4e8adfe5c9a782e62731c4b96a0086f0` |
| `chapters/05-accertamento-contestazione-notificazione-ricorsi-codice-strada.md` | frozen | `ad4c0bb00299a7fff0ce8cddd2c34f4adf1e3e562f831b3e1667190702da4d48` |
| `chapters/06-procedimento-sanzionatorio-amministrativo-applicato.md` | frozen | `e4da6ce66189a7a0a26a86cbb5a34f97970d9f7b504e05c2ee9f7b33bb1061b4` |
| `chapters/07-polizia-giudiziaria-atti-essenziali.md` | frozen | `e5d72096a87bee0bdc5227e3f278bec53e38ad9c68ab262a9ec5afb8c9ef0db3` |
| `chapters/08-tulps-pubblica-sicurezza-immigrazione.md` | frozen | `261621d77941c98a38ad588e40ce45b9f58d0f48ddda1c95c1b7a6e4ae4f0a6e` |
| `chapters/09-sicurezza-urbana-ordinanze-coordinamento.md` | frozen | `e8a5b4a94b8f6ecb2fee148c5aaf2265fceef6ca137cf2047f52defbd901164e` |
| `chapters/10-commercio-pubblici-esercizi-suap.md` | frozen | `0539979eefd2d5b82e21ad27485e884f4afc09b4579257f0ed8dd155818dcf4a` |
| `chapters/11-vigilanza-edilizia-procedimenti-repressivi.md` | frozen | `af47dc9c08da4ecfb0a266f54e589f535790a06f6c7f41465f8a9522a01dabba` |
| `chapters/12-ambiente-rifiuti-rumore-tutela-locale.md` | frozen | `43db1d2549e438d4fb03792f55af256a595d37a4037822399a706258610d93c7` |
| `chapters/13-sinistri-rilievi-gestione-prova.md` | frozen | `f578887a415a48760d79a5db2bcdd247283d7b6d58f8400fd555d08a82435ffb` |
| `chapters/14-ufficiale-pl-comando-contenzioso-emergenze.md` | frozen | `7560c79934c909db65ee694cc858977a2c5b0c6b9ed87c49955dd44ce59fbb97` |
| `chapters/15-laboratorio-atti-verbali-polizia-locale.md` | frozen | `9beee0036d8932915acdb345abf1dc3482bc0006155bdf0b7dcb1f046eeb0878` |

## Regola successiva al freeze

Ogni modifica sostanziale successiva deve essere tracciata e sottoposta nuovamente a copertura, Humanizer, revisione trasversale e audit specialistico prima di un nuovo freeze.
