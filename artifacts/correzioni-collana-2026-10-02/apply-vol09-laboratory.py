from pathlib import Path
import importlib.util,re
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-laboratorio-soluzioni-verificate-2026-10-03.md'
slug='14-laboratorio-atti-casi-simulazioni';t=u.read(slug)
t=t.replace('Se manca il valore dell\'affidamento, non si inserisce una soglia.','Se manca il valore dell’affidamento, non si inventa un importo; si possono però richiamare le soglie di legge note per spiegare quali percorsi dipendano dal dato mancante.')
t=t.replace('Ho evitato soglie, termini, versioni o istruzioni non presenti nella traccia e non verificati.','Ho applicato soglie e termini normativi pertinenti, distinguendoli dagli importi e dalle date fattuali che la traccia deve fornire.')
t=t.replace('La milestone riguarda un risultato o uno stato di avanzamento definito dagli atti applicabili.','La milestone è un traguardo qualitativo definito dagli atti applicabili; il target esprime un risultato quantitativo.')
cases={
1:'''### Simulazione 1 - Dal fabbisogno alla programmazione

**Traccia.** Il Comune Alfa deve acquisire un servizio digitale per cinque sportelli. Nel 2025 sono stati gestiti 12.000 appuntamenti, con 900 chiamate mensili per prenotazioni o modifiche. Il contratto attuale termina fra sei mesi e non contiene un’opzione di rinnovo. La nuova acquisizione prevede 144.000 euro per due anni, un’opzione di prosecuzione di 72.000 e ulteriori prestazioni opzionali per 18.000. Importi al netto dell’IVA; niente lotti separati. L’ente ha risorse e una centrale qualificata disponibile.

**Consegna — 25 minuti.** Redigi una nota di fabbisogno, calcola il valore e individua programmazione, procedura e verifiche preliminari. Motiva perché non basta «rinnovare al precedente fornitore».

#### Soluzione svolta

La nota può aprirsi così: «Il servizio deve consentire prenotazione, modifica e annullamento degli appuntamenti dei cinque sportelli, notifiche agli utenti e report per ufficio. La domanda rilevata è di 12.000 appuntamenti annui; il carico telefonico richiede di misurare quante operazioni possono essere eseguite autonomamente dagli utenti. Il nuovo sistema deve prevedere migrazione dei dati, accessibilità, assistenza e prove di accettazione».

Il valore stimato comprende le opzioni: **144.000 + 72.000 + 18.000 = 234.000 euro**. Non si usa il solo biennio iniziale per scegliere la procedura. L’acquisizione supera 150.000 euro e rientra nel programma triennale degli acquisti; nel 2026–2027 supera anche la soglia di 216.000 euro per i servizi ordinari delle amministrazioni subcentrali. Non è quindi un affidamento diretto sotto 140.000 euro.

Si programma l’acquisto, si assegna il CUI e si avvia un percorso ordinario tramite soggetto qualificato, per esempio una procedura aperta. Il RUP verifica prima gli obblighi e gli strumenti Consip applicabili ai servizi informatici: se ricorrono le condizioni di una deroga, devono essere istruite e autorizzate secondo il capitolo 7. La scadenza del contratto non crea un rinnovo inesistente. I sei mesi disponibili vanno usati per gara, transizione, test e avvio; un’eventuale necessità successiva non rende automatiche proroghe o affidamenti all’uscente.

**Evidenze da consegnare:** calcolo completo del valore, nota dei cinque sportelli, programma, verifica strumenti d’acquisto, accordo con la centrale e cronoprogramma. Riferimenti: capitoli 2, 3 e 7; artt. 14, 17, 37 e 62 del Codice.

**Controllo della risposta:** attribuisci i 2 punti sui fatti solo se hai incluso entrambe le opzioni; per i 3 punti normativi servono soglie pertinenti, programma e percorso ordinario. Una motivazione basata soltanto sulla buona esperienza con l’uscente non risolve la traccia.

''',
2:'''### Simulazione 2 - Decisione di avvio e requisiti tecnici

**Traccia.** Un Comune acquista arredi interni per 90.000 euro netti. Nell’ipotesi non esistono convenzioni obbligatorie o vincoli di aggregazione pertinenti; la categoria è disponibile sul MePA. L’ufficio propone il fornitore Beta, mai affidatario di questa categoria presso l’ente, con esperienze documentate adeguate. L’offerta comprende una garanzia di sette anni. Il capitolato richiama il DM 23 giugno 2022 n. 254 e richiede consegna e montaggio in trenta giorni.

**Consegna — 20 minuti.** Predisponi lo schema essenziale della decisione e una matrice di tre requisiti. Non inventare punteggi se la procedura non prevede una competizione qualitativa.

#### Soluzione svolta

L’importo consente l’affidamento diretto di forniture ai sensi dell’articolo 50, comma 1, lettera b. Per il Comune l’acquisto di beni e servizi da 5.000 euro e sotto la soglia UE richiede il ricorso al mercato elettronico o agli strumenti ammessi dalla legge 296/2006, articolo 1, comma 450: nella traccia si utilizza il MePA. La possibilità di affidare direttamente non elimina motivazione, esperienza idonea, verifiche dei requisiti e congruità della spesa.

La decisione ai sensi dell’articolo 17, comma 2, identifica oggetto, importo, contraente, ragioni della scelta, requisiti generali e quelli speciali eventualmente necessari. I controlli non sono sostituibili dal regime semplificato dell’articolo 52, che riguarda gli affidamenti inferiori a 40.000 euro. Il fascicolo collega preventivo, esperienze, esito dei controlli, disponibilità delle risorse, CIG e documenti di acquisto.

| Requisito | Prova | Controllo |
|---|---|---|
| Garanzia offerta di sette anni, almeno cinque obbligatori | Documento scritto, contatti e condizioni dei ricambi | Coerenza con offerta e criterio 4.2.2 |
| Ritiro imballaggi | Dichiarazione di destinazione e accordi previsti | Verbale alla consegna o gestione del ritiro differito |
| Consegna e montaggio entro trenta giorni | Ordine, calendario e verbale | Data effettiva e completezza della prestazione |

La matrice è parziale rispetto all’intero CAM: gli altri criteri pertinenti vanno anch’essi inseriti. I sette anni offerti entrano nel contratto; in questa procedura non si attribuiscono automaticamente i punti di una griglia OEPV che non è stata prevista. Riferimenti: capitoli 4, 5, 7 e 12.

**Controllo della risposta:** la soluzione deve contenere tutti gli elementi della decisione, distinguere minimo e impegno migliorativo e non usare la semplificazione sotto 40.000 euro per un acquisto di 90.000.

''',
3:'''### Simulazione 3 - Affidamento sotto soglia e operatore uscente

**Traccia.** Il Comune propone un nuovo affidamento di pulizia da 8.000 euro netti all’uscente. Settore e fascia di valore coincidono con il contratto precedente. L’ufficio motiva con il servizio soddisfacente e uno sconto del 3%. Sono documentati altri operatori idonei sul mercato elettronico; non risultano particolarità del mercato o effettiva assenza di alternative. Non ricorre alcuna diversa deroga alla rotazione.

**Consegna — 15 minuti.** Scrivi una proposta al dirigente che concluda se l’istruttoria consenta la scelta indicata.

#### Soluzione svolta

La proposta, nelle condizioni date, è di **non procedere al riaffidamento all’uscente**. Il valore consente l’affidamento diretto, ma la rotazione dell’articolo 49 opera nel perimetro descritto. La deroga per affidamenti inferiori a 5.000 euro non riguarda un contratto di 8.000. Il buon esito e lo sconto non dimostrano, da soli, i presupposti della deroga del comma 4; la traccia attesta invece l’esistenza di alternative idonee.

La nota può concludere: «Si propone di individuare altro operatore idoneo attraverso lo strumento elettronico applicabile, documentando esperienze, adeguatezza della prestazione e congruità del prezzo. L’affidamento diretto non richiede di trasformare ogni confronto istruttorio in una gara, ma la scelta deve essere motivata e rispettare la rotazione».

Il nuovo operatore rende le dichiarazioni richieste; per l’importo inferiore a 40.000 euro si applica il controllo dell’articolo 52 secondo le modalità predeterminate dall’ente. Il RUP conserva l’esito e gestisce le conseguenze se emergono requisiti mancanti. Non si divide artificialmente il servizio in due affidamenti da 4.000 per rientrare nella deroga. Riferimenti: capitoli 3 e 4; artt. 49, 50 e 52.

**Controllo della risposta:** la conclusione è determinata dai fatti, non un generico «dipende». Per il punteggio pieno occorrono 8.000 rispetto a 5.000, insufficienza dei motivi addotti, presenza di alternative e proposta praticabile.

''',
4:'''### Simulazione 4 - Procedura digitale con dato incoerente

**Traccia.** Una procedura ha due lotti. Per comodità didattica i codici sono chiamati CIG-A e CIG-B: non sono codici reali. La ricevuta della PAD e la registrazione BDNCP associano il lotto A a CIG-A. La determina e la bozza d’ordine del lotto A riportano invece CIG-B, copiato dal lotto B. Non è ancora stata emessa fattura. Importi, oggetti e aggiudicatari risultano corretti.

**Consegna — 15 minuti.** Prepara una nota di rettifica e cinque controlli conseguenti.

#### Soluzione svolta

Si ricostruisce l’associazione corretta lotto–CIG dalle ricevute e dalle registrazioni, senza scegliere il documento più recente per abitudine. Qui i dati consentono di individuare un errore materiale nella determina e nella bozza d’ordine: non emerge la necessità di creare un nuovo CIG.

La proposta al soggetto competente è di rettificare il solo riferimento errato della determina, indicando atto originario, lotto interessato, codice da sostituire, codice corretto e fonte del riscontro. La versione originaria resta conservata; l’atto di rettifica spiega che oggetto, importo e contraente non cambiano. La bozza d’ordine viene corretta prima dell’emissione e collegata alla rettifica.

I cinque controlli sono: corrispondenza PAD–BDNCP; corretta associazione nei documenti del lotto A; assenza di alterazioni al lotto B; allineamento delle comunicazioni e degli adempimenti pubblicitari coinvolti; indicazione del codice corretto al fornitore per fattura e pagamento. Il fascicolo conserva ricevute, segnalazione, atto e versione dell’ordine. Se la ricostruzione mostrasse invece un errore nei sistemi, si attiverebbe il percorso di correzione della piattaforma con relativa traccia.

Riferimenti: capitoli 6 e 11; ciclo digitale del Codice e legge 136/2010. **Controllo della risposta:** non basta «correggo il campo»; servono competenza, atto, collegamento ai due lotti e verifica degli effetti successivi.

''',
5:'''### Simulazione 5 - Esecuzione e non conformità

**Traccia.** Un contratto di fornitura, valore netto 100.000 euro, prevede un sistema unitario completo e funzionante entro il giorno T. Alla verifica del giorno T manca una componente essenziale. Il sistema diventa completo dieci giorni dopo. Il ritardo è imputabile all’esecutore; non ricorrono cause di sospensione o giustificazioni. Il contratto stabilisce una penale giornaliera dell’1 per mille del valore netto, entro il limite del 10%. Il fornitore chiede subito il pagamento integrale.

**Consegna — 20 minuti.** Scrivi il verbale al giorno T e il successivo prospetto di calcolo, distinguendo accertamento e decisione sulla penale.

#### Soluzione svolta

Il verbale identifica contratto, data, presenti, prestazione attesa, documenti esaminati e componente mancante. Registra che il sistema non è ancora completo e funzionante e che non può essere attestata l’integrale conformità. Si descrive la verifica effettuata, si comunica la contestazione all’esecutore secondo il contratto e si richiede il completamento, fissando il controllo successivo. Non si certifica una prestazione completa solo perché è stata presentata la fattura.

Al completamento, il verbale successivo documenta la data e gli esiti dei test. La penale teorica è **100.000 × 0,001 × 10 = 1.000 euro**. Il limite complessivo è **10.000 euro**; l’importo calcolato non lo supera. L’aliquota contrattuale rientra nell’intervallo dell’articolo 126, da 0,5 a 1,5 per mille giornaliero. La proposta di applicazione segue istruttoria, contraddittorio e competenza previsti; non nasce dalla sola moltiplicazione.

La liquidazione considera prestazione verificata, penale adottata e altre condizioni del pagamento. Non si conclude automaticamente che il contratto debba essere risolto né si paga integralmente al giorno T una prestazione essenziale incompleta. Riferimento: capitolo 8, artt. 116, 125 e 126.

**Controllo della risposta:** distinguere i due verbali e le due date vale quanto il calcolo. «1% al giorno» produce 10.000 euro ed è errato: 1 per mille è 0,1%.

''',
6:'''### Simulazione 6 - Accesso dopo aggiudicazione

**Traccia.** Procedura aperta sopra soglia UE con sei concorrenti, senza eccezioni al termine dilatorio. L’ultima comunicazione dell’aggiudicazione è inviata al giorno 0. Il terzo classificato, non definitivamente escluso, chiede l’offerta dell’aggiudicatario. La decisione comunicata al giorno 0 dispone un oscuramento motivato per segreti tecnici. Il concorrente intende contestare sia l’oscuramento sia l’aggiudicazione. La numerazione relativa serve a confrontare i termini; non è un calendario processuale reale.

**Consegna — 20 minuti.** Costruisci la timeline e indica cosa deve essere già disponibile digitalmente.

#### Soluzione svolta

Ai sensi dell’articolo 36, l’offerta dell’aggiudicatario, i verbali e gli atti e dati presupposti all’aggiudicazione sono resi disponibili sulla piattaforma ai candidati e offerenti non definitivamente esclusi, con i limiti applicabili. Inoltre, fra i primi cinque classificati opera la disponibilità reciproca delle rispettive offerte. Non si parte quindi dall’idea che ogni documento richieda una nuova istanza ordinaria e trenta giorni di attesa.

| Termine relativo | Questione da presidiare |
|---|---|
| Giorno 0 | Comunicazione, disponibilità documenti e decisione sull’oscuramento |
| Entro 10 giorni | Notifica e deposito dell’impugnazione della decisione sui segreti ai sensi dell’art. 36 |
| Entro 30 giorni, secondo la decorrenza dell’art. 120 c.p.a. | Eventuale ricorso contro l’aggiudicazione |
| Dopo il decorso di 32 giorni dall’ultima comunicazione | Prima stipula consentita dal termine dilatorio, salvo ulteriori impedimenti |

Il funzionario distingue i due oggetti di contestazione; non attende trenta giorni per risolvere la questione soggetta al termine speciale di dieci. La stazione appaltante motiva la tutela del segreto nei limiti di legge: la formula «tutta l’offerta è riservata» non basta. L’eventuale ricorso con domanda cautelare può determinare l’ulteriore impedimento alla stipula dell’articolo 18, comma 4. La sola scadenza dei trentadue giorni non prova quindi che si possa stipulare comunque.

Riferimento: capitolo 9, artt. 18, 35 e 36 del Codice e art. 120 c.p.a. **Controllo della risposta:** servono disponibilità automatica, primi cinque, distinzione 10/30/32 e possibile blocco cautelare. Non usare il vecchio termine di trentacinque giorni.

''',
7:'''### Simulazione 7 - PNRR e target a rischio

**Traccia.** Il report è datato 25 agosto 2026. Nell’esercizio il target richiede cento sportelli digitali funzionanti entro il 31 agosto 2026. Sono state consegnate cento postazioni, ma soltanto novantadue superano i test. La spesa prevista è stata interamente registrata. Le otto postazioni residue possono essere riparate entro il 28 agosto e testate il 29–30 agosto; tale previsione è ancora da confermare con il fornitore. Il caso è collocato prima della scadenza e non introduce una proroga.

**Consegna — 20 minuti.** Redigi lo status report e la richiesta di decisione.

#### Soluzione svolta

Il report distingue: consegne 100/100; risultato verificato **92/100, pari al 92%**; otto postazioni non funzionanti; avanzamento finanziario registrato 100%. Il target non è raggiunto. Non lo si trasforma in una milestone qualitativa e non si usa il dato finanziario per attestarlo.

Il referente allega elenco delle postazioni, verbali di test e difetti. Chiede conferma del calendario di riparazione, assegna responsabile e data al controllo delle otto unità e segnala all’amministrazione titolare il rischio secondo le istruzioni della misura. Il piano prevede riparazione entro il 28 e test il 29–30, con esito documentato; l’esistenza del piano non equivale al risultato.

Il 31 agosto si registra l’esito effettivo. Se tutte le unità superano i test, la documentazione deve dimostrare il raggiungimento tempestivo. Se alcune restano non funzionanti, il report conserva il numero reale e attiva la gestione delle conseguenze con l’amministrazione titolare. La scadenza di pagamento UE al 31 dicembre non sposta il termine di conseguimento dei risultati RRF. Il caricamento in ReGiS deve corrispondere alle evidenze e allo stato dei controlli, distinguendo inserimento, prevalidazione e validazione.

Riferimenti: capitoli 10 e 11. **Controllo della risposta:** target 92%, piano con responsabile e prove, assenza di attestazioni anticipate o proroghe inventate. Un report senza decisione richiesta descrive il problema ma non ne organizza la gestione.

''',
8:'''### Simulazione 8 - Rendicontazione e doppio finanziamento

**Traccia.** Una spesa ammissibile di 100.000 euro, integralmente pagata, compare nella domanda al programma A per 60.000 euro e in quella al programma B per altri 60.000. Si tratta dello stesso costo; le quote sono sovrapposte per la parte eccedente. Le regole consentono il cofinanziamento con quote distinte. Le domande non sono ancora state liquidate. CUP e CIG sono corretti.

**Consegna — 15 minuti.** Calcola l’anomalia e scrivi una proposta di rettifica.

#### Soluzione svolta

Le richieste totalizzano **120.000 euro su un costo di 100.000**: l’eccedenza sovrapposta è di **20.000 euro**. Codici e pagamento corretti non eliminano il problema. La proposta è bloccare l’ulteriore lavorazione del dato errato e rettificare, secondo le procedure dei programmi, la domanda B a 40.000 euro, mantenendo A a 60.000 e identificando le quote distinte.

Il prospetto contiene fattura, costo ammissibile, quota A, quota B, totale, pagamento e riferimenti alle domande. Si conservano versione originaria, motivazione, autorizzazione e ricevuta della rettifica. Poiché nell’ipotesi il cumulo è consentito e le domande non sono liquidate, la ripartizione 60.000/40.000 può ricondurre la richiesta al costo effettivo. Non basta abbassare una cifra senza ricostruire l’imputazione.

Se il cumulo fosse vietato, la soluzione andrebbe modificata; se le somme fossero già erogate, occorrerebbe gestire anche rettifica finanziaria e recupero. L’identità della fattura in due dossier non dimostra da sola un illecito: in questo caso è la sovrapposizione delle quote, specificata nella traccia, a fondare la correzione. Riferimento: capitolo 11, art. 9 del regolamento RRF.

**Controllo della risposta:** calcolo 20.000, correzione 60.000/40.000 subordinata al cumulo ammesso e traccia delle versioni. Non concludere automaticamente che l’intera spesa sia inesistente o che sia provata una frode intenzionale.

''',
9:'''### Simulazione 9 - DNSH e CAM

**Traccia.** Una gara per arredi applica il DM 23 giugno 2022 n. 254. La garanzia minima è di cinque anni e il criterio di estensione assegna al massimo otto punti secondo il punto 4.3.8. Il concorrente Alfa offre sette anni, Beta tre anni. Alfa allega soltanto una brochure che definisce i prodotti «ecologici»; il documento di garanzia e le prove richieste devono essere esaminati secondo gli atti di gara. L’acquisto appartiene a un progetto PNRR con obblighi DNSH.

**Consegna — 20 minuti.** Distingui ammissibilità, punteggio, mezzi di prova e verifica DNSH.

#### Soluzione svolta

Sette anni corrispondono a due anni aggiuntivi: il punteggio di Alfa è **0,50 × 8 = 4 punti**, subordinatamente alla dimostrazione dell’impegno secondo la gara e alla conformità complessiva. La brochure non sostituisce il documento scritto con durata, condizioni dei ricambi e contatti richiesti. Si accerta la natura della carenza e si applicano i limiti delle integrazioni ammesse; non si inventa dopo la scadenza un contenuto tecnico che l’offerta non aveva.

Beta propone tre anni, quindi non rispetta il minimo di cinque. Assegnargli semplicemente zero punti lascerebbe irrisolta una non conformità sostanziale. La stazione appaltante applica gli atti e la disciplina, senza trasformare il soccorso istruttorio in una modifica dell’offerta tecnica.

La matrice dei controlli separa almeno garanzia, ricambi e ritiro degli imballaggi, con la relativa prova e il momento del controllo. Per il DNSH si ricostruiscono misura, attività e prescrizioni: la conformità ai tre criteri CAM esaminati non prova automaticamente il rispetto dell’intero decreto né dei sei obiettivi ambientali del progetto. Riferimento: capitolo 12.

**Controllo della risposta:** 4 punti ad Alfa non significa conformità già dimostrata; zero punti a Beta non rende ammissibile la sua durata. Deve inoltre emergere la distinzione CAM/DNSH.

''',
10:'''### Simulazione 10 - Project management e recupero del ritardo

**Traccia.** Si usa la rete del capitolo 13: A dura 2 giorni; B, dopo A, 4; C, dopo A, 3; D, dopo B e C, 2; E, dopo B, 1; F, dopo D ed E, 1. La baseline dura 9 giorni lavorativi. L’ambiente di test C subirà un ritardo certo di due giorni rispetto alla durata prevista. D contiene test obbligatori e non può essere abbreviata arbitrariamente. È disponibile un intervento che limita a un giorno il ritardo di C, con costo aggiuntivo da autorizzare.

**Consegna — 25 minuti.** Calcola l’effetto sulla fine del progetto e compila issue log, rischio e richiesta di decisione.

#### Soluzione svolta

C ha un giorno di margine: nella baseline termina al giorno 5, mentre B termina al giorno 6. Se la durata di C passa da 3 a 5, termina al giorno 7; D può iniziare soltanto allora e termina al giorno 9; F termina al giorno 10. Il ritardo del progetto è quindi **un giorno**, non due. La dipendenza di D da entrambe le attività impedisce di iniziare i test completi quando manca l’ambiente.

| Registro | Voce compilata |
|---|---|
| Issue log | I-01: indisponibilità già accertata dell’ambiente; C termina al giorno 7; responsabile tecnico incaricato del ripristino |
| Risk register | R-01: possibili ulteriori guasti o test negativi dopo il ripristino; monitoraggio con prova di disponibilità e test |
| Decisione richiesta | Autorizzare, se ammissibile e conveniente, l’intervento che porta C a durata 4; altrimenti registrare previsione di chiusura al giorno 10 |
| Evidenza di recupero | Ambiente disponibile, esito dei test, calendario aggiornato e decisione approvata |

Con C di durata 4, B e C terminano entrambe al giorno 6: D finisce al giorno 8 e F al giorno 9. L’alternativa recupera la baseline, ma richiede l’autorizzazione competente e il controllo dei vincoli contrattuali e finanziari. Il responsabile non anticipa nel report un recupero ancora soltanto proposto. Conserva la baseline originaria per confrontare previsione, decisione e risultato.

Ridurre i test senza presupposti sarebbe un diverso intervento sulla qualità e sugli obblighi contrattuali, non un semplice aggiustamento del calendario. Riferimento: capitolo 13 e relativo Gantt.

**Controllo della risposta:** 10 giorni senza intervento, 9 con C di durata4, distinzione issue/rischio e decisione autorizzata. La sola frase «aggiornare il Gantt» non dimostra il calcolo né la fattibilità del recupero.

'''
}
for n,body in cases.items():
 pattern=rf'### Simulazione {n} - .*?(?=### Simulazione {n+1} - |## N-TR02-|### ▣ Verifica intermedia)'
 t,count=re.subn(pattern,lambda m:body,t,flags=re.S)
 assert count==1,(n,count)
t=t.replace('## N-TR02-14-04 · Simulazione 10 - Project management e recupero del ritardo','## N-TR02-14-04 · Recupero del ritardo e verifica delle decisioni')
t=t.replace('## N-TR02-14-05 · Mini-esercizio','## N-TR02-14-05 · Autovalutazione, diario e piano di studio')
anchor='### ▣ Verifica finale - Controllo prima della prova'
t=u.replace(t,anchor,'''### Rubrica comune alle dieci simulazioni

Per confrontare tentativi diversi usa la stessa scala. È una rubrica di allenamento, non quella di un concorso specifico: se il bando pubblica criteri propri, applica quelli nella simulazione della prova.

| Dimensione | Punti | Evidenza per il massimo |
|---|---|---|
| Fatti e calcoli | 0–2 | Dati decisivi corretti, nessuna ipotesi nascosta, calcolo verificabile |
| Regola e applicazione | 0–3 | Norma pertinente e conseguenza corretta nel caso |
| Output e proposta | 0–3 | Documento richiesto riconoscibile e conclusione motivata |
| Evidenze e seguito | 0–2 | Prove, responsabile e controllo successivo identificati |

Assegna zero quando la dimensione manca o contraddice il caso. Per una dimensione da due punti assegna uno se è presente ma incompleta. Per una da tre assegna uno se soltanto nominata, due se sviluppata con un’omissione rilevante, tre se completa. Non compensare una soglia sbagliata con molte citazioni corrette: la soluzione del percorso rimane errata. Un risultato di almeno 7/10 può essere il tuo obiettivo iniziale; non equivale a una soglia ufficiale di idoneità.

Per l’orale usa le stesse quattro dimensioni in tre minuti: trenta secondi per i fatti, un minuto per regola e applicazione, un minuto per proposta, trenta secondi per prove e seguito. Registra l’audio o chiedi a un compagno di segnare le omissioni. La ripetizione deve variare almeno un dato: 8.000 diventa 4.000, il cumulo ammesso diventa vietato, la durata di C aumenta di un solo giorno. Poi spiega che cosa cambia e che cosa resta uguale.

### Diario degli errori compilabile

Una riga deve descrivere un errore recuperabile, non un giudizio sulla persona. Scrivere «non so gli appalti» non indica quale esercizio ripetere. Scrivere «ho escluso l’opzione dal valore stimato» porta a un’azione precisa.

| Campo | Esempio compilato |
|---|---|
| Data, prova e punteggio | 3 ottobre, simulazione1, 5/10 |
| Errore osservato | Ho confrontato144.000 con la soglia, ignorando90.000 di opzioni |
| Causa | Ho confuso corrispettivo iniziale e valore stimato |
| Regola corretta | Art.14: includere opzioni; totale234.000 |
| Recupero | Rileggere cap3 e risolvere due casi con durate/opzioni diverse |
| Riprova | Dopo2giorni: totale e procedura senza consultare la soluzione |
| Esito | Corretta/da ripetere, con nuova data |

Compila ora una tua scheda: **prova e data** __________; **errore** __________; **causa** __________; **regola e capitolo** __________; **azione** __________; **data della riprova** __________; **esito** __________. Se la riprova è ancora errata, modifica il recupero: spiegazione a voce, tabella di confronto o caso più semplice, non soltanto un’altra lettura passiva.

### Piano a 30, 60 o 90 giorni

Il piano comprende trenta unità. Nel percorso da30giorni svolgi un’unità al giorno; in60giorni distribuisci ciascuna unità su due giorni; in90giorni su tre. Le unità non sono ore fisse: stima il carico leggendo la prima e assegnando tempo disponibile realistico. Nei percorsi più lunghi separa studio, esercizio e riprova; non aggiungere automaticamente materie estranee al bando.

| Unità | Lavoro principale | Prodotto richiesto |
|---|---|---|
| 1–3 | Bando, diagnosi, cap1–2 | Mappa materie, ruoli e calendario personale |
| 4–7 | Cap3–5 | Valori, procedure, requisiti e una griglia di gara svolta |
| 8–10 | Cap6–7 | Sequenza digitale e scelta motivata dello strumento |
| 11–14 | Cap8–9 | Verbale esecutivo, calcolo penale e timeline dei rimedi |
| 15–18 | Cap10–12 | Report PNRR, riconciliazione spesa e matrice ambientale |
| 19–21 | Cap13 | WBS, dipendenze, rischio e decisione di recupero |
| 22–26 | Due simulazioni al giorno-unità | Dieci elaborati corretti con la rubrica |
| 27–29 | Recupero dei tre errori più ricorrenti | Riprova con dati variati e orale cronometrato |
| 30 | Prova completa secondo il bando | Risultato, errori residui e programma dell’ultimo ripasso |

Per il profilo appalti/RUP dedica gli approfondimenti delle unità27–29 soprattutto a cap3–9; per procurement operativo a cap3–8, senza saltare valore e requisiti; per PNRR a cap10–12 e al collegamento con gara ed esecuzione; per project management a cap10–13 e alle decisioni sui vincoli. Questa è una distribuzione del ripasso, non un’autorizzazione a escludere materie presenti nel programma del tuo concorso.

La sera registra unità conclusa, minuti effettivi e un errore. Ogni tre unità verifica se il tempo stimato era realistico. Se resti indietro, riduci le ripetizioni già corrette e conserva i nuclei ancora deboli; non segnare studiato un capitolo soltanto aperto. Nel percorso da30giorni può servire un impegno quotidiano maggiore: se incompatibile con il tempo disponibile, scegli un calendario sostenibile e dai priorità in base al bando.

'''+anchor)
t+='''
### Riferimenti e uso degli strumenti nel volume

Per valori, procedure e strumenti: capitoli3–7 e d.lgs.36/2023, artt.14,17,37,49–52,62 e108. Per esecuzione e rimedi: capitoli8–9, artt.18,35–36,116,125–126 e art.120 c.p.a. Per finanziamenti: capitoli10–12, regolamento2021/241, artt.5,9,22 e24, e istruzioni della misura; per arredi DM23giugno2022n.254. Per WBS e dipendenze: capitolo13, Guida PM²3.1 e diagramma svolto. Le dieci tracce sono originali e non riproducono quesiti ufficiali; importi e soggetti sono didattici.
'''
u.save(slug,t,['V09-35','V09-36'],u.REF);u.record()
