---
id: chapter-m-tr03-12-bim-gis-catasto-patrimonio
type: book_chapter
title: "BIM, GIS, rilievi, catasto e patrimonio pubblico"
status: draft
domain: concorsi pubblici italiani
topics: ["BIM", "GIS", "rilievi", "catasto", "patrimonio pubblico", "gestione informativa"]
entities: ["Ministero delle infrastrutture e dei trasporti", "AgID", "Agenzia delle entrate", "AINOP"]
source_refs: ["sources/bim-gis-catasto-patrimonio-fonti-ufficiali-2026.md", "sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024.md", "sources/catasto-cartografia-estimo-pubblicita-immobiliare-aggiornamento-2026-07-18.md", "sources/codice-civile-beni-pubblici-demanio-patrimonio.md", "sources/infrastrutture-viabilita-ponti-monitoraggio-fonti-ufficiali-2026.md", "sources/campione-bandi-tecnici-pa-vol-10-2026.md", "sources/modulo-m-tr03-tecnico-ingegneristico-vol-10.md"]
book_refs: ["m-tr03-tecnico-ingegneristico"]
confidence: 0.9
updated_at: "2026-08-12T00:00:00+02:00"
created_at: "2026-07-30T00:00:00+02:00"
review_required: true
canonical: true
tags: ["chapter", "vol-10", "m-tr03", "bim", "gis", "catasto", "patrimonio", "format-2"]
book_id: m-tr03-tecnico-ingegneristico
outline_section: "12"
format_version: 2
draft_stage: step-09-format-2-retrofit
dati_operativi: []
last_compiled_from: ["wiki/books/moduli/m-tr03-tecnico-ingegneristico/planning/08-capitolo-12-piano-completamento.md", "wiki/sources/bim-gis-catasto-patrimonio-fonti-ufficiali-2026.md", "wiki/sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024.md", "wiki/sources/catasto-cartografia-estimo-pubblicita-immobiliare-aggiornamento-2026-07-18.md", "wiki/sources/codice-civile-beni-pubblici-demanio-patrimonio.md", "wiki/sources/infrastrutture-viabilita-ponti-monitoraggio-fonti-ufficiali-2026.md", "wiki/sources/campione-bandi-tecnici-pa-vol-10-2026.md", "wiki/sources/modulo-m-tr03-tecnico-ingegneristico-vol-10.md", "wiki/topics/bim-gis-catasto-patrimonio-pubblico.md"]
---

# BIM, GIS, rilievi, catasto e patrimonio pubblico

## Apertura, obiettivo e Mappa BANDO

La quantità di dati disponibili non garantisce, da sola, la conoscenza di un bene pubblico. Una planimetria, un modello informativo, una visura catastale, un layer cartografico, una nuvola di punti e una scheda inventariale possono descrivere lo stesso edificio, ma rispondono a domande diverse. Il tecnico pubblico deve saperle distinguere prima di usarle: che cosa rappresentano, chi le ha prodotte, quando, con quale metodo, con quale qualità e per quale decisione.

L'obiettivo è costruire una mappa dato-opera-decisione. Alla fine devi saper spiegare la differenza tra BIM, GIS, rilievo, catasto, pubblicità immobiliare, stato legittimo, patrimonio, inventario e AINOP; devi inoltre saper riconciliare dati non coincidenti senza promettere un'integrazione automatica dei sistemi.

**Mappa BANDO**

- **Bando:** cerca parole come BIM, gestione informativa, GIS, cartografia, rilievo, catasto, patrimonio, inventario e manutenzione.
- **Aree:** collega il tema a lavori pubblici, edilizia, territorio, manutenzione, gestione patrimoniale e dati tecnici.
- **Nuclei:** studia requisito, fonte, versione, qualità, modello, geometria, attributo, identificativo, regime del bene e sistema da aggiornare.
- **Diario:** registra gli errori in cui confondi modello e opera, mappa e territorio, catasto e conformità, inventario tecnico e valore contabile.
- **Output:** produci una risposta orale, una tabella di riconciliazione o una checklist che dica quale dato usare, per quale scopo e con quale cautela.

> **Da sapere in 5 righe**
>
> BIM organizza processi e informazioni sulle costruzioni, non coincide con un render o con un software.
> GIS collega geometrie, attributi e relazioni spaziali, ma una sovrapposizione cartografica non prova da sola un vincolo o un diritto.
> Il rilievo produce dati osservati con metodo, riferimento e qualità dichiarati.
> Il catasto identifica e descrive immobili per le proprie funzioni, ma resta distinto da titolo, pubblicità immobiliare e stato legittimo.
> L'inventario patrimoniale è utile solo se resta collegato al bene reale, alle decisioni e agli aggiornamenti.

## N-TR03-12-01 · Dato tecnico e ciclo informativo

### Teoria essenziale

Il dato tecnico è un'informazione riferita a un'opera, a una parte di opera, a un'area o a un elemento territoriale. Non è un numero isolato e non è un file qualunque: ha senso solo se sono chiari oggetto, requisito, fonte, autore, data, metodo, qualità e versione. Un dato può indicare la posizione di un edificio, la consistenza di una scuola, lo stato di una pavimentazione, la destinazione d'uso di un ambiente, la presenza di un vincolo o il responsabile gestionale di un bene. In tutti i casi il primo controllo non è tecnologico, ma logico: quale domanda deve risolvere?

Il ciclo informativo parte dal requisito. Prima di acquisire un dato, l'amministrazione deve sapere perché le serve: progettare, verificare, programmare manutenzione, aggiornare inventario, controllare un documento, rispondere a una richiesta o assumere una decisione. L'acquisizione produce l'informazione; il controllo ne verifica coerenza, qualità e adeguatezza allo scopo; l'uso trasforma il dato in valutazione; la decisione genera effetti; l'aggiornamento riporta quegli effetti nei sistemi competenti; la conservazione consente di ricostruire nel tempo fonte, versione e responsabilità.

La versione è parte del significato. Due elaborati con lo stesso nome possono descrivere stati diversi: progetto, variante, as built, rilievo successivo, aggiornamento catastale, scheda inventariale rivista. La data più recente non vince automaticamente. Un file recente può essere solo una copia non approvata; un documento meno recente può restare l'atto utile per una certa verifica; un rilievo osserva lo stato di fatto ma non prova da solo la regolarità edilizia. La competenza tecnica consiste nel collocare ogni dato nella catena corretta.

### Schema operativo

| Passaggio | Domanda da fare | Rischio se manca |
| --- | --- | --- |
| Requisito | Quale decisione deve sostenere il dato? | acquisire informazioni inutili o insufficienti |
| Acquisizione | Chi produce il dato e con quale metodo? | trattare il file come evidenza neutra |
| Controllo | Qualità, coerenza e versione sono verificabili? | usare dati incompatibili o non aggiornati |
| Uso | Il dato risponde proprio alla domanda posta? | confondere funzione tecnica, giuridica e contabile |
| Decisione | Quale atto o scelta deriva dall'informazione? | lasciare il dato senza conseguenza operativa |
| Aggiornamento | Quali sistemi devono essere aggiornati? | creare archivi divergenti |
| Conservazione | Come si ricostruiscono fonte e responsabilità? | perdere tracciabilità nella gestione futura |

### Applicazione al profilo tecnico

In un concorso tecnico, questa logica compare spesso nei casi pratici. Ti viene chiesto di gestire un edificio comunale, programmare un intervento, verificare una difformità o coordinare dati territoriali. La risposta efficace non parte dicendo "uso il BIM" o "apro il GIS"; parte dal requisito informativo. Se il problema è localizzare il bene in un contesto territoriale, userai dati cartografici e GIS. Se devi coordinare informazioni dell'edificio nel ciclo di vita, userai gestione informativa e modelli. Se devi controllare lo stato osservato, serve un rilievo adeguato. Se devi identificare catastalmente l'immobile, userai visura, mappa o planimetria nei limiti della loro funzione. Se devi aggiornare la gestione dell'ente, guarderai inventario, responsabilità e fascicolo del bene.

La commissione valuta soprattutto la capacità di non saltare passaggi. Una risposta matura distingue la fonte dal dato, il dato dalla valutazione e la valutazione dalla decisione. Quando segnali un conflitto, non devi risolverlo per intuizione: devi indicare quali evidenze confrontare, quale ufficio o competenza coinvolgere e quale sistema aggiornare dopo l'esito. Questo evita due errori tipici: credere che il documento più nuovo cancelli tutti gli altri e pensare che una piattaforma integrata renda superflua la responsabilità tecnica.

### Controllo vicino

Prendi quattro dati sullo stesso edificio: planimetria catastale, modello informativo, rilievo recente e scheda inventariale. Per ciascuno indica oggetto, funzione, fonte, data, qualità dichiarata e decisione che può sostenere. Se non riesci a completare una riga, non hai ancora un dato utilizzabile: hai solo un documento da verificare. Conviene definire prima la domanda e scegliere poi il dato, non il contrario. In una risposta orale, questa griglia rende evidente il metodo: evita di partire dallo strumento e porta a dichiarare limiti, verifiche e sistema da aggiornare.

## N-TR03-12-02 · BIM e gestione informativa

### Teoria essenziale

Il BIM, nella preparazione concorsuale, va studiato come gestione informativa digitale delle costruzioni. Non coincide con il modello tridimensionale, con un programma software, con un render o con una tavola graficamente evoluta. Il modello informativo può contenere geometrie, relazioni e attributi, ma il valore amministrativo e tecnico dipende dal processo che lo produce: requisiti della stazione appaltante, documenti di gestione informativa, ambiente di condivisione, stati di approvazione, verifiche, consegne e aggiornamenti nel ciclo di vita dell'opera.

Il D.Lgs. 36/2023, con l'art. 43 e l'Allegato I.9, colloca metodi e strumenti di gestione informativa digitale dentro il sistema dei contratti pubblici. I decreti ministeriali sul tema restano riferimenti di coordinamento, da leggere nel quadro vigente. Per lo studio non serve memorizzare soglie mobili o ricostruire configurazioni operative; serve capire la logica: quando la gestione informativa è prevista, l'amministrazione non chiede un modello fine a se stesso, ma informazioni utilizzabili per progettazione, affidamento, esecuzione, controllo e gestione.

Il processo prende avvio dai requisiti informativi. La stazione appaltante deve chiarire quali informazioni occorrono, con quale livello di dettaglio utile allo scopo, in quali momenti e con quali criteri di verifica. L'operatore economico organizza la propria risposta nei documenti previsti dal processo. Il modello, le tavole, le relazioni, gli elaborati contabili, i manuali e la documentazione di consegna non sono intercambiabili: ciascuno conserva una funzione. Un modello può coordinare informazioni, ma non trasforma automaticamente un dato non verificato in dato approvato.

Un elemento essenziale è l'ambiente di condivisione dei dati. Serve a governare accessi, caricamenti, revisioni, stati, approvazioni, versioni e conservazione. Caricare un file non significa approvarlo; condividere un modello non significa che ogni attributo sia corretto; leggere un formato scambiabile non significa conservare tutto il significato informativo. L'interoperabilità richiede formati e regole che mantengano struttura, relazioni e attributi per l'uso previsto, non solo apertura tecnica del file.

### Schema operativo

| Elemento BIM | Funzione corretta | Limite da ricordare |
| --- | --- | --- |
| Requisito informativo | definisce quali dati servono e quando | non va dedotto dal software disponibile |
| Modello informativo | organizza oggetti, geometrie e attributi | non prova da solo titolo, conformità o collaudo |
| Elaborati | rappresentano e documentano scelte specifiche | non sono semplici esportazioni grafiche |
| Ambiente di condivisione | traccia stati, versioni e approvazioni | caricamento e validazione restano distinti |
| Consegna alla gestione | trasferisce informazioni utili al ciclo di vita | non avviene automaticamente senza regole |

### Applicazione al profilo tecnico

Nel profilo tecnico pubblico, il BIM è rilevante perché collega progetto, esecuzione e gestione. Un funzionario o istruttore tecnico può dover leggere documenti di gara, controllare consegne informative, coordinare dati di un edificio o predisporre un fascicolo utile alla manutenzione. La risposta concorsuale deve quindi evitare sia l'entusiasmo generico sia la diffidenza generica. Non basta dire che il BIM "digitalizza l'opera"; occorre spiegare quale informazione viene richiesta, dove viene conservata, chi la verifica secondo competenza e come passa alla gestione del bene.

Un esempio semplice: alla fine di un intervento su una scuola, il modello aggiornato può essere utile per conoscere locali, componenti, impianti, documenti collegati e informazioni manutentive. Tuttavia l'ente deve distinguere modello, elaborati come costruito, certificazioni, fascicolo, piano di manutenzione e inventario. Se un attributo del modello indica una porta tagliafuoco, il tecnico non deve trattarlo come verità assoluta: verifica fonte, stato, documento collegato e coerenza con il sopralluogo o con gli atti disponibili. L'uso professionale del BIM è proprio questa capacità di trasformare un contenitore informativo in un sistema controllabile.

### Controllo vicino

Rispondi in tre passaggi alla domanda: "Che cosa consegna l'appaltatore quando consegna un modello BIM?". Prima distingui modello, elaborati e documenti; poi spiega che l'ambiente di condivisione conserva versioni e stati; infine precisa che la consegna diventa utile alla gestione solo se gli attributi necessari sono verificati e collegati al bene. Aggiungi sempre chi controlla secondo competenza e quale evidenza resta conservata. Se nella risposta usi la parola "automaticamente", controlla se stai promettendo più di quanto le fonti consentano.

## N-TR03-12-03 · GIS, cartografia e qualità spaziale

### Teoria essenziale

Il GIS è un sistema per gestire dati georiferiti, cioè informazioni collegate a una posizione nello spazio. Non è semplicemente una mappa digitale. Una mappa mostra; un GIS permette di organizzare geometrie, attributi, layer, relazioni spaziali e interrogazioni. Le geometrie possono rappresentare punti, linee o aree; gli attributi descrivono caratteristiche come destinazione, stato, classificazione, fonte, data o responsabile; i layer separano temi diversi, per esempio edifici pubblici, viabilità, vincoli, reti, aree verdi o particelle.

La forza del GIS è anche il suo rischio principale: sovrapporre dati diversi fa vedere relazioni che sembrano immediate. Un edificio appare dentro un'area, una strada interseca una fascia, una particella ricade in un perimetro. Questa evidenza grafica non è ancora una conclusione giuridica o tecnica. Occorre verificare fonte, data, scala, sistema di riferimento, metadati e disciplina applicabile. Un layer vecchio può non rappresentare lo stato attuale; un dataset molto dettagliato può essere stato acquisito con scarsa accuratezza; due dati in sistemi di riferimento diversi possono apparire traslati; un poligono cartografico può avere funzione ricognitiva e non decisoria.

Le parole precisione, accuratezza, risoluzione e scala non sono sinonimi. La precisione riguarda la ripetibilità o finezza della misura; l'accuratezza riguarda la vicinanza al valore di riferimento; la risoluzione indica il dettaglio distinguibile; la scala incide sul rapporto di rappresentazione e sull'uso corretto del dato. Molte cifre decimali non rendono automaticamente affidabile una coordinata. Una base cartografica utile per pianificare può essere insufficiente per verifiche di dettaglio; un rilievo locale può essere accurato per un edificio ma non adeguato a rappresentare una rete territoriale.

I metadati sono la scheda di identità del dato territoriale. Le regole collegate a INSPIRE, al D.Lgs. 32/2010, al Repertorio nazionale dei dati territoriali e alle indicazioni AgID servono a rendere ricercabili e comprensibili dati e servizi geografici. Per il candidato non è necessario trasformarsi in amministratore di infrastrutture dati; è necessario capire che un dato territoriale senza metadati è debole, perché non consente di giudicare origine, aggiornamento, qualità e uso appropriato.

### Schema operativo

| Componente GIS | Che cosa indica | Domanda di controllo |
| --- | --- | --- |
| Geometria | punto, linea o area rappresentata | rappresenta davvero l'oggetto che sto valutando? |
| Attributo | informazione descrittiva collegata | da quale fonte deriva e quanto è aggiornata? |
| Layer | tema separato dagli altri | è coerente con scala e finalità dell'analisi? |
| Query | interrogazione del dato | la domanda è tecnica, spaziale o giuridica? |
| Metadato | contesto del dataset | posso ricostruire fonte, data, qualità e limiti? |

### Applicazione al profilo tecnico

Un tecnico comunale può usare il GIS per localizzare immobili, verificare interferenze preliminari, programmare manutenzioni, visualizzare reti o preparare istruttorie. In prova, però, devi sempre trasformare la mappa in ragionamento. Se una scuola appare vicina a un'area vincolata, la risposta corretta non è "il GIS dimostra il vincolo"; è "il GIS segnala una possibile interferenza da verificare con fonte, data, perimetro, disciplina e atti competenti". Se una particella non coincide perfettamente con l'edificio rilevato, non concludi subito che c'è abuso o errore catastale: distingui base cartografica, sistema di riferimento, scala, aggiornamento e funzione del dato.

Nella prova orale questo approccio dimostra prudenza tecnica. Chi sa leggere un GIS non si limita a descrivere colori e layer: chiarisce la domanda, espone i limiti, distingue l'analisi spaziale dalla decisione amministrativa e indica il successivo controllo documentale o tecnico. Il GIS offre elementi per decidere, ma non sostituisce il titolo edilizio, l'accertamento catastale, la valutazione strutturale o la scelta patrimoniale.

### Controllo vicino

Hai un layer dei vincoli, un rilievo recente e una mappa catastale. Le geometrie non coincidono. Prima di parlare di errore, rispondi a cinque domande: i dati hanno lo stesso sistema di riferimento? hanno la stessa scala o risoluzione utile? sono aggiornati alla stessa data? rappresentano lo stesso oggetto? servono alla stessa funzione? Solo dopo puoi indicare quale verifica proseguire. La formula da ricordare è: sovrapposizione come indizio, metadato come garanzia minima, atto competente come base della decisione.

## N-TR03-12-04 · Rilievo e restituzione

### Teoria essenziale

Il rilievo è l'attività con cui si osserva, misura e rappresenta uno stato fisico. Può riguardare un edificio, un'area, una strada, un ponte, una rete, un confine materiale o una componente impiantistica. La sua funzione non è produrre "più dati possibile", ma produrre dati adeguati allo scopo. Un rilievo per progettare una manutenzione non coincide necessariamente con un rilievo per aggiornare una base cartografica, controllare una contabilità, ricostruire una geometria complessa o documentare lo stato di fatto prima di un intervento.

La catena corretta è scopo, accuratezza richiesta, metodo, strumenti, controlli, sistema di riferimento, restituzione e conservazione. Lo scopo stabilisce quali elementi rilevare e con quale livello di dettaglio. L'accuratezza richiesta orienta il metodo. Gli strumenti disponibili, come GNSS, stazione totale, laser scanner o fotogrammetria, hanno funzioni e limiti diversi; non esiste uno strumento migliore in assoluto. I controlli servono a capire se il dato è coerente e ripetibile per l'uso previsto. Il sistema di riferimento rende leggibili le coordinate. La restituzione trasforma le misure in elaborati, modelli, nuvole di punti, sezioni, planimetrie o dataset.

La nuvola di punti merita una distinzione specifica. È un insieme di punti misurati nello spazio, spesso molto ricco, ma non è già un modello informativo. Per diventare supporto decisionale deve essere controllata, pulita, interpretata e restituita secondo una finalità. Una nuvola può aiutare a leggere geometrie esistenti, deformazioni apparenti, ingombri o interferenze, ma non attribuisce automaticamente funzioni, titoli, responsabilità o stati manutentivi. Il passaggio da misura a informazione richiede competenza.

Anche la restituzione non è neutra. Una planimetria, una sezione, un modello, una tabella di coordinate o un report fotografico selezionano e organizzano la realtà. Se la restituzione non dichiara limiti e metodo, l'utente successivo può usarla per scopi impropri. In un ente pubblico questo errore produce effetti concreti: progettazioni basate su dati incompleti, contenziosi su misure, inventari non allineati, manutenzioni programmate su consistenze sbagliate.

### Schema operativo

| Fase del rilievo | Contenuto | Errore tipico |
| --- | --- | --- |
| Scopo | motivo della misura | rilevare senza sapere quale decisione seguirà |
| Metodo | tecnica scelta | scegliere lo strumento perché moderno, non perché adatto |
| Controlli | verifiche di coerenza | accettare la restituzione senza riscontri |
| Restituzione | elaborato o dataset finale | confondere misura, interpretazione e modello |
| Conservazione | archiviazione con riferimenti | perdere autore, data, versione e limiti |

### Applicazione al profilo tecnico

In prova potresti ricevere un caso in cui un'amministrazione deve riqualificare un immobile e possiede documenti non coincidenti. Il rilievo recente è un elemento forte perché fotografa lo stato osservato, ma non basta a chiudere ogni questione. Se il rilievo mostra un ampliamento rispetto alla planimetria, occorre distinguere fatto fisico, dato catastale, titolo edilizio, stato legittimo e aggiornamento inventariale. Se la nuvola di punti permette di ricostruire la geometria, il modello derivato dovrà comunque essere controllato rispetto al requisito informativo.

Il candidato tecnico deve spiegare come imposta l'incarico o l'istruttoria senza trasformarla in procedura eseguibile. Non servono parametri inventati; serve dire che si definiscono scopo, oggetto, accuratezza richiesta, metodo, controlli, restituzione attesa e responsabilità del dato. Una risposta così è solida perché non confonde professione e concorso: mostra criterio, non promette un rilievo reale in astratto. La commissione capisce che sai usare il rilievo come fonte tecnica dentro un processo amministrativo più ampio. Nello scritto, conviene chiudere indicando quali elaborati saranno prodotti e quali decisioni non possono essere assunte solo dalla misura, per esempio conformità edilizia, proprietà o priorità manutentiva senza ulteriori verifiche.

### Controllo vicino

Completa questa frase: "La nuvola di punti non è già un modello informativo perché...". Nella risposta considera almeno tre aspetti: i punti devono essere controllati; la restituzione richiede interpretazione; gli attributi gestionali, documentali o amministrativi non nascono dalla misura geometrica. Aggiungi lo scopo, perché rilievi destinati a contabilità, progetto, manutenzione o inventario generano restituzioni diverse. Nella prova, cita anche l'elaborato atteso, la verifica minima e il responsabile tecnico del dato. Omettere uno di questi aspetti significa trattare lo strumento come se sostituisse il processo.

## N-TR03-12-05 · Catasto e distinzioni immobiliari

### Teoria essenziale

Il catasto identifica e descrive immobili secondo le proprie funzioni. Nel catasto terreni e nel catasto fabbricati compaiono dati che consentono di individuare beni, unità, intestazioni catastali, dati censuari, rendite o altri elementi descrittivi. Foglio, particella e subalterno, quando presente, sono chiavi di identificazione catastale. Visura, mappa e planimetria non sono la stessa cosa: la visura restituisce dati identificativi e censuari; la mappa rappresenta particelle e geometrie catastali; la planimetria riguarda la rappresentazione dell'unità immobiliare urbana nei limiti della funzione catastale.

La funzione catastale non va confusa con la prova piena della proprietà, con la pubblicità immobiliare, con lo stato dei luoghi, con il titolo edilizio o con lo stato legittimo. La pubblicità immobiliare riguarda vicende giuridiche degli immobili attraverso trascrizioni, iscrizioni e annotazioni, secondo la disciplina propria. Il catasto può indicare un'intestazione catastale, ma le vicende dei diritti richiedono la consultazione degli strumenti della pubblicità immobiliare e dei relativi atti. Allo stesso modo, una planimetria catastale coerente non dimostra da sola la conformità urbanistico-edilizia.

Lo stato di fatto è ciò che si osserva sul bene; il titolo è l'atto o il provvedimento che legittima una trasformazione; lo stato legittimo dipende dalla disciplina edilizia e dalla documentazione rilevante; il catasto risponde alla propria funzione censuaria e fiscale. Queste dimensioni possono essere allineate, ma possono anche divergere. Il tecnico pubblico non deve scegliere il documento che gli conviene: deve riconoscere quale domanda può essere risolta da ciascuna fonte.

Gli aggiornamenti catastali hanno procedure e strumenti specifici, come dichiarazioni per unità immobiliari urbane, atti geometrici di aggiornamento del catasto terreni o volture per intestazioni. In un manuale concorsuale è sufficiente conoscere le funzioni generali e le distinzioni. Non è corretto trasformare la trattazione in istruzioni operative, versioni software o passaggi eseguibili, perché dipendono dalla normativa, dalle specifiche vigenti, dall'abilitazione professionale e dal caso concreto.

### Schema operativo

| Fonte o dato | Domanda a cui può rispondere | Domanda a cui non basta |
| --- | --- | --- |
| Visura catastale | come è identificato e censito l'immobile | chi è proprietario in modo definitivo |
| Mappa catastale | come è rappresentata la particella | quale sia lo stato edilizio legittimo |
| Planimetria catastale | come è rappresentata l'unità | se l'opera è conforme al titolo |
| Pubblicità immobiliare | quali atti o formalità risultano | quale sia lo stato fisico attuale |
| Rilievo | che cosa si osserva sul posto | quale diritto o titolo legittima l'opera |

### Applicazione al profilo tecnico

Immagina che una commissione chieda: "La planimetria catastale coincide con il modello BIM; possiamo considerare l'immobile regolare?". La coincidenza costituisce un indizio utile, non una conclusione. Catasto, modello informativo, stato dei luoghi, titolo edilizio e pubblicità immobiliare hanno infatti funzioni diverse. L'allineamento geometrico può ridurre un dubbio operativo, ma non sostituisce la verifica degli atti e della disciplina applicabile.

Nel lavoro di un ente, le distinzioni catastali servono anche alla gestione patrimoniale. Un edificio pubblico deve essere identificato correttamente, collegato all'inventario, ai fascicoli, agli interventi e ai responsabili. Se la visura riporta un dato non aggiornato, non significa automaticamente che il bene non sia dell'ente; significa che occorre verificare atti, formalità e aggiornamenti. Se l'inventario indica una consistenza diversa dalla planimetria, occorre capire se è cambiato il bene, se la fonte è superata o se il sistema gestionale non è stato aggiornato. La prova valuta proprio questa prudenza: non trasformare una banca dati in giudice unico dell'immobile.

### Controllo vicino

Per allenarti, prendi tre affermazioni e correggile: "La visura prova la proprietà"; "la planimetria catastale prova la conformità edilizia"; "la mappa catastale coincide sempre con il rilievo". Una risposta da concorso deve sostituire ogni frase con una distinzione: funzione catastale, pubblicità immobiliare, stato di fatto, titolo e stato legittimo. Se la risposta resta generica, aggiungi quale fonte useresti per proseguire la verifica, quale ufficio coinvolgeresti e quale effetto avrebbe l'eventuale aggiornamento sull'inventario dell'ente pubblico. Questa aggiunta trasforma la nozione in istruttoria.

## N-TR03-12-06 · Patrimonio e caso dato-opera-decisione

### Teoria essenziale

Il patrimonio pubblico non è soltanto l'elenco degli immobili posseduti o utilizzati da un ente. È un insieme di beni con regime giuridico, funzione, destinazione, stato tecnico, responsabilità gestionale, valore amministrativo-contabile e ruolo nel servizio pubblico. Il Codice civile offre la tripartizione essenziale: beni demaniali, beni patrimoniali indisponibili e beni patrimoniali disponibili. La distinzione ruota attorno alla destinazione e incide su uso, circolazione, concessione, tutela, valorizzazione e gestione. Nei casi concreti possono intervenire discipline speciali; per il concorso serve soprattutto non trattare tutti i beni pubblici come beni liberamente disponibili.

L'inventario tecnico e l'inventario amministrativo-contabile dialogano, ma non coincidono. L'inventario tecnico risponde a domande operative: che bene è, dove si trova, a che cosa serve, quali parti contiene, in quale stato è, quali rischi presenta, quali manutenzioni richiede, quali documenti lo descrivono e chi lo gestisce. L'inventario amministrativo-contabile aggiunge classificazioni, valori, registrazioni e raccordi propri della gestione economico-patrimoniale dell'ente. Confonderli produce un errore doppio: si pretende dal dato contabile una diagnosi tecnica, oppure si pretende dalla scheda tecnica una rappresentazione contabile completa.

La scheda del bene è il punto di incontro. Dovrebbe collegare identificativi, ubicazione, regime, funzione, consistenza, componenti, stato, prestazioni, rischi, documenti, modelli, interventi, manutenzioni, costi, priorità, responsabile, fonte, data e versione. Non tutti questi elementi stanno nello stesso sistema e non tutti hanno la stessa autorevolezza. Per questo l'integrazione informativa deve conservare la provenienza del dato e registrare conflitti, non cancellarli.

AINOP, Archivio Informatico Nazionale delle Opere Pubbliche, rileva per le opere pubbliche perché collega identificazione e informazioni sul ciclo di vita. È utile per censimento, dati anagrafici, tecnici, territoriali, manutentivi e di monitoraggio nel perimetro previsto. Non coincide però con l'inventario dell'ente, con il GIS, con il modello BIM o con il catasto. L'allineamento tra sistemi richiede identificativi, regole, responsabilità e aggiornamenti espliciti. Copiare lo stesso valore in più archivi senza governance non integra i dati: moltiplica gli errori.

### Schema operativo

| Sistema | Uso principale | Sistema da aggiornare dopo la decisione |
| --- | --- | --- |
| BIM | informazioni dell'opera e dei componenti | modello e documenti di gestione informativa |
| GIS | collocazione e relazioni territoriali | layer o dataset interessati |
| Catasto | identificazione e dati catastali | archivi catastali secondo funzione e procedura |
| Inventario tecnico | consistenza, uso, stato e responsabilità | scheda del bene e fascicolo tecnico |
| Inventario contabile | classificazione e valore gestionale | registrazioni amministrativo-contabili dell'ente |
| AINOP | dati dell'opera pubblica nel ciclo di vita | archivio dell'opera, se rientra nel perimetro |

### Applicazione al profilo tecnico

Caso guidato: un Comune deve riqualificare una scuola. La planimetria catastale non coincide con l'ultimo elaborato edilizio; il modello del progetto non contiene alcuni dati manutentivi; un layer GIS dei vincoli è datato; il rilievo recente dichiara metodo, sistema di riferimento e controlli; l'inventario indica una consistenza e un responsabile non aggiornati. Il tecnico non sceglie una fonte vincente. Costruisce una tabella dato-opera-decisione: usa fascicolo edilizio e rilievo per confrontare stato e documenti; usa il catasto per identificazione e dati catastali; verifica fonte e data del layer prima di valutare il vincolo; integra nel modello le informazioni necessarie alla gestione; aggiorna inventario e responsabile dopo l'accertamento; conserva evidenza delle decisioni e indica i sistemi da aggiornare.

Nel concludere la risposta occorre precisare che l'integrazione non è automatica. BIM, GIS, catasto, inventario e AINOP possono dialogare solo se l'ente stabilisce identificativi, versioni, flussi e controlli. Il tecnico pubblico deve governare il conflitto tra dati, non nasconderlo. Una divergenza non è sempre un errore: può dipendere da funzione, data, scala, approvazione o responsabilità differenti. La competenza tecnica emerge dalla capacità di tradurre queste differenze in decisioni verificabili.

### Controllo vicino

Risolvi il caso della scuola in quattro righe: una per lo stato di fatto, una per l'identificazione catastale, una per la gestione patrimoniale, una per l'aggiornamento dei sistemi. Ogni riga deve dire fonte usata, limite della fonte e decisione successiva. Se scrivi che "il sistema si aggiorna", la risposta è incompleta: devi specificare quale sistema, dopo quale verifica e con quale evidenza.

## ▣ Verifica dopo i nuclei

### Quiz 1

Quale frase descrive meglio un dato tecnico utilizzabile da un ente?

A. Un file recente, purché prodotto con software professionale.
B. Un'informazione collegata a oggetto, fonte, data, metodo, qualità, versione e scopo.
C. Una rappresentazione grafica più dettagliata delle altre.
D. Un documento archiviato nel sistema informatico dell'ente.

**Risposta corretta:** B. Il dato tecnico non coincide con il file: è utilizzabile solo se si conoscono contesto, origine, qualità e funzione della decisione che deve sostenere.

### Quiz 2

Nel BIM, quale distinzione è essenziale?

A. Modello informativo, render, elaborati e documenti non hanno la stessa funzione.
B. Il modello sostituisce sempre tavole e relazioni.
C. Il software scelto determina automaticamente la validità del processo.
D. Il caricamento nell'ambiente di condivisione equivale ad approvazione.

**Risposta corretta:** A. Il BIM è gestione informativa; modello, elaborati, documenti, stati e verifiche restano distinti.

### Quiz 3

Una sovrapposizione GIS mostra un edificio dentro un perimetro. Che cosa puoi concludere subito?

A. L'edificio è certamente vincolato.
B. Il perimetro non ha valore perché è solo digitale.
C. Esiste una possibile relazione spaziale da verificare con fonte, data, scala, metadati e disciplina.
D. La mappa catastale deve essere aggiornata automaticamente.

**Risposta corretta:** C. Il GIS aiuta l'analisi, ma la conclusione richiede controllo della fonte e del quadro applicabile.

### Quiz 4

Perché una nuvola di punti non è già un modello informativo?

A. Perché contiene troppe coordinate.
B. Perché deve essere controllata, interpretata e arricchita secondo un requisito informativo.
C. Perché non può mai essere usata negli enti pubblici.
D. Perché vale solo per edifici nuovi.

**Risposta corretta:** B. La misura geometrica è una base; il modello informativo richiede organizzazione, attributi, controlli e finalità.

### Quiz 5

Quale affermazione è corretta sul catasto?

A. La visura catastale prova definitivamente la proprietà.
B. La planimetria catastale prova lo stato legittimo.
C. Catasto, pubblicità immobiliare, stato di fatto, titolo e stato legittimo hanno funzioni diverse.
D. La mappa catastale coincide sempre con il rilievo.

**Risposta corretta:** C. Il catasto identifica e descrive immobili per funzioni proprie, ma non sostituisce atti, diritti, rilievo e verifiche edilizie.

### Quiz 6

Qual è l'errore principale nell'integrazione tra BIM, GIS, catasto, inventario e AINOP?

A. Usare identificativi comuni.
B. Conservare fonte e versione dei dati.
C. Pensare che i sistemi si aggiornino automaticamente dopo una decisione.
D. Registrare i conflitti tra archivi.

**Risposta corretta:** C. L'integrazione richiede regole, responsabilità e aggiornamenti espliciti; l'automatismo non va promesso.

### Caso ragionato: riconciliare i dati di una scuola

Una scuola comunale deve entrare in un piano di riqualificazione. Il GIS segnala una possibile interferenza; la mappa catastale non coincide con il rilievo; il modello deriva dal progetto ma non contiene dati manutentivi; l'inventario assegna il bene a un responsabile cessato; AINOP contiene dati dell'opera da verificare.

La soluzione non è scegliere il documento più recente. Il tecnico separa collocazione territoriale, stato osservato, identificazione catastale, gestione patrimoniale e aggiornamento dell'opera pubblica. Ogni risposta indica fonte, limite e archivio da aggiornare.

### Domanda da commissario

Come si integrano BIM, GIS, catasto, inventario e AINOP nella gestione di un bene pubblico?

Risposta attesa: si assegna a ogni sistema la propria funzione, si usano identificativi coerenti, si verificano fonte, qualità e versione, si registrano i conflitti e si aggiorna il sistema competente. L'integrazione è un processo governato, non un effetto automatico della tecnologia.

### Domanda-trappola

Se planimetria catastale e modello BIM coincidono, l'immobile è automaticamente conforme?

No. La coincidenza geometrica è un indizio, ma non sostituisce titolo, stato dei luoghi, stato legittimo e verifiche urbanistico-edilizie.

### Errore tipico

L'errore più frequente è trattare il file più recente come fonte assoluta. La data conta, ma va letta insieme a funzione, autore, metodo, approvazione, qualità e versione.

### Mini-esercizio

Associa ogni conflitto alla prima verifica corretta: coordinate senza sistema dichiarato; planimetria catastale non allineata al rilievo; modello privo di dati manutentivi; inventario con responsabile cessato.

Soluzione: coordinate con sistema e metadati; planimetria confrontata con funzione catastale, rilievo e documenti; modello integrato con attributi verificati; inventario aggiornato nella responsabilità.

### Checklist

- Il bene è identificato in modo univoco.
- Fonte, autore, data, metodo, qualità e versione sono noti.
- BIM, GIS, rilievo, catasto e inventario non sono confusi.
- Catasto, pubblicità immobiliare, stato di fatto, titolo e stato legittimo restano distinti.
- Regime del bene, uso, responsabile e consistenza sono verificati.
- I conflitti tra fonti sono registrati, non cancellati.

### Riferimenti essenziali

Riferimenti: D.Lgs. 36/2023, art. 43 e Allegato I.9; D.M. 560/2017 e 312/2021; D.Lgs. 32/2010 e Linee guida RNDT AgID; funzioni catastali e ipotecarie dell'Agenzia delle entrate; Codice civile sui beni pubblici; AINOP.
