# Piano di completamento — Capitolo 02

## Target

`chapters/02-informatica-specialistica-oltre-vol-01.md`

## Esito della ricognizione

Il capitolo contiene soltanto frontmatter, titolo e specifica della struttura madre. Nessun nucleo è ancora completo. La matrice assegna al capitolo la riga «Informatica specialistica — architetture e sistemi», con copertura teorica da sviluppare, applicazione mediante checklist, output per quiz e orale e verifica tramite quiz.

Il VOL-01 copre già informatica di base, distinzione hardware/software/dati, bit e byte, CPU, RAM, ROM, memoria di massa, periferiche e funzioni essenziali del sistema operativo. Il capitolo 2 deve quindi partire da queste conoscenze senza rispiegarle in forma elementare e sviluppare il livello richiesto a un funzionario ICT.

## Collegamento riga per riga alla matrice

| Campo della matrice | Presa in carico nel piano |
| --- | --- |
| Famiglia/profilo: Funzionario ICT | Apertura e casi calibrati sul ragionamento tecnico richiesto al funzionario ICT, senza estendere automaticamente il livello a tutti i profili del volume. |
| Materia: Informatica specialistica | Perimetro esplicito del delta rispetto al VOL-01 e raccordo con i successivi capitoli specialistici. |
| Concetto: architetture e sistemi | Architettura funzionale, esecuzione delle istruzioni, rappresentazione dei dati, gerarchia di memoria, I/O, prestazioni e ruolo del sistema operativo. |
| Frequenza/peso: da validare | Nessuna dichiarazione quantitativa; priorità presentate come scelta didattica da verificare sui bandi. |
| Fonte consolidata: dossier M-TR01 | Dossier usato per il perimetro editoriale, non come fonte tecnica o normativa autosufficiente. |
| Collocazione: capitolo 02 | Tutti i nuclei sotto elencati restano nel capitolo 2; programmazione, reti, cloud e cyber sono soltanto raccordi. |
| Copertura teorica: da sviluppare | Ogni nucleo riceve definizione, funzione, componenti, distinzioni, conseguenze e limite di approfondimento. |
| Applicazione: checklist | Output principale: checklist diagnostica delle competenze specialistiche, compilabile e collegata ai nuclei. |
| Output concorsuale: quiz e orale | Quiz ragionati, domande da commissario e spiegazioni brevi causa-effetto. |
| Verifica: quiz | Batteria finale breve con soluzione motivata; non risultano quiz consolidati già collegati, quindi vanno redatti e revisionati. |
| Stato: parziale | Lo step 09 dovrà produrre il testo completo; lo stato potrà cambiare solo dopo riscontro nel capitolo. |
| Review: fonti tecniche | Necessaria validazione umana delle fonti tecniche e delle semplificazioni su prestazioni e architetture. |

## Nuclei assegnati

1. Confine tra informatica di base del VOL-01 e informatica specialistica del VOL-08.
2. Modello funzionale di un elaboratore: CPU, memoria, bus e dispositivi di I/O come sistema coordinato.
3. Ciclo di esecuzione delle istruzioni e ruoli essenziali di unità di controllo, ALU e registri.
4. Rappresentazione digitale: binario, interi, caratteri e cenni alla rappresentazione dei reali; relazione tra codifica, intervallo, precisione ed errore.
5. Gerarchia di memoria: registri, cache, RAM e memoria persistente; località e compromesso capacità-latenza-costo.
6. I/O, interrupt, buffering e trasferimento dei dati a livello concettuale.
7. Prestazioni: tempo di risposta, throughput, latenza, colli di bottiglia, parallelismo e limiti dei confronti basati su un solo parametro.
8. Ruolo del sistema operativo nella gestione di processi, memoria, file, dispositivi e protezione, senza duplicare l’uso operativo di file e cartelle.
9. Metodo per riconoscere il livello specialistico richiesto dal bando.
10. Checklist finale delle competenze.

## Nuclei già completi

Nessuno nel capitolo. Nel VOL-01 sono già disponibili i prerequisiti seguenti, ai quali si può rinviare in modo puntuale:

- capitolo 10, § 1, per hardware, software, dati, bit/byte, CPU, RAM, ROM, storage e periferiche;
- capitolo 10, § 2, per funzioni di base del sistema operativo, file e cartelle.

Il rinvio serve come prerequisito, non come prova della copertura specialistica assegnata al capitolo 2.

## Nuclei da sviluppare

- spiegazione integrata dei componenti, oltre il semplice riconoscimento nominale;
- passaggio dal codice binario ai problemi di intervallo, precisione e rappresentazione;
- gerarchia di memoria e principio di località;
- interazione CPU-memoria-I/O e ruolo degli interrupt;
- lettura corretta delle prestazioni e individuazione del collo di bottiglia;
- funzioni del sistema operativo viste come gestione e astrazione delle risorse;
- applicazione dei concetti a quiz, orale e diagnosi di configurazioni;
- checklist che distingua «conosco il termine», «so spiegarne la funzione» e «so applicarlo».

## Sezioni da conservare

- frontmatter e identificativi del capitolo;
- H1 esistente;
- sezione «Specifica struttura madre» come vincolo redazionale;
- collegamento al dossier M-TR01;
- output previsto: checklist delle competenze.

La specifica potrà essere mantenuta come nota editoriale durante la lavorazione e rimossa dal testo destinato al lettore soltanto secondo il normale workflow di compilazione.

## Duplicazioni da evitare

- classificazioni elementari hardware/software e input/output;
- definizioni isolate di bit, byte, CPU, RAM, ROM, SSD e HDD;
- operazioni pratiche su file, cartelle, finestre ed estensioni;
- Office, web, posta elettronica, CAD e competenze digitali comuni;
- algoritmi, pseudocodice e strutture dati, assegnati al capitolo 3;
- protocolli, servizi di rete e troubleshooting, assegnati al capitolo 5;
- virtualizzazione, container e DevOps, assegnati al capitolo 7;
- cybersecurity, IAM e incident response, assegnati ai capitoli 8 e 9.

## Esempi, casi, domande ed esercizi necessari

- esempio guidato del percorso di un dato da input a memoria, elaborazione e output;
- confronto ragionato tra registro, cache, RAM e storage;
- caso di prestazioni nel quale l’aumento della frequenza della CPU non elimina il collo di bottiglia di I/O;
- esempio di overflow o perdita di precisione, senza trasformare il capitolo in un corso di matematica discreta;
- domanda da commissario sul ciclo di esecuzione di un’istruzione;
- domanda-trappola che distingua capacità, latenza e throughput;
- mini-esercizio di ordinamento della gerarchia di memoria;
- quiz con distrattori basati sulle confusioni CPU/memoria, cache/RAM e latenza/throughput;
- checklist finale a tre livelli: riconoscere, spiegare, applicare.

## Fonti da usare

### Fonti e pagine già consolidate

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — per perimetro e collocazione editoriale, non per i claim tecnici;
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]] — prerequisiti e confine con il VOL-01;
- [[topics/hardware-e-architettura-pc]];
- [[topics/informatica]];
- [[topics/sistemi-operativi-e-gestione-file]];
- [[sources/informatica-operativa-office-sistemi-hardware]];
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]].

### Fonti tecniche da consolidare prima o durante lo step 09

- manuale universitario o documentazione didattica istituzionale sull’architettura degli elaboratori;
- documentazione autorevole sulla rappresentazione dei dati e sullo standard IEEE 754, limitatamente ai concetti effettivamente trattati;
- documentazione tecnica ufficiale sulle funzioni dei sistemi operativi e sulle metriche di prestazione;
- bandi ufficiali del campione VOL-08 per verificare terminologia, profondità e peso dei nuclei.

Non usare il dossier editoriale come unica fonte di fatti tecnici. Non risultano entity page o quiz consolidati specificamente collegati al capitolo 2.

## Review umane richieste

- specialista di architettura degli elaboratori: correttezza di ciclo d’istruzione, gerarchia di memoria, I/O e semplificazioni;
- specialista di sistemi operativi: confine tra gestione delle risorse e nozioni operative di base;
- responsabile editoriale: rispetto del delta VOL-01/VOL-08 e assenza di duplicazioni con i capitoli 3, 5 e 7;
- revisore didattico: coerenza fra teoria, checklist, quiz e orale;
- responsabile del campione bandi: validazione di peso, terminologia e profondità concorsuale;
- revisore fonti: acquisizione e tracciabilità delle fonti tecniche mancanti.

## Struttura proposta e budget KDP

# Informatica specialistica: cosa serve oltre il VOL-01

## Apertura: dal riconoscere i componenti al ragionare sul sistema — 120 parole

## Obiettivo e confine con il VOL-01 — 160 parole

### Prerequisiti già coperti

### Il delta richiesto al funzionario ICT

## Mappa BANDO dell’informatica specialistica — 180 parole

### Nuclei, profondità e output

## L’elaboratore come sistema — 300 parole

### CPU, registri, unità di controllo e ALU

### Bus, memoria e dispositivi di I/O

### Il ciclo di esecuzione di un’istruzione

## Rappresentare dati e istruzioni — 260 parole

### Binario, intervallo e codifica

### Caratteri, interi e numeri reali

### Precisione, arrotondamento e overflow

## La gerarchia di memoria — 260 parole

### Registri, cache, RAM e memoria persistente

### Località e compromesso capacità-latenza-costo

## Input/output e gestione degli eventi — 180 parole

### Interrupt, buffering e trasferimento

## Capire le prestazioni — 260 parole

### Latenza, throughput e tempo di risposta

### Colli di bottiglia, parallelismo e confronti ingannevoli

## Il sistema operativo come gestore delle risorse — 240 parole

### Processi e memoria

### File, dispositivi e protezione

### Confine con reti, cloud e cybersecurity

## Caso guidato: diagnosticare un sistema lento — 180 parole

## Domanda da commissario e domanda-trappola — 120 parole

## Errore tipico — 70 parole

## Checklist delle competenze specialistiche — 180 parole più tabella compilabile

## Mini-esercizi e quiz ragionati — 180 parole

## Da sapere in cinque righe — 60 parole

## Riferimenti consolidati e note di review — 60 parole

Budget orientativo: 2.500–2.800 parole, tabelle e checklist incluse. Il budget mantiene il capitolo autosufficiente sul delta specialistico senza assorbire i contenuti dei capitoli successivi.

## Criteri di approvabilità per lo step 09

- ogni nucleo della riga di matrice compare nella struttura e ha un output verificabile;
- il rinvio al VOL-01 indica sezioni precise e non sostituisce il delta specialistico;
- nessuna frequenza è presentata come dato statistico finché non è validata;
- le fonti tecniche mancanti sono consolidate prima di introdurre claim specialistici;
- checklist, quiz e domande verificano gli stessi concetti sviluppati nella teoria;
- le review umane restano esplicite finché non vengono realmente eseguite.
