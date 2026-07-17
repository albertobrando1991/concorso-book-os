---
id: dashboard-copertura-didattica-globale
type: dashboard
title: "Copertura didattica globale"
status: active
domain: "concorsi pubblici italiani"
topics: ["copertura didattica integrale", "catalogo editoriale"]
entities: ["Metodo BANDO", "ConcorsoBook OS"]
source_refs: ["sources/principio-copertura-didattica-integrale-2026-07-17.md", "sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["books/moduli/architettura-moduli-specialistici.md"]
confidence: 0.96
updated_at: 2026-07-17T00:00:00+02:00
created_at: 2026-07-17T00:00:00+02:00
review_required: true
canonical: false
tags: ["dashboard", "inventory", "didactic-coverage"]
---

# Copertura didattica globale

> Fotografia strutturale della working tree sporca al 17 luglio 2026. E' un inventario, **non un audit semantico**. File, parole e stato `source_ready` non equivalgono a copertura completa o pubblicabilita.

## Quadro sintetico

| Indicatore | Valore | Lettura corretta |
| --- | ---: | --- |
| Volumi commerciali canonici | 12 | 2 con artefatto proprio; 10 solo aggregatori definiti in architettura |
| Moduli canonici | 25 | 25 cartelle/index presenti |
| Moduli con capitoli sostanziali | 3 | M-FC01, M-FC02, M-FC03 |
| Moduli scaffold | 22 | index/piano senza capitoli sostanziali |
| Capitoli propri dei volumi | 55 | 54 VOL-01; 1 VOL-03 |
| Parole indicative nei volumi | 194.633 | non include i moduli aggregati |
| Capitoli dei moduli | 48 | 15 + 14 + 19 |
| Parole indicative nei moduli | 110.839 | non misura completezza |
| Matrici didattiche dedicate conformi | 0 | Appendice F VOL-01 e matrice materie M-FC03 sono strumenti preesistenti da riallineare |
| Elementi dichiarabili pubblicabili | 0 | audit semantico e review non ancora eseguiti |

Convenzione: `Source refs` conta i riferimenti distinti dei capitoli e indica separatamente quelli dell'index. `Matrice` significa matrice didattica dedicata conforme al nuovo gate; l'Appendice F di VOL-01 e altre matrici editoriali preesistenti non sono conteggiate come conformi finche' non riallineate.

## Semaforo volumi

| ID | Stato filesystem/editoriale | Moduli aggregati | Cap./parole propri | Source refs | Matrice |
| --- | --- | --- | ---: | ---: | --- |
| VOL-01 | draft/revised esteso, non verificato | base + ricettario | 54 / 191.026 | 129 | no |
| VOL-02 | aggregatore, cartella assente | M-FL01/04 | 0 / 0 | 0 | no |
| VOL-03 | aggregatore source-ready con draft | M-FC01/03 | 1 / 3.607 | 6 capitolo; 2 index | no |
| VOL-04 | aggregatore, cartella assente | M-FC04 | 0 / 0 | 0 | no |
| VOL-05 | aggregatore, cartella assente | M-FC05 | 0 / 0 | 0 | no |
| VOL-06 | aggregatore, cartella assente | M-IR01/04 | 0 / 0 | 0 | no |
| VOL-07 | aggregatore, cartella assente | M-SA01/04 | 0 / 0 | 0 | no |
| VOL-08 | aggregatore, cartella assente | M-TR01 | 0 / 0 | 0 | no |
| VOL-09 | aggregatore, cartella assente | M-TR02 | 0 / 0 | 0 | no |
| VOL-10 | aggregatore, cartella assente | M-TR03 | 0 / 0 | 0 | no |
| VOL-11 | aggregatore, cartella assente | M-TR04 | 0 / 0 | 0 | no |
| VOL-12 | aggregatore, cartella assente | M-SP01/04 | 0 / 0 | 0 | no |

Un volume aggregatore privo di capitoli propri non e' automaticamente mancante se aggrega moduli identificati; non e' pero copertura verificata.

## Semaforo moduli

| Famiglia | Moduli | Stato strutturale | Capitoli/parole | Matrice |
| --- | --- | --- | ---: | --- |
| Funzioni Centrali | M-FC01 | source-ready; structure/revised | 15 / 8.902 | no |
| Funzioni Centrali | M-FC02 | source-ready; draft/revised | 14 / 43.147 | no |
| Funzioni Centrali | M-FC03 | source-ready; structure/revised | 19 / 58.790 | no; matrice materie da riallineare |
| Funzioni Centrali | M-FC04, M-FC05 | scaffold | 0 / 0 | no |
| Funzioni Locali | M-FL01, M-FL02, M-FL03, M-FL04 | scaffold | 0 / 0 | no |
| Istruzione e Ricerca | M-IR01, M-IR02, M-IR03, M-IR04 | scaffold | 0 / 0 | no |
| Sanita | M-SA01, M-SA02, M-SA03, M-SA04 | scaffold | 0 / 0 | no |
| Trasversali | M-TR01, M-TR02, M-TR03, M-TR04 | scaffold | 0 / 0 | no |
| Carriere Speciali | M-SP01, M-SP02, M-SP03, M-SP04 | scaffold | 0 / 0 | no |

Tutti i 25 moduli hanno cartella e `index.md`. Gli scaffold hanno in genere due source refs nell'index, mentre i tre moduli source-ready dichiarano rispettivamente 13, 12 e 6 riferimenti nell'index; questi riferimenti non certificano che i contenuti siano completi.

## Coda prioritaria

1. Creare e validare le matrici didattiche, iniziando dal pilota M-FC02/VOL-03.
2. Eseguire audit semantici sulle promesse formative; nessun elemento e' oggi certificato pubblicabile.
3. Chiudere gli stati `structure`, `source_ready` e `draft` nei tre moduli avviati.
4. Trasformare i 22 scaffold in contenuto soltanto dopo fonti consolidate.
5. Formalizzare cartella/index dei dieci aggregatori quando serve al workflow, senza duplicare i moduli.

Dettaglio, metodo e blocker: [[reviews/audit-copertura-didattica-inventario-globale-2026-07-17]]. Regola vincolante: [[sources/principio-copertura-didattica-integrale-2026-07-17]] e [[topics/copertura-didattica-integrale]].
