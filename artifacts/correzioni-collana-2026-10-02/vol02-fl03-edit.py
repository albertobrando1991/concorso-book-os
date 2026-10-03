from pathlib import Path
import re,json,hashlib
root=Path('wiki/books/moduli/m-fl03-camere-commercio/chapters')
archive=Path('artifacts/correzioni-collana-2026-10-02/before-fl03');archive.mkdir(exist_ok=True)
source='sources/vol-02-camerale-verifica-2026-10-03'
def load(n):
 p=next(root.glob(n+'-*.md'));t=p.read_text(encoding='utf-8')
 a=archive/p.name
 if a.exists():raise RuntimeError('Non rieseguire: snapshot presente '+n)
 a.write_text(t,encoding='utf-8');return p,t
def save(p,t):
 for key,val in [('source_refs',source),('topics','topics/vol-02-camerale-registro-servizi-organi'),('last_compiled_from','wiki/'+source+'.md')]:
  t=re.sub(r'^'+key+r': \[(.*)\]$',lambda m:key+': ['+m.group(1)+', "'+val+'"]',t,count=1,flags=re.M)
 t=re.sub(r'^updated_at:.*$', 'updated_at: 2026-10-03',t,count=1,flags=re.M)
 t=re.sub(r'^volume_chapter:.*$', 'volume_chapter: '+str(29+int(p.name[:2])),t,count=1,flags=re.M)
 p.write_text(t,encoding='utf-8')
def insert(t,anchor,body):
 assert t.count(anchor)==1,anchor
 return t.replace(anchor,body.strip()+'\n\n'+anchor)
p,t=load('02')
start=t.index('La pubblicità legale non significa');end=t.index('## N-FL03-02-02')
t=t[:start]+'''La sezione ordinaria comprende, fra gli altri, società di capitali, cooperative, società di persone diverse dalle società semplici e imprenditori commerciali individuali non piccoli. Le sezioni speciali comprendono piccoli imprenditori, imprenditori agricoli e società semplici; ulteriori iscrizioni speciali identificano qualifiche previste da discipline settoriali, come l'innovazione. Non basta conoscere il nome della sezione: per risolvere il quesito occorre identificare soggetto, atto e relativo effetto.

### Tre effetti della pubblicità

**Pubblicità dichiarativa.** L'art. 2193 c.c. governa l'opponibilità: il soggetto obbligato non può opporre ai terzi un fatto soggetto a iscrizione ma non iscritto, salvo provare che essi lo conoscevano. Dopo l'iscrizione, il terzo non può opporre l'ignoranza del fatto, salve disposizioni speciali. L'atto non diventa per questo sempre valido: pubblicità e validità sono questioni diverse.

**Pubblicità costitutiva.** In una fattispecie prevista dalla legge l'iscrizione concorre a produrre un effetto giuridico. Per esempio, la società per azioni acquista personalità giuridica con l'iscrizione ai sensi dell'art. 2331 c.c. Qui l'iscrizione non serve soltanto a rendere conoscibile un effetto già prodotto.

**Pubblicità notizia.** Rende conoscibili dati e fatti senza attribuire, per ciò solo, gli effetti dichiarativi o costitutivi appena descritti. Non associare automaticamente questa categoria a ogni sezione speciale: l'art. 2 D.Lgs. 228/2001 attribuisce anche efficacia dichiarativa ex art. 2193 all'iscrizione di imprenditori agricoli, coltivatori diretti e società semplici esercenti attività agricola.

| Situazione | Qualificazione | Conseguenza da spiegare |
|---|---|---|
| Fatto soggetto a iscrizione, omessa dall'obbligato | Regola dichiarativa dell'art. 2193 | Non opponibile al terzo, salvo prova della sua conoscenza. |
| Iscrizione della costituzione di una S.p.A. | Effetto costitutivo dell'art. 2331 | Acquisto della personalità giuridica. |
| Iscrizione di un imprenditore agricolo nella sezione speciale | Eccezione all'equazione speciale/notizia | Opera anche l'art. 2193. |

### Caso: informazione conosciuta, fatto non iscritto

La traccia precisa che un fatto è soggetto a iscrizione e che l'impresa, obbligata a iscriverlo, ha omesso l'adempimento. L'impresa vuole opporlo a un terzo che nega di averlo conosciuto. La sola esistenza del fatto non basta: occorre iscrizione oppure prova della conoscenza effettiva del terzo. Se l'impresa produce soltanto una propria comunicazione mai recapitata, la traccia non dimostra quella conoscenza. Non si può inventare una presunzione favorevole all'impresa.

Se invece la traccia dichiara il fatto regolarmente iscritto e non indica una disciplina speciale, il terzo non supera l'effetto pubblicitario affermando di non avere consultato il Registro. Questo è il passaggio che distingue conoscenza reale e conoscibilità legale.

La consultazione camerale non certifica ogni qualità dell'impresa. Un'amministrazione che verifica un operatore economico deve individuare i dati pertinenti e compiere gli ulteriori controlli richiesti dal procedimento. L'iscrizione non garantisce solvibilità, correttezza di ogni attività o possesso di qualsiasi autorizzazione.

Per rispondere all'orale usa quattro passaggi: identifica l'atto, indica la pubblicità prevista, spiega l'effetto e applicalo al terzo. Evita la formula «tutto ciò che è iscritto diventa valido»: confonde conoscibilità, opponibilità e formazione dell'effetto. Evita anche «la sezione speciale informa soltanto»: trascura l'eccezione agricola e le discipline delle singole qualifiche.

''' + t[end:]
t=insert(t,'## N-FL03-02-03', '''Il REA può comprendere anche soggetti, come enti o associazioni, che esercitano attività economica in via non principale e sono tenuti alla relativa denuncia. Questo non significa che ogni associazione debba iscriversi al Registro come imprenditore commerciale: si qualifica l'attività concretamente esercitata e si distingue l'obbligo anagrafico dalla pubblicità legale.
''')
t=insert(t,'## N-FL03-02-04', '''### Conservatore, giudice e rimedi

L'ufficio del Registro cura l'istruttoria e i provvedimenti di competenza del conservatore; il giudice del Registro esercita le funzioni di vigilanza e decide i ricorsi previsti dalla legge. Non è un ordinario rapporto gerarchico fra un ufficio e il suo dirigente.

Per l'iscrizione su domanda, l'art. 2189 c.c. richiede il controllo dell'autenticità della sottoscrizione e delle condizioni di legge. Il rifiuto è comunicato al richiedente, che può ricorrere al giudice entro **otto giorni**. Contro il decreto del giudice, l'art. 2192 prevede ricorso al tribunale entro **quindici giorni dalla comunicazione**.

Il codice disciplina anche l'iscrizione omessa e la cancellazione di iscrizioni prive delle condizioni negli artt. 2190 e 2191. Queste regole vanno coordinate con l'art. 40 D.L. 76/2020: nelle procedure d'ufficio lì indicate il provvedimento conclusivo spetta al conservatore. La determinazione è comunicata entro otto giorni e il ricorso al giudice del Registro si propone entro quindici giorni dalla comunicazione. Non scambiare gli otto giorni per comunicare quel provvedimento con il termine per impugnarlo.

**Controllo rapido.** Rifiuto dell'iscrizione richiesta dall'interessato: ricorso ex art. 2189, otto giorni. Cancellazione d'ufficio adottata dal conservatore ai sensi dell'art. 40: ricorso al giudice, quindici giorni. Il termine dipende dal tipo di provvedimento, non dal fatto che entrambi provengano dal Registro.
''')
t=t.replace('Il certificato ha una funzione diversa: è il documento da richiedere quando occorre una certificazione. In una risposta orale basta questa distinzione netta. Evita di aggiungere formule su esenzioni, bolli, validità temporale o contenuti puntuali se il quesito non li richiede oppure se non hai davanti la disciplina applicabile.', '''Il certificato attesta le risultanze per gli usi consentiti, ma occorre distinguere il destinatario. Nei rapporti con pubbliche amministrazioni e gestori di pubblici servizi operano le dichiarazioni sostitutive e l'acquisizione d'ufficio secondo gli artt. 40 e 43 D.P.R. 445/2000. L'ufficio procedente non deve chiedere all'impresa un certificato camerale come adempimento ordinario al posto dell'acquisizione dei dati. Nei rapporti fra privati si identifica invece il documento richiesto e il regime applicabile.''')
t=t.replace('ma non ha valore di certificazione e non è opponibile a terzi. Quando serve una certificazione, bisogna individuare il certificato richiesto e verificare il caso concreto.', 'ma non ha valore di certificazione. Non confondere questo limite documentale con gli effetti dei fatti iscritti: l’opponibilità dipende dalla legge, in particolare dall’art. 2193 c.c. Per un uso certificativo si verifica il destinatario, ricordando la decertificazione nei rapporti con PA e gestori di pubblici servizi.')
t=t.replace('ComUnica e i servizi telematici del sistema camerale permettono di presentare pratiche e atti in modalità digitale. In concorso, la sigla conta meno della funzione: la Camera partecipa alla semplificazione degli adempimenti dell’impresa, ma ciascuna amministrazione conserva le proprie competenze.', '''La Comunicazione unica d'impresa, prevista dall'art. 9 D.L. 7/2007, è una pratica digitale presentata al Registro con modello riepilogativo e modelli destinati agli enti interessati. Collega gli adempimenti camerali, fiscali, previdenziali e assicurativi: Registro, Agenzia delle entrate, INPS e INAIL; può includere la SCIA destinata al SUAP quando pertinente. Vale anche per modifiche e cessazione.

La sequenza è: predisposizione dei modelli pertinenti, invio telematico, ricevuta e inoltro agli enti, controlli ed esiti di ciascuna amministrazione. La ricevuta consente l'avvio immediato soltanto quando sussistono i presupposti di legge; non rende lecito avviare un'attività soggetta a un'autorizzazione non ancora ottenuta. Il comma 4 vigente distingue la comunicazione immediata di codice fiscale e partita IVA dagli ulteriori dati definitivi comunicati entro quattro giorni. Questo termine non è una promessa universale di conclusione di ogni procedimento SUAP.''')
t=insert(t,'### Caso finale ragionato', '''### Quiz 7

Un fatto soggetto alla regola dichiarativa dell'art. 2193 non è stato iscritto. Quando l'obbligato può opporlo al terzo?

A. Mai, neppure se prova che il terzo lo conosceva.
B. Se prova che il terzo ne aveva conoscenza.
C. Per il solo invio della pratica, anche non ricevuta.
D. Sempre, purché esista una visura precedente.

**Risposta corretta: B.** La prova della conoscenza effettiva è l'eccezione alla non opponibilità del fatto non iscritto. L'invio non equivale all'iscrizione.

### Quiz 8

Una PA deve verificare l'iscrizione di un'impresa nel proprio procedimento. Qual è la condotta ordinaria coerente con gli artt. 40 e 43 D.P.R. 445/2000?

A. Pretendere sempre un certificato a carico dell'impresa.
B. Accettare soltanto una visura comprata dall'impresa.
C. Acquisire d'ufficio i dati e applicare il regime delle dichiarazioni sostitutive.
D. Omettere ogni verifica perché il Registro è pubblico.

**Risposta corretta: C.** La decertificazione modifica il modo di acquisire e verificare il dato, senza eliminare il controllo.
''')
t=t.replace('- D.P.R. 7 dicembre 1995, n. 581', '- codice civile, artt. 2188–2193 e 2331; D.Lgs. 228/2001, art. 2; D.L. 76/2020, art. 40; D.L. 7/2007, art. 9; D.P.R. 445/2000, artt. 40 e 43;\n- D.P.R. 7 dicembre 1995, n. 581')
save(p,t)
p,t=load('03')
t=t.replace('opera attraverso attribuzioni specifiche che lo step specialistico dovrà verificare nel testo vigente.', 'esercita i poteri attribuiti dalle norme relative a ciascun servizio.')
t=t.replace('Non confondere mediazione o arbitrato con la decisione giudiziaria.', 'Distinguere l’accordo di mediazione dalla decisione arbitrale e dai suoi effetti.')
t=insert(t,'## N-FL03-03-04', '''### Mediazione e arbitrato: chi costruisce l'esito

Nella mediazione un terzo imparziale aiuta le parti a raggiungere un accordo: la soluzione deriva dal loro consenso. Nel procedimento disciplinato dal D.Lgs. 28/2010, l'art. 12 attribuisce efficacia esecutiva all'accordo sottoscritto dalle parti e dagli avvocati quando tutte sono assistite e questi attestano la conformità alle norme imperative e all'ordine pubblico. Negli altri casi è necessaria l'omologazione del presidente del tribunale alle condizioni previste. Non basta chiamare un documento «verbale di mediazione» per attribuirgli ogni effetto.

Nell'arbitrato gli arbitri decidono la controversia affidata loro nei limiti della convenzione arbitrale. Il lodo rituale ha, dalla data dell'ultima sottoscrizione, gli effetti della sentenza, salva la disciplina dell'art. 825 c.p.c. per l'esecutività. Il mediatore non emette quel lodo; la Camera può organizzare il servizio senza essere per questo il giudice di tutte le liti commerciali.

**Caso.** Due imprese concordano durante la mediazione un pagamento rateale e sottoscrivono l'accordo. L'esito è consensuale. Se invece, dopo un procedimento arbitrale, gli arbitri stabiliscono chi deve pagare in una controversia loro devoluta, l'esito è una decisione. La distinzione riguarda chi determina la soluzione, non soltanto l'edificio in cui si svolge l'incontro.

### Protesti: cancellazione e riabilitazione

La cancellazione modifica le risultanze del Registro dei protesti secondo presupposti documentati. L'art. 4 L. 77/1955 consente al debitore che ha pagato una cambiale o un vaglia cambiario entro dodici mesi dalla levata, con interessi e spese, di chiedere la cancellazione alla Camera. I dodici mesi riguardano il pagamento: non vanno trasformati senza base normativa in un termine generale di decadenza della domanda. Per il pagamento successivo è prevista l'annotazione. Un'ulteriore istanza può fondarsi sulla levata erronea o illegittima, da dimostrare.

Il dirigente decide entro venti giorni dalla presentazione; in caso di accoglimento cura la cancellazione entro cinque giorni dalla pronuncia. Contro il rigetto o la mancata decisione, l'art. 12 D.Lgs. 150/2011 prevede ricorso al giudice di pace del luogo di residenza del debitore protestato, con rito del lavoro.

La riabilitazione dell'art. 17 L. 108/1996 è diversa: presuppone l'adempimento dell'obbligazione, l'assenza di ulteriori protesti e almeno un anno dalla levata. Il testo vigente ammette il provvedimento del presidente del tribunale oppure l'atto notarile; la successiva cancellazione si richiede al Registro. Non applicare agli assegni il percorso camerale del pagamento entro dodici mesi proprio delle cambiali e dei vaglia cambiari.

**Caso.** Una cambiale è pagata dopo otto mesi, con interessi e spese: il debitore presenta la prova del pagamento per la domanda camerale. Se il pagamento è avvenuto dopo quattordici mesi, non si usa quella stessa causale di cancellazione: si valuta l'annotazione e, ricorrendone tutti i presupposti, la riabilitazione. La data del pagamento cambia il percorso; una semplice quietanza non cancella da sola il protesto.
''')
t=insert(t,'## N-FL03-03-05', '''### Chi verifica e chi vigila

Il D.M. 93/2017 distingue verificazione periodica, controlli casuali o a richiesta e vigilanza. La verificazione periodica accerta la permanenza dell'affidabilità dello strumento e l'integrità dei contrassegni e sigilli: le frequenze dipendono dalla tipologia indicata nell'allegato IV, non esiste una scadenza unica per tutte le bilance e tutti i contatori.

| Soggetto | Compito da riconoscere |
|---|---|
| Titolare dello strumento | Cura lo strumento, conserva libretto e sigilli, richiede le verifiche dovute e comunica inizio/fine uso alla Camera entro trenta giorni. |
| Organismo accreditato con SCIA a Unioncamere | Esegue ordinariamente la verificazione periodica secondo il decreto. |
| Camera di commercio | Effettua controlli casuali e a richiesta, tiene l'elenco dei titolari e svolge la vigilanza attribuita. |
| Unioncamere | Tiene l'elenco nazionale degli organismi. |
| Organismo nazionale di accreditamento | Vigila sul mantenimento dei requisiti di accreditamento. |

L'art. 4, comma 1-bis, vigente consente anche alle Camere di eseguire la verificazione periodica quando, per la tipologia di strumento, non vi siano organismi nell'elenco: è errata una risposta che attribuisca sempre ed esclusivamente il servizio a operatori privati.

Il titolare richiede la verificazione almeno cinque giorni lavorativi prima della scadenza oppure entro dieci giorni lavorativi dalla riparazione che abbia comportato la rimozione di etichette o sigilli. L'organismo esegue entro quarantacinque giorni dalla richiesta. Questi termini hanno eventi iniziali e destinatari diversi: la scadenza periodica dello strumento non coincide con il termine per eseguire il servizio richiesto.

**Caso.** Un cliente segnala che una bilancia pesa quantità superiori a quelle effettive. Il controllo camerale a richiesta riguarda la correttezza della misura; non si risponde semplicemente «attenda la prossima verifica periodica». Si identificano strumento, titolare, luogo e fatti della segnalazione, si attiva il servizio competente e si conservano le risultanze. Un esito regolare del controllo non autorizza a cancellare gli obblighi periodici futuri.
''')
t=insert(t,'### Caso finale ragionato', '''### Quiz 7

Quale coppia è corretta?

A. Mediazione: lodo imposto dal mediatore; arbitrato: sola informazione.
B. Mediazione: accordo delle parti; arbitrato rituale: decisione mediante lodo.
C. Mediazione: cancellazione dei protesti; arbitrato: verifica degli strumenti.
D. Entrambi producono sempre un semplice parere privo di effetti.

**Risposta corretta: B.** Il mediatore facilita l'accordo; gli arbitri decidono nei limiti della convenzione. L'efficacia esecutiva va verificata secondo la disciplina del singolo esito.

### Quiz 8

Una cambiale è pagata dopo otto mesi dalla levata, compresi interessi e spese. Quale percorso è pertinente?

A. Domanda camerale di cancellazione documentando il pagamento entro dodici mesi.
B. Cancellazione automatica alla scadenza dell'ottavo mese.
C. Necessaria attesa di cinque anni in ogni caso.
D. Applicazione della stessa regola a ogni assegno protestato.

**Risposta corretta: A.** Serve l'istanza con prova dei presupposti; il pagamento non determina da solo la cancellazione e il procedimento non va esteso agli assegni.
''')
t+='\nRiferimenti di approfondimento del capitolo: D.M. 93/2017, artt. 3–5, 8–10 e 13–14; L. 77/1955, art. 4; L. 108/1996, art. 17; D.Lgs. 150/2011, art. 12; D.Lgs. 28/2010, art. 12; art. 824-bis c.p.c.\n'
save(p,t)
p,t=load('04')
start=t.index('La Camera di commercio è un ente pubblico con una propria organizzazione.');end=t.index('## N-FL03-04-02')
t=t[:start]+'''L'art. 9 L. 580/1993 individua quattro organi: Consiglio, Giunta, presidente e Collegio dei revisori dei conti. Il segretario generale è il vertice amministrativo; non è un quinto organo di quell'elenco. La distinzione permette di attribuire indirizzo, esecuzione, rappresentanza, controllo e gestione al soggetto corretto.

| Organo | Formazione e durata | Attribuzioni essenziali |
|---|---|---|
| Consiglio | Rappresentanti designati secondo l'art. 12 e nominati dal presidente della Giunta regionale; cinque anni | Statuto e regolamenti, indirizzi e programma pluriennale, approvazione di preventivo e bilancio; elezione di presidente e Giunta, nomina dei revisori. |
| Giunta | Presidente e cinque o sette componenti eletti dal Consiglio; mandato di cinque anni coincidente con quello consiliare | Organo esecutivo; predispone documenti di programmazione e bilancio e adotta gli atti nelle attribuzioni di legge. |
| Presidente | Eletto dal Consiglio; cinque anni, rinnovabile non più di due volte | Rappresenta la Camera, convoca e presiede Consiglio e Giunta. |
| Collegio dei revisori | Tre effettivi e tre supplenti; nomina del Consiglio su designazioni previste dalla legge; quattro anni | Controllo sulla gestione finanziaria e relazione sul bilancio; non sostituisce gli uffici nella gestione. |

Il Consiglio esprime le componenti economiche del territorio. L'art. 10 prevede sedici o ventidue rappresentanti dei settori secondo la dimensione camerale, ai quali si aggiungono i tre rappresentanti del comma 6 per lavoratori, consumatori e professionisti. Non memorizzare «sedici membri totali» come regola generale. Il rinnovo ordinario non è un'elezione politica universale dei residenti: segue la rappresentatività e le designazioni disciplinate dall'art. 12.

Per eleggere il presidente occorrono i due terzi dei componenti nelle prime due votazioni; dalla terza opera la maggioranza dei componenti e, in caso di ulteriore insuccesso, il ballottaggio secondo l'art. 16. La Giunta comprende rappresentanti dei settori indicati dalla legge. Per i revisori le designazioni spettano a MEF, MIMIT e presidente della Giunta regionale; il designato del MEF presiede il Collegio.

### Il segretario generale e la gestione

L'art. 20 attribuisce al segretario generale le funzioni di vertice amministrativo, con coordinamento e sovrintendenza della struttura e richiamo alle funzioni dirigenziali dell'art. 16 D.Lgs. 165/2001. La Giunta lo designa mediante procedura comparativa fra gli iscritti nell'apposito elenco; il ministro lo nomina e il presidente stipula il contratto. L'incarico dura fino a quattro anni, con possibile conferma fino a due anni, una sola volta, previa valutazione.

Il segretario generale non ha quindi lo stesso mandato quinquennale degli organi politici camerali. Dirigenti e uffici curano i compiti attribuiti dall'ordinamento e dagli atti organizzativi. L'organigramma aiuta a trovare il servizio, ma la firma di un provvedimento richiede una competenza: non deriva dalla semplice vicinanza della casella al vertice.

### Caso: dal programma alla pratica

La Camera intende sostenere la digitalizzazione delle imprese. Il Consiglio definisce indirizzi e programmazione e approva i documenti economici di propria competenza; la Giunta svolge le attribuzioni esecutive e predispone i documenti; la struttura amministrativa cura l'avviso e istruisce le domande secondo le competenze. Il presidente rappresenta l'ente, mentre il Collegio verifica la gestione finanziaria. Nessuno di questi ruoli permette di promettere a un'impresa un contributo prima dell'istruttoria.

L'urgenza non cancella le attribuzioni: la Giunta può adottare gli atti urgenti di competenza consiliare previsti dall'art. 14, con ratifica alla prima riunione successiva; il presidente può adottare quelli urgenti di competenza della Giunta secondo l'art. 16, con analoga ratifica. In prova occorre indicare potere, presupposto e passaggio di ratifica, non soltanto scrivere «decide il presidente».

''' + t[end:]
t=insert(t,'Nei bandi possono comparire istruttori, funzionari', '''### Aree, incarico EQ e progressioni

Il CCNL Funzioni locali del 16 novembre 2022 articola il personale in quattro aree: **Operatori, Operatori esperti, Istruttori, Funzionari ed Elevata Qualificazione**. Il CCNL del 23 febbraio 2026 aggiorna la disciplina. L'area individua il livello professionale; il profilo descrive attività e competenze; l'incarico di EQ assegna temporaneamente responsabilità organizzative o di alta professionalità. Essere assunto nell'area dei Funzionari ed EQ non attribuisce automaticamente quell'incarico.

La progressione fra aree cambia inquadramento e richiede la procedura comparativa prevista, con almeno metà dei posti riservati all'accesso dall'esterno. La progressione economica interna attribuisce differenziali stipendiali senza mansioni superiori: è selettiva e dipende dalle risorse. Le progressioni transitorie in deroga ai titoli seguono presupposti propri, con termine prorogato al 31 dicembre 2026, e non diventano un passaggio automatico per anzianità.

L'EQ si conferisce con atto scritto e motivato, ordinariamente fino a tre anni; la regola speciale degli enti privi di dirigenti consente fino a cinque anni. Prima di applicare l'eccezione a una Camera bisogna verificarne l'assetto. Retribuzione di posizione e di risultato remunerano l'incarico secondo il contratto, non trasformano il dipendente in dirigente.

**Caso.** Un istruttore ottiene un differenziale: resta nella propria area. Un funzionario riceve un incarico EQ: assume responsabilità a termine senza passare alla dirigenza. Un dipendente vince la progressione fra aree: cambia inquadramento. Tre esiti, tre procedimenti diversi.
''')
t=insert(t,'## N-FL03-04-05', '''**Registro pubblico e fascicolo istruttorio.** Chi chiede una visura o un atto soggetto alla pubblicità del Registro utilizza il servizio pubblico secondo le relative regole, senza dover dimostrare per ciò solo l'interesse diretto, concreto e attuale dell'accesso documentale. Diversa è la domanda di un concorrente che vuole gli allegati riservati di una pratica di contributo: si qualifica l'istanza, si verificano presupposti, controinteressati e limiti e si valuta un eventuale accesso parziale. Non si nega una normale visura invocando genericamente la privacy e non si invia un intero fascicolo soltanto perché riguarda un'impresa iscritta.
''')
t=insert(t,'### Caso finale ragionato', '''### Quiz 7

Quale soggetto non è fra i quattro organi elencati dall'art. 9 L. 580/1993?

A. Il Consiglio.
B. Il presidente.
C. Il Collegio dei revisori.
D. Il segretario generale.

**Risposta corretta: D.** È il vertice amministrativo disciplinato dall'art. 20. La Giunta completa l'elenco dei quattro organi.

### Quiz 8

Un funzionario camerale riceve un incarico di EQ. Che cosa ne consegue?

A. Diventa automaticamente dirigente.
B. Assume una responsabilità a termine, distinta dall'area di inquadramento.
C. È eletto componente della Giunta.
D. Ottiene necessariamente una progressione tra aree.

**Risposta corretta: B.** Area, incarico e progressione sono istituti distinti; il nome dell'area non attribuisce da solo l'incarico.
''')
t=t.replace('- fonti ARAN sul comparto e sul CCNL Funzioni Locali applicabile;', '- CCNL Funzioni locali 16 novembre 2022, artt. 12 e 18, e CCNL 23 febbraio 2026, artt. 12–16 e 19;')
save(p,t)
p,t=load('01')
t=t.replace('I bandi camerali acquisiti nel 2026 mostrano profili amministrativi e istruttori collegati a servizi camerali, supporto organizzativo, comunicazione istituzionale, servizi anagrafici, tutela del mercato e servizi promozionali. Questo conferma l’utilità di M-FL03 come modulo breve e operativo.', 'Gli esempi di questo capitolo sono scenari didattici compositi: combinano attività amministrative, anagrafiche, promozionali e di tutela del mercato per allenare la lettura del profilo. Non riproducono il programma di un singolo bando né provano la frequenza di una materia nelle selezioni.')
t=t.replace('Leggi il seguente estratto sintetico di bando:', 'Leggi il seguente avviso simulato, costruito per esercizio e non tratto da una procedura reale:')
save(p,t)
p,t=load('05')
t=t.replace('Il campione richiamato nel capitolo è reale ma non va copiato meccanicamente: ogni nuova procedura richiede il controllo della versione vigente del bando, degli allegati, delle rettifiche e delle date.', 'Gli esempi di profilo e gli scenari del capitolo sono compositi, costruiti per esercizio; non riproducono una specifica selezione. Per applicare il laboratorio a una procedura reale occorre leggere il suo bando con allegati, rettifiche e date.')
t=t.replace('l’utente necessità','l’utente necessita').replace('non inventarlo: segnalo come dubbio','non inventarlo: segnalalo come dubbio')
t=t.replace('| Quali dati si possono inviare? | Valuta titolo della richiesta, canale, dati personali e limiti applicabili; non inviare indistintamente informazioni relative a terzi. |', '| Quali dati si possono inviare? | Se si chiede una visura o un atto pubblico del Registro, usa il relativo servizio senza imporre un interesse qualificato. Per allegati di un fascicolo istruttorio, qualifica invece l’accesso e verifica presupposti, controinteressati e limiti. |')
t=t.replace('Per i dati relativi a terzi applico le regole su accesso, riservatezza e protezione dei dati, evitando una trasmissione non verificata.', 'Distinguo la consultazione dei dati pubblici del Registro dalla richiesta di documenti di un fascicolo istruttorio: per la prima indico il servizio di pubblicità, per la seconda applico il regime di accesso pertinente e i suoi limiti.')
t=insert(t,'### Da sapere in 5 righe', '''**Variante risolta.** L'impresa concorrente chiede soltanto la visura ordinaria: non deve dimostrare un interesse qualificato come nell'accesso documentale. Se chiede invece relazioni tecniche e allegati personali presentati dall'altra impresa per un contributo, la pubblicità del Registro non basta. L'ufficio individua il fascicolo e il regime della domanda, coinvolge gli eventuali controinteressati e motiva l'accesso, il limite o il differimento; considera l'oscuramento dei dati non necessari. La parola «concorrente» non determina da sola né accoglimento né diniego.
''')
t=t.replace('C. scegliere il valore più prudente.\nD. scrivere «da verificare» e indicare il canale ufficiale da controllare;', 'C. scegliere il valore più prudente;\nD. scrivere «da verificare» e indicare il canale ufficiale da controllare.')
save(p,t)
print('Modificati cinque capitoli, snapshot preservati.')
