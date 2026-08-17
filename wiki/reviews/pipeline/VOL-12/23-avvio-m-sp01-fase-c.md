---
id: pipeline-vol-12-23-avvio-m-sp01-fase-c
type: pipeline_handover
title: "VOL-12 — Avvio M-SP01: perimetro chiuso, corpus completo, via libera alla scrittura"
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp01-forze-ordine
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-14T01:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp01", "handover", "fase-c"]
---

# VOL-12 — Avvio M-SP01: stato reale del corpus

M-SP04 è chiuso (review in [[reviews/pipeline/VOL-12/22-review-m-sp04-fase-c]]). Si apre M-SP01, come da § 8 di `11-ordine-di-lavoro-codex-fase-c.md`. Stesso avvertimento già dato per M-SP04: **la matrice era disallineata dalla source note**, terza occorrenza dello stesso difetto nel volume dopo M-SP03 e M-SP04. È stata risincronizzata in questa review — leggila aggiornata, non la versione che ricordi da prima dell'11-13 agosto.

## Le due decisioni di perimetro che bloccavano l'avvio sono chiuse

1. **D1 — livello ufficiali dei Carabinieri (Accademia Militare, 65 posti): escluso.** Decisa l'11 agosto.
2. **D4 — livello ufficiali della Guardia di Finanza (Accademia GdF, 69 posti): escluso, per un motivo diverso da D1.** Non è lo status militare — la GdF resta nel perimetro per la sua funzione di polizia — ma proporzione e preparazione pluriennale non assimilabile ai due binari. Decisa da questa review il 14 agosto.

Entrambe documentate in `wiki/books/volumi/vol-12-carriere-speciali-premium/planning/05-decisioni-di-perimetro.md` (D1 e D4) e dichiarate nell'index del modulo. **Il modulo resta a due binari, base e ispettivo, 10 sezioni**, come da `planning/00-piano-editoriale.md`. Non introdurre un terzo binario: la decisione è presa e motivata, non è un'opzione aperta in fase C.

## Il corpus è completo — nessun blocker di reperimento o verifica residuo

La matrice (`planning/02-matrice-copertura-didattica.md`) elencava il 2026-08-11 nove blocker di alta/media priorità. **Sono tutti risolti**, non per deduzione ma per lettura integrale delle fonti:

- **d.m. 198/2003 e giurisprudenza sulla condotta** (N-SP01-04-01, 04-03): non era un conflitto giurisprudenziale ma un accostamento improprio. La condotta è materia dell'art. 26 L. 53/1989 (valutazione caso per caso, mai automatica); la Corte cost. n. 40/2024 lo conferma dichiarando incostituzionale una clausola di esclusione automatica della GdF. Sintesi completa in `wiki/sources/ordinamento-forze-di-polizia-quadro-normativo-m-sp01.md`. Questo era l'unico punto originariamente classificato «review umana»: non serve più.
- **d.lgs. 95/2017 e correttivo 126/2018** (N-SP01-02-01): vigenza verificata.
- **L. 121/1981, d.lgs. 66/2010** (N-SP01-01-01, 01-02, 11-01): testo vigente letto su Normattiva.
- **Efficienza fisica GdF** (N-SP01-06-01): Allegato 4 del bando 69 allievi ufficiali acquisito. PS, CC e GdF ora coperti allo stesso livello.
- **Accertamenti psico-fisici e attitudinali PS** (N-SP01-06-02, 06-03): i tre documenti procedurali riletti integralmente, non solo nella parte sulle prove fisiche.
- **Rinvio VOL-01** (N-SP01-10-01): destinazione verificata, `banca-dati-ufficiale-studiarla-senza-memorizzare-male.md` esiste nel volume base.
- **Contingenti e riserve, TULPS, c.p.p.**: verificati nel perimetro del modulo.

Non c'è nulla da reperire prima di scrivere. Non rileggere da capo quello che le source note dichiarano già `VERIFICATO`.

## Un'attenzione che riguarda solo la scrittura, non le fonti

Il d.m. 198/2003 **non è abolito**: resta la fonte per idoneità psichica e attitudinale. È **abolito solo il requisito di statura**, sostituito dai parametri misurati del d.P.R. 207/2015 per i concorsi banditi dopo il 13 gennaio 2016. Non scrivere valori di statura nel capitolo 4: è l'errore diffuso che la source note segnala esplicitamente.

## Da fare, in ordine

1. **Non toccare la decisione di perimetro.** Le sezioni 1, 2 e 4 si scrivono sui due binari già definiti.
2. **Scrivere i dieci capitoli** secondo § 4.2 di `11-ordine-di-lavoro-codex-fase-c.md`, con il contratto del formato 2 di § 1 e la regola dei cinque nuclei di § 1.5. Il capitolo 2 porta le due avvertenze pesanti già indicate nel mandato: il limite di età reale (29 anni, non «18-26» come riportano le fonti secondarie) e il fatto che le cause di esclusione, ora risolte, vanno scritte sul principio della valutazione caso per caso — non come lista chiusa.
3. **Avvertenza medica obbligatoria** nel capitolo sull'efficienza fisica (§ 1 di § 2 delle regole di merito del mandato): il modulo descrive prove e criteri, non prescrive allenamenti.
4. Alla consegna: esito dei due gate capitolo per capitolo, matrice ricalcolata (colonna Stato da `mancante` a `completo` solo dove il capitolo esiste e supera entrambi i gate), elenco esplicito delle incognite dichiarate, come da § 9 dell'ordine di lavoro.

## Comando per riprendere in mano lo stato

```
npm run pipeline -- status VOL-12 --json
```

Lo step 07 su `moduli/m-sp01-forze-ordine` risulta ancora `in-progress` (owner `info`, provider `codex`, dall'11 agosto). Il gate `coverage` di quello step non passerà finché i capitoli non esistono — è l'esito corretto, non forzarlo con `--accept`. La scheda di pipeline del volume dichiara ancora solo le fasi A e B: finché non viene estesa (§ 7 dell'ordine di lavoro, da fare quando l'indice dei dieci capitoli è stabile), i gate di capitolo si eseguono con lo script temporaneo che importa `didactic-density-gate` e `chapter-lint-gate`, come già fatto per M-SP02 e M-SP04.
