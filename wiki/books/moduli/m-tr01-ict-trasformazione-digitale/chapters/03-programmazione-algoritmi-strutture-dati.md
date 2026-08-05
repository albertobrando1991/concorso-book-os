---
id: chapter-m-tr01-03
type: book_chapter
title: "Programmazione, algoritmi e strutture dati"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["programmazione", "algoritmi", "strutture dati", "complessità"]
entities: []
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/database-programmazione-formati-concorsi", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/programmazione-algoritmi-strutture-dati-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.78
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: false
canonical: true
tags: ["chapter", "m-tr01", "programmazione", "algoritmi"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 3
draft_stage: cross-reviewed
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/database-programmazione-formati-concorsi", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/programmazione-algoritmi-strutture-dati-fonti-tecniche", "topics/programmazione-e-linguaggi", "topics/informatica", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-03-piano-completamento"]
---

# Programmazione, algoritmi e strutture dati

Nelle prove tecniche, conoscere una parola chiave non è sufficiente. Può essere necessario leggere un algoritmo, seguirne l’esecuzione, trovare un errore, scegliere una struttura dati o spiegare perché una soluzione rallenta al crescere dell’input.

La sintassi varia da un linguaggio all’altro, mentre il metodo resta sostanzialmente lo stesso: definire il problema, rappresentare i dati, ordinare i passi, controllare i casi limite e valutare il costo della soluzione. Il capitolo adotta quindi soprattutto lo pseudocodice.

## Obiettivo e confine con il VOL-01

Il VOL-01, capitolo 10, § 8, definisce programma, linguaggio, algoritmo, variabile, funzione, condizione e ciclo. Presenta inoltre compilatore, interprete e linguaggi di marcatura. Questi sono i prerequisiti.

Questo capitolo sviluppa quei prerequisiti. Al termine dovrai saper:

- trasformare un problema in input, vincoli e output;
- leggere e scrivere pseudocodice;
- scegliere tipi e strutture dati coerenti con le operazioni;
- usare selezione, iterazione e funzioni;
- confrontare ricerca lineare e binaria;
- spiegare due strategie di ordinamento;
- stimare tempo e spazio al crescere dell’input;
- verificare correttezza e casi limite.

Le basi dati sono trattate nel capitolo 4; ciclo di vita, test di sistema e API nel capitolo 6; algoritmi di machine learning nel capitolo 11.

## Mappa BANDO della programmazione

| Passaggio | Domanda da porsi | Azione |
| --- | --- | --- |
| **B — Bando** | Sono richiesti concetti, pseudocodice o un linguaggio specifico? | Separare il nucleo comune dalle sintassi nominate. |
| **A — Aree** | La richiesta riguarda controllo, funzioni, strutture, algoritmi o complessità? | Collocare ogni voce nell’area corretta. |
| **N — Nuclei** | Quali operazioni devo saper spiegare o eseguire? | Preparare micro-esempi e confronti. |
| **D — Diario** | L’errore dipende da concetto, traccia, caso limite o costo? | Registrare causa e correzione, non solo la risposta. |
| **O — Output** | La prova chiede quiz, orale o esercizio? | Allenare riconoscimento, spiegazione e produzione. |

Se il bando cita Java, Python, C# o un altro linguaggio, occorre aggiungere la sintassi richiesta. Lo pseudocodice non sostituisce quella preparazione; serve a separare la logica dalle regole del linguaggio.

## Dal problema all’algoritmo

Un **problema computazionale** descrive una relazione fra dati in ingresso e risultato atteso. Un’istanza è un caso concreto del problema. “Trovare una pratica dato un identificativo” è il problema; cercare la pratica `A-1042` è un’istanza.

Un **algoritmo** è una procedura finita e non ambigua che, ricevuto un input ammesso, produce l’output previsto. Un **programma** è l’implementazione dell’algoritmo in un linguaggio eseguibile in un determinato ambiente.

Prima di scrivere i passi, chiarisci:

- input e loro formato;
- output atteso;
- vincoli sui dati;
- comportamento sui casi limite;
- criterio con cui giudicare corretta la risposta.

Supponiamo di dover contare le pratiche con stato `DA_VERIFICARE`. L’input è una collezione di pratiche; l’output è un intero non negativo. Il caso della collezione vuota deve restituire zero. Un valore di stato non riconosciuto richiede una regola: ignorarlo, segnalarlo o interrompere l’elaborazione. Senza questa scelta, il problema è incompleto.

### Correttezza e terminazione

Un algoritmo è corretto se produce l’output previsto per tutti gli input ammessi, non soltanto per un esempio favorevole. Deve inoltre terminare: un ciclo che non modifica mai la propria condizione può proseguire indefinitamente.

I test aiutano a trovare errori, ma non dimostrano da soli la correttezza per ogni input possibile. In una prova, conviene motivare la soluzione con un’invariante semplice: una proprietà che resta vera durante l’esecuzione. Nel conteggio delle pratiche, dopo aver esaminato i primi `k` elementi, il contatore deve coincidere con il numero di stati cercati fra quei `k` elementi.

## Pseudocodice e tracciamento

Il **pseudocodice** descrive un algoritmo con istruzioni leggibili e convenzioni dichiarate, senza adottare tutta la sintassi di un linguaggio. Deve essere abbastanza preciso da permettere a un’altra persona di eseguire i passi.

Le convenzioni adottate sono:

- `←` per l’assegnazione;
- `=` per il confronto;
- `SE`, `ALTRIMENTI`, `FINE SE` per la selezione;
- `PER OGNI` e `MENTRE` per i cicli;
- `RESTITUISCI` per l’output di una funzione.

```text
FUNZIONE contaDaVerificare(pratiche)
    conteggio ← 0
    PER OGNI pratica IN pratiche
        SE pratica.stato = "DA_VERIFICARE"
            conteggio ← conteggio + 1
        FINE SE
    FINE PER
    RESTITUISCI conteggio
FINE FUNZIONE
```

La **trace table** registra lo stato dopo ogni iterazione:

| Iterazione | Stato letto | Conteggio |
| --- | --- | --- |
| iniziale | — | 0 |
| 1 | COMPLETA | 0 |
| 2 | DA_VERIFICARE | 1 |
| 3 | DA_VERIFICARE | 2 |
| 4 | ARCHIVIATA | 2 |

Tracciare l’esecuzione fa emergere assegnazioni mancanti, condizioni invertite e limiti errati. È particolarmente utile quando un ciclo usa un indice.

## Paradigmi di programmazione

Un **paradigma** è un modo generale di organizzare il calcolo.

- Nel paradigma **imperativo** il programma modifica uno stato attraverso istruzioni.
- La programmazione **procedurale** organizza tali istruzioni in procedure e funzioni.
- La programmazione **orientata agli oggetti** combina dati e comportamenti in oggetti appartenenti a classi o tipi.
- La programmazione **funzionale** privilegia composizione di funzioni e controllo degli effetti sullo stato.
- La programmazione **dichiarativa** descrive il risultato o le regole, lasciando al sistema parte della scelta del procedimento.

I linguaggi reali possono sostenere più paradigmi. Non è quindi corretto dedurre da un solo esempio che un linguaggio appartenga in modo esclusivo a una categoria.

## Tipi, espressioni e strutture di controllo

Un **valore** è un dato concreto. Una **variabile** associa un nome a un valore o a una posizione che lo contiene. Una **costante** esprime un valore che il programma non dovrebbe modificare nel contesto previsto.

Il **tipo** stabilisce l’insieme dei valori ammessi e le operazioni disponibili. Numeri, valori booleani, caratteri e stringhe hanno comportamenti diversi. Una conversione può essere esplicita o implicita; in entrambi i casi può fallire o perdere informazione.

Un’**espressione** combina valori, variabili e operatori e produce un risultato. L’assegnazione modifica lo stato associando un valore calcolato a una variabile.

### Sequenza, selezione e iterazione

La **sequenza** esegue istruzioni nell’ordine indicato. La **selezione** sceglie un percorso in base a una condizione. L’**iterazione** ripete un blocco.

```text
SE punteggio >= soglia
    esito ← "AMMESSO"
ALTRIMENTI
    esito ← "NON AMMESSO"
FINE SE
```

Un ciclo `PER OGNI` è adatto quando si visita una collezione. Un ciclo `MENTRE` è utile quando il numero di ripetizioni dipende da una condizione:

```text
i ← 0
MENTRE i < lunghezza(pratiche)
    elabora(pratiche[i])
    i ← i + 1
FINE MENTRE
```

L’errore classico è dimenticare `i ← i + 1`, oppure usare `i <= lunghezza(pratiche)` quando gli indici validi terminano prima. Il risultato può essere un ciclo infinito o un accesso fuori limite.

## Funzioni e procedure

Una **funzione** incapsula un calcolo e restituisce un valore. Una **procedura**, nel lessico didattico, esegue un’azione senza che il valore restituito sia il suo scopo principale. I linguaggi adottano terminologie diverse.

I **parametri** compaiono nella definizione; gli **argomenti** sono i valori forniti nella chiamata.

```text
FUNZIONE massimo(a, b)
    SE a >= b
        RESTITUISCI a
    ALTRIMENTI
        RESTITUISCI b
    FINE SE
FINE FUNZIONE
```

L’**ambito** stabilisce dove un nome è visibile. Una variabile locale appartiene alla funzione o al blocco che la dichiara; una variabile condivisa amplia le dipendenze e può rendere più difficile capire chi modifica lo stato.

La **ricorsione** si ha quando una funzione richiama sé stessa su un problema più piccolo. Richiede un caso base che interrompa le chiamate. Senza caso base, o senza avvicinamento a esso, la computazione non termina correttamente.

## Strutture dati e operazioni

Una **struttura dati** organizza valori e relazioni per rendere possibili determinate operazioni. La scelta va rapportata alle esigenze di accesso, ricerca, inserimento, cancellazione, ordine e memoria.

### Array e liste

Un **array** memorizza una sequenza indicizzata. Nel modello più comune consente accesso diretto tramite indice. Inserire un elemento nel mezzo può richiedere lo spostamento di quelli successivi.

Una **lista** rappresenta una sequenza e può essere realizzata in modi diversi. In una lista concatenata, ogni nodo collega il successivo; raggiungere l’elemento in posizione `k` richiede normalmente di attraversare i precedenti. Inserimenti e cancellazioni possono essere convenienti quando il punto è già noto.

Dire che “la lista è più veloce dell’array” non ha senso senza specificare operazione e rappresentazione.

### Pile e code

La **pila** segue la regola LIFO: l’ultimo elemento inserito è il primo rimosso. Operazioni tipiche sono `push`, `pop` e lettura della cima. È utile per annullamento, chiamate di funzione e attraversamenti.

La **coda** segue la regola FIFO: il primo elemento inserito è il primo servito. È adatta a richieste in attesa, messaggi e visite per livelli. Una coda di priorità, invece, estrae secondo una priorità e non secondo il solo ordine di arrivo.

### Insiemi e mappe

Un **insieme** conserva elementi senza duplicati secondo la nozione di uguaglianza adottata. Serve per appartenenza, eliminazione dei duplicati e operazioni insiemistiche.

Una **mappa** o **dizionario** associa chiavi a valori. Può collegare l’identificativo di una pratica al suo stato. Le chiavi devono rispettare i requisiti della rappresentazione scelta; i costi delle operazioni dipendono dall’implementazione, per esempio tabella hash o albero.

### Alberi e grafi

Un **albero** descrive una struttura gerarchica senza cicli nel modello radicato. Ogni nodo, tranne la radice, ha un genitore. Alberi di ricerca e heap aggiungono proprietà specifiche.

Un **grafo** è formato da vertici e archi e rappresenta relazioni più generali: collegamenti fra sistemi, dipendenze o percorsi. Può essere orientato o non orientato, pesato o non pesato. Il capitolo introduce la struttura; gli algoritmi avanzati sui grafi restano fuori perimetro.

## Ricerca

La **ricerca lineare** esamina gli elementi uno dopo l’altro finché trova la chiave o termina la collezione.

```text
FUNZIONE cercaLineare(elementi, chiave)
    PER i DA 0 A lunghezza(elementi) - 1
        SE elementi[i] = chiave
            RESTITUISCI i
        FINE SE
    FINE PER
    RESTITUISCI -1
FINE FUNZIONE
```

Nel caso peggiore visita tutti gli `n` elementi: il tempo cresce linearmente, `O(n)`.

La **ricerca binaria** usa una collezione ordinata e confronta la chiave con l’elemento centrale. A ogni passo elimina circa metà dell’intervallo.

```text
FUNZIONE cercaBinaria(elementi, chiave)
    basso ← 0
    alto ← lunghezza(elementi) - 1
    MENTRE basso <= alto
        medio ← parteIntera((basso + alto) / 2)
        SE elementi[medio] = chiave
            RESTITUISCI medio
        ALTRIMENTI SE elementi[medio] < chiave
            basso ← medio + 1
        ALTRIMENTI
            alto ← medio - 1
        FINE SE
    FINE MENTRE
    RESTITUISCI -1
FINE FUNZIONE
```

Il numero di confronti cresce come `O(log n)`. Applicare questo algoritmo a dati non ordinati rende il risultato inaffidabile: l’ordinamento è un prerequisito, non un dettaglio.

## Ordinamento

L’ordinamento dispone gli elementi secondo una relazione coerente. Due algoritmi possono produrre lo stesso ordine ma avere costi e proprietà differenti.

L’**insertion sort** costruisce una parte ordinata inserendo ogni nuovo elemento nella posizione corretta. È semplice e può funzionare bene su collezioni piccole o quasi ordinate. Nel caso peggiore, confronti e spostamenti crescono quadraticamente: `O(n²)`.

Il **merge sort** divide la collezione, ordina ricorsivamente le parti e le fonde. Il suo tempo cresce come `O(n log n)` nei casi tipicamente analizzati, ma la fusione richiede memoria aggiuntiva nella rappresentazione comune.

L’ordine di crescita è uno dei criteri di scelta. Vanno considerati anche la dimensione, la memoria disponibile, lo stato iniziale dei dati, la stabilità richiesta e il costo effettivo delle operazioni.

## Capire la complessità

La **complessità temporale** descrive come cresce il lavoro al crescere della dimensione `n` dell’input. La **complessità spaziale** descrive la crescita della memoria aggiuntiva.

La notazione **O grande** esprime un limite superiore asintotico. Tralascia costanti e termini di ordine inferiore per mettere in evidenza la crescita dominante. Non misura direttamente i secondi impiegati su una macchina.

| Crescita | Esempio intuitivo |
| --- | --- |
| `O(1)` | accesso diretto a una posizione nota |
| `O(log n)` | ricerca binaria su dati ordinati |
| `O(n)` | scansione completa |
| `O(n log n)` | merge sort |
| `O(n²)` | doppio confronto fra molte coppie |

Se `n` raddoppia, un algoritmo lineare tende a raddoppiare il lavoro dominante; uno quadratico tende a quadruplicarlo. L’analisi va però riferita a un modello e a un’operazione dichiarati.

## Caso guidato: classificare le pratiche

Un ufficio deve separare pratiche complete, incomplete e con stato non riconosciuto. Ogni pratica ha identificativo e stato.

Una soluzione usa tre liste:

```text
complete ← lista vuota
incomplete ← lista vuota
anomalie ← lista vuota

PER OGNI pratica IN pratiche
    SE pratica.stato = "COMPLETA"
        aggiungi pratica A complete
    ALTRIMENTI SE pratica.stato = "INCOMPLETA"
        aggiungi pratica A incomplete
    ALTRIMENTI
        aggiungi pratica A anomalie
    FINE SE
FINE PER
```

L’algoritmo visita ogni pratica una volta, quindi il tempo cresce come `O(n)`. Le tre liste occupano complessivamente spazio proporzionale al numero di pratiche. La categoria `anomalie` evita di perdere silenziosamente dati inattesi.

## Domanda da commissario

**Come sceglie una struttura dati per risolvere un problema?**

Parto dalle operazioni richieste: accesso per posizione, ricerca per chiave, inserimento, cancellazione, mantenimento dell’ordine o gestione FIFO/LIFO. Considero poi dimensione, frequenza delle operazioni, memoria e implementazione disponibile. La scelta va motivata sul carico: una struttura efficace per accessi indicizzati può non esserlo per inserimenti frequenti nel mezzo.

## Domanda-trappola

**La ricerca binaria è sempre preferibile alla ricerca lineare?**

No. Richiede dati ordinati e un accesso compatibile alla posizione centrale. Se la collezione non è ordinata e deve essere cercata una sola volta, il costo dell’ordinamento può superare il beneficio. La ricerca lineare resta inoltre adatta a raccolte piccole o prive di accesso diretto.

## Errore tipico

Associare una complessità alla struttura senza indicare operazione e rappresentazione. “La mappa è O(1)” è incompleto: alcune implementazioni offrono costo medio costante per certe operazioni, altre hanno costi logaritmici, e il caso peggiore può differire.

## Mini-esercizi e quiz

### Esercizio 1

Traccia il valore di `somma`:

```text
somma ← 0
PER OGNI x IN [3, 1, 4]
    somma ← somma + x
FINE PER
```

**Soluzione:** i valori successivi sono 3, 4 e 8. L’output finale è 8.

### Esercizio 2

Quale struttura useresti per servire richieste nell’ordine di arrivo?

**Soluzione:** una coda FIFO. Una pila invertirebbe l’ordine; una coda di priorità seguirebbe un criterio diverso dall’arrivo.

### Quiz

Quale affermazione è corretta?

- A. La ricerca binaria funziona correttamente su qualunque sequenza.
- B. Merge sort ha crescita quadratica in ogni caso.
- C. Una funzione ricorsiva richiede un caso base raggiungibile.
- D. Un insieme conserva necessariamente duplicati e ordine di inserimento.

**Risposta corretta: C.** A ignora l’ordinamento, B attribuisce una crescita errata, D contraddice la funzione dell’insieme.

## Checklist finale

| Competenza | Riconosco | Spiego | Applico |
| --- | --- | --- | --- |
| Distinguere problema, algoritmo e programma | ☐ | ☐ | ☐ |
| Tracciare pseudocodice | ☐ | ☐ | ☐ |
| Usare selezione e iterazione | ☐ | ☐ | ☐ |
| Spiegare parametri, ambito e ricorsione | ☐ | ☐ | ☐ |
| Scegliere una struttura dati | ☐ | ☐ | ☐ |
| Confrontare ricerca lineare e binaria | ☐ | ☐ | ☐ |
| Confrontare insertion sort e merge sort | ☐ | ☐ | ☐ |
| Stimare tempo e spazio | ☐ | ☐ | ☐ |
| Individuare casi limite | ☐ | ☐ | ☐ |

## Da sapere in 5 righe

- Un algoritmo collega input, vincoli, passi e output.
- Lo pseudocodice rende verificabile la logica senza imporre una sintassi.
- La struttura dati si sceglie in base alle operazioni.
- Ricerca binaria e complessità richiedono prerequisiti e modello dichiarati.
- Test, trace table e casi limite riducono gli errori di ragionamento.

## Riferimenti consolidati

- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, § 8;
- [[topics/programmazione-e-linguaggi]];
- [[topics/informatica]];
- [[sources/database-programmazione-formati-concorsi]];
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[sources/programmazione-algoritmi-strutture-dati-fonti-tecniche]];
- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]].

## Note di review

- Verificare con uno specialista pseudocodice, trace table, complessità e soluzioni degli esercizi.
- Validare sui bandi ufficiali quali linguaggi e quale profondità siano effettivamente richiesti.
- Mantenere paradigmi, ricorsione, alberi e grafi al livello introduttivo finché il programma non richiede sviluppo ulteriore.
- Verificare nel renderer KDP leggibilità dei blocchi di pseudocodice e delle caselle della checklist.
- Sottoporre quiz ed esercizi a revisione didattica prima della pubblicazione.
