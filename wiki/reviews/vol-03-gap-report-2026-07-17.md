---
id: review-vol-03-gap-report-2026-07-17
type: review
title: "VOL-03 - Gap report finale della ricostruzione"
status: completed
domain: "concorsi pubblici italiani"
topics: ["vol-03", "copertura", "quality assurance"]
entities: ["AE", "ADM", "AdER", "INPS", "INAIL", "INL"]
source_refs: ["sources/vol-03-corpus-ufficiale-2026-07-17"]
book_refs: ["vol-03-fisco-dogane-previdenza-ispettivo", "m-fc02-agenzie-fiscali", "m-fc03-enti-non-economici"]
confidence: 0.94
updated_at: 2026-07-17T20:30:00+02:00
created_at: 2026-07-17T20:30:00+02:00
review_required: true
canonical: true
tags: ["review", "gap-report", "volume-code-vol-03"]
issue_type: final_coverage
severity: medium
affected_pages: ["intero volume"]
---

# Gap report finale

## Sintesi

La ricostruzione copre tutte le materie previste dal dossier v4 mediante 40 capitoli, quattro blocchi editoriali, strumenti e appendici. Sono state acquisite 20 nuove fonti ufficiali oltre al corpus persistente: 7 M-FC02 e 13 M-FC03. Nessun download è fallito e tutti i file acquisiti sono non vuoti e dotati di hash SHA-256.

## Matrice di copertura

| Modulo | Materia | Profili | Capitoli | Fonti | Stato | Dati mobili/review |
| --- | --- | --- | --- | --- | --- | --- |
| M-FC02 | ordinamento agenzie | tutti | 1-4 | D.Lgs. 300/1999; atti enti; bandi | completa | atti organizzativi |
| M-FC02 | tributario sostanziale | tributario, assistenti, ACFI | 5-8 | TUIR, IVA, Statuto, adempimenti | completa | aliquote, termini |
| M-FC02 | accertamento/compliance | tributario, ACFI | 9-10 | DPR 600; D.Lgs. 128; riforma | completa | soglie e correttivi |
| M-FC02 | riscossione/processo | tributario, AdER | 11-13 | DPR 602; D.Lgs. 546 | completa | riforme e PTT |
| M-FC02 | sanzioni/reati | tributario, ADM | 12 | D.Lgs. 471, 472, 74 e 87 | completa | interpretazione coordinata |
| M-FC02 | dogane/accise | ADM | 14-16 | CDU; D.Lgs. 141; TUA | completa | atti UE e aliquote |
| M-FC02 | giochi | ADM | 17 | D.Lgs. 41; portale ADM | completa selettiva | rete fisica e regole tecniche |
| M-FC02 | catasto/audit/civile | tecnici, ACFI | 18-20 | fonti catastali; codice civile; bandi | completa | principi OIC |
| M-FC03 | previdenza/contribuzione | CPS, ispettori | 22-24 | RDL 1827; L. 153; L. 335 | completa | requisiti/importi |
| M-FC03 | ammortizzatori/ISEE | CPS | 25-26 | D.Lgs. 148; DPCM 159 | completa | circolari 2026 |
| M-FC03 | INAIL | CPS, ispettori, FA | 27 | DPR 1124; D.Lgs. 38 | completa | prestazioni/importi |
| M-FC03 | ricorsi | CPS, FA | 28 | DPR 639; regolamenti enti | completa | regolamenti correnti |
| M-FC03 | vigilanza/tecnica | ispettori, VC | 29-31 | D.Lgs. 124; L. 689; prassi INL | completa | nuove circolari |
| M-FC03 | sicurezza | ispettori | 32 | D.Lgs. 81; D.Lgs. 758 | completa nel delta | rinvio nucleo generale |
| M-FC03 | documenti contabili | ispettori | 33 | contabilità, LUL e prassi | completa selettiva | contratti e paghe |
| M-FC03 | EPNE/governance | FA, VC | 34-35 | L. 70; D.Lgs. 479; statuti | completa | statuti/regolamenti |
| M-FC03 | personale/servizi | FA | 36-37 | CCNL 2022-2024; fonti enti | completa nel delta | ipotesi CCNL 2025-2027 |
| M-FC03 | PIAO/compliance | FA, VC | 38-39 | PIAO, controlli, documenti enti | completa | PIAO annuali |
| Trasversale | ICT/procurement/sanitari/carriere | profili speciali | rinvii | VOL-07/08/09/12 | rinvio_cross_family | nessuna duplicazione |

## Review umana obbligatoria

1. Interpretazione delle disposizioni transitorie delle riforme fiscali 2024-2026.
2. Selezione e massimazione della giurisprudenza.
3. Requisiti pensionistici, importi, aliquote contributive e ISEE dell'anno di pubblicazione.
4. Regole tecniche dei giochi e atti ADM mobili.
5. Allegati integrali e comunicazioni successive dei bandi.
6. Statuti, regolamenti, PIAO e bilanci dell'ente scelto per il singolo concorso.
7. Stato dell'ipotesi CCNL Funzioni Centrali 2025-2027 al momento della pubblicazione.

## Limiti tecnici

- LocalAgentMemory è stato invocato tramite il servizio canonico, ma il ranking sul deposito reale fallisce quando incontra almeno un record storico senza il campo `keywords`. Il difetto è preesistente; non è stato corretto perché fuori scope.
- `apply_patch` non ha potuto aggiornare alcuni file non tracciati già presenti a causa del wrapper sandbox Windows. Le nuove versioni sono state create separatamente e sostituite solo sui sette percorsi VOL-03 esplicitamente verificati.
- Il manifest include le fonti-obiettivo e le principali nuove acquisizioni; le source notes contengono l'elenco completo dei raw integrativi.

## Giudizio

Il volume è **source-ready** per la scrittura professionale. Non è ancora pubblicabile come testo completo: richiede la stesura dei capitoli e la review editoriale/normativa prevista dal progetto.

