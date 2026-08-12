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
review_required: true
canonical: true
format_version: 2
dati_operativi: []
tags: ["chapter", "m-tr01", "programmazione", "algoritmi"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 3
draft_stage: professional-draft
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/database-programmazione-formati-concorsi", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/programmazione-algoritmi-strutture-dati-fonti-tecniche", "topics/programmazione-e-linguaggi", "topics/informatica", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-03-piano-completamento"]
---

# Programmazione, algoritmi e strutture dati

Nelle prove tecniche, conoscere una parola chiave non è sufficiente. Può essere necessario leggere un algoritmo, seguirne l’esecuzione, trovare un errore, scegliere una struttura dati o spiegare perché una soluzione rallenta al crescere dell’input.

La sintassi cambia da un linguaggio all’altro. Il metodo, invece, parte dal problema, rappresenta i dati, ordina i passi, controlla i casi limite e valuta il costo della soluzione. Per questo il capitolo usa soprattutto lo pseudocodice.

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

Se il bando cita Java, Python, C# o un altro linguaggio, va studiata anche la sintassi richiesta. Lo pseudocodice non sostituisce quella preparazione: separa la logica dalle regole del linguaggio.

## N-TR01-03-01 · Problema, algoritmo e correttezza

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

I test aiutano a trovare errori, ma non dimostrano da soli la correttezza per ogni input possibile. In una prova, la soluzione può essere motivata con un’invariante semplice: una proprietà che resta vera durante l’esecuzione. Nel conteggio delle pratiche, dopo aver esaminato i primi `k` elementi, il contatore deve coincidere con il numero di stati cercati fra quei `k` elementi.

### Pseudocodice e tracciamento

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

### Principi di specifica, precondizioni e casi limite

Una specifica separa ciò che la soluzione deve fare dal modo in cui lo farà. La **precondizione** descrive ciò che deve essere vero prima dell'esecuzione; la **postcondizione** descrive il risultato garantito al termine. Per una ricerca binaria, la precondizione essenziale è che la collezione sia ordinata secondo lo stesso criterio usato nei confronti.

I casi limite incidono sul contratto dell'algoritmo. Una collezione vuota, un solo elemento, una chiave assente, valori duplicati o un input non valido possono cambiarne il comportamento. Prima del codice si decide se l'input non valido viene rifiutato, corretto o gestito come risultato speciale.

Nel colloquio tecnico, la correttezza si argomenta collegando ogni passo alla specifica. La trace table dimostra il comportamento su istanze scelte; un'invariante spiega perché il ragionamento continua a valere durante tutte le iterazioni. Test e argomentazione svolgono ruoli diversi e complementari.

Per dimostrare un ciclo si controllano tre momenti. L'invariante deve essere vera prima della prima iterazione, conservarsi dopo ogni esecuzione del corpo e, insieme alla condizione di uscita, implicare la postcondizione. La terminazione richiede inoltre una quantità che progredisca verso un limite. Questo schema rende la risposta più solida del semplice «funziona nei test».

Quando il problema ammette più risultati corretti, la specifica deve chiarire il criterio. Cercare una pratica duplicata può significare restituire la prima occorrenza, tutte le occorrenze oppure segnalare l'anomalia. Algoritmi diversi possono essere corretti rispetto a specifiche diverse.

## N-TR01-03-02 · Paradigmi e flusso di controllo

Un **paradigma** è un modo generale di organizzare il calcolo.

- Nel paradigma **imperativo** il programma modifica uno stato attraverso istruzioni.
- La programmazione **procedurale** organizza tali istruzioni in procedure e funzioni.
- La programmazione **orientata agli oggetti** combina dati e comportamenti in oggetti appartenenti a classi o tipi.
- La programmazione **funzionale** privilegia composizione di funzioni e controllo degli effetti sullo stato.
- La programmazione **dichiarativa** descrive il risultato o le regole, lasciando al sistema parte della scelta del procedimento.

I linguaggi reali possono sostenere più paradigmi. Un singolo esempio non basta quindi ad assegnare un linguaggio in modo esclusivo a una categoria.

### Tipi, espressioni e strutture di controllo

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

### Scegliere il costrutto

Il paradigma orienta la soluzione, ma non sostituisce l'analisi del problema. Un flusso procedurale può essere chiaro per elaborare una sequenza di pratiche; gli oggetti aiutano quando dati e comportamenti evolvono insieme; una trasformazione funzionale è utile quando si vuole limitare lo stato modificabile. Nei linguaggi multiparadigma queste scelte possono convivere.

La selezione è appropriata quando il programma sceglie fra alternative. Le condizioni devono coprire tutti i casi previsti e, quando necessario, essere mutuamente esclusive. Un ramo finale generico può intercettare dati inattesi, ma non deve nasconderli senza una decisione esplicita.

L'iterazione si sceglie in base a ciò che è noto. PER OGNI esprime bene la visita di tutti gli elementi; MENTRE è adatto quando la ripetizione termina al verificarsi di una condizione. Il controllo deve progredire verso la terminazione: indice, elemento corrente o stato devono cambiare in modo coerente.

**Applicazione.** Per validare una lista di identificativi, il candidato può usare un ciclo, una selezione per distinguere valori validi e non validi e un accumulatore per contare gli errori. La risposta deve dichiarare tipo dei dati, condizione di validità e comportamento sull'input vuoto.

Gli operatori logici combinano condizioni. AND richiede che entrambe siano vere, OR che ne sia vera almeno una, NOT nega il risultato. Le parentesi rendono esplicita la precedenza e riducono ambiguità. Nei quiz, negare una condizione composta è una fonte frequente di errore.

Una conversione di tipo può fallire. Prima di trasformare una stringa in numero, il programma verifica il formato oppure gestisce l'errore. Assumere che ogni input sia corretto sposta il difetto dal requisito all'esecuzione.

Nel tracciamento, ogni espressione va valutata con i valori correnti, prima dell'eventuale assegnazione. Confondere il vecchio e il nuovo stato produce errori soprattutto quando più variabili vengono aggiornate nello stesso ciclo. Una tabella con una colonna per variabile rende visibile l'ordine.

### Micro-verifica: controllo del flusso

Devi esaminare tutte le pratiche e contare quelle con importo negativo. Quale struttura di controllo scegli e quale paradigma stai usando?

**Soluzione:** un ciclo PER OGNI visita le pratiche; al suo interno una selezione controlla l’importo e un contatore viene aggiornato. È una soluzione imperativa o procedurale: modifica uno stato secondo istruzioni ordinate.

## N-TR01-03-03 · Funzioni e procedure

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

### Contratto e scomposizione

Una buona funzione ha uno scopo riconoscibile. Il nome, i parametri e il valore restituito formano un contratto leggibile: chi la usa deve sapere quali dati fornire, quale risultato attendersi e quali condizioni di errore gestire. Se una funzione modifica anche stato esterno, l'effetto deve essere esplicito.

Scomporre un algoritmo riduce il numero di dettagli da considerare nello stesso momento. Invece di mescolare lettura, validazione, classificazione e conteggio, si possono definire funzioni separate e comporle. La scomposizione aiuta test, riuso e manutenzione, ma frammentare ogni istruzione in una funzione distinta rende il flusso difficile da seguire.

Una funzione di validazione può restituire un valore booleano, mentre una funzione di conteggio governa l'iterazione e usa la prima. Il chiamante non deve conoscere i dettagli della validazione, ma dipende dal suo contratto. Cambiare la regola in un solo punto evita duplicazioni e risultati incoerenti.

### Parametri, passaggio e stato

I linguaggi differiscono nel modo in cui trasferiscono argomenti e riferimenti. In prova va distinto il valore fornito alla chiamata dall'oggetto eventualmente condiviso. Modificare una struttura ricevuta può produrre effetti visibili al chiamante; creare e restituire una nuova struttura rende il flusso più esplicito, ma può richiedere memoria aggiuntiva.

Le variabili globali facilitano l'accesso condiviso, ma aumentano l'accoppiamento. Una funzione che dipende da uno stato nascosto è più difficile da testare perché lo stesso input esplicito può produrre risultati diversi. Passare le dipendenze come parametri rende il comportamento più leggibile.

La ricorsione usa lo stack delle chiamate. Ogni invocazione conserva parametri e stato locale finché la chiamata più interna termina. Una soluzione ricorsiva può rispecchiare bene strutture come alberi, ma non è automaticamente più efficiente di un ciclo: vanno considerati profondità, memoria e chiarezza.

**Errore tipico.** Confondere parametro e argomento, oppure descrivere una procedura come se fosse priva di effetti solo perché non restituisce un valore. Nell'orale va chiarito sia il risultato sia lo stato eventualmente modificato.

### Coesione, dipendenze e test

Una funzione è coesa quando le sue istruzioni collaborano a un solo compito comprensibile. Una funzione che valida dati, scrive file e aggiorna statistiche contiene responsabilità diverse: separarle permette di verificare ogni parte con input mirati. La separazione non impone un numero fisso di righe; dipende dal contratto.

Le dipendenze esplicite facilitano il test. Se una funzione riceve i dati e restituisce un risultato, si possono preparare casi ordinari, vuoti e non validi. Se legge direttamente una risorsa globale, il test deve anche predisporre e ripristinare quello stato.

Per una funzione ricorsiva si provano almeno il caso base, il primo caso ricorsivo e un input abbastanza grande da rivelare errori nella progressione. La risposta concorsuale deve spiegare quale parte del problema si riduce a ogni chiamata.

Una funzione troppo dipendente dal contesto è difficile da riusare. Parametri essenziali, risultato chiaro ed effetti dichiarati permettono invece di sostituire l'implementazione senza cambiare chi la chiama. Questo è il valore pratico dell'astrazione, non soltanto una scelta di stile.

## N-TR01-03-04 · Strutture lineari e associative

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

### Operazioni e criteri di scelta

La struttura si sceglie partendo dalle operazioni dominanti. Un array è adatto quando serve spesso l'accesso per posizione; una lista concatenata può favorire inserimenti quando il punto è già noto; una coda mantiene l'ordine di arrivo; una pila recupera per primo l'ultimo elemento inserito; una mappa cerca per chiave; un insieme controlla appartenenza e duplicati.

| Esigenza | Struttura candidata | Domanda da verificare |
| --- | --- | --- |
| Accesso per indice | array | la dimensione cambia spesso? |
| Ordine di arrivo | coda | esistono priorità diverse? |
| Annullamento dell'ultima azione | pila | quante operazioni vanno conservate? |
| Ricerca per identificativo | mappa | come sono gestite chiavi e collisioni? |
| Valori unici | insieme | quale regola stabilisce l'uguaglianza? |

La tabella propone strutture candidate. L'implementazione concreta ne determina costi e vincoli. Una mappa basata su hash e una basata su albero offrono la stessa relazione chiave-valore, ma hanno proprietà differenti su ordinamento e prestazioni.

### Mutabilità, duplicati e ordine

Una struttura **mutabile** può essere modificata dopo la creazione; una struttura immutabile produce una nuova versione a ogni trasformazione. La mutabilità può ridurre copie, ma richiede attenzione quando più parti del programma condividono lo stesso oggetto. L'immutabilità semplifica il ragionamento sugli effetti, con possibili costi di rappresentazione.

Duplicati e ordine sono proprietà separate. Una lista può contenere duplicati e conservarne la sequenza; un insieme elimina duplicati ma non garantisce necessariamente un ordine significativo; una mappa richiede chiavi uniche, mentre i valori possono ripetersi. Il candidato deve dichiarare quali proprietà servono al problema.

**Mini-caso.** Un ufficio deve evitare di elaborare due volte lo stesso identificativo, conservare l'ordine di arrivo e recuperare rapidamente lo stato. Una singola struttura potrebbe non soddisfare tutto. Una lista o coda conserva l'ordine, un insieme segnala duplicati e una mappa associa identificativi e stati. La soluzione va motivata anche per il costo di mantenere più rappresentazioni coerenti.

Anche inserimento e cancellazione richiedono una domanda precisa: si conosce già la posizione o bisogna prima cercarla? In una lista concatenata modificare i collegamenti può essere economico quando il nodo è noto, ma trovarlo può richiedere una scansione. Il costo complessivo include entrambe le fasi.

Alcune strutture dinamiche riservano capacità aggiuntiva per evitare una riallocazione a ogni inserimento. Una singola espansione può essere costosa, mentre il costo medio distribuito su molte operazioni resta contenuto. Anche qui va dichiarata l'implementazione considerata.

## N-TR01-03-05 · Alberi, grafi, ricerca e ordinamento

### Alberi e grafi

Un **albero** descrive una struttura gerarchica senza cicli nel modello radicato. Ogni nodo, tranne la radice, ha un genitore. Alberi di ricerca e heap aggiungono proprietà specifiche.

Un **grafo** è formato da vertici e archi e rappresenta relazioni più generali: collegamenti fra sistemi, dipendenze o percorsi. Può essere orientato o non orientato, pesato o non pesato. Il capitolo introduce la struttura; gli algoritmi avanzati sui grafi restano fuori perimetro.

### Ricerca

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

### Ordinamento

L’ordinamento dispone gli elementi secondo una relazione coerente. Due algoritmi possono produrre lo stesso ordine ma avere costi e proprietà differenti.

L’**insertion sort** costruisce una parte ordinata inserendo ogni nuovo elemento nella posizione corretta. È semplice e può funzionare bene su collezioni piccole o quasi ordinate. Nel caso peggiore, confronti e spostamenti crescono quadraticamente: `O(n²)`.

Il **merge sort** divide la collezione, ordina ricorsivamente le parti e le fonde. Il suo tempo cresce come `O(n log n)` nei casi tipicamente analizzati, ma la fusione richiede memoria aggiuntiva nella rappresentazione comune.

L’ordine di crescita è uno dei criteri di scelta. Vanno considerati anche la dimensione, la memoria disponibile, lo stato iniziale dei dati, la stabilità richiesta e il costo effettivo delle operazioni.

### Collegare struttura e algoritmo

Ricerca e ordinamento non sono indipendenti dalla rappresentazione. La ricerca binaria richiede accesso efficiente all'elemento centrale e dati ordinati; su una lista concatenata, raggiungere il centro può costare attraversamenti ripetuti. Un albero di ricerca conserva una relazione d'ordine durante gli inserimenti, ma le prestazioni dipendono dalla sua forma e dalle proprietà dell'implementazione.

Nei grafi, la ricerca diventa visita delle relazioni. Una coda sostiene una visita per livelli, mentre una pila o la ricorsione sostengono una visita in profondità. Il capitolo non richiede gli algoritmi avanzati, ma questa connessione mostra perché la struttura dati influenza direttamente il procedimento.

**Domanda-trappola.** Ordinare prima rende sempre migliore la ricerca? No. Se la raccolta viene interrogata una sola volta, il costo dell'ordinamento può superare il risparmio. Se invece molte ricerche seguono e i dati cambiano poco, mantenere un ordine o un indice può essere conveniente.

Un ordinamento è **stabile** se conserva l'ordine relativo degli elementi con la stessa chiave. La proprietà conta quando esistono criteri successivi: dopo aver ordinato pratiche per data, un ordinamento stabile per stato può preservare l'ordine cronologico all'interno di ogni stato.

La scelta considera anche il caso peggiore, la memoria aggiuntiva e lo stato iniziale dei dati. Insertion sort può essere adatto a pochi elementi quasi ordinati; merge sort offre crescita O(n log n) ma usa spazio per la fusione nella versione comune. Nessuna etichetta sostituisce il profilo del carico.

Nel confronto orale è utile dichiarare anche l'output in caso di insuccesso. Una ricerca può restituire una posizione speciale, un valore assente o un errore controllato. La convenzione deve evitare di confondere «non trovato» con una posizione valida.

## N-TR01-03-06 · Complessità e output concorsuale

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

La notazione asintotica confronta la crescita per input grandi e trascura fattori costanti. Due algoritmi entrambi O(n) possono avere tempi diversi su input reali; l'etichetta dice che il lavoro dominante cresce linearmente, non che le implementazioni siano equivalenti. Per input piccoli, semplicità e costi fissi possono pesare più dell'ordine di crescita.

Si distinguono caso migliore, medio e peggiore quando hanno significato. La ricerca lineare trova subito una chiave posta all'inizio, ma nel caso peggiore visita tutta la collezione. Dichiarare soltanto O(n) senza specificare scenario e operazione può nascondere l'ipotesi usata.

La complessità spaziale considera la memoria aggiuntiva rispetto all'input. Un algoritmo può ridurre il tempo creando una struttura ausiliaria, oppure risparmiare memoria accettando più passaggi. Il compromesso va motivato rispetto ai vincoli del problema.

### Dalla traccia alla risposta

In un esercizio tecnico, il candidato procede in ordine: definisce input e output, dichiara precondizioni, sceglie struttura e algoritmo, tratta i casi limite, stima tempo e spazio, quindi verifica con una trace table. Nell'orale può esporre la stessa sequenza in forma breve.

Nel debug, cambiare istruzioni a tentativi rende difficile capire la causa. Si riproduce invece il difetto con un input minimo, si confrontano stato atteso e stato osservato, si localizza il primo passaggio divergente e si corregge la causa. Un nuovo test conserva l'evidenza del caso scoperto.

La stima asintotica non sostituisce la misurazione, e la misurazione non sostituisce l'analisi. La prima anticipa la crescita, la seconda verifica una specifica implementazione su dati e ambiente dichiarati. Una risposta completa tiene separati i due piani.

### Caso guidato: classificare le pratiche

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

L’algoritmo visita ogni pratica una volta: il tempo cresce come `O(n)`. Le tre liste occupano complessivamente spazio proporzionale al numero di pratiche. La categoria `anomalie` evita di perdere silenziosamente dati inattesi.

### Domanda da commissario

**Come sceglie una struttura dati per risolvere un problema?**

Parto dalle operazioni richieste: accesso per posizione, ricerca per chiave, inserimento, cancellazione, mantenimento dell’ordine o gestione FIFO/LIFO. Considero poi dimensione, frequenza delle operazioni, memoria e implementazione disponibile. La scelta va motivata sul carico: una struttura efficace per accessi indicizzati può non esserlo per inserimenti frequenti nel mezzo.

### Domanda-trappola

**La ricerca binaria è sempre preferibile alla ricerca lineare?**

No. Richiede dati ordinati e un accesso compatibile alla posizione centrale. Se la collezione non è ordinata e deve essere cercata una sola volta, il costo dell’ordinamento può superare il beneficio. La ricerca lineare resta inoltre adatta a raccolte piccole o prive di accesso diretto.

### Errore tipico

Associare una complessità alla struttura senza indicare operazione e rappresentazione. “La mappa è O(1)” è incompleto: alcune implementazioni offrono costo medio costante per certe operazioni, altre hanno costi logaritmici, e il caso peggiore può differire.

## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento consente di verificare la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-03-01` | Esercizio 1 |
| `N-TR01-03-02` | Micro-verifica: controllo del flusso |
| `N-TR01-03-03` | Quiz 4 |
| `N-TR01-03-04` | Quiz 3 |
| `N-TR01-03-05` | Quiz 2 |
| `N-TR01-03-06` | Quiz 5 |

## ▣ Verifica

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

### Quiz 1

Quale affermazione è corretta?

- A. La ricerca binaria funziona correttamente su qualunque sequenza.
- B. Merge sort ha crescita quadratica in ogni caso.
- C. Una funzione ricorsiva richiede un caso base raggiungibile.
- D. Un insieme conserva necessariamente duplicati e ordine di inserimento.

**Risposta corretta: C.** A ignora l’ordinamento, B attribuisce una crescita errata, D contraddice la funzione dell’insieme.

### Quiz 2

Quale affermazione descrive una precondizione della ricerca binaria?

- A. La collezione deve essere ordinata secondo il criterio di confronto.
- B. La collezione deve contenere duplicati.
- C. L'algoritmo deve usare una pila.
- D. La chiave deve trovarsi nella prima metà.

**Risposta corretta: A.** Senza ordinamento coerente, eliminare metà dell'intervallo dopo un confronto non è giustificato.

### Quiz 3

Quale struttura segue la regola FIFO?

- A. Pila.
- B. Coda.
- C. Insieme.
- D. Albero binario.

**Risposta corretta: B.** Nella coda il primo elemento inserito è il primo servito; la pila segue invece la regola LIFO.

### Quiz 4

Che cosa distingue un parametro da un argomento?

- A. Il parametro compare nella definizione; l'argomento è fornito nella chiamata.
- B. Il parametro è sempre globale.
- C. L'argomento è sempre una stringa.
- D. Non esiste alcuna differenza.

**Risposta corretta: A.** La distinzione descrive due ruoli nello stesso meccanismo di chiamata.

### Quiz 5

Se la dimensione dell'input raddoppia, quale crescita tende a quadruplicare il lavoro dominante?

- A. O(1).
- B. O(log n).
- C. O(n).
- D. O(n²).

**Risposta corretta: D.** Il termine quadratico passa da n² a (2n)² = 4n², nel modello asintotico considerato.

### Quiz 6

Quale affermazione sulla ricorsione è corretta?

- A. È sempre più veloce di un ciclo.
- B. Richiede un caso base raggiungibile.
- C. Non usa memoria per le chiamate.
- D. Può risolvere soltanto problemi numerici.

**Risposta corretta: B.** Il caso base e il progresso verso di esso impediscono una sequenza indefinita di chiamate.

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

## Riferimenti professionali essenziali

- *Il Metodo BANDO*, capitolo 10, paragrafo 8, per i prerequisiti di programmazione.
- Documentazione ufficiale Python per tipi, controllo, funzioni e strutture fondamentali, usata soltanto per concetti trasferibili.
- Materiali didattici universitari e riferimenti tecnici su algoritmi, strutture dati e analisi asintotica.
- Programma del singolo bando, decisivo per linguaggi, profondità e formato della prova.
