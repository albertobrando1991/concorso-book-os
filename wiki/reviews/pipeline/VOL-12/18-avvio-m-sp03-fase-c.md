---
id: pipeline-vol-12-18-avvio-m-sp03-fase-c
type: pipeline_handover
title: "VOL-12 — Avvio M-SP03: stato reale del corpus prima di scrivere"
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp03-magistratura-avvocatura-notariato
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp03", "handover", "fase-c"]
---

# VOL-12 — Avvio M-SP03: stato reale del corpus

M-SP02 e M-SP04 sono chiusi. Si apre M-SP03, ultimo modulo del volume per cui non serve una decisione umana preliminare (M-SP01 resta bloccato sulla decisione di perimetro del livello ufficiali). Stesso avvertimento dato per M-SP04: **la matrice è disallineata dalla source note**, e in più la source note contiene una **contraddizione interna**. Non ripetere l'errore una terza volta.

## Quello che la matrice dichiara ancora aperto, e non lo è

I blocker di alta priorità 1, 2 e 3 in `planning/02-matrice-copertura-didattica.md` dicono «testi vigenti non letti», «da accertare», «verificare se». La source note (`wiki/sources/bandi-magistratura-avvocatura-notariato-m-sp03.md`) mostra che sono **già risolti**, con data:

- **d.lgs. 160/2006, art. 2 vigente**: letto in coordinamento con l'art. 33 del d.l. 144/2022 e con l'art. 2 del bando a 450 posti. Risolto anche il nucleo N-SP03-03-01: le categorie storiche di accesso restano vie autonome, il laureato è ammesso senza ulteriori titoli.
- **Svolgimento informatizzato della prova scritta**: verificato che per la tornata a 450 posti **non è stato attivato** — il diario ufficiale del 10 marzo 2026 dispone lo svolgimento tradizionale secondo gli artt. 7 e 10 del r.d. 1860/1925, pur essendo la facoltà prevista dal d.m. 15 giugno 2023.
- **r.d. 1860/1925**: acquisito e schedato.
- **L. 89/1913, art. 5** (requisiti del notariato): dichiarato letto nel testo vigente, originale di Gazzetta Ufficiale acquisito.
- **Limiti ai tentativi**: risolti per tutti e tre i binari — quattro inidoneità per la magistratura, cinque per il notariato, per l'Avvocatura il vincolo caratterizzante è il limite anagrafico di 35 anni del bando, non un numero di tentativi.
- **L. 1035/1966** (ordinamento Avvocatura dello Stato): acquisita da Gazzetta Ufficiale e schedata.

## Una contraddizione interna da sciogliere, non da ignorare

La stessa source note contiene due affermazioni incompatibili sull'art. 5 della L. 89/1913:

- riga 157: *«DA VERIFICARE (fonte secondaria): la compiuta pratica notarile come titolo... Il requisito discende dall'art. 5 della legge notarile, **che va letto**.»*
- riga 234, nella checklist di chiusura: *«[x] L. 89/1913, art. 5, **letta** nel testo vigente e originale G.U. acquisito.»*

Non è un dettaglio: l'art. 5 nn. 1-5 è la fonte diretta dei requisiti d'accesso al notariato, compresa la durata della pratica notarile che il bando richiede come titolo. **Prima di scrivere il capitolo sul binario C, rileggere l'art. 5 sul PDF acquisito (`wiki/raw/m-sp03-magistratura-avvocatura-notariato/legge-89-1913-ordinamento-notariato.pdf`) e sostituire la riga 157 con il dato verificato** — durata della pratica, eventuale alternativa dell'idoneità in precedente concorso, termine di certificazione. Se il dettaglio richiesto dal bando non coincide con l'art. 5, la discrepanza va dichiarata, non nascosta scegliendo una delle due righe a caso.

## Quello che resta genuinamente aperto

- **N-SP03-16-02** — l'Avvocatura dello Stato: la L. 1035/1966 è acquisita e «schedata», un livello di verifica più leggero di «letta nel testo vigente» usato per le altre due leggi ordinamentali. Va confermato se la lettura articolo per articolo è stata fatta per le disposizioni che il capitolo userà, o va completata prima di scrivere.
- **N-SP03-05-02** — disciplina dei testi di consultazione ammessi alla prova del notariato: risulta ancora nell'elenco dei dati mobili della tornata, non in un paragrafo verificato a sé. Va scritta nel capitolo come dato mobile con box di verifica sul bando, sul modello già usato in M-SP02 e M-SP04 per i dati che cambiano a ogni tornata — non va costruita come se fosse stabile.

## Da fare, in ordine

1. **Sincronizzare la matrice**: aggiornare i blocker e la colonna «Stato» dei nuclei ora risolti, con data e riferimento alla source note.
2. **Sciogliere la contraddizione sull'art. 5** rileggendo il PDF, come descritto sopra.
3. **Chiudere i due punti ancora aperti** (Avvocatura, testi di consultazione).
4. **Scrivere i nove capitoli** secondo § 4.3 di `11-ordine-di-lavoro-codex-fase-c.md`, rispettando il contratto del formato 2 e la regola dei cinque nuclei di §§ 1 e 1.5 dello stesso documento. Il modulo ha **tre binari separati** (magistratura, Avvocatura, notariato): ogni capitolo di binario dichiara in apertura a quale si rivolge, come già fatto in M-SP04 per i suoi due binari.
5. Il notariato porta **l'avvertenza sul mancato accesso al pubblico impiego**, richiesta dalla scheda di volume: va in apertura di modulo (capitolo 1) e ripresa nel capitolo del binario C.
6. Alla consegna: esito dei due gate capitolo per capitolo, matrice ricalcolata, elenco esplicito delle incognite dichiarate, come da § 9 dell'ordine di lavoro. Scrivere la consegna in `wiki/reviews/pipeline/VOL-12/19-consegna-m-sp03-fase-c.md`.

Non serve rifare il reperimento fonti già fatto. Non serve rileggere quello che la source note dichiara già `VERIFICATO` con data — tranne l'art. 5 della L. 89/1913, che va riletto per la ragione spiegata sopra.
