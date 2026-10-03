from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-gara-requisiti-verifica-2026-10-03.md'
slug='04-progettazione-gara-documenti';t=u.read(slug)
t=u.replace(t,'Quando lavori su una procedura reale, non usare questo capitolo per fissare soglie, termini, formule di punteggio o istruzioni operative di piattaforma. Questi dati vanno verificati nel Codice dei contratti pubblici vigente, nei documenti istituzionali applicabili e negli atti dell\'ente.','Il capitolo presenta le regole del d.lgs. 36/2023 verificate al 3 ottobre 2026. Le soglie e la scelta della procedura sono sviluppate nei capitoli 3 e 5; il funzionamento delle piattaforme nel capitolo 6. Per applicarle a una gara reale occorre controllare eventuali modifiche successive e le condizioni dei suoi documenti.')
anchor='### Il fascicolo di gara\n'
t=u.replace(t,anchor,'''### Decisione di contrarre: contenuto e caso compilato

L’art. 17, comma 1, colloca la **decisione di contrarre prima dell’avvio**: individua elementi essenziali del contratto e criteri di selezione degli operatori e delle offerte. Nell’affidamento diretto il comma 2 richiede oggetto, importo e contraente, ragioni della scelta, requisiti generali e, se necessari, speciali. La decisione iniziale di una gara non va confusa con la successiva aggiudicazione: l’organo di valutazione formula la proposta, quello competente verifica e dispone l’aggiudicazione, immediatamente efficace ai sensi del comma 5. Questa non equivale ad accettazione dell’offerta né a stipulazione.

**Caso compilato: estratto didattico di decisione.** Il Comune Alfa è qualificato SF3; deve affidare assistenza e migrazione applicativa per 24 mesi, con rinnovo opzionale di 12 mesi. Il valore massimo stimato, IVA esclusa, è 234.000 euro, come calcolato nel capitolo 3. Il finanziamento è ordinario; si assume che non si tratti di un progetto di investimento pubblico e che non siano attive convenzioni obbligatorie pertinenti. I nomi e gli estremi seguenti sono dati di esercitazione.

| Parte dell’atto | Contenuto motivato |
| --- | --- |
| Presupposti | Fabbisogno degli uffici e analisi dei carichi; inserimento nel programma triennale; disponibilità del prospetto di copertura approvato; RUP nominato nel primo atto |
| Oggetto e valore | Assistenza 24 mesi a 6.000 euro/mese, rinnovo 12 mesi alle stesse condizioni, migrazione opzionale 18.000 euro: massimo 234.000 euro oltre IVA |
| Procedura | Procedura aperta, art. 71: valore oltre la soglia UE subcentrale 2026–2027; PAD certificata e pubblicità prevista, secondo capitolo 6 |
| Requisiti | Generali artt. 94–98; iscrizione pertinente; esperienze analoghe di assistenza e migrazione negli ultimi dieci anni, con livello proporzionato al volume dei dati e degli utenti descritto nel capitolato, ammettendo RTI e avvalimento nei limiti di legge |
| Aggiudicazione | Qualità/prezzo: 80 punti tecnici e 20 economici; scelta motivata da migrazione, continuità e sicurezza, non soltanto dal prezzo orario |
| Documenti approvati | Bando, disciplinare con criteri e metodo di calcolo, capitolato con livelli minimi, schema contrattuale con incorporazione degli allegati, quadro economico e copertura |
| Dispositivo | Avviare la gara; approvare gli allegati; attribuire al RUP gli adempimenti di competenza; demandare comunicazioni e flussi digitali agli incaricati; assicurare la copertura della spesa secondo il regime contabile dell’ente |

L’estratto fa vedere le scelte, ma non inventa un CIG, un capitolo di bilancio o una firma. In una prova che fornisce tali dati li riporti; se mancano, li indichi come presupposti da acquisire. Il contraente non è già scelto nell’atto iniziale della procedura aperta. In un diretto, invece, la motivazione deve identificare anche il contraente e le ragioni della sua scelta.

''' + anchor)
t=u.replace(t,"Un livello di servizio citato nel capitolato ma assente dal contratto rischia di restare una promessa senza conseguenza.","Un livello di servizio del capitolato può vincolare il contraente anche senza essere ricopiato nello schema, se il capitolato è incorporato nel contratto. Occorre controllare il richiamo agli allegati, il loro ordine in caso di contrasto e le conseguenze dell’inadempimento.")
t=u.replace(t,"Se il capitolato prevede un livello di servizio che il contratto non misura, l'amministrazione perde forza nella fase esecutiva.","Se il capitolato incorporato nel contratto prevede un livello di servizio misurabile, questo può essere vincolante senza duplicazione; mancanza di verifiche e clausole contraddittorie ne rendono invece più difficile il controllo.")
anchor='### ▣ Verifica 1 - documenti, avvio e requisiti\n'
t=u.replace(t,anchor,'''### Requisiti generali: esclusione automatica e valutazione motivata

L’**art. 94** individua le cause automatiche: determinate condanne definitive o decreti penali irrevocabili per i reati elencati, fattispecie antimafia, interdizioni e altre situazioni del comma 5, gravi violazioni fiscali o contributive definitivamente accertate del comma 6. Non basta dire “precedente penale”: occorrono reato, provvedimento e soggetto rilevante secondo i commi 1–4. La disciplina considera anche cessazione degli effetti, riabilitazione e altre condizioni espressamente previste.

L’**art. 95** comprende cause non automatiche: gravi infrazioni in materia di lavoro, sicurezza e ambiente; conflitto di interessi non diversamente risolvibile; distorsione concorrenziale non rimediabile causata dal precedente coinvolgimento; offerte imputabili a un unico centro decisionale; grave illecito professionale. Vi rientrano anche gravi violazioni fiscali o contributive non definitive nelle condizioni del comma 2. “Non automatica” non significa facoltativa: l’amministrazione deve accertare e motivare la sussistenza dei presupposti.

Per il **grave illecito professionale**, l’art. 98 richiede insieme: una delle fattispecie previste, incidenza su integrità o affidabilità, mezzi di prova adeguati. Una precedente risoluzione per inadempimento può rilevare, ma la decisione deve motivare gravità, circostanze e affidabilità, considerando anche le misure successive. Una voce di stampa, da sola, non sostituisce i mezzi richiesti dalla norma.

Il **self-cleaning** dell’art. 96 consiste nella dimostrazione di affidabilità attraverso risarcimento o impegno a risarcire, collaborazione per chiarire i fatti e misure concrete tecniche, organizzative e sul personale. Le misure devono essere sufficienti e tempestive; non autorizzano a ritardare l’aggiudicazione. Non si applica con questo regime alle violazioni fiscali/contributive dell’art. 94, comma 6, e dell’art. 95, comma 2, che hanno proprie condizioni di regolarizzazione. È inoltre precluso durante il periodo di esclusione disposto con sentenza definitiva. Non memorizzare “tre anni per tutto”: durata ed effetti variano secondo i commi 8–12 dell’art. 96.

### Requisiti speciali, FVOE, RTI e avvalimento

L’**art. 100** distingue idoneità professionale, capacità economica e finanziaria, capacità tecnica e professionale. Nei lavori da 150.000 euro si richiede la qualificazione SOA per categorie e classifiche adeguate. Per servizi e forniture l’iscrizione deve riguardare un’attività pertinente, non necessariamente identica all’oggetto. Nel regime del comma 11, applicabile fino al regolamento ivi previsto, il fatturato globale richiesto non supera il doppio del valore stimato ed è maturato nei migliori tre degli ultimi cinque anni; l’esperienza riguarda contratti analoghi negli ultimi dieci anni, anche per privati. Il massimo consentito non è automaticamente il livello da chiedere: serve proporzionalità.

L’**art. 99** richiede verifica tramite FVOE, interoperabilità e documenti pertinenti. Non si richiedono nuovamente documenti già disponibili nei casi del comma 3. Il malfunzionamento informatico non equivale a requisito posseduto: dopo trenta giorni dalla proposta, il comma 3-bis consente l’aggiudicazione previa autocertificazione sui requisiti non verificabili a causa del guasto, mantenendo l’obbligo di completare i controlli in tempo congruo. Se negativi, operano recesso e altre conseguenze previste, con pagamento delle prestazioni e rimborso delle spese nei limiti dell’utilità conseguita. La regola ordinaria rimane la verifica prima dell’aggiudicazione.

| Istituto | Come funziona | Controllo decisivo |
| --- | --- | --- |
| RTI, art. 68 | Più imprese presentano un’offerta comune; ciascuna esegue le parti dichiarate; una mandataria le rappresenta | Requisiti generali di tutti; capacità complessive e qualificazione dell’esecutore per la propria prestazione |
| RTI costituendo | Offerta firmata da tutti e impegno a conferire mandato collettivo speciale con rappresentanza | Non serve costituzione anticipata; mandato e ripartizione devono rispettare la disciplina |
| Avvalimento, art. 104 | Ausiliaria mette a disposizione risorse specifiche per partecipare o migliorare l’offerta | Contratto scritto, risorse determinate, requisiti e impegno dell’ausiliaria, uso effettivo in esecuzione |

Nel RTI la responsabilità è solidale ai sensi dell’art. 68, comma 9. Se un componente perde un requisito, l’art. 97 consente estromissione o sostituzione tempestiva alle condizioni previste, senza modifica sostanziale dell’offerta; non si elimina automaticamente tutto il raggruppamento senza esaminare tali condizioni.

Nell’avvalimento operatore e ausiliaria rispondono in solido delle prestazioni. Nei casi di autorizzazioni o titoli di cui all’art. 104, comma 3, l’ausiliaria esegue direttamente le prestazioni e si applicano le regole del subappalto. Non è ammesso usare l’avvalimento per l’iscrizione all’Albo nazionale dei gestori ambientali. Per l’avvalimento che migliora l’offerta, la partecipazione alla stessa gara anche dell’ausiliaria richiede la prova documentale di autonomia decisionale prevista dal comma 12: non basta ignorare il collegamento tra imprese.

**Caso.** Beta ha le capacità operative ma presenta un contratto di avvalimento che dice soltanto “si prestano tutti i requisiti”. Prima di considerarlo adeguato occorre verificare l’indicazione concreta delle risorse richieste dall’art. 104. Se invece il contratto idoneo esisteva con data certa prima della scadenza ma non è stato allegato, il problema documentale può rientrare nell’art. 101. Il soccorso non consente di creare dopo la scadenza un contratto prima inesistente.

''' + anchor)
anchor='Specifiche funzionali e capitolato\n'
t=u.replace(t,anchor,'''### Qualità/prezzo e minor prezzo: quando si usano

L’art. 108 impone il miglior rapporto **qualità/prezzo**, tra l’altro, per servizi sociali, ristorazione ospedaliera, assistenziale e scolastica, servizi ad alta intensità di manodopera; servizi tecnici e intellettuali da 140.000 euro; servizi e forniture tecnologici o innovativi da 140.000 euro; dialogo competitivo, partenariato per l’innovazione, appalto integrato, lavori tecnologici o innovativi e trasporto per uscite didattiche e viaggi di istruzione. Il minor prezzo può essere usato per servizi e forniture standardizzati o con condizioni definite dal mercato, ma non per superare l’obbligo relativo all’alta intensità di manodopera.

Non esiste una regola universale “70 punti qualità e 30 prezzo”. Il tetto economico del 30% riguarda i servizi ad alta intensità di manodopera e i trasporti scolastici indicati dalla norma. Per beni e servizi informatici impiegati a tutela degli interessi nazionali strategici il tetto è del 10%; negli acquisti ICT occorre comunque considerare la cybersicurezza. Criteri, pesi e metodo devono essere definiti prima della valutazione.

**Griglia svolta per il Comune Alfa.** Il caso non riguarda interessi nazionali strategici e adotta 80/20. I punteggi tecnici massimi sono: migrazione e reversibilità 25, continuità e assistenza 20, sicurezza 20, formazione e accessibilità 15. Ogni criterio è articolato nel disciplinare in elementi osservabili e livelli: insufficiente 0; minimo adeguato 0,50; completo e coerente 0,75; completo con prove verificabili di miglioramento 1. Il punteggio del criterio è peso × coefficiente; questa è una formula dell’esercizio, non una formula obbligatoria di legge.

| Criterio | Peso | Offerta A: coefficiente → punti | Offerta B: coefficiente → punti |
| --- | --- | --- | --- |
| Migrazione | 25 | 0,75 → 18,75 | 1 → 25 |
| Continuità | 20 | 1 → 20 | 0,75 → 15 |
| Sicurezza | 20 | 0,75 → 15 | 1 → 20 |
| Formazione/accessibilità | 15 | 0,50 → 7,50 | 0,75 → 11,25 |
| Totale tecnico | 80 | 61,25 | 71,25 |

Per il prezzo il caso stabilisce 20 × prezzo minimo/prezzo offerto. Su basi omogenee, A offre 190.000 e B 200.000 euro: A riceve 20 punti, B 19. Totali: **A 81,25; B 90,25**. B prevale, salvo verifica di anomalia e requisiti, pur costando di più: la qualità premiata deve diventare prestazione controllabile. La commissione non può cambiare pesi dopo avere letto le offerte. Ai sensi del comma 9, l’offerta economica indica costi della manodopera e oneri aziendali di sicurezza, salvo forniture senza posa e servizi intellettuali; non confonderli con oneri da interferenza stabiliti dalla stazione appaltante.

''' + anchor)
old="Il soccorso istruttorio, quando applicabile, appartiene a un piano diverso: riguarda integrazioni o chiarimenti su elementi della domanda nei limiti previsti, non la riscrittura sostanziale dell'offerta. In sede di studio, la prudenza è obbligatoria: non trasformare la regola generale in automatismo. Bisogna sempre verificare la disciplina vigente, il tipo di procedura e il contenuto da integrare."
t=u.replace(t,old,'''Il **soccorso istruttorio dell’art. 101** opera su domanda, DGUE e documenti amministrativi: l’amministrazione assegna **da cinque a dieci giorni** per integrazioni o sanatorie, salvo documento già nel FVOE alla scadenza. La mancata risposta nel termine comporta esclusione. Non sana identità assolutamente incerta né consente di integrare l’offerta tecnica o economica.

Garanzia provvisoria, contratto di avvalimento e impegno a conferire mandato per RTI costituendo possono essere prodotti in sanatoria solo con **data certa anteriore alla scadenza delle offerte**. È diverso il chiarimento sull’offerta: il comma 3 consente di richiederlo, sempre entro cinque–dieci giorni, ma senza cambiarne il contenuto. Il comma 4 permette al concorrente di chiedere prima dell’apertura la rettifica di un errore materiale, alle condizioni di anonimato e assenza di nuova offerta o modifica sostanziale.

**Verifica rapida.** Domanda amministrativa incompleta ma identità certa: valuta soccorso. Prezzo offerto da abbassare per superare un concorrente: non sanabile. Garanzia stipulata prima del termine ma non allegata, con data certa: producibile nei limiti dell’art. 101. Garanzia creata soltanto dopo: non si rimedia presentandola come un documento dimenticato.''')
t=u.replace(t,"Se manca il contratto, la promessa non si governa.","Se manca l’incorporazione contrattuale degli impegni, la promessa non si governa in modo coerente.")
u.save(slug,t,['V09-11','V09-12','V09-13'],u.REF);u.record()
