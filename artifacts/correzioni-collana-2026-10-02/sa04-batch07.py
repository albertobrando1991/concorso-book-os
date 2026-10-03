from pathlib import Path
import re,json
B=Path('wiki/books/moduli');m='m-sa04-tecnici-sanitari-prevenzione'
def cp(n):return next((B/m/'chapters').glob(f'{n:02}-*.md'))
def put(p,s):
 s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M);s=re.sub(r'^review_required:.*$','review_required: true',s,flags=re.M);s=re.sub(r'^draft_stage:.*$','draft_stage: revision-in-progress',s,flags=re.M);p.write_text(s,encoding='utf8')
p=cp(2);s=p.read_text(encoding='utf8')
t='''### Principi analitici da riconoscere

In **biochimica clinica** si misura un analita, per esempio glucosio o creatinina, collegando una proprietà osservabile alla sua quantità. Nella spettrofotometria il segnale è l'assorbimento di luce a una determinata lunghezza d'onda; entro le condizioni e l'intervallo del metodo, la relazione con la concentrazione consente la misura. Nei metodi elettrochimici il segnale deriva da proprietà elettriche, come la differenza di potenziale in un elettrodo selettivo. Il metodo non misura «la malattia»: produce un risultato che va interpretato nel contesto clinico. Emolisi, lipemia o ittero possono interferire in modo diverso secondo analita e tecnologia; non tutti i risultati dello stesso campione sono automaticamente invalidi.

In **microbiologia**, coltura, ricerca antigenica e amplificazione di acidi nucleici rispondono a domande diverse. La coltura dimostra crescita nelle condizioni adottate e può fornire un isolato per identificazione e studio della sensibilità agli antimicrobici. Un test molecolare cerca una sequenza bersaglio: rilevarla non prova da solo vitalità del microrganismo o malattia attiva. Un risultato negativo può dipendere da assenza del bersaglio, quantità sotto il limite di rilevazione, campione non rappresentativo o inibizione. Il controllo interno aiuta a distinguere alcune di queste condizioni; non rende irrilevante la qualità del prelievo. Nell'antibiogramma si interpreta la sensibilità rispetto a criteri aggiornati e al microrganismo, senza scegliere la terapia al posto del clinico.

In **ematologia**, l'emocromo quantifica popolazioni cellulari e parametri correlati. Conta mediante impedenza e analisi ottica sono principi differenti; la citometria a flusso studia cellule in sospensione attraverso segnali di diffusione della luce e, quando previsti, marcature fluorescenti. Uno striscio consente la valutazione morfologica e integra l'informazione numerica. Un flag strumentale indica un approfondimento previsto dal percorso, non equivale già a una diagnosi. Nell'emostasi, esami come PT e aPTT misurano tempi di formazione del coagulo in condizioni definite: la loro alterazione non identifica da sola una specifica causa e risente anche di problemi preanalitici.

In **immunologia**, molti saggi sfruttano il riconoscimento tra antigene e anticorpo, reso misurabile mediante un segnale enzimatico, luminoso o fluorescente. Si può cercare un antigene oppure la risposta anticorpale; una positività anticorpale non coincide sempre con un'infezione attiva. Cross-reattività e interferenze possono modificare il segnale. La soglia di positività, il periodo dall'esposizione e lo scopo del test incidono sull'interpretazione. La sensibilità analitica, cioè la capacità di rilevare piccole quantità del bersaglio, non coincide con la sensibilità diagnostica, cioè la quota di malati correttamente identificati.

In **istologia e citologia**, fissazione e preparazione conservano quanto possibile strutture e componenti da osservare. Nell'istologia si studia anche l'architettura del tessuto; nella citologia prevalgono le caratteristiche delle cellule. Un campione mal identificato, non rappresentativo o alterato nella preparazione può compromettere la successiva valutazione. Il TSLB assicura la qualità tecnica nel proprio ruolo; la diagnosi resta attribuita al professionista competente.

**Verifica.** Un test molecolare è positivo e la coltura è negativa: è necessariamente un errore? **No.** Le due tecniche rilevano proprietà diverse; occorre considerare vitalità, terapie precedenti, qualità del campione, quantità del bersaglio e condizioni di coltura. La discordanza va analizzata, non eliminata scegliendo il risultato preferito.

'''
s=s.replace('### La griglia quesito-campione-metodo-controlli-limiti',t+'### La griglia quesito-campione-metodo-controlli-limiti',1)
t='''### Precisione, esattezza e calibrazione

La **precisione** descrive quanto concordano misure ripetute nelle condizioni dichiarate. Una serie molto raccolta può essere precisa ma sistematicamente spostata rispetto al riferimento. L'**esattezza** riguarda la vicinanza della media di molte misure al valore di riferimento; lo scostamento sistematico è il bias. L'accuratezza esprime complessivamente la vicinanza del risultato al riferimento e non si dimostra con la sola ripetibilità. La deviazione standard descrive la dispersione; il coefficiente di variazione la rapporta alla media: CV = deviazione standard / media × 100, quando questo rapporto è appropriato.

La **calibrazione** stabilisce la relazione tra segnale e valori assegnati a materiali di riferimento o calibratori. Il **controllo qualità** verifica che il sistema continui a fornire prestazioni accettabili: usa materiali e criteri predisposti a questo scopo e non coincide con il calibratore. Ricalibrare per far rientrare un controllo, senza indagare la causa e senza seguire il metodo, può mascherare un problema.

Esempio: un materiale ha riferimento 100 unità. Misure ripetute 109, 110 e 111 sono vicine tra loro, ma la loro media 110 è spostata di +10. Non basta quindi dire «le repliche concordano». Vanno considerate sia dispersione sia scostamento dal riferimento, insieme all'incertezza e ai criteri del metodo.

### Leggere una serie di controllo

Un grafico di Levey–Jennings riporta in ascissa la successione delle sedute e in ordinata il risultato del controllo; linee orizzontali indicano media e multipli della deviazione standard. Per confrontare la posizione dei risultati possiamo usare z = (valore − media) / deviazione standard. La tabella seguente contiene dati interamente didattici, riferiti a un solo materiale con media 100 e deviazione standard 2.

| Seduta | Risultato | Posizione z |
| --- | --- | --- |
| 1 | 100 | 0 |
| 2 | 101 | +0,5 |
| 3 | 102 | +1 |
| 4 | 103 | +1,5 |
| 5 | 104 | +2 |
| 6 | 105 | +2,5 |
| 7 | 106 | +3 |
| 8 | 107 | +3,5 |

**Domanda.** La sesta seduta può essere considerata affidabile solo perché il risultato non supera ancora +3 deviazioni standard?

**Soluzione.** No: esiste già un andamento progressivamente crescente. Il trend suggerisce una variazione sistematica da indagare, per esempio nei reagenti, nella calibrazione o nel sistema, senza attribuire una causa certa dalla sola forma. Un improvviso assestamento su una nuova media sarebbe invece uno shift. Il singolo limite non sostituisce le regole del piano QC: queste devono essere definite per metodo e prestazioni richieste. Prima del rilascio dei risultati interessati si applica il percorso documentato di valutazione e gestione della non conformità; ripetere finché compare un valore favorevole non risolve il problema.

'''
s=s.replace('### Documenti e registrazioni',t+'### Documenti e registrazioni',1)
t='''## Biosicurezza: obblighi nazionali e scelta delle barriere

Il Titolo X del D.Lgs. 81/2008 classifica gli agenti biologici in quattro gruppi. Il gruppo non coincide automaticamente con la valutazione di ogni attività: quantità, procedure, aerosol e vie di esposizione incidono sul rischio. La valutazione, però, non può disapplicare le misure minime previste dalla legge.

| Gruppo | Significato essenziale |
| --- | --- |
| 1 | Poco probabile che causi malattie nell'uomo. |
| 2 | Può causare malattie e rischio per i lavoratori; diffusione nella comunità poco probabile; normalmente disponibili misure profilattiche o terapeutiche efficaci. |
| 3 | Può causare malattie gravi e serio rischio per i lavoratori; può propagarsi nella comunità; normalmente disponibili misure profilattiche o terapeutiche efficaci. |
| 4 | Può causare malattie gravi e serio rischio; può presentare elevato rischio di diffusione; di norma mancano misure profilattiche o terapeutiche efficaci. |

L'art. 275 prevede, per l'uso deliberato in laboratorio, livelli di contenimento almeno 2, 3 e 4 per agenti dei rispettivi gruppi. Per materiali potenzialmente contaminati da patogeni per l'uomo, il minimo è il livello 2; per agenti non ancora classificati il cui uso può comportare grave rischio, almeno il livello 3. Classificazione e misure vanno lette con gli allegati XLVI e XLVII e con la valutazione specifica.

### Cappe: protezioni diverse

Una cappa di sicurezza biologica di classe I protegge operatore e ambiente, ma non garantisce la protezione del prodotto dall'aria in ingresso. La classe II protegge anche il prodotto mediante flussi e filtrazione progettati a questo scopo. La classe III costituisce un sistema chiuso con manipolazione attraverso guanti integrati. Tipo, installazione, manutenzione e impiego devono essere appropriati all'attività: il numero della cappa non coincide con il gruppo biologico dell'agente.

Un banco a flusso laminare destinato alla protezione del prodotto può convogliare aria verso l'operatore e non sostituisce una cappa biologica. La cappa chimica è progettata per captare contaminanti chimici secondo le sue caratteristiche; non si presume idonea al contenimento biologico. Analogamente, un filtro HEPA per particelle non trattiene automaticamente gas e vapori chimici.

### Detersione, disinfezione, sterilizzazione e rifiuti

La detersione rimuove sporco e materiale organico. La disinfezione inattiva microrganismi con efficacia dipendente da agente, prodotto, superficie e condizioni; non equivale necessariamente all'eliminazione delle spore. La sterilizzazione è un processo validato finalizzato a eliminare microrganismi vitali, comprese le spore. Per scegliere il processo occorrono compatibilità del materiale, efficacia attesa e verifica: non basta aumentare arbitrariamente concentrazione o tempo di contatto.

Il D.P.R. 254/2003 distingue rifiuti sanitari non pericolosi, pericolosi non a rischio infettivo, pericolosi a rischio infettivo e categorie con particolari sistemi di gestione. Un reagente chimico pericoloso non è automaticamente un rifiuto infettivo; un tagliente contaminato richiede attenzione sia al rischio biologico sia alla puntura; medicinali citotossici o citostatici seguono il proprio percorso. L'origine sanitaria, da sola, non assegna ogni rifiuto alla stessa categoria. Identificazione, separazione all'origine, contenitori idonei e tracciabilità precedono il conferimento al circuito previsto.

**Caso.** Un operatore propone di manipolare campioni potenzialmente infettivi su un banco che protegge soltanto il prodotto. La proposta è adeguata? **No.** Proteggere il campione dalla contaminazione non garantisce la protezione dell'operatore. Occorre verificare valutazione del rischio, contenimento minimo e idoneità della barriera prima di iniziare; non si corregge il problema aggiungendo soltanto guanti.

'''
s=s.replace('## Domanda da commissario',t+'## Domanda da commissario',1);put(p,s)
p=cp(3);s=p.read_text(encoding='utf8')
t='''### Indicatori dosimetrici e unità

Il **CTDIvol**, espresso in mGy, è un indice standardizzato della dose in TC basato su misure in fantocci. Descrive l'uscita dell'apparecchiatura nelle condizioni di riferimento; non è la dose assorbita da ogni organo della persona esaminata. Il **DLP**, in mGy·cm, tiene conto anche della lunghezza acquisita: per una serie si ricava dal prodotto CTDIvol × lunghezza. Nell'esame con più serie occorre considerare i contributi pertinenti, evitando di confrontare il valore di una sola serie con quello dell'intero esame.

Il **prodotto kerma-area**, spesso indicato come prodotto dose-area o DAP, combina il kerma in aria con l'area del fascio; l'unità comunemente usata è Gy·cm². È utile in radiografia e fluoroscopia, ma non coincide con la dose cutanea massima né con la dose efficace. Due esposizioni con uguale DAP possono distribuirsi diversamente sulla cute.

**Esempio numerico.** CTDIvol 8 mGy e lunghezza 30 cm producono DLP 240 mGy·cm. Se una seconda serie nelle stesse condizioni copre 10 cm, aggiunge 80 mGy·cm: totale 320. Questi dati, da soli, non permettono di assegnare un rischio individuale o di decidere una ripetizione. Dimensioni del paziente, distretto, geometria e protocollo incidono sulle valutazioni dosimetriche; la conversione in dose efficace non è un semplice cambio di unità.

### Effetti e protezione: collegare la fisica al rischio

Le **reazioni tissutali** possono comparire sopra una soglia, dipendente da tessuto e condizioni di esposizione; oltre la soglia la gravità tende a crescere con la dose. Gli **effetti stocastici**, come l'induzione di tumori, sono trattati in radioprotezione con un modello prudenziale in cui cresce la probabilità con la dose, senza assumere una soglia sicura; non si confonde probabilità con gravità del singolo effetto.

Ridurre il **tempo** di esposizione, aumentare la **distanza** e usare **schermature** appropriate sono principi di protezione per le persone esposte. Nel modello di una sorgente puntiforme, senza attenuazione o diffusione, raddoppiare la distanza riduce l'intensità a un quarto. Una sala reale, con paziente come sorgente di radiazione diffusa, geometrie e barriere, richiede la valutazione dell'esperto: non si trasferisce quel rapporto a ogni situazione. La schermatura va scelta per tipo ed energia della radiazione e percorso di esposizione.

### Limiti per lavoratori e popolazione

Il quadro dell'art. 146 del D.Lgs. 101/2020 distingue dose efficace e dose equivalente ai tessuti. La tabella riguarda lavoratori esposti e individui della popolazione nelle condizioni ordinarie previste dalla norma; apprendisti, studenti ed esposizioni particolari richiedono la disciplina specifica.

| Grandezza, per anno solare | Lavoratori esposti | Popolazione |
| --- | --- | --- |
| Dose efficace | 20 mSv | 1 mSv |
| Dose equivalente al cristallino | 20 mSv | 15 mSv |
| Dose equivalente alla pelle | 500 mSv | 50 mSv |
| Dose equivalente alle estremità | 500 mSv | Non indicata qui come limite autonomo |

Per la pelle il limite si riferisce alla media su qualsiasi superficie di 1 cm², indipendentemente dall'area complessivamente esposta. Questi limiti non sono obiettivi da raggiungere e non sostituiscono l'ottimizzazione. **Non si applica il limite della popolazione di 1 mSv alla prestazione medica del paziente:** quest'ultima si governa con giustificazione, ottimizzazione e strumenti pertinenti, inclusi i DRL.

'''
s=s.replace('## Principi e quadro teorico della radioprotezione',t+'## Principi e quadro teorico della radioprotezione',1)
t='''## Sicurezza RM e gravidanza

La risonanza magnetica non utilizza radiazioni ionizzanti. Il campo statico può però attrarre oggetti ferromagnetici, trasformandoli in proiettili; l'assenza di acquisizione non garantisce l'assenza del campo. Per accesso di persone, barelle, bombole, strumenti e dispositivi occorre il percorso di controllo del sito RM.

Per un impianto non basta chiedere se sia «metallico». Servono identificazione univoca e documentazione: **MR Safe** indica assenza di rischi noti negli ambienti RM previsti dalla classificazione; **MR Conditional** consente l'impiego soltanto nelle condizioni specificate; **MR Unsafe** indica rischio inaccettabile nell'ambiente RM. Un dispositivo conditional non è compatibile senza condizioni con ogni apparecchiatura o sequenza. La valutazione segue il modello organizzativo della struttura e coinvolge i responsabili previsti dal D.M. 14 gennaio 2021.

Le radiofrequenze possono produrre riscaldamento e ustioni, anche per configurazioni di contatto o circuiti conduttivi. I gradienti variabili producono rumore e possono indurre stimolazione periferica; la protezione uditiva segue il protocollo del sito. Nei sistemi con criogeni, il rilascio di gas può ridurre l'ossigeno disponibile e generare pressioni pericolose: ventilazione, evacuazione e risposta al quench appartengono al piano di sicurezza, senza manovre improvvisate. Campo statico, radiofrequenze, gradienti e criogeni richiedono controlli diversi.

**Gravidanza.** Prima di una prestazione con radiazioni ionizzanti occorre accertare la possibile gravidanza e informare i professionisti responsabili. Ai sensi dell'art. 166 del D.Lgs. 101/2020, giustificazione e ottimizzazione considerano donna e nascituro, urgenza, distretto, alternative e possibilità di rinvio. La gravidanza non determina da sola un divieto assoluto, ma nemmeno autorizza a procedere senza valutazione. In medicina nucleare anche l'allattamento richiede considerazione specifica del radiofarmaco. Per la RM, il D.M. 14 gennaio 2021 richiede particolare attenzione alla giustificazione e all'ottimizzazione e informazione della paziente. Le regole delle pazienti non vanno confuse con la tutela lavorativa delle operatrici gestanti.

**Verifica.** «Il paziente ha già effettuato una RM con quel dispositivo, quindi può entrare senza nuovi controlli»: affermazione errata. Vanno verificati dispositivo, condizioni e documentazione rispetto al sito e all'esame attuale; un precedente esame non dimostra che tutte le condizioni odierne coincidano.

'''
s=s.replace('## Casi guidati',t+'## Casi guidati',1);put(p,s)
p=cp(4);s=p.read_text(encoding='utf8')
s=s.replace("L'incidente grave è distinto in base alle conseguenze reali o potenziali gravi definite dai regolamenti.","L'incidente grave è un evento che ha causato, può avere causato o può causare, direttamente o indirettamente, morte, grave deterioramento temporaneo o permanente della salute oppure una grave minaccia per la salute pubblica. Non occorre quindi attendere che il danno si sia effettivamente prodotto.")
t='''### Classi di rischio e identificazione

Il MDR suddivide i dispositivi nelle classi **I, IIa, IIb e III**; l'IVDR usa **A, B, C e D**. La progressione esprime una diversa rilevanza regolatoria del rischio e incide sulla valutazione della conformità. Non è una graduatoria di prezzo o di utilità clinica: contano destinazione d'uso e regole dell'allegato VIII del rispettivo regolamento. Nel MDR assumono rilievo, fra gli altri aspetti, invasività, durata del contatto e funzioni del dispositivo; nell'IVDR conta anche l'impatto di un risultato errato sulla persona e sulla salute pubblica. Le due serie di classi non si scambiano e un analizzatore non riceve automaticamente la stessa classe di ogni test che vi si esegue.

L'**UDI** sostiene identificazione e tracciabilità. L'UDI-DI identifica il dispositivo in relazione a fabbricante e modello; l'UDI-PI ne identifica la produzione, per esempio mediante lotto o seriale secondo il prodotto. L'UDI-DI di base raggruppa dispositivi ai fini della documentazione e della banca dati ed è distinto dal codice del singolo lotto. UDI, numero d'inventario aziendale e marcatura CE hanno funzioni diverse: il primo non sostituisce l'etichetta, il secondo localizza il bene nell'organizzazione, la terza esprime conformità al quadro applicabile.

**Esempio.** Un avviso riguarda il modello X, lotti 12 e 13. Trovare in inventario «modello X» non basta per escludere o includere tutti gli esemplari: occorre risalire alla produzione interessata, alla collocazione e agli utilizzatori secondo i dati dell'avviso.

'''
s=s.replace('## Il ciclo di vita della tecnologia',t+'## Il ciclo di vita della tecnologia',1)
t='''### Azione correttiva di sicurezza e avviso

La **FSCA** è l'azione correttiva di sicurezza intrapresa dal fabbricante per motivi tecnici o medici per prevenire o ridurre il rischio di un incidente grave relativo a un dispositivo disponibile sul mercato. Può comportare interventi sul prodotto, aggiornamenti, richiamo o altre misure appropriate: non è sempre un ritiro fisico.

La **FSN** è l'avviso di sicurezza con cui il fabbricante comunica agli utilizzatori o clienti l'azione e le indicazioni pertinenti. Ricevere l'avviso non equivale ad aver completato l'azione: la struttura identifica prodotti e lotti coinvolti, informa i destinatari, esegue le attività richieste nel proprio ruolo e ne conserva evidenza. Non si estendono le istruzioni a modelli diversi né si sostituisce la FSCA con una riparazione non autorizzata.

**Verifica.** Un avviso richiede di identificare un lotto e sospenderne l'uso fino a una verifica autorizzata. La FSN è il documento ricevuto; la FSCA comprende le misure attuate sul campo. Archiviare il messaggio senza controllare la presenza del lotto lascia incompleta la gestione.

'''
s=s.replace('## HTA: valutare prima di adottare',t+'## HTA: valutare prima di adottare',1)
s=re.sub(r' Il capitolo è stato verificato nello step 15[^\n]*','',s);put(p,s)
changes={}
for n,ids,change in [(2,[35,36],'Integrati principi delle discipline, precisione/esattezza, calibrazione/QC e serie numerica commentata; gruppi biologici, contenimento, cappe, decontaminazione e categorie rifiuti.'),(3,[37,38],'Aggiunti CTDIvol, DLP, DAP, esempio calcolato, effetti, protezione, limiti normativi; rischi RM, impianti e gravidanza.'),(4,[40],'Esplicitati esiti dell’incidente grave, classi MDR/IVDR, UDI e FSCA/FSN; preservati termini 10/30 giorni.')]:
 for i in ids:changes[f'V07-{i:02}']={'change':change,'files':[str(cp(n)).replace('\\','/')],'evidence':'Nuove sezioni didattiche e soluzioni confrontate con le source note aggiornate il 3 ottobre; controllo specialistico e PDF successivi ancora necessari. Grafico QC richiesto al coordinatore per V07-35; testo e dati pronti.','status':'applicato'}
changes['V07-41']={'change':'Eliminati residui Humanizer, gate e step dalla prosa pubblica SA03/06–07 e SA04/04, preservando limiti informativi per il candidato.','files':[str(cp(4)).replace('\\','/')]+[str(next((B/'m-sa03-dirigenza-medica-sanitaria'/'chapters').glob(f'{n:02}-*.md'))).replace('\\','/') for n in [6,7]],'evidence':'Ricerca mirata dei residui e rilettura dei paragrafi conclusivi.','status':'applicato'}
Path('artifacts/correzioni-collana-2026-10-02/batch07.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
