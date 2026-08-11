---
id: chapter-m-tr01-12
type: book_chapter
title: "Procurement ICT e gestione dei fornitori"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["procurement ICT", "capitolato tecnico", "SLA", "vendor management", "exit strategy"]
entities: ["ANAC", "Consip", "RUP", "Direttore dell'esecuzione", "AgID"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/procurement-ict-sla-vendor-management-fonti-consolidate", "sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024", "sources/ciclo-contratti-pubblici-rup-stazione-appaltante-operatore-economico", "sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp", "sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche", "sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie", "sources/iam-crittografia-logging-incident-response-fonti-primarie", "sources/data-governance-open-data-interoperabilita-fonti-primarie"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati", "il-metodo-bando", "m-tr02-appalti-pnrr-fondi-ue"]
confidence: 0.88
updated_at: 2026-08-11
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "procurement-ict", "sla", "fornitori"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 12
draft_stage: format-2-retrofit
format_version: 2
dati_operativi: []
last_compiled_from: ["sources/procurement-ict-sla-vendor-management-fonti-consolidate", "topics/procurement-ict-sla-gestione-fornitori", "planning/08-capitolo-12-piano-completamento"]
---

# Procurement ICT e gestione dei fornitori

Anche un servizio aggiudicato correttamente può fallire durante l'esecuzione. Accade se il bisogno resta vago, i requisiti non sono verificabili o gli SLA misurano ciò che è facile contare invece di ciò che serve agli utenti. In altri casi, l'ente scopre troppo tardi di non poter recuperare dati e configurazioni.

Nel procurement ICT la competenza tecnica non sostituisce quella amministrativa. Entrambe concorrono allo stesso risultato: tradurre il fabbisogno in una prestazione, precisarla con requisiti e verificarla attraverso evidenze utili al governo del contratto.

## Obiettivo e confini

Al termine del capitolo il candidato saprà:

- tradurre un fabbisogno in requisiti funzionali e non funzionali;
- distinguere requisito, criterio di accettazione, criterio di valutazione, obbligo e SLA;
- costruire un livello di servizio misurabile;
- collegare ruoli tecnici e contrattuali durante l'esecuzione;
- inserire sicurezza, dati, continuità e supply chain nel governo del fornitore;
- riconoscere lock-in e progettare portabilità, reversibilità ed uscita;
- orientarsi tra ciclo digitale e strumenti di acquisto senza confonderli.

La disciplina generale dei contratti pubblici va studiata insieme alle nozioni comuni sul ciclo contrattuale. Per procedure, soglie e appalti avanzati il lettore può approfondire in VOL-09/M-TR02 — Appalti, PNRR e fondi UE; questo rinvio non è necessario per comprendere il governo tecnico-organizzativo dell'acquisto ICT qui trattato.

## Mappa BANDO dell'acquisto ICT

- **B — Bisogno:** risultato pubblico, utenti, perimetro, baseline e vincoli.
- **A — Attori:** RUP, direttore dell'esecuzione, owner del servizio, referenti tecnici, sicurezza, DPO e fornitore.
- **N — Nodi:** requisiti vaghi, misure ambigue, dipendenze, incidenti, modifiche, subfornitori e lock-in.
- **D — Documenti:** capitolato, matrice dei requisiti, piano dei test, SLA, resoconto tecnico, verbali, registro rischi ed exit plan.
- **O — Output:** servizio accettato e controllato, con evidenze, continuità e possibilità reale di uscita.

## N-TR01-12-01 · Fabbisogno, baseline e strategia di acquisizione

### Risultato, perimetro e baseline

Il fabbisogno parte dal problema pubblico da risolvere, non dal prodotto desiderato. «Acquistare una piattaforma cloud» indica già una soluzione; «garantire ai cittadini l'accesso continuativo al servizio, riducendo tempi di indisponibilità e oneri di gestione» esplicita invece il risultato.

La **baseline** fotografa la situazione iniziale: utenti, volumi, tempi, costi, incidenti, tecnologie, competenze e vincoli. Senza baseline non si può dimostrare se l'acquisto abbia migliorato il servizio.

Il perimetro chiarisce ciò che il fornitore deve consegnare e ciò che resta all'ente. Include ambienti, integrazioni, dati, migrazione, assistenza, manutenzione, formazione, documentazione e uscita. Se il confine resta incerto, alcune attività non trovano un responsabile e altri costi emergono soltanto durante l'esecuzione.

### Make, buy e reuse

L'ente può sviluppare internamente, acquistare, riusare soluzioni disponibili o combinare le opzioni. La scelta considera competenze, tempi, criticità, mercato, interoperabilità, manutenzione, sicurezza e sostenibilità nel ciclo di vita.

Anche dopo l'acquisto, l'ente deve conservare competenze interne. Se nessuno nell'ente sa verificare requisiti, dati, configurazioni e livelli di servizio, il fornitore finisce per controllare anche il significato delle misure con cui viene valutato.

### Costo e dipendenze

Il prezzo iniziale è solo una parte del costo. Contano migrazione, integrazioni, licenze, gestione, formazione, crescita dei volumi, assistenza, modifiche, transizione e dismissione. Il **costo totale di possesso** è una lente decisionale; il calcolo concreto dipende dagli atti e dai dati disponibili.

Il risparmio iniziale può svanire se la soluzione richiede formati proprietari, competenze rare o costi elevati per esportare dati e configurazioni. Per questo il rischio di uscita si valuta prima dell'affidamento.

### Applicazione: decidere prima di acquistare

Una baseline non è un elenco di apparati. Deve spiegare quale servizio esiste oggi, chi lo usa, quali tempi di attesa o indisponibilità produce, quali integrazioni lo sostengono e quali vincoli non possono essere rimossi. Per un portale comunale, ad esempio, non basta sapere che è ospitato in cloud: servono i flussi con identità digitale, pagamenti, protocollo, notifiche e archivi. Servono anche le persone che gestiscono il servizio e il momento in cui un fermo diventa un danno concreto per utenti o uffici.

La scelta tra sviluppo, acquisto, riuso o combinazione non è una gara tra tecnologie. Lo sviluppo interno può aumentare controllo e conoscenza, ma chiede capacità di manutenzione. Un prodotto o servizio già disponibile può ridurre il tempo iniziale, ma può imporre interfacce, licenze o modalità operative difficili da cambiare. Il riuso è utile se risolve il bisogno e se l'ente può governarne evoluzione, sicurezza e integrazione. La scelta va quindi motivata con obiettivo, vincoli, competenze, tempi, costo di gestione e possibilità di uscita, non con la popolarità di un fornitore.

Un buon perimetro separa ciò che deve essere consegnato da ciò che rimane in capo all'ente: migrazione, ambienti, dati, integrazioni, formazione, documentazione, assistenza e dismissione. Questa separazione evita il costo nascosto delle attività “incluse a voce”. In prova, una risposta solida dichiara le assunzioni: se il servizio gestisce pratiche dei cittadini, continuità, accessi, tracciabilità e recupero assumono un peso diverso rispetto a un sito informativo. **Errore tipico:** partire dalla piattaforma desiderata e cercare dopo un bisogno che la giustifichi. Il percorso corretto è inverso: risultato pubblico, evidenze iniziali, requisiti e soltanto allora scelta della soluzione.

La scelta resta quindi un atto di governo: documentare assunzioni, alternative scartate, dipendenze e criterio di verifica rende la decisione esaminabile anche quando cambiano persone o fornitori. Il costo iniziale non esaurisce la valutazione: migrazione, formazione, integrazioni, manutenzione, crescita dei volumi e uscita possono modificare il costo effettivo del servizio. Una risposta concorsuale completa esplicita questo ciclo e non presenta make, buy o reuse come formule automatiche.

### Controllo della scelta e strumenti di acquisto

La strategia non termina con l'individuazione della soluzione. Prima di definire l'acquisto, l'ente verifica se il servizio deve essere unico o separabile in componenti: per esempio hosting, migrazione, manutenzione applicativa, assistenza e formazione. Separare senza ragione può moltiplicare interfacce e responsabilità; concentrare tutto in un solo affidamento può rendere difficile il subentro. La domanda pratica è quale confine consenta di governare qualità, sicurezza, tempi e continuità senza creare una dipendenza che l'ente non sa più misurare.

Anche gli strumenti di acquisto e negoziazione non sostituiscono questa analisi. Convenzioni, accordi, mercati elettronici e altri canali possono orientare il modo di approvvigionarsi, ma non trasformano un fabbisogno vago in una buona prestazione. Il candidato deve prima saper descrivere l'oggetto, i vincoli e le evidenze; solo dopo colloca la scelta nello strumento e nella procedura che gli atti consentono. Banca dati e piattaforme digitali rendono tracciabile il ciclo, non decidono al posto dell'amministrazione che cosa sia necessario acquistare.

Una scheda iniziale utile mette sulla stessa pagina risultato atteso, utenti, dati coinvolti, integrazioni, volume previsto, indisponibilità accettabile, competenze interne e dipendenze esterne. Aggiunge poi le assunzioni da confermare e le alternative da confrontare. Se l'ipotesi di volume cambia, se un'integrazione non è disponibile o se l'ente non possiede una competenza essenziale, deve cambiare anche la valutazione dell'opzione. In questo senso la baseline è viva: viene aggiornata quando emergono dati nuovi, mantenendo traccia della decisione e del suo motivo.

Per evitare una scelta solo economica, conviene includere fin dall'inizio il costo del non fare e il costo dell'uscita. Un servizio lasciato senza manutenzione può produrre ritardi, errori e perdita di fiducia; una transizione improvvisata può imporre doppi ambienti, estrazioni manuali e supporto urgente. Non servono numeri universali: serve mostrare che la decisione considera l'intero ciclo di vita. Questo è anche il criterio per leggere criticamente una proposta apparentemente conveniente: chiedere quali attività, conoscenze e dati resterebbero all'ente se il fornitore cambiasse domani.
## N-TR01-12-02 · Requisiti verificabili e capitolato tecnico

### Funzionali e non funzionali

Un **requisito funzionale** descrive ciò che il sistema deve fare. Esempio: «l'operatore può consultare lo stato della pratica e la cronologia delle modifiche».

Un **requisito non funzionale** riguarda qualità o vincoli. Può riferirsi a disponibilità, prestazioni, sicurezza, accessibilità, interoperabilità, manutenibilità, capacità o portabilità. Esempio: «la cronologia deve essere esportabile in un formato documentato e leggibile da strumenti indipendenti».

Questa distinzione orienta le verifiche, ma i due gruppi restano collegati: una funzione priva di requisiti di sicurezza e prestazione può risultare inutilizzabile.

### Scrivere requisiti verificabili

Per essere efficace, un requisito specifica:

1. soggetto o componente interessato;
2. comportamento o qualità richiesta;
3. condizioni operative;
4. risultato osservabile;
5. criterio di accettazione;
6. evidenza attesa.

«Il sistema deve essere veloce» non è verificabile. «Nelle condizioni di carico definite nel piano di test, il servizio risponde entro la soglia stabilita, misurata dal punto concordato e registrata nel resoconto tecnico» indica almeno come completare la specifica. Il valore numerico va motivato e approvato, non inventato.

**Errore tipico:** descrivere una marca o una tecnologia senza collegarla al bisogno, ai vincoli e alla disciplina applicabile. Le specifiche devono consentire una valutazione tecnica trasparente e gestire correttamente standard, compatibilità ed equivalenze.

### Requisito, criterio, obbligo e SLA

Quattro elementi spesso confusi hanno funzioni diverse:

| Elemento | Domanda |
| --- | --- |
| requisito | che cosa deve fare o garantire la soluzione? |
| criterio di accettazione | come dimostriamo che il requisito è soddisfatto? |
| criterio di valutazione | come confrontiamo le offerte secondo gli atti? |
| SLA | quale livello deve essere mantenuto durante il servizio? |

Un requisito può essere verificato, per servizi e forniture ICT, nell'ambito della verifica di conformità oppure monitorato nel tempo. Il collaudo riguarda invece i lavori. Un criterio di valutazione opera nella scelta dell'offerta; non sostituisce l'obbligo di esecuzione. Lo SLA riguarda il servizio erogato e deve collegarsi a misure e conseguenze definite.

### Tracciabilità e accettazione

La matrice requisito-test-evidenza collega promessa e verifica:

| ID | Requisito | Verifica | Evidenza | Esito |
| --- | --- | --- | --- | --- |
| R-01 | esportazione dati | prova su campione | file e verbale | da compilare |
| R-02 | gestione accessi | test dei ruoli | log e resoconto tecnico | da compilare |
| R-03 | ripristino | esercitazione | rapporto di prova | da compilare |

Accettare una prestazione non significa esprimere un assenso generico. Registra versione, ambiente, dati di prova, risultato, anomalie, riserve, responsabili e decisione. Se il requisito cambia, devono cambiare in modo controllato anche test ed evidenze.

### Applicazione: dalla frase generica alla prova

Il capitolato deve consentire a persone diverse di capire la stessa cosa. Per questo un requisito collega un soggetto, un comportamento o una qualità, condizioni d'uso, criterio di accettazione ed evidenza. “Il sistema deve essere sicuro” non permette di decidere se la prestazione è resa; “gli accessi amministrativi devono essere attribuiti a identità individuali, registrati e verificabili nel resoconto tecnico concordato” indica invece una proprietà controllabile. Il valore esatto, il metodo e l'ambito restano da definire negli atti, ma la struttura della verifica è già chiara.

La neutralità tecnica non equivale a vaghezza. È possibile descrivere interfacce, standard, compatibilità, prestazioni, accessibilità e portabilità senza fissare una marca come soluzione obbligata. Se un vincolo tecnico è necessario, deve essere collegato a interoperabilità, continuità, sicurezza o altra esigenza dimostrabile e gestito secondo la disciplina applicabile. Il candidato deve distinguere l'oggetto della prestazione dal modo con cui le offerte sono confrontate: un criterio di valutazione opera nella scelta dell'offerta; un requisito e un obbligo regolano ciò che dovrà essere consegnato; il criterio di accettazione serve a verificare il risultato.

La matrice requisito-test-evidenza evita che la verifica di conformità diventi un giudizio impressionistico. Per ciascun requisito critico annota identificativo, test o ispezione, ambiente, dati di prova, responsabile, evidenza attesa ed esito. Se la migrazione produce un file esportato ma il file non può essere letto nel sistema destinatario, l'evidenza non dimostra ancora portabilità. Se una funzione opera solo su dati preparati dal fornitore, occorre chiarire se quel campione rappresenti l'uso reale. **Errore tipico:** confondere la documentazione consegnata con l'accettazione. La prima può essere necessaria; la seconda richiede una verifica tracciabile.

### Dalla specifica alla verifica di conformità

Un capitolato robusto non è una lista di desideri. Ordina i requisiti per oggetto, priorità e dipendenza, chiarendo cosa è indispensabile per avviare il servizio e cosa può essere consegnato in una fase successiva. La priorità non riduce l'obbligo di verificare: aiuta a decidere quali prove sono bloccanti, quali anomalie ammettono una correzione e quali condizioni impediscono l'accettazione. Quando un requisito dipende da un'integrazione di terzi, la specifica deve dire chi fornisce l'accesso, quale ambiente viene usato e come si tratta l'indisponibilità del soggetto esterno.

Il criterio di accettazione deve essere proporzionato alla promessa. Per una funzione critica può servire una prova end-to-end con utenti, dati rappresentativi, gestione delle eccezioni e traccia dell'esito. Per un documento tecnico possono bastare completezza, aggiornamento e verificabilità di ciò che descrive. Una dimostrazione guidata dal fornitore è utile, ma non coincide automaticamente con un test indipendente: chi verifica deve poter riprodurre, controllare o almeno comprendere la prova e le sue condizioni.

È utile distinguere tre piani temporali. Nella selezione si valuta, secondo gli atti, la proposta disponibile; prima dell'avvio si accerta che ambienti, configurazioni e consegne iniziali siano pronti; durante l'esecuzione si misura che il servizio resti conforme. Confondere i piani porta a due errori: usare una promessa di offerta come se fosse una prova di esercizio, oppure pretendere, nella verifica di conformità, una qualità che non è stata descritta. La tracciabilità requisito-test-evidenza collega i piani e rende visibili le lacune.

Quando una richiesta cambia, non basta aggiornare una riga di testo. Occorre rivalutare impatto su utenti, sicurezza, dati, tempi, costo, integrazioni, test e documentazione. La nuova versione del requisito deve indicare chi l'ha approvata e quale prova la renderà accettabile. Così il capitolato resta uno strumento di governo e non un documento congelato che viene interpretato solo quando nasce un conflitto.
## N-TR01-12-03 · SLA, SLI, KPI e misurazione del servizio

### SLA, SLI e soglia

Lo **SLA** è l'impegno contrattuale sul livello di servizio. Lo **SLI** è l'indicatore osservato. La soglia o obiettivo indica il livello atteso. Il lessico può variare tra documenti; ciò che conta è rendere non ambigue definizione, misura e responsabilità.

Una scheda SLA completa specifica:

- servizio e popolazione osservata;
- formula o regola di misura;
- soglia;
- finestra e periodo di osservazione;
- fonte dei dati e punto di misura;
- esclusioni ammesse;
- severità o classe dell'evento;
- rendicontazione tecnica e responsabile della verifica;
- escalation e conseguenze previste dagli atti.

### Disponibilità e tempi

La **disponibilità** indica la quota di tempo in cui il servizio è utilizzabile nel perimetro concordato. Senza finestra di servizio, periodo, componenti inclusi ed esclusioni, la percentuale è equivoca.

Il **tempo di presa in carico** misura quanto passa prima che il fornitore inizi a gestire una segnalazione. Il **tempo di ripristino** riguarda il ritorno a una condizione operativa; il **tempo di risoluzione** può richiedere la rimozione definitiva della causa. Un workaround può ripristinare il servizio senza chiudere il problema.

La severità dipende dall'impatto e dall'urgenza. Un malfunzionamento che blocca tutti gli utenti non è equivalente a un difetto cosmetico. Classi e regole devono essere definite prima dell'incidente.

### SLA e KPI

Un **KPI** sostiene il governo del servizio: volume ticket, tasso di riapertura, modifiche fallite, vulnerabilità scadute, soddisfazione o backlog. Può essere utile anche senza costituire uno SLA.

Una penale o un service credit non ripara da solo il servizio. L'ente deve ottenere ripristino, analisi della causa, azione correttiva e prevenzione della ricorrenza. Le conseguenze contrattuali concrete dipendono dagli atti e dal quadro vigente.

### Applicazione: misurare ciò che conta

Un livello di servizio diventa utile quando collega una misura a una decisione. L'indicatore osservato può provenire da strumenti del fornitore, dell'ente o da entrambi; questo non basta, perché occorre definire quale componente è osservata, con quale orologio, in quale finestra e come sono trattati eventi eccezionali. La stessa percentuale di disponibilità cambia significato se si riferisce al solo front-end o anche alle integrazioni necessarie per completare una pratica. Senza perimetro e fonte dei dati, un resoconto tecnico può apparire preciso ma non essere contestabile.

Conviene separare gli indicatori di esito dagli indicatori di governo. Disponibilità, presa in carico o ripristino possono essere impegni contrattuali se gli atti li definiscono come tali. Numero di ticket, riaperture, modifiche fallite o arretrati aiutano invece a comprendere tendenze e rischi; possono essere KPI importanti senza diventare automaticamente SLA. Anche le classi di severità devono essere concordate prima del disservizio, usando impatto su utenti, servizio e attività amministrativa, non solo la comodità tecnica di chi riceve la segnalazione.

Una soglia non sostituisce la gestione. Davanti a uno scostamento, l'ente deve ottenere evidenza, valutare l'impatto, chiedere ripristino, analisi della causa e azione preventiva, registrando responsabile e scadenza. Penali o service credit, se previsti, seguono gli atti e non rendono accettabile un servizio che continua a fallire. In un orale, formula una risposta in questo ordine: servizio e utenti, misura e fonte, soglia e finestra, eccezioni, rendicontazione tecnica, escalation e verifica della chiusura. **Errore tipico:** usare “KPI” come sinonimo di qualsiasi numero del resoconto tecnico.

La scheda SLA deve rimanere leggibile: servizio, indicatore, definizione, soglia, finestra, periodo, fonte, esclusioni, severità, rendicontazione tecnica, escalation e responsabile della verifica. Se uno di questi campi manca, il dato può essere utile come osservazione tecnica ma non basta a sostenere una contestazione o una decisione contrattuale.

### Leggere uno scostamento senza automatismi

La misura va progettata prima che il servizio entri in difficoltà. Per ogni indicatore è necessario stabilire chi raccoglie il dato, con quale strumento, come si gestiscono dati mancanti e differenze di orologio, chi può contestare il calcolo e dove resta la traccia della decisione. Un dato prodotto dal fornitore non è inattendibile per definizione; diventa fragile quando l'ente non può ricostruire il perimetro o confrontarlo con segnali indipendenti, come segnalazioni degli utenti, log applicativi o esiti delle integrazioni.

La disponibilità non esaurisce l'esperienza del servizio. Un portale può essere raggiungibile e insieme impedire di completare una pratica perché l'autenticazione o il pagamento non rispondono. Per questo la scheda distingue componenti, percorsi essenziali e classi di impatto. La stessa cautela vale per presa in carico, ripristino e risoluzione: sono momenti diversi. Dire che un ticket è stato preso in carico non dimostra che l'utente abbia recuperato la funzione; dire che è stato ripristinato non dimostra ancora che la causa non ricorrerà.

Davanti a una deviazione, la sequenza ordinata è: accertare il fatto, delimitare utenti e servizi coinvolti, attivare il canale previsto, registrare le azioni di contenimento, chiedere analisi e piano correttivo, quindi verificare l'esito. Un indicatore può segnalare l'evento, ma non decide da solo la risposta. Le conseguenze economiche o contrattuali, quando previste, dipendono da atti e circostanze; non vanno dedotte da una percentuale isolata. L'obiettivo prioritario resta riportare il servizio in una condizione affidabile e prevenire la ricorrenza.

Un buon cruscotto non contiene solo valori verdi o rossi. Mostra tendenza, cause, rischio residuo, azioni in scadenza e decisioni richieste. Il candidato può dimostrare maturità osservando che una metrica stabile può nascondere un problema se cambia il volume di utenti o si riduce il perimetro osservato. La domanda corretta non è «il numero rispetta la soglia?», ma «il numero descrive ancora il servizio che cittadini e uffici ricevono?».
## N-TR01-12-04 · Ruoli, evidenze e governo dell'esecuzione

### Competenze diverse, un solo sistema di controllo

Il **RUP**, responsabile unico del progetto, presidia il progetto secondo la disciplina applicabile. Il **direttore dell'esecuzione**, quando previsto, controlla l'esecuzione. L'owner del servizio presidia risultato e utenti; il referente tecnico verifica architettura e deliverable; sicurezza e DPO intervengono per competenza. Il fornitore organizza le proprie responsabilità e produce le evidenze dovute.

Una matrice RACI può chiarire chi esegue, approva, consulta e riceve informazioni. È uno strumento organizzativo: non modifica competenze stabilite dalla normativa o dagli atti.

### Avvio, rendicontazione tecnica e verifiche

Il kick-off traduce il contratto in un assetto operativo: contatti, canali, calendario, deliverable, ambienti, accessi, rendicontazione tecnica, rischi ed escalation. Le decisioni vanno verbalizzate e collegate ai documenti applicabili.

Un resoconto tecnico periodico serve a decidere e controllare, non a raccogliere numeri senza esito. Deve mostrare livelli raggiunti, scostamenti, incidenti, modifiche, rischi, azioni, responsabili e scadenze. L'ente conserva dati sufficienti per verificare la misura anche quando il calcolo è prodotto dal fornitore.

### Non conformità ed escalation

Una **non conformità** è uno scostamento rispetto a requisito, deliverable o obbligo verificabile. Va descritta con evidenza, impatto, causa nota o da analizzare, azione, termine, responsabile e verifica di chiusura.

L'escalation può essere tecnica, gestionale o contrattuale. Saltare subito al livello direzionale crea rumore; restare nel supporto operativo quando il servizio è critico ritarda la risposta. Trigger e canali devono essere stabiliti prima.

### Applicazione: far parlare il resoconto tecnico

Una riunione periodica, da sola, non governa l'esecuzione. Al kick-off si trasformano documenti e impegni in un calendario operativo: contatti, ambienti, canali, deliverable, accessi, frequenza del resoconto tecnico, registro dei rischi e regole di escalation. Un resoconto tecnico utile confronta il risultato atteso con quello osservato e mostra ciò che richiede una decisione. Ticket, livelli di servizio, vulnerabilità, modifiche e scadenze devono quindi avere un responsabile, una data, un'evidenza e un esito, non soltanto un colore di stato.

Il RUP, il direttore dell'esecuzione quando previsto, il referente tecnico, l'owner del servizio, sicurezza e DPO svolgono funzioni che devono restare coerenti con normativa e atti. Una matrice RACI può rendere visibile chi lavora, chi approva, chi viene consultato e chi riceve informazioni; non attribuisce però poteri che non esistono. Il fornitore può produrre misure e resoconto tecnico, ma l'ente deve poterli leggere e verificare. Se nessuno sa contestare una misura o ricostruire una configurazione, il controllo è solo formale.

Una non conformità parte da un fatto osservabile: requisito, deliverable o livello non rispettato. Il registro deve indicare impatto, evidenza disponibile, causa nota o da analizzare, azione, termine, responsabile e criterio di chiusura. L'escalation sale quando l'impatto o il ritardo lo richiedono; non è né una punizione automatica né una catena infinita di e-mail. **Errore tipico:** pensare che la stipula trasferisca al fornitore il risultato pubblico. L'ente conserva il dovere di governare servizio, decisioni ed evidenze.

La chiusura di un'azione deve verificare il risultato e non soltanto la risposta del fornitore. Un ticket “risolto” senza prova, un resoconto tecnico firmato senza confronto con la fonte e una riunione senza decisioni lasciano il rischio invariato. Per questo il registro è anche uno strumento d'esame: obbliga a collegare fatto, criterio, responsabile, azione ed evidenza.

### Catena decisionale e evidenze

Ogni riunione operativa dovrebbe produrre una decisione o una domanda ancora aperta. Per questo il verbale separa fatti osservati, ipotesi, impegni, responsabili e date di riesame. Se il fornitore segnala una difficoltà, l'ente non deve limitarsi a ricevere l'informazione: deve capire quale requisito, servizio o dipendenza è coinvolto, quali utenti sono esposti, quale misura provvisoria è attiva e quale prova chiuderà il problema. Questa disciplina trasforma il confronto periodico in governo del contratto.

Il ruolo tecnico non coincide con il ruolo contrattuale. Il referente applicativo può sapere che una funzione è inutilizzabile; sicurezza può indicare un rischio negli accessi; il DPO può richiedere un esame dei trattamenti; il responsabile unico del progetto e le figure previste dagli atti governano le decisioni nel perimetro delle loro competenze. Collegare questi contributi non significa attribuire a ciascuno poteri inventati. Significa predisporre canali e tempi perché l'evidenza arrivi a chi può decidere.

Una matrice di responsabilità è particolarmente utile nelle attività che attraversano più uffici: attivazione di un account amministrativo, gestione di un incidente, rilascio urgente, verifica di un export dati o passaggio a un nuovo fornitore. Per ciascuna attività occorre distinguere chi prepara il lavoro, chi approva, chi deve essere consultato e chi deve conoscere l'esito. La matrice va poi confrontata con contratto, nomine e procedure interne: se non coincide, prevalgono questi ultimi.

La trasparenza delle evidenze protegge entrambe le parti. Il fornitore sa quale risultato deve dimostrare; l'ente può motivare una richiesta di correzione o la chiusura di un'anomalia. La mancanza di una traccia condivisa, invece, trasforma problemi ordinari in discussioni sulla memoria delle persone. Perciò registri, verbali e prove non sono burocrazia aggiuntiva: sono il ponte tra il servizio realmente erogato e la decisione amministrativa.
## N-TR01-12-05 · Sicurezza, dati e supply chain contrattuale

### Sicurezza come prestazione verificabile

La formula «il fornitore garantisce la sicurezza» non definisce una prestazione verificabile. I requisiti possono riguardare accessi privilegiati, segregazione, logging, patching, vulnerabilità, cifratura, incidenti, backup, test di ripristino e conservazione delle evidenze. Ogni controllo deve essere proporzionato al rischio e verificabile.

Il contratto chiarisce tempi e modalità di cooperazione negli incidenti, preservazione dei log, comunicazioni, contenimento e ripristino. Gli obblighi normativi dell'ente e del fornitore vanno verificati sul caso; lo SLA interno non sostituisce eventuali termini legali.

### Dati e subfornitori

Occorre conoscere quali dati sono trattati, dove transitano, chi vi accede, per quanto tempo sono conservati e come vengono restituiti o cancellati. Formati e procedure di esportazione vanno provati, non soltanto dichiarati.

I subfornitori possono introdurre dipendenze tecniche e geografiche. L'ente deve avere visibilità coerente con rischio e disciplina applicabile. Ruoli privacy, istruzioni, trasferimenti e misure richiedono validazione di giurista e DPO.

### Supply chain

Componenti software, librerie, servizi esterni e aggiornamenti appartengono alla supply chain. Quando pertinente, inventario, provenienza, vulnerabilità, supporto ed eventuale SBOM aiutano a governare il rischio. Il capitolo 8 sviluppa la teoria; qui questi elementi diventano requisiti, resoconto tecnico o condizioni di gestione.

### Applicazione: trasformare il rischio in requisiti

La sicurezza diventa governabile quando si traduce in prestazioni verificabili e proporzionate. A seconda del servizio, il contratto può richiedere gestione degli accessi privilegiati, registrazione degli eventi rilevanti, trattamento delle vulnerabilità, cooperazione negli incidenti, copie di sicurezza, prove di recupero e conservazione delle evidenze. Non esiste una formula valida per tutti i casi: ciò che è ragionevole per un servizio informativo può non bastare per un servizio che gestisce pratiche, pagamenti o dati sensibili.

Per i dati bisogna sapere quali categorie sono trattate, dove transitano, chi accede, quali integrazioni le ricevono e come saranno restituite o cancellate. Il contratto non può decidere da solo ruoli privacy o trasferimenti: questi aspetti vanno esaminati nel caso concreto con le figure competenti. Il candidato deve però riconoscere l'errore di rinviare tutto a una clausola generica. Anche un'esportazione dichiarata disponibile va provata su dati e formati definiti, verificando metadati, completezza e riuso.

La supply chain comprende componenti, librerie, servizi esterni, aggiornamenti e subfornitori che rendono possibile la prestazione. L'ente non deve trasformarsi nel gestore tecnico di ogni componente, ma deve conoscere le dipendenze rilevanti, le evidenze disponibili e i trigger di escalation. Un inventario, una dichiarazione di provenienza o una SBOM possono aiutare quando sono pertinenti, senza diventare un adempimento decorativo. **Errore tipico:** scrivere che il fornitore “garantisce la sicurezza” senza dire come l'ente verifica accessi, incidenti, dati, subfornitori e rimedi.

Quando il servizio usa componenti esterni, l'ente deve prevedere come ricevere notifiche, come valutare impatto e chi autorizza le azioni urgenti. Questa preparazione evita due errori opposti: accettare automaticamente ogni aggiornamento del fornitore oppure bloccare ogni cambiamento fino a compromettere sicurezza e continuità. La decisione resta proporzionata, documentata e verificabile.

### Presidi proporzionati e verificabili

La sicurezza contrattuale richiede un equilibrio. Elencare ogni possibile controllo senza collegarlo al servizio genera obblighi difficili da valutare; una clausola astratta lascia invece spazio a interpretazioni incompatibili. Il punto di partenza è il rischio: dati, criticità del servizio, esposizione esterna, utenti, integrazioni, privilegi amministrativi e dipendenze. Da qui si scelgono requisiti osservabili, fonti di evidenza e modalità di riesame. Il lettore non deve memorizzare una lista universale, ma imparare a collegare controllo, minaccia e prova.

Gli accessi amministrativi meritano una particolare attenzione perché consentono modifiche ampie. Devono essere attribuibili, limitati, riesaminabili e tracciati secondo il perimetro definito. Analogamente, log e alert non sono utili se nessuno sa conservarli, leggerli e collegarli a un incidente. Nel contratto contano quindi sia la disponibilità del dato sia la cooperazione: chi avvisa, con quali informazioni, chi decide il contenimento e come viene conservata l'evidenza della chiusura.

La presenza di un subfornitore non equivale automaticamente a una non conformità, ma non può restare invisibile. L'ente deve conoscere, nella misura richiesta dal caso, quale parte del servizio è affidata all'esterno, quali dati o componenti coinvolge, quali controlli si applicano e come viene gestita una variazione. Lo stesso vale per componenti che arrivano tramite una filiera software: provenienza, supporto, aggiornamenti e vulnerabilità diventano rilevanti quando incidono su continuità o sicurezza del servizio acquistato.

Nella pratica la verifica può combinare evidenze diverse: configurazioni, registri di accesso, risultati di test, attestazioni, elenco delle dipendenze, esiti di esercitazioni e verbali di gestione dell'incidente. Nessuna prova isolata basta sempre. L'ente cerca coerenza tra ciò che è promesso, ciò che è configurato e ciò che accade durante l'esercizio. Questo evita sia l'affidamento cieco a una dichiarazione, sia una richiesta di documenti privi di un criterio di lettura.
## N-TR01-12-06 · Modifiche, rilasci e continuità del servizio

### Classificare le modifiche

Correzione di un difetto, manutenzione ordinaria, evoluzione funzionale, variazione del perimetro e modifica contrattuale non sono sinonimi. La classificazione determina analisi, approvazioni, costi, test e documentazione.

Una change request descrive motivo, impatto, dipendenze, rischio, piano di test, rilascio e rollback. Versioni di requisito, configurazione, codice, documentazione e approvazione devono essere riconciliabili.

### Cutover e rollback

Il **cutover** è il passaggio operativo alla nuova soluzione o versione. Richiede prerequisiti, sequenza, responsabili, comunicazioni e criteri di go/no-go. Il **rollback** riporta a una condizione precedente controllata se il rilascio non soddisfa i criteri.

### Continuità

Backup, replica, alta disponibilità e disaster recovery rispondono a scopi diversi. RPO e RTO, spiegati nel capitolo 7, diventano qui requisiti da provare. Finché non viene provato, il piano non dimostra la capacità di ripristino.

Il contratto deve considerare anche obsolescenza ed end of support. Un componente non più supportato può trasformare manutenzione e sicurezza in un rischio di continuità.

### Applicazione: non confondere il rilascio con il risultato

Una modifica può correggere un difetto, aggiornare una componente, estendere una funzione, cambiare un perimetro o incidere sugli impegni contrattuali. La distinzione serve perché non tutte le variazioni chiedono lo stesso controllo. Una change request ben costruita indica motivo, impatto su utenti e dipendenze, versione coinvolta, rischi, test, approvazioni, piano di rilascio e condizioni di rollback. Se cambia un requisito, devono rimanere riconciliabili anche criteri di accettazione, test ed evidenze.

Il cutover è il passaggio alla nuova versione o soluzione. Prima del go/no-go occorrono prerequisiti, responsabilità, comunicazioni e criteri osservabili; dopo il rilascio occorre verificare l'effetto, non soltanto la riuscita tecnica della procedura. Il rollback riporta a una condizione precedente controllata quando non sono rispettati i criteri. Non è un'ammissione di fallimento: è un presidio per limitare l'impatto mentre si analizza il problema.

Backup, replica, alta disponibilità e disaster recovery rispondono a bisogni differenti. RPO e RTO aiutano a esprimere rispettivamente la perdita di dati tollerabile e il tempo di recupero atteso, ma acquistano valore soltanto se sono coerenti con il servizio e vengono provati. Un piano non testato non dimostra capacità di ripristino. Anche l'obsolescenza e la fine del supporto devono entrare nel monitoraggio: una dipendenza non più mantenuta può trasformare un aggiornamento rinviato in un problema di sicurezza e continuità. **Errore tipico:** trattare ogni rilascio come manutenzione ordinaria e scoprire solo dopo l'impatto su dati, integrazioni o utenti.

Per il candidato, la domanda utile è: quale evidenza dimostra che il servizio può continuare dopo un cambiamento? La risposta combina test, inventario delle dipendenze, documentazione aggiornata, responsabilità chiare e prova di recupero. Un contratto può prevedere questi elementi; l'efficacia dipende però dalla loro applicazione durante l'esecuzione, non dalla sola presenza di un titolo nel capitolato.

### Continuità come prova, non come etichetta

Il piano di rilascio deve descrivere non solo la sequenza tecnica ma anche l'impatto sul servizio. Chi comunica agli utenti? Quali integrazioni possono risentirne? Quale dato deve essere salvaguardato? Quale condizione ferma il passaggio e quale consente il ritorno alla versione precedente? Queste domande aiutano a costruire criteri di go/no-go concreti. Il go non è la semplice autorizzazione a premere un pulsante; è la decisione, basata su evidenze, che prerequisiti e rischi residui sono accettabili.

Prima di un rilascio rilevante sono utili test coerenti con l'uso previsto: funzionali, di integrazione, di sicurezza, di prestazione o di recupero, secondo il caso. L'ambiente di prova e i dati utilizzati devono essere sufficientemente rappresentativi, altrimenti un esito positivo può non dire nulla sul funzionamento reale. Dopo il rilascio, l'osservazione prosegue: un controllo su log, ticket, tempi di risposta e percorsi utente può rivelare una regressione che il test iniziale non aveva intercettato.

RPO e RTO non sono sigle decorative. Esprimono, rispettivamente, quanta perdita di dati può essere tollerata e in quale tempo il servizio deve recuperare una condizione operativa. I valori non sono standard: derivano dal danno che il fermo o la perdita produrrebbero per utenti e amministrazione. Per questo vanno collegati a responsabilità, mezzi tecnici, prova periodica e decisione sulle eccezioni. Dire che esiste un backup non dimostra che il ripristino sia possibile entro il bisogno del servizio.

Anche l'obsolescenza richiede anticipo. Una libreria senza supporto, una piattaforma che cambia condizioni o un'integrazione destinata a chiudere possono produrre un rischio prevedibile. Il registro delle dipendenze, aggiornato nel governo del fornitore, consente di pianificare migrazione, aggiornamento o sostituzione prima che la scelta diventi emergenziale. In prova, il candidato mostra questa continuità: modifica, test, decisione, monitoraggio e aggiornamento dell'inventario.
## N-TR01-12-07 · Lock-in, portabilità, reversibilità ed exit strategy

### Forme di dipendenza

Il **lock-in** non riguarda soltanto la tecnologia. Può dipendere da:

- formati o API non trasferibili;
- licenze e condizioni contrattuali;
- costi di estrazione o migrazione;
- processi organizzativi costruiti sul fornitore;
- documentazione incompleta;
- competenze presenti solo nel gruppo esterno;
- dati, configurazioni o log non esportabili.

### Portabilità e reversibilità

La **portabilità** consente di trasferire dati, applicazioni o carichi in un altro ambiente. La **reversibilità** comprende il ritorno o il passaggio controllato del servizio, con conoscenze, configurazioni, documenti e assistenza alla transizione.

La consegna finale di un file, da sola, non garantisce la portabilità. Occorre verificare completezza, struttura, metadati, leggibilità, tempi e capacità del destinatario di riutilizzarlo.

### Exit plan

L'exit plan definisce:

1. eventi che lo attivano;
2. ruoli e governance della transizione;
3. inventario di dati, configurazioni, integrazioni e documenti;
4. formati e procedure di estrazione;
5. supporto al subentro;
6. continuità durante il passaggio;
7. verifica di restituzione e cancellazione;
8. criteri di chiusura e accettazione finale.

Preparare l'exit plan soltanto alla scadenza è tardivo: l'ente deve progettarlo all'ingresso e provarlo durante l'esecuzione.

### Uscita progettata fin dall'ingresso

Il lock-in è spesso il risultato di piccole decisioni accumulate. Un formato proprietario senza schema, un'API non documentata, un ambiente configurato solo dal fornitore o una squadra interna che non conosce più il servizio possono rendere impossibile il cambio anche quando il contratto è formalmente concluso. Per questo la dipendenza va osservata in cinque dimensioni: tecnica, dati, contratto, economia e organizzazione. Ciascuna richiede una domanda concreta: cosa bisogna trasferire, chi ne possiede il diritto, quanto costa estrarlo, chi sa usarlo e quale servizio deve rimanere disponibile durante la transizione.

La portabilità riguarda la possibilità materiale di trasferire elementi riutilizzabili; la reversibilità riguarda il percorso controllato che permette di uscire, rientrare o passare a un altro gestore. Un'esportazione è utile solo se include gli oggetti necessari, conserva struttura e metadati, è accompagnata da documentazione e può essere verificata dal destinatario. Per le configurazioni, la domanda non è solo «posso scaricarle?», ma «posso ricostruire un ambiente funzionante senza conoscere segreti non consegnati?».

L'exit plan deve essere trattato come un deliverable vivo. All'avvio raccoglie inventario, ruoli e condizioni di restituzione; durante l'esecuzione viene aggiornato quando cambiano dati, integrazioni, componenti o subfornitori; prima della transizione definisce sequenza, supporto, controlli di continuità e criteri di chiusura. I trigger possono essere scadenza, recesso, insostenibilità tecnica, cambiamento organizzativo o semplice esigenza di verifica periodica. La loro disciplina concreta dipende dal contratto, ma la preparazione tecnica non può aspettare l'evento.

Una prova di uscita non richiede necessariamente di migrare davvero tutto il servizio. Può iniziare con un campione rappresentativo: esportare dati, verificare schema e completezza, ricostruire una configurazione in ambiente controllato, misurare le dipendenze non trasferite e annotare le correzioni. Se il test fallisce, l'esito non è un dettaglio tecnico: segnala che requisito, documentazione, competenze o supporto al subentro sono insufficienti. L'ente deve quindi aggiornare piano e controllo prima che il rischio diventi urgente.

L'uscita ha anche una dimensione di continuità e sicurezza. Durante il passaggio si proteggono accessi, dati, log e servizi essenziali; al termine si verifica che permessi, copie e trattamenti residui siano gestiti secondo il caso. Non basta dichiarare che i dati sono stati cancellati o consegnati: occorre disporre dell'evidenza prevista e verificare che il nuovo assetto sappia svolgere il servizio. **Errore tipico:** chiamare exit strategy un elenco di file finali. Un'uscita reale trasferisce capacità operativa, non soltanto materiale digitale.

Una verifica di uscita ben documentata riduce anche l'asimmetria informativa: permette all'ente di capire quali attività restano indispensabili, quali dipendenze richiedono un piano e quali conoscenze devono essere trasferite prima della chiusura.

L'esito della prova va condiviso con i responsabili del servizio, così che l'uscita resti una capacità organizzativa e non una conoscenza isolata.

## ▣ Verifica

Le domande seguenti controllano le distinzioni che rendono governabile un contratto ICT. Rispondi prima a voce, poi confronta la motivazione.

### Quiz 1 — Dal bisogno alla scelta

Un ufficio chiede «un nuovo cloud» senza descrivere utenti, carichi, integrazioni o indisponibilità attuale. Qual è il primo passo?

**Risposta corretta:** costruire una baseline e definire il risultato pubblico, il perimetro e i vincoli prima di scegliere la soluzione. La tecnologia può essere una risposta, non il bisogno da dimostrare.

### Quiz 2 — Requisito e accettazione

«Il portale deve essere sicuro» è sufficiente per accettare la prestazione?

**Risposta corretta:** no. Occorrono requisiti osservabili, condizioni di prova, criterio di accettazione ed evidenza. Un'affermazione generica non permette di stabilire né il risultato né la chiusura di un'anomalia.

### Quiz 3 — SLA, SLI e KPI

Un cruscotto mostra il numero di ticket aperti: è automaticamente uno SLA?

**Risposta corretta:** no. Può essere un KPI di governo. Per essere uno SLA occorrono un impegno definito, metrica, soglia, finestra, fonte, esclusioni e responsabilità di verifica.

### Quiz 4 — Governo dell'esecuzione

Il fornitore invia una misura mensile; l'ente può limitarvisi?

**Risposta corretta:** no. Deve poter comprendere perimetro e fonte del dato, collegarlo a utenti e requisiti, registrare scostamenti e verificare le azioni correttive. La misura prodotta dal fornitore non sostituisce il controllo dell'ente.

### Quiz 5 — Sicurezza e filiera

Una clausola che impone al fornitore di «garantire la sicurezza» basta a governare la filiera?

**Risposta corretta:** no. Il contratto deve tradurre il rischio in evidenze e modalità di cooperazione: accessi, log, vulnerabilità, incidenti, dati, dipendenze e subfornitori, in modo proporzionato al servizio.

### Quiz 6 — Portabilità ed uscita

Alla scadenza il fornitore consegna un archivio dati. L'exit è dimostrata?

**Risposta corretta:** non ancora. Occorre verificare completezza, struttura, metadati, configurazioni, documentazione, supporto alla transizione e capacità del destinatario di riutilizzare quanto ricevuto senza interrompere il servizio.
## Strumenti di acquisto e ciclo digitale

Consip opera nell'ambito del programma di razionalizzazione degli acquisti. Acquisti in Rete è il canale attraverso cui amministrazioni e imprese accedono agli strumenti; il MEPA è uno di questi. Convenzioni, accordi quadro e sistemi dinamici hanno logiche diverse. Nessuno strumento elimina la necessità di definire fabbisogno, requisiti, copertura e controlli.

La digitalizzazione riguarda tutto il ciclo del contratto. La BDNCP è la banca dati nazionale gestita da ANAC; la PCP e il FVOE svolgono funzioni specifiche nell'ecosistema. Non vanno trattati come sinonimi. Dettagli operativi, procedure e soglie devono essere verificati sulle fonti vigenti e restano nella sede contrattuale generale.

## Caso guidato: servizio cloud comunale

Un comune acquisisce migrazione, hosting cloud, manutenzione e assistenza per un portale al cittadino.

1. **Bisogno:** garantire accesso e continuità; baseline con utenti, carichi e incidenti.
2. **Perimetro:** migrazione, ambienti, integrazioni, supporto, sicurezza, documentazione ed uscita.
3. **Requisiti:** funzioni del portale più disponibilità, accessibilità, capacità, logging e portabilità.
4. **Accettazione:** test funzionali, prestazionali, di accesso, migrazione e ripristino con verbale.
5. **SLA:** indicatori distinti per disponibilità, presa in carico e ripristino; fonte e finestra concordate.
6. **Sicurezza:** account privilegiati, log, vulnerabilità, incidenti e subfornitori tracciati.
7. **Esecuzione:** resoconto tecnico mensile, registro rischi, non conformità e escalation.
8. **Change:** ogni rilascio ha impatto, test, go/no-go e rollback.
9. **Continuità:** backup e ripristino sono provati; RPO/RTO coerenti col servizio.
10. **Uscita:** esportazione di dati e configurazioni, documentazione, supporto al subentro e verifica di cancellazione.

Il caso non determina procedura, soglia o penale: tali elementi dipendono dagli atti e dalla disciplina vigente.

## Laboratorio operativo

### Checklist del capitolato

- [ ] bisogno, baseline, utenti e perimetro sono chiari;
- [ ] requisiti funzionali e non funzionali sono verificabili;
- [ ] ogni requisito critico ha criterio di accettazione ed evidenza;
- [ ] dati, integrazioni, ambienti e migrazione sono descritti;
- [ ] SLA indicano misura, soglia, finestra, fonte ed esclusioni;
- [ ] ruoli, rendicontazione tecnica, non conformità ed escalation sono definiti;
- [ ] sicurezza, incidenti, continuità e subfornitori sono governati;
- [ ] change, versioni, cutover e rollback sono tracciati;
- [ ] portabilità, reversibilità ed exit plan sono provabili.

### Scheda SLA

| Campo | Compilazione |
| --- | --- |
| servizio e indicatore | che cosa misuriamo |
| soglia e periodo | livello e intervallo |
| fonte e punto di misura | da quali dati |
| esclusioni | casi ammessi e motivati |
| rendicontazione tecnica | frequenza e responsabile |
| escalation | trigger e canale |

### Registro fornitore

| Elemento | Dipendenza | Rischio | Controllo | Evidenza |
| --- | --- | --- | --- | --- |
| servizio | da compilare | da valutare | da definire | resoconto tecnico |
| dati | da compilare | da valutare | esportazione | prova |
| subfornitore | da compilare | da valutare | monitoraggio | registro |

## Domanda da commissario

**Come imposteresti e controlleresti un contratto per un servizio cloud destinato ai cittadini?**

Partirei dal risultato pubblico, dalla baseline e dal perimetro. Tradurrei il bisogno in requisiti funzionali e non funzionali, ciascuno collegato a criteri di accettazione ed evidenze. Definirei SLA misurabili con fonte, finestra, soglia ed esclusioni. Assegnerei ruoli a RUP, direzione dell'esecuzione, owner, tecnici, sicurezza, DPO e fornitore. Governerei resoconto tecnico, non conformità, incidenti, modifiche, continuità e supply chain. Infine predisporrei fin dall'inizio portabilità, reversibilità ed exit plan. Procedura e clausole puntuali sarebbero verificate sugli atti e sul quadro vigente.

## Domande-trappola

- **Un requisito molto dettagliato è sempre verificabile?** No: servono condizione, risultato ed evidenza.
- **Disponibilità del 99,9% basta da sola?** No: mancano perimetro, finestra, fonte, periodo ed esclusioni.
- **SLA e KPI sono sinonimi?** No: un KPI può non essere un impegno contrattuale.
- **La stipula conclude il controllo dell'ente?** No: l'esecuzione richiede verifica e governo.
- **La penale risolve il disservizio?** No: servono ripristino e azione correttiva.
- **Il backup è disaster recovery?** No: è solo uno dei possibili presidi.
- **Il cloud trasferisce ogni responsabilità al provider?** No: i ruoli dipendono dal caso e dagli atti.
- **L'exit strategy si prepara alla scadenza?** No: si progetta all'ingresso.
- **MEPA è Consip?** No: MEPA è uno strumento; Consip è il soggetto che opera nel programma.

## Mini-esercizi e soluzioni

**1.** «Il portale deve essere intuitivo» è un requisito verificabile?

**Soluzione:** no. Occorre tradurlo in condizioni e verifiche osservabili, per esempio compiti, profili di utenti, criteri di completamento e test di accessibilità o usabilità appropriati.

**2.** Un resoconto tecnico indica soltanto «disponibilità 99,5%». Che cosa manca?

**Soluzione:** almeno perimetro, finestra, periodo, fonte, regola di calcolo, esclusioni e soglia contrattuale di confronto.

**3.** Il fornitore propone una nuova versione il giorno prima del rilascio. Quali evidenze chiedere?

**Soluzione:** impatto, versione, dipendenze, test, approvazione, piano di cutover, criteri di go/no-go e rollback.

**4.** Alla scadenza l'ente riceve un file senza schema né metadati. È portabilità effettiva?

**Soluzione:** non ancora. Deve verificare completezza, struttura, documentazione, leggibilità e riuso nel sistema destinatario.

## Da sapere in 5 righe

Il fabbisogno deve diventare una prestazione verificabile.
Requisito, accettazione, criterio di valutazione e SLA non sono sinonimi.
Un livello di servizio vale solo se misura, finestra, fonte ed esclusioni sono chiare.
Acquistare non trasferisce all'esterno il governo del servizio.
Portabilità ed uscita si progettano prima della stipula e si verificano durante l'esecuzione.

## Riferimenti per l'approfondimento

- Codice dei contratti pubblici e relativi allegati, nel testo vigente.
- Indicazioni ufficiali di ANAC sulla digitalizzazione del ciclo di vita del contratto.
- Materiali istituzionali di Consip e Acquisti in Rete sugli strumenti di acquisto e negoziazione.
- Documentazione istituzionale applicabile su cloud della PA, interoperabilità, sicurezza e protezione dei dati.
- Standard e buone pratiche di service management, continuità e portabilità, da applicare in modo coerente con gli atti del caso.

## Avvertenze operative

Procedure, soglie, termini, penali, clausole, qualificazione cloud, ruoli privacy e condizioni di subfornitura dipendono dal quadro vigente e dagli atti del caso. Vanno quindi verificati, alla data del bando o della pubblicazione, sulle fonti istituzionali vigenti; questo capitolo non fissa valori o modelli contrattuali universali.
