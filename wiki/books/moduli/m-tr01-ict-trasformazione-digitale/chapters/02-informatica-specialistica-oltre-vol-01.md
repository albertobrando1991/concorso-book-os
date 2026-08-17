---
id: chapter-m-tr01-02
type: book_chapter
title: "Informatica specialistica: cosa serve oltre il VOL-01"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["architettura elaboratori", "informatica specialistica", "sistemi operativi"]
entities: []
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/informatica-operativa-office-sistemi-hardware", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.72
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: false
canonical: true
format_version: 2
dati_operativi: []
tags: ["chapter", "m-tr01", "informatica-specialistica"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 2
draft_stage: professional-draft
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/informatica-operativa-office-sistemi-hardware", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "topics/hardware-e-architettura-pc", "topics/informatica", "topics/sistemi-operativi-e-gestione-file", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-02-piano-completamento", "sources/architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche"]
---

# Informatica specialistica: cosa serve oltre il VOL-01

In una prova da funzionario ICT, riconoscere i componenti è solo il punto di partenza. Le domande specialistiche chiedono di collegare le parti del sistema: dove si trova un dato, chi esegue un'istruzione, perché le memorie hanno tempi diversi, quale risorsa limita le prestazioni e come interviene il sistema operativo quando più programmi competono per CPU e memoria.

Office, gestione elementare dei file e classificazioni di base restano fuori dal perimetro. CPU, memoria, dispositivi e software di sistema vengono qui studiati nelle loro relazioni, così da poterli usare nei quiz, nell'orale e nei casi tecnici.

## Obiettivo e confine con il VOL-01

Il VOL-01, capitolo 10, § 1, presenta i prerequisiti: hardware, software, dati, bit e byte, CPU, RAM, ROM, memoria di massa e periferiche. Il § 2 introduce sistema operativo, file e cartelle. Qui quei concetti sono dati per acquisiti.

La preparazione specialistica richiede di:

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

## N-TR01-02-01 · L’elaboratore come sistema

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

### Architettura, stato e coordinamento

La CPU non opera isolatamente. Il **clock** fornisce un riferimento temporale alle attività interne, ma la sola frequenza non misura il lavoro utile completato: architetture diverse possono eseguire quantità differenti di lavoro nello stesso numero di cicli. Anche il numero di unità di esecuzione, la disponibilità dei dati e le dipendenze fra istruzioni incidono sul risultato.

I registri comprendono sia valori manipolati dal programma sia informazioni di controllo. Il contatore di programma identifica il punto del flusso da eseguire; altri registri conservano lo stato necessario a proseguire correttamente. Quando avviene un'interruzione o il sistema operativo assegna la CPU a un altro processo, una parte di questo contesto deve essere salvata e poi ripristinata.

Il bus è un canale governato da regole. Le linee dati trasportano contenuti, quelle di indirizzo individuano destinazioni, quelle di controllo specificano operazioni e sincronizzazione. Quando più componenti richiedono lo stesso collegamento, un meccanismo di arbitraggio assegna gli accessi. La capacità del canale può diventare il limite del sistema.

### Applicazione al profilo

In una prova orale, una risposta chiara parte dalle funzioni: elaborare, conservare, trasferire e coordinare. Poi colloca CPU, memoria, controller e bus, e segue un'istruzione dal prelievo alla scrittura del risultato. Così i componenti non restano un elenco mnemonico: ciascuno trova posto nella catena causa-effetto.

**Mini-caso.** Una CPU più rapida non migliora sensibilmente un'elaborazione. Se il processore trascorre molto tempo in attesa dei dati, il limite può trovarsi nella memoria, nel bus o nell'I/O. La risposta corretta non sceglie subito un componente: identifica il percorso dei dati, misura le attese e localizza la risorsa satura.

## N-TR01-02-02 · Rappresentare dati e istruzioni

Un sistema digitale opera su configurazioni di bit. Il significato non è contenuto nei bit in sé: dipende dalla **codifica** e dall’interpretazione scelta. La stessa sequenza può rappresentare un numero, un carattere, una parte di un’immagine o un’istruzione.

### Intervallo e codifica

Un numero finito di bit produce un insieme finito di configurazioni. Disporre di più bit amplia l'intervallo rappresentabile oppure consente una descrizione più precisa.

Per gli interi va distinta almeno la rappresentazione senza segno da quella con segno. Nel primo caso tutte le configurazioni possono indicare valori non negativi; nel secondo serve una convenzione che comprenda anche i negativi. La stessa sequenza binaria può quindi assumere valori diversi secondo il formato adottato.

I caratteri sono associati a codici numerici definiti da uno standard. La codifica rende possibile memorizzare e scambiare testo, ma mittente e destinatario devono interpretare i byte secondo regole compatibili.

### Precisione, arrotondamento e overflow

I numeri reali non possono essere tutti rappresentati esattamente con una quantità finita di bit. Una rappresentazione in virgola mobile descrive un insieme limitato di valori e deve approssimarne altri. Per questo alcuni calcoli possono produrre piccoli errori di arrotondamento.

L’**overflow** si verifica quando un risultato supera l’intervallo previsto dal formato. La **perdita di precisione** riguarda invece l’impossibilità di conservare tutte le cifre o differenze rilevanti. Sono problemi distinti: un valore può rientrare nell’intervallo ma essere rappresentato con precisione insufficiente.

### Dal bit all'informazione

Il bit ammette due stati, convenzionalmente indicati con 0 e 1. Raggruppare i bit consente di costruire configurazioni più numerose: con `n` bit si ottengono `2^n` combinazioni. Questa relazione serve a ragionare sull'intervallo, non a memorizzare elenchi. Se un campo senza segno dispone di otto bit, per esempio, può distinguere 256 configurazioni. Il valore massimo dipende poi dalla convenzione scelta e dal fatto che una configurazione possa essere riservata.

Il **byte** è normalmente un gruppo di otto bit. Le unità maggiori descrivono capacità di memoria o quantità di dati. Il contesto conta: una misura decimale e una basata su potenze di due non sono automaticamente equivalenti. Nei quiz si identifica prima l'unità richiesta, poi la codifica e, per ultima, l'operazione.

Una codifica è un accordo fra chi produce e chi interpreta i dati. Nel testo, un codice associa numeri a caratteri; nelle immagini, i bit rappresentano campioni o componenti di colore; nell'audio, descrivono campioni del segnale. Aumentare il numero di bit disponibili può ampliare i valori distinguibili, ma non garantisce da solo qualità: contano anche il metodo di acquisizione, la codifica, la compressione e l'uso previsto.

### Interi, valori reali e istruzioni

Per gli interi con segno, i sistemi moderni usano comunemente una rappresentazione che rende efficienti somma e sottrazione. Ai fini concorsuali è più importante comprenderne l'effetto: una sequenza di bit ha valore solo entro un formato dichiarato. Interpretare come senza segno un campo progettato con segno può produrre un risultato completamente diverso.

I valori in virgola mobile separano, in forma codificata, segno, grandezza e precisione significativa. Il modello consente di rappresentare numeri molto grandi e molto piccoli, ma non tutti i reali. Ne deriva che il confronto diretto fra risultati calcolati può richiedere una tolleranza. In un procedimento amministrativo informatizzato, un importo monetario non dovrebbe essere trattato con leggerezza come un'approssimazione binaria: formato, regole di arrotondamento e controlli devono essere espliciti.

Anche un'istruzione è una configurazione codificata. Una parte indica l'operazione, altre parti possono identificare registri, dati o modalità per reperirli. La CPU non attribuisce significato linguistico all'istruzione: riconosce un formato previsto dalla propria architettura e attiva le unità necessarie.

### Applicazione al profilo

Il funzionario ICT deve saper collegare un'anomalia al livello corretto. Un carattere illeggibile suggerisce un problema di codifica; un contatore che supera il massimo riguarda l'intervallo; un risultato decimale leggermente diverso dall'atteso può dipendere dalla precisione; un file interpretato con il formato sbagliato non è necessariamente corrotto. La diagnosi parte quindi dalla domanda: «quale significato attribuisce il sistema a questi bit?».

**Mini-esercizio.** Un campo dispone di quattro bit senza segno. Quante configurazioni distingue? La risposta è sedici, perché `2^4 = 16`. Questo non significa che possa rappresentare sedici valori arbitrari: il significato delle configurazioni dipende dalla codifica adottata.

## N-TR01-02-03 · La gerarchia di memoria

Non esiste una memoria ideale che sia contemporaneamente vastissima, velocissima, persistente ed economica. I sistemi combinano livelli diversi.

| Livello | Funzione prevalente | Caratteristica da ricordare |
| --- | --- | --- |
| Registri | Operandi e stato immediato della CPU | Capacità molto ridotta, accesso rapidissimo |
| Cache | Copia temporanea di dati e istruzioni usati con maggiore probabilità | Riduce gli accessi ai livelli più lenti |
| RAM | Programmi e dati attivi | Volatile, più ampia della cache |
| Memoria persistente | File, programmi e dati conservati | Grande capacità, permanenza senza alimentazione |

La gerarchia funziona perché i programmi tendono a riutilizzare dati e istruzioni già usati e ad accedere a posizioni vicine. È il **principio di località**: temporale quando un elemento viene riutilizzato a breve; spaziale quando è probabile l’accesso a elementi vicini.

Una cache non aumenta la capacità complessiva come farebbe l’aggiunta di storage. Cerca invece di ridurre il tempo medio di accesso mantenendo vicino alla CPU ciò che potrebbe servire presto. Se il dato richiesto è presente si ha un *hit*; se manca, un *miss* impone il recupero da un livello più lento.

### Perché servono più livelli

La CPU può eseguire operazioni molto più rapidamente di quanto i livelli lontani riescano a fornire dati. La gerarchia riduce questa distanza combinando memorie con caratteristiche diverse. I livelli prossimi al processore privilegiano rapidità e accesso immediato; quelli più lontani privilegiano capacità, persistenza e costo per unità di informazione. Non esiste quindi un livello «migliore» in assoluto: ciascuno risponde a una funzione.

Quando la CPU richiede un dato, il sistema cerca di soddisfare la richiesta al livello più vicino utile. Un hit evita l'accesso al livello successivo; un miss introduce una penalità. Il tempo medio dipende sia dalla rapidità del livello sia dalla frequenza con cui i dati richiesti vi sono presenti. Per questo una cache molto veloce ma usata male non elimina le attese.

La località temporale emerge, per esempio, quando un ciclo riusa la stessa variabile. La località spaziale compare quando il programma percorre in ordine gli elementi contigui di un vettore. Strutture dati e modalità di accesso possono quindi incidere sulle prestazioni anche senza cambiare la frequenza della CPU.

### RAM, memoria virtuale e persistenza

La RAM contiene codice e dati dei programmi attivi ed è volatile: perdendo alimentazione, non conserva stabilmente il contenuto. Lo storage mantiene file e programmi, ma ha finalità e tempi diversi. Confondere RAM e spazio su disco porta a diagnosi sbagliate: liberare storage non equivale ad aggiungere memoria di lavoro.

Il sistema operativo offre a ciascun processo uno spazio di indirizzamento e traduce gli indirizzi usati dal programma nelle posizioni effettivamente disponibili. La **memoria virtuale** è anzitutto questa astrazione organizzativa e protettiva; non coincide con il semplice uso del disco come estensione della RAM. Se parti non immediatamente necessarie vengono spostate verso un livello persistente, l'accesso successivo può però diventare molto più lento.

La persistenza richiede regole di organizzazione e affidabilità. Il salvataggio attraversa buffer, controller e file system; la conferma dell'applicazione non garantisce sempre che ogni livello abbia già completato la scrittura fisica. Nei sistemi critici servono politiche coerenti di sincronizzazione, ridondanza e backup. Sono temi distinti dalla gerarchia di memoria.

### Applicazione al profilo

Di fronte a un'applicazione lenta, il candidato deve chiedersi se il working set entra in RAM, se si verificano molti miss di cache, se il sistema ricorre frequentemente allo storage e se più processi competono per la memoria. Aggiungere RAM aiuta quando la pressione di memoria è reale; incide poco se il limite è un algoritmo inefficiente o un dispositivo di I/O saturo.

**Errore tipico.** Ordinare i livelli solo per capacità e concludere che il più grande sia il più efficace. La risposta completa espone il compromesso fra vicinanza, latenza, capacità, costo e persistenza.

## N-TR01-02-04 · Input/output e gestione degli eventi

Le periferiche hanno tempi e modalità di funzionamento molto diversi dalla CPU. Costringere il processore a controllare senza sosta se un dispositivo ha terminato sprecherebbe capacità di calcolo.

Con un **interrupt**, un dispositivo o un evento segnala che richiede attenzione. La CPU interrompe il flusso corrente, salva lo stato necessario, esegue la routine prevista e riprende il lavoro. Questo non rende istantanea la gestione: il sistema deve riconoscere l'evento, stabilirne la priorità e servirlo.

Il **buffering** usa un’area temporanea per assorbire differenze di velocità o di dimensione dei trasferimenti. Un buffer non elimina il limite del dispositivo: può rendere più regolare il flusso e ridurre le attese immediate, ma se i dati arrivano stabilmente più in fretta di quanto possano essere elaborati il collo di bottiglia rimane.

### Controller, driver e trasferimenti

Un dispositivo presenta registri, comandi e vincoli propri. Il **controller** governa gli aspetti elettronici e temporali del trasferimento; il **driver** è il componente software con cui il sistema operativo controlla quella famiglia di dispositivi. Questa separazione consente alle applicazioni di usare interfacce relativamente uniformi senza conoscere ogni dettaglio dell'hardware.

Il trasferimento può coinvolgere la CPU in misura diversa. Nel controllo programmato, o polling, il processore interroga ripetutamente lo stato del dispositivo. La soluzione è semplice e può essere adeguata per attese brevissime o sistemi elementari, ma spreca tempo se l'evento è raro. Con gli interrupt, invece, il dispositivo segnala la necessità di servizio. Per blocchi consistenti di dati, meccanismi dedicati possono trasferire informazioni fra dispositivo e memoria riducendo il lavoro puntuale della CPU.

Un interrupt ha un costo. Il sistema salva lo stato, individua la sorgente, esegue il gestore e riprende l'attività interrotta. Troppi eventi consumano risorse; per contenerne l'effetto, il sistema può aggregarli o regolarne le priorità. La scelta dipende dalla frequenza degli eventi, dalla loro urgenza e dal volume dei dati.

### Sincronia, asincronia e code

Un'operazione **sincrona** trattiene il flusso chiamante finché non raggiunge il punto di completamento previsto. Un'operazione **asincrona** consente al programma di proseguire e ricevere in seguito una notifica o controllare l'esito. Asincrono non vuol dire automaticamente più rapido: permette soprattutto di organizzare meglio l'attesa.

Buffer e code separano produttore e consumatore. Se una stampante riceve dati a raffiche, una coda consente all'applicazione di consegnare il lavoro e continuare, mentre il dispositivo procede alla propria velocità. Se però i lavori arrivano più rapidamente di quanto siano smaltiti, la coda cresce: il ritardo viene differito, non eliminato.

Perdita, duplicazione e ordine sono problemi diversi. Un sistema di acquisizione deve stabilire che cosa accade quando il buffer è pieno, come riconoscere un trasferimento completato e come reagire a un errore. Queste decisioni incidono sulla correttezza del servizio oltre che sulle prestazioni.

### Applicazione al profilo

In un caso d'esame, il candidato può confrontare polling e interrupt indicando funzione, vantaggio, costo e contesto. Per diagnosticare un I/O lento deve osservare profondità delle code, tempi di servizio, quantità trasferite, errori e utilizzo del dispositivo. Dire soltanto «il disco è lento» non distingue un limite fisico, richieste casuali, contesa, driver o buffering inadeguato.

**Mini-caso.** Un servizio riceve documenti a raffiche e li protocolla più lentamente. Un buffer assorbe i picchi brevi; se il tasso medio di arrivo supera stabilmente quello di lavorazione, servono capacità aggiuntiva, regolazione del flusso o una diversa organizzazione. Aumentare indefinitamente il buffer rinvia la saturazione e può peggiorare il tempo di risposta.

Nell'orale, il confronto deve arrivare a una conseguenza pratica. Polling, interrupt, buffer e trasferimenti dedicati possono convivere nello stesso sistema. La scelta considera frequenza degli eventi, volume, urgenza, costo di gestione e rischio di perdita. Una definizione tecnica diventa così una decisione motivata.

## N-TR01-02-05 · Capire le prestazioni

La parola “veloce” è troppo generica. Prima del confronto va definito il risultato che interessa.

- **Latenza**: tempo necessario perché un’operazione o una risposta si completi.
- **Throughput**: quantità di lavoro completata nell’unità di tempo.
- **Tempo di risposta**: intervallo percepito fra richiesta e risultato, che può includere attese, elaborazione e trasferimenti.

Una minore latenza della singola operazione non garantisce il massimo throughput complessivo. Può accadere anche l'opposto: il sistema elabora molte richieste al secondo, ma una richiesta specifica riceve risposta troppo tardi.

### Colli di bottiglia e parallelismo

Il **collo di bottiglia** è la risorsa o la fase che limita il risultato osservato. Può essere CPU, memoria, storage, rete, dispositivo esterno, software o contesa fra attività. La diagnosi corretta parte dalla metrica e dal carico: non dall’acquisto automatico del componente con il numero commerciale più alto.

Il parallelismo può aumentare il lavoro svolto quando le attività possono procedere in modo indipendente. Non rende però parallela una parte intrinsecamente sequenziale e introduce costi di coordinamento, sincronizzazione e scambio dei dati.

### Misurare prima di intervenire

Una misura ha senso solo se specifica carico, intervallo e punto di osservazione. Il tempo della CPU, il tempo trascorso percepito dall'utente e il tempo passato in attesa di I/O descrivono fenomeni diversi. Anche una media può nascondere richieste molto lente: per un servizio al pubblico interessano spesso distribuzione e valori di coda, non soltanto il valore medio.

Il **benchmark** riproduce un carico definito per confrontare sistemi o configurazioni. Deve essere rappresentativo: un test che usa dati già in cache non descrive necessariamente un'importazione reale; un test con un solo utente non misura la contesa di cento accessi concorrenti. Modificare più componenti insieme rende inoltre difficile attribuire il risultato.

La capacità indica quanto lavoro il sistema può sostenere entro livelli di servizio accettabili. Quando il carico cresce, inizialmente il throughput può aumentare; vicino alla saturazione, le code e il tempo di risposta possono crescere rapidamente. Questo spiega perché un servizio apparentemente stabile degradi in modo improvviso nelle ore di punta.

### Diagnosi del collo di bottiglia

Un metodo ordinato comprende cinque mosse: definire il sintomo; scegliere la metrica; raccogliere evidenze su CPU, memoria, I/O e code; formulare un'ipotesi; modificare una variabile e misurare di nuovo. La correlazione temporale aiuta, ma non prova da sola la causa. Una CPU molto utilizzata può essere il limite oppure svolgere lavoro inutile provocato da un altro difetto.

Il parallelismo distingue almeno concorrenza e simultaneità. Più attività possono avanzare alternandosi su una CPU; con più unità di esecuzione alcune possono procedere nello stesso istante. Il beneficio massimo resta limitato dalle parti sequenziali e dai costi di coordinamento. Se molti lavoratori accedono alla stessa risorsa protetta, la contesa può annullare il vantaggio.

Scalabilità significa mantenere un comportamento utile al crescere del carico aggiungendo o organizzando risorse. Non coincide con una singola prestazione elevata. Un sistema può essere rapido per dieci utenti e degradare male al centesimo; un altro può avere una latenza iniziale maggiore ma sostenere meglio l'aumento.

### Applicazione al profilo

Una risposta tecnica non parte dalla prescrizione. «Aggiungere CPU» è una soluzione solo dopo aver dimostrato che il lavoro è limitato dal calcolo e può sfruttare la risorsa. Se il tempo è dominato da letture casuali, attese di rete o lock, l'investimento può incidere poco.

**Domanda-trappola.** Un throughput doppio implica tempo di risposta dimezzato? No. Le metriche descrivono aspetti diversi e dipendono dal carico. Il candidato deve dichiarare che cosa viene misurato e in quali condizioni.

Va considerato anche il costo dell'ottimizzazione. Ridurre di poco la latenza di un'operazione rara può essere meno utile che eliminare una coda frequente. Il funzionario ICT collega la misura all'obiettivo del servizio: tempi per l'utente, capacità nelle scadenze, affidabilità o uso efficiente delle risorse.

## N-TR01-02-06 · Il sistema operativo come gestore delle risorse

Il sistema operativo offre ai programmi un ambiente di esecuzione e governa l’accesso alle risorse. Non è soltanto l’interfaccia grafica vista dall’utente.

Un **programma** è un insieme di istruzioni memorizzate; un **processo** è un’istanza in esecuzione, con stato e risorse. Il sistema operativo decide quando assegnare tempo di CPU ai processi, ne conserva il contesto durante gli avvicendamenti e coordina le attese.

Nella gestione della memoria assegna spazi ai processi, protegge aree che non devono essere usate indebitamente e offre astrazioni che separano la visione del programma dalla disposizione fisica. Nella gestione dell’I/O usa driver e meccanismi di controllo per fornire interfacce più uniformi a dispositivi differenti.

Il file system organizza dati persistenti attraverso file, directory, metadati e permessi. Qui interessa la funzione di organizzazione, accesso e protezione; le operazioni pratiche su file e cartelle restano nel VOL-01.

La protezione tra processi impedisce che un programma possa leggere o modificare liberamente lo spazio di un altro. Il sistema operativo combina separazione degli indirizzi, modalità di esecuzione e controlli sugli accessi. Questa funzione non elimina ogni vulnerabilità, ma crea il confine entro cui applicazioni e utenti esercitano soltanto le autorizzazioni previste.

### Caso guidato: il gestionale rallenta durante l’importazione

Un ente importa un archivio molto grande. Durante l’operazione il gestionale risponde lentamente. Un collega propone di sostituire subito la CPU.

La diagnosi deve procedere per ipotesi verificabili:

1. definire la metrica: tempo totale dell’importazione o risposta delle altre funzioni;
2. osservare quali risorse sono sature;
3. distinguere elaborazione, lettura da storage, scrittura, memoria e attese;
4. verificare se più processi competono per la stessa risorsa;
5. provare l’intervento sulla risorsa limitante e misurare di nuovo.

Se la CPU attende lo storage, sostituirla con un modello più rapido può incidere poco. Se la trasformazione dei dati occupa stabilmente tutta la capacità di calcolo, la CPU è invece un candidato plausibile. Per formulare la diagnosi non basta una specifica tecnica isolata.

### Domanda da commissario

**Descriva il ciclo di esecuzione di un’istruzione e il ruolo della memoria.**

Una risposta ordinata parte dal prelievo dell’istruzione dalla memoria, prosegue con decodifica, acquisizione degli operandi, esecuzione e scrittura del risultato. L’unità di controllo coordina le fasi, l’ALU svolge le operazioni previste e i registri conservano le informazioni immediatamente necessarie. Cache e RAM appartengono alla gerarchia che alimenta la CPU, con compromessi diversi fra capacità e tempo di accesso.

### Domanda-trappola

**Aumentare la RAM rende sempre più veloce il processore?**

No. Più RAM può evitare la carenza di memoria e ridurre il ricorso a livelli persistenti più lenti. In determinati carichi, il sistema ne trae beneficio. La velocità interna della CPU però non cambia e un collo di bottiglia collocato altrove rimane.

### Errore tipico

Confrontare componenti usando una sola cifra. Frequenza, capacità o numero di unità non descrivono da soli le prestazioni osservate. Prima si identifica l’output richiesto, poi la metrica, infine la risorsa che limita quel carico.

### Checklist delle competenze specialistiche

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

Il sistema operativo realizza dunque una mediazione continua. Offre astrazioni stabili ai programmi, assegna risorse scarse, isola attività che non devono interferire e registra gli eventi necessari alla gestione. In una risposta concorsuale, questa sintesi va accompagnata da almeno un meccanismo concreto — scheduling, memoria virtuale, driver o permessi — e dalla relativa conseguenza operativa.

## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento consente di verificare la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-02-01` | Mini-caso. Una CPU più rapida non migliora sensibilmente un'elaborazione. |
| `N-TR01-02-02` | Quante configurazioni distingue? |
| `N-TR01-02-03` | Quiz 2 |
| `N-TR01-02-04` | Quiz 3 |
| `N-TR01-02-05` | Quiz 4 |
| `N-TR01-02-06` | Quiz 5 |

## ▣ Verifica

### Esercizio 1

Ordina dal livello normalmente più vicino alla CPU a quello destinato alla conservazione persistente: RAM, registri, storage, cache.

**Soluzione:** registri, cache, RAM, storage. L’ordine descrive la gerarchia funzionale generale, non una garanzia assoluta sulle prestazioni di ogni prodotto.

### Esercizio 2

Un servizio completa 500 richieste al secondo, ma una singola richiesta attende molto prima della risposta. Quale distinzione devi applicare?

**Soluzione:** throughput e latenza o tempo di risposta. Un throughput elevato non dimostra che ogni richiesta riceva risposta rapidamente.

### Quiz 1

Quale affermazione è corretta?

- A. La cache serve principalmente ad aumentare la capacità persistente.
- B. Un buffer elimina qualunque collo di bottiglia di I/O.
- C. Un processo è un programma in esecuzione con stato e risorse.
- D. La RAM modifica sempre la frequenza della CPU.

**Risposta corretta: C.** Le altre opzioni attribuiscono a cache, buffer e RAM effetti che non hanno necessariamente.

### Quiz 2

Quale situazione descrive meglio un cache miss?

- A. Il dato richiesto è già in un registro.
- B. Il dato non è nel livello di cache consultato e va cercato più lontano.
- C. Lo storage ha esaurito lo spazio.
- D. Il processo ha terminato l'esecuzione.

**Risposta corretta: B.** Il miss riguarda l'assenza del dato nella cache interrogata e comporta l'accesso a un livello successivo, normalmente più lento.

### Quiz 3

Quale affermazione distingue correttamente polling e interrupt?

- A. Il polling interroga lo stato; l'interrupt segnala un evento.
- B. L'interrupt elimina ogni costo di gestione.
- C. Il polling trasferisce sempre più dati.
- D. Sono due nomi dello stesso meccanismo.

**Risposta corretta: A.** Nel polling la CPU controlla ripetutamente; con l'interrupt riceve una segnalazione. Entrambe le modalità hanno costi e contesti appropriati.

### Quiz 4

Un sistema completa molte richieste al secondo, ma alcune attendono a lungo. Quale conclusione è corretta?

- A. Il throughput elevato esclude problemi.
- B. La latenza delle singole richieste deve essere misurata separatamente.
- C. Occorre aumentare subito la RAM.
- D. Il processore è necessariamente guasto.

**Risposta corretta: B.** Throughput e latenza non sono intercambiabili; una misura aggregata può nascondere code o richieste lente.

### Quiz 5

Che cosa distingue un programma da un processo?

- A. Il programma è il codice memorizzato; il processo è un'istanza in esecuzione con stato e risorse.
- B. Il processo è sempre un file.
- C. Il programma dispone sempre di una CPU dedicata.
- D. Non esiste alcuna distinzione.

**Risposta corretta: A.** Più processi possono derivare dallo stesso programma e possedere contesti di esecuzione distinti.

### Quiz 6

Qual è il primo passo corretto davanti a un rallentamento?

- A. Sostituire il componente con la frequenza più bassa.
- B. Definire sintomo, carico e metrica osservabile.
- C. Aumentare tutti i buffer.
- D. Disattivare lo scheduling.

**Risposta corretta: B.** Senza una metrica e condizioni definite non è possibile individuare il collo di bottiglia né verificare l'effetto dell'intervento.

## Da sapere in 5 righe

- L’architettura si comprende collegando CPU, memoria e I/O.
- I bit acquistano significato attraverso una codifica.
- La gerarchia di memoria bilancia capacità, latenza, costo e persistenza.
- Le prestazioni richiedono una metrica e l’individuazione del collo di bottiglia.
- Il sistema operativo gestisce e astrae le risorse per programmi e utenti.

## Riferimenti professionali essenziali

- *Il Metodo BANDO*, capitolo 10, paragrafi 1-2, per i prerequisiti di informatica di base.
- *The RISC-V Instruction Set Manual, Volume I — Unprivileged Architecture*, per la distinzione fra istruzioni, architettura e dettagli di implementazione.
- IEEE 754-2019, *Standard for Floating-Point Arithmetic*, per intervallo, precisione e arrotondamento.
- *The Unicode Standard* e *Unicode Character Encoding Model (UTR #17)*, per caratteri e forme di codifica.
- Documentazione ufficiale del kernel Linux su gestione della memoria e interrupt, usata qui a sostegno dei concetti generali e non delle API specifiche.
- Documentazione SPEC CPU sulle metriche orientate alla velocità e al throughput.
- Programma del singolo bando, che resta decisivo per stabilire profondità e lessico richiesti.
