from pathlib import Path
import re,json,shutil,hashlib,datetime
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
p=next(B.glob('07-*.md'));t=p.read_text('utf-8');b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
before=hashlib.sha256(p.read_bytes()).hexdigest()
t=t.replace('In un manuale professionale non si cristallizzano termini e decorrenze senza verifica del testo vigente. Si costruisce prima la mappa operativa, poi si controllano i dettagli normativi sulla fonte ufficiale.','Le regole processuali qui illustrate sono verificate al 3 ottobre 2026; l’applicazione al singolo fascicolo richiede anche il controllo del regime temporale. La mappa serve a collegare norme e attività, mentre gli esempi insegnano a riconoscere gli effetti degli atti.')
t=t.replace('distinguere il processo penale operativo dal processo penale teorico;','collegare le regole processuali agli adempimenti di ufficio;')
t=t.replace('prova penale sostanziale in dettaglio','teoria avanzata della prova penale').replace('e calcolo puntuale dei termini senza controllo aggiornato','e questioni sui termini estranee ai casi e alle regole qui illustrate')
t=t.replace('| Profilo UPP | Supporto organizzativo e conoscitivo nei limiti del progetto | Schede, ricerche, cronologie, udienza |','| UPP | Non è prevista una struttura ordinaria presso ogni Procura della Repubblica; distinta disciplina per la Procura generale della Cassazione. | Supporto negli uffici giudicanti previsti dal D.Lgs. 151/2022: schede, ricerche, cronologie, udienza. |')
start=t.index('### Notizia di reato, registri e fascicolo');end=t.index('### Dibattimento, decisione e fase post-udienza',start)
t=t[:start]+'''### Indagato, imputato, persona offesa e parte civile

La persona sottoposta alle indagini, comunemente chiamata **indagato**, non è ancora imputato. L'art. 60 c.p.p. collega la qualità di **imputato** agli atti con cui si esercita l'azione penale: per esempio richiesta di rinvio a giudizio, richiesta di decreto penale o decreto di citazione diretta. Ricevere l'avviso di conclusione delle indagini non produce da solo questo passaggio. L'art. 61 estende all'indagato diritti e garanzie dell'imputato: la diversa denominazione non crea una fase priva di difesa.

La **persona offesa** è il titolare dell'interesse protetto dalla norma incriminatrice. Il **danneggiato** è chi ha subito un danno risarcibile dal reato; può esercitare l'azione civile nel processo penale mediante costituzione di parte civile, nei casi e nei tempi previsti. Le figure possono coincidere, ma non necessariamente: l'erede di una vittima può far valere un danno proprio senza essere la persona contro cui fu direttamente commesso il fatto. Non registrare automaticamente ogni denunciante come parte civile.

Durante l'interrogatorio, gli avvertimenti dell'art. 64 riguardano l'utilizzabilità delle dichiarazioni, la facoltà di non rispondere, salvo i dati identificativi dovuti, e le conseguenze delle dichiarazioni sulla responsabilità altrui. Il procedimento prosegue anche se la persona tace. Sono vietati metodi che incidano sulla libertà di autodeterminazione o sulla capacità di ricordare e valutare. Per il personale d'ufficio queste garanzie impongono precisione nei verbali e negli avvisi: una formula mancante non va aggiunta a posteriori come se fosse stata pronunciata.

**Errore da evitare.** «È iscritto nel registro, dunque è colpevole». L'iscrizione avvia o documenta l'accertamento; non è una condanna. Anche la ragionevole previsione di condanna utilizzata nei filtri processuali è diversa dalla prova della colpevolezza oltre ogni ragionevole dubbio richiesta dall'art. 533 per condannare.

### Notizia di reato, iscrizione e annotazione preliminare

L'art. 335 richiede al pubblico ministero di iscrivere immediatamente la notizia che rappresenta un fatto determinato, non inverosimile e riconducibile in ipotesi a un reato. Il nome della persona è iscritto quando emergono indizi a suo carico, contestualmente alla notizia o successivamente. È il PM a compiere le valutazioni previste dalla norma; la segreteria cura gli adempimenti conseguenti secondo competenza, senza decidere autonomamente la qualificazione del fatto.

Il registro collega numero, anno, ufficio, soggetti, qualificazione e fase. Un mutamento della qualificazione giuridica o delle circostanze comporta l'aggiornamento previsto dall'art. 335, non automaticamente una nuova iscrizione. Il fascicolo raccoglie gli atti relativi alla posizione; il suo numero va sempre accompagnato dall'ufficio e dal registro per evitare omonimie o confusioni tra fasi.

Dal 2026 esiste una distinzione ulteriore. Quando appare evidente che il fatto è stato compiuto in presenza di una causa di giustificazione, l'art. 335, comma 1-bis.1, prevede l'**annotazione preliminare** del nome in separato modello. La circolare ministeriale del 7 maggio 2026 illustra il **modello 45-bis**, istituito per questa funzione presso le Procure dei tribunali. Non è il modello degli atti privi di rilevanza penale e non equivale ad archiviazione.

L'art. 335-quinquies mantiene diritti e garanzie dell'indagato. Se non occorrono ulteriori accertamenti, il PM assume le determinazioni sulla richiesta di archiviazione senza ritardo e comunque entro trenta giorni; se servono accertamenti, provvede entro centoventi giorni e, all'esito, dispone degli ulteriori trenta giorni previsti dalla norma, salvo il passaggio all'iscrizione ordinaria. In caso di incidente probatorio si procede all'iscrizione del nome; se si passa all'iscrizione ordinaria, i termini dell'art. 405 decorrono dall'annotazione preliminare. Il registro separato non consente quindi di azzerare la cronologia o di negare le garanzie.

### Conoscibilità e segreto

Indagato, persona offesa e rispettivi difensori possono chiedere la comunicazione delle iscrizioni nei limiti dell'art. 335. Sono esclusi i casi indicati dall'art. 407, comma 2, lettera a; per specifiche esigenze investigative il PM può inoltre disporre con decreto motivato il segreto sulle iscrizioni per un periodo non superiore a tre mesi, non rinnovabile. Dopo sei mesi dalla denuncia o querela, l'offeso può chiedere informazioni sullo stato del procedimento, senza pregiudizio del segreto investigativo.

L'art. 329 protegge gli atti investigativi indicati dalla norma sino a quando l'imputato può conoscerli e, comunque, non oltre la chiusura delle indagini, ferme le disposizioni particolari sui singoli atti. Conoscibilità da parte della difesa e pubblicabilità sono questioni diverse. Una stampa del registro o una copia di un verbale non si consegnano a chiunque affermi di conoscere una delle persone coinvolte. Il capitolo 8, nella sezione sull'accesso processuale, distingue la consultazione del fascicolo dalle richieste di copie ex art. 116.

### Indagini: termini e decisioni del pubblico ministero

Le indagini raccolgono gli elementi necessari alle determinazioni del PM, anche mediante la polizia giudiziaria. Il GIP interviene nei casi previsti per controlli, autorizzazioni e decisioni; non dirige ordinariamente l'indagine al posto del PM.

| Regola di base | Termine | Controllo sulla scheda |
|---|---|---|
| Delitto ordinario, art. 405 | Un anno | Data di iscrizione del nome; eventuali condizioni di procedibilità. |
| Contravvenzione | Sei mesi | Corretta qualificazione del reato. |
| Delitti indicati dall'art. 407, comma 2 | Un anno e sei mesi | Appartenenza al catalogo pertinente. |
| Proroga ex art. 406 | Una volta, non oltre sei mesi | Richiesta prima della scadenza e provvedimento del giudice per complessità. |

L'art. 407 fissa i massimi di diciotto mesi in via ordinaria, un anno per le contravvenzioni e due anni nei casi del comma 2. Questi dati vanno coordinati con le regole sulle condizioni di procedibilità e con gli atti integrativi dell'art. 415-bis. La scadenza delle indagini non determina da sola un'archiviazione: occorrono la determinazione del PM e, per archiviare, la decisione del giudice. Nemmeno il termine delle indagini coincide con il termine di prescrizione del reato.

### Avviso di conclusione delle indagini

Se non deve chiedere l'archiviazione, il PM, nel percorso regolato dall'art. 415-bis, fa notificare l'avviso all'indagato e al difensore. Per i reati di maltrattamenti e atti persecutori la norma prevede anche il destinatario offeso indicato nel comma 1. L'avviso riassume fatto, norme ritenute violate, data e luogo; informa del deposito degli atti presso la segreteria e della possibilità di esaminarli ed estrarne copia.

Nei **venti giorni** previsti l'indagato può presentare memorie e documenti, depositare investigazioni difensive, chiedere atti di indagine, rendere dichiarazioni o chiedere l'interrogatorio. Se quest'ultimo è chiesto tempestivamente, il PM deve procedervi. Le nuove indagini disposte a seguito della richiesta devono essere compiute entro trenta giorni, prorogabili dal GIP una sola volta per non più di sessanta giorni.

Per la segreteria contano notifiche, date, istanze e convocazioni. Per il giudice che riceve la richiesta di rinvio a giudizio rileva anche il rispetto delle garanzie: l'art. 416 sanziona con nullità la richiesta non preceduta dall'avviso o dall'invito all'interrogatorio tempestivamente richiesto. Non confondere la richiesta dell'interrogatorio entro venti giorni con un obbligo di celebrarlo entro quello stesso termine.

### Archiviazione: il PM chiede, il giudice decide

Quando gli elementi non consentono una ragionevole previsione di condanna o di applicazione di una misura di sicurezza diversa dalla confisca, il PM presenta richiesta di archiviazione ai sensi dell'art. 408. Fuori dai casi di rimessione della querela, l'offeso che abbia chiesto di essere informato riceve l'avviso e può prendere visione degli atti e proporre opposizione entro **venti giorni**. Per i delitti commessi con violenza alla persona e per il furto in abitazione o con strappo dell'art. 624-bis, l'avviso è dovuto in ogni caso e il termine è **trenta giorni**.

L'opposizione deve indicare l'oggetto dell'investigazione suppletiva e i relativi elementi di prova: il solo «non sono d'accordo» non soddisfa l'art. 410. Il giudice può archiviare con decreto motivato nelle condizioni previste oppure fissare l'udienza camerale. All'esito può indicare ulteriori indagini o, se non accoglie la richiesta e non servono tali indagini, ordinare al PM di formulare l'imputazione entro dieci giorni. La cancelleria registra il provvedimento effettivamente adottato; una richiesta del PM non va caricata come archiviazione già disposta.

### Udienza preliminare e filtro predibattimentale

L'udienza preliminare segue la richiesta di rinvio a giudizio nei procedimenti che la prevedono. Il GUP pronuncia sentenza di non luogo a procedere nelle ipotesi dell'art. 425, anche quando gli elementi non consentono una ragionevole previsione di condanna; se il processo prosegue, si dispone il giudizio. Non è corretto inserire un'udienza preliminare in ogni cronologia penale.

La **citazione diretta** dell'art. 550 riguarda contravvenzioni, delitti entro il limite ordinario di quattro anni di reclusione e i reati specificamente elencati. Il percorso comprende l'udienza di comparizione predibattimentale degli artt. 554-bis e 554-ter, in camera di consiglio, con partecipazione necessaria di PM e difensore. Si controllano costituzione delle parti, avvisi, notifiche e imputazione; possono intervenire definizioni alternative. Anche qui è possibile il non luogo a procedere per mancanza di ragionevole previsione di condanna.

Se il giudizio prosegue, il dibattimento si svolge davanti a un **giudice diverso**, con un intervallo non inferiore a venti giorni dal provvedimento; il fascicolo del PM è restituito. Per preparare l'udienza occorre quindi identificare il tipo di filtro, non soltanto scrivere «udienza penale» sul ruolo.

### Fascicolo del PM e fascicolo per il dibattimento

Il fascicolo delle indagini non passa integralmente e indistintamente al giudice del dibattimento. L'art. 431 prevede un fascicolo formato nel contraddittorio delle parti, contenente categorie determinate: atti relativi alla procedibilità e all'azione civile, verbali di atti irripetibili, prove assunte nell'incidente probatorio, atti acquisiti all'estero nei casi indicati, documenti previsti e corpo del reato, salvo custodia separata. Le parti possono concordare l'acquisizione di ulteriori atti consentiti.

**Esempio.** Un verbale di sommarie informazioni raccolte durante le indagini non entra nel fascicolo dibattimentale per il solo fatto di essere utile alla cronologia. Occorre una base processuale per l'acquisizione o l'utilizzazione. La selezione non è una scelta editoriale dell'addetto UPP: la scheda distingue «atto presente nel fascicolo PM», «atto acquisito al dibattimento» e «contenuto utilizzabile», senza equipararli.

La prova è normalmente ammessa su richiesta di parte, con esclusione delle prove vietate e di quelle manifestamente superflue o irrilevanti (art. 190). La valutazione è motivata; gli indizi devono essere gravi, precisi e concordanti (art. 192). Il candidato deve distinguere richiesta, ammissione, assunzione e valutazione: allegare un documento non equivale a ottenere una decisione favorevole.

''' +t[end:]
start=t.index('### Riti speciali e impugnazioni essenziali');end=t.index('### Comunicazioni, notificazioni, depositi e termini',start)
t=t[:start]+'''### Riti speciali: presupposto ed effetto

| Rito | Presupposto e percorso | Effetto da ricordare |
|---|---|---|
| Abbreviato | Richiesta dell'imputato; decisione di regola allo stato degli atti, con integrazioni ammesse dalla legge. Escluso per delitti puniti con ergastolo. | In caso di condanna: riduzione di un terzo per delitti, metà per contravvenzioni. |
| Applicazione della pena su richiesta | Accordo imputato–PM, controllo del giudice; pena detentiva, dopo riduzione fino a un terzo, non oltre cinque anni. | Non è un'accettazione automatica: il giudice verifica qualificazione, circostanze e congruità; operano esclusioni e condizioni speciali. |
| Direttissimo | Tra le ipotesi: arresto in flagranza con presentazione entro 48 ore, arresto già convalidato o confessione alle condizioni dell'art. 449. | Accesso accelerato al dibattimento; non presuppone un accordo sulla pena. |
| Immediato | Evidenza della prova e garanzie dell'art. 453; distinta ipotesi custodiale e richiesta dell'imputato. | Salta l'udienza preliminare; non elimina il dibattimento e la difesa. |
| Decreto penale | Richiesta motivata del PM al GIP per sola pena pecuniaria, anche sostitutiva, nel termine dell'art. 459. | Opposizione entro quindici giorni dalla notificazione; in mancanza, esecutività secondo le regole del codice. |
| Messa alla prova | Sospensione con programma e requisiti di legge; per adulti e minori valgono discipline distinte. | Esito positivo con estinzione del reato nei casi previsti; non è applicazione negoziata di una pena. |

Nell'abbreviato l'ulteriore riduzione di un sesto dell'art. 442, comma 2-bis, è applicata dal giudice dell'esecuzione quando né l'imputato né il difensore impugnano la condanna. Non va sommata anticipatamente come beneficio già certo nella scheda della sentenza.

Nel patteggiamento oltre due anni operano le esclusioni dell'art. 444, comma 1-bis; per taluni reati contro la pubblica amministrazione la richiesta è subordinata alla restituzione integrale del prezzo o profitto. Per i reati protetti elencati nel comma 1-quater, la richiesta presentata fuori udienza deve essere notificata al destinatario offeso previsto dalla norma, a pena di inammissibilità. Il controllo delle notifiche può quindi essere determinante anche in un rito concordato. Gli effetti della sentenza sono regolati dall'art. 445: non è corretto equipararla a ogni effetto a una condanna pronunciata dopo dibattimento.

La messa alla prova e la distinzione dalla giustizia riparativa sono sviluppate nel capitolo 13. Per il lavoro d'ufficio, la scheda deve separare richiesta, ordinanza di ammissione, programma, verifiche ed esito: l'istanza non prova che il processo sia già sospeso.

### Impugnazioni: durata e decorrenza

Appello e ricorso per cassazione hanno presupposti e limiti propri. L'appello non è consentito per ogni sentenza a ogni parte: l'art. 593 contiene limiti specifici. La cassazione controlla i vizi ammessi dalla legge e non è un terzo libero giudizio sul fatto. Prima di registrare la scadenza bisogna identificare rimedio, legittimato, forma del provvedimento, motivazione e avvisi.

| Ipotesi dell'art. 585 | Termine ordinario | Evento da verificare |
|---|---|---|
| Provvedimento camerale; motivazione contestuale ex art. 544, comma 1 | 15 giorni | Avviso di deposito nel primo caso; lettura del provvedimento nel secondo, per le parti presenti o da considerare presenti. |
| Motivazione non contestuale ex art. 544, comma 2 | 30 giorni | Scadenza del termine previsto per il deposito, salve le ipotesi di avviso ex art. 548. |
| Termine più lungo per motivazione complessa ex art. 544, comma 3 | 45 giorni | Termine indicato dal giudice per il deposito, coordinato con gli avvisi richiesti. |

Per l'impugnazione del difensore dell'imputato giudicato in assenza i termini aumentano di quindici giorni. Se la decorrenza è diversa per imputato e difensore, opera per entrambi il termine che scade per ultimo. Questi termini sono previsti a pena di decadenza: non si può usare sempre la data della sentenza o sempre quella della sua notificazione.

**Esempio.** Il 2 marzo 2026 il giudice legge la sentenza con motivazione contestuale; imputato e difensore sono presenti e non ricorrono regimi speciali. Il termine ordinario di quindici giorni scade il 17 marzo. Se invece la motivazione è riservata, manca il presupposto dell'esempio: si ricostruiscono termine di deposito e decorrenza pertinente prima di calcolare.

''' +t[end:]
t=t.replace('Memorizzare numeri senza testo vigente','Confondere durata, decorrenza e sospensione')
at=t.index('### Processo penale telematico')
t=t[:at]+'''### Computo e deposito

L'art. 172 esclude il giorno iniziale salvo diversa disposizione e proroga la scadenza festiva al successivo giorno non festivo. Non trasferire automaticamente al penale la regola civile sul sabato. Per il deposito telematico, nel regime applicabile, rileva l'accettazione da parte del sistema entro le ore 24 dell'ultimo giorno utile; per gli atti in ufficio rileva l'orario previsto. L'articolo disciplina anche i termini decorrenti da un deposito telematico fuori orario, collegandoli all'apertura successiva salvo diversa regola. Il capitolo 12 spiega i canali e i regimi di deposito: un'e-mail ordinaria non diventa deposito rituale per il solo fatto di essere stata letta.

''' +t[at:]
start=t.index('### Processo penale telematico');end=t.index('### Esecuzione penale essenziale',start)
t=t[:start]+'''### Processo penale telematico

Il PPT collega redazione, deposito, comunicazione, notificazione e consultazione di atti informatici. Il riferimento regolamentare è il D.M. 217/2023 con le successive modifiche, da coordinare con ufficio, soggetto, tipo di atto e fase. Il capitolo 12, nella parte dedicata al deposito penale, sviluppa il regime verificato e i casi applicativi.

Il **Portale dei Servizi Telematici** è il punto istituzionale per servizi e avvisi; il **Portale Deposito atti Penali** è uno specifico canale di deposito per i soggetti e gli atti abilitati. Le specifiche tecniche non sostituiscono la norma processuale. I documenti storici recanti la sigla DGSIA conservano la loro identificazione originaria; l'organizzazione attuale del DIT è illustrata nel capitolo 2.

Per l'ufficio il controllo minimo comprende identificativo, atto, allegati, soggetto, ricevuta, data ed esito. Per l'UPP la consultazione è limitata ai compiti e alle autorizzazioni attribuite. Un atto presente nel sistema può richiedere ulteriori verifiche di ammissibilità o tempestività; l'accessibilità tecnica non autorizza la diffusione del suo contenuto.

''' +t[end:]
start=t.index('### Esecuzione penale essenziale');end=t.index('### ',start+5)
t=t[:start]+'''### Esecuzione penale essenziale

Pronuncia, deposito e irrevocabilità sono eventi diversi. Gli artt. 648 e 650 collegano ordinariamente la forza esecutiva di sentenze e decreti penali all'irrevocabilità, secondo gli esiti delle impugnazioni e i termini previsti. Non si dichiara definitiva una condanna soltanto perché il dispositivo è stato letto.

Il **PM cura d'ufficio l'esecuzione** ai sensi dell'art. 655 e, per la pena detentiva, emette l'ordine dell'art. 656, con le sospensioni e le altre disposizioni applicabili. Il **giudice dell'esecuzione** decide le questioni di propria competenza secondo gli artt. 665–666; il magistrato e il tribunale di sorveglianza hanno le attribuzioni illustrate nel capitolo 14. Sono funzioni distinte, anche quando il fascicolo passa tra uffici della stessa sede.

La scheda deve registrare titolo, attestazione di irrevocabilità, pena, provvedimenti esecutivi, notifiche e trasmissioni. Non ricava autonomamente la pena da espiare da una semplice sottrazione: cumuli, presofferto, benefici e provvedimenti competenti vanno documentati. La custodia cautelare durante il processo non è esecuzione di una pena definitiva e non prova la colpevolezza.

''' +t[end:]
start=t.index('### Laboratorio operativo: controllo di un fascicolo penale');end=t.index('### Mappa BANDO del capitolo',start)
t=t[:start]+'''### Laboratorio svolto: dall'avviso all'imputazione

**Dossier fittizio, uffici di Bologna.** Il procedimento riguarda un delitto per il quale è prevista l'udienza preliminare, senza misure cautelari, sospensioni o discipline speciali sui termini del caso. Si dispone dei seguenti documenti, numerati per la prova.

| Documento | Dato verificato |
|---|---|
| P1 — annotazione di registro | Iscrizione della notizia e del nome il 12 gennaio 2026; indagato Luca Verdi. |
| P2 — avviso ex art. 415-bis | Notificato all'indagato e al difensore il 2 marzo 2026; deposito degli atti in segreteria. |
| P3 — istanza difensiva | Depositata il 18 marzo: richiesta di interrogatorio e produzione di due documenti. |
| P4 — invito e verbale | Invito documentato; interrogatorio eseguito il 25 marzo. |
| P5 — richiesta del PM | Richiesta di rinvio a giudizio depositata il 30 marzo. |
| P6 — indice del fascicolo trasmesso | Elenca i due documenti di P3; il secondo non è visibile nella copia di lavoro. |

**Consegna.** Compila cronologia, stato della persona, controllo del termine e nota al referente. Non decidere il merito dell'accusa.

| Campo | Soluzione compilata |
|---|---|
| Stato sino al 29 marzo | Persona sottoposta alle indagini. L'avviso del 2 marzo non basta a renderla imputato. |
| Stato dal 30 marzo | Imputato per effetto della richiesta di rinvio a giudizio ex art. 60. |
| Termine difensivo | Venti giorni dal 2 marzo, escluso il giorno iniziale: 22 marzo, domenica; scadenza prorogata a lunedì 23. |
| Richiesta di interrogatorio | Il 18 marzo è tempestiva; il PM deve procedere. Invito e verbale del 25 marzo documentano il seguito. |
| Anomalia | Secondo documento difensivo indicato nell'indice ma non visibile nella copia di lavoro; non equivale a documento mai depositato. |
| Prossima attività | Verifica della completezza del fascicolo trasmesso alla cancelleria del GUP e segnalazione al referente competente. |

**Nota pronta.** «Procedimento fittizio: verificati avviso e notifiche del 2 marzo, istanza del 18, invito e verbale d'interrogatorio del 25, richiesta di rinvio del 30. L'istanza è entro la scadenza del 23 marzo. Il secondo allegato di P3 è elencato in P6 ma non visibile nella copia consultata: si chiede riscontro dell'acquisizione e disponibilità nell'originale informatico. La scheda non esprime valutazioni di colpevolezza né attesta l'assenza dell'allegato dal fascicolo originale».

L'UPP dell'ufficio giudicante può predisporre questa scheda per il lavoro del GUP; la segreteria della Procura cura gli adempimenti del PM. Non occorre inventare un UPP presso la Procura per descrivere la collaborazione tra gli uffici.

**Variante.** Nel dossier non vi sono né invito né verbale, ma rimane la richiesta tempestiva di interrogatorio. La scheda evidenzia la mancanza e la sottopone al magistrato per la valutazione dell'art. 416; l'operatore non scrive «interrogatorio rinunciato» senza un atto che lo dimostri e non dichiara autonomamente la nullità.

**Autovalutazione, dieci punti.** Assegna due punti a ciascuno dei cinque controlli: distinzione indagato/imputato, calcolo del 23 marzo, effetto della richiesta d'interrogatorio, distinzione copia/originale, corretta attribuzione dei ruoli. Un punto se il controllo è corretto ma non motivato; zero se manca o è errato. Ripeti il caso se hai attribuito una decisione processuale al personale amministrativo.

''' +t[end:]
t=t.replace('La mappa serve a mantenere il capitolo nel suo perimetro: abbastanza procedura per lavorare, non abbastanza teoria per disperdersi.','La mappa collega le regole processuali ai prodotti richiesti: cronologia, scheda, controllo del termine e risposta motivata.')
t=t.replace('| UPP | Può supportare lettura, cronologia e organizzazione nei limiti del progetto |','| UPP dell’ufficio giudicante | Interviene nel supporto al giudice quando gli atti arrivano alla fase pertinente; non sostituisce la segreteria della Procura. |')
t=t.replace("L'UPP, se coinvolto secondo il progetto organizzativo, può aiutare a ricostruire cronologia, atti rilevanti e questioni.","L'UPP dell'ufficio giudicante può ricostruire cronologia e questioni per il giudice quando gli atti giungono a quell'ufficio; non si presume un UPP ordinario presso la Procura.")
t=t.replace('Bisogna controllare D.M., specifiche DGSIA e avvisi PST','Disciplina e casi del capitolo 12; decreti, specifiche tecniche e avvisi PST.').replace('su D.M., specifiche DGSIA e PST aggiornati','secondo la disciplina del capitolo 12 e gli avvisi istituzionali aggiornati')
t=re.sub(r'### Quiz commentato\n.*?(?=### Checklist di ripasso)', '''### Quiz commentato

1. **Quando Luca, nel dossier, assume la qualità di imputato?**
   - A. Il 12 gennaio, con l'iscrizione del nome.
   - B. Il 2 marzo, con l'avviso di conclusione delle indagini.
   - C. Il 30 marzo, con la richiesta di rinvio a giudizio.
   **Risposta corretta: C.** È l'atto di esercizio dell'azione penale indicato dall'art. 60. Le date precedenti riguardano la fase delle indagini.

2. **Il difensore chiede tempestivamente l'interrogatorio dopo l'avviso ex art. 415-bis. Quale controllo occorre?**
   - A. Verificare che il PM vi proceda e che invito e verbale siano documentati.
   - B. Considerare la richiesta irrilevante perché le indagini sono concluse.
   - C. Far decidere alla segreteria se l'interrogatorio sia utile.
   **Risposta corretta: A.** Il PM deve procedervi; l'art. 416 collega una conseguenza processuale alla richiesta di rinvio non preceduta dall'invito dovuto.

3. **Un PM chiede l'archiviazione. Quale registrazione descrive correttamente lo stato?**
   - A. Condanna definitiva.
   - B. Richiesta di archiviazione in attesa della decisione del giudice.
   - C. Archiviazione amministrativa già perfezionata dalla segreteria.
   **Risposta corretta: B.** La richiesta non è il provvedimento che definisce il procedimento; il giudice può adottare esiti differenti.

4. **Che cosa distingue il fascicolo per il dibattimento da quello delle indagini?**
   - A. Il solo formato digitale.
   - B. Il fatto che contenga soltanto le conclusioni del PM.
   - C. La selezione degli atti prevista dal codice e le acquisizioni consentite, senza trasferimento indiscriminato di tutto il materiale.
   **Risposta corretta: C.** L'art. 431 presidia formazione e contenuto; utilità per una scheda e utilizzabilità processuale non coincidono.

5. **Nell'abbreviato, quale riduzione ordinaria segue una condanna per un delitto?**
   - A. Un terzo, mentre per una contravvenzione è della metà.
   - B. Sempre la metà, come per qualsiasi reato.
   - C. Un sesto, già comprensivo di ogni beneficio successivo.
   **Risposta corretta: A.** L'ulteriore sesto dell'art. 442, comma 2-bis, dipende dalla mancata impugnazione dell'imputato e del difensore ed è applicato in esecuzione.

6. **L'annotazione preliminare nel modello 45-bis comporta che la persona sia priva delle garanzie dell'indagato?**
   - A. Sì, finché non intervenga l'iscrizione ordinaria.
   - B. No, l'art. 335-quinquies mantiene diritti e garanzie e disciplina i successivi accertamenti.
   - C. Sì, perché equivale a un'archiviazione definitiva.
   **Risposta corretta: B.** È una modalità specifica prevista in presenza dell'evidente causa di giustificazione, non una sottrazione delle garanzie né una decisione definitiva.

''',t,flags=re.S)
for s in ['vol-04-processo-penale-verifica-2026-10-03','vol-04-organizzazione-upp-verifica-2026-10-03']:
 t=t.replace('source_refs: [',f'source_refs: [\n  "sources/{s}.md",',1).replace('last_compiled_from: [',f'last_compiled_from: [\n  "wiki/sources/{s}.md",',1)
t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true')
p.write_text(t,'utf-8')
assert datetime.date(2026,3,2)+datetime.timedelta(days=20)==datetime.date(2026,3,22)
assert datetime.date(2026,3,22).weekday()==6
assert datetime.date(2026,3,2)+datetime.timedelta(days=15)==datetime.date(2026,3,17)
keys=re.findall(r'Risposta corretta: ([ABC])',t);assert keys==list('CAB CAB'.replace(' ',''))
(A/'VOL-04-penale-delta.json').write_text(json.dumps({'path':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'quizKeys':keys,'calendarChecked':True,'reviewRequired':True},indent=2),'utf-8')
print('Capitolo07 integrato; 6quiz e calendario verificati')
