from pathlib import Path
import json,re
O=Path('artifacts/correzioni-collana-2026-10-02');p=Path('wiki/books/moduli/m-fc05-authority-indipendenti/chapters/15-laboratorio-prove-authority.md');s=p.read_text(encoding='utf8')
s=s.replace('Le fonti normative e regolamentari vanno verificate sul bando e al cut-off della prova.',"Le regole usate nelle soluzioni sono quelle consolidate nei capitoli precedenti al 3 ottobre 2026; il bando target può richiedere un diverso riferimento temporale. Dati, imprese e dossier sono didattici. Tempo suggerito: 25 minuti per G/E/P1–P3 e 15 per P4; prevale sempre il tempo del bando. Copri la soluzione, redigi la tua risposta e poi confronta le singole conclusioni.")
data={
'G1':'''**Dossier didattico.** Messaggio principale: «abbonamento a una biblioteca digitale, senza vincoli». Prezzo 10 euro al mese; al recesso entro dodici mesi si richiedono 90 euro. La clausola appare soltanto in un documento scaricabile dopo il pulsante di acquisto. Sono disponibili schermate datate, contratto e dodici addebiti contestati. Non si tratta di un servizio di comunicazione elettronica.

**Soluzione modello.** La questione rientra nella tutela del consumatore: AGCM, articoli 20–22 e 27 del Codice del consumo. Il messaggio può alterare la scelta economica facendo credere che l'uscita non comporti un costo rilevante; la disponibilità remota della clausola non dimostra da sola che l'informazione sia tempestiva e comprensibile. L'istruttoria acquisisce versioni delle pagine, percorso di acquisto, evidenza della clausola prima dell'ordine, periodi della campagna, contratti e reclami. Si valuta il consumatore destinatario e l'effettiva presentazione, senza dedurre la scorrettezza dal solo numero di reclami. La contestazione permette accesso e difese secondo il procedimento applicabile; eventuali misure cautelari richiedono i propri presupposti. Se i fatti sono confermati, può essere ordinata la cessazione della pratica e applicata la sanzione pertinente. Il rimborso richiesto dal singolo segue il proprio percorso contrattuale/giudiziario o ADR: la sanzione pubblica non è un risarcimento. Non si attribuisce il caso ad AGCOM soltanto perché il servizio è online.

**Esito da ottenere:** qualificazione consumer e ipotesi ingannevole motivata, istruttoria mirata, separazione enforcement/rimedio. **Ripasso:** capitoli 5, 6 e 8.
''',
'G2':'''**Dossier didattico.** Il Comune Alfa pubblica nome, punteggio, indirizzo di casa e copia della carta d'identità dei candidati; il fornitore tecnico è tedesco. Il trattamento è svolto per la selezione pubblica e il fornitore opera sulle istruzioni comunali. Non è indicata una norma che imponga indirizzi e documenti di identità nella graduatoria pubblica.

**Soluzione modello.** Il Comune determina finalità e mezzi essenziali del trattamento; si controlla l'atto di designazione del responsabile ex articolo 28 e l'effettiva condotta del fornitore. La pubblicità della graduatoria non estende automaticamente la base giuridica a ogni documento raccolto: gli articoli 5 e 6 GDPR richiedono finalità, necessità e minimizzazione. Il reclamante indica URL, data, dati esposti e misure richieste, allegando prove; il Garante acquisisce fonte della pubblicazione, istruzioni, impostazioni e log. Per il trattamento comunale italiano vale **55(2)**: non opera lo sportello unico dell'articolo 56, anche con responsabile tedesco. Si valuta la limitazione dell'esposizione e la conformazione, assicurando garanzie; ammonimento e sanzione richiedono i relativi presupposti. Il Garante informa entro tre mesi; articolo 143 del Codice per nove/dodici mesi e sospensione della cooperazione pertinente. Il risarcimento non è liquidato dal Garante. La conclusione propone una rimozione mirata dei dati eccedenti, mantenendo la pubblicità lecita della graduatoria, senza formulare una sanzione numerica priva di istruttoria.

**Esito da ottenere:** minimizzazione e competenza pubblica, istruttoria, misura mirata. **Ripasso:** capitolo 13.
''',
'G3':'''**Dossier didattico.** Segnalazione interna al RPCT il 2 settembre, ricevuta il 4; documenti di pagamento per prestazioni apparentemente non eseguite. Valutazione negativa del 20 settembre, a fronte di precedenti positive. Il dirigente invoca genericamente «scarso rendimento», senza produrre indicatori. Un collega facilitatore è escluso da una riunione.

**Soluzione modello.** Si controllano ambito pubblico, informazioni lavorative, violazione pertinente e fondato motivo ex ante; non occorre una sentenza sul contratto. La comunicazione delle presunte ritorsioni va ad ANAC ex articolo **19**, distinta dalla segnalazione esterna ex articolo 6. Per il segnalante, dimostrata la segnalazione protetta e allegata la misura, opera la presunzione dell'articolo **17**: è il decisore a dover provare ragioni estranee. La formula «scarso rendimento» non basta; servono obiettivi, misurazioni, criteri applicati e documenti contemporanei. La cronologia non sostituisce tutti i presupposti ma non si rovescia sul segnalante l'onere di provare il movente interiore. Il facilitatore può avere tutela, senza automatica estensione di tale presunzione. Si proteggono identità e documenti, acquisendo le difese del soggetto coinvolto. ANAC valuta la ritorsione e le sanzioni attribuite; il giudice decide nullità, ripristino e danni. La verifica delle prestazioni e dei pagamenti continua sul distinto piano contrattuale, senza che l'eventuale archiviazione della segnalazione escluda da sola la protezione.

**Esito da ottenere:** articolo 6/19, presunzione e limite soggettivo, ANAC/giudice. **Ripasso:** capitolo 14.
''',
'E1':'''**Dossier didattico.** Due tipi di reclamo: semplice e complesso. Periodo A: 80 semplici con media 10 giorni e 20 complessi con media 30. Periodo B: 20 semplici a 10 giorni e 80 complessi a 30. Costi complessivi invariati; conteggi completi e tempi riferiti allo stesso evento finale. Il dato non contiene uno standard legale.

**Soluzione e calcolo.** La media ponderata A è (80 × 10 + 20 × 30)/100 = **14 giorni**; B è (20 × 10 + 80 × 30)/100 = **26 giorni**. L'aumento di dodici giorni non deriva qui da peggioramento all'interno dei gruppi: i tempi di ciascun tipo sono invariati, cambia la composizione. Si richiedono criteri di classificazione, distribuzioni e code, reclami aperti non inclusi, carichi, risorse e casi fuori standard. Per confrontare l'efficienza, si può mantenere la composizione iniziale: 80% × 10 + 20% × 30 = 14 anche in B. Questa standardizzazione risponde a una domanda diversa dalla durata effettivamente sperimentata dall'insieme degli utenti, che resta 26. Non si elimina quindi il disagio aggregato. La nota propone monitoraggio per tipologia, mediana/percentili e arretrato; verifica la competenza e lo standard settoriale prima di ipotizzare penalità. Costi invariati non provano né efficienza né violazione. Un incentivo deve evitare che i casi complessi siano riclassificati o esclusi per migliorare artificialmente la media.

**Esito da ottenere:** calcolo 14/26, effetto composizione, dati mancanti e incentivo senza distorsioni. **Ripasso:** capitoli 7 e 9.
''',
'E2':'''**Dossier didattico.** Consultazione su accesso a rete, ipotizzando verificata la fonte attributiva dell'Autorità. Opzione 0: nessun nuovo obbligo, costi/benefici incrementali nulli. A: costo annuo 12.000 euro, beneficio annuo 18.000. B: costo 35.000, beneficio 42.000. In uno scenario avverso, il beneficio B scende a 30.000. Valori didattici stimati per un anno; distribuzione dei benefici ancora ignota.

**Soluzione modello.** Il problema va formulato come ostacolo verificabile all'accesso, non come preferenza per una tecnica. La consultazione chiede dati su richieste respinte, capacità, prezzi, investimenti e costi di adeguamento, con risposte comparabili e motivazione delle stime. A produce beneficio netto **6.000**; B **7.000**, ma nello scenario avverso B scende a **−5.000**. Il vantaggio centrale di B su A è solo 1.000 a fronte di 23.000 di maggior costo: non basta il beneficio lordo più alto per sceglierla. Si indagano probabilità/scenari, effetti su piccoli operatori e utenti, capacità di attuazione, oneri informativi e alternative meno onerose. I contributi non sono voti: il peso dipende dalla qualità delle evidenze. La decisione motiva la scelta e le osservazioni non accolte, prevede un indicatore sull'accesso effettivo e una revisione a data definita. Con questi dati non si inventa la probabilità dello scenario avverso; si mostra che la preferenza è sensibile all'incertezza.

**Esito da ottenere:** opzione zero, netti, incertezza e consultazione non referendaria. **Ripasso:** capitolo 4.
''',
'E3':'''**Dossier didattico.** Costi diretti regolati 500.000 euro; non regolati 300.000. Costi comuni 300.000. Il gestore chiede di imputare tutti i comuni al ramo regolato. Le ore verificabili di attività di supporto sono 6.000 per il regolato e 4.000 per il non regolato; si assume, per il calcolo, che siano un driver causale adeguato. RAB ammessa 1 milione, WACC 6%, ammortamento riconosciuto 50.000; quantità 10.000 unità. Si assume assenza di altre componenti e limiti: non è un metodo tariffario nazionale.

**Soluzione e calcolo.** Quota regolata del driver = 6.000/10.000 = **60%**. Comuni attribuiti al regolato = 300.000 × 60% = **180.000**; al non regolato **120.000**. Totali operativi: **680.000** e **420.000**, la cui somma 1.100.000 riconcilia i costi totali. La proposta del gestore avrebbe imputato 800.000 al regolato, cioè **120.000 in eccesso**, trasferendo il relativo onere fra attività.

Nelle sole ipotesi della traccia, remunerazione = 1.000.000 × 6% = **60.000**; ricavo riconosciuto = 680.000 + 50.000 + 60.000 = **790.000**. Tariffa media didattica = 790.000/10.000 = **79 euro per unità**. La proposta non corretta darebbe (800.000 + 50.000 + 60.000)/10.000 = **91 euro**: differenza **12 euro**. Ammortamento e remunerazione sono componenti diverse e non si somma l'intera RAB al ricavo annuo. Prima di deliberare si validano contabilità separata, pertinenza dei costi, assenza di duplicazioni, driver e registrazioni delle ore, riconciliazione al bilancio e metodo settoriale effettivo. Se il driver fosse manipolato, il risultato numerico corretto non renderebbe ammissibile l'imputazione.

**Esito da ottenere:** 180/120 mila, 790 mila, 79 euro; controllo del driver. **Ripasso:** capitoli 7 e 9.
''',
'P1':'''**Dossier didattico.** Una piattaforma designata VLOP pubblica una nuova regola sui contenuti e offre ai professionisti maggiore visibilità dietro commissione. Non è dato sapere se sia designata gatekeeper. Un rapporto segnala possibili rischi sistemici nella diffusione di contenuti illegali; un venditore lamenta anche una retrocessione dell'offerta. Non sono note posizione dominante e definizione del mercato.

**Soluzione modello.** Il DSA è il regolamento 2022/2065. Per gli obblighi della sezione 5 del capo III sulle VLOP/VLOSE, inclusi i rischi sistemici, la competenza di vigilanza/enforcement è **esclusiva della Commissione** ex articolo 56. AGCOM, coordinatore italiano, coopera nelle funzioni attribuite: non assume per questo ogni decisione sulla VLOP. Per gli altri obblighi DSA della piattaforma occorre applicare il riparto dell'articolo 56, inclusi i poteri della Commissione e il coordinatore competente; la presenza di un utente italiano non risolve da sola il caso. La retrocessione commerciale richiede condizioni, criteri, motivazioni e dati: non basta l'etichetta «piattaforma» per provare abuso ex articolo 102 TFUE. Un'ipotesi consumer va separata dalla controversia del professionista. Il DMA riguarda gatekeeper designati e specifici obblighi; senza verifica della designazione non lo si applica per analogia. Si acquisiscono atto di designazione, condizioni, criteri di visibilità, remunerazioni, comunicazioni, log ed effetti, indirizzando ciascun profilo all'autorità competente senza duplicare decisioni.

**Esito da ottenere:** esclusiva Commissione per III.5, nessun gatekeeper presunto, condotte separate. **Ripasso:** capitoli 8 e 10.
''',
'P2':'''**Dossier didattico.** Banca italiana raccomanda personalmente a una cliente retail un titolo complesso per il 70% dei risparmi. Mancano dati su capacità di perdita e obiettivi; la perdita contestata è 40.000 euro. Reclamo rimasto senza risposta per 70 giorni, presentato quattro mesi fa. La banca è LSI e la redditività è scesa; non sono forniti dati patrimoniali o di liquidità.

**Soluzione modello.** La raccomandazione configura consulenza: serve **adeguatezza**, non la sola appropriatezza. Senza informazioni necessarie non si formula una raccomandazione; si esaminano conoscenza/esperienza, situazione finanziaria e capacità di perdita, obiettivi e tolleranza al rischio, non soltanto il documento firmato. Si acquisiscono profilatura, raccomandazione e motivazione, costi, conflitti e registrazioni. Il piano di condotta rientra nella disciplina MiFID/TUF e nella competenza Consob secondo il riparto; i 40.000 euro sono entro il limite ACF di 500.000 e il reclamo soddisfa i dati temporali della traccia, restando da controllare gli altri requisiti. Non è ABF per il solo fatto che il venditore è banca. Il rendimento negativo non prova da solo una violazione e ACF non sanziona. Sul piano prudenziale, la LSI è vigilata direttamente dall'autorità nazionale nel SSM; autorizzazione e altri procedimenti comuni coinvolgono BCE. Redditività minore richiede analisi di modello di attività, rischi, capitale e liquidità, non una diagnosi automatica di dissesto. Le due istruttorie usano dati e finalità differenti.

**Esito da ottenere:** adeguatezza e ACF, separazione dalla prudenza, assenza di dissesto presunto. **Ripasso:** capitoli 11–12.
''',
'P3':'''**Dossier didattico.** Polizza danni: contraente chiede 12.000 euro; diniego confermato dopo reclamo documentato del 1° settembre 2026. I fatti sono di giugno 2026. Non vi sono altri procedimenti. Fondi ammissibili SCR 90 milioni, SCR 100, MCR 40; crescita premi 25%. Si assume che il MCR sia coperto con fondi ammissibili appropriati.

**Soluzione modello.** Il rapporto di copertura SCR è **90%**, insufficiente: coprire il distinto MCR non cancella la criticità. La crescita dei premi non prova solvibilità; si richiedono composizione rischi, riserve tecniche, fondi, riassicurazione, liquidità, ORSA e piano di intervento pertinente. IVASS vigila su solvibilità e condotta nei propri ambiti. Sul sinistro si esaminano contratto, esclusioni, informativa, distribuzione, evento e motivazione dei dinieghi seriali; la serie può segnalare un problema di condotta, senza dimostrare che ogni richiesta sia fondata. Per il contraente la domanda di 12.000 è entro il limite AAS danni di 25.000; risposta negativa al reclamo consente l'accesso senza attendere ulteriormente 45 giorni, verificati gli altri presupposti. Non si usa il limite di 2.500, riservato al danneggiato con azione diretta. AAS decide su documenti, non irroga sanzioni e non dispone CTU; resta il giudice. Il ricorso individuale non risolve il deficit patrimoniale, così come l'intervento prudenziale non determina da solo il diritto all'indennizzo.

**Esito da ottenere:** SCR 90%, AAS corretto, condotta/solvibilità distinte. **Ripasso:** capitolo 12.
''',
'P4':'''**Dossier.** The service is a designated very large online platform. The proposed measure concerns systemic risk duties under Chapter III, Section 5 of the Digital Services Act. Prepare a cooperation memo; do not assume that the national authority may adopt the final enforcement measure.

**Model memo (108 words).** The reported systemic risk concerns a designated very large online platform. Under Article 56 of the Digital Services Act, the Commission has exclusive competence to supervise and enforce the obligations in Chapter III, Section 5. Our national authority should preserve the evidence, identify the relevant duties and cooperate with the Commission through the applicable procedures. The file should distinguish verified facts from allegations and document the platform's response. Cooperation supports consistent enforcement and protects procedural rights; it does not transfer the Commission's exclusive powers to a national body. We should therefore propose a documented referral and assistance, leaving the competent institution to determine the appropriate enforcement action.

**Controllo.** La soluzione nomina il presupposto VLOP, il riparto e un passo operativo. Non promette una decisione nazionale che la cooperazione non può rendere competente. **Ripasso:** capitoli 3 e 10.
'''
}
for key,body in data.items():
 a=s.index('### Percorso '+key[0]+' — Simulazione '+key+':');b=s.find('\n### ',a+5)
 if b<0:raise ValueError(key)
 block=s[a:b];start=block.find('**Chiave di correzione.**')
 if key=='P4':start=block.index('**Model outline.**')
 # Nucleus 03 was inserted after P2; keep it outside its solution.
 suffix=''
 if '## N-MF05-15-03' in block:suffix='\n\n## N-MF05-15-03 · Poteri, procedura e conseguenze\n'
 s=s[:a]+block[:start]+body+suffix+s[b:]
s=s.replace('| 3. Fonte prudente | Ho richiamato la fonte o dichiarato la necessità di verificarla? |','| 3. Fonte corretta | Ho identificato la regola applicabile e l’ho applicata correttamente? Dichiarare ignoranza non vale il punto. |')
s=s.replace('Una risposta sotto 6/10',"Un'attribuzione di potere a un'autorità incompetente o una regola sostanziale errata richiedono correzione anche con un totale alto. La prudenza vale quando manca un fatto; non sostituisce lo studio di una norma spiegata nel volume. Una risposta sotto 6/10")
s=s.replace('richiami puntuali a  |','richiami puntuali al VOL-01, capitoli su procedimento e prove |')
s=s.replace('### Mini-esercizio di consolidamento\n\nScegli','## N-MF05-15-05 · Consolidamento e verifica\n\n### Mini-esercizio di consolidamento\n\nScegli').replace('\n## N-MF05-15-05 · Consolidamento e verifica\n\n| Campo','\n| Campo')
a=s.index("### Checklist per una nota d'ufficio");s=s[:a]+'''### ▣ Verifica ragionata

**Quesito 1.** Nella simulazione E1, la media sale da 14 a 26 giorni ma resta invariata in ogni categoria. È dimostrata una minore efficienza interna?

**Risposta corretta:** no. Nei dati proposti cambia la composizione; si distinguono esperienza aggregata dell'utente e prestazione a composizione costante. Occorre verificare comunque arretrato, distribuzioni e standard applicabili.

**Quesito 2.** Nella E3, attribuire tutti i 300.000 euro comuni al regolato produce lo stesso risultato del driver 60%?

**Risposta corretta:** no. Il driver attribuisce 180.000 al regolato; la proposta eccede di 120.000, equivalenti a 12 euro per unità nelle ipotesi. Il driver deve essere verificabile e causalmente adeguato.

**Quesito 3.** L'opzione B della E2 è sempre preferibile perché produce 42.000 euro di benefici?

**Risposta corretta:** no. Il netto centrale è 7.000, poco sopra i 6.000 di A, e lo scenario avverso scende a −5.000. Costi, incertezza, distribuzione e fattibilità vanno valutati; non si inventano probabilità.

**Quesito 4.** Una banca raccomanda un prodotto senza dati finanziari del cliente. Il solo questionario di conoscenza ed esperienza risolve la P2?

**Risposta corretta:** no. La consulenza richiede adeguatezza, che comprende situazione finanziaria e obiettivi. L'appropriatezza ha oggetto diverso e non autorizza a eludere gli obblighi della consulenza.

**Quesito 5.** Nel memo P4, la cooperazione rende AGCOM competente alla decisione sugli obblighi VLOP della sezione 5?

**Risposta corretta:** no. L'articolo 56 riserva tali poteri alla Commissione. La soluzione deve proporre cooperazione e trasmissione documentata, non una misura nazionale priva di competenza.

**Quesito 6.** In una prova chiusa, scrivere «verificherò la norma» assegna sempre il punto fonte della rubrica?

**Risposta corretta:** no. Serve la regola pertinente applicata correttamente. Si dichiara l'incertezza quando la traccia non fornisce un fatto necessario; non si scambia l'assenza di preparazione normativa per cautela professionale.

### Caso ragionato di chiusura

**Traccia.** Una simulazione di 25 minuti assegna la E3. Il candidato calcola 91 euro, propone di sanzionare il gestore per abuso di posizione dominante e dichiara superfluo verificare il driver. Attribuisce alla propria risposta 9/10 perché ha citato tre authority. Correggi elaborato e autovalutazione.

**Soluzione.** Novantuno euro deriva dall'imputazione integrale non giustificata dei costi comuni. Nelle ipotesi, il riparto 60/40 dà 180.000/120.000, costi regolati 680.000, ricavo 790.000 e tariffa 79 euro. La causalità e la documentazione del driver restano indispensabili anche con aritmetica esatta. La traccia riguarda ammissibilità tariffaria: non offre mercato rilevante, dominanza e condotta abusiva per concludere su articolo 102 TFUE. La proposta è verificare contabilità, driver e metodo del regolatore competente, correggere l'imputazione se confermata e motivare la determinazione; una sanzione richiede fattispecie e procedimento propri. La rubrica non premia il numero di sigle: falliscono metodo del dato, qualificazione, competenza e conclusione. Si ripassano capitoli 7–9, poi si riscrive entro 350 parole e si controllano separatamente calcolo e fondamento giuridico.

**Autovalutazione:** un punto per calcolo, uno per driver, uno per assenza dei presupposti dell'abuso, uno per rubrica applicata senza autocompiacimento.

**Riferimenti per il ripasso.** Le dieci simulazioni applicano le fonti illustrate nei capitoli 4–14: Codice del consumo, GDPR e Codice privacy, D.Lgs. 24/2023, DSA, MiFID/TUF, disciplina prudenziale e ADR. Per la teoria comune, usa il VOL-01 nelle sezioni sul procedimento e sulle prove: la mappa e le destinazioni puntuali sono indicate nel capitolo 1 di questo volume. Dati quantitativi e dossier sono originali didattici, non dati osservati di operatori reali. Regole verificate al 3 ottobre 2026.
'''
notes=['vol-05-garante-procedimenti-verifica-2026-10-03','vol-05-anac-whistleblowing-verifica-2026-10-03','vol-05-consob-verifica-2026-10-03','vol-05-banca-ivass-verifica-2026-10-03']
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ['+', '.join('"sources/'+n+'.md"' for n in notes)+', ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/topics/authority-rettifiche-2026.md", ',1)
memo=re.search(r'\*\*Model memo \(108 words\)\.\*\* (.*?)\n',s).group(1);count=len(memo.split());s=s.replace('Model memo (108 words)','Model memo ('+str(count)+' words)');p.write_text(s,encoding='utf8')
(O/'VOL-05-simulations-verification.json').write_text(json.dumps({'count':10,'readOriginalComplete':True,'solutionsApplied':list(data),'englishWordCount':count,'calculations':{'E1':[14,26,14],'E2':[6000,7000,-5000],'E3':{'regulatedCommon':180000,'nonRegulatedCommon':120000,'regulatedOperating':680000,'totalRevenue':790000,'tariff':79,'incorrectTariff':91,'difference':12},'P3SCR':.9},'legalSources':'Sources consolidated for chapters 4–14; dates and conditions embedded in each dossier.'},ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,16));d['chaptersReadThisCycle']=list(range(1,16));d['findingsFullyApplied']+=['V05-02','V05-28','V05-30','V05-31','V05-32'];d['findingsPartiallyApplied'].pop('V05-02',None);d['findingsPartiallyApplied'].pop('V05-28',None);d['pending'][0]='Matrice, indici, pulizia, audit e freeze';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][14]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Applied chapter 15; English words:',count)
