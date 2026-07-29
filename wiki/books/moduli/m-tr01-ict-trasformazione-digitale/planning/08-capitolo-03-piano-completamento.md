# Piano di completamento — Capitolo 03

## Target

`chapters/03-programmazione-algoritmi-strutture-dati.md`

## Esito della ricognizione

Il capitolo contiene frontmatter, titolo e specifica della struttura madre, ma non ancora il testo destinato al lettore. Nessun nucleo assegnato è completo.

La matrice assegna al capitolo la riga «Programmazione — algoritmi e strutture dati», con teoria da sviluppare, pseudocodice come applicazione, esercizio tecnico come output e verifica tramite esercizio. La specifica estende il perimetro a paradigmi, tipi, strutture di controllo, funzioni, ricerca, ordinamento e complessità.

Il VOL-01, capitolo 10, § 8, definisce già programma, linguaggio, algoritmo, variabile, funzione, condizione, ciclo, compilatore e interprete a livello introduttivo. Il capitolo 3 deve usare questi concetti come prerequisiti e portarli al livello richiesto a un funzionario ICT.

## Collegamento riga per riga alla matrice

| Campo della matrice | Presa in carico nel piano |
| --- | --- |
| Famiglia/profilo: Funzionario ICT | Teoria, pseudocodice e casi calibrati su comprensione, progettazione e analisi di soluzioni semplici. |
| Materia: Programmazione | Confine esplicito tra nozioni introduttive del VOL-01 e ragionamento algoritmico specialistico. |
| Concetto: algoritmi e strutture dati | Proprietà degli algoritmi, pseudocodice, tipi, controllo, funzioni, strutture lineari e associative, ricerca, ordinamento e complessità. |
| Frequenza/peso: da validare | Nessuna frequenza quantitativa; profondità e linguaggi specifici restano dipendenti dal singolo bando. |
| Fonte consolidata: dossier M-TR01 | Il dossier stabilisce perimetro e collocazione, ma non è fonte tecnica autosufficiente. |
| Collocazione: capitolo 03 | Tutti i nuclei elencati restano nel capitolo 3; database, API e AI sono soltanto raccordi. |
| Copertura teorica: da sviluppare | Ogni nucleo avrà definizione, funzione, elementi, distinzioni, conseguenze ed esempio. |
| Applicazione: pseudocodice | Esempi neutrali rispetto al linguaggio, lettura passo-passo e tracciamento dello stato. |
| Output: esercizio tecnico | Progettazione, completamento o correzione di un algoritmo breve. |
| Verifica: esercizio | Trace table, domanda orale, quiz, errore tipico ed esercizio con soluzione motivata. |
| Stato: parziale | Lo stato potrà diventare completo solo dopo riscontro della teoria e delle verifiche nel testo reale. |
| Review: fonti tecniche | Necessarie fonti primarie per linguaggi, strutture dati e analisi della complessità, oltre a revisione specialistica. |

## Nuclei assegnati

1. Confine fra programmazione introduttiva del VOL-01 e livello specialistico del VOL-08.
2. Problema, algoritmo, programma e implementazione: relazioni e differenze.
3. Proprietà di un algoritmo: input, output, finitezza, determinatezza ed efficacia operativa.
4. Pseudocodice e tracciamento dello stato.
5. Paradigmi principali, limitati alla funzione didattica: imperativo/procedurale, orientato agli oggetti, funzionale e dichiarativo.
6. Valori, variabili, costanti, tipi, espressioni, assegnazione e conversioni.
7. Strutture di controllo: sequenza, selezione e iterazione.
8. Funzioni e procedure: parametri, valore restituito, ambito e cenni alla ricorsione.
9. Strutture dati: array, liste, pile, code, insiemi, mappe/dizionari, alberi e grafi a livello concettuale.
10. Scelta della struttura in funzione delle operazioni richieste.
11. Ricerca lineare e binaria, con prerequisito dell’ordinamento per la ricerca binaria.
12. Ordinamento: almeno un metodo semplice e un metodo più efficiente per mostrare il compromesso.
13. Complessità temporale e spaziale; crescita asintotica e notazione O grande a livello concorsuale.
14. Correttezza, casi limite, test e debug del pseudocodice.
15. Produzione di pseudocodice, quiz, risposta orale ed esercizio tecnico.

## Nuclei già completi

Nessuno nel capitolo 3.

Sono già completi nel VOL-01, capitolo 10, § 8, i prerequisiti introduttivi:

- definizione generale di programma e linguaggio;
- definizione di algoritmo e sue proprietà essenziali;
- significato elementare di variabile, costante, funzione, condizione e ciclo;
- distinzione introduttiva fra compilatore e interprete;
- distinzione fra linguaggi di programmazione e linguaggi di marcatura.

Il rinvio è valido come prerequisito, ma non copre pseudocodice, strutture dati, ricerca, ordinamento o complessità.

## Nuclei da sviluppare

- trasformazione di un problema in input, vincoli, passi e output;
- lettura ed esecuzione manuale di pseudocodice;
- scelta del tipo e della struttura dati;
- distinzione fra parametro, argomento, variabile locale e valore restituito;
- uso motivato di selezione e iterazione;
- confronto fra strutture sulla base delle operazioni;
- ricerca lineare rispetto alla ricerca binaria;
- ordinamenti semplici rispetto a strategie più efficienti;
- differenza fra correttezza e prestazione;
- complessità temporale e spaziale senza ridurla a una formula da memorizzare;
- test di casi ordinari, limite ed errore;
- esposizione orale di una soluzione algoritmica.

## Sezioni da conservare

- frontmatter e identificativi;
- H1 esistente;
- specifica della struttura madre come vincolo editoriale durante la lavorazione;
- collegamento al dossier M-TR01;
- output previsti: pseudocodice, quiz ed errori tipici.

## Duplicazioni da evitare

- definizioni elementari già complete nel VOL-01, salvo richiamo sintetico;
- architettura, memoria e ciclo d’istruzione, sviluppati nel capitolo 2;
- modelli, tabelle, chiavi, SQL e transazioni, assegnati al capitolo 4;
- protocolli e troubleshooting di rete, assegnati al capitolo 5;
- ciclo di vita del software, test di sistema, API e interoperabilità, assegnati al capitolo 6;
- pipeline CI/CD, container e automazione DevOps, assegnati al capitolo 7;
- algoritmi di machine learning, rischi e compliance, assegnati al capitolo 11;
- esempi lunghi legati a una sintassi proprietaria quando il bando non richiede uno specifico linguaggio.

## Esempi, casi, domande ed esercizi necessari

- algoritmo per validare e classificare una lista di pratiche;
- trace table di un ciclo con accumulatore e condizione;
- confronto array/lista per accesso, inserimento e cancellazione;
- pila per annullare operazioni e coda per gestire richieste;
- mappa per associare identificativo e stato di una pratica;
- ricerca lineare in una raccolta non ordinata;
- ricerca binaria in una raccolta ordinata, con verifica del prerequisito;
- confronto didattico fra ordinamento per selezione o inserimento e merge sort;
- caso limite con input vuoto, elemento assente o duplicato;
- domanda da commissario sulla scelta della struttura dati;
- domanda-trappola su ricerca binaria applicata a dati non ordinati;
- esercizio di completamento del pseudocodice;
- esercizio di stima della crescita del numero di operazioni;
- checklist finale «comprendo, traccio, progetto, valuto».

## Fonti da usare

### Fonti e pagine già consolidate

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — per perimetro editoriale;
- [[sources/database-programmazione-formati-concorsi]] — per nuclei introduttivi e documentazione tecnica già acquisita;
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[topics/programmazione-e-linguaggi]];
- [[topics/informatica]];
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, § 8;
- documentazione Python già censita nella source note, soltanto per esempi e concetti trasferibili.

### Fonti tecniche da consolidare prima o durante lo step 09

- documentazione ufficiale di un linguaggio per tipi, controllo, funzioni e strutture dati fondamentali;
- testo o materiale universitario autorevole su algoritmi e strutture dati;
- riferimento tecnico primario o accademico per notazione asintotica e complessità;
- fonte didattica verificabile per ricerca e ordinamento;
- bandi ufficiali del campione VOL-08 per validare profondità, linguaggi e output richiesti.

Non risultano entity page o quiz consolidati specificamente collegati al capitolo 3. Gli esercizi nuovi dovranno essere revisionati prima della pubblicazione.

## Review umane richieste

- specialista di algoritmi e strutture dati: correttezza di pseudocodice, ricerca, ordinamento e complessità;
- sviluppatore o docente: chiarezza di tipi, controllo, funzioni e paradigmi;
- responsabile editoriale: rispetto del delta con VOL-01 e dei confini con i capitoli 2, 4 e 6;
- revisore didattico: coerenza tra teoria, trace table, esercizi, quiz e orale;
- responsabile del campione bandi: validazione di terminologia e profondità concorsuale;
- revisore fonti: acquisizione e tracciabilità delle fonti tecniche mancanti.

## Struttura proposta e budget KDP

# Programmazione, algoritmi e strutture dati

## Apertura: leggere una soluzione, non soltanto il codice — 120 parole

## Obiettivo e confine con il VOL-01 — 150 parole

### Prerequisiti già coperti

### Il delta specialistico

## Mappa BANDO della programmazione — 180 parole

### Nuclei, profondità e output

## Dal problema all’algoritmo — 260 parole

### Input, vincoli e output

### Correttezza, finitezza e casi limite

## Pseudocodice e tracciamento — 320 parole

### Convenzioni minime

### Trace table

### Errori di logica

## Paradigmi di programmazione — 220 parole

### Imperativo e procedurale

### Orientato agli oggetti, funzionale e dichiarativo

## Tipi, espressioni e controllo — 340 parole

### Valori, variabili, costanti e conversioni

### Sequenza, selezione e iterazione

## Funzioni e procedure — 260 parole

### Parametri, argomenti e valore restituito

### Ambito e ricorsione

## Strutture dati e operazioni — 440 parole

### Array e liste

### Pile e code

### Insiemi e mappe

### Alberi e grafi

## Ricerca e ordinamento — 420 parole

### Ricerca lineare e binaria

### Ordinamenti semplici e strategie più efficienti

## Capire la complessità — 300 parole

### Tempo, spazio e dimensione dell’input

### Notazione O grande e crescita

## Caso guidato: classificare le pratiche — 200 parole

## Domanda da commissario e domanda-trappola — 140 parole

## Errore tipico — 70 parole

## Mini-esercizi, quiz e trace table — 260 parole

## Checklist finale — 150 parole più tabella

## Da sapere in cinque righe — 60 parole

## Riferimenti consolidati e note di review — 80 parole

Budget orientativo: 3.400–3.700 parole, pseudocodice, tabelle ed esercizi inclusi. Il budget riflette la densità del nucleo senza anticipare basi dati, ingegneria software o AI.

## Criteri di approvabilità per lo step 09

- ogni elemento della specifica e della riga di matrice riceve teoria e verifica;
- il rinvio al VOL-01 resta preciso e limitato ai prerequisiti;
- pseudocodice ed esercizi applicano concetti già spiegati;
- ricerca binaria dichiara il prerequisito dell’ordinamento;
- la complessità è collegata alla dimensione dell’input e non trattata come etichetta isolata;
- gli esempi restano neutrali rispetto al linguaggio, salvo esigenze del bando;
- le fonti tecniche mancanti sono consolidate prima di introdurre claim specialistici;
- le review umane restano aperte finché non vengono realmente eseguite.
