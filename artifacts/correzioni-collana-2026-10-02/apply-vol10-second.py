from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico');changes=[]
def load(n):
 p=next((base/'chapters').glob(f'{n:02}-*.md'));return p,p.read_text(encoding='utf8')
def before(s,anchor,body):
 assert s.count(anchor)==1,anchor
 return s.replace(anchor,body.strip()+'\n\n'+anchor)
def save(p,s):p.write_text(s,encoding='utf8');changes.append(p.as_posix())
p,s=load(8)
s=s.replace('La fase esecutiva presuppone un contratto efficace e una base tecnica definita.', 'Nel percorso ordinario la fase esecutiva segue la stipula e l’efficacia del contratto, con una base tecnica definita.')
s=before(s,'### Verbale e stato dei luoghi', '''L'art. 17, comma 8, consente però di iniziare prima della stipula per motivate ragioni; impone l'avvio anticipato quando ricorrono le ragioni d'urgenza del comma 9. Queste riguardano eventi oggettivamente imprevedibili e la necessità di evitare i pericoli individuati dalla norma, oppure un grave danno all'interesse pubblico per mancata esecuzione immediata, compresa la perdita di finanziamenti UE. Per i contratti sotto soglia, l'art. 50, comma 6, consente l'esecuzione anticipata dopo la verifica dei requisiti dell'aggiudicatario.

La motivazione e l'ordine della stazione appaltante delimitano l'avvio; l'impresa non può anticipare liberamente. Se non si stipula, opera il rimborso delle prestazioni ordinate nei limiti della disciplina. **Esempio:** l'urgenza documentata di proteggere persone da un pericolo non è equivalente alla sola preferenza dell'impresa di occupare subito il cantiere. Avvio anticipato dell'esecuzione e anticipazione del prezzo sono istituti distinti.''')
s=before(s,'### Sospensione, ripresa e ritardi', '''### Quale fattispecie di modifica?

L'art. 120 consente modifiche senza nuova gara soltanto nei casi ammessi. Le categorie principali si leggono così:

- **Clausola iniziale:** modifica già prevista da clausole chiare, precise e inequivocabili nei documenti di gara. Non basta un generico richiamo a «eventuali esigenze».
- **Prestazioni supplementari necessarie:** cambio dell'esecutore impraticabile per ragioni economiche o tecniche e tale da produrre notevoli disagi o consistente aumento dei costi.
- **Circostanze imprevedibili per una stazione diligente:** necessità sopravvenuta nelle condizioni della norma; non si può chiamare imprevedibile una carenza rilevabile con l'ordinaria istruttoria.
- **Modifiche di valore ridotto:** importo sotto la soglia UE e sotto il 15% del valore iniziale per lavori, oppure il 10% per servizi/forniture, senza alterare la natura complessiva; si considera il valore cumulato delle modifiche successive.
- **Modifiche non sostanziali:** non alterano materialmente struttura e operazione economica secondo i criteri dell'articolo. Una diversa platea di concorrenti, un indebito spostamento dell'equilibrio economico o un'estensione considerevole sono segnali da verificare, non dettagli trascurabili.

Per supplementari e circostanze imprevedibili, nei settori ordinari l'aumento di prezzo non supera il 50% del valore iniziale per ciascuna modifica; le modifiche successive non possono eludere il Codice. Il 50% è un limite, non una causa autonoma che autorizzi qualsiasi variante. Per il **quinto d'obbligo** occorre che la facoltà sia prevista nei documenti iniziali: entro un quinto la stazione può imporre aumento o diminuzione alle condizioni originarie, nei presupposti della norma. Non si deduce il potere dal solo fatto che il 20% non sia superato.

**Caso.** Lavori da 1 milione, modifica di 100.000 euro: 10%, quindi entro il limite quantitativo del 15% e sotto soglia UE; occorre ancora verificare natura complessiva, cumulo e procedimento. Modifica da 400.000 euro: non passa per il valore ridotto; il fatto che sia sotto il 50% non basta, dovendo dimostrare un'altra fattispecie ammessa.''')
s=before(s,'### Contestazioni e riserve', '''L'art. 121 distingue i soggetti. Il **DL** dispone la sospensione se circostanze speciali, temporanee e imprevedibili alla stipula impediscono che i lavori procedano utilmente a regola d'arte; redige il verbale, con l'intervento dell'esecutore se possibile, e lo trasmette al RUP entro **cinque giorni**. Il **RUP** può sospendere per ragioni di necessità o pubblico interesse. Una sospensione parziale deve individuare le attività impedite, senza arrestare automaticamente quelle utilmente eseguibili.

Cessate le cause, il RUP dispone la ripresa e indica il nuovo termine contrattuale. Se la sospensione supera un quarto della durata complessiva prevista o comunque sei mesi, l'esecutore può chiedere la risoluzione senza indennità; se la stazione si oppone, opera il ristoro dei maggiori oneri oltre quei limiti secondo la norma. La proroga chiesta dall'esecutore per cause non imputabili va richiesta con congruo anticipo rispetto alla scadenza; il RUP decide entro trenta giorni, sentito il DL. Non si confonde con una sospensione già avvenuta.

**Confronto di casi.** Un impedimento temporaneo imprevedibile che rende impossibile una lavorazione chiama il DL a verificare l'art. 121. Una sospensione necessaria per pubblico interesse riguarda il RUP. Una singola lavorazione con pericolo grave e imminente direttamente riscontrato chiama invece il potere immediato del CSE descritto sotto: finalità e presupposti sono diversi.''')
s=before(s,'### PSC, POS e coordinamento in esecuzione', '''Quando è prevista la presenza di **più imprese esecutrici, anche non contemporanea**, l'art. 90 D.Lgs. 81/2008 richiede al committente o responsabile dei lavori la nomina del **CSP contestualmente all'affidamento della progettazione** e del **CSE prima dell'affidamento dei lavori**. Se dopo l'affidamento a una sola impresa subentrano altre imprese esecutrici, va nominato il CSE; nel caso dell'art. 90, comma 5, questi redige anche PSC e fascicolo nei termini dell'art. 92, comma 2.

L'eccezione per lavori privati senza permesso e sotto 100.000 euro riguarda la nomina del CSP: le sue funzioni sono svolte dal CSE. Non esenta da coordinamento e obblighi di sicurezza. Una sola impresa con lavoratori autonomi non è automaticamente «più imprese esecutrici»: si qualifica l'organizzazione reale, verificando comunque gli obblighi pertinenti.''')
s=s.replace('In tutti questi casi l\'intervento materiale non può precedere l\'istruttoria. Occorre accertare e qualificare il fatto, individuare la competenza, formalizzare la decisione e quindi eseguirla.', '''La soluzione definitiva e la modifica contrattuale seguono l'istruttoria e le autorizzazioni necessarie. **Le cautele urgenti non attendono quella conclusione:** il CSE, in caso di pericolo grave e imminente direttamente riscontrato, sospende le singole lavorazioni fino alla verifica degli adeguamenti dell'impresa, ai sensi dell'art. 92, comma 1, lett. f), D.Lgs. 81/2008. Si documentano subito evidenze, lavorazioni interessate, comunicazioni e condizioni della ripresa; DL e RUP gestiscono gli effetti contrattuali di propria competenza. L'intervento di sicurezza immediato non autorizza, da solo, una variante o un maggior pagamento.''')
save(p,s)
p,s=load(9)
s=s.replace('Il certificato esprime l\'esito delle operazioni e segue il regime previsto dal Codice. Termini, carattere dell\'atto e passaggi di approvazione vanno verificati sul testo vigente: per la preparazione concorsuale conta soprattutto comprendere funzione, sequenza e conseguenze.', '''L'art. 116 prevede che il collaudo finale sia completato entro **sei mesi dall'ultimazione**, elevabili a **un anno per lavori di particolare complessità**. Il certificato ha carattere provvisorio e diventa definitivo dopo **due anni dall'emissione**. La provvisorietà non significa che l'opera sia inutilizzabile per definizione; consegna e uso seguono i propri presupposti. Non elimina neppure garanzie e responsabilità per i vizi secondo Codice e diritto civile.''')
s=before(s,'### Collaudo statico e verifica di conformità', '''L'art. 28 dell'Allegato II.14 consente alla stazione appaltante di scegliere il CRE per lavori **pari o inferiori a 1 milione di euro**. Sopra 1 milione e sotto la soglia UE lavori, sono escluse le tipologie indicate dalla norma: opere di classe III/IV, salvo manutenzione; particolari complessità strutturali; miglioramento o adeguamento sismico; le categorie speciali del Libro IV richiamate; lavori in cui il RUP sia anche progettista o DL.

Il **DL emette il CRE entro tre mesi dall'ultimazione** e lo trasmette subito al **RUP**, che ne prende atto e ne conferma la completezza. Il collaudatore emette invece il certificato nel percorso di collaudo. Il CRE non sostituisce il collaudo statico quando dovuto.

**Scelta motivata.** Per lavori ordinari da 800.000 euro la stazione può avvalersi del CRE. Per miglioramento sismico da 2 milioni, pur sotto soglia UE, la specifica esclusione impedisce di scegliere il CRE solo per ragioni di velocità. Per ciascuno si indicano importo, oggetto, ruoli e norma applicata.''')
s=before(s,'### Durabilità, ispezione e priorità', '''### I tre documenti del piano

L'art. 27 dell'Allegato I.7 articola il piano, salvo diversa motivata indicazione dell'amministrazione, in **manuale d'uso**, **manuale di manutenzione** e **programma di manutenzione**. Il primo consente all'utente di utilizzare correttamente il bene e riconoscere anomalie; il secondo descrive risorse, prestazioni minime, anomalie e manutenzioni, distinguendo attività dell'utente e personale specializzato. Il programma ordina nel tempo prestazioni attese, controlli e interventi attraverso tre sottoprogrammi distinti.

**Componente: scarico della copertura della scuola.** Il manuale d'uso ne identifica la posizione e spiega come segnalare ristagni senza esporre l'utente ad accessi non consentiti. Il manuale di manutenzione descrive accesso sicuro, risorse e personale competente per pulizia o sostituzione, anomalie e requisiti funzionali. Il sottoprogramma delle **prestazioni** considera il regolare deflusso; quello dei **controlli** indica che cosa verificare e quando, secondo progetto/produttore e condizioni; quello degli **interventi** pianifica le attività conseguenti. Una frequenza assegnata al controllo non prova che la pulizia sia già stata eseguita: il registro deve conservarne data ed esito.

Se in cantiere cambia il componente installato, non basta sostituire una fotografia: vanno allineati manuali, programma, elaborati e dati del bene effettivo.''')
save(p,s)
p,s=load(10)
s=before(s,'### Costi della sicurezza e quadro economico', '''### Analisi di un prezzo: risorse, spese generali, utile

L'art. 31 dell'Allegato I.7 scompone una voce mancante in materiali, manodopera, noli e trasporti necessari all'unità di lavorazione; aggiunge spese generali tra il 13% e il 17%, motivate dalle caratteristiche dell'intervento, e infine utile del 10%. Prima di aggiungerle, si controlla che queste componenti non siano già comprese nel prezzo elementare o nella voce di prezzario, per evitare duplicazioni.

Esempio per **1 m² di una lavorazione didattica**; prezzi assegnati, non tariffa ufficiale:

| Risorsa | Quantità × costo elementare | Euro per m² |
| --- | --- | --- |
| Materiale | 2 unità × 20 €/unità | 40 |
| Manodopera | 1,5 ore × 30 €/ora | 45 |
| Nolo | 0,2 ore × 50 €/ora | 10 |
| Trasporto non già incluso | 0,1 unità × 50 €/unità | 5 |

Costo diretto = 100 €/m². Si assume motivatamente SG = 15%: 100 × 0,15 = 15. Subtotale 115. Utile = 115 × 10% = 11,50. **Prezzo analizzato = 126,50 €/m²**. Sommare semplicemente 15% + 10% al costo diretto darebbe 125 e salterebbe la base dell'utile. Per 20 m² l'importo è 2.530 euro. L'analisi resta verificabile perché ogni risorsa ha quantità, unità e provenienza dichiarate.''')
s=before(s,'## N-TR03-10-03', '''### Sicurezza, manodopera e costo dell'intervento

La stazione appaltante individua nei documenti i costi della manodopera e della sicurezza e li scorpora dall'importo assoggettato al ribasso, ai sensi dell'art. 41, comma 14. L'operatore può dimostrare che un ribasso complessivo deriva da una più efficiente organizzazione aziendale: la manodopera non è un numero da ridurre automaticamente né un dato sottratto a qualsiasi giustificazione. I minimi e le tutele applicabili restano vincolanti.

I **costi della sicurezza di progetto**, per esempio misure di coordinamento del PSC, sono distinti dagli **oneri aziendali di sicurezza** legati all'organizzazione dell'offerente. L'art. 108, comma 9, richiede che l'offerta indichi manodopera e oneri aziendali, salvo le eccezioni per forniture senza posa e servizi intellettuali. Non si somma due volte la stessa misura dentro una voce, nelle spese generali e nel PSC.

**Quadro economico didattico semplificato.** Lavori 100.000 euro, inclusa manodopera già stimata; costi sicurezza separati 5.000: subtotal appalto 105.000. Somme a disposizione assegnate dalla traccia: rilievi 2.000, spese tecniche 10.000, imprevisti 6.000, collaudi 2.000, imposte complessive convenzionalmente date 25.000. Totale intervento **150.000 euro**. I 25.000 sono un dato dell'esercizio, non un'aliquota IVA generale. La manodopera già compresa nei 100.000 non si riaggiunge; le somme a disposizione non diventano tutte corrispettivo dell'appaltatore. Nel caso reale l'art. 5 dell'Allegato I.7 richiede le voci pertinenti, accantonamenti e basi fiscali effettive.

La revisione prezzi dell'art. 60 è un percorso separato dalle quantità del SAL. Per i lavori nel nuovo regime, la variazione oltre il 3% attiva il riconoscimento del 90% dell'eccedenza sulle prestazioni da eseguire, anche in diminuzione; per procedure avviate dal 27 aprile 2026 si applica il sistema TOL dell'Allegato II.2-bis e del D.D. MIT 743/2026. Prima di calcolare si identifica il regime temporale del contratto, non si applica il prezzario più recente a tutte le quantità già eseguite.''')
s=s.replace('La riserva deve poter essere collegata al fatto, al documento e alla pretesa. Il dettaglio delle procedure e dei termini va sempre verificato sul testo vigente; qui conta la relazione fra evento, registrazione e tutela della posizione.', '''L'art. 7 dell'Allegato II.14 richiede, a pena di decadenza, l'iscrizione sul primo atto idoneo successivo all'insorgenza o cessazione del fatto pregiudizievole e, in ogni caso, nel registro di contabilità alla firma immediatamente successiva. La riserva deve essere specifica, motivata e precisamente quantificata; la quantificazione è definitiva salvo fatti continuativi. Ordini di servizio e contestazioni tecniche pertinenti vanno identificati. Il semplice «mi riservo ogni diritto» non espone la pretesa richiesta.

Le riserve vanno confermate sul conto finale; la firma è richiesta entro **trenta giorni dall'invito del RUP**. Non si introducono nuove domande per oggetto o importo rispetto a quelle già formulate nel registro; mancata firma nel termine o firma senza conferma producono gli effetti di accettazione/rinuncia previsti. Non tutte le pretese passano attraverso riserva: il comma 1 esclude, tra l'altro, gli interessi moratori per ritardo nei pagamenti. Il primo controllo consiste quindi nel qualificare la pretesa, poi individuare atto e tempestività.''')
s=before(s,'### Riserve e tracciabilità', '''### Documento, soggetto e termine

L'art. 125 collega il pagamento all'accertamento dell'avanzamento, non alla semplice richiesta dell'impresa.

| Passaggio | Responsabile e tempo essenziale |
| --- | --- |
| Misure e documenti contabili | DL, con tempestiva registrazione dell'eseguito |
| SAL | DL, al verificarsi delle condizioni contrattuali |
| Certificato di pagamento | RUP, contestualmente al SAL e comunque entro 7 giorni dalla sua adozione |
| Pagamento acconto | Entro 30 giorni dall'adozione del SAL; fino a 60 solo se espressamente pattuito e oggettivamente giustificato dalla natura o caratteristiche del contratto |

Il ritardo nell'emissione del certificato non sposta liberamente la decorrenza. Fatturazione e controlli previsti vanno coordinati con la disciplina, senza trasformarli in una dilazione non ammessa.

**Caso temporale.** SAL adottato il 10 giugno; nessuna pattuizione speciale dei sessanta giorni. Escludendo il giorno iniziale nel computo didattico, il certificato deve essere emesso non oltre il 17 giugno e il pagamento avvenire entro il 10 luglio. Il certificato emesso il 15 giugno non porta il termine al 15 luglio. Nel calendario effettivo si verificano anche le regole applicabili ai giorni festivi.''')
save(p,s)
p,s=load(11)
s=before(s,'### Continuità del servizio e conseguenze', '''### La classificazione tecnico-funzionale

L'art. 2 del Codice della strada distingue:

| Tipo | Denominazione e carattere essenziale |
| --- | --- |
| A | Autostrada: carreggiate separate, accessi controllati, assenza di intersezioni a raso |
| B | Extraurbana principale: carreggiate separate e almeno due corsie per senso, senza intersezioni a raso |
| C | Extraurbana secondaria: unica carreggiata, almeno una corsia per senso e banchine |
| D | Urbana di scorrimento: carreggiate separate; eventuali intersezioni a raso semaforizzate |
| E | Urbana di quartiere: unica carreggiata, almeno due corsie, banchine e marciapiedi |
| E-bis | Urbana ciclabile: limite non superiore a 30 km/h, segnalazione e priorità ai velocipedi |
| F | Locale: urbana o extraurbana, fuori dagli altri tipi |
| F-bis | Itinerario ciclopedonale: uso prevalentemente pedonale/ciclabile e tutela dell'utenza vulnerabile |

La tabella seleziona i caratteri per distinguere le categorie, non sostituisce tutti i requisiti geometrici del comma 3. «Provinciale» indica invece classificazione amministrativa/proprietà: non è una categoria alternativa alla C. Una strada può essere extraurbana secondaria e provinciale. Per individuare obblighi progettuali si affiancano categoria, intervento nuovo/esistente e norme tecniche applicabili.''')
s=s.replace('Le Linee guida adottano un processo multilivello: censimento e ispezione alimentano la classificazione; gli esiti indirizzano approfondimenti e valutazioni. Livelli, schede e frequenze vanno letti negli atti vigenti, non ricostruiti per analogia.', '''Le Linee guida ponti adottate con D.M. 204/2022 prevedono sei livelli, con approfondimento crescente:

| Livello | Funzione e risultato |
| --- | --- |
| 0 | Censimento: identità, caratteristiche e documentazione disponibile |
| 1 | Ispezioni visive dirette e rilievo speditivo: degrado, geometria e contesto geomorfologico/idraulico |
| 2 | Classe di attenzione: elaborazione di pericolosità, vulnerabilità ed esposizione |
| 3 | Valutazioni preliminari: chiarire necessità e priorità delle verifiche accurate |
| 4 | Valutazioni accurate di sicurezza secondo NTC |
| 5 | Rilevanza trasportistica e resilienza della rete per opere significative; livello richiamato, ma non trattato esplicitamente dalle Linee guida |

Le classi di attenzione sono **bassa, medio-bassa, media, medio-alta e alta**. Si considerano i profili strutturale-fondazionale, sismico, frane e idraulico secondo il metodo ufficiale. Non si costruisce una media intuitiva che compensi una criticità con un dato favorevole. Per classe alta si procede alle valutazioni accurate del livello 4; per le altre classi si applicano il percorso e i controlli previsti, riesaminando la classe dopo nuovi esiti. La sequenza non impone di aspettare tutti i livelli per adottare cautele urgenti.''')
s=before(s,'## ▣ Verifica', '''### Leggere una scheda senza inventare una diagnosi

Scheda didattica assegnata: ponte P-17, strada provinciale di tipo C, due campate; ispezione 3 ottobre 2026; anomalia G1 al giunto lato spalla A con infiltrazione sottostante; scarico S2 parzialmente ostruito; intradosso della seconda campata non accessibile; foto F1 e F2 localizzate; precedente ispezione disponibile, progetto strutturale incompleto; classificazione di attenzione non ancora completata.

**Lettura modello.** La classificazione stradale è duplice e coerente. G1 e S2 sono fatti osservati da registrare, non prova automatica di perdita della capacità portante. «Non accessibile» è un limite conoscitivo, non «assenza di difetti». Il confronto con la precedente ispezione deve distinguere difetto nuovo, invariato o non confrontabile. Per completare il livello 2 servono i dati richiesti dal metodo; non si attribuisce una classe numerica inventata. Si attivano il gestore e le competenze necessarie per valutare urgenza, accesso e approfondimenti; il fascicolo conserva chi decide e su quale evidenza.

**Errore da correggere:** scrivere «ponte sicuro perché nessuna soglia è superata» quando lo strumento non misura il difetto osservato e una campata non è stata ispezionata. La scheda deve conservare questi limiti fino al loro effettivo superamento.''')
save(p,s)
p,s=load(12)
s=before(s,'### Ambiente di condivisione e responsabilità', '''### Quando è obbligatorio e quali documenti servono

Dal **1 gennaio 2025**, l'art. 43 richiede metodi e strumenti di gestione informativa digitale per nuove opere e interventi su esistenti con costo presunto lavori **superiore a 2 milioni di euro**. Per edifici culturali dell'art. 10, comma 1, D.Lgs. 42/2004, il riferimento è la soglia UE lavori dell'art. 14, comma 1, lett. a: **5.404.000 euro nel biennio 2026–2027**. Sono escluse manutenzione ordinaria e straordinaria, salvo che riguardino opere già eseguite con questi metodi. Anche l'adozione facoltativa richiede le misure organizzative dell'Allegato I.9.

Prima dell'adozione, la stazione definisce e attua formazione e acquisizione/gestione degli strumenti e adotta l'atto di organizzazione. Acquistare un programma di modellazione non soddisfa da solo queste condizioni.

**Capitolato informativo, CI.** È della stazione appaltante: stabilisce requisiti informativi, usi e consegne, modalità di produzione/scambio/archiviazione, ambiente di condivisione, accessi, validità e interoperabilità. Per esempio, per gli impianti della scuola richiede identificativo del componente, ubicazione, produttore, manutenzione e collegamento al manuale.

**Offerta di gestione informativa, OGI.** Nelle procedure con criterio dell'offerta economicamente più vantaggiosa, il concorrente risponde al CI descrivendo organizzazione, risorse, responsabilità e flussi. Non riscrive liberamente i requisiti del committente.

**Piano di gestione informativa, PGI.** L'aggiudicatario lo redige sulla base dell'OGI, da sottoporre dopo la sottoscrizione e prima dell'esecuzione; è aggiornabile. In avvio urgente la stazione può richiederlo prima della stipula. Traduce gli impegni in un processo effettivo: chi produce il dato dell'impianto, chi lo controlla, con quale versione e quando lo consegna.

Al collaudo l'affidatario consegna modelli aggiornati al realizzato e relazione specialistica sulla modellazione; il controllo riguarda anche l'adempimento informativo. Una geometria gradevole ma senza gli attributi richiesti può essere una consegna incompleta.''')
s=before(s,'### Interoperabilità e consegna alla gestione', '''L'Allegato I.9 distingue nell'organizzazione della stazione il **gestore dell'ambiente di condivisione dei dati**, almeno un **gestore dei processi digitali** e, per ciascun intervento, il **coordinatore dei flussi informativi** nella struttura di supporto al RUP. Servono competenze adeguate documentate; se non reperibili internamente, le funzioni si affidano all'esterno secondo il Codice. Non basta assegnare etichette inglesi a persone prive di un incarico e di competenze coerenti.

Il gestore dell'ambiente presidia il sistema di condivisione; il gestore dei processi opera sul metodo organizzativo; il coordinatore raccorda i flussi del singolo intervento. Questi compiti non assorbono decisioni del RUP, responsabilità del progettista, verifiche del DL o giudizio del collaudatore.''')
s=before(s,'### Dal rilievo alla restituzione', '''### Vettori, raster e un controllo sulle coordinate

Un dato **vettoriale** descrive oggetti mediante punti, linee e poligoni: un punto per un accesso, una linea per una condotta, un poligono per una particella. Un **raster** è una griglia di celle con valori: una ortofoto o un modello di elevazione. In un raster la dimensione della cella influisce sul dettaglio; un pixel piccolo non elimina un errore di georeferenziazione.

**Esercizio.** Due punti hanno coordinate (500.000; 4.600.000) e (500.030; 4.600.040), in metri nello stesso CRS proiettato assegnato dalla traccia, per esempio ETRS89 / UTM zona 32N. La distanza piana è √(30² + 40²) = **50 m**. Se il secondo file fornisce invece longitudine e latitudine in gradi, non si sottraggono quei numeri dalle coordinate metriche: si identifica il CRS originale e si esegue una trasformazione appropriata. «Assegnare» l'etichetta del primo CRS al secondo file non trasforma le coordinate.

Il risultato di 50 m è una distanza piana tra i punti assegnati, non un rilievo della lunghezza reale di una condotta curva o inclinata.''')
s=s.replace('Gli atti di aggiornamento dipendono dal tipo di variazione e dalle procedure ufficiali dell\'Agenzia delle entrate. PREGEO, DOCFA e voltura hanno funzioni distinte; il dettaglio operativo richiede abilitazione e fonte vigente.', '''La procedura si sceglie in base a ciò che cambia:

| Variazione | Procedura e funzione |
| --- | --- |
| Geometria del terreno, frazionamento o inserimento del fabbricato nella mappa | PREGEO, atti geometrici del catasto terreni |
| Nuova unità urbana o variazione delle sue caratteristiche | DOCFA, dichiarazioni al catasto fabbricati |
| Intestazione conseguente ad atto o fatto giuridico | Voltura catastale, aggiornamento degli intestatari |

Un nuovo fabbricato può richiedere passaggi coordinati PREGEO e DOCFA; una compravendita non si aggiorna modificando con DOCFA il nome del proprietario. La voltura non sostituisce l'atto né la pubblicità immobiliare; queste sono funzioni distinte. Il dettaglio della pratica segue le procedure ufficiali e le competenze professionali richieste.''')
s=before(s,'### Scheda del bene e ciclo di vita', '''Il **demanio** comprende le categorie dell'art. 822 c.c.; l'art. 823 ne stabilisce inalienabilità e diritti dei terzi soltanto nei modi e limiti delle leggi. Esempio: una spiaggia demaniale non si tratta come un appartamento liberamente vendibile. La concessione d'uso ammessa non trasferisce automaticamente la proprietà.

Il **patrimonio indisponibile** comprende, tra gli altri, edifici destinati a uffici pubblici e altri beni destinati a pubblico servizio, secondo l'art. 826. L'art. 828 impedisce di sottrarli alla destinazione se non nei modi previsti dalla legge. Esempio: un edificio statale effettivamente destinato a sede di uffici non diventa disponibile perché per qualche settimana una stanza è vuota.

Il **patrimonio disponibile** è la categoria residuale: si applicano le regole civilistiche salvo discipline speciali e obblighi pubblicistici. Esempio: un appartamento dell'ente privo di destinazione a pubblico servizio e di altro regime speciale può essere locato secondo il percorso applicabile. La mera proprietà pubblica non rende demaniale qualunque immobile.

**Caso.** Prima di proporre la vendita di un ex edificio di servizio, non basta la casella «inutilizzato» nell'inventario: si verifica classificazione, cessazione della destinazione nei modi di legge ed eventuali vincoli culturali. L'inventario registra il risultato; non crea da solo il nuovo regime.''')
save(p,s)
p,s=load(13)
s=s.replace('Per il metodo generale della risposta breve, rinvia a `VOL-01`, capitolo **Risposta sintetica: scrivere poco, dire tutto**, sezioni *Leggere la traccia in 60 secondi* e *La griglia di revisione finale*.', 'Per il metodo generale della risposta breve usa il volume 1, capitolo 15, nelle sezioni **La lettura della traccia** e **Lo schema base: definizione, riferimento, funzione, esempio, conclusione**. Il protocollo R19, *Risposta sintetica: scrivere poco, dire tutto*, è un approfondimento del Ricettario digitale opzionale, non un capitolo dell’edizione cartacea.')
s=s.replace('**Consegna.** Su una planimetria semplificata di una scuola, imposta lo schema per un sopralluogo successivo a infiltrazioni segnalate al piano superiore.', '**Consegna.** Usa la planimetria D1 e il dossier completo della simulazione nel nucleo 7 di questo capitolo. Imposta lo schema del sopralluogo dopo la segnalazione di un alone sul soffitto dell’aula A; non presumere che sia già accertata una infiltrazione o la sua causa. Puoi ricopiare lo schema e coprire il percorso modello per svolgere la prova.')
start=s.index('Poi usa un dossier didattico su un edificio pubblico con:');end=s.index('La simulazione può includere',start)
s=s[:start]+'''### Dossier cartaceo completo

I documenti seguenti sono **interamente didattici**; nomi, date, misure e prezzi sono assegnati per l'esercizio. Non descrivono una scuola reale. La figura F01 è un'illustrazione, non una fotografia di sopralluogo. La planimetria include un percorso modello che puoi coprire nella prima esecuzione.

**Segnalazione S1 — 1 ottobre 2026.** Il referente dell'edificio segnala un alone sul soffitto dell'aula A, notato dopo un periodo piovoso. Non sono segnalati distacchi o gocciolamento; questo non prova che siano esclusi. Si chiede all'ufficio tecnico di documentare lo stato osservabile e indicare gli approfondimenti necessari.

**D1 — Planimetria di consistenza, revisione 2024.** Rettangolo complessivo 12 × 8 m; corridoio sul lato sud 12 × 2 m, aula A a ovest e B a est, ciascuna 6 × 6 m. Quote nette; spessori murari trascurati soltanto nel modello didattico. Nord in alto. La rappresentazione non è un titolo edilizio né una verifica di conformità.

![D1 — Planimetria didattica del sopralluogo](../assets/correzioni-2026-10/planimetria-sopralluogo.png)

**D2 — Scheda di manutenzione, revisione 2025.** Identificativo edificio SC-01; locale A: larghezza 5 m, profondità 6 m, superficie soffitto 30 m². Ultima finitura registrata: 2019. Origine dell'alone: campo non compilato. Allegati tecnici della revisione dimensionale: non disponibili. Il documento è più recente di D1, ma non spiega la differenza di misura.

**R1 — Dati del rilievo assegnati, 3 ottobre 2026, ore 10.00.** Aula A accessibile: misure nette ortogonali 6,00 × 6,00 m; soffitto piano, senza aperture da detrarre. Proiezione convenzionale dell'area interessata dall'alone: rettangolo 2 × 1 m. Aula B non accessibile perché utilizzata durante il sopralluogo; non è stata interdetta per un pericolo accertato. Copertura, impianti e porzioni nascoste non ispezionati. Il dossier non fornisce misure di umidità, prove sui materiali o esiti strutturali.

**F01 — Documento illustrativo.** Punto P3 nell'aula A, orientamento verso nord-ovest e soffitto. L'immagine mostra un alone; la sua estensione di 2 m² deriva esclusivamente dal dato assegnato in R1 e dalla proiezione D1. Non si misura la fotografia e non si deduce la causa dal colore.

![F01 — Illustrazione didattica dell'alone, causa non accertata](../assets/correzioni-2026-10/f01-alone-illustrativo.png)

**E1 — Voce economica assegnata.** Rifacimento della finitura dell'intero soffitto dell'aula A, dopo l'accertamento e la risoluzione della causa: prezzo didattico 24 €/m², comprensivo delle operazioni di finitura descritte dalla traccia. Sono esclusi ricerca/riparazione della causa, opere strutturali, imposte e altre lavorazioni. Il mini-computo è una stima parziale della finitura, non autorizza l'esecuzione né rappresenta il costo totale di bonifica.

### Consegna e spazio di lavoro

Allenamento autonomo di **50 minuti**, senza attribuire questi tempi a un bando reale: 10 lettura e schema, 25 relazione e calcolo, 10 risposta orale preparata, 5 controllo. Produci uno schema con percorso, punti, F01 e limite di accesso; una relazione di massimo 250 parole; il mini-computo E1; una risposta orale di due minuti alla domanda «Quale documento aggiorneresti e perché?». Usa fogli aggiuntivi se necessario.

| Campo da compilare | Risposta |
| --- | --- |
| Fatto osservato e documento | ______________________________ |
| Discordanza fra D1 e D2 | ______________________________ |
| Dato assunto per il computo | ______________________________ |
| Limite del sopralluogo | ______________________________ |
| Approfondimento e soggetto | ______________________________ |
| Quantità × prezzo e importo | ______________________________ |

### Elaborato modello

**Schema.** Ingresso da sud P1, percorso nel corridoio e accesso all'aula A P2; osservazione P3 con orientamento F01 verso nord-ovest. Si identifica il rettangolo convenzionale dell'alone e si tratteggia B soltanto come non ispezionata. Non si disegna una provenienza dell'acqua non dimostrata.

**Relazione.** «Il sopralluogo didattico del 3 ottobre 2026 documenta l'alone sul soffitto dell'aula A, segnalato in S1 e rappresentato da F01. Le misure assegnate R1 sono 6 × 6 m, coerenti con D1 e discordanti con D2, che indica 5 × 6 m senza allegato esplicativo. Per la stima della finitura si assumono le misure R1; D2 va verificata e corretta conservando versione e ragione della rettifica. L'alone ha proiezione convenzionale di 2 m²; non è stata accertata la causa. Aula B, copertura, impianti e parti nascoste non sono stati ispezionati. Si propone al responsabile del servizio di organizzare gli accessi e gli approfondimenti tecnici pertinenti, valutando contestualmente le cautele sulla base delle condizioni riscontrate. La finitura può essere programmata dopo l'accertamento e la soluzione della causa; l'eventuale urgenza di sicurezza segue il proprio percorso. Il computo allegato riguarda la sola finitura assegnata, senza certificare conformità edilizia o sicurezza strutturale». 

**Computo.** Quantità soffitto A = 6 × 6 = **36 m²**; importo = 36 × 24 = **864 euro**, con esclusioni E1. Usare D2 produrrebbe 30 × 24 = 720 euro: sottostima di **144 euro**. Usare soltanto l'alone darebbe 2 × 24 = 48 euro, ma contraddice la consegna dell'intero soffitto. La superficie dell'area osservata e quella della lavorazione sono grandezze diverse.

**Risposta orale modello.** «Verificherei la scheda D2 confrontandola con D1 e R1; la data più recente non rende affidabile una misura priva di evidenza. Conserverei il documento precedente e registrerei la rettifica motivata nell'inventario manutentivo. Aggiornerei il fascicolo con S1, schema, R1, F01 e limiti di accesso. Catasto o titoli edilizi richiederebbero verifiche specifiche: una discordanza della sola scheda non dimostra la necessità di una pratica catastale né un abuso».

### Griglia della simulazione

| Criterio | Punti massimi | Evidenza richiesta |
| --- | --- | --- |
| Lettura della consegna | 4 | Intero soffitto, prodotti e limiti rispettati |
| Schema e documenti | 6 | Orientamento, percorso, F01, area B, confronto D1/D2/R1 |
| Ragionamento tecnico | 8 | Fatto distinto da causa; cautele e approfondimenti motivati |
| Computo | 6 | 36 m², 864 euro, differenza 144 ed esclusioni |
| Chiarezza e orale | 6 | Relazione ordinata, aggiornamento motivato, nessuna diagnosi inventata |

Totale 30 punti **solo per autovalutazione**, senza soglia ufficiale di idoneità. Per ogni criterio assegna zero se assente o errato, metà dei punti se incompleto, massimo se tutte le evidenze indicate sono presenti. Il modello, se riprodotto con ragionamento autonomo e nei limiti assegnati, soddisfa le cinque voci. Una risposta con importo corretto ma causa dell'alone inventata perde punti nel ragionamento; se usa 2 m² invece di 36 perde anche lettura e computo. Registra la ragione della perdita, non soltanto il numero.

''' +s[end:]
save(p,s)
Path('artifacts/correzioni-collana-2026-10-02/VOL-10-second-changes.json').write_text(json.dumps(changes,indent=2),encoding='utf8');print('Updated',len(changes),'chapters')
