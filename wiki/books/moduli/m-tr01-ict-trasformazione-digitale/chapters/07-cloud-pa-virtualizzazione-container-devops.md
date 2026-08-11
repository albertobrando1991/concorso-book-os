---
id: chapter-m-tr01-07
type: book_chapter
title: "Cloud PA, virtualizzazione, container e DevOps"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["cloud pa", "virtualizzazione", "container", "devops", "osservabilità", "business continuity"]
entities: ["Agenzia per la cybersicurezza nazionale", "NIST", "Kubernetes", "OpenTelemetry"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/reti-sistemi-infrastrutture-fonti-tecniche", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.82
updated_at: 2026-08-10
created_at: 2026-07-28
review_required: false
canonical: true
tags: ["chapter", "m-tr01", "cloud", "devops", "continuita"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 7
draft_stage: cross-reviewed
format_version: 2
dati_operativi: []
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/reti-sistemi-infrastrutture-fonti-tecniche", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-07-piano-completamento"]
---

# Cloud PA, virtualizzazione, container e DevOps

Spostare un servizio pubblico «su Internet» non basta a modernizzarlo. Una migrazione al cloud cambia il modo in cui si erogano le risorse, si distribuiscono le modifiche e si affrontano i guasti. Cambia anche la ripartizione delle responsabilità.

In una prova tecnica, elencare IaaS, PaaS e SaaS serve a poco se il ragionamento si ferma lì. La risposta deve collegare il modello cloud alla classificazione dei dati, distinguere macchine virtuali e container e descrivere una pipeline controllata. Osservabilità, backup e continuità operativa completano il quadro.

## Obiettivo e confine con il volume base

Il capitolo 10, § 17, del VOL-01 introduce cloud computing, IaaS, PaaS e SaaS e i criteri generali per la PA. Qui quei prerequisiti diventano competenza specialistica.

Al termine del capitolo saprai:

- riconoscere caratteristiche e modelli del cloud;
- spiegare la ripartizione delle responsabilità;
- confrontare virtualizzazione e containerizzazione;
- impostare assessment e strategia di migrazione;
- descrivere DevOps, CI/CD e Infrastructure as Code;
- distinguere monitoraggio e osservabilità;
- collegare resilienza, backup, disaster recovery e continuità;
- costruire una checklist utilizzabile in prova.

Reti e troubleshooting sono nel capitolo 5; ciclo di vita, test e API nel capitolo 6; sicurezza nel capitolo 8; IAM e incident response nel capitolo 9; procurement e SLA contrattuali nel capitolo 12.

## Mappa BANDO: dalla classificazione all’esercizio

Nel bando cerca formule come *cloud computing*, *infrastrutture virtuali*, *container*, *orchestrazione*, *DevOps*, *CI/CD*, *monitoraggio*, *backup*, *disaster recovery* e *continuità operativa*. La profondità dipende dal profilo e dal tipo di prova.

| Segnale | Nucleo | Output |
| --- | --- | --- |
| IaaS/PaaS/SaaS | modelli e responsabilità | confronto motivato |
| Cloud PA, ACN | classificazione e qualificazione | piano di migrazione |
| Virtualizzazione | hypervisor, VM, immagini | schema host-guest |
| Container | immagini, runtime, orchestrazione | confronto VM-container |
| DevOps, CI/CD | pipeline, artefatti, rollback | flusso di rilascio |
| Observability | metriche, log, trace | diagnosi guidata |
| Backup, DR, BC | copie, RPO, RTO, piani | scenario di continuità |

Il metodo segue quattro passaggi: classificare, motivare, progettare e verificare. Prima si chiariscono servizio, dati e impatti. Su questa base si sceglie l’architettura e si dimostra che rilascio, esercizio e ripristino sono governati.

## N-TR01-07-01 · Quadro, modelli cloud e responsabilità

Il modello cloud va letto come un insieme di caratteristiche operative e di confini di responsabilità. La risposta utile non si limita alle sigle: collega servizio, dati, soggetti coinvolti e conseguenze per l'ente.

### Cinque caratteristiche essenziali

La definizione NIST riconosce il cloud attraverso cinque caratteristiche:

1. **servizio su richiesta**, con provisioning fortemente automatizzato;
2. **accesso ampio tramite rete**, mediante meccanismi standard;
3. **condivisione delle risorse**, assegnate dinamicamente a più consumatori;
4. **elasticità rapida**, per crescere o ridursi al variare del carico;
5. **servizio misurato**, così da osservare e rendicontare il consumo.

Queste proprietà distinguono il cloud da una semplice macchina remota. Un server accessibile via rete, assegnato manualmente e dimensionato una volta per tutte, può essere infrastruttura esterna senza offrire davvero il modello operativo del cloud.

La **scalabilità** è la capacità di sostenere più carico aggiungendo risorse. L’**elasticità** aggiunge l’adattamento dinamico, anche verso il basso. Lo scaling è verticale quando aumenta le risorse di una singola istanza, orizzontale quando aumenta le istanze.

### Modelli di servizio

| Modello | Il provider offre | L’amministrazione governa soprattutto |
| --- | --- | --- |
| IaaS | calcolo, rete, storage e virtualizzazione | guest OS, middleware, applicazioni, dati e configurazioni |
| PaaS | infrastruttura e piattaforma | applicazioni, dati, configurazioni e uso |
| SaaS | applicazione completa | utenti, dati, configurazione funzionale e processi |

Da IaaS a SaaS diminuisce la gestione tecnica diretta, ma non scompare la responsabilità dell’ente. Restano classificazione dei dati, scelta del servizio, identità, autorizzazioni, configurazione, controllo del fornitore, continuità del processo e possibilità di uscita.

Il modello **serverless** nasconde provisioning e gestione dei server al consumatore. Il termine non significa che i server non esistano.

### Modelli di distribuzione

Il **cloud pubblico** è offerto a una pluralità di clienti: «pubblico» non significa «della pubblica amministrazione». Il **cloud privato** è destinato a una sola organizzazione. Il **cloud ibrido** coordina ambienti differenti. Il **community cloud** è condiviso da organizzazioni con esigenze comuni.

Nelle architetture dei provider ricorrono:

- **regione**, area geografica in cui sono disponibili risorse;
- **zona**, dominio infrastrutturale separato;
- **tenancy**, modalità di assegnazione delle risorse a uno o più clienti.

Distribuire istanze su più zone può ridurre l’impatto di un guasto, ma non crea automaticamente continuità: servono dati coerenti, instradamento, capacità, procedure e test.

### Responsabilità condivisa

La linea di separazione fra provider e cliente varia con servizio e contratto. In IaaS l’ente governa una parte maggiore dello stack; in SaaS il provider ne gestisce una parte più ampia. Non è mai corretto concludere: «è nel cloud, quindi se ne occupa tutto il fornitore».

Per ogni componente occorre chiedere:

1. chi lo configura?
2. chi lo aggiorna?
3. chi ne osserva lo stato?
4. chi interviene e risponde se fallisce?

La matrice fa emergere le zone grigie: il provider può garantire l’infrastruttura mentre l’ente mantiene account o configurazioni errate; il servizio tecnico può essere disponibile mentre il procedimento amministrativo non dispone di una modalità alternativa.

In sede concorsuale conviene trasformare la responsabilità condivisa in una piccola matrice. Per esempio, in un servizio SaaS il fornitore può curare la disponibilità dell'applicazione, ma l'amministrazione deve decidere chi può accedere, con quali profili, quali dati inserire e come controllare le configurazioni che incidono sul procedimento. Se il servizio usa un'integrazione con un archivio dell'ente, occorre inoltre chiarire chi monitora il collegamento e chi comunica l'interruzione agli uffici. La risposta è più solida quando individua il componente, il responsabile, l'evidenza attesa e il punto di escalation.

La scelta del modello non discende solo dal carico previsto. Un'applicazione legacy con requisiti particolari può richiedere maggiore controllo dell'ambiente; un servizio standard può beneficiare di una piattaforma gestita. In entrambi i casi l'ente deve valutare competenze interne, vincoli sui dati, integrazioni, continuità e possibilità di cambiare soluzione. "Più gestito" non significa automaticamente "più adatto": sposta il confine tecnico, ma non elimina le decisioni organizzative.

## N-TR01-07-02 · Virtualizzazione, container e orchestrazione

Un candidato deve saper motivare la scelta senza ridurla a una preferenza di prodotto.

Qui la questione decisiva è capire che cosa viene isolato, come viene distribuito e quali dati devono sopravvivere al riavvio. La tecnologia scelta deve rendere l'esercizio più controllabile, non soltanto più rapido da avviare.

### Hypervisor e macchine virtuali

La virtualizzazione presenta risorse logiche separate sopra la stessa infrastruttura fisica. L’**hypervisor** crea e governa macchine virtuali, ripartendo CPU, memoria, storage e dispositivi. Quello di **tipo 1** opera direttamente sull’hardware; quello di **tipo 2** si appoggia a un sistema operativo host.

Ogni VM possiede normalmente sistema operativo guest, librerie e applicazioni. L’isolamento permette carichi differenti sullo stesso host, ma richiede gestione di immagini, patch, configurazioni e capacità.

Una **immagine** è una base da cui creare istanze; un **template** aggiunge spesso configurazioni e metadati. Lo **snapshot** registra lo stato in un momento dato, ma non è automaticamente un backup indipendente: può condividere storage, amministrazione e dominio di guasto con l’originale.

La sovra-allocazione aumenta l’efficienza quando i carichi non raggiungono insieme il massimo, ma produce contesa se le assunzioni sono errate. Le prestazioni vanno quindi misurate.

### Immagini e container

Un container esegue un processo isolato con codice e dipendenze, condividendo il kernel dell’host secondo il modello del runtime. Una **container image** è il pacchetto pronto all’esecuzione; il **registry** conserva e distribuisce immagini; il **runtime** ne governa esecuzione e ciclo di vita.

L’immagine deve essere identificabile, versionata e ricostruibile. Modificare manualmente un container in esecuzione crea differenze non tracciate: si produce invece una nuova immagine e si ricrea il workload.

I dati che devono sopravvivere alla sostituzione del container richiedono storage persistente progettato e protetto.

| Aspetto | VM | Container |
| --- | --- | --- |
| Unità | sistema virtuale con OS guest | processo con dipendenze |
| Kernel | normalmente proprio guest kernel | normalmente condiviso con l’host |
| Avvio | in genere più pesante | in genere più rapido |
| Portabilità | immagine dell’ambiente | immagine applicativa |
| Uso | OS diversi, legacy, isolamento infrastrutturale | servizi replicabili e distribuibili |

VM e container possono convivere: molti cluster di container funzionano sopra VM. La scelta dipende da requisiti, competenze, isolamento e carico.

### Orchestrazione e stato desiderato

Un orchestratore assegna workload ai nodi, mantiene repliche, espone servizi, distribuisce configurazioni e reagisce a determinati guasti.

Kubernetes è un esempio. Il suo principio centrale è la **riconciliazione**: si dichiara lo stato desiderato e il control plane confronta continuamente stato attuale e desiderato, adottando azioni correttive. Un **Pod** è la minima unità distribuibile e può contenere uno o più container co-localizzati.

L’orchestratore non rende affidabile un’applicazione per magia. Se tutte le repliche dipendono da un unico database fragile, quello resta un punto critico. Vanno progettati anche configurazioni, secret, storage, rete e limiti di risorse.

Un confronto utile parte dall'unità che si vuole governare. La VM incapsula un intero ambiente operativo e rende possibile eseguire sistemi diversi sullo stesso hardware; il container impacchetta soprattutto il processo applicativo con le sue dipendenze. Per questo un container non sostituisce automaticamente una VM e non ne eredita, da solo, le garanzie di isolamento, persistenza o continuità. In un servizio pubblico possono convivere: VM per componenti legacy o per delimitare ambienti, container per servizi che si aggiornano e si replicano con maggiore frequenza.

L'orchestrazione introduce una disciplina ulteriore. Il team descrive il numero di repliche, le risorse richieste, le configurazioni e le condizioni di salute; il sistema tenta di riportare il carico allo stato dichiarato. Questo rende visibile la differenza tra una ripartenza casuale e una procedura ripetibile, ma richiede immagini controllate, registri affidabili, configurazioni separate dal codice e limiti che impediscano a un singolo workload di consumare tutte le risorse. La domanda da evitare è "quale orchestratore usiamo?" prima di aver chiarito disponibilità, dipendenze, dati persistenti e competenze di esercizio.

## N-TR01-07-03 · Cloud PA e percorso di migrazione

Il piano deve indicare ciò che cambia, ciò che resta e come si controlla il passaggio.

Una migrazione ordinata parte dalla funzione pubblica, non dalla piattaforma. Ogni scelta deve lasciare una motivazione, una prova e una via di ritorno praticabile.

### Classificare prima di scegliere

La Strategia Cloud Italia si fonda su classificazione di dati e servizi, qualificazione dei servizi cloud e Polo Strategico Nazionale. La classificazione valuta l’impatto della compromissione e distingue dati e servizi **strategici**, **critici** e **ordinari**.

La sequenza conta. Prima si esaminano dati, funzioni, utenti, dipendenze, impatti e obblighi; solo dopo si individua una destinazione compatibile. Partire dal prodotto rovescia l’ordine del problema.

La qualificazione dei servizi cloud per la PA è di competenza dell’ACN. Il quadro consolidato comprende il Regolamento unico adottato nel 2024 e il catalogo dei servizi qualificati. Poiché disciplina e catalogo evolvono, ogni decisione richiede il controllo della versione vigente.

Il **Polo Strategico Nazionale** è un’infrastruttura ad alta affidabilità destinata, nel quadro della strategia, anche a dati e servizi critici e strategici. Non è la destinazione automatica di ogni applicazione.

### Assessment

Per ogni applicazione occorre rilevare:

- finalità, utenti e finestre di servizio;
- dati, classificazione e vincoli;
- componenti, versioni e manutenzione;
- dipendenze da database, directory, file, API, rete e dispositivi;
- volumi, picchi, latenza e capacità;
- identità e ruoli operativi;
- disponibilità, RPO e RTO;
- contratti, licenze, competenze e costi;
- backup, ripristino e modalità di uscita.

L’inventario evita di migrare l’applicazione scoprendo solo dopo che una dipendenza rimasta on premise rende il servizio lento o inutilizzabile.

### Strategie di migrazione

Le cosiddette «R» sono una tassonomia operativa:

- **rehost:** trasferimento con modifiche minime;
- **replatform:** modifica di alcuni componenti per usare servizi gestiti;
- **refactor:** riprogettazione sostanziale;
- **repurchase:** sostituzione con una soluzione acquistata come servizio;
- **retain:** mantenimento temporaneo motivato;
- **retire:** dismissione dopo aver gestito dati e dipendenze.

La strategia può differire fra componenti dello stesso servizio. Va scelta in base a benefici, rischio, tempi, competenze e reversibilità, non per moda.

### Portabilità, reversibilità ed exit strategy

La portabilità consente di spostare applicazioni o dati con sforzo accettabile. La reversibilità permette di ritornare o trasferire il servizio. L’exit strategy specifica:

- formati e modalità di esportazione;
- volumi, tempi e costi;
- dipendenze proprietarie;
- restituzione o cancellazione dei dati;
- trasferimento di configurazioni, log e documentazione;
- responsabilità durante la transizione;
- test della procedura.

Il lock-in può essere tecnologico, contrattuale, organizzativo o legato alle competenze. Deve essere gestito, non semplicemente dichiarato assente.

### Cutover e rollback

Il **cutover** è il passaggio controllato al nuovo ambiente. Richiede criteri di ingresso, sincronizzazione dei dati, test finali, comunicazioni e responsabilità. Il **rollback** riporta a uno stato precedente quando i criteri non sono soddisfatti.

Un rollback credibile indica fino a quando è possibile tornare indietro, come riallineare i dati e chi decide. Dopo nuove transazioni, non basta riavviare il vecchio ambiente.

La migrazione è quindi un cambiamento di servizio, non una copia di macchine. L'assessment deve produrre decisioni verificabili: quali componenti si spostano, quali restano temporaneamente dove sono, quale dipendenza condiziona il passaggio e quale prova dimostra che il nuovo ambiente funziona. Una scelta di rehost può ridurre il tempo iniziale, ma può conservare vincoli del sistema precedente; un refactor può migliorare portabilità o resilienza, ma aumenta il rischio di modifica. Non esiste una "R" migliore in astratto.

Nel contesto della PA, classificazione e qualificazione vanno lette prima dell'architettura di dettaglio. La disciplina Cloud Italia e il catalogo ACN sono soggetti ad aggiornamento: nella prova si descrive il metodo di verifica della destinazione compatibile, senza trasformare nel testo un catalogo di prodotti o una lista di soglie. L'evidenza finale comprende inventario, esito della classificazione, scelta motivata, piano di test, procedura di cutover, condizioni di rollback e responsabilità durante la transizione.

## N-TR01-07-04 · DevOps, CI/CD e Infrastructure as Code

La pipeline è una catena di responsabilità, non un semplice automatismo. Il codice viene associato a una richiesta, trasformato in un artefatto identificabile e sottoposto ai controlli adatti al suo impatto. L'artefatto verificato non dovrebbe cambiare mentre attraversa gli ambienti: altrimenti non si sa più se la produzione esegue ciò che è stato provato. Quando un controllo fallisce, il flusso deve fermarsi e produrre un'evidenza utile alla correzione.

Anche il rollback richiede preparazione. Una nuova versione può essere tecnicamente distribuibile ma incompatibile con una modifica del dato o con un'interfaccia già usata da altri sistemi. Per questo si definiscono compatibilità, criteri di annullamento, responsabilità e modalità di comunicazione. Il rilascio progressivo limita l'esposizione iniziale, ma non sostituisce test, osservazione e decisioni sulle conseguenze per gli utenti.

DevOps mette in relazione sviluppo, rilascio ed esercizio. Il suo risultato atteso è una modifica identificabile, verificata e recuperabile, non una sequenza più veloce di passaggi non controllati.

### DevOps come modello operativo

DevOps mette sviluppo e operazioni sullo stesso flusso di lavoro. Riduce i passaggi manuali poco trasparenti, accorcia i tempi di feedback e favorisce modifiche circoscritte, verificabili e recuperabili.

Gli elementi ricorrenti sono collaborazione, responsabilità sul servizio, automazione, versionamento, feedback, misurazione e miglioramento continuo. DevOps non coincide con un team, una qualifica o un prodotto.

### Pipeline CI/CD

Una pipeline tipica comprende:

1. acquisizione del codice;
2. build o packaging;
3. test automatici;
4. controlli di qualità e sicurezza;
5. produzione di un artefatto identificato;
6. promozione fra ambienti;
7. distribuzione;
8. verifica ed evidenze.

La **continuous integration** integra spesso le modifiche e le verifica automaticamente. La **continuous delivery** mantiene il software rilasciabile, lasciando possibile una decisione esplicita per la produzione. La **continuous deployment** distribuisce automaticamente ogni modifica che supera i gate.

L’automazione rende i controlli ripetibili; non li elimina. La pipeline può registrare approvazioni, separazione dei compiti ed evidenze. L’artefatto che supera i test dovrebbe essere lo stesso promosso negli ambienti successivi, perché ricostruirlo introduce differenze.

### Infrastructure as Code

Con l’**Infrastructure as Code** l’infrastruttura è descritta in file versionati e applicata automaticamente. Le modifiche diventano confrontabili, revisionabili e ripetibili.

Il modello dichiarativo descrive lo stato desiderato; quello imperativo una sequenza di operazioni. IaC non garantisce correttezza: un errore codificato può essere replicato ovunque. Servono revisioni, test, gestione separata dei segreti, accessi controllati e confronto con lo stato reale.

### Distribuzione e rollback

Il **rolling update** sostituisce gradualmente le istanze. Il **blue-green** prepara un ambiente parallelo e sposta il traffico dopo le verifiche. Il **canary release** espone inizialmente la versione a una quota limitata.

Queste tecniche non sostituiscono compatibilità dei dati e rollback. È utile separare **deployment** e **release**: il codice può essere distribuito senza attivare subito la funzione.

Un processo DevOps maturo non accelera le modifiche saltando i controlli. Li rende osservabili e ripetibili. Ogni passaggio deve poter rispondere a quattro domande: quale modifica è stata richiesta, quale artefatto è stato verificato, chi ha autorizzato il passaggio e quale evidenza dimostra l'esito. Questa catena è utile anche quando lo sviluppo è affidato a un fornitore, perché permette all'amministrazione di governare il servizio senza confondere la consegna del codice con la sua effettiva messa in esercizio.

L'Infrastructure as Code applica lo stesso principio alla configurazione. Una modifica a rete, capacità o ambiente non resta in una console amministrativa priva di storia: viene proposta, letta, testata e applicata con un identificativo. Il vantaggio non è l'assenza di errori, ma la possibilità di confrontare lo stato previsto con quello reale e di riprodurre un ambiente. Gli elementi sensibili, come segreti e credenziali, non vanno copiati nei file ordinari: richiedono gestione separata e accessi controllati. Dopo un rilascio il lavoro continua con la verifica delle funzioni, delle prestazioni e degli effetti sui dati.

## N-TR01-07-05 · Operabilità, osservabilità, capacità e costi

La capacità non riguarda soltanto il numero di server. Comprende connessioni, code, spazio, limiti imposti da servizi esterni e persone in grado di intervenire. Un piano di capacità confronta il profilo storico con gli eventi attesi, dichiara quale margine è necessario e stabilisce cosa fare quando il margine si riduce. Questo evita sia il sovradimensionamento costoso sia una reazione tardiva durante una scadenza.

L'osservabilità è utile anche dopo una modifica. Si confrontano i segnali prima e dopo il rilascio, si verificano errori, tempi di completamento e comportamento delle integrazioni. Se gli utenti non riescono a concludere una pratica, il fatto che i singoli componenti risultino attivi non basta. Occorre seguire la transazione, individuare il punto di blocco e registrare la decisione presa. Lo stesso ragionamento aiuta a discutere il costo: una spesa va collegata a capacità effettivamente richiesta, finestra di utilizzo, livello di continuità e rischio che si intende ridurre.

La revisione periodica trasforma i dati raccolti in gestione: si eliminano indicatori che non guidano alcuna azione, si affinano le soglie che producono falsi allarmi e si aggiornano le procedure quando il servizio o le sue dipendenze cambiano.

Un servizio governato produce segnali leggibili e li collega a decisioni. Osservare non significa accumulare dati: significa poter spiegare un degrado, decidere una priorità e verificare se l'intervento ha funzionato.

### Metriche, log e trace

Il monitoraggio verifica condizioni note. L’osservabilità permette di comprendere lo stato interno attraverso i segnali prodotti, anche per problemi non previsti da una soglia.

- **metriche:** misure numeriche nel tempo;
- **log:** registrazioni di eventi con contesto;
- **trace:** percorso di una richiesta fra componenti;
- **eventi:** cambiamenti significativi, come un deployment.

I segnali sono complementari: la metrica mostra un aumento di latenza; la trace localizza il tratto lento; il log spiega un rifiuto del database; l’evento collega il problema a una modifica.

Pannello operativo e alert devono rappresentare il servizio. Un server può essere attivo mentre l’utente non completa la pratica. Gli alert devono essere azionabili, con impatto, contesto ed escalation.

### Capacità, elasticità e costi

Il capacity planning stima risorse e margini in base a domanda e obiettivi. L’autoscaling reagisce a segnali e politiche, ma non corregge una query inefficiente o una dipendenza satura.

Il consumo misurato richiede attribuzione dei costi, budget, allarmi e spegnimento delle risorse inutili. Nel governo FinOps il prezzo è uno dei criteri: continuità, sicurezza, competenze e reversibilità conservano il loro peso.

Operare un servizio significa collegare segnali tecnici e risultato per l'utente. Un pannello operativo che mostra solo CPU e memoria aiuta il gestore, ma non basta a capire se una pratica viene protocollata o se un pagamento termina correttamente. Per questo si definiscono indicatori del servizio, finestre temporali, soglie, destinatari degli avvisi e procedure di escalation. Un alert utile contiene almeno il sintomo, l'impatto presunto, il componente coinvolto e il primo controllo da eseguire.

Metriche, log e trace svolgono ruoli diversi. La metrica quantifica un fenomeno nel tempo, il log conserva un evento con il suo contesto e la trace ricostruisce il cammino di una singola richiesta. Durante un rallentamento del portale, l'aumento della latenza può segnalare il problema, una trace può mostrare che il tempo si concentra sull'integrazione esterna e i log possono indicare rifiuti o timeout. Nessun segnale, isolato, sostituisce gli altri.

Capacità e costi richiedono la stessa disciplina: si misurano domanda, picchi, margini e consumo, poi si assegnano responsabilità per le decisioni. Autoscaling e spegnimento programmato sono opzioni, non formule universali. Un aumento automatico delle istanze non risolve una dipendenza saturata, un limite di database o un errore applicativo che moltiplica le richieste. Il candidato deve dimostrare di saper scegliere una misura, osservare l'effetto e riesaminare la decisione.

## N-TR01-07-06 · Resilienza, backup, disaster recovery e continuità operativa

Ogni scelta resta verificabile nel tempo.

La scelta delle copie e delle architetture deve quindi essere proporzionata: non tutti i servizi richiedono la stessa rapidità di recupero, ma nessun servizio essenziale può basarsi su un ripristino mai eseguito.

La continuità richiede di distinguere ciò che riduce l'interruzione da ciò che permette di recuperare dati e servizi dopo un evento grave. La misura corretta dipende dall'impatto della funzione pubblica e deve essere dimostrata con prove.

### Resilienza e alta disponibilità

La resilienza è la capacità di assorbire guasti, adattarsi e ripristinare. L’alta disponibilità riduce le interruzioni mediante ridondanza, bilanciamento, replica e rimozione dei punti singoli di guasto.

La ridondanza funziona solo se i componenti non condividono lo stesso dominio di guasto. Due istanze sul medesimo host non proteggono dal guasto dell’host. Due zone non proteggono da una configurazione errata distribuita ovunque.

La **degradazione controllata** mantiene le funzioni essenziali quando una parte non è disponibile. La priorità deriva dall’impatto sul servizio pubblico.

### Backup, snapshot e replica

Il backup è una copia destinata al ripristino. Può essere:

- **completo**, se copia tutto l’insieme previsto;
- **incrementale**, se copia le modifiche dall’ultimo backup;
- **differenziale**, se copia le modifiche dall’ultimo completo.

Vanno definite frequenza, conservazione, cifratura, accessi, separazione, immutabilità quando appropriata e cancellazione.

Uno **snapshot** registra rapidamente uno stato; una **replica** mantiene una copia aggiornata. Nessuno dei due è automaticamente un backup. La replica può propagare cancellazioni o corruzioni; lo snapshot può condividere il dominio di guasto.

Un job concluso con esito positivo dimostra che la copia è stata eseguita, non che il ripristino funzionerà. La verifica richiede il recupero effettivo dei dati entro l’obiettivo e controlla integrità, dipendenze, credenziali, procedure e tempi.

### RPO e RTO

Il **Recovery Point Objective (RPO)** esprime la perdita temporale massima di dati tollerabile. Il **Recovery Time Objective (RTO)** esprime il tempo obiettivo entro cui il servizio deve tornare utilizzabile.

RPO e RTO derivano dall’analisi d’impatto. Obiettivi più stringenti richiedono normalmente architetture e costi maggiori; non vanno copiati da valori standard.

### Disaster recovery e business continuity

Il **disaster recovery** riguarda il ripristino di sistemi e servizi dopo un evento grave: architettura alternativa, copie, priorità, ruoli, failover e failback.

La **business continuity** è più ampia: mantiene o riprende le attività essenziali mediante persone, sedi, fornitori, comunicazioni e anche procedure manuali temporanee.

| Concetto | Domanda |
| --- | --- |
| Alta disponibilità | come riduco le interruzioni ordinarie? |
| Backup | da quale copia recupero dati e configurazioni? |
| Disaster recovery | come ripristino i sistemi dopo un evento grave? |
| Business continuity | come mantengo le funzioni essenziali dell’ente? |

Un piano acquista valore operativo solo quando viene provato. Simulazioni e prove di ripristino fanno emergere dipendenze dimenticate, accessi scaduti, documentazione incompleta e tempi irrealistici.

RPO e RTO non sono promesse generiche di "ripartenza rapida". Il primo impone di stabilire quale quantità di dati può andare persa fra due punti di ripristino; il secondo impone di stabilire entro quando la funzione deve tornare utilizzabile. Se un servizio acquisisce pratiche fino a una scadenza, un RPO troppo ampio può rendere necessario ricostruire molte operazioni; se la funzione è indispensabile in una finestra amministrativa, un RTO troppo lungo può interrompere il procedimento. Gli obiettivi nascono dall'analisi d'impatto e vanno tradotti in copie, procedure, ruoli e prove.

Una soluzione resiliente deve considerare anche i guasti comuni. Repliche nello stesso dominio di guasto, credenziali disponibili solo a una persona, runbook non aggiornati o un collegamento esterno non alternativo possono vanificare l'architettura. Il test di ripristino non è un adempimento conclusivo: misura tempi, integrità dei dati, sequenza delle dipendenze, comunicazioni e capacità di operare in modalità degradata. La business continuity completa il disaster recovery perché decide come l'ente continua le attività essenziali mentre i sistemi sono ripristinati.

## ▣ Verifica 07.A

### Caso ragionato: migrazione di un servizio comunale

Un Comune deve migrare il portale per le richieste di occupazione del suolo pubblico. Il servizio comprende front end, applicazione, database, archivio documentale, autenticazione, protocollo e pagamenti. L'obiettivo non è trasferire un server, ma mantenere il procedimento accessibile e recuperabile.

**Classificazione e inventario.** Il gruppo descrive dati e servizio, applica il percorso vigente di classificazione e definisce le attività essenziali e l'impatto dell'indisponibilità. Rileva versioni, volumi, picchi, API, licenze e dipendenze. Scopre che il protocollo accetta richieste solo da indirizzi autorizzati e che alcuni allegati sono ancora su un file server locale.

**Scelta motivata.** Front end e applicazione diventano workload containerizzati; il database passa a un servizio gestito compatibile; l'integrazione con il protocollo resta inizialmente ibrida. Questa scelta non elimina il rischio: rende esplicite le dipendenze da testare. Il Comune verifica che la destinazione sia compatibile con la classificazione e con la disciplina vigente, senza assumere che qualunque servizio cloud sia idoneo.

**Rilascio ed esercizio.** La pipeline costruisce un'immagine identificata, esegue i controlli e distribuisce in preproduzione. Il cutover avviene dopo la sincronizzazione dei dati e una prova completa della pratica. Sono definiti il punto di stop, l'autorità che decide il passaggio e il rollback. In esercizio metriche misurano errori e latenza, trace e log seguono una richiesta, mentre backup e ripristino sono provati. RPO e RTO derivano dall'impatto sulle pratiche e non da valori scelti per consuetudine.

**Uscita.** Il piano specifica esportazione dei dati, configurazioni, tempi, responsabilità e cancellazione finale. Il caso è ben risolto quando impatti, architettura, responsabilità, controlli e recuperabilità restano collegati. Un elenco di strumenti non dimostra la qualità della soluzione.

### Laboratorio: checklist di migrazione

| Area | Domanda | Evidenza |
| --- | --- | --- |
| Servizio | Quale funzione e quali utenti supporta? | Scheda del servizio |
| Dati | Quali dati tratta e come sono classificati? | Esito della classificazione |
| Dipendenze | Quali sistemi, reti, identità e fornitori coinvolge? | Mappa delle dipendenze |
| Carico | Quali volumi, picchi e tempi di risposta sono attesi? | Misure e stime |
| Strategia | Quale strategia di migrazione e perché? | Motivazione scritta |
| Destinazione | I requisiti e la qualificazione sono compatibili? | Verifica vigente |
| Responsabilità | Chi configura, osserva e ripristina? | Matrice dei ruoli |
| Test | Quali criteri devono essere superati? | Evidenze di prova |
| Cutover e rollback | Quando si passa e come si torna indietro? | Runbook provato |
| Esercizio | Quali metriche, log, trace e alert servono? | Pannello operativo e procedura |
| Continuità | Quali RPO, RTO, backup e alternative sono necessari? | Piano e test |
| Uscita | Come avvengono esportazione e cancellazione? | Exit plan |

### Domanda da commissario

**"Come imposteresti la migrazione al cloud di un servizio pubblico?"**

Descriverei servizio, classificazione e impatti; inventarierei componenti e dipendenze; definirei requisiti e continuità; sceglierei strategia e destinazione motivate; assegnerei responsabilità; pianificherei dati, test, cutover e rollback; predisporrei osservabilità, backup, ripristino ed exit strategy. La tecnologia viene dopo il problema.

### Domanda-trappola

**"Se il database è replicato in un'altra zona, il backup non serve?"**

No. La replica sostiene disponibilità e ripartenza, ma può propagare cancellazioni, corruzioni o errori. Il backup conserva punti recuperabili secondo una retention e deve essere testato. Rispondono a rischi diversi.

### Errore tipico

Scegliere provider o orchestratore prima di classificare servizio, dipendenze e impatti produce una migrazione tecnicamente elegante ma incompatibile con dati, processi, continuità o uscita.

### Quiz 1 — Responsabilità in SaaS

In un servizio SaaS l'ente conserva certamente:

- A. manutenzione dell'hardware;
- B. gestione corretta di utenti, dati e configurazioni proprie;
- C. patch dell'hypervisor;
- D. sostituzione dei dischi.

**Risposta corretta: B.** Il perimetro tecnico del provider è più ampio rispetto a IaaS, ma l'ente mantiene responsabilità su uso, accessi, dati, configurazioni e continuità del proprio procedimento.

### Quiz 2 — Container e VM

Un container, rispetto a una VM ordinaria:

- A. non usa CPU;
- B. condivide normalmente il kernel dell'host;
- C. contiene sempre un database;
- D. non usa rete.

**Risposta corretta: B.** Il container isola il processo e le dipendenze secondo il runtime, mentre una VM include normalmente un sistema operativo guest. Le due tecniche possono convivere.

### Quiz 3 — Continuous delivery

La continuous delivery:

- A. elimina ogni approvazione;
- B. mantiene il software rilasciabile;
- C. coincide con il backup;
- D. richiede Kubernetes.

**Risposta corretta: B.** Il software rimane in una condizione verificata e rilasciabile; l'attivazione in produzione può richiedere una decisione esplicita e controlli aggiuntivi.

### Quiz 4 — Segnali di osservabilità

Il percorso di una richiesta fra componenti è mostrato da:

- A. una trace;
- B. uno snapshot;
- C. un template;
- D. l'RPO.

**Risposta corretta: A.** Le trace permettono di seguire una richiesta tra servizi; metriche e log restano complementari per misurare il fenomeno e leggerne il contesto.

### Quiz 5 — RPO

Un RPO di due ore riguarda:

- A. il tempo di sostituzione di un server;
- B. la perdita temporale massima di dati tollerabile;
- C. la durata del contratto;
- D. la latenza della rete.

**Risposta corretta: B.** L'RPO esprime quanto indietro nel tempo può collocarsi il punto di ripristino; l'RTO riguarda invece il tempo entro cui il servizio deve tornare utilizzabile.

### Quiz 6 — Snapshot e backup

Perché uno snapshot non è automaticamente un backup?

**Risposta corretta: perché può condividere storage, amministrazione o dominio di guasto con l'originale.** Per essere utile al ripristino, una copia deve rispettare la conservazione prevista e la procedura deve essere provata.

### Quiz 7 — Repliche e continuità

Indica due motivi per cui tre repliche non garantiscono da sole la continuità.

**Risposta corretta: le repliche possono condividere un dominio di guasto e possono dipendere dallo stesso database, collegamento, configurazione o credenziale.** La continuità richiede anche procedure, ruoli, dati coerenti e test.

### Mini-esercizio

Per un servizio di prenotazione comunale descrivi, in dieci righe, una dipendenza critica, il segnale che ne mostrerebbe il degrado, il proprietario della correzione e la prova che conferma il ripristino. Poi indica se il caso richiede alta disponibilità, backup, disaster recovery o una combinazione delle tre misure.

### Checklist finale

Verifica di aver distinto caratteristiche, servizi e modelli di distribuzione; assegnato le responsabilità; separato VM, container, immagine, snapshot e backup; spiegato stato desiderato e orchestrazione; classificato prima della scelta; motivato migrazione e uscita; descritto pipeline, artefatti e controlli; distinto integration, delivery e deployment; collegato IaC a versionamento e review; usato metriche, log e trace insieme; distinto ridondanza, replica, backup, disaster recovery e continuità; ricavato RPO e RTO dall'impatto; previsto cutover, rollback e prove.

### Da sapere in 5 righe

Il cloud è un modello elastico e misurato, non un server remoto. IaaS, PaaS e SaaS spostano il confine delle responsabilità senza annullare quelle dell'ente. Container e VM sono diversi e complementari. DevOps rende modifiche e infrastruttura versionate, verificabili e osservabili. Backup, disaster recovery e business continuity rispondono a domande diverse e devono essere provati.

### Riferimenti normativi e professionali essenziali

- NIST SP 800-145, *The NIST Definition of Cloud Computing*.
- Strategia Cloud Italia e documentazione ACN su classificazione e qualificazione dei servizi cloud per la PA.
- Documentazione Kubernetes sui container, sugli oggetti e sui Pod.
- Documentazione OpenTelemetry su metriche, log e trace.
- NIST SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*.