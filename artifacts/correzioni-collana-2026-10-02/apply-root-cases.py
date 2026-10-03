from pathlib import Path
import importlib.util
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
ref='sources/vol-01-candidatura-casi-correzioni-2026-10-03.md';u.REF=ref
for topic in ['casi-pratici','quesiti-situazionali','concorsi-pubblici']:
 p=Path('wiki/topics')/(topic+'.md');assert p.exists(),p
 with p.open('a',encoding='utf8') as f:f.write('\n\n## Candidatura e applicazioni — 3 ottobre 2026\n\n[[sources/vol-01-candidatura-casi-correzioni-2026-10-03]] verifica misure di partecipazione e ambito DPR487, quattro dossier risolti e otto situazionali con chiavi bilanciate.\n')
s='casi-pratici-problem-solving-amministrativo';t=u.read(s)
def block(n,nextn,new):
 global t
 a=t.index('## Caso '+str(n)+' -');b=t.index('## Caso '+str(nextn)+' -',a)
 t=t[:a]+new+'\n\n'+t[b:]
block(1,2,'''## Caso 1 - Istanza incompleta

### Dossier e consegna

Il Comune fittizio di Rivafonte riceve una domanda individuale, non competitiva, di contributo per un intervento domestico. Il regolamento descritto nella traccia ammette l’integrazione entro **10 giorni dalla ricezione della richiesta**. Mancano relazione tecnica e certificato di residenza; la residenza è però dichiarata e verificabile dall’ufficio, mentre la relazione non è detenuta da altre PA. Il termine finale della pratica è 30 giorni; la traccia non dichiara una sospensione già disposta. Redigi la richiesta istruttoria e indica che cosa controllare dopo.

### Soluzione svolta

Il responsabile acquisisce d’ufficio il dato sulla residenza secondo l’art. 18 della legge241/1990 e l’art.43 DPR445/2000; chiede soltanto la relazione tecnica mancante. Non presume che ogni richiesta fermi automaticamente il termine finale: verifica separatamente i presupposti di sospensione e ne documenta l’eventuale applicazione.

> Oggetto: domanda di contributo — integrazione della relazione tecnica.
>
> Per completare l’istruttoria occorre la relazione tecnica prevista dal regolamento indicato nel dossier. Si invita a trasmetterla mediante il portale della pratica entro dieci giorni dalla ricezione della presente richiesta. La verifica della residenza sarà svolta d’ufficio sulla dichiarazione resa. Questa comunicazione non anticipa la decisione sul contributo.

Alla scadenza l’ufficio verifica ricezione, contenuto e sufficienza dell’integrazione. L’eventuale esito negativo richiede la valutazione della disciplina applicabile, incluse le garanzie dell’art.10-bis ove dovute: non si copia automaticamente un diniego dalla richiesta istruttoria.

**Autoverifica:** documento da chiedere: relazione tecnica; documento da acquisire d’ufficio: dato di residenza; termine dell’integrazione:10 giorni dal ricevimento, perché lo assegna il dossier; sospensione del termine finale: da verificare e motivare, non implicita.''')
block(2,3,'''## Caso 2 - Richiesta di accesso con dati di terzi

### Dossier e consegna

Un’associazione presenta espressamente un’istanza di **accesso civico generalizzato** per conoscere importi e criteri dei contributi assistenziali comunali dell’ultimo anno. Il fascicolo contiene nomi, indirizzi e diagnosi. L’ente dispone già di una tabella per importi e tipologia di intervento, che può essere resa non identificativa eliminando anche dettagli indiretti; la traccia esclude che i dati residui consentano reidentificazione. Non è stata chiesta tutela di una posizione personale qualificata. Proponi un esito motivato entro il termine applicabile.

### Soluzione svolta

La richiesta va trattata secondo l’art.5, comma2, D.Lgs.33/2013. Il termine è **30 giorni**, con le sospensioni previste se vengono individuati controinteressati. L’ufficio valuta la loro presenza in base al pregiudizio concreto, senza equiparare ogni terzo nominato a un controinteressato necessario.

La soluzione del dossier è l’**accoglimento parziale**, rendendo conoscibili importi e criteri nella tabella già detenuta, con oscuramento degli elementi identificativi e sanitari non ostensibili. Non si pubblica il fascicolo integrale sul sito e non si forniscono diagnosi per dimostrare la trasparenza. Per la pubblicazione dei benefici, l’art.26, comma4, protegge anche gli identificativi da cui si ricavino salute o disagio economico-sociale.

> L’istanza è accolta limitatamente ai dati sugli importi e sui criteri indicati nella tabella allegata, privata degli elementi identificativi e delle informazioni sanitarie. Le parti escluse rivelano condizioni personali protette e non sono necessarie alla conoscenza dell’impiego delle risorse richiesta. La limitazione è motivata ai sensi dell’art.5-bis; sono indicati i rimedi previsti dall’art.5.

**Controllo:** oscurare il solo nome basta? No, se indirizzo o combinazione di dettagli identificano ancora la persona. Si può negare tutto solo dicendo “privacy”? No: occorre motivare il limite e valutare la parte ostensibile. Nel dossier l’allegato utilizzabile esiste già: non si impone di creare nuovi documenti.''')
block(3,4,'''## Caso 3 - Ritardo nel procedimento

### Dossier e consegna

Una procedura comunale individuale ha un termine di **30 giorni** fissato dalla disciplina richiamata nella traccia. Il termine è scaduto, senza sospensioni o interruzioni; siamo al giorno33. Il dossier esclude che operino silenzio-assenso o silenzio-rigetto. L’istruttoria è ferma per una richiesta a un altro ufficio dello stesso ente. Il cittadino sollecita e chiede se la domanda sia ormai accolta. Redigi una risposta e il percorso interno.

### Soluzione svolta

Il silenzio è **inadempimento**, non esito favorevole. L’ufficio ricostruisce le date e la fase mancante, sollecita il collega competente e attiva il responsabile del procedimento; non ordina al cittadino di ottenere da sé i dati interni. Il ritardo non consente di inventare una proroga retroattiva.

> Il termine della pratica risulta scaduto e l’istruttoria è ancora in corso per l’acquisizione interna indicata. La mancata risposta non equivale ad accoglimento nel regime applicabile. Il responsabile ha attivato il completamento della fase mancante. È possibile rivolgersi al soggetto titolare del potere sostitutivo, individuato e pubblicato dall’amministrazione ai sensi dell’art.2 della legge241/1990, oltre alle tutele previste.

L’ufficio rende disponibile il riferimento effettivo del sostituto e registra l’eventuale attivazione. Nel regime dell’art.2, comma9-ter, il sostituto conclude entro un termine pari alla **metà di quello originario**, quindi15 giorni nell’ipotesi data, attraverso gli uffici o un commissario. Il conteggio si collega all’attivazione del potere sostitutivo: non si sommano quindici giorni come proroga spontanea della pratica.

**Controllo:** l’altro ufficio giustifica l’inerzia verso il cittadino? No. Il ritardo prova automaticamente un diritto al contributo o al risarcimento? No: esito sostanziale e responsabilità richiedono i rispettivi presupposti.''')
block(7,8,'''## Caso 7 - Acquisto urgente di beni o servizi

### Dossier e consegna

Il Comune deve acquisire assistenza informatica per **18.000 euro al netto IVA**, valore complessivo senza rinnovi. La necessità è ravvicinata per un ritardo organizzativo dell’ufficio, ma non vi sono eventi imprevedibili o pericoli che fondino una procedura di emergenza. Copertura disponibile, assenza di interesse transfrontaliero certo, fornitore non uscente; la verifica del dossier esclude una convenzione obbligatoria pertinente e individua il servizio sul MePA. Il fornitore propone di iniziare su telefonata e regolarizzare gli atti dopo. Indica procedura e condizioni per l’avvio.

### Soluzione svolta

Il servizio può ricadere nel **diretto dell’art.50, comma1, lettera b**, perché inferiore a140.000 euro. La motivazione deve riguardare scelta, idoneità, prezzo e fabbisogno; il semplice ritardo dell’ufficio non crea somma urgenza. Il RUP è nominato nel primo atto di avvio, si verificano copertura, competenza e requisiti, e la decisione dell’art.17, comma2, identifica prestazione, importo e operatore.

La trattativa diretta sul MePA coinvolge un solo operatore; non sostituisce gli atti e i controlli. L’ufficio acquisisce il CIG attraverso il flusso digitale applicabile e formalizza il contratto nelle forme consentite. L’eventuale esecuzione anticipata segue l’art.50, comma6, dopo la verifica dei requisiti e con disposizione competente: non nasce dalla telefonata informale.

> Non è autorizzato l’avvio sulla sola intesa telefonica. L’ufficio avvia il percorso di affidamento diretto nel rispetto degli obblighi di acquisto e della copertura, descrive le prestazioni e documenta la scelta. L’inizio del servizio seguirà la stipula o un legittimo provvedimento di esecuzione anticipata, con controlli e tracciabilità.

**Controllo:** il valore modesto esonera da CIG e motivazione? No, nel caso ordinario dato. Urgenza percepita e somma urgenza sono sinonimi? No. Un incarico urgente di150.000 euro avrebbe la stessa base del diretto? No: cambia la fascia, come spiegato nel Capitolo9.''')
u.save(s,t,['V01-37'],ref)
s='quesiti-situazionali-soft-skills';t=u.read(s)
a=t.index('### Quesito 1 -');b=t.index('![Figura 18.6',a)
items=[
('Utente irritato','Un cittadino lamenta il ritardo di una pratica. Sei allo sportello, puoi vedere lo stato generale ma non decidere l’esito. Non emerge un pericolo immediato.',[
'Ascolti, controlli lo stato accessibile e registri il sollecito nel canale previsto.',
'Invii subito al dirigente una richiesta di priorità, senza consultare lo stato disponibile.',
'Indichi il termine generale della procedura e inviti a ricontattare l’ufficio alla sua scadenza.',
'Fissi un appuntamento con il responsabile e assicuri che in quella sede arriverà la decisione.'], 'A','A usa le informazioni disponibili e lascia traccia. B anticipa un’escalation senza verificare. C non accerta se il termine sia già scaduto. D promette un esito fuori dalla tua competenza.'),
('Dati di un familiare','Una persona chiede al telefono lo stato della pratica del fratello. La parentela è dichiarata, ma identità e titolo non sono verificati. La procedura dell’ente prevede un canale per le deleghe.',[
'Comunichi soltanto lo stato sintetico, evitando documenti e informazioni economiche di dettaglio.',
'Richiami il numero indicato dal chiamante per ottenere una conferma verbale dal fratello.',
'Spieghi il percorso di delega e verifica prima di comunicare informazioni sulla pratica.',
'Invii al chiamante il modulo di accesso e confermi che la pratica del fratello è presente.'], 'C','C protegge i dati e orienta al canale previsto. A rivela comunque dati della pratica. B non verifica affidabilmente identità e titolo. D conferma un’informazione personale prima dei controlli.'),
('Collega in difficoltà','Un collega nuovo ripete un errore di classificazione. Le registrazioni restano recuperabili, non vi sono scadenze immediate e il confronto formativo non è ancora stato tentato.',[
'Proponi al responsabile di togliere al collega tutte le protocollazioni finché non sarà formato.',
'Rivedi con lui la procedura e i casi errati, concordando un controllo successivo.',
'Riclassifichi i documenti a fine giornata e rinvii il confronto finché il carico sarà minore.',
'Invii al gruppo un promemoria generale, evitando di esaminare insieme gli errori già commessi.'], 'B','B interviene sulla causa e verifica l’apprendimento. A può risultare prematura rispetto ai fatti. C corregge l’effetto ma rinvia il recupero. D può aiutare, ma non chiarisce la difficoltà concreta né ripara i casi.'),
('Pressione di un conoscente','Un conoscente chiede una verifica fuori canale sulla propria pratica. Non sei assegnato a quel fascicolo e non hai una ragione di servizio per consultarlo.',[
'Chiedi a un collega assegnato al settore di anticiparti soltanto la data prevista di conclusione.',
'Consulti il solo stato della pratica e poi lo rimandi al portale per ogni altra informazione.',
'Raccogli la richiesta sul telefono personale per inoltrarla all’ufficio quando hai un momento.',
'Indichi il canale ufficiale e spieghi che non puoi effettuare quella verifica informale.'], 'D','D mantiene ruolo e imparzialità. A sposta la richiesta informale su un collega. B accede senza ragione di servizio. C usa un percorso personale non previsto e senza adeguata tracciabilità.'),
('Errore scoperto in ritardo','Hai inviato a un ufficio interno un allegato con dati personali eccedenti. Non sai chi l’abbia aperto. La procedura interna impone immediata segnalazione al referente competente.',[
'Attivi subito la segnalazione, descrivi i dati coinvolti e segui le misure di contenimento.',
'Chiedi prima conferma a tutti i destinatari e segnali soltanto se qualcuno ha letto l’allegato.',
'Invii una versione corretta e conservi entrambe le copie per la verifica periodica del responsabile.',
'Chiedi la cancellazione ai destinatari e rinvii la valutazione finché non confermano tutti.'], 'A','A segue il flusso e consente valutazione tempestiva. B e D ritardano la segnalazione prescritta. C corregge la circolazione futura, ma omette l’attivazione immediata. Non spetta al singolo impiegato decidere da solo se notificare al Garante.'),
('Carico di lavoro e scadenza','Devi chiudere una lavorazione con scadenza oggi; il collega chiede aiuto per un compito rinviabile. Puoi offrire quindici minuti senza compromettere la tua scadenza.',[
'Accetti l’intero compito e chiedi al responsabile una proroga della tua scadenza.',
'Rinunci a ogni aiuto e chiedi al collega di rivolgersi direttamente al dirigente.',
'Concordi un aiuto limitato e un seguito successivo, mantenendo la priorità della scadenza.',
'Rimetti al responsabile la scelta tra le due attività e nel frattempo attendi indicazioni.'], 'C','C usa il margine indicato senza perdere la priorità. A mette a rischio la scadenza per un compito rinviabile. B trascura una collaborazione sostenibile. D trasferisce una decisione gestibile e interrompe il lavoro.'),
('Regola non chiara','Un utente domanda se possiede un requisito. Puoi consultare subito la fonte ufficiale, ma il testo presenta un dubbio interpretativo reale e non puoi decidere l’ammissione.',[
'Leggi il requisito e indichi l’interpretazione che l’ufficio ha usato in una procedura precedente.',
'Spieghi il dubbio, chiedi verifica al competente e indichi un canale per il riscontro.',
'Consigli di presentare la domanda e assicuri che il dubbio non causerà esclusione.',
'Consegni il testo della norma e inviti l’utente a ricontattare lo sportello dopo averlo letto.'], 'B','B evita promesse e organizza un riscontro affidabile. A non verifica identità di disciplina e contesto. C garantisce un esito che non puoi assicurare. D fornisce la fonte ma lascia irrisolto il bisogno di chiarimento.'),
('Conflitto tra colleghi','Due colleghi discutono davanti al pubblico su chi debba trattare una pratica. Puoi mantenere la ricezione degli utenti mentre il responsabile chiarisce l’assegnazione.',[
'Decidi pubblicamente a chi spetta la pratica sulla base della consuetudine dell’ufficio.',
'Sospendi la ricezione degli utenti finché il responsabile non abbia risolto il confronto.',
'Servi gli utenti in attesa e lasci che i colleghi concludano la discussione allo sportello.',
'Sposti il confronto fuori dall’area pubblica e mantieni il servizio durante il chiarimento.'], 'D','D tutela continuità e gestione riservata del conflitto. A decide senza accertare la competenza. B interrompe un servizio che il dossier consente di mantenere. C limita l’attesa ma lascia proseguire il disservizio visibile.')
]
new=''
for i,(title,scenario,opts,key,why) in enumerate(items,1):
 new+=f'### Quesito {i} - {title}\n\n**Scenario.** {scenario}\n\n'+ '\n'.join(f'{chr(65+j)}. {opt}' for j,opt in enumerate(opts))+f'\n\n**Risposta più efficace: {key}.** {why}\n\n'
t=t[:a]+new+t[b:];u.save(s,t,['V01-38'],ref)
u.record()
