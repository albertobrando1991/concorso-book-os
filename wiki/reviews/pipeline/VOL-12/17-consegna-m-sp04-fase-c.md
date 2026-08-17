---
id: vol-12-consegna-m-sp04-fase-c
type: pipeline_review
title: 'VOL-12 - Consegna M-SP04 fase C'
status: complete
volume_id: VOL-12
module_code: M-SP04
updated_at: 2026-08-13T19:00:00+02:00
created_at: 2026-08-13T19:00:00+02:00
review_required: true
canonical: true
tags: ['vol-12', 'm-sp04', 'fase-c', 'consegna']
---

# VOL-12 - Consegna M-SP04 fase C

## Esito

Fase C completata. La matrice è stata sincronizzata con la source note, i tre punti sostanziali aperti sono stati risolti e il modulo è stato redatto in sette capitoli sostenibili nel formato 2. La riduzione dai nove titoli nominali deriva da due accorpamenti imposti dalla soglia dei cinque nuclei reali, non da una rinuncia di copertura.

Nessun blocco reale resta aperto. Il file pipeline/VOL-12/run-state.json non è stato modificato.

## Chiusura dei tre punti aperti

1. **d.P.R. 18/1967.** Letti e consolidati gli articoli 99-110-bis nel testo vigente: servizio delle relazioni con l'estero, accesso esclusivo per concorso, ruolo speciale unitario, gradi, funzioni centrali e all'estero, formazione iniziale di nove mesi, formazione continua, progressione non automatica, durata generale degli incarichi e rientro presso l'amministrazione centrale. Prima sede, calendario individuale e progressione personale restano correttamente dichiarati ignoti.
2. **Prova attitudinale diplomatica.** Verificato l'articolo 7: 50 quesiti in 60 minuti; storia delle relazioni internazionali dal Congresso di Vienna, diritto internazionale e UE, economia e cooperazione multilaterale, inglese senza dizionario e logica; +1 risposta corretta, -0,25 errata, 0 omessa; soglia del 60 per cento; punteggio escluso dalla graduatoria finale; gestione automatizzata.
3. **Rinvio al VOL-01.** Verificata l'esistenza e la destinazione del capitolo *Banca dati ufficiale: studiarla senza memorizzare male*. Il delta M-SP04 è esplicito: il protocollo del set chiuso si attiva soltanto dopo la pubblicazione effettiva di una banca ufficiale e dopo il controllo di autenticità, versione, perimetro e rettifiche.

## Gate capitolo per capitolo

Esecuzione effettuata sui file finali con runDidacticDensityGate e runChapterLintGate, richiedendo il formato 2. Tutti i blocker e tutti i warning restituiti dall'ultima esecuzione sono vuoti.

| Cap. | File | Nuclei | Parole corpo | Quiz | Casi | didactic-density | chapter-lint |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| 01 | 01-mappa-scelta-bando-decoder.md | 5 | 4.055 | 6 | 1 | PASS | PASS |
| 02 | 02-carriera-prefettizia-prove-materie-ordinamento.md | 5 | 3.911 | 6 | 2 | PASS | PASS |
| 03 | 03-carriera-diplomatica-prove-materie-ordinamento.md | 7 | 5.120 | 7 | 2 | PASS | PASS |
| 04 | 04-le-lingue-straniere.md | 5 | 3.781 | 6 | 2 | PASS | PASS |
| 05 | 05-prova-orale-postura-professionale.md | 5 | 3.762 | 6 | 2 | PASS | PASS |
| 06 | 06-piano-preparazione-tentativi.md | 5 | 3.737 | 6 | 2 | PASS | PASS |
| 07 | 07-errori-casi-checklist.md | 5 | 3.808 | 6 | 4 | PASS | PASS |

Totale del corpo dei sette capitoli: **28.174 parole**. Totale nuclei: **37**. Ogni capitolo contiene almeno cinque nuclei, almeno sei quiz con soluzione, almeno un caso e una sezione di verifica. Il gate di densità conferma il rispetto della soglia per tutti i nuclei.

## Stato finale della matrice

La matrice finale assegna ciascun nucleo al capitolo e alla relativa sezione, con copertura teorica, applicazione, output e verifica.

- completo: **37**
- parziale: **0**
- solo-nominato: **0**
- rinviato: **0**
- mancante: **0**
- totale nuclei: **37**
- copertura: **100%**

Il precedente stato disallineato è stato rimosso: i nuclei già verificati nella source note non risultano più bloccati; il rinvio al VOL-01 è stato verificato e trattato nel capitolo, quindi il nucleo è completo; l'assenza di un livello QCER ufficiale è un'incognita esplicita, non una lacuna da riempire.

## Incognite dichiarate nei capitoli

### Capitolo 01

- Posti e riserve sono dati mobili della tornata esaminata.
- La futura banca prefettizia non è pubblicata: restano ignoti file, numero e distribuzione dei quesiti e possibili rettifiche.
- Il limite diplomatico dei quattro scritti completati va ricontrollato nella nuova tornata e ricostruito documentalmente sul candidato.

### Capitolo 02

- Età, elevazioni, categorie, formati, durate, materiali e soglie vanno ricontrollati sul nuovo bando.
- Contenuto e ampiezza della futura raccolta prefettizia dei quesiti non sono noti.
- Nessuna distribuzione per argomento o copertura integrale della banca viene promessa prima della pubblicazione.

### Capitolo 03

- Non è disponibile una probabilità personale di riuscita ricavabile da posti e tentativi.
- Per una tornata futura non sono noti banca dei quesiti, distribuzione effettiva fra aree, ordine e interfaccia.
- Non sono fissati numero universale di parole, struttura obbligatoria degli elaborati o tastiera futura.
- Il programma non fornisce manuale ufficiale, numero di pagine o indice esaustivo dei sottoargomenti.
- Non esiste un livello QCER formale dichiarato.
- Restano ignoti durata delle singole risposte orali, tema di attualità, applicativi, domande e sequenza della commissione.
- L'ordinamento non consente di prevedere prima sede, calendario individuale delle assegnazioni, grado raggiunto o durata personale della carriera.

### Capitolo 04

- Non sono anticipabili testo, quesito, lessico, interlocuzione o standard QCER della commissione.
- Una diagnosi interna non predice il voto ufficiale.
- Non è possibile stabilire quale lingua sia in astratto più facile o premiata.
- Le fonti non fissano lunghezza ideale, velocità di eloquio o numero di consultazioni del vocabolario.
- Non esiste una quantità universale di ore che garantisca il livello.

### Capitolo 05

- Non sono noti domande, ordine, durata delle componenti e composizione futura della commissione.
- La struttura didattica della risposta e le durate di allenamento non sono prescrizioni ufficiali.
- Tema di attualità, strumenti informatici, lingua delle domande e collegamenti richiesti restano ignoti.
- Non esiste un modello estetico ufficiale del candidato.
- Le griglie e i punteggi interni non replicano né predicono il giudizio della commissione.

### Capitolo 06

- Le fonti non indicano ore o mesi necessari al superamento; sei-dodici mesi è un minimo operativo condizionato.
- Durata delle fasi e struttura della settimana non sono universali.
- Il voto di simulazione non predice l'esito ufficiale.
- Non sono prevedibili numero, date e posti delle tornate future.
- Gli scenari temporali restano ipotesi da aggiornare con fonti e prestazioni.

### Capitolo 07

- I dati mobili possono cambiare nella futura tornata.
- Le fonti non stabiliscono numero ideale di simulazioni o distribuzione personale delle ore.
- Non esiste una probabilità individuale ufficiale di successo.
- Non sono disponibili in anticipo banca prefettizia futura, calendario e istruzioni non pubblicati.
- Non sono anticipabili imprevisti di sede, tracce o istruzioni operative.

## Accorpamenti e sintomo

### Bando Decoder nel capitolo 01

**Sintomo:** N-SP04-10-01 esauriva i contenuti disponibili in requisiti, scelta del binario, sequenza delle prove, comunicazioni, dati mobili e rinvio alla banca ufficiale. Tenuto autonomo, avrebbe duplicato i capitoli 01-03 e non avrebbe prodotto cinque nuclei distinti da almeno 600 parole.

**Esito:** il nucleo resta separato e verificabile nella matrice, ma confluisce in *Mappa, scelta del binario e Bando Decoder*.

### Errori e casi con checklist nel capitolo 07

**Sintomo:** il gruppo errori-casi e il gruppo checklist, considerati separatamente, esaurivano ciascuno la fonte sotto la soglia dei cinque nuclei. Mantenerli autonomi avrebbe richiesto elenchi diagnostici riprodotti o prosa di riempimento.

**Esito:** l'accorpamento produce cinque protocolli reali: errori di fonte-data-binario; errori di sequenza-soglia-formato; errori decisionali e rischio biografico; checklist candidatura-aggiornamento; checklist prova-debrief.

## File finali

- source note aggiornata: wiki/sources/bandi-carriera-prefettizia-e-diplomatica-m-sp04.md
- piano editoriale aggiornato: wiki/books/moduli/m-sp04-prefettizia-diplomatica/planning/00-piano-editoriale.md
- matrice finale: wiki/books/moduli/m-sp04-prefettizia-diplomatica/planning/02-matrice-copertura-didattica.md
- indice del modulo aggiornato: wiki/books/moduli/m-sp04-prefettizia-diplomatica/index.md
- capitoli: wiki/books/moduli/m-sp04-prefettizia-diplomatica/chapters/01-*.md fino a 07-*.md

Nessun commit e nessun push sono stati eseguiti.
