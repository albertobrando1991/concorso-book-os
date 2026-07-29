---
id: chapter-m-tr01-02
type: book_chapter
title: "Informatica specialistica: cosa serve oltre il VOL-01"
status: developing
domain: "concorsi pubblici italiani"
topics: ["architettura elaboratori", "informatica specialistica", "sistemi operativi"]
entities: []
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/informatica-operativa-office-sistemi-hardware", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.72
updated_at: 2026-07-29
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "informatica-specialistica"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 2
draft_stage: content-draft
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/informatica-operativa-office-sistemi-hardware", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "topics/hardware-e-architettura-pc", "topics/informatica", "topics/sistemi-operativi-e-gestione-file", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-02-piano-completamento", "sources/architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche"]
---

# Informatica specialistica: cosa serve oltre il VOL-01

In una prova da funzionario ICT, riconoscere i componenti è solo il punto di partenza. Le domande specialistiche chiedono di collegare le parti del sistema: dove si trova un dato, chi esegue un'istruzione, perché le memorie hanno tempi diversi, quale risorsa limita le prestazioni e come interviene il sistema operativo quando più programmi competono per CPU e memoria.

Office, gestione elementare dei file e classificazioni di base restano fuori dal perimetro. CPU, memoria, dispositivi e software di sistema vengono qui studiati nelle loro relazioni, così da poterli usare nei quiz, nell'orale e nei casi tecnici.

## Obiettivo e confine con il VOL-01

Il VOL-01, capitolo 10, § 1, presenta i prerequisiti: hardware, software, dati, bit e byte, CPU, RAM, ROM, memoria di massa e periferiche. Il § 2 introduce sistema operativo, file e cartelle. Qui quei concetti sono dati per acquisiti.

A livello specialistico occorre saper:

- descrivere l’elaboratore come un insieme coordinato di unità;
- ricostruire, a livello concettuale, l’esecuzione di un’istruzione;
- collegare la rappresentazione dei dati a intervallo e precisione;
- spiegare la gerarchia di memoria;
- distinguere latenza, throughput e tempo di risposta;
- individuare un collo di bottiglia;
- leggere il sistema operativo come gestore e astrattore delle risorse.

Programmazione, reti, cloud e cybersecurity saranno sviluppati nei rispettivi capitoli. Qui compaiono soltanto quando servono a chiarire l’architettura del sistema.

## Mappa BANDO dell’informatica specialistica

| Passaggio | Domanda operativa | Azione del candidato |
| --- | --- | --- |
| **B — Bando** | Il programma richiede semplice conoscenza informatica o architetture e sistemi? | Evidenziare verbi e nuclei: conoscere, descrivere, confrontare, progettare, diagnosticare. |
| **A — Aree** | Il nucleo riguarda elaborazione, memoria, I/O, prestazioni o sistema operativo? | Separare le aree senza confonderle con reti, sviluppo o cloud. |
| **N — Nuclei** | Quali relazioni devo saper spiegare? | Costruire coppie causa-effetto: cache e latenza, RAM e processi, I/O e throughput. |
| **D — Diario** | Quale confusione ha prodotto l’errore? | Registrare l’opposizione corretta: capacità/velocità, latenza/throughput, processo/programma. |
| **O — Output** | Che cosa richiede la prova? | Preparare una risposta orale, risolvere un quiz o diagnosticare un caso. |

La profondità non si deduce dal solo titolo della materia. “Informatica” può indicare competenze operative di base; “architettura degli elaboratori”, “sistemi operativi”, “prestazioni” o “gestione delle risorse” richiedono invece una preparazione specialistica. Il singolo bando resta decisivo per delimitare il programma.

## L’elaboratore come sistema

Un elaboratore riceve dati e istruzioni, li conserva, li trasferisce, li elabora e produce risultati. Queste funzioni coinvolgono quattro gruppi essenziali:

- la **CPU**, che interpreta ed esegue le istruzioni;
- la **memoria**, che conserva istruzioni e dati in uso;
- i **dispositivi di input/output**, che scambiano informazioni con l’esterno;
- i **collegamenti di comunicazione**, che trasportano dati, indirizzi e segnali di controllo.

Contano soprattutto le relazioni fra le parti. Una CPU rapida lavora al di sotto delle proprie possibilità se deve attendere di continuo dati provenienti da una memoria o da un dispositivo più lento. Una maggiore quantità di RAM consente di mantenere più dati e programmi in uso, ma non accelera per questo ogni elaborazione.

### CPU, registri, unità di controllo e ALU

La CPU contiene unità con funzioni diverse. L’**unità di controllo** coordina l’esecuzione delle istruzioni e genera i segnali necessari. L’**unità aritmetico-logica**, o ALU, svolge operazioni aritmetiche e logiche. I **registri** conservano temporaneamente operandi, indirizzi, istruzioni e risultati immediatamente necessari.

I registri sono pochi e molto vicini alle unità di esecuzione. Non sostituiscono la RAM: servono a rendere disponibili alla CPU le informazioni richieste nell’istante di lavoro.

### Bus e dispositivi di I/O

Un **bus** è un insieme di linee e regole che permette ai componenti di comunicare. I segnali hanno compiti diversi: trasportare dati, identificare una posizione o un dispositivo, coordinare lettura, scrittura e temporizzazione.

I dispositivi di I/O non dialogano necessariamente con la CPU come se fossero semplici celle di memoria. Controller e interfacce traducono richieste, gestiscono differenze di velocità e segnalano il completamento delle operazioni.

### Il ciclo di esecuzione di un’istruzione

Un modello didattico efficace divide l’esecuzione in passaggi:

1. la CPU preleva l’istruzione dalla memoria;
2. l’istruzione viene interpretata;
3. sono acquisiti gli operandi necessari;
4. l’operazione viene eseguita;
5. il risultato viene scritto nella destinazione prevista;
6. il flusso prosegue con l’istruzione successiva o con quella indicata da un salto.

Questa sequenza, spesso riassunta come prelievo, decodifica ed esecuzione, è un modello concettuale. Le CPU reali possono sovrapporre fasi, eseguire più operazioni e adottare strategie complesse. In prova, il modello serve a spiegare le funzioni, non a descrivere ogni dettaglio di una specifica architettura.

## Rappresentare dati e istruzioni

Un sistema digitale opera su configurazioni di bit. Il significato non è contenuto nei bit in sé: dipende dalla **codifica** e dall’interpretazione scelta. La stessa sequenza può rappresentare un numero, un carattere, una parte di un’immagine o un’istruzione.

### Intervallo e codifica

Un numero finito di bit produce un insieme finito di configurazioni. Disporre di più bit amplia l'intervallo rappresentabile oppure consente una descrizione più precisa.

Per gli interi va distinta almeno la rappresentazione senza segno da quella con segno. Nel primo caso tutte le configurazioni possono indicare valori non negativi; nel secondo serve una convenzione che comprenda anche i negativi. La stessa sequenza binaria può quindi assumere valori diversi secondo il formato adottato.

I caratteri sono associati a codici numerici definiti da uno standard. La codifica rende possibile memorizzare e scambiare testo, ma mittente e destinatario devono interpretare i byte secondo regole compatibili.

### Precisione, arrotondamento e overflow

I numeri reali non possono essere tutti rappresentati esattamente con una quantità finita di bit. Una rappresentazione in virgola mobile descrive un insieme limitato di valori e deve approssimarne altri. Per questo alcuni calcoli possono produrre piccoli errori di arrotondamento.

L’**overflow** si verifica quando un risultato supera l’intervallo previsto dal formato. La **perdita di precisione** riguarda invece l’impossibilità di conservare tutte le cifre o differenze rilevanti. Sono problemi distinti: un valore può rientrare nell’intervallo ma essere rappresentato con precisione insufficiente.

## La gerarchia di memoria

Non esiste una memoria ideale che sia contemporaneamente vastissima, velocissima, persistente ed economica. I sistemi combinano livelli diversi.

| Livello | Funzione prevalente | Caratteristica da ricordare |
| --- | --- | --- |
| Registri | Operandi e stato immediato della CPU | Capacità molto ridotta, accesso rapidissimo |
| Cache | Copia temporanea di dati e istruzioni usati con maggiore probabilità | Riduce gli accessi ai livelli più lenti |
| RAM | Programmi e dati attivi | Volatile, più ampia della cache |
| Memoria persistente | File, programmi e dati conservati | Grande capacità, permanenza senza alimentazione |

La gerarchia funziona perché i programmi tendono a riutilizzare dati e istruzioni già usati e ad accedere a posizioni vicine. È il **principio di località**: temporale quando un elemento viene riutilizzato a breve; spaziale quando è probabile l’accesso a elementi vicini.

Una cache non aumenta la capacità complessiva come farebbe l’aggiunta di storage. Cerca invece di ridurre il tempo medio di accesso mantenendo vicino alla CPU ciò che potrebbe servire presto. Se il dato richiesto è presente si ha un *hit*; se manca, un *miss* impone il recupero da un livello più lento.

## Input/output e gestione degli eventi

Le periferiche hanno tempi e modalità di funzionamento molto diversi dalla CPU. Costringere il processore a controllare senza sosta se un dispositivo ha terminato sprecherebbe capacità di calcolo.

Con un **interrupt**, un dispositivo o un evento segnala che richiede attenzione. La CPU interrompe il flusso corrente, salva lo stato necessario, esegue la routine prevista e riprende il lavoro. Questo non rende istantanea la gestione: il sistema deve riconoscere l'evento, stabilirne la priorità e servirlo.

Il **buffering** usa un’area temporanea per assorbire differenze di velocità o di dimensione dei trasferimenti. Un buffer non elimina il limite del dispositivo: può rendere più regolare il flusso e ridurre le attese immediate, ma se i dati arrivano stabilmente più in fretta di quanto possano essere elaborati il collo di bottiglia rimane.

## Capire le prestazioni

La parola “veloce” è troppo generica. Prima di confrontare due sistemi occorre stabilire quale risultato interessa.

- **Latenza**: tempo necessario perché un’operazione o una risposta si completi.
- **Throughput**: quantità di lavoro completata nell’unità di tempo.
- **Tempo di risposta**: intervallo percepito fra richiesta e risultato, che può includere attese, elaborazione e trasferimenti.

Una minore latenza della singola operazione non garantisce il massimo throughput complessivo. Può accadere anche l'opposto: il sistema elabora molte richieste al secondo, ma una richiesta specifica riceve risposta troppo tardi.

### Colli di bottiglia e parallelismo

Il **collo di bottiglia** è la risorsa o la fase che limita il risultato osservato. Può essere CPU, memoria, storage, rete, dispositivo esterno, software o contesa fra attività. La diagnosi corretta parte dalla metrica e dal carico: non dall’acquisto automatico del componente con il numero commerciale più alto.

Il parallelismo può aumentare il lavoro svolto quando le attività possono procedere in modo indipendente. Non rende però parallela una parte intrinsecamente sequenziale e introduce costi di coordinamento, sincronizzazione e scambio dei dati.

## Il sistema operativo come gestore delle risorse

Il sistema operativo offre ai programmi un ambiente di esecuzione e governa l’accesso alle risorse. Non è soltanto l’interfaccia grafica vista dall’utente.

Un **programma** è un insieme di istruzioni memorizzate; un **processo** è un’istanza in esecuzione, con stato e risorse. Il sistema operativo decide quando assegnare tempo di CPU ai processi, ne conserva il contesto durante gli avvicendamenti e coordina le attese.

Nella gestione della memoria assegna spazi ai processi, protegge aree che non devono essere usate indebitamente e offre astrazioni che separano la visione del programma dalla disposizione fisica. Nella gestione dell’I/O usa driver e meccanismi di controllo per fornire interfacce più uniformi a dispositivi differenti.

Il file system organizza dati persistenti attraverso file, directory, metadati e permessi. Qui interessa la funzione di organizzazione, accesso e protezione; le operazioni pratiche su file e cartelle restano nel VOL-01.

## Caso guidato: il gestionale rallenta durante l’importazione

Un ente importa un archivio molto grande. Durante l’operazione il gestionale risponde lentamente. Un collega propone di sostituire subito la CPU.

La diagnosi deve procedere per ipotesi verificabili:

1. definire la metrica: tempo totale dell’importazione o risposta delle altre funzioni;
2. osservare quali risorse sono sature;
3. distinguere elaborazione, lettura da storage, scrittura, memoria e attese;
4. verificare se più processi competono per la stessa risorsa;
5. provare l’intervento sulla risorsa limitante e misurare di nuovo.

Se la CPU attende lo storage, sostituirla con un modello più rapido può incidere poco. Se la trasformazione dei dati occupa stabilmente tutta la capacità di calcolo, la CPU è invece un candidato plausibile. Per formulare la diagnosi non basta una specifica tecnica isolata.

## Domanda da commissario

**Descriva il ciclo di esecuzione di un’istruzione e il ruolo della memoria.**

Una risposta ordinata parte dal prelievo dell’istruzione dalla memoria, prosegue con decodifica, acquisizione degli operandi, esecuzione e scrittura del risultato. L’unità di controllo coordina le fasi, l’ALU svolge le operazioni previste e i registri conservano le informazioni immediatamente necessarie. Cache e RAM appartengono alla gerarchia che alimenta la CPU, con compromessi diversi fra capacità e tempo di accesso.

## Domanda-trappola

**Aumentare la RAM rende sempre più veloce il processore?**

No. Più RAM può evitare la carenza di memoria e ridurre il ricorso a livelli persistenti più lenti. In determinati carichi, il sistema ne trae beneficio. La velocità interna della CPU però non cambia e un collo di bottiglia collocato altrove rimane.

## Errore tipico

Confrontare componenti usando una sola cifra. Frequenza, capacità o numero di unità non descrivono da soli le prestazioni osservate. Prima si identifica l’output richiesto, poi la metrica, infine la risorsa che limita quel carico.

## Checklist delle competenze specialistiche

Per ogni riga segnare: **R** se riconosci il concetto, **S** se sai spiegarlo, **A** se sai applicarlo.

| Competenza | R | S | A |
| --- | --- | --- | --- |
| Collegare CPU, memoria, bus e I/O | ☐ | ☐ | ☐ |
| Ricostruire il ciclo di un’istruzione | ☐ | ☐ | ☐ |
| Distinguere codifica, intervallo e precisione | ☐ | ☐ | ☐ |
| Spiegare overflow e perdita di precisione | ☐ | ☐ | ☐ |
| Ordinare e confrontare i livelli di memoria | ☐ | ☐ | ☐ |
| Spiegare località, hit e miss | ☐ | ☐ | ☐ |
| Distinguere latenza, throughput e tempo di risposta | ☐ | ☐ | ☐ |
| Individuare un possibile collo di bottiglia | ☐ | ☐ | ☐ |
| Distinguere programma e processo | ☐ | ☐ | ☐ |
| Spiegare il sistema operativo come gestore di risorse | ☐ | ☐ | ☐ |

Una riga segnata soltanto con R non è ancora pronta per l’orale. Per passare ad A, formulare un esempio o risolvere un caso.

## Mini-esercizi e quiz ragionati

### Esercizio 1

Ordina dal livello normalmente più vicino alla CPU a quello destinato alla conservazione persistente: RAM, registri, storage, cache.

**Soluzione:** registri, cache, RAM, storage. L’ordine descrive la gerarchia funzionale generale, non una garanzia assoluta sulle prestazioni di ogni prodotto.

### Esercizio 2

Un servizio completa 500 richieste al secondo, ma una singola richiesta attende molto prima della risposta. Quale distinzione devi applicare?

**Soluzione:** throughput e latenza o tempo di risposta. Un throughput elevato non dimostra che ogni richiesta riceva risposta rapidamente.

### Quiz

Quale affermazione è corretta?

- A. La cache serve principalmente ad aumentare la capacità persistente.
- B. Un buffer elimina qualunque collo di bottiglia di I/O.
- C. Un processo è un programma in esecuzione con stato e risorse.
- D. La RAM modifica sempre la frequenza della CPU.

**Risposta corretta: C.** Le altre opzioni attribuiscono a cache, buffer e RAM effetti che non hanno necessariamente.

## Da sapere in 5 righe

- L’architettura si comprende collegando CPU, memoria e I/O.
- I bit acquistano significato attraverso una codifica.
- La gerarchia di memoria bilancia capacità, latenza, costo e persistenza.
- Le prestazioni richiedono una metrica e l’individuazione del collo di bottiglia.
- Il sistema operativo gestisce e astrae le risorse per programmi e utenti.

## Riferimenti consolidati

- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, §§ 1-2;
- [[topics/hardware-e-architettura-pc]];
- [[topics/informatica]];
- [[topics/sistemi-operativi-e-gestione-file]];
- [[sources/informatica-operativa-office-sistemi-hardware]];
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]];
- [[sources/architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche]].

## Note di review

- Validare con uno specialista di architettura degli elaboratori le semplificazioni su ciclo d’istruzione, gerarchia di memoria, interrupt e parallelismo.
- Verificare periodicamente versioni e stabilità dei riferimenti tecnici consolidati per architettura, sistemi operativi e metriche di prestazione.
- Mantenere la trattazione della virgola mobile entro intervallo, precisione e arrotondamento finché una review specialistica non approva ulteriori dettagli.
- Verificare sui bandi ufficiali del campione VOL-08 terminologia e profondità effettivamente richieste; il capitolo non attribuisce frequenze statistiche ai nuclei.
- Sottoporre quiz e checklist a revisione didattica prima della pubblicazione.
