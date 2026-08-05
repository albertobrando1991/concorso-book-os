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
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "cloud", "devops", "continuita"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 7
draft_stage: cross-reviewed
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

## Modelli cloud e responsabilità

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

Così emergono le zone grigie: il provider può garantire l’infrastruttura mentre l’ente mantiene account o configurazioni errate; il servizio tecnico può essere disponibile mentre il procedimento amministrativo non dispone di una modalità alternativa.

## Virtualizzazione, container e orchestrazione

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

## Cloud PA e percorso di migrazione

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

## DevOps, CI/CD e Infrastructure as Code

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

Il modello dichiarativo descrive lo stato desiderato; quello imperativo una sequenza di operazioni. IaC non garantisce correttezza: un errore codificato può essere replicato ovunque. Servono review, test, gestione dei secret, accessi controllati e verifica dello stato reale.

### Distribuzione e rollback

Il **rolling update** sostituisce gradualmente le istanze. Il **blue-green** prepara un ambiente parallelo e sposta il traffico dopo le verifiche. Il **canary release** espone inizialmente la versione a una quota limitata.

Queste tecniche non sostituiscono compatibilità dei dati e rollback. È utile separare **deployment** e **release**: il codice può essere distribuito senza attivare subito la funzione.

## Operabilità e osservabilità

### Metriche, log e trace

Il monitoraggio verifica condizioni note. L’osservabilità permette di comprendere lo stato interno attraverso i segnali prodotti, anche per problemi non previsti da una soglia.

- **metriche:** misure numeriche nel tempo;
- **log:** registrazioni di eventi con contesto;
- **trace:** percorso di una richiesta fra componenti;
- **eventi:** cambiamenti significativi, come un deployment.

I segnali sono complementari: la metrica mostra un aumento di latenza; la trace localizza il tratto lento; il log spiega un rifiuto del database; l’evento collega il problema a una modifica.

Dashboard e alert devono rappresentare il servizio. Un server può essere attivo mentre l’utente non completa la pratica. Gli alert devono essere azionabili, con impatto, contesto ed escalation.

### Capacità, elasticità e costi

Il capacity planning stima risorse e margini in base a domanda e obiettivi. L’autoscaling reagisce a segnali e politiche, ma non corregge una query inefficiente o una dipendenza satura.

Il consumo misurato richiede attribuzione dei costi, budget, allarmi e spegnimento delle risorse inutili. Nel governo FinOps il prezzo è uno dei criteri: continuità, sicurezza, competenze e reversibilità conservano il loro peso.

## Resilienza, backup e continuità operativa

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

## Caso guidato: migrazione di un servizio comunale

Un Comune deve migrare il portale per le richieste di occupazione del suolo pubblico, composto da front end, applicazione, database, archivio documentale, autenticazione, protocollo e pagamenti.

**Classificazione.** Il gruppo descrive dati e servizio, applica il percorso vigente e definisce attività essenziali e impatto dell’indisponibilità.

**Inventario.** Rileva versioni, volumi, picchi, API, licenze e dipendenze. Scopre che il protocollo accetta richieste solo da indirizzi autorizzati e che alcuni allegati sono su un file server locale.

**Strategia.** Front end e applicazione vengono containerizzati; il database passa a un servizio gestito compatibile; l’integrazione con il protocollo resta inizialmente ibrida. La strategia è quindi mista.

**Responsabilità.** Il provider governa infrastruttura e piattaforma secondo il servizio. Il Comune mantiene classificazione, utenti, configurazione, dati, controllo e continuità del procedimento.

**Rilascio.** La pipeline costruisce un’immagine identificata, esegue test e distribuisce in preproduzione. Il cutover segue la sincronizzazione dei dati; sono stabiliti stop e rollback.

**Esercizio.** Metriche misurano errori e latenza; trace e log seguono una richiesta. Backup e ripristino sono provati. RPO e RTO derivano dall’impatto.

**Uscita.** Il piano documenta esportazione, configurazioni, tempi, responsabilità e cancellazione finale.

Il caso è ben risolto quando impatti, architettura, responsabilità, controlli e recuperabilità restano collegati. Un elenco di strumenti, da solo, non dimostra la qualità della soluzione.

## Laboratorio: checklist di migrazione

| Area | Domanda | Evidenza |
| --- | --- | --- |
| Servizio | funzione e utenti? | scheda servizio |
| Dati | quali e come classificati? | esito classificazione |
| Dipendenze | sistemi, reti, identità, fornitori? | mappa |
| Carico | volumi, picchi, latenza? | misure e stime |
| Strategia | quale «R» e perché? | motivazione |
| Destinazione | requisiti e qualifica compatibili? | verifica vigente |
| Responsabilità | chi configura, osserva e ripristina? | matrice |
| Dati | copia e sincronizzazione? | piano dati |
| Test | quali criteri devono passare? | evidenze |
| Cutover | quando e chi decide? | runbook |
| Rollback | come si torna indietro? | procedura provata |
| Esercizio | metriche, log, trace e alert? | dashboard |
| Continuità | RPO, RTO, backup e alternative? | piano e test |
| Uscita | esportazione e cancellazione? | exit plan |

## Domanda da commissario

**«Come imposteresti la migrazione al cloud di un servizio pubblico?»**

Descriverei servizio, classificazione e impatti; inventarierei componenti e dipendenze; definirei requisiti e continuità; sceglierei strategia e destinazione motivate; assegnerei responsabilità; pianificherei dati, test, cutover e rollback; predisporrei osservabilità, backup, ripristino ed exit strategy. La tecnologia viene dopo il problema.

## Domanda-trappola

**«Se il database è replicato in un’altra zona, il backup non serve?»**

No. La replica sostiene disponibilità e ripartenza, ma può propagare cancellazioni, corruzioni o errori. Il backup conserva punti recuperabili secondo una retention e deve essere testato. Rispondono a rischi diversi.

## Errore tipico

Scegliere provider o orchestratore prima di classificare servizio, dipendenze e impatti produce una migrazione tecnicamente elegante ma incompatibile con dati, processi, continuità o uscita.

## Mini-esercizi e quiz

1. In SaaS l’ente conserva certamente:
   - A. manutenzione hardware
   - B. gestione corretta di utenti, dati e configurazioni proprie
   - C. patch dell’hypervisor
   - D. sostituzione dischi

2. Un container, rispetto a una VM ordinaria:
   - A. non usa CPU
   - B. condivide normalmente il kernel dell’host
   - C. contiene sempre un database
   - D. non usa rete

3. La continuous delivery:
   - A. elimina ogni approvazione
   - B. mantiene il software rilasciabile
   - C. coincide con il backup
   - D. richiede Kubernetes

4. Il percorso di una richiesta fra componenti è mostrato da:
   - A. trace
   - B. snapshot
   - C. template
   - D. RPO

5. Un RPO di due ore riguarda:
   - A. tempo di sostituzione server
   - B. perdita temporale massima di dati
   - C. durata del contratto
   - D. latenza

6. Spiega perché uno snapshot non è automaticamente un backup.

7. Indica due motivi per cui tre repliche non garantiscono da sole continuità.

**Soluzioni:** 1-B; 2-B; 3-B; 4-A; 5-B. Nelle risposte aperte devono comparire dominio di guasto, conservazione separata, ripristino, dipendenze condivise e procedure.

## Checklist finale

Verifica di aver:

- distinto caratteristiche, servizi e distribuzione;
- assegnato le responsabilità;
- separato VM, container, immagine, snapshot e backup;
- spiegato stato desiderato e orchestrazione;
- classificato prima della scelta;
- motivato migrazione e uscita;
- descritto pipeline, artefatti e gate;
- distinto integration, delivery e deployment;
- collegato IaC a versionamento e review;
- usato metriche, log e trace insieme;
- distinto ridondanza, replica, backup, DR e continuità;
- ricavato RPO e RTO dall’impatto;
- previsto cutover, rollback e prove.

## Da sapere in 5 righe

Il cloud è un modello elastico e misurato, non un server remoto. IaaS, PaaS e SaaS spostano il confine delle responsabilità senza annullare quelle dell’ente. Container e VM sono diversi e complementari. DevOps rende modifiche e infrastruttura versionate, verificabili e osservabili. Backup, disaster recovery e business continuity rispondono a domande differenti e devono essere provati.

## Riferimenti consolidati

- [[sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie]]
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]]
- [[sources/sicurezza-informatica-privacy-nis2-pa]]
- [[sources/reti-sistemi-infrastrutture-fonti-tecniche]]
- [[sources/campione-bandi-ict-pa-vol-08-2024-2026]]
- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]]
- [[topics/open-data-interoperabilita-cloud-pa]]
- [[topics/ict-digitale-cybersecurity-dati-concorsi-pa]]
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], § 17.

## Note di review

- Verificare prima del text freeze Regolamento unico, catalogo e terminologia ACN vigenti.
- Sottoporre virtualizzazione, container, CI/CD, IaC e osservabilità a cloud architect e platform/SRE engineer.
- Sottoporre backup, RPO/RTO, disaster recovery e continuità a review specialistica.
- Validare strategie e profondità rispetto ai bandi ufficiali del campione.
- Mantenere nei capitoli 8-9 sicurezza e IAM di dettaglio; nel capitolo 12 clausole e SLA.
