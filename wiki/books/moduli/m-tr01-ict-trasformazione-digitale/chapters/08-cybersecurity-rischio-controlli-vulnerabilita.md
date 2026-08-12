---
id: chapter-m-tr01-08
type: book_chapter
title: "Cybersecurity operativa: rischio, controlli e vulnerabilità"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["cybersecurity", "risk assessment", "vulnerabilità", "secure software", "software supply chain"]
entities: ["Agenzia per la cybersicurezza nazionale", "NIST", "OWASP", "CVE", "CWE", "FIRST", "CISA"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.84
updated_at: 2026-08-11
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "cybersecurity", "risk", "vulnerability"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 8
draft_stage: format-2-retrofit
format_version: 2
dati_operativi: []
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-08-piano-completamento"]
---

# Cybersecurity operativa: rischio, controlli e vulnerabilità

Una vulnerabilità critica non coincide automaticamente con il rischio più urgente per un ente. La priorità dipende dal servizio interessato, dall’esposizione, dalla possibilità di sfruttamento, dagli impatti e dai controlli già presenti. La cybersecurity operativa traduce queste informazioni tecniche in decisioni motivate.

Il percorso parte dagli asset. Collega minacce e vulnerabilità a scenari concreti, valuta il rischio e seleziona i controlli. Affronta poi la correzione delle debolezze, lo sviluppo sicuro e la software supply chain, dove possono nascere vulnerabilità già prima del rilascio.

## Obiettivo e confine con il volume base

Il VOL-01, capitolo 10, § 6, tratta sicurezza di base, password, MFA, phishing, malware, antivirus, firewall, backup, aggiornamenti e inquadramento generale NIS2. Il capitolo li assume come prerequisiti.

Al termine saprai:

- distinguere asset, minaccia, vulnerabilità, evento, impatto e rischio;
- costruire una valutazione con scale dichiarate;
- distinguere rischio inerente e residuo;
- scegliere e classificare controlli;
- impostare threat modeling e vulnerability management;
- spiegare secure SDLC, secure coding e supply chain;
- produrre una risk matrix e una scheda di trattamento.

Continuità e backup sono nel capitolo 7. IAM, crittografia, logging e risposta all’incidente sono nel capitolo 9. Requisiti contrattuali e governo dei fornitori sono nel capitolo 12.

## Mappa BANDO: dal contesto al trattamento

| Formula nel bando | Nucleo | Output |
| --- | --- | --- |
| rischio cyber, risk assessment | scenario, probabilità, impatto | risk matrix |
| controlli, misure di sicurezza | natura, funzione, adeguatezza | piano di trattamento |
| vulnerability management | scoperta, priorità, remediation | registro vulnerabilità |
| threat modeling | asset, flussi, confini, minacce | modello di minaccia |
| secure coding, OWASP | debolezze e pratiche preventive | analisi applicativa |
| supply chain, SBOM | dipendenze, pipeline, artefatti | verifica di filiera |

In prova conviene seguire un ordine stabile: contesto, asset, scenario, rischio, trattamento, evidenza e riesame. Lo strumento scelto è secondario rispetto alla coerenza del ragionamento.

## N-TR01-08-01 · Obiettivi di sicurezza e asset

### Obiettivi di sicurezza e asset

### Proprietà da proteggere

La triade CIA riassume tre proprietà:

- **riservatezza:** informazioni accessibili soltanto ai soggetti autorizzati;
- **integrità:** dati e sistemi non alterati in modo improprio e modifiche rilevabili;
- **disponibilità:** informazioni e servizi accessibili quando servono.

Si aggiungono, secondo il contesto, autenticità, tracciabilità e accountability. Il non ripudio riguarda la capacità di impedire che un soggetto neghi in modo plausibile una determinata azione, quando il sistema e il quadro applicabile lo consentono. Queste proprietà non sono intercambiabili: la cifratura può sostenere la riservatezza, ma non garantisce da sola disponibilità o correttezza del processo.

### Asset, valore e dipendenze

Un **asset** è qualcosa che ha valore per l’organizzazione e richiede protezione. Può essere:

- informativo, come un archivio;
- tecnologico, come server, applicazioni e reti;
- umano, come competenze e ruoli;
- fisico, come locali e apparati;
- organizzativo, come procedure e reputazione;
- di servizio, come la capacità di erogare una prestazione pubblica.

L’inventario registra responsabile, collocazione, dipendenze, criticità e ciclo di vita. Un asset isolato sulla carta può dipendere da identità, DNS, connettività, provider e personale reperibile. Senza tali relazioni, l’analisi sottostima i punti di guasto.


### Valore e responsabilità dell'asset

La classificazione non parte dalla tecnologia, ma dal servizio che l'ente deve rendere. Un archivio può essere tecnicamente ordinario e tuttavia essenziale se blocca una graduatoria, un pagamento o una pratica con una scadenza. Per ogni asset occorre quindi chiedersi quale risultato pubblico sostiene, chi lo usa, quali dati tratta, quale proprietà CIA è più esposta e quali altri elementi devono funzionare insieme. Un portale che sembra autonomo può dipendere dal servizio di identità, dal dominio, dalla rete, dall'archivio documentale, dal fornitore e da persone con compiti distinti.

Il responsabile dell'asset non coincide sempre con chi amministra il server. Il primo deve chiarire il valore del servizio, le conseguenze di un fermo e le priorità; il secondo può gestire una configurazione o un controllo. Questa separazione evita una valutazione fatta solo sul valore tecnico del componente. In prova è utile esplicitare sia l'asset sia la dipendenza: "la disponibilità del portale dipende anche dall'identità digitale e dal deposito dei documenti" è una frase più verificabile di "proteggerei il server".

Un inventario utile non è un elenco statico. Collega asset, proprietario, collocazione, versione, dipendenze, dati trattati e criticità. Le informazioni consentono di aggiornare l'analisi quando cambia un'integrazione o un fornitore. L'errore opposto consiste nel classificare tutti gli asset come critici: così la priorità perde significato. La criticità deve derivare dal servizio, dalle persone coinvolte, dalle conseguenze e dalle alternative disponibili.


### Priorità legata al servizio

Considera due asset: un archivio di manuali pubblici e il registro che abilita un pagamento dovuto. Entrambi contengono informazioni e richiedono protezione, ma l'interruzione non produce lo stesso effetto. Nel secondo caso la disponibilità può essere decisiva in una data precisa; nel primo può prevalere l'integrità delle versioni pubblicate. Questa differenza deve comparire nella valutazione, altrimenti la scelta dei controlli rimane astratta.

Le dipendenze rendono visibile un altro aspetto: la sicurezza è una proprietà del servizio, non del singolo apparato. Se l'accesso al portale dipende da un componente esterno, la sua indisponibilità può interrompere la prestazione anche con il database integro. Il candidato può rappresentare il legame con una frase semplice: servizio, asset, dipendenza, proprietà da proteggere e conseguenza. La stessa traccia rende verificabile il ragionamento e consente di aggiornare la valutazione quando cambiano architettura o responsabilità.

Infine, valore non significa solo costo di sostituzione. Comprende obblighi di servizio, continuità amministrativa, affidabilità delle decisioni e fiducia degli utenti. Un asset non critico oggi può diventarlo in una finestra concorsuale o in prossimità di una scadenza. Per questo la classificazione deve avere un riesame, non un'etichetta definitiva.

## N-TR01-08-02 · Minacce, vulnerabilità e scenari


### Inquadramento: un linguaggio senza ambiguità

Una **minaccia** è una circostanza o causa potenziale capace di produrre un evento dannoso. Il **threat actor** è il soggetto che può agire intenzionalmente; non tutte le minacce, però, hanno un attore ostile: esistono errori, guasti ed eventi ambientali.

Una **vulnerabilità** è una debolezza che può essere sfruttata o contribuire al danno. Può trovarsi nel codice, nella configurazione, nel processo, nelle persone o nell’architettura. L’**exploit** è un mezzo o una tecnica che sfrutta una vulnerabilità. Il **vettore di attacco** è il percorso usato per raggiungere il bersaglio.

L’**evento** è ciò che accade; l’**impatto** è la conseguenza per l’organizzazione. Il **rischio** combina incertezza, probabilità o verosimiglianza e conseguenze rispetto agli obiettivi.

Esempio: il portale usa un componente vulnerabile (vulnerabilità); un attore invia una richiesta costruita per sfruttarlo (minaccia e vettore); il componente esegue un’operazione non prevista (evento); pratiche e servizio diventano indisponibili (impatto).

### Superficie di attacco e scenario

La **superficie di attacco** comprende punti attraverso i quali un sistema può essere raggiunto o influenzato: interfacce, API, account, dipendenze, dispositivi, persone e processi. Ridurla significa eliminare funzioni inutili, limitare esposizioni e controllare interazioni.

Uno scenario di rischio deve indicare:

1. asset e obiettivo compromesso;
2. fonte o attore della minaccia;
3. vulnerabilità e condizioni;
4. evento temuto;
5. conseguenze.

La formula «rischio ransomware alto» è troppo generica. Bisogna precisare il servizio coinvolto, il percorso d’attacco, le dipendenze e l’impatto atteso.


### Dallo scenario alla decisione

Uno scenario ben scritto rende controllabile il ragionamento. Indica un asset, una condizione di debolezza, una minaccia, un percorso plausibile, un evento e una conseguenza. Non richiede la descrizione di tecniche offensive: basta spiegare perché quella combinazione può compromettere una proprietà del servizio. Per esempio, una funzione esposta e una dipendenza non aggiornata non sono già un incidente. Diventano uno scenario quando si chiarisce che un soggetto esterno può raggiungere la funzione e che l'evento temuto comporta accesso improprio o indisponibilità.

La superficie di attacco include la pagina visibile del portale, API, account, canali di amministrazione, componenti di terze parti, processi di aggiornamento e confini fra ambienti. Ridurla può significare dismettere un'interfaccia non necessaria, limitare un privilegio, separare un ambiente di prova o rendere tracciabile una modifica. Il candidato deve usare questi elementi per motivare una scelta, non per compilare un elenco di parole chiave.

Nel linguaggio della prova, minaccia, vulnerabilità ed evento devono restare distinti. Una vulnerabilità è una debolezza; la minaccia è una causa possibile; l'evento è ciò che accade; l'impatto è la conseguenza. Il rischio esprime la possibilità e la gravità della conseguenza rispetto agli obiettivi. Confondere il punteggio tecnico di una debolezza con il rischio dell'ente porta a una priorità priva di contesto.


### Condizioni che cambiano lo scenario

La medesima vulnerabilità può produrre scenari diversi. Su un componente non esposto e isolato il percorso di attacco può essere poco plausibile; sullo stesso componente raggiungibile da Internet e collegato a documenti sensibili la priorità cambia. Anche le credenziali, la segmentazione, la validazione lato server e la presenza di un percorso alternativo modificano probabilità e impatto. L'analisi deve dichiarare queste condizioni invece di assumere che un nome tecnico le contenga già tutte.

Una buona descrizione evita formule ambigue. Non dire soltanto "esiste un rischio di accesso". Indica quale attore può raggiungere quale funzione, quale debolezza rende possibile l'evento, quali dati o servizi sono coinvolti e quale controllo limita il danno. Questa impostazione è utile anche quando la minaccia non è intenzionale: una configurazione errata, un aggiornamento difettoso o un guasto possono compromettere lo stesso servizio e richiedere trattamenti diversi.

L'uso concorsuale consiste nel mostrare che la sicurezza parte dal contesto. Dopo aver definito lo scenario, il candidato può proporre un controllo e motivarne il legame con la condizione osservata. Una lista di prodotti o sigle senza scenario non dimostra capacità di analisi.

## N-TR01-08-03 · Valutazione e trattamento del rischio

### Valutare e trattare il rischio

### Probabilità e impatto

La probabilità stima quanto sia plausibile lo scenario, considerando capacità dell’attore, esposizione, frequenza, vulnerabilità e controlli. L’impatto considera conseguenze su servizi, dati, persone, finanze, conformità e fiducia istituzionale.

Una scala qualitativa può usare basso, medio e alto. Ogni livello deve avere criteri. «Impatto alto» potrebbe indicare interruzione di un servizio essenziale o compromissione significativa di dati; la definizione dipende dal contesto.

La matrice incrocia probabilità e impatto:

| Impatto \ Probabilità | Bassa | Media | Alta |
| --- | --- | --- | --- |
| Alto | Medio | Alto | Alto |
| Medio | Basso | Medio | Alto |
| Basso | Basso | Basso | Medio |

Questa matrice ordina le priorità, ma non produce una misura assoluta. Scale diverse possono dare risultati diversi; scenari con lo stesso livello possono richiedere decisioni differenti.

### Inerente e residuo

Il **rischio inerente** è valutato prima di considerare i controlli pertinenti secondo il metodo scelto. Il **rischio residuo** rimane dopo l’applicazione dei controlli. Dichiarare «residuo basso» richiede evidenze che i controlli siano presenti e funzionino.

Un controllo soltanto previsto non riduce il rischio. Anche un controllo installato offre garanzie deboli se nessuno ne verifica il funzionamento.

### Processo di assessment

Un risk assessment comprende:

1. definizione di scopo, contesto, metodo e criteri;
2. identificazione di asset e dipendenze;
3. costruzione degli scenari;
4. analisi di probabilità e impatto;
5. valutazione rispetto a soglie e propensione al rischio;
6. priorità, trattamento e documentazione;
7. monitoraggio e aggiornamento.

Il **risk register** conserva scenario, asset, livello inerente, controlli, trattamento, responsabile, scadenza, evidenza e rischio residuo. Deve essere aggiornato quando cambiano architettura, minacce, vulnerabilità o impatti.

### Opzioni di trattamento

- **Evitare:** cessare l’attività che genera il rischio.
- **Ridurre o mitigare:** intervenire su probabilità o impatto.
- **Trasferire o condividere:** allocare parte delle conseguenze a un altro soggetto, senza cancellare la responsabilità dell’ente.
- **Accettare:** assumere consapevolmente il rischio residuo entro autorità e criteri definiti.

L’accettazione non equivale a ignorare. Richiede motivazione, titolare autorizzato, durata e riesame.


### Criteri, soglie e accettazione consapevole

La matrice aiuta a ordinare le decisioni solo se le scale sono dichiarate prima del risultato. "Probabilità alta" può significare esposizione pubblica, sfruttabilità plausibile e assenza di un controllo efficace; "impatto alto" può riferirsi a un'interruzione rilevante del servizio o alla compromissione di informazioni importanti. I criteri cambiano con l'ente, ma non possono cambiare a posteriori per giustificare una scelta già presa.

Il trattamento deve lasciare una traccia verificabile. Per ridurre un rischio non basta scrivere "applicare un controllo": occorrono un'azione, un responsabile, una data, un'evidenza e un criterio di chiusura. Se il rischio viene accettato, l'accettazione riguarda il residuo dopo avere valutato le alternative; richiede un soggetto autorizzato e una data di riesame. Trasferire una parte delle conseguenze a un fornitore non trasferisce automaticamente la responsabilità dell'ente verso il servizio.


### Dalla matrice al registro operativo

La matrice ordina rapidamente gli scenari, mentre il registro conserva le informazioni necessarie per agire. Una riga utile riporta identificativo, asset, scenario, valutazione inerente, controlli esistenti, scelta di trattamento, responsabile, data prevista, evidenza richiesta, valutazione residua e criterio di riesame. Il registro rende confrontabili decisioni ripetute; la matrice da sola non spiega perché un livello è stato attribuito.

Il rischio inerente aiuta a capire la gravità dello scenario prima di contare i controlli. Il rischio residuo non è un punteggio scelto per chiudere una pratica: deriva dalla verifica che i controlli siano presenti, adeguati e funzionanti. Se manca questa evidenza, il valore residuo è un'ipotesi e deve rimanere trattato con prudenza. Quando una misura riduce l'impatto ma non la probabilità, oppure viceversa, la motivazione deve dirlo.

Per l'orale, una risposta efficace segue un filo costante: definisco criteri e confini, identifico asset e dipendenze, costruisco lo scenario, valuto, scelgo il trattamento e programmo il riesame. Questa sequenza è preferibile a una formula numerica priva di assunzioni.

## N-TR01-08-04 · Controlli e difesa per livelli

### Controlli e difesa per livelli

### Natura e funzione

Per natura, i controlli possono essere organizzativi, tecnici o fisici. Per funzione possono essere:

- **preventivi**, se riducono la probabilità;
- **detective**, se individuano eventi o anomalie;
- **correttivi**, se rimuovono o limitano una condizione;
- **di recupero**, se ripristinano capacità;
- **deterrenti**, se scoraggiano;
- **compensativi**, se offrono protezione alternativa quando il controllo previsto non è praticabile.

Le tassonomie possono variare; la classificazione chiarisce la funzione del controllo, non aggiunge etichette fini a sé stesse.

Esempi: formazione e policy sono organizzativi; segmentazione e protezione endpoint sono tecnici; controllo degli accessi ai locali è fisico. Un medesimo controllo può avere più effetti.

### Difesa in profondità

La difesa in profondità combina controlli diversi affinché il fallimento di uno non esponga direttamente l’asset. Inventario, hardening, patching, minimo privilegio, segmentazione, monitoraggio e backup agiscono su punti differenti.

I livelli devono essere sufficientemente indipendenti. Due strumenti che dipendono dalla stessa identità amministrativa possono fallire insieme se quell’identità è compromessa.

Il principio Zero Trust, quando applicato, evita di attribuire fiducia implicita soltanto per posizione di rete. Richiede verifica esplicita, minimo privilegio e valutazione continua del contesto; non è un prodotto.

### NIST CSF 2.0

Il NIST CSF 2.0 organizza outcome in sei funzioni:

- **Govern:** strategia, ruoli, politiche e supervisione;
- **Identify:** asset, contesto e rischi;
- **Protect:** salvaguardie;
- **Detect:** individuazione degli eventi;
- **Respond:** gestione della risposta;
- **Recover:** ripristino e miglioramento.

Le funzioni sono concorrenti e continue, non fasi rigide. Il CSF aiuta a comunicare outcome e lacune, ma non sostituisce l’assessment né prescrive un singolo insieme di tecnologie.


### Adeguatezza e prova del controllo

Un controllo è adeguato quando risponde allo scenario e quando la sua efficacia può essere verificata. La stessa misura può avere funzioni diverse: una regola di autorizzazione può prevenire un accesso improprio, mentre il log associato può aiutare a rilevarlo. Classificare per natura e funzione serve a vedere lacune e dipendenze, non a ottenere una tassonomia perfetta.

La difesa per livelli richiede una domanda ulteriore: i controlli falliscono tutti per la stessa causa? Due protezioni amministrate con la stessa credenziale privilegiata possono perdere efficacia insieme. Per questo asset inventory, hardening, segmentazione, aggiornamento, minimo privilegio e monitoraggio assumono valore quando sono collegati a responsabilità ed evidenze. Il NIST CSF 2.0 offre una mappa di outcome per discutere governo, identificazione, protezione, rilevazione, risposta e recupero. È un riferimento tecnico utile, non un obbligo generale della PA italiana e non una sequenza rigida da applicare in ogni caso.


### Controlli coerenti con il rischio

La scelta non parte da un catalogo. Si parte dalla condizione da modificare. Se il problema è una funzione esposta non necessaria, la rimozione o limitazione dell'esposizione può essere un controllo preventivo. Se il rischio riguarda modifiche non autorizzate, autorizzazioni separate e registrazioni delle operazioni svolgono funzioni differenti. Se la correzione richiede tempo, una misura compensativa può ridurre temporaneamente l'esposizione, ma deve avere durata definita e non diventare una soluzione invisibile.

Le evidenze sono parte del controllo. Una procedura può dimostrare che una responsabilità è assegnata; una configurazione approvata può dimostrare l'applicazione di una regola; un test può mostrare che il controllo produce l'effetto atteso. Senza evidenza, il controllo è soltanto dichiarato. La verifica periodica intercetta anche controlli che erano corretti quando sono stati installati ma non lo sono più dopo una modifica.

Un candidato non deve promettere sicurezza assoluta. Deve spiegare come più livelli indipendenti riducono il rischio residuo e come l'ente saprà se funzionano. Questa è la differenza fra una risposta tecnica e una lista generica di misure.



La scelta va riesaminata quando cambiano asset, esposizione, minaccia, architettura o efficacia del controllo. Un controllo adeguato ieri può non esserlo dopo un'integrazione, una variazione di servizio o un cambiamento organizzativo. Il riesame mantiene il trattamento collegato alla realtà del servizio.

## N-TR01-08-05 · Threat modeling e gestione delle vulnerabilità

### Threat modeling

Il threat modeling anticipa domande di sicurezza durante progettazione ed evoluzione. Il gruppo:

1. descrive sistema, attori e obiettivi;
2. disegna componenti, flussi e confini di fiducia;
3. individua asset e scenari di minaccia;
4. seleziona mitigazioni;
5. verifica assunzioni e copertura.

STRIDE è una tassonomia possibile: spoofing, tampering, repudiation, information disclosure, denial of service ed elevation of privilege. Non è l’unico metodo e non deve diventare un elenco scollegato dal sistema.

Un diagramma dei flussi mostra dove i dati entrano, cambiano fiducia, vengono elaborati e conservati. Ogni confine suggerisce domande su validazione, identità, autorizzazione e protezione.

### Gestione delle vulnerabilità

### Scoperta e validazione

L’inventario di asset, versioni e dipendenze è il punto di partenza. Le vulnerabilità emergono da scanning, test, segnalazioni, intelligence, advisory e comunicazioni dei fornitori.

Ogni risultato richiede una validazione. Un **falso positivo** segnala una condizione inesistente o non applicabile; un **vero positivo** richiede trattamento. La validazione non autorizza prove invasive indiscriminate: scopo, permessi e sicurezza del test vanno definiti.

### CVE, CWE e CVSS

- **CVE** identifica una specifica vulnerabilità pubblicamente nota.
- **CWE** descrive una classe di debolezze che può generare vulnerabilità.
- **CVSS** comunica caratteristiche e gravità mediante un punteggio e un vettore.

CVSS 4.0 distingue metriche Base, Threat, Environmental e Supplemental. Il punteggio di base non conosce da solo criticità dell’asset, esposizione, exploit osservati o controlli locali. Perciò il CVSS più alto non è sempre la prima priorità.

### Priorità e remediation

La priorità considera:

- gravità tecnica;
- sfruttabilità e attività osservata;
- esposizione;
- criticità del servizio;
- presenza di dati sensibili;
- controlli compensativi;
- disponibilità e rischio della correzione.

La remediation assegna responsabile e scadenza, prova la patch, pianifica la distribuzione e verifica la chiusura. Se la patch non è applicabile subito, una mitigazione temporanea può ridurre esposizione o funzionalità. L’eccezione deve indicare rischio residuo, approvazione e data di riesame.

La responsible disclosure coordina segnalazione e correzione evitando diffusione prematura di dettagli. Nel lavoro pubblico vanno rispettati canali, autorizzazioni e procedure applicabili.


### Priorità contestuale e chiusura verificata

La gestione delle vulnerabilità è un ciclo, non la somma dei risultati di uno strumento. Inventario, scoperta, validazione, priorità, trattamento e verifica di chiusura devono rimanere collegati. Un risultato può essere un falso positivo oppure non essere applicabile alla configurazione esaminata; trattarlo come un incidente genera lavoro inutile. All'opposto, ignorare una segnalazione senza motivazione impedisce di spiegare il rischio residuo.

CVE identifica una vulnerabilità pubblicamente nota, CWE descrive una classe di debolezza e CVSS comunica caratteristiche e gravità. Nessuno dei tre sostituisce l'analisi del servizio. La priorità considera anche esposizione, sfruttabilità, valore dell'asset, controlli e rischio della modifica. Una patch può richiedere test e una finestra di rilascio; nel frattempo una mitigazione temporanea può ridurre l'esposizione. L'eccezione deve avere proprietario, motivazione, scadenza e riesame.


### Modello di minaccia come strumento di progetto

Il threat modeling è utile quando accompagna una decisione concreta. Per un portale, il gruppo può disegnare utenti, front end, servizi applicativi, archivio documentale e sistemi esterni; poi identifica dove il dato attraversa un confine di fiducia. A ciascun passaggio associa una domanda: chi può inviare il dato, come viene verificata l'identità, quale autorizzazione serve, quale trasformazione avviene e quale evidenza resta. Serve a collegare ogni flusso alla minaccia e alla mitigazione che lo riguarda.

STRIDE può aiutare a classificare famiglie di minacce, ma non sostituisce la conoscenza del sistema. Un diagramma incompleto o una lista di categorie non genera da sola un trattamento. Lo stesso vale per la gestione delle vulnerabilità: il risultato di una scansione diventa utile quando è attribuito a un asset, validato e collegato a un'azione verificabile. Il ciclo deve poter spiegare anche perché una segnalazione è stata chiusa, rinviata o dichiarata non applicabile.

Quando una vulnerabilità non può essere corretta immediatamente, la scelta responsabile non è nasconderla. Occorre limitare il rischio, approvare l'eccezione, fissare una data e verificare che la condizione temporanea non diventi permanente.

## N-TR01-08-06 · Secure SDLC e software supply chain

### Secure SDLC e secure coding

### Sicurezza lungo il ciclo di vita

Il NIST SSDF integra pratiche di sicurezza nel ciclo di sviluppo. Le pratiche di sicurezza accompagnano requisiti, progettazione, implementazione, verifica, rilascio, esercizio e dismissione.

**Security by design** significa considerare minacce e requisiti durante la progettazione. **Security by default** significa fornire configurazioni iniziali prudenti. Una scansione finale difficilmente corregge una scelta architetturale insicura.

Le attività comprendono requisiti verificabili, threat modeling, ambienti protetti, dipendenze governate, review, test, artefatti controllati, gestione delle vulnerabilità e apprendimento dalle cause.

### Pratiche di codice sicuro

- validare input rispetto a tipo, formato, lunghezza e dominio attesi;
- codificare l’output secondo il contesto;
- usare query parametrizzate invece di concatenare input;
- gestire errori senza esporre dettagli sensibili;
- non incorporare secret nel codice;
- applicare autorizzazioni sul server;
- mantenere dipendenze e configurazioni;
- fallire in modo sicuro quando una condizione non è gestibile.

La validazione client migliora l’esperienza, ma non sostituisce quella lato server. Una denylist di stringhe pericolose è spesso meno robusta della definizione positiva dei valori ammessi.

### Verifiche diverse

La **code review** esamina logica e modifiche. La **SAST** analizza codice o rappresentazioni senza eseguire l’applicazione. La **DAST** osserva il comportamento di un’applicazione in esecuzione. La **software composition analysis** esamina componenti e dipendenze. Il **penetration test** simula scenari entro uno scopo autorizzato.

Le tecniche hanno coperture diverse. I risultati vanno validati e ricondotti allo scenario di rischio.

OWASP Top 10 è un documento di awareness sui rischi delle applicazioni web. L’edizione 2025 include categorie come controllo accessi, configurazione, supply chain, crittografia, injection e design insicuro. Non certifica la sicurezza e non sostituisce requisiti, threat modeling o test basati sul contesto.

### Software supply chain

La supply chain comprende codice proprio, librerie, componenti open source e commerciali, repository, tool di build, runner, pipeline, artefatti e canali di distribuzione. L’attaccante può compromettere un componente, una credenziale, il processo di build oppure il canale di aggiornamento.

I controlli includono:

- inventario di componenti e versioni;
- fonti e repository autorizzati;
- protezione di account e pipeline;
- review delle modifiche;
- isolamento e aggiornamento della toolchain;
- artefatti identificati e verificabili;
- provenienza e attestazioni;
- monitoraggio degli advisory;
- capacità di ricostruire e revocare una release.

Una **SBOM** è un record formale dei componenti e delle relazioni. Aiuta a rispondere «dove usiamo questa libreria?», ma non dimostra che il software sia sicuro, aggiornato o privo di componenti non dichiarati. Deve essere mantenuta, associata all’artefatto e usata nei processi di gestione.

Il rischio di terze parti resta dell’organizzazione anche quando alcune attività sono affidate fuori. Requisiti contrattuali e SLA sono trattati nel capitolo 12.


### Prevenzione prima del rilascio

La sicurezza del software non inizia con una scansione finale. Requisiti verificabili, progettazione, revisione, test, rilascio ed esercizio producono evidenze diverse e riducono classi diverse di errore. Validare un input, gestire correttamente gli errori e applicare autorizzazioni sul server sono esempi di principi; non costituiscono una ricetta universale. Una review del codice, SAST, DAST, analisi delle dipendenze e penetration test osservano aspetti differenti e richiedono scopo e autorizzazioni.

La filiera comprende anche repository, account, runner, strumenti di build, artefatti e canali di distribuzione. Una SBOM aiuta a sapere dove una libreria è usata; non dimostra da sola che il prodotto sia sicuro. Per questo la filiera richiede componenti identificati, modifiche revisionate, accessi protetti, provenienza verificabile e capacità di ricostruire una release. I requisiti contrattuali dettagliati restano nel capitolo 12, mentre qui il candidato deve saper riconoscere il rischio tecnico e l'evidenza necessaria.


### Evidenze della filiera

Una catena di rilascio affidabile rende possibile rispondere a domande semplici: quale codice è stato usato, quali componenti erano inclusi, chi ha autorizzato la modifica, quale artefatto è stato distribuito e come si può tornare a una versione precedente. Queste domande non richiedono dettagli riservati o procedure offensive; servono a collegare prevenzione, tracciabilità e recupero.

La sicurezza per impostazione predefinita riduce il numero di decisioni rischiose richieste a chi usa o gestisce il sistema. Non elimina la responsabilità di configurare, testare e aggiornare. Un requisito di sicurezza ben scritto indica comportamento atteso, vincolo, evidenza e criterio di accettazione. Questa logica aiuta anche a distinguere una promessa generica di "software sicuro" da un impegno verificabile.

## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento rende controllabile la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-08-01` | Caso guidato: portale per le domande |
| `N-TR01-08-02` | Costruisci uno scenario distinguendo minaccia, vulnerabilità, evento e impatto. |
| `N-TR01-08-03` | Laboratorio: costruire una risk matrix |
| `N-TR01-08-04` | Indica un controllo preventivo, uno detective e uno compensativo per lo stesso scenario. |
| `N-TR01-08-05` | Micro-verifica: confine di fiducia |
| `N-TR01-08-06` | Quale tecnica analizza un’applicazione in esecuzione? |

## ▣ Verifica

### Micro-verifica: confine di fiducia

Un portale riceve allegati da utenti esterni e li inoltra a un archivio documentale. Indica un confine di fiducia e una domanda da porre nel threat modeling.

**Soluzione:** il passaggio dall’input pubblico al servizio che conserva i documenti è un confine di fiducia. Occorre chiedere, per esempio, come il sistema valida il file e quale autorizzazione consente di leggerlo.



### Caso guidato: portale per le domande

Un ente gestisce un portale per presentare domande di contributo. L’applicazione usa una libreria con una vulnerabilità pubblica; il servizio è esposto e tratta documenti personali.

**Scenario.** Un attore remoto sfrutta la libreria tramite una funzione di caricamento e accede a documenti non autorizzati.

**Asset.** Documenti, profili utenti, applicazione e continuità del procedimento.

**Valutazione inerente.** Probabilità alta per esposizione e applicabilità; impatto alto per riservatezza e servizio. Nella matrice 3×3 il rischio è alto.

**Controlli esistenti.** Segmentazione, privilegi limitati e monitoraggio riducono propagazione e tempo di rilevazione, ma non eliminano la debolezza.

**Trattamento.** Il responsabile applica la patch dopo test; nel frattempo limita la funzione, rafforza le regole applicative e monitora gli indicatori pertinenti. Registra scadenza ed evidenze.

**Rischio residuo.** Viene rivalutato dopo verifica della versione e test funzionale. Il livello non scende automaticamente: servono evidenze sulla correzione e sull’efficacia dei controlli.

**Supply chain.** La SBOM consente di individuare altri servizi con la stessa libreria. L’ente traduce quanto appreso in nuovi requisiti di aggiornamento e controlli della pipeline.

### Laboratorio: costruire una risk matrix

Compila una riga per ciascuno scenario.

| Campo | Domanda |
| --- | --- |
| Asset | che cosa ha valore e chi ne risponde? |
| Scenario | quale minaccia sfrutta quale vulnerabilità? |
| Evento | che cosa può accadere? |
| Impatto | quali conseguenze e con quale livello? |
| Probabilità | quali fattori la rendono plausibile? |
| Inerente | quale livello prima dei controlli? |
| Controlli | quali esistono e quali evidenze? |
| Trattamento | evitare, ridurre, trasferire o accettare? |
| Responsabile | chi attua e chi accetta? |
| Scadenza | entro quando? |
| Residuo | che cosa rimane dopo la verifica? |
| Riesame | quale evento o data riapre la valutazione? |

### Domanda da commissario

**«Come imposteresti un risk assessment cyber?»**

Definirei scopo, metodo e criteri; identificherei asset e dipendenze; costruirei scenari con minacce, vulnerabilità, eventi e impatti; stimerei il rischio inerente; valuterei poi i controlli; sceglierei il trattamento, con responsabile, scadenza ed evidenza; infine stimerei il rischio residuo e fisserei il riesame.

### Domanda-trappola

**«La vulnerabilità con CVSS più alto va sempre corretta per prima?»**

No. CVSS comunica la gravità tecnica, ma la priorità dipende anche da esposizione, sfruttabilità, criticità dell’asset, impatto, controlli e rischio della modifica. Il punteggio è un input, non la decisione.

### Errore tipico

L’errore consiste nell’assegnare un «rischio alto» senza descrivere lo scenario e le scale adottate. Una valutazione verificabile esplicita asset, minaccia, vulnerabilità, impatto, probabilità, controlli e assunzioni.

### Mini-esercizi e quiz

1. Una configurazione predefinita con credenziali note è:
   - A. una minaccia
   - B. una vulnerabilità
   - C. un impatto
   - D. un rischio residuo

2. Il rischio dopo i controlli è:
   - A. inerente
   - B. residuo
   - C. assoluto
   - D. CVE

3. Quale identificatore riguarda una vulnerabilità specifica?
   - A. CWE
   - B. CVE
   - C. CVSS
   - D. CSF

4. Quale tecnica analizza un’applicazione in esecuzione?
   - A. DAST
   - B. SAST
   - C. SBOM
   - D. risk register

5. Una SBOM:
   - A. certifica che il software è sicuro
   - B. elenca componenti e relazioni della supply chain
   - C. sostituisce il penetration test
   - D. corregge le dipendenze

6. Costruisci uno scenario distinguendo minaccia, vulnerabilità, evento e impatto.

7. Indica un controllo preventivo, uno detective e uno compensativo per lo stesso scenario.

**Soluzioni sintetiche:** 1-B; 2-B; 3-B; 4-A; 5-B.

**Risposta corretta: B.** Una configurazione con credenziali note è una debolezza sfruttabile: non descrive ancora un attore, un evento o l'impatto.

**Risposta corretta: B.** Il rischio residuo è quello che rimane dopo avere considerato controlli pertinenti ed evidenze della loro efficacia.

**Risposta corretta: B.** CVE identifica una vulnerabilità nota; CWE descrive una classe di debolezza e CVSS ne comunica caratteristiche e gravità.

**Risposta corretta: A.** DAST osserva il comportamento dell'applicazione in esecuzione. SAST è analisi statica; i due approcci non sono intercambiabili.

**Risposta corretta: B.** La SBOM è un inventario formale di componenti e relazioni. Non certifica il software e non sostituisce i controlli di sviluppo.

**Risposta corretta: risposta aperta.** Lo scenario deve separare minaccia, vulnerabilità, evento e impatto; l'esercizio sui controlli deve motivare come ciascuna misura riduce probabilità o conseguenze.
### Checklist finale

- ho definito scopo, metodo e scale;
- ho inventariato asset e dipendenze;
- ho distinto minaccia, vulnerabilità, evento e impatto;
- ho costruito scenari verificabili;
- ho valutato inerente e residuo;
- ho associato controlli a evidenze;
- ho assegnato responsabile e scadenza;
- ho prioritizzato vulnerabilità con il contesto;
- ho distinto CVE, CWE e CVSS;
- ho integrato sicurezza nel ciclo di sviluppo;
- ho considerato dipendenze, pipeline e artefatti;
- ho previsto riesame e chiusura.

### Da sapere in 5 righe

Il rischio nasce da uno scenario, non da un punteggio isolato. Minaccia, vulnerabilità, evento e impatto sono concetti distinti. I controlli riducono probabilità o conseguenze e devono produrre evidenze. CVE identifica, CWE classifica debolezze, CVSS comunica gravità. Sviluppo sicuro e supply chain portano la prevenzione prima del rilascio.

## Riferimenti normativi e professionali essenziali

- NIST Cybersecurity Framework 2.0 e NIST SP 800-30, per outcome e valutazione del rischio.
- NIST Secure Software Development Framework, SP 800-218, per le pratiche lungo il ciclo di sviluppo.
- CVE Program, Common Weakness Enumeration e CVSS v4.0, per distinguere identificazione, classe di debolezza e gravità.
- OWASP Top 10, come documento di awareness sui rischi applicativi.
- CISA, Software Bill of Materials e pratiche per il consumo della SBOM.
- Quadro italiano di cybersicurezza applicabile al bando e all'ente, da verificare al cut-off della procedura.
