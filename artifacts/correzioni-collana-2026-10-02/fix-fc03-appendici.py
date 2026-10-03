from pathlib import Path
import re
B=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters')
def f(prefix):return next(B.glob(prefix+'*.md'))
def add(prefix,heading,text):
 p=f(prefix);s=p.read_text(encoding='utf8');assert heading in s;s=s.replace(heading,text.strip()+'\n\n'+heading,1);p.write_text(s,encoding='utf8')
add('appendice-a','### Materie da attivare','''### Poteri, atti e garanzie della vigilanza

Il d.lgs. 124/2004 disciplina il raccordo fra accertamento, regolarizzazione e tutela; il d.lgs. 149/2015 istituisce l'INL e organizza il coordinamento. Le modifiche del 2024 hanno superato i ruoli ispettivi ad esaurimento di INPS e INAIL e rafforzato i rispettivi organici: non è corretto descrivere ogni ispettore dei due istituti come personale assorbito dall'INL. Il coordinamento evita duplicazioni, mentre la competenza concreta discende da legge, funzione e qualifica del personale.

L'accesso ispettivo consente i controlli nei luoghi e nelle attività soggetti a vigilanza, l'identificazione dei lavoratori, l'acquisizione di dichiarazioni e l'esame della documentazione pertinente, nei limiti dei poteri conferiti. Non è una perquisizione penale generalizzata. Documenti, dichiarazioni e riscontri vanno distinti dalle valutazioni giuridiche. Se emergono fatti penalmente rilevanti si seguono i poteri e gli obblighi propri della qualifica, senza confondere sanzione amministrativa, recupero contributivo e notizia di reato.

L'articolo 13 prevede un **verbale di primo accesso**, consegnato al termine delle attività iniziali, con identificazione dei lavoratori e modalità d'impiego, attività svolte, dichiarazioni ricevute e richieste documentali pertinenti. La chiusura dell'accertamento si esprime nel **verbale unico di accertamento e notificazione**: riporta gli esiti motivati, le fonti di prova, le violazioni e gli strumenti di regolarizzazione e tutela. Una richiesta di documenti non equivale a una contestazione definitiva; un rilievo non può fondarsi su una formula priva dei fatti che lo sostengono.

### Le due diffide e la conciliazione

| Istituto | Oggetto ed effetto | Distinzione decisiva |
| --- | --- | --- |
| Diffida alla regolarizzazione, art. 13 | Per inosservanze materialmente sanabili: invita a rimuoverle e consente il trattamento sanzionatorio agevolato se si adempie alle condizioni. | Non liquida da sola ogni credito salariale. |
| Diffida accertativa, art. 12 | Intima il pagamento di crediti patrimoniali del lavoratore emersi dagli accertamenti; può acquistare efficacia esecutiva. | Non è il recupero dei contributi dovuti all'ente. |
| Conciliazione monocratica, art. 11 | Composizione davanti al funzionario nei casi previsti, su diritti patrimoniali del lavoratore. | Non permette di rinunciare liberamente ai contributi dovuti per legge. |

Per la diffida dell'articolo 13, nel quadro generale, la regolarizzazione avviene entro trenta giorni dalla notificazione del verbale; segue il pagamento entro quindici giorni dalla scadenza del termine di regolarizzazione, secondo la misura agevolata prevista. Si controllano sempre le discipline speciali della violazione: non ogni illecito è sanabile e non ogni atto usa gli stessi termini. L'adempimento tardivo o parziale non dà automaticamente il beneficio.

Per la **diffida accertativa** il datore può, entro trenta giorni dalla notifica, promuovere il tentativo di conciliazione oppure presentare ricorso al direttore dell'ufficio che ha adottato l'atto, notificandolo anche al lavoratore. Il ricorso sospende l'esecutività ed è deciso entro sessanta giorni; non va descritto come silenzio-rigetto automatico allo scadere. L'accordo conciliativo fa perdere efficacia alla diffida nei confronti delle parti interessate; senza iniziativa nel termine, oppure dopo esito negativo della conciliazione o rigetto del ricorso, si forma il titolo esecutivo secondo l'articolo 12. La vecchia necessità di una successiva validazione non appartiene alla disciplina riformata nel 2020.

Nella conciliazione monocratica l'accordo e l'adempimento degli obblighi retributivi e contributivi possono produrre l'estinzione del procedimento ispettivo nei limiti di legge. L'accordo sul credito del lavoratore non trasforma però i contributi pubblici in un bene liberamente disponibile. Occorre leggere separatamente retribuzioni riconosciute, imponibile contributivo, pagamento e presupposti degli effetti estintivi.

### Recuperi, sanzioni e rimedi: individuare prima l'atto

Il credito per contributi INPS o premi INAIL appartiene all'ente; il credito salariale appartiene al lavoratore; la sanzione amministrativa punisce una violazione. Possono originare dallo stesso fatto, ma hanno destinatari, disciplina e rimedi differenti. Il verbale documenta gli accertamenti: gli atti successivi di recupero e riscossione seguono le rispettive regole. Non si applica la tutela contro la diffida salariale a ogni avviso di addebito.

Contro gli atti che riguardano la sussistenza o qualificazione del rapporto assumono rilievo, nei casi previsti, i rimedi amministrativi dell'articolo 17 del d.lgs. 124/2004; le ordinanze-ingiunzione e gli atti di recupero hanno i propri strumenti amministrativi o giudiziali. Il destinatario individua atto, autorità, termine, effetto sospensivo ed eventuale tutela davanti al giudice. Il ricorso amministrativo non sospende sempre e automaticamente ogni obbligo: l'effetto va ricavato dalla norma del rimedio utilizzato.

**Caso svolto.** L'accertamento riscontra 1.200 euro di retribuzioni non corrisposte e contributi omessi. Sono due crediti diversi. La diffida accertativa tutela il lavoratore per i 1.200 euro; l'ente quantifica e recupera i contributi secondo la relativa disciplina. Il datore presenta ricorso contro la diffida entro trenta giorni e lo notifica al lavoratore: si sospende l'esecutività di quella diffida, senza poter dedurre che sia sospeso anche qualunque recupero contributivo. Se la contestazione riguarda una registrazione materialmente sanabile, si esamina inoltre la diversa diffida dell'articolo 13. La soluzione separa tre strumenti anziché chiamarli tutti «multa».

Questa appendice fornisce la sequenza essenziale e i principali istituti procedurali. Per un programma ispettivo specialistico restano da studiare gli specifici rapporti di lavoro, gli imponibili, le singole violazioni e la sicurezza tecnica richiesti dal bando: non è una promessa di copertura esaustiva di ogni concorso di vigilanza.''')

p=f('appendice-b');s=p.read_text(encoding='utf8')
replacements={
'Evento dannoso collegato all\'attività lavorativa secondo la disciplina applicabile.':'Evento dovuto a causa violenta in occasione di lavoro, nel campo assicurativo previsto; comprende l’in itinere nei presupposti di legge.',
'Patologia collegata all\'attività lavorativa secondo criteri e procedure previsti.':'Patologia causata dal lavoro con azione generalmente lenta e progressiva; le condizioni tabellari incidono sulla prova del nesso.',
'Termine legato al finanziamento dell\'assicurazione e al rapporto assicurativo.':'Somma dovuta per finanziare la copertura: nella forma ordinaria dipende da retribuzioni assicurate e tasso della lavorazione; esistono premi speciali.',
'Non entrare in calcoli o dettagli se il bando non li richiede.':'Non confonderlo con l’indennizzo pagato all’assicurato; distinguere rata e regolazione nell’autoliquidazione.',
'Concetto richiamato nel sistema INAIL e nella fonte di riforma consolidata.':'Menomazione dell’integrità psicofisica valutabile medico-legalmente, distinta dalla perdita di reddito.',
'Usalo con cautela: per articoli, percentuali o tabelle serve verifica ufficiale.':'Regime d.lgs. 38/2000: sotto 6% franchigia, 6–15% capitale, dal 16% rendita; esempio del capitolo 4.',
'Non promettere riconoscimenti automatici: servono istruttoria, accertamento e comunicazione.':'Automaticità contro l’omissione del datore e accertamento del rischio sono compatibili; per autonomi valgono limiti specifici.',
'| Previdenza / Assicurazione sociale INAIL | La previdenza INPS riguarda tutele e posizioni previdenziali; l\'assicurazione INAIL riguarda rischi ed eventi connessi al lavoro. | Chiamare tutto genericamente "previdenza". |':'| Previdenza / Assicurazione sociale INAIL | L’assicurazione INAIL è parte della previdenza sociale, con rischi e prestazioni propri. | Escludere INAIL dalla previdenza o attribuirgli tutte le prestazioni INPS. |',
'La previdenza richiama soprattutto il contesto INPS: contributi, posizione dell\'utente, requisiti, domanda e prestazioni. L\'assicurazione sociale, nel contesto INAIL, richiama invece rischio lavorativo, infortunio, malattia professionale, prevenzione e tutela. La prestazione non è un diritto automatico, ma l\'eventuale esito di un procedimento fondato su presupposti, istruttoria e comunicazione corretta.':'La previdenza comprende diverse assicurazioni sociali, incluse quelle INPS e INAIL. Nell’INAIL si distinguono rischio lavorativo, evento, nesso e tutela. L’automaticità protegge il dipendente dall’omissione assicurativa del datore; non elimina l’accertamento dei presupposti. Prestazione e procedimento sono dunque concetti diversi, senza negare il diritto riconosciuto dalla legge.'}
for a,b in replacements.items(): assert a in s,a;s=s.replace(a,b)
p.write_text(s,encoding='utf8')

p=f('appendice-f');s=p.read_text(encoding='utf8')
s=s.replace('Questa appendice ne conserva la copertura minima per orientamento, ma la scrittura pubblicabile deve decidere se trattarlo come estensione M-FC03 o rinviarlo a un modulo sociale/sanitario.','Questa appendice offre il raccordo amministrativo e assicurativo INAIL. La preparazione professionale del servizio sociale è fuori dal suo perimetro: il bando va integrato con un percorso specifico su metodologia, legislazione sociale e servizi territoriali. Non si considera questa mappa una copertura completa del profilo.')
a=s.index('### Specifica struttura madre');b=s.index('### Diritto dell',a);s=s[:a]+s[b:]
s=s.replace('Corruzione, concussione, peculato e abuso non sono etichette generiche della cattiva amministrazione. La disciplina vigente va letta nel codice penale e nelle sue modifiche; il manuale deve formare il metodo di distinzione, non congelare formule o pene suscettibili di intervento legislativo.','Il peculato dell’articolo 314 riguarda l’appropriazione del denaro o della cosa mobile altrui di cui il pubblico agente ha possesso o disponibilità per l’ufficio; la concussione dell’articolo 317 implica costrizione abusiva alla dazione o promessa indebita. Nella corruzione degli articoli 318–319 rileva il patto illecito collegato alla funzione o a un atto contrario ai doveri. L’articolo 323, abuso d’ufficio, è stato abrogato dalla legge 114/2024: non va studiato come fattispecie vigente. L’articolo 314-bis, indebita destinazione di denaro o cose mobili, ha propri presupposti di destinazione vincolata, condotta ed evento intenzionale; non reintroduce ogni precedente ipotesi di abuso. Si distingue sempre la violazione amministrativa dagli elementi di un reato.')
p.write_text(s,encoding='utf8')
add('appendice-f','### Elementi di processo civile','''### Distinzioni civilistiche applicate

Nella responsabilità **contrattuale**, articolo 1218 c.c., il debitore che non esegue esattamente la prestazione risponde se non prova l'impossibilità derivante da causa a lui non imputabile; il creditore prova il titolo e allega l'inadempimento, provando danno e nesso quando chiede il risarcimento. Nella responsabilità **extracontrattuale**, articolo 2043, il danneggiato deve provare fatto, dolo o colpa, danno ingiusto e nesso, salvi i regimi speciali. Non basta dunque chiamare una vicenda «danno» per scegliere il regime.

La **nullità** riguarda vizi radicali, come la mancanza di un elemento essenziale o la contrarietà a norme imperative nei casi previsti; l'**annullabilità** protegge, tra l'altro, contro incapacità e vizi del consenso. La **risoluzione** opera su un contratto validamente formato per cause successive, come l'inadempimento non di scarsa importanza; il **recesso** è lo scioglimento unilaterale consentito da legge o contratto. Una fornitura valida ma non consegnata pone quindi un problema di adempimento e rimedi, non prova da sola la nullità originaria.

Il capitolo 12 del modulo Agenzie fiscali, sezioni «Patologie del contratto» e «Responsabilità», sviluppa le distinzioni e i relativi casi civilistici. Nel contesto INAIL il danno biologico assicurato e il risarcimento civile non coincidono: il primo segue presupposti e indennizzi dell'assicurazione sociale; il secondo richiede il titolo di responsabilità e può porre questioni di danno differenziale e azioni dell'Istituto.''')
add('appendice-f','### Diritto del lavoro, legislazione sociale e sicurezza','''### Il rito del lavoro e le controversie previdenziali

Le controversie individuali di lavoro seguono il rito degli articoli 409 e seguenti c.p.c.; quelle in materia di previdenza e assistenza obbligatorie sono regolate dagli articoli 442 e seguenti. Il giudice ordinario in funzione di giudice del lavoro conosce delle controversie sui diritti alle prestazioni secondo le regole di giurisdizione e competenza. Non si sceglie il TAR per il solo fatto che la controparte sia INPS o INAIL.

La domanda si propone con ricorso che individua giudice, parti, oggetto, fatti, elementi di diritto, mezzi di prova e documenti, secondo l'articolo 414. La costituzione del convenuto, l'udienza, i poteri istruttori e la decisione seguono il rito speciale. Allegazioni e prove vanno preparate tempestivamente: la concentrazione del rito non elimina il contraddittorio. Per le controversie previdenziali si verificano inoltre domanda amministrativa, eventuali procedimenti amministrativi necessari e condizioni dell'articolo 443, senza confondere improcedibilità e decadenza dal diritto.

L'accertamento tecnico preventivo obbligatorio dell'articolo 445-bis riguarda le controversie sanitarie espressamente elencate, tra cui invalidità civile e prestazioni della legge 222/1984. Non è un passaggio universale per ogni lite pensionistica o INAIL. La controversia sul requisito contributivo non diventa una perizia sanitaria perché riguarda una pensione. Nei casi INAIL si distinguono il disaccordo sulla qualificazione assicurativa, il nesso professionale, la valutazione dei postumi e gli altri presupposti: ciascuno richiede fatti e prove pertinenti.

Caso: una lavoratrice contesta un diniego di prestazione fondato sull'assenza di contribuzione, mentre un'altra contesta il requisito sanitario per l'assegno ordinario di invalidità. Entrambe devono individuare la tutela competente, ma solo la seconda presenta il problema dell'ATP sanitario nel campo dell'articolo 445-bis. Il medesimo ente convenuto non rende identico il percorso processuale.''')
add('appendice-f','### Scienze delle finanze','''### Sicurezza: attribuire gli obblighi al soggetto corretto

Il datore di lavoro ha il potere decisionale e di spesa dell'organizzazione secondo la definizione del d.lgs. 81/2008. L'articolo 17 rende non delegabili la valutazione di tutti i rischi con il relativo documento e la designazione del RSPP. Gli altri obblighi seguono gli articoli 18 e seguenti e le condizioni dell'eventuale delega: incaricare un consulente non trasferisce automaticamente ogni responsabilità.

| Soggetto | Funzione e obbligo essenziale |
| --- | --- |
| Datore di lavoro e dirigente | Organizzano e attuano prevenzione, misure, informazione e formazione nelle rispettive attribuzioni; il datore conserva gli obblighi non delegabili. |
| Preposto | Sovrintende e vigila sull'attività, interviene sulle condotte non conformi e segnala le carenze; nei presupposti previsti interrompe l'attività pericolosa. |
| Lavoratore | Si prende cura della sicurezza propria e altrui, osserva le istruzioni, usa correttamente attrezzature e dispositivi, segnala pericoli. |
| RSPP | Coordina il servizio di prevenzione e protezione, individua fattori di rischio e propone misure; non sostituisce per questo il datore nelle decisioni. |
| Medico competente | Collabora alla valutazione dei rischi ed effettua sorveglianza sanitaria nei casi previsti, formulando i giudizi di idoneità. |
| RLS | È consultato e rappresenta i lavoratori sui temi di sicurezza; accede alle informazioni e formula proposte nelle attribuzioni dell'articolo 50. |

Il DVR non è una polizza né un certificato di assenza di rischio. Descrive valutazione e misure; le misure devono essere attuate e aggiornate quando necessario. I DPI proteggono dal rischio residuo e non sostituiscono senza ragione la prevenzione collettiva. INAIL contribuisce a prevenzione, ricerca, assistenza e reinserimento; non diventa il datore di lavoro dell'impresa assicurata né l'unico organo di vigilanza sulla sicurezza.

Caso: il consulente ha redatto una bozza di DVR, ma il datore non l'ha valutata né adottata e il reparto continua una lavorazione pericolosa senza le misure necessarie. La presenza del documento non soddisfa da sola gli obblighi. Si distinguono responsabilità del datore, vigilanza del preposto e compiti consultivi del RSPP, senza attribuire a quest'ultimo ogni omissione dell'organizzazione.''')
add('appendice-f','### Reati contro la pubblica amministrazione','''### Entrate e intervento pubblico: distinguere presupposti ed effetti

L'**imposta** è un prelievo coattivo collegato a un indice di capacità contributiva, senza corrispettivo individuale di un servizio. La **tassa** si collega a un'attività pubblica riferibile al soggetto; il **contributo** può collegarsi a un beneficio o a un obbligo previdenziale secondo la specifica disciplina. Il nome usato nel linguaggio comune non basta a qualificare un'entrata: il premio INAIL finanzia un'assicurazione obbligatoria, mentre una sanzione per violazione ha finalità punitiva.

Un prelievo proporzionale mantiene costante l'aliquota al variare della base; in quello progressivo aumenta l'incidenza secondo il meccanismo previsto. Se su 20.000 euro l'imposta è 2.000 e su 40.000 è 4.000, l'aliquota media è in entrambi i casi 10%: il semplice aumento dell'importo non prova progressività. L'articolo 53 Cost. riferisce la progressività al sistema tributario.

Le funzioni economiche dell'intervento pubblico comprendono allocazione, redistribuzione e stabilizzazione. Un investimento per ridurre gli infortuni può correggere carenze informative e costi sociali non pienamente considerati dalle imprese; una prestazione redistribuisce risorse verso soggetti protetti; il sostegno al reddito può anche attenuare cadute della domanda. Per valutare l'efficienza si rapportano risorse e risultati; per l'equità si osserva chi beneficia e chi resta escluso. Nessuno dei due giudizi si ricava dal solo numero di pratiche lavorate.''')
print('Appendici A, B, F integrate; restano quiz, simulazioni e rinvii puntuali.')
