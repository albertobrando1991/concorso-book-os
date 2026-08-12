---
id: chapter-m-tr01-06
type: book_chapter
title: "Ingegneria software, API e interoperabilità PA"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["ingegneria software", "api", "interoperabilità", "PDND", "testing"]
entities: ["IEEE Computer Society", "IETF", "OpenAPI Initiative", "AgID", "PDND", "Unione europea"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale", "sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.82
updated_at: 2026-08-10
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "software-engineering", "api", "interoperabilita"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 6
format_version: 2
dati_operativi: false
draft_stage: written
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale", "sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche", "topics/open-data-interoperabilita-cloud-pa", "topics/pa-digitale", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-06-piano-completamento"]
---

# Ingegneria software, API e interoperabilità PA

Un servizio digitale nasce da un bisogno, non dal codice. Coinvolge persone e amministrazioni, tratta dati, dipende da altri sistemi e deve continuare a funzionare mentre requisiti e contesto cambiano. Perciò non basta realizzarlo: occorre dimostrare che risponde al bisogno, governarne l’evoluzione e consentire ad altri sistemi di usarlo senza conoscerne l’implementazione interna.

L’ingegneria software disciplina questo percorso. Le API rendono espliciti i contratti fra sistemi; l’interoperabilità li collega a regole organizzative, semantiche e tecniche. Nella PA il risultato atteso è un servizio affidabile, comprensibile, autorizzato e governabile. L’endpoint ne costituisce soltanto l’interfaccia tecnica.

## Obiettivo, inquadramento e confine con il VOL-01

Il VOL-01, capitolo 10, § 16, introduce API, interoperabilità e PDND e chiarisce che scambio autorizzato e pubblicazione open data sono fenomeni diversi. Qui quei prerequisiti diventano strumenti di progettazione.

Dopo lo studio del capitolo dovrai saper:

- trasformare un bisogno in requisiti verificabili;
- confrontare modelli di ciclo di vita senza applicarli meccanicamente;
- leggere un’architettura per componenti, interfacce e dipendenze;
- distinguere verifica, validazione e livelli di test;
- spiegare controllo di versione e gestione delle modifiche;
- progettare il contratto essenziale di un’API;
- riconoscere compatibilità, idempotenza, errori e livelli di servizio;
- distinguere i livelli dell’interoperabilità;
- costruire un caso e-service con erogatore, fruitore, finalità ed evidenze.

Programmazione e strutture dati sono nel capitolo 3; basi dati nel capitolo 4; HTTP come protocollo e i servizi di rete nel capitolo 5. Cloud e CI/CD operativa sono nel capitolo 7; sicurezza, IAM e incident response nei capitoli 8-9; data governance e interoperabilità semantica nel capitolo 10; SLA contrattuali e fornitori nel capitolo 12.

## Mappa BANDO dal requisito all’e-service

| Passaggio | Domanda da porsi | Azione |
| --- | --- | --- |
| **B — Bando** | Sono richiesti metodologie, testing, API, standard o piattaforme specifiche? | Separare il nucleo trasferibile dai dettagli di prodotto. |
| **A — Aree** | La domanda riguarda bisogno, progetto, test, contratto API o interoperabilità? | Collocare il problema nella fase e nel livello corretti. |
| **N — Nuclei** | Quali elementi devono restare verificabili ed evolvibili? | Collegare requisito, interfaccia, test, versione ed evidenza. |
| **D — Diario** | Quale assunzione ha prodotto un errore o una modifica incompatibile? | Registrare decisione, impatto, prova e correzione. |
| **O — Output** | Serve una risposta orale, un caso, una specifica o una matrice? | Produrre l’artefatto richiesto, non una lista di acronimi. |

## N-TR01-06-01 · Requisiti e ciclo di vita verificabile

Un **bisogno** descrive il risultato atteso da un soggetto. Un **requisito** traduce quel bisogno in una proprietà o capacità che il sistema deve possedere. Un **vincolo** limita le soluzioni ammissibili: può derivare da norme, standard, tecnologie già presenti, tempi, budget o organizzazione. Il **criterio di accettazione** indica invece una condizione osservabile con cui stabilire se il requisito è soddisfatto.

Esempio: «ridurre le richieste di certificati già disponibili» è un bisogno. «Il servizio deve verificare, previa autorizzazione, il possesso del requisito anagrafico presso il sistema erogatore» è un requisito funzionale. «La risposta deve essere disponibile entro il tempo concordato e ogni richiesta deve essere tracciabile» introduce requisiti non funzionali. «Dato valido → esito coerente; dato inesistente → errore classificato; fruitore non abilitato → richiesta rifiutata» fornisce criteri verificabili.

### Requisiti funzionali e non funzionali

I **requisiti funzionali** descrivono comportamenti, dati elaborati e risultati. I **requisiti non funzionali** qualificano il servizio: prestazioni, disponibilità, usabilità, accessibilità, sicurezza, manutenibilità, portabilità e osservabilità.

I requisiti non funzionali hanno effetti concreti. Un servizio può restituire il dato corretto e risultare comunque inadeguato perché non regge il carico, esclude parte degli utenti o rende impossibile ricostruire gli errori.

Per essere utilizzabile, un requisito deve rispondere a un bisogno riconoscibile, evitare ambiguità e restare coerente con gli altri. Deve inoltre risultare realizzabile, verificabile e collegabile a progetto, test e rilascio.

### Tracciabilità

La tracciabilità consente di seguire un requisito lungo il ciclo di vita.

| Requisito | Componente o API | Criterio | Test | Evidenza |
| --- | --- | --- | --- | --- |
| verificare un requisito anagrafico | servizio di verifica | esito coerente per tre classi di input | integrazione e accettazione | esito di esecuzione registrato |
| registrare l’uso | componente di audit | evento presente e correlabile | sistema | evento con identificativo |

Se una modifica interessa il requisito, la matrice aiuta a individuare contratto, test e documentazione da aggiornare. Se un test non è collegato a nessuna promessa, può essere ridondante; se una promessa non ha test, manca un’evidenza.

### Ciclo di vita e organizzazione dello sviluppo

Il **ciclo di vita del software** comprende attività di concezione, analisi, progettazione, realizzazione, verifica, rilascio, esercizio, manutenzione e dismissione. Le attività possono sovrapporsi e ripetersi: la sequenza dipende da rischio, stabilità dei requisiti, dimensione, vincoli e capacità dell’organizzazione.

Un modello **sequenziale** rende esplicite fasi e approvazioni ed è utile quando requisiti e vincoli sono abbastanza stabili. Il limite emerge quando il feedback arriva tardi. Un modello **iterativo** rivede più volte la soluzione; uno **incrementale** consegna parti utilizzabili in passi successivi. Gli approcci Agile privilegiano feedback frequente, collaborazione e adattamento, ma non eliminano architettura, documentazione, controllo e responsabilità.

La scelta del modello dipende dalla capacità di produrre evidenze in tempo utile, governare i rischi e rispettare i vincoli del servizio. L’etichetta «Agile» o «tradizionale», da sola, dice poco.

### Ruoli e responsabilità

Il committente definisce obiettivi e vincoli insieme agli utenti e agli altri portatori d’interesse. Gli analisti precisano i requisiti; progettisti e sviluppatori costruiscono la soluzione, mentre i tester raccolgono le evidenze e operations gestisce l’esercizio. Un responsabile del prodotto o del servizio ordina priorità e accettazione. Anche quando un fornitore riunisce più ruoli, responsabilità e criteri decisionali devono restare espliciti.

### Configurazione e controllo di versione

La **gestione della configurazione** identifica gli elementi controllati — codice, specifiche, schemi, configurazioni, test e documenti — e ne governa le modifiche. Il **controllo di versione** conserva la storia e permette di associare uno stato a una release.

Nel modello distribuito diffuso da Git, un repository conserva oggetti e riferimenti; un commit registra uno stato; un branch rappresenta una linea di sviluppo; un merge integra storie divergenti; un tag identifica un punto significativo. Il repository non garantisce qualità: servono regole su revisione, test, approvazione, tracciabilità e ripristino. L’integrazione continua automatizza controlli frequenti; deployment e infrastruttura della pipeline appartengono al capitolo 7.

## N-TR01-06-02 · Architettura e qualità del software

L’**architettura software** descrive elementi significativi, responsabilità, relazioni e decisioni che condizionano l’evoluzione del sistema. Un **componente** racchiude una responsabilità; un’**interfaccia** espone modalità di interazione; una **dipendenza** indica che un elemento necessita di un altro.

Alta **coesione** significa che le responsabilità di un componente sono correlate. Basso **accoppiamento** riduce le conoscenze e le dipendenze necessarie fra componenti. Non sono valori assoluti: l’obiettivo è evitare legami inutili e rendere visibili quelli inevitabili.

### Forme architetturali

Un sistema **monolitico** distribuisce insieme più funzioni. Può essere semplice da avviare e operare, ma una crescita disordinata rende più difficili modifiche e rilasci. Un’architettura **a livelli** separa responsabilità. Il modello **client-server** distingue richiedente ed erogatore. Un’architettura **a servizi** scompone capacità dietro contratti, aumentando l’autonomia potenziale ma anche esigenze di rete, osservabilità e governo.

Scala, competenze, vincoli, frequenza delle modifiche e qualità richieste determinano quale forma architetturale sia più adatta al caso.

### Attributi di qualità e trade-off

Fra gli attributi di qualità rientrano affidabilità, prestazioni, usabilità, accessibilità, sicurezza e manutenibilità. Portabilità, interoperabilità e osservabilità diventano decisive quando il sistema deve integrarsi ed evolvere. Ogni scelta comporta un costo: molti servizi acquistano autonomia ma introducono comunicazioni remote e gestione distribuita; una cache riduce la latenza ma richiede una politica di coerenza. Il progetto deve dichiarare il compromesso adottato.

### Dal requisito alla decisione architetturale

Una decisione architetturale ha valore se collega una necessità a una conseguenza verificabile. Una funzione che deve evolvere senza imporre il rilascio dell’intero sistema richiede responsabilità e contratto separati; in cambio, introduce versioni, dipendenze e gestione operativa. Con un carico prevedibile e un gruppo piccolo, invece, una distribuzione unitaria può contenere complessità e costi. La forma architetturale dipende dal problema, non dalla moda del momento.

| Esigenza | Decisione da valutare | Conseguenza da verificare |
| --- | --- | --- |
| modifiche frequenti a una funzione | confine di componente più autonomo | impatto su dipendenze, test e rilascio |
| alta disponibilità | ridondanza dei componenti critici | coerenza dello stato e gestione dei guasti |
| integrazione con più fruitori | contratto esterno stabile | compatibilità, documentazione e versioni |
| dati sensibili | separazione delle responsabilità e accessi minimi | autorizzazioni, tracciabilità e superficie esposta |
| tempi di risposta contenuti | cache o elaborazione differita | consistenza, invalidazione e osservabilità |

Ogni diagramma risponde a una domanda diversa. La vista di contesto mostra attori e sistemi esterni; quella dei componenti chiarisce responsabilità e dipendenze; la vista di distribuzione colloca gli elementi in esecuzione. Sono rappresentazioni complementari. In una prova va scelta quella pertinente alla domanda, dichiarandone il livello di astrazione.

La qualità va resa misurabile. “Manutenibile” può tradursi in componenti con responsabilità chiare, dipendenze controllate, test aggiornati e tempo sostenibile per introdurre una modifica. “Affidabile” richiede scenari di guasto, comportamento atteso e prove. L’attributo non coincide con una tecnologia: è una proprietà osservabile del sistema nel suo contesto.

**Uso concorsuale.** Una risposta architetturale solida muove dai requisiti più vincolanti, propone una struttura, considera almeno un’alternativa e motiva il compromesso. Va inoltre chiarito come verificare la decisione: con test, metriche, un prototipo o una revisione dell’architettura. Senza criteri di verifica, il disegno resta soltanto illustrativo.

Le decisioni significative vanno registrate con contesto, opzioni, scelta, motivazione e conseguenze. Questa traccia evita che un vincolo temporaneo diventi una regola incomprensibile e permette di riesaminare la scelta quando cambiano carico, requisiti o dipendenze. Non serve documentare ogni dettaglio: conta conservare ciò che limita le evoluzioni future.

Un confine architetturale è efficace se protegge una responsabilità e offre un’interfaccia comprensibile. Separare componenti senza autonomia reale moltiplica chiamate e versioni; accorpare responsabilità indipendenti rende invece ogni modifica più rischiosa. Coesione e accoppiamento si valutano osservando quali cambiamenti si propagano e quali dati ogni parte deve conoscere.

**Errore ricorrente.** Disegnare molti blocchi e chiamarli “microservizi” non dimostra modularità. Il candidato deve spiegare proprietà dei confini, gestione dei dati, dipendenze e costo operativo. Il nome della forma architetturale viene dopo la motivazione.

## N-TR01-06-03 · Verifica, validazione, test e configurazione

La **verifica** controlla che il prodotto sia costruito secondo specifiche e progetto. La **validazione** controlla che il prodotto risponda al bisogno d’uso.

| Livello | Oggetto | Esempio |
| --- | --- | --- |
| unitario | funzione o componente isolato | calcolo di una regola |
| integrazione | interazione fra elementi | chiamata fra servizio e database |
| sistema | comportamento complessivo | flusso end-to-end |
| accettazione | criteri concordati con stakeholder | esito del caso amministrativo |
| regressione | funzioni già valide dopo una modifica | suite rieseguita su nuova release |

Un **caso di test** specifica identificativo, obiettivo, precondizioni, dati di ingresso, passi, risultato atteso e risultato ottenuto. Un **difetto** è una carenza nel prodotto o in un artefatto; una **failure** è il comportamento osservato che non soddisfa il risultato atteso. Gravità e priorità non coincidono: la prima misura l’impatto, la seconda ordina l’intervento.

### Strategia, copertura ed evidenze

La strategia di test stabilisce che cosa verificare, a quale livello, con quali dati e in quale ambiente. Una quantità elevata di test unitari non compensa l’assenza di prove sulle integrazioni; affidarsi a un solo test end-to-end, d’altra parte, rende la diagnosi lenta e poco precisa. I livelli si completano: vicino al codice si localizzano rapidamente gli errori, mentre le prove più ampie verificano contratti e flussi reali.

La copertura non si riduce alla percentuale di righe eseguite. Occorre coprire regole, classi di input, confini, errori e rischi. Per un servizio di verifica anagrafica servono almeno esito positivo, requisito assente, identificativo non valido, fruitore non autorizzato, dipendenza indisponibile e risposta oltre il tempo previsto. Ogni caso deve dichiarare l’oracolo, cioè la regola con cui si decide se l’esito è corretto.

| Artefatto | Domanda di controllo | Evidenza |
| --- | --- | --- |
| requisito | è chiaro e verificabile? | criterio di accettazione approvato |
| componente | rispetta responsabilità e contratto? | test unitario o di componente |
| integrazione | i sistemi scambiano dati ed errori corretti? | test con dipendenza controllata |
| sistema | il flusso soddisfa il caso d’uso? | esecuzione end-to-end |
| rilascio | le funzioni esistenti restano valide? | suite di regressione ed esiti registrati |

I dati di test devono essere pertinenti e governati. Dati sintetici facilitano casi limite e ripetibilità; dati realistici aiutano a cogliere distribuzioni e formati, ma non autorizzano l’uso indiscriminato di dati personali. Ambiente, configurazione, versione e dipendenze vanno registrati, altrimenti un esito non è riproducibile.

La gestione della configurazione collega test e prodotto. Il difetto va riferito alla versione, all’ambiente e al caso che lo ha mostrato; la correzione modifica un elemento controllato e richiede prove mirate più regressione pertinente. Una release non è soltanto un pacchetto: è un insieme identificabile di codice, configurazioni, schemi, documentazione ed evidenze.

**Costruzione della risposta.** Un caso di test nasce da un criterio preciso. Deve riportare precondizioni e input, il risultato atteso e l’evidenza da conservare. Dire soltanto “testare l’API” non basta: occorre dichiarare operazione, classe di input, risposta attesa e versione del contratto.

I test positivi dimostrano il comportamento previsto con input ammessi; quelli negativi verificano rifiuti ed errori controllati. Servono anche valori limite, sequenze di operazioni e condizioni concorrenti quando pertinenti. Un esito inatteso non va subito classificato come difetto del codice: può rivelare requisito ambiguo, ambiente incoerente, dato errato o test costruito male.

La validazione coinvolge il contesto d’uso. Una funzione può rispettare la specifica e risultare inadatta al procedimento amministrativo perché il requisito iniziale era incompleto. Prototipi, dimostrazioni e prove di accettazione anticipano questo rischio, purché raccolgano osservazioni trasformabili in decisioni e criteri.

| Esito | Prima domanda | Azione |
| --- | --- | --- |
| test fallito | atteso, input e ambiente sono corretti? | riprodurre e classificare |
| test intermittente | esiste dipendenza da tempo, ordine o concorrenza? | isolare la condizione |
| test superato ma utente insoddisfatto | il criterio rappresenta davvero il bisogno? | riesaminare requisito e validazione |
| regressione dopo modifica | quale dipendenza è stata coinvolta? | tracciare impatto e correggere |

**Errore ricorrente.** Accumulare test senza una strategia crea una suite lenta e poco informativa. Ogni prova deve proteggere un requisito, un rischio o un contratto; i duplicati privi di valore aumentano manutenzione e falsi allarmi.

## N-TR01-06-04 · API come contratto

Un’**API** definisce come un sistema può richiedere capacità o dati a un altro. Il contratto comprende operazioni, indirizzamento, parametri, rappresentazioni, precondizioni, risposte, errori e vincoli di utilizzo. L’implementazione interna può cambiare senza rompere i fruitori finché il comportamento promesso resta compatibile.

Un’interazione **sincrona** attende una risposta nel contesto della richiesta. In un’interazione **asincrona**, richiesta ed elaborazione o notifica possono essere separate nel tempo. Eventi e messaggi sono utili quando il produttore non deve attendere il completamento immediato, ma richiedono gestione di duplicati, ordine, errori e correlazione.

### REST, SOAP e rappresentazioni

REST è uno stile architetturale; nelle API HTTP orienta l’uso di risorse, identificatori, rappresentazioni e semantica del protocollo. SOAP è un protocollo di messaggistica basato su XML. Dire «REST usa JSON, SOAP usa XML» è incompleto: JSON è frequente nelle API REST, ma non definisce REST; SOAP possiede regole proprie oltre al formato XML.

In una API HTTP, l’URI identifica la risorsa o il punto di interazione; il metodo esprime la semantica; gli header trasportano metadati; il corpo contiene una rappresentazione quando prevista; il codice di stato descrive la classe di esito; lo schema definisce struttura e vincoli.

`GET` recupera una rappresentazione senza richiedere una modifica dello stato; `POST` invia dati per un’elaborazione; `PUT` sostituisce o crea lo stato della risorsa identificata secondo il contratto; `PATCH` applica una modifica parziale; `DELETE` richiede la rimozione.

L’**idempotenza** riguarda l’effetto intenzionale di più richieste uguali: ripeterle produce lo stesso effetto previsto sul server della singola richiesta. Non significa che ogni risposta debba essere identica né che l’operazione sia priva di effetti interni, come il logging.

### Errori e descrizione formale

La risposta di errore deve permettere al fruitore di capire la classe del problema, correlare l’evento e decidere se correggere la richiesta o riprovarla. Input non valido, risorsa assente, autorizzazione mancante, conflitto e indisponibilità non possono confluire tutti in un generico errore interno.

Una descrizione **OpenAPI** rappresenta in modo indipendente dal linguaggio la superficie di un’API HTTP: percorsi, operazioni, parametri, corpi, risposte, schemi e requisiti di sicurezza descritti. Può alimentare documentazione, test e strumenti, ma non implementa da sola il comportamento e non prova che il servizio rispetti il contratto.

### Dal caso d’uso al contratto osservabile

La progettazione muove dalle capacità richieste dal fruitore. Prima si chiariscono attori, precondizioni e risultato; da questi elementi discendono operazioni e rappresentazioni. Il contratto deve restare comprensibile a chi non conosce tabelle interne, classi o dettagli del codice. Esporre direttamente il modello di persistenza aumenta l’accoppiamento e ostacola l’evoluzione del servizio.

Per ogni operazione vanno precisati:

- scopo e semantica;
- dati obbligatori, opzionali e relativi vincoli;
- esito normale e classi di errore;
- effetti, idempotenza e comportamento in caso di ripetizione;
- autorizzazioni richieste e informazioni restituite;
- versione, limiti e identificativo di correlazione.

Un errore applicativo dovrebbe avere struttura stabile: codice riconoscibile dal programma, messaggio destinato alla diagnosi, riferimento alla richiesta ed eventuali dettagli consentiti. Il codice HTTP offre la classe dell’esito, ma non sostituisce la semantica del dominio. Due condizioni diverse non devono diventare indistinguibili se richiedono azioni diverse del fruitore.

| Condizione | Esito contrattuale | Azione del fruitore |
| --- | --- | --- |
| input non valido | errore di validazione con campo o regola | correggere la richiesta |
| risorsa assente | esito di assenza previsto | chiudere o modificare il flusso |
| conflitto di stato | errore correlato alla versione o allo stato | rileggere e decidere |
| indisponibilità temporanea | errore distinguibile e correlabile | applicare la politica di retry |

Le interazioni asincrone richiedono un contratto anche per consegna, duplicati, ordine e correlazione. Chi pubblica un evento dichiara significato e schema; chi lo consuma deve tollerare l’evoluzione prevista. “Asincrono” non significa privo di risposta: può esistere una conferma di ricezione o un’operazione separata per conoscere lo stato.

**Traccia operativa.** Il disegno essenziale di un’API indica finalità, operazione, input minimo, output, errori, effetti e versione. Solo dopo queste decisioni un esempio di payload diventa davvero utile. OpenAPI consente di formalizzarle, ma la qualità dipende dal contratto e non dallo strumento scelto per descriverlo.

## N-TR01-06-05 · Evoluzione e gestione delle API

Una modifica è **compatibile** quando i fruitori conformi al contratto precedente possono continuare a funzionare. Aggiungere un campo opzionale può essere compatibile se i client ignorano elementi sconosciuti; rinominare un campo obbligatorio o cambiarne il tipo può rompere il contratto.

Il **versionamento** rende distinguibili contratti o comportamenti. La **deprecazione** annuncia che un elemento resta temporaneamente disponibile ma sarà sostituito; richiede documentazione, transizione e percorso di migrazione. Versione dell’API, versione dell’implementazione e versione della specifica OpenAPI sono concetti distinti.

### Requisiti operativi e API management

Un contratto utile specifica limiti di dimensione, paginazione e filtri; timeout e retry; throttling; disponibilità e latenza attese; identificativi di correlazione; metriche, log e canale per modifiche e incidenti.

Uno **SLO** esprime un obiettivo misurabile di servizio; uno **SLA** formalizza impegni e conseguenze nel rapporto fra parti. Il capitolo 12 affronta il profilo contrattuale.

L’API management comprende catalogazione, pubblicazione, controllo degli accessi, politiche di utilizzo, versioni, documentazione, misurazione e dismissione. Un gateway può applicare alcune politiche, ma non sostituisce governance, qualità del contratto o autorizzazione applicativa.

### Progettare l’evoluzione prima della rottura

La compatibilità si giudica dal punto di vista del fruitore. Il server può accettare nuovi input senza imporre modifiche ai client, così come un client può tollerare campi aggiuntivi; altre variazioni, invece, richiedono un aggiornamento coordinato. La compatibilità all’indietro preserva i fruitori del contratto precedente. Quella in avanti riguarda la capacità dei componenti meno recenti di gestire elementi prodotti da versioni nuove, nei limiti consentiti dal contratto.

Una politica di evoluzione definisce quali cambiamenti sono ammessi nella stessa versione, come viene annunciata una deprecazione, per quanto tempo convivono i contratti e quali evidenze autorizzano la dismissione. Il solo numero di versione non protegge i fruitori. Servono inventario degli utilizzatori, telemetria, documentazione, ambiente di prova e un canale per le comunicazioni.

| Modifica | Rischio | Trattamento possibile |
| --- | --- | --- |
| aggiunta di campo opzionale | client rigidi rifiutano elementi ignoti | verificare regole di tolleranza e testare i fruitori |
| rinomina di campo obbligatorio | rottura del parsing o della logica | nuova versione o transizione esplicita |
| nuovo valore di enumerazione | codice client non gestisce il caso | contratto estensibile e comportamento di fallback |
| modifica del significato | risposta formalmente valida ma semanticamente errata | nuovo contratto e migrazione documentata |
| riduzione di un limite | richieste prima valide vengono rifiutate | preavviso, misura dell’uso e adeguamento concordato |

Retry e idempotenza vanno progettati insieme. Un timeout lascia incerto se l’operazione sia stata eseguita; ripetere una creazione non idempotente può produrre duplicati. Il contratto può prevedere una chiave idempotente, un identificativo di richiesta o un’operazione di consultazione dello stato. La scelta dipende dal processo e deve essere verificata con casi di perdita della risposta.

Paginazione e filtri proteggono risorse e rendono prevedibile la fruizione, ma devono avere ordinamento, limiti e semantica stabili. Il throttling controlla il tasso di richieste; non sostituisce il dimensionamento né il trattamento delle priorità. Metriche e identificativi di correlazione consentono di collegare esperienza del fruitore, log del servizio e versione del contratto.

**Criterio di valutazione.** Una proposta di versionamento deve indicare modifica, fruitori coinvolti, rischio di incompatibilità, periodo di transizione, test e criterio di dismissione. Limitarsi a “creare la v2” sposta il problema: senza un piano di migrazione, si rischia di mantenere due contratti senza una scadenza definita.

La deprecazione ha un inizio e una fine verificabili. Si annuncia l’alternativa, si misura l’uso del contratto precedente, si assiste la migrazione e si controllano gli ultimi fruitori. La dismissione avviene quando i criteri concordati sono soddisfatti, non soltanto quando il produttore ritiene vecchia la versione.

L’osservabilità sostiene anche l’evoluzione: tasso di errori per versione, latenze, volumi, retry e operazioni deprecate mostrano l’impatto reale. Le metriche devono evitare dati personali non necessari e restare correlate a versioni e richieste. Senza questa base, una compatibilità presunta può nascondere errori dei fruitori.

## N-TR01-06-06 · Interoperabilità PA ed e-service

L’interoperabilità consente a organizzazioni e sistemi differenti di scambiare informazioni e usarle correttamente. Può essere letta sui livelli **giuridico**, **organizzativo**, **semantico** e **tecnico**.

Una API tecnicamente funzionante non risolve da sola gli altri livelli. Due enti possono scambiare un campo chiamato `stato` ma attribuirgli significati diversi; oppure condividere il significato ma non avere finalità e responsabilità definite.

### ModI, PDND ed e-service

Il Modello di interoperabilità della PA organizza tecnologie, pattern di interazione e sicurezza, profili e regole di governance. Le fonti AgID richiamano API documentate ed evolvibili, catalogazione, tracciabilità, limitazioni d’uso e livelli di servizio.

Nel contesto PDND, un **erogatore** rende disponibile una capacità; un **fruitore** ne richiede l’uso. L’**e-service** descrive il servizio disponibile nel catalogo e collega l’offerta alle API e alle condizioni di fruizione. La **finalità** esplicita lo scopo dell’accesso. Versioni, richieste di fruizione, attributi, accordi e meccanismi tecnici devono essere verificati sulla documentazione vigente prima di configurare un caso reale.

Il principio **once only** orienta a non chiedere nuovamente a cittadini e imprese informazioni già legittimamente disponibili. Non autorizza accessi indiscriminati: finalità, minimizzazione, responsabilità, autorizzazioni e tracciabilità restano requisiti del servizio.

Il Regolamento (UE) 2024/903 inquadra l’interoperabilità del settore pubblico a livello europeo. Per una prova generale conta cogliere la continuità fra dimensione tecnica, organizzativa, semantica e giuridica; obblighi e applicazioni puntuali richiedono verifica normativa aggiornata.

### Caso guidato: verifica di un requisito anagrafico

Un’amministrazione fruitrice deve verificare un requisito anagrafico durante l’istruttoria di una pratica. L’amministrazione erogatrice possiede il dato autorevole.

1. **Finalità:** usare il dato solo per l’istruttoria prevista.
2. **Dato minimo:** ottenere un esito, non l’intero profilo anagrafico.
3. **Requisito funzionale:** inviare l’identificativo previsto e ricevere esito, data e riferimento correlabile.
4. **Requisiti non funzionali:** tracciare la richiesta, rispettare il livello di servizio e classificare gli errori.
5. **Contratto:** definire input, output, errori, schema e versione.
6. **Autorizzazione:** consentire la fruizione secondo ruoli, finalità e condizioni applicabili.
7. **Test:** verificare esito positivo, requisito assente, input non valido, fruitore non abilitato e indisponibilità.
8. **Evidenza:** correlare richiesta, risposta, versione ed esito del test.

Restituire un esito invece dell’intero record riduce dati e accoppiamento. Se il significato dell’esito cambia, contratto, documentazione e test devono evolvere insieme.

### Laboratorio: disegno essenziale di un’API

| Campo | Decisione |
| --- | --- |
| bisogno | quale risultato amministrativo serve? |
| erogatore e fruitore | chi possiede la capacità e chi la usa? |
| finalità | perché lo scambio è necessario? |
| operazione | quale capacità viene richiesta? |
| input minimo | quali dati sono indispensabili? |
| output | quale esito è utile e comprensibile? |
| errori | quali condizioni deve distinguere il fruitore? |
| idempotenza | cosa accade in caso di retry? |
| versione | quali modifiche sarebbero incompatibili? |
| qualità | quali obiettivi e metriche servono? |
| evidenze | come si correlano richieste, test e anomalie? |

Un possibile contratto concettuale è `POST /verifiche-requisito`. La risposta non deve essere inventata a partire dalla tecnologia: va derivata dal bisogno, dallo schema condiviso e dalle condizioni di trattamento.

### Domanda da commissario

**Come passa da un requisito a un e-service interoperabile?**

Inizio dal bisogno e chiarisco stakeholder, finalità e vincoli. Traduco il requisito in criteri di accettazione, poi progetto componenti, contratto API, errori e requisiti di qualità. I test devono fornire evidenza per ogni promessa. Nel caso di un e-service individuo anche erogatore, fruitore, dati minimi, condizioni di fruizione e livelli di servizio; versione, documentazione e osservabilità ne accompagnano l’evoluzione.

### Domanda-trappola

**Un’API pubblicata è automaticamente accessibile a chiunque?**

No. Pubblicare o catalogare una descrizione rende conoscibile il contratto secondo le regole del contesto, ma non elimina autenticazione, autorizzazione, finalità, protezione dei dati o condizioni di fruizione. Interoperabilità e open data non sono sinonimi.

### Errore tipico

Disegnare subito endpoint e payload. La struttura tecnica finisce così per nascondere decisioni su finalità, significato, errori e qualità. Conviene partire dal bisogno e dal contratto osservabile; soltanto dopo si sceglie la rappresentazione.

## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento rende controllabile la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-06-01` | Esercizio 1 — Requisito e test |
| `N-TR01-06-02` | Quiz 3 |
| `N-TR01-06-03` | Quiz 1 |
| `N-TR01-06-04` | Esercizio 2 — Compatibilità |
| `N-TR01-06-05` | Esercizio 2 — Compatibilità |
| `N-TR01-06-06` | Esercizio 3 — Caso e-service |

## ▣ Verifica

### Esercizio 1 — Requisito e test

Trasforma «il servizio deve essere veloce» in un requisito verificabile.

**Soluzione:** definire operazione, carico, indicatore, valore obiettivo e finestra di misurazione. Senza questi elementi, «veloce» non produce un criterio di accettazione.

### Esercizio 2 — Compatibilità

Un campo obbligatorio `esito` viene rinominato `risultato`. La modifica è compatibile?

**Soluzione:** in generale no per i fruitori che cercano `esito`. Occorre mantenere il campo durante una transizione, introdurre una nuova versione o concordare una migrazione verificabile.

### Esercizio 3 — Caso e-service

Elenca cinque elementi da chiarire prima della fruizione.

**Soluzione:** erogatore, fruitore, finalità, dato o capacità minima, condizioni di accesso; vanno inoltre definiti contratto, errori, livelli di servizio ed evidenze.

### Quiz 1

Quale affermazione è corretta?

- A. Validazione e verifica sono sempre sinonimi.
- B. OpenAPI implementa automaticamente il servizio descritto.
- C. Un test di regressione controlla funzioni già valide dopo una modifica.
- D. Interoperabilità significa rendere ogni dato pubblico.

**Risposta corretta: C.** A confonde adeguatezza allo scopo e conformità; B attribuisce alla descrizione il comportamento dell’implementazione; D confonde scambio governato e open data.

### Quiz 2

Quale formulazione è un criterio di accettazione verificabile?

- A. Il servizio deve essere moderno.
- B. Il servizio deve essere facile da usare.
- C. Con input valido, il servizio restituisce esito e identificativo correlabile secondo i casi concordati.
- D. Il gruppo deve adottare un metodo Agile.

**Risposta corretta: C.** Indica una condizione osservabile e un risultato atteso. A e B sono qualità non misurate; D prescrive un metodo senza collegarlo al bisogno o all’esito.

### Quiz 3

Quale affermazione descrive correttamente un trade-off architetturale?

- A. Più servizi riducono sempre la complessità.
- B. Una cache può ridurre la latenza ma introduce problemi di coerenza e invalidazione.
- C. Un monolite non può avere componenti interni.
- D. La tecnologia determina da sola la qualità.

**Risposta corretta: B.** La decisione migliora una proprietà e crea nuovi costi da governare. A, C e D trasformano scelte contestuali in regole assolute.

### Quiz 4

Un test verifica l’interazione fra servizio applicativo e database. A quale livello appartiene?

- A. Unitario.
- B. Integrazione.
- C. Accettazione, necessariamente.
- D. Regressione, necessariamente.

**Risposta corretta: B.** L’oggetto è l’interazione fra elementi. Lo stesso test può entrare in una suite di regressione, ma “regressione” descrive lo scopo della riesecuzione, non sostituisce il livello.

### Quiz 5

Quale modifica presenta il rischio più evidente di rompere i fruitori esistenti?

- A. Correggere un refuso nella documentazione.
- B. Aggiungere un esempio non normativo.
- C. Rinominare un campo obbligatorio della risposta.
- D. Aggiungere una metrica interna non esposta.

**Risposta corretta: C.** I fruitori che cercano il nome precedente non trovano più il dato atteso. Le altre modifiche non cambiano necessariamente il contratto osservabile.

### Quiz 6

Che cosa rende legittima e governabile la fruizione di un e-service?

- A. La sola presenza dell’API nel catalogo.
- B. La disponibilità tecnica dell’endpoint.
- C. Finalità, ruoli, condizioni di fruizione, dati minimi, autorizzazioni ed evidenze coerenti.
- D. L’uso obbligatorio di un formato aperto per qualunque dato.

**Risposta corretta: C.** Catalogazione e raggiungibilità tecnica non bastano. La fruizione deve rispettare il contesto giuridico-organizzativo, semantico e tecnico.

## Checklist finale

| Competenza | Riconosco | Spiego | Applico |
| --- | --- | --- | --- |
| Distinguere bisogno, requisito, vincolo e criterio | ☐ | ☐ | ☐ |
| Collegare requisito, progetto, test ed evidenza | ☐ | ☐ | ☐ |
| Confrontare modelli di ciclo di vita | ☐ | ☐ | ☐ |
| Leggere componenti, interfacce e dipendenze | ☐ | ☐ | ☐ |
| Distinguere verifica, validazione e livelli di test | ☐ | ☐ | ☐ |
| Spiegare configurazione e controllo di versione | ☐ | ☐ | ☐ |
| Progettare il contratto essenziale di un’API | ☐ | ☐ | ☐ |
| Valutare compatibilità, errori e idempotenza | ☐ | ☐ | ☐ |
| Distinguere i livelli di interoperabilità | ☐ | ☐ | ☐ |
| Costruire un caso e-service | ☐ | ☐ | ☐ |

## Da sapere in 5 righe

- Il ciclo di vita collega bisogno, requisiti, progetto, test, rilascio ed evoluzione.
- Architettura e qualità si valutano attraverso trade-off espliciti.
- Un’API è un contratto: operazioni, dati, errori, vincoli e livelli di servizio.
- Interoperabilità tecnica, semantica, organizzativa e giuridica devono convergere.
- Un e-service richiede erogatore, fruitore, finalità, condizioni, evidenze e governo delle modifiche.

## Riferimenti normativi e professionali essenziali

- Codice dell’amministrazione digitale, decreto legislativo 7 marzo 2005, n. 82, per il quadro generale dell’interoperabilità pubblica.
- AgID, *Linee guida sull’interoperabilità tecnica delle Pubbliche Amministrazioni* e relativi allegati.
- AgID, *Linee guida sull’infrastruttura tecnologica della PDND per l’interoperabilità dei sistemi informativi e delle basi di dati*.
- Piano Triennale per l’informatica nella PA 2024-2026, sezione sugli e-service in interoperabilità tramite PDND.
- Regolamento (UE) 2024/903, *Interoperable Europe Act*, per il quadro europeo dell’interoperabilità del settore pubblico.
- IETF, RFC 9110, per la semantica HTTP; OpenAPI Initiative, *OpenAPI Specification*, per la descrizione delle API HTTP.
- IEEE Computer Society, *Guide to the Software Engineering Body of Knowledge*, per requisiti, progettazione, qualità, test e gestione della configurazione.
- *Il Metodo BANDO*, capitolo 10, § 16, per i prerequisiti su API, PDND e interoperabilità richiamati nel confine iniziale.
