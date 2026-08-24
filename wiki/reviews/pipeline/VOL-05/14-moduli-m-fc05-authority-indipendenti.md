---
id: review-pipeline-vol-05-step-14-m-fc05
type: review
title: "VOL-05 step 14 — applicazione correzioni M-FC05"
status: complete
book_id: vol-05-authority-regolazione
module_code: M-FC05
updated_at: 2026-08-22
review_required: false
canonical: true
---

# Applicazione delle correzioni — M-FC05

## Esito

Tutti gli ID del report trasversale sono chiusi. Le modifiche sostanziali hanno superato nuovamente lint, copertura/densità, protezione delle citazioni e micro-revisione nei rispettivi cicli di capitolo. La matrice registra 75 nuclei completi e i frontmatter dichiarano Formato 2, fonti, compilazione e stato reale.

## Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| M05-01 | Capp. 01-15 | Struttura | Grave | Assenza del Formato 2. | Segmentare e verificare 75 nuclei. | Corretto |
| M05-02 | Capp. 01-15 | Autonomia | Grave | Presenza di note interne nel corpo. | Rimuovere sezioni di lavorazione e wikilink. | Corretto |
| M05-03 | Capp. 03 e 09 | Fact-check | Grave | REMIT non aggiornato alla riforma. | Integrare poteri investigativi ACER e competenza nazionale finale. | Corretto |
| M05-04 | Cap. 07 | Approfondimento | Importante | Strumenti quantitativi troppo sintetici. | Ampliare econometria e contabilità regolatoria. | Corretto |
| M05-05 | Cap. 10 | Contenuto | Importante | DMA e memo inglese insufficienti. | Sviluppare riparto e modello di memo. | Corretto |
| M05-06 | Capp. 11-12 | Coerenza | Grave | MiCAR, SSM, DORA e ADR incompleti. | Integrare fonti, riparti, date e limiti. | Corretto |
| M05-07 | Cap. 14 | Fact-check | Importante | Regime probatorio della ritorsione assente. | Esporre presunzione e limiti. | Corretto |
| M05-08 | Cap. 15 | Conclusione | Importante | Chiusura editoriale assente. | Inserire conclusione di sintesi applicativa. | Corretto |
| M05-09 | Figure | Stile | Migliorabile | Didascalie seriali. | Differenziare le funzioni delle tavole. | Corretto |
| M05-10 | Cap. 15 | Tipografia | Importante | Salto gerarchico H2→H4. | Uniformare le simulazioni a H3. | Corretto |

## Registro operativo

| ID | File modificato | Correzione | Fonte/evidenza | Stato finale |
| --- | --- | --- | --- | --- |
| M05-01 | `chapters/01-15`; `planning/02-matrice-copertura-didattica.md` | Formato 2, cinque nuclei e sei risposte commentate per capitolo | gate step 09-10 superati | chiuso |
| M05-02 | `chapters/01-15` | eliminate specifiche, riferimenti consolidati e note di review dal corpo | gate chapter-lint e citation guard | chiuso |
| M05-03 | `chapters/03`; dossier specialistico | corretto il riparto REMIT | regolamento (UE) 2024/1106 | chiuso |
| M05-04 | `chapters/07` | aggiunti HHI, elasticità, specificazione, controfattuale e cost allocation | fonte economica consolidata e caso numerico didattico | chiuso |
| M05-05 | `chapters/10` | chiariti DMA/DSA e inserito memo in inglese | regolamenti UE e riparto di enforcement | chiuso |
| M05-06 | `chapters/11`, `chapters/12`; dossier specialistico | integrati MiCAR, SSM, DORA, ABF e AAS | BCE, Banca d'Italia, IVASS, EUR-Lex | chiuso |
| M05-07 | `chapters/14`; dossier specialistico | integrato onere della prova e limite soggettivo | d.lgs. n. 24/2023 e linee guida ANAC | chiuso |
| M05-08 | `chapters/15` | conclusione autonoma e memorabile | promessa della Bibbia di Volume | chiuso |
| M05-09 | `chapters/01-15` | didascalie rese descrittive | confronto trasversale delle 75 figure | chiuso |
| M05-10 | `chapters/15` | titoli simulazioni promossi a H3 | gate chapter-lint | chiuso |

## Secondo controllo

Il controllo successivo all'applicazione ha verificato che nessuna modifica abbia rimosso source_refs, last_compiled_from, casi, verifiche o collocazioni della matrice. Non risultano regressioni né correzioni assegnate alla revisione umana.

## Giudizio

Pubblicabile con correzioni minori.

Le correzioni testuali previste dal report sono applicate. Restano i controlli di specialità, freeze, immagini, layout e consegna previsti dalla pipeline.
