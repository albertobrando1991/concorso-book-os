from pathlib import Path
import importlib.util,re
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-tracciabilita-antifrode-spesa-2026-10-03.md'
slug='11-gestione-finanziaria-rendicontazione-controlli';t=u.read(slug)
t=re.sub(r'^last_compiled_from:.*$', 'last_compiled_from: ["sources/pagamenti-tracciabilita-contratti-pnrr-rendicontazione", "sources/vol-09-tracciabilita-antifrode-spesa-2026-10-03.md"]',t,flags=re.M)
t=t.replace('## N-TR02-11-02 · Controllo operativo sui codici','## N-TR02-11-02 · Tracciabilità, codici e condizioni di pagamento')
t=t.replace('## N-TR02-11-03 · Struttura del fascicolo','## N-TR02-11-03 · Fascicolo, conflitti e controlli antifrode')
t=t.replace('## N-TR02-11-04 · Controlli e casi','## N-TR02-11-04 · Doppio finanziamento, ammissibilità e rettifiche')
t=t.replace('## N-TR02-11-05 · Mini-esercizio','## N-TR02-11-05 · Allenamento e verifiche conclusive')
t=t.replace('Le procedure operative, i campi da compilare, i documenti da caricare e le scadenze non si imparano a memoria da un manuale generale.','Occorre conoscere le regole generali e distinguere quelle stabilite dalla singola misura. I campi di piattaforma e i documenti aggiuntivi richiesti possono variare.')
t=t.replace('Il manuale non può fissare requisiti mobili validi per ogni misura. Il metodo però è stabile:','I requisiti specifici dipendono dalla misura. La verifica comprende comunque questi elementi:')
t=t.replace('Non bisogna fissare nel capitolo requisiti tecnici variabili: bisogna insegnare al candidato a cercarli nel documento corretto.','Il capitolo 12 sviluppa il raccordo DNSH/CAM e un criterio ambientale concreto, distinguendo la regola generale dalle prescrizioni della categoria.')
anchor='### Controllo operativo sui codici'
t=u.replace(t,anchor,'''### Conti dedicati e filiera: legge 136/2010

L’articolo 3 della legge 136/2010 impone la tracciabilità dei flussi relativi alle commesse pubbliche per prevenire infiltrazioni criminali. L’obbligo riguarda appaltatori, subappaltatori e subcontraenti della filiera individuata dalla disciplina, non soltanto il pagamento finale dell’ente al contraente principale. L’importo modesto del contratto non è, da solo, un’esenzione.

Si utilizzano uno o più **conti bancari o postali dedicati**, anche in via non esclusiva. Non è obbligatorio aprire un conto nuovo per ciascun appalto: un conto può servire più commesse e operazioni diverse, purché siano rispettati comunicazioni e tracciabilità. L’operatore comunica alla stazione appaltante o all’amministrazione concedente gli estremi del conto e i dati delle persone delegate entro **sette giorni** dall’apertura; se il conto esiste già, il termine decorre dal primo utilizzo per operazioni relative a una commessa pubblica. Comunica anche le successive modifiche.

I movimenti seguono il bonifico bancario o postale oppure strumenti idonei a garantire la piena tracciabilità. Nei casi richiesti gli strumenti riportano **CIG e CUP**. La clausola con cui l’appaltatore assume gli obblighi di tracciabilità deve essere inserita nel contratto a pena di nullità assoluta; l’amministrazione verifica la clausola anche nei subappalti e subcontratti interessati. La filiera non può diventare il punto in cui il flusso perde identificazione.

Chi apprende l’inadempimento della propria controparte agli obblighi di tracciabilità deve comunicarlo immediatamente alla stazione appaltante e alla prefettura competente secondo l’articolo 3, comma 8. Il mancato utilizzo degli strumenti di pagamento tracciabili costituisce causa di risoluzione ai sensi del comma 9-bis. Va distinta questa fattispecie da un refuso: non ogni irregolarità documentale produce automaticamente la stessa conseguenza.

### Modalità particolari e sanzioni

I pagamenti dell’operatore a dipendenti, consulenti e fornitori di spese generali seguono le modalità dell’articolo 3, comma 2: conto dedicato e strumenti tracciabili. ANAC chiarisce che in tali pagamenti non occorre indicare il CIG; è una previsione per queste operazioni, non un’esenzione del contratto principale.

Per tributi, enti previdenziali e le altre ipotesi del comma 3 sono ammesse modalità diverse dal bonifico, mantenendo la documentazione della spesa. Per le spese giornaliere della fattispecie, fino a **1.500 euro**, sono ammessi sistemi diversi, con divieto di contante e obbligo documentale. La cifra non significa “affidamenti della PA senza CIG fino a 1.500 euro”: confondere acquisto contrattuale e spese dell’esecutore è un errore di ambito.

L’articolo 6 prevede sanzioni amministrative differenziate. Le transazioni senza avvalersi di banche o Poste comportano una sanzione dal 5% al 20% del valore; conto non dedicato, strumenti non idonei o omissione dei codici nei casi previsti rientrano nella fascia dal 2% al 10%. Il reintegro irregolare del conto è sanzionato dal 2% al 5%; comunicazioni omesse, tardive o incomplete dei dati richiesti comportano da 500 a 3.000 euro. La competenza applicativa è del prefetto individuato dalla norma. Il candidato deve riconoscere il comportamento contestato prima di scegliere la conseguenza.

### CUP negli atti e codici nelle fatture

L’articolo 11 della legge 3/2003 prevede il CUP per i progetti di investimento pubblico. Il comma 2-bis stabilisce la nullità degli atti amministrativi che dispongono il finanziamento pubblico o autorizzano l’esecuzione di tali progetti se manca il relativo CUP, elemento essenziale. Non è una regola di nullità indistinta di ogni foglio del fascicolo: si identifica anzitutto il tipo di atto.

Per le fatture elettroniche verso la PA, l’articolo 25 del decreto-legge 66/2014 richiede il CIG, salvo i casi di esclusione previsti, e il CUP per opere pubbliche, manutenzione straordinaria, interventi finanziati da contributi comunitari e negli altri casi indicati dalla norma. Il comma 3 pone una regola precisa: **la PA non può pagare la fattura che non riporta i codici obbligatori**.

Prima dell’ordinazione, dunque, si controllano presenza e correttezza dei codici, oltre alle verifiche sostanziali. Se il codice manca ma è obbligatorio, non basta scriverlo su un prospetto interno e procedere al pagamento: si attiva la modalità di regolarizzazione ammessa dal sistema di fatturazione e dalla disciplina pertinente, conservando la traccia. Se il pagamento è già avvenuto, l’omissione non diventa lecita per effetto del fatto compiuto; vanno accertati il passaggio irregolare, gli effetti e le azioni necessarie.

'''+anchor)
anchor='### Frode e anomalie'
t=u.replace(t,anchor,'''### Regolamento finanziario UE e gestione del conflitto

Il riferimento europeo vigente è l’articolo **61 del regolamento (UE, Euratom) 2024/2509**. La regola riguarda le persone coinvolte nell’esecuzione del bilancio, comprese autorità nazionali, attività preparatorie, audit e controlli. Non si limita a chi firma il mandato. Si devono prevenire anche le situazioni che possono essere oggettivamente percepite come conflittuali.

Il conflitto può dipendere da legami familiari o affettivi, interessi economici o altri interessi personali, diretti o indiretti, che compromettono l’esercizio imparziale e obiettivo della funzione. La persona comunica il rischio al superiore competente; quest’ultimo valuta e conferma per iscritto se il conflitto esiste. Se accertato, l’autorità competente fa cessare la partecipazione della persona alla materia e adotta le ulteriori misure appropriate. La dichiarazione è quindi l’inizio del presidio, non la sua conclusione.

Nel PNRR l’articolo 22 del regolamento 2021/241 richiede controlli efficaci per prevenire, individuare e correggere frodi, corruzione e conflitti, tutelare le risorse e recuperare gli importi indebitamente utilizzati. Sul piano nazionale si raccordano gli obblighi di astensione e, per i contratti, l’articolo 16 del Codice. Una valutazione scritta deve identificare i fatti e il ruolo, non limitarsi alla formula “nessun problema”.

### Titolare effettivo: risalire alla persona fisica

La raccolta dei dati sui destinatari dei fondi, sui contraenti e sui titolari effettivi pertinenti consente verifiche incrociate e individuazione di collegamenti rilevanti. **Titolare effettivo** è la persona fisica cui, in ultima istanza, è riconducibile proprietà o controllo; non coincide necessariamente con il legale rappresentante che firma l’offerta.

L’articolo 20 del d.lgs. 231/2007 stabilisce criteri graduati. Per le società di capitali è indicativa la partecipazione **superiore al 25%**, diretta o indiretta nelle forme previste. Se l’assetto proprietario non consente un’individuazione univoca, si esaminano controllo dei voti e influenza dominante, anche tramite vincoli contrattuali. Solo quando i criteri precedenti non permettono l’identificazione si applica il criterio residuale dei poteri di rappresentanza, amministrazione o direzione, documentando le ragioni. Per altre persone giuridiche valgono le specificità del comma 4: non si applica meccanicamente una quota societaria a qualsiasi ente.

**Caso.** Alfa ha tre soci persone fisiche: Anna 40%, Bruno 35%, Carla 25%; nessun altro elemento di controllo è indicato. Anna e Bruno superano il 25% e risultano individuati attraverso la proprietà; Carla non supera tale soglia. L’amministratore Davide, privo di partecipazioni e senza ulteriori poteri di controllo indicati nel caso, non sostituisce automaticamente Anna e Bruno nella dichiarazione. Se compare soltanto il nome di Davide, l’ufficio richiede il chiarimento e documenta la ricostruzione.

Se il funzionario incaricato di verificare la prestazione è legato familiarmente ad Anna, occorrono comunicazione, valutazione e misure sul conflitto. Non basta che Alfa abbia prodotto una dichiarazione societaria; non è neppure corretto concludere da quel solo legame che sia stata commessa una frode. I due controlli si parlano, ma rispondono a domande diverse: chi controlla l’impresa e chi può decidere imparzialmente per l’amministrazione.

'''+anchor)
t=t.replace('La frode richiede elementi più gravi e va trattata con i canali previsti.','L’irregolarità è una violazione che produce o può produrre un pregiudizio agli interessi finanziari dell’Unione; può derivare anche da errore non intenzionale. La frode implica una condotta intenzionale, come l’uso deliberato di documenti falsi per ottenere risorse non dovute, nei presupposti della fattispecie applicabile. La gravità apparente non sostituisce l’accertamento dell’intenzionalità e degli altri elementi richiesti.')
anchor='Rettifiche, recuperi e chiusura'
t=u.replace(t,anchor,'''### Calcolo risolto della quota rendicontabile

Il caso seguente riguarda una misura didattica a rimborso di costi. Dati: fattura pagata di **122.000 euro**, formata da imponibile di 100.000 e IVA di 22.000; l’IVA è recuperabile e, per le regole esplicitamente assunte nel caso, non è ammissibile. Dei 100.000 euro netti, 10.000 riguardano attività estranee al progetto. Le restanti condizioni di ammissibilità sono soddisfatte. Il contributo copre l’80% della spesa ammissibile, entro un massimale non raggiunto.

| Passaggio | Calcolo | Esito |
| --- | --- | --- |
| Escludere l’IVA non ammessa | 122.000 − 22.000 | 100.000 euro |
| Escludere la parte non pertinente | 100.000 − 10.000 | 90.000 euro ammissibili |
| Applicare la quota finanziata | 90.000 × 80% | 72.000 euro di contributo |
| Ricostruire l’onere dell’ente | 122.000 − 72.000 | 50.000 euro |

I 50.000 euro dell’ente si compongono di 18.000 di cofinanziamento sulla parte ammissibile, 10.000 di prestazione estranea e 22.000 di IVA. Il prospetto quadra: **72.000 + 18.000 + 10.000 + 22.000 = 122.000**. Rendicontare 122.000 o calcolare l’80% sull’intera fattura sovrastimerebbe il contributo. Rendicontare 90.000 come base ammissibile non significa ricevere automaticamente 90.000 di rimborso.

Il trattamento dell’IVA e la percentuale dell’80% sono **dati del caso**, non regole universali del PNRR o di tutti i fondi UE. Prima del calcolo reale si verificano disciplina della misura, recuperabilità e condizioni specifiche. Analogamente, quando il finanziamento usa costi semplificati o risultati, non si sostituisce il metodo previsto con una rendicontazione analitica inventata.

### Cofinanziamento e duplicazione: prova numerica

L’articolo 9 del regolamento RRF ammette complementarità con altri programmi e strumenti UE a condizione che non coprano lo stesso costo. Per un costo ammissibile di 100.000 euro, una ripartizione di 60.000 al programma A e 40.000 al programma B può essere consentita se le rispettive regole ammettono il cumulo e le quote sono separate. La stessa fattura può documentare quote diverse; l’identità del documento non basta, da sola, a dimostrare duplicazione.

Se invece ciascun programma riceve una richiesta di 60.000 sulla medesima base di 100.000, la somma è 120.000: **20.000 euro risultano sovrapposti**. Anche restare sotto il totale non basta se una misura vieta il cumulo o se le quote attribuite coincidono materialmente. Il controllo deve ricostruire costo, quota e regola, non soltanto sommare gli importi.

Nel prospetto di riconciliazione si indicano identificativo fattura, imponibile, IVA e trattamento, costo escluso, base ammissibile, quota per fonte, quota dell’ente e pagamento. Si collegano atti di concessione e richieste già presentate. Se emerge una sovrapposizione si blocca l’imputazione non corretta, si rettifica con la procedura prevista e, se somme sono state già erogate, si gestiscono le conseguenze finanziarie e gli eventuali recuperi.

### Rettifiche, recuperi e chiusura''')
t=u.replace(t,"La spesa non va descritta come inesistente. Il servizio c'è e il pagamento risulta. Il problema è diverso: il fascicolo non dimostra ancora in modo completo il percorso della spesa.","Il servizio non va descritto come inesistente, ma il pagamento presenta una violazione specifica: l’articolo 25, comma 3, del decreto-legge 66/2014 vietava di pagare la fattura priva del CIG obbligatorio. Nel caso non è indicata alcuna esclusione applicabile. Il fatto che il CUP sia corretto non sostituisce il CIG e il pagamento già avvenuto non sana l’omissione. Inoltre il fascicolo non dimostra ancora in modo completo la verifica della prestazione.")
t=u.replace(t,"La seconda azione riguarda il codice mancante. L'ufficio controlla gli atti della procedura, il contratto, le istruzioni di fatturazione e le regole della misura. Se è possibile integrare o correggere il dato secondo le modalità ammesse, la correzione viene effettuata e conservata. Se non è possibile, la voce resta segnalata come rischio e viene sottoposta alla decisione prevista.","La seconda azione riguarda il codice mancante e il pagamento irregolare. L’ufficio ricostruisce perché il controllo preventivo non ha bloccato la fattura, verifica il CIG corretto e attiva la regolarizzazione documentale consentita, senza modificare retroattivamente il documento originario. Se anche il movimento finanziario omette i codici richiesti, si esamina separatamente la disciplina della legge 136/2010. La correzione del dato, gli effetti della violazione e l’ammissibilità della spesa sono valutazioni distinte: la prima non chiude automaticamente le altre.")
t=t.replace('La terza azione è la riconciliazione.','La terza azione è la riconciliazione, accompagnata dalla valutazione delle conseguenze e dalle comunicazioni ai soggetti competenti secondo le regole applicabili.')
t+='\n### Norme da collegare al caso\n\nLegge 136/2010, artt. 3 e 6; legge 3/2003, art. 11; decreto-legge 66/2014, art. 25; regolamento (UE) 2021/241, artt. 9 e 22; regolamento (UE, Euratom) 2024/2509, art. 61; d.lgs. 231/2007, art. 20; d.lgs. 36/2023, art. 16. Per la distinzione fra irregolarità e frode: regolamento (CE, Euratom) 2988/95, art. 1, e direttiva (UE) 2017/1371, art. 3. FAQ ANAC sulla tracciabilità, aggiornate l’11 febbraio 2026.\n'
u.save(slug,t,['V09-28','V09-29'],u.REF);u.record()
