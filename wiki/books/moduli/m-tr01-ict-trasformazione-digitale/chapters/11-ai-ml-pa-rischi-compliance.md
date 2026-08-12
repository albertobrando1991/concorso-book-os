---
id: chapter-m-tr01-11
type: book_chapter
title: "AI/ML nella PA: modelli, rischi e compliance"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["intelligenza artificiale", "machine learning", "governance AI", "rischio algoritmico", "AI Act"]
entities: ["Unione europea", "Commissione europea", "AI Office", "AgID", "NIST"]
source_refs: ["sources/ai-ml-governance-rischi-compliance-fonti-primarie", "sources/legge-23-settembre-2025-n-132-intelligenza-artificiale", "sources/basi-dati-sql-nosql-qualita-fonti-tecniche", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie", "sources/data-governance-open-data-interoperabilita-fonti-primarie"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati"]
confidence: 0.88
updated_at: 2026-08-11
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "ai", "machine-learning", "ai-act"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 11
draft_stage: format-2-retrofit
format_version: 2
dati_operativi: []
last_compiled_from: ["sources/ai-ml-governance-rischi-compliance-fonti-primarie", "topics/intelligenza-artificiale-machine-learning-governance-pa", "planning/08-capitolo-11-piano-completamento"]
---

# AI/ML nella PA: modelli, rischi e compliance

Un sistema che assegna una priorità alle segnalazioni può aiutare un comune a mettere prima i casi urgenti. Può anche incorporare dati incompleti, spostare l'attenzione su zone già più segnalate o indurre chi lavora allo sportello a fidarsi di un punteggio senza comprenderne i limiti. Per questo la domanda d'esame non è soltanto «quanto è accurato il modello?», ma «quale decisione supporta, con quali dati, controlli, evidenze e responsabilità?».

## Obiettivo e confini

Al termine del capitolo saprai distinguere algoritmo, sistema di IA, modello e output generativo; leggere dati, metriche, errori e rischi in funzione di un servizio pubblico; progettare un controllo umano reale; descrivere il ciclo di vita del sistema e orientarti nel quadro europeo e italiano senza trasformare una classificazione giuridica in uno slogan. Gli algoritmi generali restano nel capitolo 3; la qualità e il governo del dato nei capitoli 4 e 10; lifecycle software, sicurezza, logging e incidenti nei capitoli 6, 8 e 9; contratti e fornitori nel capitolo 12. Qui questi elementi sono ricomposti intorno al caso d'uso AI.

## Mappa BANDO del sistema AI

- **B — Bisogno:** problema amministrativo, finalità, destinatari e baseline.
- **A — Attori:** responsabile del caso d'uso, tecnici, operatori, controllori e fornitore.
- **N — Nodi:** dati, errori, bias, sicurezza, diritti, drift e uso improprio.
- **D — Documenti:** scheda del caso, dati, versione del modello, test, log e valutazioni.
- **O — Output:** previsione, raccomandazione o contenuto inseriti in un procedimento governato.

## N-TR01-11-01 · Algoritmo, sistema AI, modello e inferenza

Un'**automazione deterministica** applica regole esplicite: se input e regole non cambiano, il risultato resta uguale. Un **algoritmo** è una procedura finita che trasforma input in output. L'intelligenza artificiale non è invece il nome di un singolo programma: nel linguaggio tecnico e nel quadro europeo va letta come un insieme più ampio, composto dal modello quando presente, dai dati, dal software, dalle interfacce, dalle istruzioni, dalle persone e dal processo nel quale l'output viene impiegato.

Nel **machine learning** una parte delle regole viene appresa dai dati. Il modello riceve esempi, modifica parametri interni e tenta di ridurre l'errore rispetto a un obiettivo. Le **feature** sono le caratteristiche usate in ingresso; la **label** è il risultato atteso nei problemi supervisionati. Un parametro è appreso durante l'addestramento; un iperparametro è invece deciso nella configurazione del processo. Distinguere i due termini serve a evitare l'errore di trattare il modello come una scatola autonoma, priva di decisioni umane precedenti.

L'**addestramento** serve a stimare il modello usando esempi; l'**inferenza** applica il modello a nuovi casi. Una prestazione elevata sui dati già visti non dimostra che il sistema funzioni su situazioni nuove, né prova che sia utile nel procedimento amministrativo. Un servizio può classificare correttamente molte pratiche ma essere poco utile se il suo risultato arriva tardi, se gli operatori non possono contestarlo o se la soglia scelta produce troppe priorità improprie.

Un sistema **predittivo** stima una classe o un valore; un raccomandatore ordina opzioni; un sistema **generativo** produce testo, immagini, audio o altro contenuto. Quest'ultimo può formulare un testo plausibile e tuttavia errato: la plausibilità non rende l'output una fonte né trasferisce la responsabilità dell'atto all'applicazione. Nel colloquio è utile dire che l'output AI è un elemento istruttorio o operativo da verificare, non un soggetto che decide.

L'unità di analisi è sempre il caso d'uso: una stessa tecnologia può sostenere una bozza interna a basso impatto o incidere su una scelta che richiede garanzie molto maggiori. Finalità, destinatari, dati, modo d'uso e possibilità di intervento sono quindi più informativi dell'etichetta commerciale del prodotto. **Errore tipico:** chiamare “AI” qualunque automazione e, al contrario, pensare che l'uso di un modello elimini la necessità di definire regole, ruoli e controlli.

### Applicazione al profilo ICT PA

Quando un ufficio valuta un prodotto, la prima scheda non dovrebbe iniziare dal nome commerciale, ma da cinque domande: quale bisogno soddisfa, quale output produce, chi lo usa, quali dati riceve e quale scelta concreta cambia. Se la risposta è “nessuna”, può essere un semplice strumento di ricerca o redazione; se cambia l'ordine delle pratiche, l'accesso a un servizio o l'intensità di un controllo, diventa un caso d'uso da descrivere molto meglio. Questo metodo impedisce due estremi: vietare ogni automazione perché contiene una componente AI, oppure adottarla come se la sua natura tecnica bastasse a renderla affidabile.

Un modello può anche essere aggiornato senza che l'ente se ne accorga, per esempio quando un fornitore sostituisce una versione o modifica un servizio collegato. Perciò la descrizione dell'architettura deve indicare dipendenze, versione e condizioni di impiego. Non serve trasformare il candidato in un programmatore del modello: serve renderlo capace di chiedere evidenze verificabili e di riconoscere che l'inferenza avviene dentro un processo con responsabilità, non in uno spazio neutro. La stessa prudenza vale per la generazione di testo: controllare il contenuto non significa solo correggere un refuso, ma verificare fatti, fonti, destinatario e coerenza con l'atto che si sta preparando.
In pratica, la scheda del caso deve anche indicare ciò che il sistema non fa: usi esclusi, decisioni riservate alla persona e condizioni che obbligano a fermare il flusso. Questa delimitazione protegge utenti e operatori perché trasforma una promessa tecnica vaga in un impiego controllabile. Un output non previsto non va semplicemente accettato o scartato: va ricondotto alla finalità, verificato e, se necessario, registrato come anomalia da riesaminare.
## N-TR01-11-02 · Paradigmi, partizioni e generalizzazione

Nell'**apprendimento supervisionato** gli esempi contengono input e risultato atteso. La classificazione assegna una categoria, per esempio “urgente/non urgente”; la regressione stima un valore numerico, come un tempo atteso di lavorazione. Nell'**apprendimento non supervisionato** non esiste una label-obiettivo e il metodo cerca strutture nei dati, come gruppi con caratteristiche simili. L'apprendimento per rinforzo usa ricompense e penalità per apprendere una strategia: è utile riconoscerne la logica, senza confonderlo con una comune classificazione.

La scelta del paradigma dipende dal problema e dai dati disponibili. Se un ente possiede esempi affidabili di esiti, il supervisionato può essere valutato; se possiede soltanto molte osservazioni non etichettate, un raggruppamento può servire a esplorare fenomeni, non a decidere automaticamente. La domanda corretta è: quale output deve sostenere quale fase del processo, e con quali conseguenze se sbaglia? Un modello non compensa una finalità vaga o etichette prodotte da prassi storiche incoerenti.

Per stimare la capacità di generalizzare, il dataset viene separato. Il blocco di **training** serve ad apprendere; quello di **validation** consente di confrontare configurazioni e soglie; il **test set** misura la prestazione finale su dati non usati nelle decisioni di sviluppo. Se il test è consultato ripetutamente per migliorare il sistema, perde la propria indipendenza e diventa di fatto un altro set di validazione. La separazione può essere temporale quando il servizio cambia nel tempo, oppure deve evitare che pratiche molto simili finiscano contemporaneamente in addestramento e test.

L'**overfitting** si verifica quando il modello aderisce eccessivamente ai dati di training e rende male su casi nuovi. L'**underfitting** indica un modello troppo semplice o una configurazione incapace di cogliere relazioni utili. Il **data leakage** introduce nella previsione informazioni che, al momento reale della decisione, non sarebbero disponibili: usare la data finale di chiusura per prevedere all'apertura un ritardo è un esempio classico. Il leakage può anche derivare da trasformazioni applicate prima della separazione dei dati.

Nella PA la generalizzazione non è soltanto una proprietà statistica. Deve riguardare il periodo, il territorio, le tipologie di domanda e le condizioni operative per le quali il sistema sarà davvero usato. Una procedura modificata, nuovi canali di accesso o una campagna informativa possono cambiare gli input. **Errore tipico:** dichiarare valido un modello perché supera una prova interna senza spiegare come sono stati separati dati, soglie e casi futuri. In sede d'esame, descrivere il processo di validazione vale più che elencare nomi di algoritmi.

### Esempio: ordinare non significa decidere

Immagina che il comune disponga di diecimila segnalazioni storiche. Il team può addestrare un classificatore, ma deve prima chiedersi se l'ordine scelto dagli operatori nel passato sia una label affidabile o il prodotto di carichi, consuetudini e risorse diseguali. Se il sistema propone solo una priorità, l'operatore conserva una fase di valutazione; se invece il punteggio chiude automaticamente una pratica, cambiano rischio, garanzie e controlli richiesti. La stessa differenza vale per un cluster: raggruppare segnalazioni simili può suggerire un'analisi, ma non prova che i gruppi abbiano un significato amministrativo o che sia lecito usarli per trattare le persone in modo diverso.

La verifica deve essere ripetibile. Si annotano data del campione, criteri di inclusione, regole di pulizia, partizioni, modello, metriche e soglia. Se un dato futuro è entrato per errore nel training, non basta correggere una cella: occorre rieseguire la valutazione e aggiornare l'evidenza. Questa disciplina è utile anche nella prova scritta: mostra che il candidato distingue una sperimentazione promettente da un servizio pronto per l'esercizio. L'obiettivo è una decisione proporzionata, non la massimizzazione astratta di una percentuale.
Una separazione corretta richiede inoltre che il team documenti la ragione della scelta: non esiste un unico schema valido per ogni servizio. Se le pratiche appartengono allo stesso evento o alla stessa persona, distribuirle casualmente tra i set può gonfiare artificialmente il risultato. Il controllo metodologico deve perciò essere comprensibile anche a chi governa il processo, non soltanto a chi sviluppa il modello.
## N-TR01-11-03 · Dati, provenienza, etichette e rappresentatività

Il dato per l'AI non è una materia prima neutra. Ogni dataset ha una provenienza, un periodo, una finalità, una popolazione osservata e una serie di trasformazioni. Una scheda minima deve indicare chi ha prodotto i dati, che cosa rappresentano, come sono state create le etichette, quali campi mancano, quali categorie sono poco rappresentate e quali limitazioni impediscono determinati usi. Questa documentazione rende discutibile e migliorabile il sistema; non è un adempimento decorativo.

Le etichette possono riprodurre errori passati. Se “urgenza” coincide con la priorità storicamente attribuita da un ufficio, il modello può imparare abitudini organizzative e non l'urgenza reale. La qualità va quindi letta rispetto allo scopo: accuratezza, completezza, tempestività, coerenza, validità e rappresentatività possono avere pesi diversi. L'assenza di valori mancanti non dimostra che il dataset sia adeguato, soprattutto se i casi rari o i cittadini che usano canali diversi sono quasi assenti.

Lo **sbilanciamento delle classi** è frequente: se solo pochi casi sono realmente urgenti, un modello che li ignora può ottenere comunque un'accuracy elevata. Anche una variabile apparentemente neutra può funzionare da **proxy** di caratteristiche sensibili o di disuguaglianze territoriali. Eliminare il campo più evidente non elimina automaticamente il rischio di disparità: occorre capire quali correlazioni siano rilevanti, testare gli effetti e valutare le conseguenze nel processo.

La raccolta deve essere proporzionata alla finalità e accompagnata da accessi, classificazione, conservazione e sicurezza adeguati. Per inventario, lineage, qualità trasversale e ruoli sul dato si applicano le logiche del capitolo 10; qui conta l'effetto specifico del dato sull'addestramento e sulla decisione. Dati personali, profilazione e decisioni automatizzate richiedono una valutazione nel quadro applicabile e non possono essere risolti con una formula tecnica generica.

Un buon esercizio consiste nel confrontare due campioni: uno ricco di segnalazioni digitali e uno che include anche sportello e telefono. Il primo potrebbe rappresentare meglio chi usa un canale, non l'intera popolazione. La correzione può richiedere nuovi dati, un diverso uso dell'output, un controllo umano più forte o perfino la rinuncia al modello. **Errore tipico:** scambiare il dataset disponibile per il dataset necessario. La disponibilità tecnica non autorizza da sola una raccolta, un riuso o una conclusione automatizzata.

### Applicazione: una scheda dati prima del modello

Per ciascun campo rilevante conviene indicare definizione, fonte, frequenza di aggiornamento, trasformazioni, qualità conosciuta e rischio d'uso. La data di apertura, per esempio, può essere un dato legittimo e utile; un campo raccolto dopo la decisione non lo è per una previsione fatta prima della decisione. Questa semplice tabella aiuta a scoprire leakage, campi duplicati e variabili che sembrano tecniche ma riflettono modalità di accesso al servizio. Aiuta inoltre a distinguere un dato incompleto da un dato deliberatamente non raccolto perché non necessario alla finalità.

L'ente dovrebbe coinvolgere competenze di processo, dati, sicurezza e protezione dei dati prima di trasformare uno storico in addestramento. Non tutti i difetti richiedono la stessa risposta: un errore di battitura può essere corretto; un campione che esclude sistematicamente un canale richiede cautela più profonda; una label priva di significato condiviso può rendere improprio l'intero progetto. Il candidato può esporre questa logica con una formula chiara: “documento il dato, ne verifico l'adeguatezza all'uso, misuro l'effetto dell'errore e definisco chi può correggerlo”.
Le evidenze sui dati devono restare aggiornabili. Quando si aggiunge un nuovo canale, cambia la definizione di una variabile o si corregge un archivio, occorre sapere quali versioni del modello sono state influenzate. Questa catena permette di rispondere a una contestazione con elementi verificabili, anziché con una generica affermazione sulla qualità del sistema.
La qualità è quindi una proprietà della relazione tra dato, finalità e contesto; va riesaminata quando cambia uno di questi elementi, non solo quando un controllo automatico segnala un valore anomalo.
## N-TR01-11-04 · Baseline, metriche e conseguenze degli errori

Prima di misurare un modello occorre fissare una **baseline**: può essere una regola semplice, il procedimento attuale o una prestazione minima. Senza confronto, un valore percentuale isolato non dice se il sistema migliora davvero il servizio. La baseline obbliga a dichiarare che cosa si vuole superare: tempi, coerenza, capacità di individuare i casi urgenti, carico degli operatori o qualità della motivazione.

In una classificazione binaria la matrice di confusione distingue vero positivo, falso positivo, falso negativo e vero negativo. Se il modello tratta come non urgente una segnalazione effettivamente urgente, produce un falso negativo; se porta in cima alla coda una pratica ordinaria, produce un falso positivo. Queste non sono soltanto caselle: rappresentano possibili ritardi, risorse assorbite o controlli aggiuntivi. La valutazione deve chiedere chi sostiene il costo dell'errore e quale misura può ridurlo.

L'**accuracy** indica la quota complessiva di classificazioni corrette. La **precision** dice quanti casi segnalati come positivi lo sono davvero; il **recall** dice quanti casi realmente positivi vengono intercettati; l'**F1** sintetizza precision e recall. Non esiste una metrica migliore in assoluto. Se perdere un'urgenza è molto grave, il recall può diventare decisivo, accettando che aumentino falsi positivi e attività di verifica. La soglia non è quindi un dato puramente matematico: è una scelta di servizio da motivare e riesaminare.

La valutazione non finisce con la media. Occorre osservare periodi, territori, gruppi pertinenti, casi limite e condizioni di uso. La **calibrazione** verifica se le probabilità stimate corrispondono in modo ragionevole alle frequenze osservate; la robustezza riguarda la tenuta a variazioni degli input e del contesto. Un modello può essere accurato e mal calibrato, o buono in media ma debole proprio nella situazione più delicata.

Per una prova concorsuale, una risposta solida collega metrica, errore e decisione: «Nel caso delle segnalazioni urgenti misuro recall e precision, confronto la baseline manuale, analizzo sottogruppi e scelgo una soglia con operatori capaci di verificare i casi». **Errore tipico:** presentare l'accuracy come certificato di qualità, equità e conformità. Le metriche descrivono aspetti diversi; nessuna sostituisce l'analisi del servizio e dei suoi destinatari.

### Lettura ragionata delle metriche

Supponi che cento segnalazioni siano urgenti e il modello ne riconosca novanta: il recall è 90%. Per capire se questa è una buona prestazione servono però anche quanti casi ordinari siano stati dichiarati urgenti, quale era la baseline e quante verifiche aggiuntive l'ufficio può assorbire. Una soglia più bassa può aumentare il recall ma generare una lista troppo lunga; una soglia più alta può ridurre i falsi positivi ma lasciare fuori urgenze reali. La scelta non è un difetto del modello: è una responsabilità organizzativa che deve essere visibile e riesaminabile.

Anche una metrica ben scelta deve essere calcolata su dati coerenti con l'uso futuro. Se il test riguarda un inverno con molte emergenze e il rilascio avviene in un periodo ordinario, la prestazione può essere difficile da interpretare. Per questo report e confronto con la baseline devono indicare condizioni, limiti e intervalli di osservazione. Un buon candidato non promette precisione assoluta: propone un rilascio controllato, un monitoraggio iniziale e criteri per sospendere la raccomandazione se gli errori superano la capacità di controllo umano.
È utile distinguere la metrica scelta per il rilascio da quella usata per sorvegliare il servizio. Una prestazione accettabile al test può deteriorarsi nel tempo; per questo si definiscono frequenza di controllo, soglia di attenzione, responsabile della lettura e azione conseguente. Senza queste decisioni il numero resta una fotografia, non uno strumento di governo.
La scelta deve essere annotata con il motivo, il responsabile e il criterio di revisione: così l'ente può verificare se il compromesso tra urgenze intercettate e carico operativo sia ancora proporzionato.
## N-TR01-11-05 · Bias, fairness, spiegabilità e controllo umano

Il **bias** può nascere nel campionamento, nelle etichette, nelle feature, nell'obiettivo ottimizzato o nel modo in cui il risultato entra nel lavoro quotidiano. Una disparità osservata non prova da sola una discriminazione illecita, ma è un segnale che impone analisi tecnica, organizzativa e giuridica. Il punto di partenza non è scegliere una formula di fairness, ma capire quale effetto il servizio può produrre su persone e gruppi, con quale meccanismo e quali possibilità di correzione.

Le metriche di **fairness** sono strumenti contestuali. Alcune misurano differenze tra gruppi, altre parità di errore o di trattamento; possono entrare in tensione tra loro. Non esiste un numero universale che certifichi l'equità. Un candidato deve quindi spiegare che una metrica è utile per individuare un problema e confrontare alternative, non per sostituire valutazione del caso, regole di servizio e tutela delle persone.

L'**interpretabilità globale** aiuta a capire il comportamento generale del modello; una spiegazione locale riguarda un singolo output. La trasparenza comprende anche finalità, dati usati, limiti, ruolo del sistema e possibilità di riesame. Una spiegazione post-hoc può essere utile per l'operatore, ma non dimostra che il risultato sia corretto né rende automaticamente motivata una decisione amministrativa. **Errore tipico:** confondere una frase convincente prodotta da un sistema con una spiegazione verificata.

Il controllo umano deve essere sostanziale. Human-in-the-loop, human-on-the-loop e human-in-command descrivono modelli di presenza umana, ma da soli non garantiscono nulla. La persona deve comprendere scopo e limiti, ricevere informazioni utili, disporre di tempo e competenza, poter discostarsi dall'output, sospendere il flusso o attivare un'escalation. Deve inoltre essere possibile tracciare quando l'output è stato seguito o corretto e perché.

L'**automation bias** spinge a privilegiare la raccomandazione automatica anche quando vi sono segnali contrari. Un pulsante “approva” non crea supervisione se chi lo usa non ha dati, autorità o tempo per dissentire. Nel caso delle segnalazioni, l'operatore deve poter cambiare priorità, vedere gli elementi rilevanti e segnalare pattern anomali. Il controllo umano collega qualità tecnica e responsabilità amministrativa: non è un passaggio formale messo alla fine del processo.

### Dal punteggio alla decisione motivata

L'equità non coincide con trattare ogni caso come identico. Un servizio può dover riconoscere differenze reali, ma deve dimostrare che siano pertinenti alla finalità e che non producano un danno ingiustificato. Per questo una verifica sui sottogruppi non è una sentenza automatica: è un modo per scoprire dove chiedere spiegazioni, controllare dati e modificare il processo. La trasparenza rivolta al cittadino e la spiegazione disponibile all'operatore possono avere forma e dettaglio diversi; entrambe devono essere comprensibili e proporzionate al ruolo.

Un override ben progettato richiede un motivo selezionabile, uno spazio breve per la motivazione e una revisione periodica dei casi in cui l'operatore si discosta dal sistema. Se tutti confermano il modello, l'ente deve chiedersi se l'output sia davvero affidabile o se il flusso impedisca di dissentire. Se tutti lo correggono, può essere il modello a non essere adatto. Il log degli override non serve a sorvegliare chi lavora, ma a rendere osservabile il rapporto tra raccomandazione, competenza umana e risultato del servizio.
Il riesame non deve attendere un danno conclamato. Reclami ripetuti, differenze inattese negli override, difficoltà di comprensione o cambiamenti negli utenti sono segnali da analizzare. Il controllo umano diventa così una fonte di apprendimento organizzativo: rende visibili limiti del modello e limiti della procedura, senza trasformare l'operatore in un semplice esecutore della raccomandazione.
Anche la formazione degli operatori è un controllo: chi non sa leggere limiti e incertezze non può svolgere una supervisione sostanziale, per quanto il flusso preveda formalmente un intervento umano.
Una supervisione reale rende quindi discutibile ogni output e conserva una via praticabile per correggere l'errore prima che produca effetti non rimediabili.
## N-TR01-11-06 · Lifecycle, MLOps, rischio e governance

Un sistema AI va governato lungo il suo ciclo di vita: definizione del problema, raccolta e preparazione dei dati, sviluppo, validazione, rilascio, uso, monitoraggio, modifica e dismissione. **MLOps** porta in questo ciclo pratiche di ingegneria e operations: versionamento di dati, codice, configurazioni e modello; ambienti controllati; approvazioni; test ripetibili; osservazione del comportamento in esercizio. Il risultato deve essere ricostruibile: non basta sapere che “il modello è stato aggiornato”.

Il monitoraggio comprende qualità degli input, prestazioni, errori, sottogruppi, override umani, reclami, incidenti e usi fuori perimetro. Il **data drift** è un cambiamento nella distribuzione degli input; il **concept drift** riguarda un mutamento della relazione tra input e risultato. Una nuova procedura amministrativa può modificare entrambi. Anche senza drift, l'efficacia può peggiorare perché cambia l'organizzazione o perché il sistema viene usato per una finalità diversa da quella testata.

Quando emerge un problema, le opzioni non sono soltanto “tenere” o “spegnere” il sistema. Si possono correggere dati e regole, rieseguire i test, cambiare soglia, riaddestrare, limitare l'uso, passare a controllo manuale, eseguire un rollback o dismettere. La scelta richiede evidenze e un responsabile; il rollback non è una formula magica, perché la versione precedente deve essere ancora nota, sicura e adatta al contesto.

La governance parte da un inventario dei casi d'uso, anche quando il modello è acquistato. Per ogni caso occorrono finalità, dati, versione, destinatari, owner, operatori, fornitore, rischi, controlli e evidenze. La valutazione considera effetti su persone, diritti, servizio, finanze, sicurezza e reputazione. Per ogni scenario si descrivono causa, evento, conseguenza, probabilità, gravità, controlli e rischio residuo. Il rischio tecnico e la classificazione giuridica sono collegati ma non coincidono.

Un contratto non trasferisce automaticamente tutte le responsabilità dell'ente. Versioni, prestazioni, dati, audit, subfornitori, incidenti, restituzione delle evidenze, portabilità e uscita devono essere governati insieme a chi acquista e a chi esercisce il servizio. Il capitolo 12 sviluppa gli strumenti di procurement; qui l'errore da evitare è acquistare un sistema come se fosse un risultato già validato. **Errore tipico:** trattare monitoraggio e revisione come attività successive al rilascio, quando devono essere progettati fin dall'inizio.

### Griglia operativa di rischio

Una griglia sintetica può riportare, per ogni rischio, causa, evento, conseguenza, evidenza, controllo e responsabile. Per esempio: etichette storiche incoerenti possono produrre una priorità distorta; il controllo è la revisione delle etichette e il test per gruppi pertinenti; il responsabile è il titolare del caso insieme a chi cura i dati. Questa scrittura costringe a collegare una preoccupazione generica a una scelta osservabile. Lo stesso vale per la dipendenza dal fornitore: non basta annotare “vendor risk”, ma occorre indicare versione, accesso alle evidenze, gestione delle modifiche e condizioni di uscita.

Governare significa anche decidere quando non usare l'AI. Se il bisogno può essere risolto con una regola trasparente o se non esistono dati adeguati, una soluzione più semplice può essere preferibile. La proporzionalità riguarda costi, impatti, competenze e reversibilità. Nel tempo, un sistema inizialmente adeguato può non esserlo più: una nuova fonte dati, una modifica contrattuale o un reclamo ricorrente sono segnali che attivano riesame. La documentazione di queste decisioni rende possibile spiegare perché il sistema è stato limitato, corretto o sospeso.
La governance efficace separa chi propone una modifica, chi la valuta e chi autorizza il rilascio, secondo dimensioni e rischi del servizio. Non occorre creare una burocrazia uniforme: occorre rendere chiaro chi decide, su quale evidenza e con quale possibilità di revisione. Anche un piccolo pilota deve avere criteri di successo e di uscita, altrimenti la sperimentazione tende a diventare esercizio permanente senza controllo.
La revisione periodica deve includere anche i destinatari del servizio e chi raccoglie reclami, perché le criticità d'uso possono emergere fuori dai soli indicatori tecnici.
### Laboratorio compilabile: griglia di rischio del caso AI

Usa questa scheda per il caso delle segnalazioni o per un altro sistema AI descritto nel bando. Compila una riga per ogni rischio rilevante; se non riesci a indicare evidenza, controllo e responsabile, il rischio non è ancora governato. La griglia non assegna automaticamente una classe giuridica: serve a rendere verificabili le decisioni tecniche e organizzative.

| Campo | Compilazione |
| --- | --- |
| Scenario e causa | ________________________________________________ |
| Evento temuto | ________________________________________________ |
| Conseguenza per persone o servizio | ________________________________________________ |
| Evidenza da raccogliere | ________________________________________________ |
| Controllo o misura di trattamento | ________________________________________________ |
| Responsabile del controllo | ________________________________________________ |
| Rischio residuo e criterio di riesame | ________________________________________________ |

Esempio di lettura: etichette storiche incoerenti possono portare a una priorità distorta; la conseguenza è il ritardo di casi urgenti; l'evidenza comprende il campione etichettato e i risultati per gruppi pertinenti; il controllo combina riesame delle etichette, test e override; il responsabile coordina processo e dati; il rischio residuo va riesaminato quando cambiano dati, soglia o procedura.
## N-TR01-11-07 · Quadro UE e italiano: ruoli, rischio e confini

Il regolamento (UE) 2024/1689, noto come AI Act, adotta un approccio basato sul rischio. Il quadro distingue, tra l'altro, pratiche vietate, sistemi ad alto rischio, obblighi di trasparenza e modelli di IA per finalità generali. La classificazione non deriva dal fatto che un prodotto “usa AI”: richiede di verificare definizioni, uso previsto, contesto e ruolo dell'organizzazione nella catena del valore.

Per i sistemi ad alto rischio il regolamento tratta gestione del rischio, governance dei dati, documentazione, registrazione, informazioni verso il deployer, sorveglianza umana, accuratezza, robustezza e cybersicurezza. Provider e deployer svolgono funzioni diverse; anche gli obblighi di trasparenza dipendono dal tipo di sistema e dal suo impiego. In una risposta orale prudente non si assegna una classe normativa al caso di studio senza esaminare il testo vigente e le circostanze concrete.

L'alfabetizzazione in materia di IA riguarda le organizzazioni che forniscono o utilizzano sistemi nel campo previsto. Non significa un corso generico uguale per tutti: competenze, istruzioni operative e capacità di riconoscere limiti devono essere proporzionate a chi progetta, usa, controlla o decide. Per un operatore può essere essenziale comprendere soglia, errore e override; per chi governa il caso servono anche evidenze, rischi, ruoli e condizioni di sospensione.

La legge italiana 23 settembre 2025, n. 132 contiene principi e deleghe in materia di intelligenza artificiale e va letta in raccordo con il regolamento europeo. Strategia italiana, documenti AgID e framework NIST possono orientare organizzazione e metodo, ma non sono intercambiabili: una strategia o un framework volontario non crea da solo un obbligo giuridico. Privacy, procedimento, trasparenza e cybersicurezza continuano ad applicarsi secondo i rispettivi presupposti.

Il calendario dell'AI Act è progressivo e soggetto a verifiche sul testo consolidato e sugli atti applicabili. In questo capitolo non si fissano scadenze operative: prima di un atto, di una gara o della pubblicazione occorre controllare la fonte ufficiale aggiornata. Il NIST AI RMF, organizzato nelle funzioni Govern, Map, Measure e Manage, offre un linguaggio utile per gestire il rischio lungo il ciclo di vita, ma resta un riferimento tecnico volontario.

**Errore tipico:** concludere che un sistema “non è ad alto rischio” e quindi sia privo di responsabilità organizzative, contrattuali o di controllo. Il caso va sempre documentato, valutato e governato; la compliance non sostituisce la qualità tecnica, così come una buona metrica non sostituisce la verifica giuridica.

### Metodo prudente per i riferimenti mobili

Nel caso concreto occorre identificare anzitutto se l'ente agisce come provider, deployer o in altro ruolo rilevante, quindi confrontare finalità e funzionalità con il testo vigente. Un elenco di categorie non sostituisce questa analisi, perché la stessa applicazione può essere usata in contesti diversi. La distinzione tra rischio tecnico e qualificazione giuridica resta essenziale: una matrice probabilità-impatto aiuta a gestire un servizio, ma non assegna da sola lo statuto regolatorio del sistema.

Questo approccio evita anche di trasformare le fonti tecniche in prescrizioni legali. Un framework può suggerire di mappare, misurare e gestire i rischi; l'ente deve poi individuare norme, atti, ruoli e procedure applicabili. Prima di una scelta con effetti esterni, chi cura il progetto verifica testo consolidato, atti applicativi e indicazioni ufficiali aggiornate. La regola concorsuale da ricordare è semplice: nominare il quadro UE e quello nazionale, distinguere i ruoli, descrivere evidenze e controlli, e dichiarare che classificazione e calendario dipendono dal caso e dalla fonte vigente.
Nel lessico della PA conviene infine evitare formule assolute come “conforme per sempre” o “classificato una volta per tutte”. Una modifica della finalità, dei dati, del modello o del fornitore può cambiare le valutazioni. La documentazione consente di riaprire l'analisi senza perdere la storia delle versioni e delle decisioni, mantenendo coerenti qualità del servizio, diritti e responsabilità.
## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento rende controllabile la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-11-01` | Quiz 1 — Qual è la differenza più utile tra sistema AI e modello? |
| `N-TR01-11-02` | Quiz 2 — Perché il test set non va usato ripetutamente per regolare il modello? |
| `N-TR01-11-03` | Caso ragionato — Priorità alle segnalazioni di manutenzione |
| `N-TR01-11-04` | Quiz 3 — Un'accuracy elevata prova che il sistema intercetta bene le urgenze? |
| `N-TR01-11-05` | Quiz 5 — Quando il controllo umano è effettivo? |
| `N-TR01-11-06` | Laboratorio compilabile: griglia di rischio del caso AI |
| `N-TR01-11-07` | Caso ragionato — Priorità alle segnalazioni di manutenzione |

## ▣ Verifica

### Quiz 1 — Qual è la differenza più utile tra sistema AI e modello?

**Risposta corretta:** il modello è una componente che elabora input; il sistema comprende anche dati, software, persone, istruzioni e processo d'uso. La distinzione evita di attribuire al solo modello decisioni che dipendono dall'organizzazione.

### Quiz 2 — Perché il test set non va usato ripetutamente per regolare il modello?

**Risposta corretta:** perché perderebbe indipendenza e diventerebbe un set di validation. Il test deve stimare la prestazione su dati non usati nelle scelte di sviluppo.

### Quiz 3 — Un'accuracy elevata prova che il sistema intercetta bene le urgenze?

**Risposta corretta:** no. Con classi sbilanciate può restare elevata anche se molti casi urgenti non sono riconosciuti. Occorre osservare almeno recall, precision e costo dei falsi negativi.

### Quiz 4 — Eliminare un campo sensibile elimina ogni rischio di bias?

**Risposta corretta:** no. Altre variabili possono agire da proxy; inoltre il problema può dipendere da etichette, campionamento o uso dell'output.

### Quiz 5 — Quando il controllo umano è effettivo?

**Risposta corretta:** quando la persona comprende limiti e finalità, ha informazioni, tempo, competenza e potere di override o escalation, e la decisione è tracciabile.

### Quiz 6 — Il NIST AI RMF è una norma europea obbligatoria?

**Risposta corretta:** no. È un riferimento tecnico volontario utile per organizzare il rischio; non sostituisce il regolamento europeo o le verifiche sul caso concreto.

### Caso ragionato — Priorità alle segnalazioni di manutenzione

Un comune vuole ordinare le segnalazioni su strade ed edifici. La baseline è la coda manuale; i dati includono storico, esiti e tempi. Prima di adottare il sistema, il gruppo definisce “urgenza”, controlla la provenienza delle etichette, separa dati di training, validation e test e osserva recall degli urgenti, precision e risultati per territorio. Gli operatori vedono il punteggio come supporto, possono modificarlo e motivano gli override. Ogni versione di dati e modello, ogni soglia e ogni anomalia sono tracciati.

La decisione ragionata non consiste nel dichiarare subito una classe AI Act. Consiste nel documentare finalità, persone interessate, errori possibili, controlli, ruoli e quadro applicabile; se le prestazioni peggiorano o cambia il processo, il comune rivalida, limita l'uso o torna alla procedura manuale. La griglia di rischio deve collegare dati, modello, impatto, controllo umano, evidenze e responsabile.

### Microcaso — Bozza generativa per il cittadino

Un ufficio usa un modello generativo per preparare una bozza. L'operatore non inserisce dati non autorizzati, verifica fatti e fonti, corregge il testo e approva l'invio secondo il processo previsto. L'output plausibile non viene trattato come atto o fonte: la responsabilità resta nella validazione umana, nelle istruzioni di uso, negli accessi e nella tracciabilità.

## Domanda da commissario

**Come governeresti un modello usato per dare priorità alle segnalazioni comunali?**

Partirei da finalità e baseline, documenterei dati ed etichette, separerei training, validation e test, sceglierei metriche in base al costo degli errori e verificherei sottogruppi. Progetterei controllo umano, versioni, logging e monitoraggio; valuterei rischi, ruoli, fornitore e quadro applicabile sul caso concreto. Prevederei infine condizioni di riesame, rollback e sospensione.

## Domande-trappola

- Accuracy elevata significa equità? No: può nascondere errori concentrati.
- Una spiegazione convincente prova che l'output sia corretto? No.
- Il controllo umano coincide con un clic di approvazione? No.
- Il fornitore assorbe tutte le responsabilità? No: ruoli e contratto vanno verificati.

## Mini-esercizio

Compila per un caso AI cinque campi: finalità, baseline, dati e loro limite, errore più grave, potere di override. Se non riesci a indicare un'evidenza o un responsabile per ciascun campo, il sistema non è ancora pronto per l'uso.

## Da sapere in 5 righe

Il modello è solo una parte del sistema AI. Dati, metriche e soglie vanno letti in relazione agli effetti sugli utenti. Accuratezza, fairness, spiegabilità e conformità non sono sinonimi. Il controllo umano richiede competenza e autorità. Rischio, versioni, monitoraggio e quadro applicabile accompagnano l'intero ciclo di vita.

## Riferimenti essenziali

Regolamento (UE) 2024/1689; legge 23 settembre 2025, n. 132; materiali istituzionali della Commissione europea e di AgID sull'intelligenza artificiale; NIST AI Risk Management Framework. Per atti modificativi, linee guida definitive e calendario applicabile verificare sempre il testo ufficiale vigente.