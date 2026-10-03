from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters')
u.REF='sources/vol-09-esecuzione-verifica-2026-10-03.md'
slug='08-governo-esecuzione';t=u.read(slug)
start=t.index('Il capitolo mantiene un taglio metodologico')
end=t.index('### Mappa BANDO',start)
t=t[:start]+'''Il quadro che segue è verificato al 3 ottobre 2026. Devi conoscere sia le regole sia il metodo per applicarle: la data di avvio della procedura permette di individuare il regime pertinente, mentre contratto e capitolato precisano gli obblighi ammessi dalla legge. Una traccia priva dell'aliquota della penale richiede un'ipotesi dichiarata; una traccia che chiede il limite legale richiede invece di conoscere quel limite.

'''+t[end:]
t=t.replace('Il pagamento arriva dopo il controllo, non al suo posto.','Il pagamento del corrispettivo per prestazioni eseguite richiede il controllo. Va distinta l’anticipazione, che finanzia l’avvio ed è assistita dalla garanzia prevista dall’art. 125.')
start=t.index('Subappalto, modifiche e sospensioni\n',t.index('## N-TR02-08-03'))
end=t.index('### Caso ragionato',start)
t=t[:start]+'''### Subappalto: condizioni e responsabilità

Nel subappalto l’appaltatore affida parte della prestazione a un’impresa che organizza i mezzi e assume il rischio della propria esecuzione. L’art. 119 non prevede un limite generale del 30%: sono però nulli l’affidamento integrale a terzi e quello della prevalente esecuzione delle lavorazioni della categoria prevalente o dei contratti ad alta intensità di manodopera. La stazione appaltante può riservare prestazioni all’aggiudicatario, motivando nei documenti di gara le esigenze tecniche, di controllo, di sicurezza o di prevenzione criminale previste dalla norma. Può anche motivare limiti all’ulteriore subappalto; la cascata non è né sempre vietata né priva di controlli.

Per autorizzare il subappalto occorrono tre condizioni: parti da subappaltare indicate nell’offerta, qualificazione del subappaltatore e assenza delle cause di esclusione. L’affidatario trasmette contratto e documentazione almeno 20 giorni prima dell’inizio delle relative prestazioni. L’autorizzazione è rilasciata entro 30 giorni dalla richiesta, prorogabili una sola volta per giustificati motivi; decorso il termine opera il silenzio assenso. Il termine è dimezzato per subappalti inferiori al 2% delle prestazioni affidate oppure a 100.000 euro. I 20 giorni del deposito e il termine dell’autorizzazione sono adempimenti distinti.

Non basta chiamare un rapporto «fornitura» per sottrarlo ai controlli. Nei lavori, forniture con posa e noli a caldo rientrano comunque nel subappalto quando il singolo importo supera il 2% dell’appalto oppure 100.000 euro e la manodopera supera il 50% del subcontratto. Sono invece previste specifiche esclusioni, fra cui attività secondarie, accessorie o sussidiarie affidate a lavoratori autonomi e subfornitura a catalogo di prodotti informatici; restano le comunicazioni dovute. Esempio: posa da 80.000 euro in appalto da 2 milioni, con manodopera al 60%, supera il 2% dell’appalto, cioè 40.000 euro: il fatto di essere sotto 100.000 euro non evita la qualificazione come subappalto.

Appaltatore e subappaltatore rispondono solidalmente verso la stazione appaltante delle prestazioni subappaltate. Si aggiungono regole su retribuzioni, contribuzione, contratti collettivi, sicurezza e DURC. I costi della sicurezza e della manodopera relativi alle prestazioni subappaltate sono corrisposti senza ribasso. Il pagamento diretto ricorre per microimprese o piccole imprese, in caso di inadempimento del principale oppure su richiesta del subcontraente se la natura del contratto lo consente: non coincide con l’esonero da ogni responsabilità.

La disciplina vigente richiede una quota non inferiore al 20% delle prestazioni subappaltabili da affidare a PMI, consentendo all’offerente una diversa soglia motivata in relazione a oggetto, caratteristiche o mercato. Anche i subappalti e i subcontratti comunicati devono contenere le clausole di revisione prezzi previste dall’art. 119, comma 2-bis. Il controllo riguarda quindi condizioni del rapporto e filiera, oltre al nome dell’impresa.

### Modifiche: scegliere la base giuridica prima della percentuale

L’art. 120 ammette modifiche senza nuova gara in ipotesi definite. La disponibilità di fondi o il consenso dell’impresa non sono, da soli, una di queste ipotesi.

| Ipotesi | Condizioni decisive | Limite da ricordare |
| --- | --- | --- |
| Clausole e opzioni iniziali | Chiare, precise, inequivocabili; struttura e operazione economica restano inalterate. | Valore e condizioni già previsti, considerati nella stima iniziale. |
| Prestazioni supplementari | Cambio del contraente impraticabile per ragioni tecniche/economiche e fonte di notevoli disagi o sostanziali maggiori costi. | Aumento non oltre il 50% del valore iniziale per singola modifica; vietata l’elusione mediante modifiche successive. |
| Circostanze imprevedibili | Nuove disposizioni, eventi straordinari/forza maggiore, rinvenimenti o difficoltà geologiche e analoghe non prevedibili con la diligenza richiesta. | Aumento non oltre il 50%; struttura inalterata. |
| Modifica di piccolo valore | Sotto soglia UE e sotto il limite percentuale, senza alterare struttura e operazione economica. | Inferiore al 10% per servizi/forniture, al 15% per lavori; considerare il cumulo delle modifiche. |
| Modifica non sostanziale | Non cambia in modo rilevante concorrenza, equilibrio economico, ambito o identità del contraente fuori dai casi ammessi. | La qualificazione non dipende soltanto dall’importo. |

La sostituzione dell’appaltatore è ammessa soltanto nei casi del comma 1, lettera d), come una successione societaria che conservi i requisiti senza modifiche sostanziali né elusione. Il «quinto d’obbligo» non è una facoltà universale: per imporre aumenti o diminuzioni fino al 20% alle condizioni originarie deve esserci la previsione nei documenti iniziali richiesta dal comma 9.

**Caso numerico.** In un contratto di servizi da 200.000 euro, una modifica da 18.000 euro vale il 9%. Se il valore è anche sotto soglia UE, non altera la struttura e non vi sono precedenti modifiche da cumulare, può ricadere nel comma 3. Una seconda modifica da 8.000 euro porta il totale a 26.000, cioè 13%: quella base non basta più. Occorre un altro presupposto effettivo dell’art. 120 oppure una nuova procedura; dividere gli atti non azzera il cumulo.

Le modifiche e le varianti sono autorizzate dal RUP secondo l’ordinamento dell’ente; le modifiche progettuali del comma 7 sono approvate dalla stazione appaltante su proposta del RUP. Seguono aggiornamento del quadro economico, atti contrattuali, pubblicazioni e comunicazioni dovute, incluse quelle ad ANAC. Un ordine di servizio non può aggirare questi presupposti.

### Proroga, sospensione e ripresa

La proroga opzionale dell’art. 120, comma 10, è prevista fin dalla gara e opera alle condizioni stabilite. La proroga eccezionale del comma 11 richiede ritardi oggettivi e insuperabili nella conclusione della nuova procedura e il pericolo per persone, animali, cose o igiene pubblica, oppure un grave danno all’interesse pubblico in caso di interruzione. Dura solo quanto strettamente necessario; la mera convenienza di mantenere il fornitore non basta.

Diversa è la proroga del termine di ultimazione dei lavori, richiesta dall’esecutore con congruo anticipo per cause non imputabili a lui: il RUP decide entro 30 giorni, sentito il direttore dei lavori e, nei casi previsti, il CCT. Non comporta automaticamente nuove prestazioni o rinnovo del servizio.

Per circostanze speciali temporanee, imprevedibili alla stipula, che impediscono di procedere utilmente a regola d’arte, il direttore dei lavori dispone la sospensione e invia il verbale al RUP entro 5 giorni. Il RUP può disporla per necessità o pubblico interesse. Per opere sopra soglia si applica il regime dell’art. 121, comma 3, con parere del CCT ove costituito. Si proseguono le parti eseguibili se l’impedimento è parziale; cessata la causa, il RUP dispone ripresa e nuovo termine.

Se le sospensioni superano un quarto della durata prevista o comunque sei mesi complessivi, l’esecutore può chiedere la risoluzione senza indennità. Se la stazione appaltante si oppone, spettano i maggiori oneri oltre tali limiti. Contestazioni e riserve vanno documentate nei tempi dell’art. 121: non basta protestare informalmente a lavori conclusi. Le regole si applicano a servizi e forniture in quanto compatibili, riferendo al DEC le funzioni del DL e osservando le particolarità del comma 11.

### Penali e premi: un calcolo verificabile

Per il ritardo l’art. 126 prevede penali giornaliere fra **0,5 e 1,5 per mille** dell’ammontare netto contrattuale, secondo la clausola e le conseguenze del ritardo; il totale non supera il **10%** del netto. Il per mille non è il per cento. Accertamento, imputabilità, contestazione e controdeduzioni precedono la decisione.

In un contratto netto di 200.000 euro, la clausola fissa l’1 per mille al giorno. Otto giorni di ritardo imputabile producono 200.000 × 0,001 × 8 = **1.600 euro**. Il limite complessivo è 20.000 euro. La penale non autorizza l’impresa a restare inadempiente pagando indefinitamente: restano gli ulteriori rimedi contrattuali. Per i lavori il bando prevede un premio di accelerazione, nei limiti finanziari e alle condizioni dell’art. 126, dopo collaudo e con rispetto di obblighi e sicurezza; per servizi e forniture la previsione è facoltativa se compatibile.

### Revisione prezzi: obbligo, indici ed eccedenza

La clausola dell’art. 60 è obbligatoria nei documenti iniziali per i contratti che rientrano nel suo ambito. Nei servizi e nelle forniture l’allegato II.2-bis riguarda i contratti di durata, non le prestazioni istantanee. Va distinta la speciale esclusione dei prezzi già determinati sulla base di una propria indicizzazione, prevista dal comma 4-ter. Le clausole operano anche in diminuzione, non soltanto a favore dell’impresa.

| Contratto | Soglia che attiva la clausola | Quota dell’eccedenza riconosciuta |
| --- | --- | --- |
| Lavori | Variazione superiore al 3%. | 90% della parte oltre il 3%, sulle prestazioni da eseguire. |
| Servizi e forniture di durata | Variazione superiore al 5%. | 80% della parte oltre il 5%, sulle prestazioni da eseguire. |

La stazione appaltante monitora gli indici pertinenti con la frequenza prescritta e attiva automaticamente la clausola al superamento della soglia, anche senza domanda dell’impresa. «Automaticamente» non elimina il calcolo e la documentazione: significa che, accertati i presupposti, l’attivazione non è una concessione discrezionale. L’aumento delle fatture del singolo fornitore non sostituisce gli indici previsti.

**Esempio lavori.** Si assume un contratto nel nuovo regime, una variazione dell’indice pertinente del +8% e prestazioni residue interessate per 400.000 euro. L’eccedenza è 8% − 3% = 5%; il 90% dell’eccedenza è 4,5%. Revisione: 400.000 × 4,5% = **18.000 euro**. Non si applica il 90% all’intero aumento dell’8%.

**Esempio servizi.** In un contratto di durata, variazione +8% e prestazioni residue per 100.000 euro: (8% − 5%) × 80% = 2,4%; importo **2.400 euro**. I valori sono dati didattici, non rilevazioni ISTAT. Per variazioni negative si applica lo stesso criterio in diminuzione.

Per servizi e forniture può aggiungersi l’adeguamento ordinario all’indice inflattivo convenuto, ai sensi del comma 2-bis. Gli incrementi riconosciuti con tale meccanismo non si contano di nuovo nella variazione rilevante per la revisione straordinaria: evitare il doppio riconoscimento dello stesso aumento.

**La data conta.** L’allegato II.2-bis si applica ai servizi e alle forniture dalle procedure avviate dalla sua entrata in vigore. Per i lavori il nuovo sistema di indici TOL opera per procedure avviate dal **27 aprile 2026**, pubblicazione del decreto direttoriale MIT n. 743/2026. Il decreto consente anche applicazioni convenzionali a determinate procedure e contratti precedenti, nei limiti del quadro economico. Non si può trasferire senza verifica il nuovo regime a qualsiasi contratto storico. Nel caso di prova indica data, indice applicabile, periodo, prestazioni residue e calcolo.

### Anticipazione, SAL e saldo

L’anticipazione dell’art. 125 è pari al 20% del valore considerato dalla norma, elevabile fino al 30% nei documenti di gara. Nei lavori è versata entro 15 giorni dall’effettivo inizio; per appalto integrato si distinguono progettazione ed esecuzione e per contratti oltre 500 milioni valgono scadenze contrattuali specifiche. Nei servizi e nelle forniture pluriennali si considera ciascuna annualità, con versamento entro 15 giorni dall’inizio della prima prestazione utile dell’annualità.

Occorre una garanzia bancaria o assicurativa pari all’anticipazione maggiorata degli interessi legali riferiti al recupero; la garanzia diminuisce con il recupero progressivo. Il ritardo imputabile che impedisce l’esecuzione secondo i tempi comporta decadenza, restituzione e interessi. In un appalto lavori da 200.000 euro, senza incremento in gara, l’anticipazione è **40.000 euro**, non un pagamento per lavori già certificati. La garanzia deve coprire anche gli interessi: 40.000 euro da soli non ne esprimono l’intero importo.

L’allegato II.14, art. 33, esclude fra l’altro prestazioni immediate, non cronoprogrammabili, a consumo e talune prestazioni intellettuali o senza predisposizione di materiali/attrezzature. Per servizi di ingegneria e architettura è ammessa nei documenti una specifica anticipazione fino al 10%, nei limiti del quadro economico. Non estendere il 20% indistintamente a ogni incarico.

Negli acconti lavori, il DL adotta il SAL al raggiungimento delle condizioni e lo trasmette al RUP; questi emette il certificato di pagamento contestualmente e comunque entro 7 giorni. Il pagamento avviene entro 30 giorni dal SAL, salvo termine espresso fino a 60 giorni oggettivamente giustificato. Il saldo segue l’esito positivo di collaudo o conformità: certificato entro 7 giorni, pagamento ordinariamente entro 30 giorni dall’esito. La fattura non sostituisce il controllo e la sua emissione non è subordinata al certificato nei casi disciplinati dall’art. 125.

### Chiusura: collaudo e regolare esecuzione

Il collaudo riguarda i lavori, la verifica di conformità servizi e forniture. Accertano caratteristiche tecniche, economiche e qualitative, obiettivi e tempi. Il termine ordinario è sei mesi dall’ultimazione, elevabile a un anno per i casi di particolare complessità individuati nell’allegato II.14. Il certificato di collaudo diventa definitivo dopo due anni; non equivale a un’esenzione immediata da responsabilità per vizi.

Il certificato di regolare esecuzione (CRE) semplifica l’atto finale, non elimina l’accertamento. Per lavori fino a un milione di euro la stazione appaltante può usarlo in sostituzione del collaudo tecnico-amministrativo. Sopra un milione e sotto soglia UE vanno rispettate le esclusioni dell’art. 28 dell’allegato II.14: fra esse interventi sismici, particolari opere strutturali, opere in classi d’uso III/IV salvo manutenzione, specifiche forme del Libro IV e cumulo del RUP con progettista o DL. Il DL emette il CRE entro tre mesi dall’ultimazione e lo invia al RUP per conferma della completezza.

Per servizi e forniture sotto soglia, l’art. 50, comma 7, e l’art. 38 dell’allegato II.14 disciplinano la sostituzione della verifica di conformità con il CRE: emissione del DEC, conferma del RUP, termine di tre mesi dall’ultimazione. Quando RUP e DEC coincidono le funzioni restano distinguibili; nei casi di elevata complessità possono essere nominati verificatori diversi. Per il collaudo lavori servono indipendenza funzionale e rispetto delle incompatibilità dell’art. 116.

### Collegio consultivo tecnico

Il CCT previene controversie e risolve dispute tecniche durante l’esecuzione. È obbligatorio per lavori di realizzazione di opere pubbliche almeno pari alla soglia UE, comprese concessioni e partenariati pubblico-privati; negli altri casi ciascuna parte può chiederne la costituzione. Nel biennio 2026–2027 la soglia lavori è 5.404.000 euro. Non applicare automaticamente ai servizi il precedente automatismo legato a un milione di euro.

Il collegio ha tre componenti, oppure cinque per complessità dell’opera ed eterogeneità delle professionalità. Le parti li scelgono di comune accordo o concordano nomine di parte e presidente scelto dai componenti; in difetto interviene l’autorità individuata dall’allegato V.2. I compensi sono a carico delle parti, proporzionati e soggetti ai limiti legali; non sono liberamente determinabili dal solo RUP.

Il CCT esprime pareri o adotta determinazioni, eventualmente con valore di lodo contrattuale ai sensi dell’art. 808-ter c.p.c. Gli effetti non sono quelli di un semplice suggerimento informale: l’inosservanza rileva per la responsabilità e, salvo prova contraria, come grave inadempimento; l’osservanza delle determinazioni esclude la responsabilità erariale salvo dolo. Vanno quindi identificati tipo di pronuncia ed effetti, conservando quesito, istruttoria e decisione nel fascicolo.

'''+t[end:]
t=t.replace('non deve trattare la revisione prezzi come un automatismo','deve attivare la revisione prezzi quando risultano verificati i presupposti legali, senza confonderla con un aumento richiesto senza prova')
t=t.replace('Quando una traccia richiama penali, revisione prezzi, collegio consultivo tecnico, subappalto, sospensione, contabilità o pagamenti, non fissare numeri o termini se non sono forniti dalla traccia o da una fonte vigente. La risposta più solida è metodica: qualifica il fatto, individua la base applicabile, indica l’istruttoria necessaria e collega la decisione al fascicolo dell’esecuzione.','Quando una traccia richiama questi istituti, applica le regole illustrate e dichiara le ipotesi solo per i fatti che la traccia non fornisce.')
# Variante ASCII presente nel manoscritto.
start=t.index('Quando una traccia richiama penali, revisione prezzi') if 'Quando una traccia richiama penali, revisione prezzi' in t else -1
if start>=0:t=t[:start]+'''Riferimenti di studio: D.Lgs. 36/2023, artt. 60, 116, 119–121, 125–126 e 215; allegati II.2-bis, II.14 e V.2; decreto direttoriale MIT n. 743 del 30 marzo 2026, pubblicato il 27 aprile. Nel caso d’esame applica queste regole, dichiarando le ipotesi soltanto per i fatti non forniti dalla traccia.
'''
u.save(slug,t,['V09-20','V09-21','V09-22'],u.REF);u.record()
p=Path('wiki/topics/vol-09-appalti-pnrr-procurement.md');p.write_text(p.read_text(encoding='utf8').replace('`n','\n'),encoding='utf8')
