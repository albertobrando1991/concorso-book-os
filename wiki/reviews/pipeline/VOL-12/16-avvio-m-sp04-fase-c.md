---
id: pipeline-vol-12-16-avvio-m-sp04-fase-c
type: pipeline_handover
title: "VOL-12 — Avvio M-SP04: stato reale del corpus prima di scrivere"
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp04-prefettizia-diplomatica
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp04", "handover", "fase-c"]
---

# VOL-12 — Avvio M-SP04: stato reale del corpus

M-SP02 è chiuso. Si apre M-SP04, come da § 8 di `11-ordine-di-lavoro-codex-fase-c.md`. Prima di applicare quel documento un avvertimento: **la matrice di M-SP04 è disallineata dalla source note**, ed è lo stesso difetto già corretto due volte in questo volume (M-SP03 e il blocker 1 di M-SP04 stesso, l'11 e il 13 agosto). Non ripeterlo una terza volta.

## Quello che la matrice dichiara ancora aperto, e non lo è

I blocker di alta priorità 2 e 3 in `planning/02-matrice-copertura-didattica.md` dicono «testo non acquisito» e «materie non riscontrate». La source note (`wiki/sources/bandi-carriera-prefettizia-e-diplomatica-m-sp04.md`) mostra che sono **già risolti**:

- **d.m. 357/1999** (limiti di età): acquisito e letto (`wiki/raw/m-sp04-prefettizia-diplomatica/dm-357-1999-limiti-eta.pdf`).
- **d.i. 144/2002** e i modificativi **d.i. 39/2007** e **d.i. 80/2017**: acquisiti e letti. Le materie analitiche delle cinque prove scritte della prefettizia (nucleo N-SP04-03-03) sono documentate riga per riga alle linee 44-68 della source note, comprese le due precisazioni già segnalate come mancanti nella revisione strutturale del volume — che la prova b) non è un tema ma una simulazione di problem solving dirigenziale, e che la prova c) non è una prova di lingua nel senso ordinario.
- **d.lgs. 139/2000** (ordinamento prefettizia): letto nella versione vigente su Normattiva. Risolve anche la discrepanza sulla durata della formazione — minimo due anni, non uno.
- **artt. 11-12 del bando MAECI** (lingue facoltative, nucleo N-SP04-08-02): verificati il 13 agosto.
- **Limite ai tentativi per la prefettizia**: verificato che non esiste nel corpus attuale — un'assenza documentata, non un buco.

## Quello che resta genuinamente aperto

- **d.P.R. 18/1967** (ordinamento diplomatica): acquisito ma **non ancora letto** articolo per articolo. Il nucleo N-SP04-14-01 non è chiudibile finché manca questa metà.
- **N-SP04-08-03** — livello linguistico realmente necessario: dichiarato esplicitamente non desumibile da alcuna fonte. Va scritto come stima motivata, non costruito per deduzione (§ 3.5 di `11-ordine-di-lavoro-codex-fase-c.md`).
- **Quesiti pubblicati della preselettiva prefettizia**: verificato il 13 agosto che la raccolta non è ancora online. Non inventare il file. Il capitolo 2 tratta la preselettiva come metodo dell'insieme chiuso **condizionato alla pubblicazione**, sul modello già usato in M-SP02 per le incognite dichiarate della preselettiva vigili del fuoco.
- **N-SP04-04-03** — modalità della prova attitudinale della diplomatica: la source note dice che il criterio è «diverso dal centesimale» ma non ne descrive la procedura. Va approfondito se possibile sul bando MAECI già acquisito prima di scrivere il capitolo 3; se la fonte non va oltre, si dichiara il limite.
- **N-SP04-05-01** — destinazione del rinvio al VOL-01: non risulta verificato. La source note segnala già il rinvio corretto — capitolo del VOL-01 sulla banca dati ufficiale, per il pattern di volume condiviso con la preselettiva prefettizia a quesiti pubblicati.

## Da fare, in ordine

1. **Sincronizzare la matrice**: aggiornare i blocker e la colonna «Stato» dei nuclei ora risolti (in primis N-SP04-03-01, N-SP04-03-03, N-SP04-08-02), con la data e il riferimento alla source note. Non toccare `run-state.json`.
2. **Chiudere i tre punti ancora aperti** elencati sopra, nell'ordine: lettura del d.P.R. 18/1967, verifica della modalità della prova attitudinale, verifica del rinvio al VOL-01. Il livello linguistico (N-SP04-08-03) si dichiara come stima quando si scrive il capitolo 4, non prima.
3. **Scrivere i nove capitoli** secondo § 4.4 di `11-ordine-di-lavoro-codex-fase-c.md`, con il contratto del formato 2 di § 1 e § 1.5 dello stesso documento. Il modello di riferimento sono gli otto capitoli di M-SP02, in particolare 02, 03 e 04 per densità e uso delle tabelle di dati.
4. Alla consegna: esito dei due gate capitolo per capitolo, matrice ricalcolata, elenco esplicito delle incognite dichiarate (in primis N-SP04-08-03 e l'eventuale mancata pubblicazione dei quesiti), come da § 9 dell'ordine di lavoro.

Non serve rifare il reperimento fonti già fatto. Non serve rileggere quello che la source note dichiara già `VERIFICATO`.
