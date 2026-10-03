from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters')
def file(prefix): return next(B.glob(prefix+'*.md'))
def insert(prefix, heading, text):
 p=file(prefix);s=p.read_text(encoding='utf8');assert heading in s,(p,heading);s=s.replace(heading,text.strip()+'\n\n'+heading,1);p.write_text(s,encoding='utf8')

insert('02-','### Obiettivo', '''### Gli organi di INPS e INAIL: chi indirizza, chi amministra, chi controlla

Il d.lgs. 479/1994, coordinato con la legge 88/1989 e le successive modifiche, configura per INPS e INAIL un assetto che distingue indirizzo strategico, amministrazione e gestione. Non basta dire «organo politico»: occorre indicare l'organo e l'atto di sua competenza. I nominativi cambiano; la distinzione delle funzioni è il punto da studiare.

| Organo | Compito essenziale | Da non confondere con |
| --- | --- | --- |
| Presidente | Rappresentanza legale; convoca e presiede il Consiglio di amministrazione. | Il presidente del CIV, figura diversa. |
| Consiglio di amministrazione (CdA) | Amministra l'ente, predispone bilanci e piani, adotta gli atti regolamentari attribuiti dalla legge. | L'approvazione definitiva del bilancio spettante al CIV. |
| Consiglio di indirizzo e vigilanza (CIV) | Definisce indirizzi e obiettivi strategici, verifica i risultati, approva bilanci e programmi nelle competenze previste. | La decisione quotidiana sul singolo fascicolo di prestazione. |
| Direttore generale | Coordina la struttura e risponde della gestione e del conseguimento degli obiettivi. | La rappresentanza degli interessi sociali nel CIV. |
| Collegio dei sindaci | Controlla regolarità amministrativa e contabile; formula relazioni e osservazioni sui documenti di bilancio. | Il controllo di merito del CIV sugli obiettivi. |

La denominazione propria è **Collegio dei sindaci**: la funzione di revisione non autorizza a inventare un «Collegio dei revisori» come sesto organo. Il Ministero del lavoro esercita la vigilanza istituzionale; il MEF interviene per gli aspetti finanziari e gli atti per i quali è previsto il concerto. I poteri dei ministeri vigilanti si esercitano secondo la legge e non coincidono con la gestione degli uffici. Il controllo della Corte dei conti sulla gestione finanziaria è ancora distinto dal controllo interno dei sindaci.

Esempio: il CdA predispone il preventivo; il CIV lo esamina e approva nell'ambito delle proprie attribuzioni, con la relazione dell'organo di controllo e gli adempimenti di vigilanza. Il direttore generale organizza la gestione coerente con risorse e obiettivi. Non si attribuisce al CIV il pagamento materiale di una pensione, né al direttore il potere di approvare da solo il bilancio. Per altri EPNE si consulta lo statuto: l'assetto INPS/INAIL non è una formula universale.''')

insert('03-','### I cinque nuclei da padroneggiare', '''### Previdenza e assistenza: il fondamento costituzionale

L'articolo 38 della Costituzione collega la protezione sociale a due situazioni distinte. Il cittadino inabile al lavoro e sprovvisto dei mezzi necessari ha diritto al mantenimento e all'assistenza sociale; i lavoratori hanno diritto a mezzi adeguati nelle ipotesi di infortunio, malattia, invalidità, vecchiaia e disoccupazione involontaria. La previdenza si organizza prevalentemente attorno al lavoro e all'assicurazione obbligatoria; l'assistenza tutela bisogni previsti dalla legge senza esigere necessariamente una precedente contribuzione. La distinzione riguarda presupposti e finanziamento, non il valore del diritto.

L'INPS gestisce sia prestazioni previdenziali sia prestazioni assistenziali. La pensione di vecchiaia dipende da requisiti assicurativi e contributivi; l'assegno sociale è assistenziale e richiede condizioni personali, di soggiorno e reddito, non contributi versati. L'INAIL tutela infortuni e malattie professionali mediante assicurazione sociale: anch'esso appartiene al sistema previdenziale. Non si definisce la previdenza come esclusiva dell'INPS.

### Rapporto contributivo e automaticità

Nel lavoro subordinato il datore è obbligato a versare i contributi dovuti, compresa la quota trattenuta al lavoratore nei casi previsti. Il rapporto contributivo con l'ente si distingue dal rapporto di lavoro e dal rapporto previdenziale relativo alla prestazione. L'importo dovuto dipende da imponibile, aliquota, gestione e periodo. L'estratto conto contributivo è lo strumento per controllare gli accrediti: un periodo assente richiede verifica e documentazione, non l'inserimento arbitrario da parte dell'operatore.

La contribuzione **obbligatoria** deriva dall'attività assicurata; quella **figurativa** è riconosciuta per periodi tutelati dalla legge; la **volontaria** consente la prosecuzione autorizzata nei presupposti previsti; il **riscatto** valorizza periodi ammessi dalla legge, normalmente con un onere. Queste categorie non sono intercambiabili: alcune prestazioni richiedono contribuzione effettiva e non computano ogni accredito allo stesso modo.

L'articolo 2116 c.c. esprime l'automaticità: l'omissione contributiva del datore non deve, nei limiti delle leggi speciali, privare il dipendente delle prestazioni. Non significa che basti dichiarare di avere lavorato. Si accertano rapporto, periodi e requisiti, tenendo conto di prescrizione e disciplina della gestione. Per i contributi prescritti possono assumere rilievo la responsabilità risarcitoria del datore e gli strumenti di costituzione della rendita previsti dalla legge; non si promette un accredito automatico in qualsiasi situazione. Per il lavoro autonomo non si estende indiscriminatamente la tutela prevista per l'omissione altrui.

### Pensioni: accesso e calcolo sono due domande diverse

La pensione di vecchiaia richiede età e anzianità contributiva; la pensione anticipata ordinaria valorizza principalmente l'anzianità contributiva prevista dalla disciplina, con regole di decorrenza proprie. La pensione ai superstiti tutela determinati familiari: reversibilità se il dante causa era pensionato, pensione indiretta se era assicurato e ricorrono i requisiti. Il diritto non discende dalla sola parentela.

**Quadro 2026, verificato il 3 ottobre 2026 sulle schede INPS.** Per la vecchiaia ordinaria il riferimento è 67 anni e almeno 20 anni di contribuzione, ferme deroghe e discipline speciali. Per chi ha il primo accredito dal 1 gennaio 1996 opera anche una soglia d'importo pari all'assegno sociale; la via alternativa richiede nel 2026 71 anni e cinque anni di contribuzione effettiva, indipendentemente dall'importo. Non trasformare la regola ordinaria in un requisito universale né proiettarla sugli anni successivi. Le gestioni e le condizioni particolari vanno identificate prima di applicare il dato.

Il **calcolo retributivo** collega la quota pensionistica alle retribuzioni o redditi di riferimento e all'anzianità; quello **contributivo** trasforma il montante dei contributi mediante coefficienti; quello **misto** combina quote secondo l'anzianità e le regole transitorie. «Contributivo» descrive quindi anche un sistema di calcolo: non è sinonimo di pensione anticipata e non significa restituzione nominale di quanto versato.

Caso: Anna compie 67 anni nel 2026 e ha 22 anni di contributi. L'ufficio non deve chiedere soltanto l'età: verifica gestione, decorrenza, anzianità e, se la prima contribuzione è dal 1996, anche il requisito d'importo. Bruno, con la stessa età ma 18 anni, non soddisfa la regola ordinaria dei 20; prima di negare in via definitiva si controllano eventuali deroghe, periodi aggregabili e strumenti applicabili. Il caso dimostra perché due persone coetanee non hanno necessariamente lo stesso diritto.

### Sostegni al reddito, invalidità e assistenza

La **NASpI** tutela la disoccupazione involontaria di lavoratori subordinati rientranti nel campo della misura. Nel quadro verificato al 3 ottobre 2026 richiede almeno tredici settimane di contribuzione nei quattro anni precedenti; dura la metà delle settimane utili del quadriennio, escluse quelle già utilizzate per precedenti prestazioni. Le dimissioni non sono tutte equivalenti: esistono eccezioni protette, come la giusta causa. Dal 2025 opera inoltre, nei casi previsti, un requisito aggiuntivo di tredici settimane dopo una precedente cessazione volontaria da tempo indeterminato avvenuta nei dodici mesi anteriori alla nuova cessazione involontaria. Non confondere questa condizione con il criterio di calcolo della durata.

La **cassa integrazione** sostiene il reddito durante sospensione o riduzione dell'attività, con rapporto di lavoro che permane; non equivale alla NASpI dopo la perdita dell'impiego. Le prestazioni di maternità e malattia hanno eventi, soggetti e discipline proprie. L'ufficio identifica prima l'evento protetto, poi la gestione e la misura: una difficoltà economica generica non basta a scegliere la prestazione.

L'**assegno ordinario di invalidità**, legge 222/1984, richiede una capacità lavorativa, in occupazioni confacenti alle attitudini, ridotta a meno di un terzo e almeno cinque anni assicurativi e contributivi, dei quali tre nel quinquennio precedente la domanda. Non impone in assoluto di cessare ogni lavoro. La **pensione di inabilità previdenziale** richiede invece l'impossibilità assoluta e permanente di svolgere qualsiasi attività lavorativa, oltre ai requisiti contributivi; è distinta dall'inidoneità alla sola mansione. L'**invalidità civile** appartiene all'assistenza: le singole provvidenze richiedono condizioni sanitarie, personali e, ove previsti, limiti reddituali, senza la medesima anzianità contributiva. Una percentuale di invalidità civile non si trasferisce automaticamente nella valutazione della legge 222 né in quella INAIL.

### ISEE e DSU: documenti, indicatore e beneficio

La Dichiarazione sostitutiva unica (**DSU**) raccoglie dati sul nucleo, redditi e patrimoni, in parte dichiarati e in parte acquisiti dagli archivi. L'**ISEE** è l'indicatore della situazione economica equivalente: tiene conto del reddito e del patrimonio rilevante, con pesi e franchigie, rapportati alla scala di equivalenza. Non è una pensione, un contributo versato o una certificazione di invalidità.

Schema didattico: se l'indicatore reddituale è 18.000 euro, quello patrimoniale già determinato secondo le regole è 10.000 e il parametro della scala è 2, l'ISEE esemplificativo è (18.000 + 20% × 10.000) / 2 = 10.000 euro. Gli importi sono ipotesi d'esercizio già al netto delle regole applicabili, non soglie per una prestazione reale. Nel 2026 alcune misure familiari e di inclusione usano un indicatore specifico: occorre scegliere l'ISEE richiesto dal beneficio. L'ISEE corrente serve nei presupposti previsti a riflettere variazioni rilevanti; non si ottiene semplicemente cambiando una cifra della DSU ordinaria.

Una DSU corretta non attribuisce da sola il beneficio: l'ente erogatore verifica anche domanda, categoria dei destinatari e altri requisiti. Nel caso di omissioni o difformità si applicano le modalità di regolarizzazione e documentazione previste. L'operatore spiega quale elemento manca senza imporre al cittadino di produrre documenti che l'amministrazione deve acquisire d'ufficio.''')

insert('04-','### Obiettivo', '''### Il rischio assicurato: infortunio e malattia professionale

Il DPR 1124/1965 e il d.lgs. 38/2000 fondano la tutela INAIL. Si verificano congiuntamente soggetto assicurato, attività protetta, evento e conseguenze. L'assicurazione non riguarda soltanto il lavoro manuale industriale: il campo comprende categorie e attività individuate dalla legge, con regole particolari per autonomi, parasubordinati e altri assicurati. Non basta però essere presenti in un luogo di lavoro per ottenere qualsiasi prestazione.

Nell'**infortunio** la causa violenta è concentrata nel tempo; non significa necessariamente aggressione o uso di una forza eccezionale. L'**occasione di lavoro** è il collegamento funzionale fra attività e rischio: va oltre la coincidenza di luogo e orario. La caduta durante un compito lavorativo e una lesione dovuta a una condotta del tutto estranea al lavoro richiedono valutazioni diverse. Il rischio elettivo, creato da una scelta arbitraria estranea alle esigenze lavorative, non va confuso con ogni semplice imprudenza del dipendente.

L'**infortunio in itinere** riguarda, nei presupposti di legge, il normale percorso fra abitazione e lavoro, fra luoghi di lavoro o verso il luogo abituale di consumazione dei pasti quando manchi una mensa aziendale. Deviazioni e interruzioni si valutano in rapporto alle ragioni necessitate; l'uso del mezzo privato deve essere necessitato nei termini previsti. Una deviazione personale per acquisti non è automaticamente equiparata a quella imposta dalla chiusura della strada. Il mezzo, l'orario e il tragitto sono fatti da accertare, non prove sufficienti da soli.

La **malattia professionale** deriva dall'azione lavorativa nociva generalmente lenta e progressiva. Nel sistema misto sono tutelate malattie tabellate e non tabellate. Quando ricorrono malattia, lavorazione e periodo indicati dalla tabella opera la presunzione dell'origine professionale, salva prova contraria. Fuori dalle condizioni tabellari il lavoratore può dimostrare il nesso causale con il lavoro. «Non tabellata» non significa quindi «mai indennizzabile», mentre una diagnosi da sola non dimostra il nesso con qualunque attività.

### Premio e automaticità delle prestazioni

Il **premio assicurativo** finanzia la copertura; nella forma ordinaria è calcolato applicando alle retribuzioni assicurate il tasso pertinente alla lavorazione, con oscillazioni e regole tariffarie. Esistono premi speciali, tra cui quelli unitari per determinate categorie. Il premio non è la somma riconosciuta all'infortunato. Nell'autoliquidazione si distinguono la regolazione dell'anno trascorso e la rata anticipata del nuovo anno: non sono due assicurazioni diverse sul medesimo evento.

Per il dipendente opera l'**automaticità**: l'omesso pagamento del premio da parte del datore non elimina la tutela dovuta se sussistono i presupposti assicurativi. Restano denuncia, istruttoria e accertamento medico-legale. Per i lavoratori autonomi, invece, il diritto alle prestazioni economiche richiede la regolarizzazione contributiva; sono comunque garantite le prestazioni sanitarie e riabilitative secondo il quadro INAIL. Non si estende senza verifica l'eccezione dell'autonomo al dipendente né la regola del dipendente all'artigiano titolare.

### Prestazioni economiche, sanitarie e reinserimento

L'inabilità temporanea assoluta riguarda il periodo nel quale l'assicurato non può attendere al lavoro; è distinta dalla menomazione permanente accertata dopo la stabilizzazione. Il sistema comprende indennità temporanea, indennizzo del danno permanente, rendite e prestazioni ai superstiti nei casi previsti. Le cure, la riabilitazione, le protesi e gli interventi di reinserimento rispondono a finalità ulteriori rispetto al pagamento di denaro. La prestazione assicurativa non esaurisce necessariamente il tema della responsabilità civile o delle azioni di regresso e surrogazione.

Il **danno biologico** è la menomazione dell'integrità psicofisica suscettibile di valutazione medico-legale, distinta dalla perdita di reddito. Nel regime del d.lgs. 38/2000, verificato al 3 ottobre 2026, la menomazione permanente sotto il 6% resta in franchigia per questo indennizzo; dal 6% a meno del 16% dà luogo a capitale; dal 16% dà luogo a rendita, nella quale si distingue la componente biologica da quella relativa alle conseguenze patrimoniali. La franchigia non equivale a inesistenza dell'infortunio e non elimina automaticamente altre prestazioni dovute.

Caso: due dipendenti hanno postumi stabilizzati rispettivamente del 10% e del 18%. Il primo ricade nell'indennizzo in capitale, il secondo nella rendita, purché ricorrano gli altri presupposti. Il 10% non è l'aliquota del premio né il numero di giorni pagabili. Per un terzo dipendente con postumi del 4% occorre distinguere il mancato indennizzo del danno permanente in quel regime dalle cure e dall'eventuale inabilità temporanea. Il confronto serve a scegliere la categoria della tutela, senza improvvisarne l'importo.

### Caso di nesso e tutela

Un magazziniere dipendente si lesiona durante la movimentazione di un collo; il datore risulta in ritardo nel pagamento del premio. La dinamica descrive una causa concentrata nel tempo in occasione di lavoro: si raccolgono denuncia, certificazione e fatti, si verifica il campo assicurativo e si accertano le conseguenze. Il ritardo contributivo del datore non autorizza il rigetto automatico della prestazione al dipendente. Se lo stesso fascicolo riguardasse una patologia da esposizione ripetuta, si ricostruirebbero durata, mansioni ed esposizioni, verificando condizioni tabellari o prova del nesso. Cambia la qualificazione causale, non l'obbligo di un'istruttoria rigorosa.''')

insert('06-','### Obiettivo', '''### Documenti e competenze contabili degli EPNE

La disciplina di riferimento è il DPR 97/2003, regolamento di amministrazione e contabilità degli enti pubblici cui si riferisce la legge 70/1975, coordinato con l'armonizzazione del d.lgs. 91/2011 e con i regolamenti degli istituti. Per INPS il preventivo 2026 richiama espressamente il regolamento adottato con delibera CdA 172/2005; per INAIL si usano le norme dell'ordinamento amministrativo-contabile dell'Istituto. Non si applicano automaticamente il TUEL e il DUP dei comuni, né si trasferisce senza verifica la competenza finanziaria potenziata degli enti territoriali.

Il **bilancio di previsione** esprime le entrate e le spese attese e autorizza la gestione nei limiti previsti. Il preventivo finanziario distingue competenza e cassa; il preventivo economico espone costi e ricavi secondo la loro imputazione economica. Relazione programmatica, quadro generale riassuntivo e risultato di amministrazione presunto aiutano a collegare obiettivi, equilibri e risorse. Le variazioni aggiornano le previsioni con gli atti e le competenze prescritti: non sono correzioni informali di un foglio contabile.

Il **rendiconto generale** consente di confrontare gestione e previsioni. Il conto del bilancio rappresenta accertamenti, impegni, riscossioni, pagamenti e residui; il conto economico misura il risultato economico; lo stato patrimoniale espone attività, passività e patrimonio netto. Nota integrativa, situazione amministrativa e relazioni spiegano dati e risultati. Un avanzo finanziario non coincide necessariamente con un utile economico e la liquidità in cassa non è tutta liberamente spendibile.

Per INPS e INAIL il CdA predispone i documenti nelle attribuzioni stabilite; il CIV approva bilanci e rendiconti, accompagnati dalle relazioni e sottoposti ai controlli previsti. Il direttore generale coordina la gestione. Il Collegio dei sindaci verifica regolarità e attendibilità contabile, mentre ministeri vigilanti e Corte dei conti esercitano controlli diversi. Lo schema non autorizza ad attribuire le stesse funzioni a ogni altro EPNE: regolamento e statuto completano la fonte generale.

**Esempio finanziario semplificato.** Un ente parte senza residui, con cassa iniziale di 100. Accerta entrate per 1.000 e ne riscuote 900; impegna spese per 950 e paga 800. A fine anno: cassa 200, residui attivi 100, residui passivi 150. Il risultato di amministrazione è 200 + 100 − 150 = 150, prima delle specificazioni e dei vincoli del caso. Non è 200, perché la sola cassa ignora crediti e debiti della gestione finanziaria. Non si trasferisce qui senza adattamenti la distinta fase statale del versamento.

**Esempio patrimoniale.** L'acquisto di un bene strumentale per 20 genera una spesa finanziaria; il costo economico può distribuirsi negli esercizi mediante ammortamento secondo vita utile e regole contabili. Pagamento, costo e valore residuo del bene rispondono quindi a domande diverse. Nell'orale si indica prima il documento richiesto, poi il dato: «quanto ho pagato?» rimanda alla cassa, «quale costo compete all'anno?» al conto economico, «quali beni e debiti esistono?» allo stato patrimoniale.''')

p=file('08-');s=p.read_text(encoding='utf8')
s=s.replace('La fonte ARAN consolidata nel wiki ricorda un punto essenziale:','Il sistema della contrattazione collettiva richiede una distinzione essenziale:')
a=s.index('Alla data di aggiornamento del modulo, il contratto definitivo');b=s.index('\n\n',a)
s=s[:a]+'''Il CCNL Funzioni Centrali 2025–2027 è stato sottoscritto definitivamente il **6 agosto 2026**, dopo l'ipotesi del 9 giugno. Il contratto 2022–2024 del 27 gennaio 2025 e quello 2019–2021 restano rilevanti per le disposizioni non sostituite. Firma, decorrenza economica e decorrenza del singolo istituto non coincidono necessariamente: per esempio la nuova disciplina delle ferie dell'articolo 21 del contratto 2025–2027 opera dal 1 gennaio 2027. Non si applica retroattivamente al 2026 per il solo fatto che il contratto è definitivo.

Le quattro aree sono Operatori, Assistenti, Funzionari ed Elevate professionalità. Descrivono complessità, autonomia e responsabilità crescenti secondo le declaratorie; il bando specifica il profilo, i requisiti di accesso e le competenze richieste. Il personale degli enti pubblici di ricerca appartiene invece al comparto Istruzione e Ricerca anche quando svolge attività amministrativa; INAIL comprende inoltre personale ex ISPESL con il proprio inquadramento contrattuale. Prima di applicare un istituto si identifica il personale cui la norma si riferisce.''' +s[b:]
p.write_text(s,encoding='utf8')
print('Teoria integrata: governance, INPS, INAIL, contabilità, CCNL.')
