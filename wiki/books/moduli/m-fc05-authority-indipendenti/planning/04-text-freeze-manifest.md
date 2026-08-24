---
id: m-fc05-text-freeze-manifest
type: text_freeze_manifest
title: "Text freeze — M-FC05 Authority indipendenti"
status: frozen
domain: "concorsi pubblici italiani"
book_id: m-fc05-authority-indipendenti
volume_code: VOL-05
module_code: M-FC05
freeze_date: 2026-08-22
reference_commit: fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a
updated_at: 2026-08-22
created_at: 2026-08-22
review_required: false
canonical: true
tags: ["text-freeze", "vol-05", "m-fc05", "pipeline-step-16"]
---

# Text freeze — M-FC05 Authority indipendenti

## Esito

Il modulo entra in congelamento testuale il 22 agosto 2026. Sono presenti quindici capitoli e 75 nuclei completi; gli step 11 e 13-15 sono chiusi; indice, Bibbia, fonti e matrice sono coerenti. Il gate `text-freeze`, non ancora automatizzato, viene verificato manualmente prima dell'accettazione motivata.

Da questo manifest sono ammesse soltanto correzioni controllate. Ogni modifica sostanziale a teoria, fonti, casi, quiz, riferimenti o struttura riapre i gate 10-15.

## Riferimento di versione

- Commit di base: `fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a`.
- Stato da congelare: modifiche correnti degli step 07-16, identificate dagli hash seguenti.
- Algoritmo: SHA-256 sul contenuto dei file.
- Cutoff dell'audit specialistico: 22 agosto 2026.

## Verifica delle condizioni

| Condizione | Evidenza | Esito |
| --- | --- | --- |
| Capitoli presenti | Quindici target e quindici file | superata |
| Copertura integrale | 75 nuclei completi; zero parziale, solo-nominato o mancante | superata |
| Rinvii | Nessuna dipendenza editoriale nel corpo; tracciabilità nel frontmatter | superata |
| Humanizer | Tutti i quindici step 11 chiusi con citation guard | superata |
| Errori obbligatori | Step 13-14 chiusi; tutti gli ID corretti | superata |
| Audit specialistico | Step 15 verde; zero errori gravi o medi aperti | superata |
| Indice | Quindici voci e quindici capitoli; nessuna appendice o servizio inesistente promesso | superata |
| Fonti e cutoff | Source refs presenti; dossier specialistico datato | superata |
| Dati operativi | Nessun box `Dato operativo`; dati mobili datati e qualificati | superata |

## File congelati

| File | Stato | SHA-256 |
| --- | --- | --- |
| `index.md` | frozen | `d7dc961cc71fe2f3777e0f5e46d0b0a04344bfd0b288314a07c199d74f3e6b36` |
| `planning/00-piano-editoriale.md` | frozen | `e4bd6eb7adb53506380436676b01131656d8d94b804aa9e78db803a3e0ed0271` |
| `planning/02-matrice-copertura-didattica.md` | frozen | `ecba83a263711bebb252c7c8cf33f9d86588b14b0c1c5a7b2ca22884f14c185d` |
| `planning/03-bibbia-del-modulo.md` | frozen | `03d63cb0a7786347b135c6acdb62036c416f011f154335822c7f37fabd0c5153` |
| `chapters/01-authority-viste-dal-candidato.md` | frozen | `f8574d7bf9d72166f214d3e0403af848440604c9fc18b8e9b99a083219747f39` |
| `chapters/02-indipendenza-governance-accountability-personale.md` | frozen | `920c1ff9500dd56b766a975e7b96f72c212c4e348d76028f504e0325bd5158d1` |
| `chapters/03-regolazione-europea-multilivello-reti-autorita.md` | frozen | `77d7a69a8837db8ca8de6f0ba2b84a15b0711a033ea42f786f190714a47417b8` |
| `chapters/04-ciclo-regolatorio-consultazione-air-vir.md` | frozen | `8740953f4bbc7c53a09f71040bcb95ad63c7fcf2a60a0b940f77e803d98b1cfa` |
| `chapters/05-vigilanza-istruttoria-ispezioni-dati-prova.md` | frozen | `45fdee0c84a68942f64d0b43db8e5d7d6d90a3cd838f062b683a3453a7d88036` |
| `chapters/06-sanzioni-impegni-rimedi-controllo-giurisdizionale.md` | frozen | `d2f4495c2cbd7e4a39ed010d76d7fcc1904a6f0f55f515cbc840f75607b68bc0` |
| `chapters/07-economia-industriale-regolazione-econometria-contabilita.md` | frozen | `bc33e37e7784dae4c204dc111f50e3e18ed626f20271311d149ae9dc07c6389d` |
| `chapters/08-agcm-concorrenza-consumatore-pratiche-scorrette.md` | frozen | `2317707cd261e3980a9d9175f1d05ebed9d893036c83a983d0490aaa57123b5f` |
| `chapters/09-arera-energia-gas-acqua-rifiuti-tariffe.md` | frozen | `9a4e89730eadfa91c5cba137f1e459196221660a8cf8f4476b1eb54abb11f1a8` |
| `chapters/10-agcom-comunicazioni-media-utenti-piattaforme.md` | frozen | `a36f0ce9b51fbb475dff10949949409418a64d9aa5dd34c781471d5832bc9afd` |
| `chapters/11-consob-mercati-intermediari-tutela-investitore.md` | frozen | `a3c5d82bc6513fedcda5de235334a6935944f2646b0713b056ffd260c3fe7b66` |
| `chapters/12-banca-italia-ivass-vigilanza-prudenziale.md` | frozen | `ef6eb7e1aef2341ddd947539355af1ba15837c6910763f7602237641951be03d` |
| `chapters/13-garante-privacy-poteri-procedimenti-cooperazione.md` | frozen | `50ae2164be95848e7884a6e887a846d47ecec7b89768a1819b71b709d64b06b2` |
| `chapters/14-anac-prevenzione-vigilanza-whistleblowing.md` | frozen | `7933d6d83788145dc48dc7e0d44dcf0a677663a8ff8d2a1bd23bc721172ba0bd` |
| `chapters/15-laboratorio-prove-authority.md` | frozen | `5bc59ecd4514a39c7361083b07efabb0161064b1eb8347cbf488b4a14e2706a7` |

## Regola successiva al freeze

Ogni modifica sostanziale successiva deve essere tracciata e sottoposta nuovamente a copertura, Humanizer, revisione trasversale e audit specialistico prima di un nuovo freeze.

Aggiornamento controllato del 22 agosto 2026: i soli campi di stato del modulo e dei capitoli sono stati promossi a `final`/`frozen` dopo il superamento degli step 19-21; il corpo editoriale non è cambiato. Gli hash della tabella recepiscono questa promozione di metadati.
