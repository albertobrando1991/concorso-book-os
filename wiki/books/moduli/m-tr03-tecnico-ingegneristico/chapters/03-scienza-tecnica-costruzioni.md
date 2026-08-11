---
id: chapter-m-tr03-03-scienza-tecnica-costruzioni
type: book_chapter
title: "Scienza e tecnica delle costruzioni per concorsi"
status: draft
domain: "ingegneria strutturale"
topics: ["scienza delle costruzioni", "statica", "meccanica dei solidi", "resistenza dei materiali"]
entities: ["Sapienza Università di Roma", "Università di Napoli Federico II", "Politecnico di Milano", "Università di Bologna"]
source_refs: ["sources/scienza-tecnica-costruzioni-fonti-universitarie", "sources/campione-bandi-tecnici-pa-vol-10-2026", "sources/modulo-m-tr03-tecnico-ingegneristico-vol-10"]
book_refs: ["m-tr03-tecnico-ingegneristico", "vol-10-tecnico-ingegneristico-territorio-lavori-pubblici"]
confidence: 0.76
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: false
canonical: true
tags: ["book-chapter", "m-tr03", "vol-10", "structural-mechanics"]
book_id: m-tr03-tecnico-ingegneristico
outline_section: 3
draft_stage: specialist-audited
module_code: M-TR03
module_family: trasversali
format_version: 2
dati_operativi: false
last_compiled_from: ["wiki/books/moduli/m-tr03-tecnico-ingegneristico/planning/08-capitolo-03-piano-completamento.md", "wiki/books/moduli/m-tr03-tecnico-ingegneristico/planning/02-matrice-copertura-didattica.md", "wiki/sources/scienza-tecnica-costruzioni-fonti-universitarie.md", "wiki/topics/scienza-tecnica-costruzioni.md"]
---

# Scienza e tecnica delle costruzioni per concorsi

Davanti a uno schema strutturale viene spontaneo cercare subito una formula. Conviene fermarsi un momento e chiarire il problema: qual è il sistema resistente? Come è vincolato? Quali azioni riceve? Quale comportamento sto assumendo? Che cosa devo determinare o verificare?

La scienza delle costruzioni fornisce i modelli con cui descrivere equilibrio, spostamenti, deformazioni, sollecitazioni e tensioni. La tecnica delle costruzioni usa questi strumenti per progettare e verificare opere ed elementi reali, nel quadro delle regole applicabili. Nei concorsi le due prospettive spesso convivono: occorre comprendere il principio e saperlo collegare alla decisione tecnica.

Questo capitolo costruisce il lessico e il ragionamento di base. Le prescrizioni delle Norme Tecniche per le Costruzioni, la sismica e la geotecnica sono trattate nel capitolo 4.

## Obiettivo

Al termine del capitolo saprai:

- passare da una struttura reale a uno schema ragionato;
- distinguere cinematica, statica e risposta del materiale;
- riconoscere azioni, vincoli, reazioni e sollecitazioni;
- spiegare il significato di tensione e deformazione;
- distinguere resistenza, rigidezza, stabilità, duttilità e durabilità;
- impostare una risposta orale senza nasconderti dietro formule isolate.

L’output è una checklist `ipotesi–modello–azione–risposta–verifica`, utilizzabile nei quiz, negli orali e nei casi qualitativi.

## N-TR03-03-01 · Dalla struttura reale al modello

### La Mappa BANDO del problema strutturale

| Passaggio | Domanda | Risultato |
| --- | --- | --- |
| **B — Bando** | Il programma richiede statica, scienza o tecnica delle costruzioni? | profondità e tipo di prova |
| **A — Aree** | Il quesito riguarda modello, azioni, materiale o verifica? | perimetro del problema |
| **N — Nuclei** | Quali grandezze e distinzioni devo usare? | schema del ragionamento |
| **D — Diario** | Ho sbagliato ipotesi, vincoli, segni o significato fisico? | errore classificato |
| **O — Output** | Devo riconoscere, calcolare, tracciare o spiegare? | forma della risposta |

La stessa materia cambia volto nella prova. Un quiz può chiedere una distinzione; uno scritto può richiedere uno schema di calcolo; l’orale può valutare la capacità di spiegare perché un modello è adatto.

### Struttura reale e modello

Una struttura reale ha geometria, materiali, collegamenti, difetti, storia costruttiva e condizioni d’uso. Il modello ne rappresenta gli aspetti rilevanti per il problema studiato. Non è una copia ridotta dell’opera: è una scelta tecnica.

Per costruirlo servono almeno:

- geometria e dimensioni significative;
- elementi resistenti;
- vincoli e collegamenti;
- azioni esterne;
- proprietà dei materiali;
- ipotesi sul comportamento;
- grandezze da determinare.

Un impalcato può essere rappresentato mediante travi, piastre o modelli più complessi. La scelta dipende dallo scopo, dai dati disponibili e dalla precisione necessaria. Aggiungere dettagli non migliora di per sé il modello: ciò che conta è la coerenza con il problema e la possibilità di controllarlo.

### Schema statico e struttura reale

Lo schema statico descrive elementi, vincoli e azioni in una forma adatta all’analisi. La struttura reale comprende dettagli e fenomeni che lo schema può idealizzare.

Nella risposta vanno dichiarate le ipotesi essenziali. Assumere piccoli spostamenti, comportamento elastico lineare o collegamenti ideali significa delimitare la validità del risultato.

### Vincoli e gradi di libertà

I gradi di libertà descrivono i movimenti possibili del sistema. I vincoli ne impediscono alcuni e generano reazioni. Un vincolo va letto per l’effetto cinematico che produce, non memorizzato soltanto come simbolo grafico.

Un sistema è labile se conserva movimenti incompatibili con la funzione resistente prevista. È isostatico quando equilibrio e vincoli consentono di determinare le reazioni con le sole equazioni statiche. È iperstatico quando servono anche compatibilità delle deformazioni e legami costitutivi.

### Scopo, scala e qualità del modello

Un modello è adeguato rispetto a una domanda, non in assoluto. Per stimare il percorso delle azioni può bastare uno schema essenziale; per studiare un dettaglio locale occorre rappresentare fenomeni che lo schema globale trascura. Prima di scegliere il livello di complessità, chiarisci quindi quale grandezza cerchi e quale decisione dovrà sostenere.

La scala influenza ciò che viene descritto. A scala dell'opera interessano sistema resistente, collegamenti e vincoli esterni. A scala dell'elemento diventano centrali sezione, lunghezza, continuità e condizioni alle estremità. A scala del materiale si osservano tensioni, deformazioni e legame costitutivo. Passare da una scala all'altra senza dichiararlo produce risposte incoerenti.

Le ipotesi trasformano la realtà in un problema trattabile. Idealizzare un collegamento come cerniera o incastro, assumere piccoli spostamenti oppure comportamento elastico significa scegliere quali fenomeni rappresentare. L'ipotesi va dichiarata e controllata: se il risultato dipende proprio dal fenomeno escluso, il modello non è adatto.

La qualità non coincide con il numero di dettagli. Un modello molto complesso può usare dati incerti e nascondere gli errori; uno semplice può mostrare bene il comportamento dominante. Sono decisivi coerenza, tracciabilità delle ipotesi e possibilità di confrontare l'esito con l'ordine di grandezza atteso.

| Scelta | Domanda di controllo | Rischio |
| --- | --- | --- |
| sistema resistente | quali elementi portano le azioni? | trascurare un percorso essenziale |
| vincoli | quali movimenti sono impediti? | creare reazioni inesistenti |
| proprietà | quali dati servono alla risposta? | usare valori non pertinenti |
| ipotesi | entro quali limiti vale il modello? | estendere il risultato oltre il campo |
| output | che cosa devo determinare? | calcolare grandezze inutili |

### Quiz 1

Quale affermazione descrive meglio un modello strutturale? A) copia completa dell'opera; B) rappresentazione degli aspetti rilevanti per uno scopo; C) disegno privo di ipotesi; D) risultato della verifica normativa.

**Risposta corretta:** B. Il modello seleziona geometria, vincoli, azioni e comportamento necessari alla domanda. Non coincide con l'opera né con l'esito della verifica, e le sue ipotesi devono essere dichiarate.

## ▣ Verifica 1

Scegli una struttura semplice e indica scopo dell'analisi, elementi resistenti, vincoli, azioni, proprietà necessarie e ipotesi. Spiega anche quale dettaglio hai escluso e perché non è decisivo per la domanda considerata.

## N-TR03-03-02 · Vincoli, azioni, reazioni ed equilibrio

Le azioni esterne comprendono forze, momenti e altri effetti che sollecitano il sistema. Possono derivare dal peso, dall’uso, dall’ambiente, da deformazioni imposte o da altri fenomeni. Il capitolo 4 tratterà la loro classificazione normativa.

Le reazioni sono le azioni esercitate dai vincoli sul sistema. Per determinarle occorre isolare correttamente il corpo o la parte di struttura e rappresentare tutte le azioni pertinenti.

L’equilibrio richiede che risultante delle forze e risultante dei momenti rispettino le condizioni statiche del modello. È una condizione necessaria, ma non sempre sufficiente per descrivere la risposta. Un sistema può essere in equilibrio e avere deformazioni eccessive; può soddisfare le equazioni statiche ma risultare instabile.

### Il diagramma di corpo libero

Il diagramma di corpo libero separa il sistema dall’ambiente e sostituisce i vincoli con le reazioni corrispondenti. È uno strumento di ragionamento: obbliga a dichiarare che cosa stai studiando e quali azioni gli attribuisci.

Gli errori più comuni sono tre:

- dimenticare un’azione o una reazione;
- rappresentare un vincolo con reazioni incompatibili;
- applicare l’equilibrio a un sistema isolato male.

### Cinematica prima della statica

Prima di scrivere le equazioni, verifica quali movimenti il sistema potrebbe compiere. Nel piano un corpo rigido può traslare e ruotare; i vincoli eliminano alcuni di questi gradi di libertà. La rappresentazione grafica deve tradurre l'effetto cinematico, non una figura imparata a memoria.

Un vincolo insufficiente lascia un meccanismo e rende il sistema labile rispetto alla funzione considerata. Vincoli ridondanti possono invece rendere il sistema iperstatico: l'equilibrio da solo non determina tutte le reazioni e servono compatibilità e comportamento deformativo. Il conteggio è un primo controllo, ma non sostituisce l'esame geometrico; vincoli disposti male possono non impedire un movimento anche quando sembrano numericamente sufficienti.

Le azioni vanno applicate al sistema isolato. Possono essere concentrate, distribuite o rappresentare effetti imposti, secondo il modello. Le reazioni compaiono quando l'ambiente viene sostituito con le azioni che esercita sul corpo. Confondere carico e reazione significa perdere la relazione fra sistema e vincolo.

### Equilibrio e plausibilità

Le condizioni di equilibrio esprimono l'annullamento delle risultanti di forze e momenti per il sistema considerato. La scelta del polo per i momenti non cambia la fisica, ma può rendere più leggibile il calcolo. Ogni equazione deve riferirsi allo stesso corpo libero e alla stessa convenzione dei segni.

Dopo aver trovato una reazione, controlla direzione e ordine di grandezza. Un segno opposto all'ipotesi iniziale non è automaticamente un errore: può indicare che la reazione reale agisce nel verso contrario. È invece sospetto un risultato incompatibile con simmetria, dimensioni o percorso intuitivo dei carichi.

L'equilibrio non garantisce adeguatezza. Non informa da solo su deformazioni, tensioni o stabilità. Serve a costruire la risposta statica globale; altri passaggi collegano questa risposta a materiale, geometria e prestazioni richieste.

### Quiz 2

Un sistema soddisfa le equazioni di equilibrio. Si può concludere che sia adeguato? A) sì, sempre; B) no, vanno considerate anche cinematica e altre prestazioni; C) sì, se i carichi sono verticali; D) no, perché l'equilibrio non serve.

**Risposta corretta:** B. L'equilibrio è necessario ma non esclude labilità, deformazioni eccessive, crisi del materiale o instabilità. Rimane comunque un passaggio essenziale dell'analisi.

Un controllo ulteriore consiste nell'isolare porzioni diverse dello stesso sistema. Le azioni interne fra le parti devono comparire con versi opposti e mantenere l'equilibrio di ciascun corpo libero. Se le reazioni cambiano senza che cambi il sistema fisico, probabilmente è stato modificato in modo incoerente lo schema o sono stati persi carichi nel passaggio. Questo confronto è particolarmente utile negli esercizi con più elementi collegati.

Il corpo libero va infine confrontato con lo schema originario: ogni collegamento eliminato deve essere sostituito dalla corrispondente azione esterna.

Nessuna azione va duplicata.

## ▣ Verifica 2

Disegna qualitativamente il corpo libero di una trave semplice. Sostituisci i vincoli con reazioni compatibili e controlla che nessun carico venga contato due volte. Non eseguire calcoli: descrivi quali equazioni di equilibrio useresti e che cosa potrebbero determinare.

## N-TR03-03-03 · Sollecitazioni interne e diagrammi

Immagina di sezionare idealmente un elemento. Le azioni che una parte esercita sull’altra sono rappresentate dalle caratteristiche della sollecitazione.

### Sforzo normale

Lo sforzo normale agisce lungo l’asse dell’elemento. Può essere associato a trazione o compressione. Il segno dipende dalla convenzione adottata; il significato fisico non deve dipendere dalla memoria di un segno isolato.

### Taglio

Il taglio rappresenta l’azione interna trasversale rispetto all’asse dell’elemento. È collegato alla variazione del momento flettente lungo la trave e contribuisce allo stato tensionale.

### Momento flettente

Il momento flettente è associato alla curvatura dell’elemento e alla flessione. La distribuzione delle tensioni dipende, nelle ipotesi del modello, anche dalla geometria della sezione.

### Momento torcente

La torsione tende a far ruotare le sezioni intorno all’asse dell’elemento. Il comportamento dipende in modo sensibile dalla forma della sezione e dal modello adottato.

I diagrammi delle sollecitazioni mostrano come queste grandezze variano lungo l’elemento. Non sono disegni ornamentali: servono a individuare zone critiche, controllare la coerenza del risultato e preparare le verifiche.

### Dalla sezione alla lettura del comportamento

Il taglio ideale di un elemento rende visibili le azioni interne che assicurano l'equilibrio delle due parti. La risultante viene descritta attraverso caratteristiche riferite a una convenzione locale. Cambiando faccia della sezione, i versi compatibili cambiano; per questo un segno ha senso soltanto insieme alla convenzione usata.

Lo sforzo normale è collegato all'azione lungo l'asse e distingue qualitativamente trazione e compressione. Il taglio rappresenta una risultante trasversale. Il momento flettente tende a curvare l'elemento, mentre la torsione produce rotazione relativa delle sezioni intorno all'asse. In un problema reale più caratteristiche possono agire insieme.

I diagrammi descrivono la variazione lungo l'elemento. Punti di applicazione dei carichi, discontinuità e condizioni alle estremità aiutano a prevederne l'andamento. Prima di disegnare valori, individua tratti, segni e possibili massimi. La relazione qualitativa fra carico, taglio e momento offre un controllo, ma va usata nel quadro delle convenzioni adottate.

### Controlli senza calcolo dettagliato

La simmetria offre un controllo immediato: geometria e carico simmetrici dovrebbero produrre una risposta coerente, salvo condizioni che la rompano. Contano anche le condizioni al contorno: un'estremità libera non può trasmettere caratteristiche incompatibili con il modello del vincolo.

Controlla poi le unità. Forza e momento non sono intercambiabili; tensione e sollecitazione appartengono a livelli diversi. Un risultato con dimensioni sbagliate segnala un'impostazione o una manipolazione errata anche se il numero appare plausibile.

Confronta anche il diagramma con la deformata qualitativa. Momento flettente e curvatura sono collegati dal modello della trave; una forma palesemente incompatibile invita a rivedere segni, vincoli o carichi. Il confronto non sostituisce il calcolo, ma evita di consegnare un risultato privo di senso fisico.

| Caratteristica | Effetto qualitativo | Domanda di controllo |
| --- | --- | --- |
| sforzo normale | trazione o compressione | agisce lungo l'asse? |
| taglio | scorrimento relativo | è trasversale alla sezione? |
| momento flettente | curvatura | quale lato tende o comprime? |
| torsione | rotazione intorno all'asse | la sezione è sensibile alla torsione? |

### Quiz 3

Che cosa rappresenta un diagramma delle sollecitazioni? A) la geometria reale completa; B) la variazione di una caratteristica interna lungo l'elemento; C) la tensione in ogni punto del materiale; D) la verifica normativa finale.

**Risposta corretta:** B. Il diagramma riguarda una risultante interna lungo l'elemento. Per passare alle tensioni locali servono anche geometria della sezione e ipotesi del modello.

Nella risposta orale conviene associare ogni sollecitazione a un gesto fisico semplice, poi precisare che l'elemento reale può essere soggetto a combinazioni. L'immagine aiuta a ricordare il significato, ma non sostituisce convenzioni, equilibrio e distribuzione lungo l'asse. In questo modo il candidato evita definizioni puramente mnemoniche.

Una lettura corretta indica sempre elemento, sezione, asse locale e convenzione: senza questi riferimenti anche un diagramma ben tracciato resta ambiguo.

Il controllo resta qualitativo e motivato.

## ▣ Verifica 3

Per ciascuna azione interna indica l'effetto prevalente: sforzo normale, taglio, momento flettente e momento torcente. Aggiungi un controllo fisico che permetta di riconoscere un diagramma palesemente incoerente.

## N-TR03-03-04 · Tensione, deformazione e comportamento dei materiali

### Tensione e deformazione

Sollecitazione e tensione non sono sinonimi. La sollecitazione è una grandezza risultante riferita alla sezione; la tensione descrive l’intensità locale delle azioni interne nel materiale.

La deformazione descrive il cambiamento locale di forma o dimensione. Lo spostamento riguarda il movimento di un punto; la deformazione riguarda la variazione relativa tra punti vicini. Un corpo può muoversi rigidamente senza deformarsi.

Il legame costitutivo collega tensione e deformazione secondo un modello del materiale. Nel comportamento elastico, rimuovendo l’azione il materiale tende a recuperare la deformazione prevista dal modello. La linearità aggiunge una relazione proporzionale entro il campo assunto. Elasticità e linearità, quindi, non sono la stessa cosa.

Queste distinzioni servono in prova perché impediscono risposte generiche. Dire “la trave è sollecitata” non chiarisce né la risultante interna né lo stato locale del materiale.

### Proprietà e comportamento dei materiali

Il comportamento strutturale dipende dal materiale e dal modo in cui è impiegato. Tra le proprietà ricorrenti:

- resistenza rispetto a specifiche modalità di crisi;
- rigidezza nel rapporto tra azione e deformazione;
- duttilità e capacità deformativa;
- tenacità, legata all’energia assorbibile prima della rottura;
- effetti del tempo, della temperatura e dell’ambiente;
- variabilità delle proprietà.

Un unico valore non descrive l’intero comportamento. Materiali diversi possono avere resistenza simile ma rigidezza, duttilità o durabilità differenti. Anche dire “materiale resistente” è incompleto se non si specificano tipo di azione, stato limite e condizioni.

### Dal materiale al sistema

La tensione descrive l'intensità locale delle azioni interne. La sua distribuzione dipende dalla sollecitazione, dalla forma della sezione e dalle ipotesi cinematiche. Una stessa risultante può quindi produrre distribuzioni diverse in sezioni differenti. La tensione media può essere utile, ma non racconta ogni concentrazione o variazione locale.

La deformazione misura variazioni relative, mentre lo spostamento descrive il moto di un punto. Una traslazione rigida può avere spostamenti senza deformazione. Al contrario, una deformazione nasce dal cambiamento delle distanze o degli angoli fra punti vicini. Questa distinzione permette di separare cinematica globale e risposta locale.

Il legame costitutivo mette in relazione tensioni e deformazioni secondo un modello del materiale. “Elastico” significa che, nel modello considerato, la deformazione è recuperabile al venir meno dell'azione; “lineare” indica proporzionalità. Un comportamento può essere elastico senza essere lineare. Dichiarare entrambe le ipotesi come sinonimi nasconde il campo di validità.

### Proprietà e condizioni

Le proprietà meccaniche non sono etichette assolute. Dipendono dal materiale, dalla direzione, dalla storia, dal tempo e dalle condizioni ambientali secondo il fenomeno studiato. La variabilità impone di trattare i dati con la precisione coerente con la fonte e con lo scopo.

Rigidezza del materiale e rigidezza dell'elemento non coincidono. La prima è descritta attraverso proprietà costitutive; la seconda dipende anche da geometria, lunghezza, vincoli e tipo di sollecitazione. Modificare la sezione può cambiare molto la deformabilità senza cambiare materiale.

Un controllo dimensionale accompagna il ragionamento. Ogni grandezza deve avere unità coerenti con la propria definizione; somme e confronti richiedono omogeneità. Il controllo non dimostra che il modello sia corretto, ma intercetta errori che nessuna esposizione elegante può compensare.

### Quiz 4

Quale affermazione è corretta? A) spostamento e deformazione sono sinonimi; B) elasticità implica sempre linearità; C) la rigidezza dell'elemento dipende anche dalla geometria; D) sollecitazione e tensione sono la stessa grandezza.

**Risposta corretta:** C. Geometria, lunghezza, vincoli e materiale concorrono alla rigidezza dell'elemento. Le altre opzioni confondono grandezze o proprietà distinte.

Quando confronti materiali o sezioni, specifica sempre la grandezza osservata. Dire che una soluzione “si deforma meno” può riferirsi a proprietà del materiale, geometria dell'elemento o condizioni di vincolo. Senza questa precisazione non è possibile attribuire correttamente la causa della risposta.

Il lessico preciso permette quindi di collegare scala globale, sezione e materiale senza saltare passaggi.

## ▣ Verifica 4

Spiega con parole tue le differenze fra sollecitazione e tensione, spostamento e deformazione, elasticità e linearità. Per ogni coppia costruisci un esempio nel quale confondere i termini porterebbe a una conclusione sbagliata.

## N-TR03-03-05 · Cinque prestazioni strutturali

### Cinque prestazioni da non confondere

### Resistenza

La resistenza riguarda la capacità di non raggiungere la crisi considerata. La verifica confronta domanda e capacità nel modello adottato. Non dice, da sola, se gli spostamenti sono accettabili.

### Rigidezza

La rigidezza esprime l’opposizione alla deformazione. Un elemento può essere resistente ma troppo deformabile per la funzione richiesta.

### Stabilità

La stabilità riguarda la conservazione dell’equilibrio rispetto a perturbazioni. Negli elementi compressi può diventare decisiva anche quando la resistenza del materiale, considerata isolatamente, sembrerebbe sufficiente.

### Duttilità

La duttilità è la capacità di sviluppare deformazioni significative oltre il campo elastico prima della crisi, secondo il materiale e il sistema. Non coincide con la deformabilità generica.

### Durabilità

La durabilità riguarda il mantenimento nel tempo delle prestazioni richieste. Ambiente, dettagli, protezione, manutenzione e uso influenzano il degrado. Una verifica iniziale non esaurisce il problema.

### Domanda, capacità e modalità di crisi

La resistenza viene valutata rispetto a una modalità di crisi e a un modello. La domanda rappresenta l'effetto delle azioni; la capacità descrive ciò che elemento o sistema possono sostenere secondo i criteri applicabili. Un confronto ha senso soltanto se domanda e capacità si riferiscono alla stessa grandezza e alle stesse ipotesi.

La rigidezza governa il rapporto fra azione e deformazione. Un elemento può restare lontano dalla crisi e tuttavia deformarsi troppo per l'uso previsto. La conseguenza può riguardare funzionalità, comfort, integrità di componenti o compatibilità con altre parti, secondo l'opera.

La stabilità esamina la conservazione dell'equilibrio. Negli elementi compressi geometria, vincoli, imperfezioni e snellezza possono dominare la risposta. Non basta confrontare una tensione media con la resistenza del materiale, perché la crisi può coinvolgere una configurazione dell'intero elemento.

La duttilità riguarda la capacità di sviluppare deformazioni oltre il campo elastico prima della crisi, con modalità dipendenti da materiale e sistema. È diversa dalla semplice deformabilità: un sistema molto deformabile può non possedere la capacità dissipativa o la riserva post-elastica che il termine richiama.

La durabilità introduce il tempo. Ambiente, dettagli, protezione, manutenzione e uso influenzano la conservazione delle prestazioni. Un elemento adeguato inizialmente può degradarsi; progettazione e gestione devono considerare il fenomeno nel quadro tecnico applicabile.

### Leggere le interazioni

Le cinque prestazioni non sono compartimenti isolati. Una variazione geometrica può aumentare rigidezza e stabilità; il degrado può ridurre la capacità; una scelta di dettaglio può influenzare durabilità e modalità di crisi. In prova è utile partire dalla prestazione richiesta e poi indicare i collegamenti, senza confondere le definizioni.

| Prestazione | Domanda centrale | Errore tipico |
| --- | --- | --- |
| resistenza | si raggiunge la crisi considerata? | usarla come giudizio totale |
| rigidezza | deformazioni e spostamenti sono compatibili? | confonderla con resistenza |
| stabilità | l'equilibrio resta stabile? | ignorare snellezza e vincoli |
| duttilità | quale capacità deformativa precede la crisi? | chiamarla deformabilità |
| durabilità | le prestazioni si mantengono nel tempo? | limitarla alla verifica iniziale |

### Quiz 5

Un elemento è resistente ma troppo deformabile. Quale prestazione è direttamente coinvolta? A) soltanto durabilità; B) rigidezza; C) soltanto duttilità; D) nessuna, perché la resistenza basta.

**Risposta corretta:** B. La resistenza non garantisce deformazioni compatibili con la funzione. L'adeguatezza richiede tutte le prestazioni pertinenti.

Lo stesso metodo vale per una domanda sulla durabilità. Non basta elencare agenti di degrado: occorre collegare ambiente, dettaglio, protezione, ispezione e manutenzione alla prestazione da conservare. Per la duttilità, invece, bisogna chiarire quale capacità deformativa si considera e perché sia utile al comportamento del sistema. Ogni termine acquista significato nella relazione fra domanda, meccanismo e conseguenza.

Quando più prestazioni interagiscono, la risposta deve conservarne i nomi e spiegare il legame causale. Dire genericamente che l'elemento “non funziona” non chiarisce se il problema riguardi crisi, deformazione, equilibrio, capacità deformativa o degrado nel tempo.

La diagnosi della prestazione guida il controllo successivo.

## ▣ Verifica 5

Confronta due elementi: il primo è molto resistente ma deformabile; il secondo ha materiale resistente ma geometria snella in compressione. Indica quali prestazioni, oltre alla resistenza, devono essere esaminate e perché.

## N-TR03-03-06 · Metodo di analisi e caso dell'elemento compresso

### Caso ragionato: un elemento compresso

Un elemento snello riceve una forza di compressione. Una risposta superficiale controlla soltanto la tensione media. Una risposta strutturale completa procede diversamente.

La risposta definisce geometria, vincoli e imperfezioni rilevanti, quindi separa la resistenza del materiale dalla stabilità dell'equilibrio. Snellezza e condizioni alle estremità aiutano a leggere la deformata attesa. Su questa base si individua la verifica richiesta dal quadro tecnico applicabile.

Il caso mostra perché non basta chiedere “quanto resiste il materiale?”. La crisi può dipendere dal comportamento dell’intero elemento.

### Da sapere in 5 righe

Il modello è una scelta, non una copia della struttura.  
L’equilibrio è necessario ma non esaurisce la verifica.  
Sollecitazione, tensione e deformazione indicano grandezze diverse.  
Resistenza e rigidezza non sono sinonimi.  
Stabilità e durabilità richiedono controlli propri.

### Domanda da commissario

**Qual è il percorso logico per analizzare una struttura semplice?**

Si definiscono scopo e ipotesi, si costruisce lo schema con geometria e vincoli, si applicano le azioni, si determinano reazioni e sollecitazioni, si valuta la risposta in termini di tensioni e deformazioni e si eseguono le verifiche pertinenti. Il risultato va infine controllato sul piano fisico e dimensionale.

### Domanda-trappola

**Se un elemento soddisfa la verifica di resistenza, è certamente adeguato?**

No. Possono risultare decisive rigidezza, stabilità, deformazioni, durabilità e altre prestazioni richieste. L’adeguatezza dipende dall’insieme delle verifiche applicabili.

### Errore tipico

L’errore più comune è scrivere una formula senza dichiarare modello, ipotesi, grandezze e significato del risultato. Per evitarlo, segui questa sequenza: dati, schema, ipotesi, equazioni, risultato, controllo.

### Mini-esercizio

Per ciascun fenomeno indica la grandezza prevalente:

1. allungamento di una barra tesa;
2. rotazione di una trave inflessa;
3. perdita di equilibrio di un’asta compressa;
4. degrado progressivo in ambiente aggressivo;
5. azione interna trasversale in una sezione.

Le risposte attese sono: deformazione assiale; spostamento/rotazione legati alla rigidezza flessionale; stabilità; durabilità; taglio.

### Checklist di impostazione

- Ho definito il sistema e lo scopo?
- Ho dichiarato vincoli, azioni e ipotesi?
- Ho distinto reazioni e sollecitazioni?
- Ho distinto sollecitazioni, tensioni e deformazioni?
- Ho controllato resistenza, rigidezza e stabilità pertinenti?
- Il risultato è fisicamente plausibile?
- Ho indicato i limiti del modello?

### Una checklist che precede le formule

Il percorso di analisi comincia dallo scopo. Si definisce il sistema, si scelgono scala e ipotesi, si rappresentano vincoli e azioni, si controlla la cinematica e si applica l'equilibrio. Solo dopo si determinano le sollecitazioni e si passa alla risposta locale di sezione e materiale.

Il risultato deve poi essere letto rispetto alle prestazioni. Una grandezza numerica senza confronto o significato fisico non chiude il problema. Occorre chiedersi che cosa dimostri, entro quali ipotesi e quale verifica resti da svolgere secondo la disciplina applicabile.

Nel caso dell'elemento compresso, la tensione media offre un'informazione parziale. La geometria snella e le condizioni alle estremità richiamano il problema della stabilità. Imperfezioni e deformazioni possono amplificare gli effetti; la valutazione normativa appartiene al quadro del capitolo successivo e non può essere sostituita dal ragionamento qualitativo.

### Uso nelle prove

Nel quiz, individua la distinzione sottostante prima di scegliere: equilibrio non equivale ad adeguatezza; resistenza non equivale a rigidezza; elasticità non equivale a linearità. Nello scritto, dichiara modello e ipotesi prima di usare relazioni. All'orale, costruisci una catena breve e chiudila con controllo fisico e limiti.

Quando la traccia non fornisce dati sufficienti, non inventarli. Spiega quali servirebbero e quale decisione consentirebbero. Una risposta qualitativa ben delimitata dimostra più competenza di un calcolo basato su valori arbitrari.

Il controllo finale comprende segni, unità, ordine di grandezza, condizioni al contorno e coerenza fra diagrammi e deformata. Se uno di questi elementi contraddice il risultato, torna al modello prima di correggere soltanto l'ultima operazione.

### Quiz 6

In quale momento è corretto scegliere una formula? A) prima di definire il sistema; B) dopo aver chiarito scopo, modello, ipotesi e grandezza cercata; C) quando la si ricorda; D) soltanto dopo la verifica normativa.

**Risposta corretta:** B. La relazione matematica appartiene a un modello e a un campo di validità. Usarla prima di averli chiariti produce risultati formalmente ordinati ma fisicamente privi di fondamento.

## ▣ Verifica 6

Prepara una risposta orale di due minuti usando la sequenza: scopo, modello, vincoli, azioni, equilibrio, risposta, prestazioni e limiti. La spiegazione deve restare comprensibile anche senza formule e deve indicare quale controllo normativo appartiene al capitolo successivo.

## Riferimenti essenziali

- programmi e materiali didattici universitari ufficiali di statica, scienza e tecnica delle costruzioni;
- testi vigenti richiamati dal singolo bando per la profondità e il perimetro della prova;
- Norme Tecniche per le Costruzioni e relativa documentazione applicabile, trattate nel capitolo successivo;
- consegna, dati e convenzioni esplicitati nella specifica prova concorsuale.

Il capitolo fornisce un metodo qualitativo e non costituisce calcolo o verifica di un'opera reale. Il livello matematico va calibrato sul singolo bando; prescrizioni NTC, combinazioni delle azioni, sismica e geotecnica appartengono al capitolo 04.
