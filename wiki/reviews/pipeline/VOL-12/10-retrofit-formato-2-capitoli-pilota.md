---
id: pipeline-vol-12-10-retrofit-formato-2
type: pipeline_review
title: "VOL-12 — I capitoli pilota dichiaravano il formato 2 senza rispettarlo"
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp02-vigili-fuoco
domain: "concorsi pubblici italiani"
updated_at: 2026-08-12T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp02", "formato-2", "gate"]
---

# VOL-12 — I capitoli pilota dichiaravano il formato 2 senza rispettarlo

## Il difetto

I due capitoli pilota di M-SP02 dichiaravano `format_version: 2` nel frontmatter. Misurati dai gate che il formato 2 impone, valevano questo:

| Metrica | Soglia | Capitolo 02 | Capitolo 04 |
| --- | ---: | ---: | ---: |
| nuclei numerati `N-XX00-00-00 · Titolo` | 5 | **0** | **0** |
| parole per nucleo | 600 | — | — |
| blocchi `▣ Verifica` | 1 | **0** | **0** |
| quiz con risposta commentata | 6 | **0** | **0** |
| casi ragionati o guidati | 1 | **0** | **0** |
| parole del capitolo | 3.000 | 3.883 | 2.807 |

Il gate `chapter-lint` aggiungeva quattro rilievi ulteriori su entrambi: mancanza di una sezione «Obiettivo del capitolo», mancanza della «Mappa BANDO del capitolo», assenza di `draft_stage` nel frontmatter, assenza di `last_compiled_from`.

Sarebbero stati **bloccati allo step 10** in blocco, e la discussione sul conteggio delle parole che aveva occupato la sessione precedente misurava il criterio sbagliato: 2.807 parole erano il minore dei problemi di un capitolo che, per la pipeline, non aveva nuclei.

## Perché è successo

Il formato 2 è definito in due punti distinti — la scheda della skill e il codice dei gate — e la scrittura si era allineata alla descrizione discorsiva («almeno cinque nuclei, verifiche vicine, sei quiz, un caso») senza verificare **la forma sintattica** che il gate riconosce: l'heading di nucleo con l'ID e il separatore `·`, il carattere `▣` davanti a «Verifica», la stringa `Risposta corretta:`, le parole `Caso ragionato` o `Caso guidato`.

È un difetto di verifica, non di scrittura: nessuno aveva eseguito il gate sui capitoli prima di dichiararli fatti.

## Che cosa è stato fatto

Entrambi i capitoli sono stati riorganizzati in cinque nuclei numerati, agganciati agli ID della matrice di copertura, con un blocco `▣ Verifica NN.A · Quiz ragionati` di sei domande a risposta commentata, un blocco `▣ Verifica NN.B · Domande aperte` che conserva le domande già scritte, e un caso guidato per capitolo.

Portare ogni nucleo sopra le 600 parole ha richiesto un **secondo passaggio sulle fonti**, e quel passaggio ha prodotto contenuto verificato che mancava:

- la regola sui tempi di possesso dei requisiti: tutti alla scadenza della domanda, **tranne** il titolo di studio (entro la preselettiva) e l'idoneità psico-fisica, che deve sussistere agli accertamenti e **permanere fino all'immissione in ruolo**;
- il modo in cui è stata abolita la statura: soppressione della parola nell'art. 586 del TUOM, non abrogazione di una tabella;
- il **certificato di idoneità sportiva agonistica**, gli enti abilitati a rilasciarlo, la finestra dei 45 giorni e l'esclusione dal concorso in caso di mancata presentazione;
- la disciplina di **infortunio e differimento**: comunicazione immediata alla commissione a pena di inammissibilità del riesame, differimento concesso una sola volta e non rinnovabile nemmeno per forza maggiore;
- il **troncamento al secondo** del tempo nella corsa e la prevalenza del rilevamento manuale più favorevole in caso di guasto;
- la **vera geometria della prova di acquaticità**: non cinque immersioni ravvicinate ma **una sola apnea di otto metri** che attraversa cinque ostacoli, con obbligo di non emergere, tolleranze esplicite e cause di non superamento;
- la lettura delle voci da cinque punti dell'allegato B: solo le categorie con rimorchio e le due CQC, che presuppongono la patente sottostante.

Esito dei gate dopo il retrofit:

| | Capitolo 02 | Capitolo 04 |
| --- | ---: | ---: |
| parole | 5.889 | 5.865 |
| nuclei (min 600 parole) | 5 | 5 |
| quiz · casi · verifiche | 6 · 1 · 2 | 6 · 1 · 2 |
| gate densità didattica | **passa** | **passa** |
| gate contratto del lettore | **passa** | **passa** |

## Ricadute fuori dai capitoli

**Sulla numerazione.** Il capitolo delle prove d'esame era ancora numerato `05`, retaggio della struttura intermedia a tredici sezioni. Rinominato in `04`, con `outline_section` e `id` allineati.

**Sulla source note.** La rilettura integrale degli articoli 6-8 ha corretto un'omissione della nota di fonte: la preselettiva ha **quattro** tipologie di quesiti, non tre. La quarta — uso delle apparecchiature e delle applicazioni informatiche più diffuse **e lingua inglese** — era stata persa. È stato inoltre chiarito che la data del 15 settembre 2026 riguarda la comunicazione delle *modalità* della prova, non la prova, e che il punteggio della preselettiva **non concorre al voto finale di merito**.

**Sulla matrice.** I nuclei passano da ventuno a ventitré: la Prova 1 e le Prove 2-3 hanno protocolli troppo diversi per stare in un nucleo solo, e la lettura dei gradienti è diventata un nucleo autonomo. Dieci nuclei passano a `completo`; tredici restano `mancante`. Il modulo resta non pubblicabile e il gate `coverage` resta correttamente bloccato.

## Che cosa vale per gli altri moduli

I capitoli di M-SP01, M-SP03 e M-SP04 non sono ancora stati scritti. Vanno scritti **dentro** la struttura del formato 2 fin dalla prima riga, non adattati dopo: heading di nucleo con ID e separatore `·`, sezioni «Obiettivo del capitolo» e «Mappa BANDO del capitolo», blocco `▣ Verifica` con sei quiz commentati, un caso guidato, `draft_stage` e `last_compiled_from` nel frontmatter.

E vanno misurati con il gate prima di dichiararli fatti. Il criterio delle 3.000 parole, discusso a lungo sui capitoli pilota, è l'ultimo dei sei che il gate applica — e da solo non dice quasi nulla.
