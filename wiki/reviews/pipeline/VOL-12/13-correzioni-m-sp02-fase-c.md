---
id: pipeline-vol-12-13-correzioni-m-sp02
type: pipeline_review
title: "VOL-12 — M-SP02: correzioni da applicare prima della chiusura del modulo"
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp02-vigili-fuoco
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp02", "review", "correzioni"]
---

# VOL-12 — M-SP02: correzioni da applicare prima della chiusura del modulo

Review della consegna in `wiki/reviews/pipeline/VOL-12/12-consegna-m-sp02-fase-c.md`. I due gate (densità didattica, contratto del lettore) sono stati rieseguiti su tutti e otto i capitoli e passano davvero — non è in discussione la loro esecuzione. Il problema è che passano senza che il contenuto soddisfi il criterio sostanziale che approssimano.

**Non riscrivere da zero.** I tre capitoli 02-03-04 sono confermati a piena qualità. Le correzioni riguardano i capitoli 05-08 e la matrice.

## 1. Riserve mancanti nel capitolo 05 — bloccante

Il capitolo 05 e la source note B2 (bando D.D. n. 2320 dell'11/6/2025, 38 posti vice direttore ruolo ordinario) dichiarano lettura integrale del bando ma **non riportano le riserve dell'art. 1**, che coprono il 52% dei posti:

| Quota | Categoria | Condizione |
| ---: | --- | --- |
| 25% | personale del Corpo nazionale | requisiti art. 2 escluso il limite di età, alla scadenza domanda |
| 10% | personale volontario del Corpo | iscritto da almeno 7 anni, minimo 200 giorni di servizio |
| 15% | operatori del servizio civile universale | servizio concluso senza demerito |
| 2% | ufficiali delle Forze armate | ferma biennale conclusa senza demerito |

Due regole collegate, anch'esse assenti:

- il personale destinatario della riserva del 25% **non è soggetto ai limiti massimi di età** (art. 155, comma 3, d.lgs. 217/2005);
- chi ha riportato nel triennio precedente una sanzione disciplinare pari o più grave della sanzione pecuniaria è **escluso dalle riserve** delle lettere a) e b).

I posti riservati non coperti tornano in graduatoria agli altri idonei; la riserva va dichiarata in domanda — stesso meccanismo già trattato nel capitolo 02 per il binario operativo.

**Da fare:**
- Aggiungere alla source note B2 (`wiki/sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02.md`) la tabella delle riserve e le due regole collegate, letta sull'art. 1 del bando già acquisito in `wiki/raw/m-sp02-vigili-fuoco/vvf-bando-vice-direttori-ruolo-ordinario.pdf`.
- Nel capitolo 05, trattare le riserve con lo stesso livello di dettaglio del capitolo 02 per il binario operativo: chi rientra in ciascuna quota, il meccanismo di devoluzione, l'obbligo di dichiarazione, l'effetto sul limite di età per la riserva del 25%.
- Aggiornare la matrice: N-SP02-07-01 non è `completo` finché questo manca.

## 2. Sezioni-fantoccio — bloccante, in tutti e cinque i capitoli 01, 05, 06, 07, 08

`## Inquadramento teorico` e `## Errori e trappole` compaiono con una sola frase sotto (13-19 parole). Sono posizionate per far riconoscere al gate i pattern «spiegazione teorica» e «errore o trappola» — non portano contenuto autonomo.

**Da fare, per ciascuno dei cinque capitoli:** o le sezioni vengono sviluppate con contenuto reale proporzionato al resto del capitolo, o vengono rimosse e i concetti che dovrebbero introdurre confluiscono nei nuclei dove servono davvero (è il pattern già usato nei capitoli 02-03-04, che non hanno queste sezioni separate e passano lo stesso il lint gate tramite i nuclei).

## 3. Scrittura calibrata alla soglia — bloccante

Nei cinque capitoli nuovi 25 nuclei su 25 stanno fra 600 e 643 parole, contro un range 610-1.068 nei capitoli 02-04. Il capitolo 06 ha la frase «La verifica resta sempre documentata e datata.» ripetuta due volte a tre righe di distanza, la seconda isolata in fondo al nucleo — segno diretto di riempimento per superare la soglia.

Il criterio del § 1.5 dell'ordine di lavoro (`11-ordine-di-lavoro-codex-fase-c.md`) è stato applicato al contrario: prevede di dividere un nucleo di copertura in più nuclei solo quando la fonte lo giustifica, non di dividerlo per raggiungere il numero cinque e poi riempire ciascuno fino a 600 parole.

**Da fare:** per ciascun capitolo 05-08, verificare se il contenuto realmente disponibile nella fonte giustifica cinque nuclei da 600+ parole. Dove non lo giustifica, tornare al criterio del piano editoriale: accorpare a un capitolo adiacente, con la nota di struttura che spiega il sintomo (esattamente come già fatto per gli accorpamenti da 12 a 8 capitoli). Non riempire. Rimuovere la frase duplicata nel capitolo 06.

## 4. Assenza di tabelle di dati — bloccante

I capitoli 02 e 04 hanno rispettivamente 28 e 54 righe di tabella (soglie, punteggi, requisiti). I capitoli 05-08 hanno solo la tabella fissa della Mappa BANDO. Il capitolo 06 arriva a descrivere una tabella che non fornisce mai al lettore («La tabella finale contiene materia, formula del bando, copertura esistente, delta, output e test»).

**Da fare:** costruire almeno una tabella di dati reali per capitolo, tratta dalla fonte già acquisita — es. nel capitolo 05 la scheda requisiti/riserve/età del bando 2320, nel capitolo 06 la matrice riuso-delta materia per materia effettivamente compilata (non descritta), nel capitolo 07 il piano 30/60/90 con contenuti per fase, nel capitolo 08 la tabella errori/segnale/correzione già usata come modello in altri moduli del volume.

## 5. Checklist dimensionale della matrice — minore ma da correggere

La tabella «Checklist dimensionale dei nuclei» in `planning/02-matrice-copertura-didattica.md` ha 40 righe identiche, stesso `Q:6 C:1 E:5` per tutte. È falso per i capitoli 02, 03, 04, che hanno rispettivamente 10, 8, 10 domande aperte, non 5.

**Da fare:** compilare la checklist con i conteggi reali per capitolo, o rimuoverla se è ridondante con la tabella principale. Se resta, verificare che non introduca una seconda colonna «Stato» che il gate `coverage` potrebbe leggere raddoppiando il conteggio dei nuclei da 40 a 80.

## Nota per la review successiva

Confermato e non da rifare: capitoli 02, 03, 04; corpus delle fonti acquisite (incluso il bando 2320, dato verificato sull'articolato); rinvii incrociati fra capitoli; indice studente; nessuna modifica al run-state.

Quando le correzioni sono applicate, ripetere l'esecuzione dei due gate su tutti gli otto capitoli e allegare l'esito capitolo per capitolo alla nuova consegna, come richiesto dal § 9 dell'ordine di lavoro.
