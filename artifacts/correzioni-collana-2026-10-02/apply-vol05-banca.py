from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02');note='vol-05-banca-ivass-verifica-2026-10-03'
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## Banche, assicurazioni e rimedi\n\n[[sources/'+note+']] consolida SSM, capitale/liquidità, SREP, crisi, SCR/MCR/ORSA, confronto ADR e transitorio AAS. Introduce il nucleo minimo privatistico, societario e AML promesso dal percorso di studio, con articoli correnti letti.\n',encoding='utf8')
p=B/'chapters/12-banca-italia-ivass-vigilanza-prudenziale.md';s=p.read_text(encoding='utf8')
s=s.replace("### Banca d'Italia: banche, intermediari, stabilità e clientela\n\n## N-MF05-12-02 · Istituti e distinzioni", "## N-MF05-12-02 · Istituti e distinzioni\n\n### Banca d'Italia: banche, intermediari, stabilità e clientela").replace('### Dati, reclami e poteri: dal segnale all\'intervento\n\n## N-MF05-12-03 · Poteri, procedura e conseguenze','## N-MF05-12-03 · Poteri, procedura e conseguenze\n\n### Dati, reclami e poteri: dal segnale all\'intervento')
a=s.index('La qualificazione dipende dai criteri');b=s.index('### Pagamenti, ABF',a)
s=s[:a]+'''Il riferimento è il **regolamento UE 1024/2013**, con il quadro 468/2014. Fra i criteri di significatività rientrano attivi **oltre 30 miliardi di euro**, importanza per l'economia nazionale o dell'Unione, rilevanza transfrontaliera e assistenza finanziaria diretta ESM/EFSF. Il criterio attivi/PIL nazionale considera un rapporto oltre il **20%**, salvo attivi inferiori a **5 miliardi**; il criterio transfrontaliero considera attivi oltre 5 miliardi e rapporti transfrontalieri oltre il 20% secondo le regole del quadro. Sono inoltre vigilate direttamente almeno le tre banche più significative di ciascuno Stato partecipante, salve le condizioni previste. Non occorre cumulare tutti i criteri, e resta possibile l'assunzione della vigilanza diretta per garantire standard coerenti. Nel caso concreto si controlla l'elenco BCE aggiornato.

**Le procedure comuni non seguono la semplice distinzione SI/LSI.** Rilascio e revoca dell'autorizzazione bancaria e acquisizione di partecipazioni qualificate coinvolgono BCE e autorità nazionale anche per enti meno significativi. La domanda entra presso l'autorità nazionale; la decisione conclusiva di competenza è BCE secondo la procedura. «Banca piccola, quindi ogni decisione è della Banca d'Italia» è una risposta errata. La vigilanza prudenziale europea non assorbe automaticamente la tutela contrattuale del cliente né la funzione antiriciclaggio.

### TUB, CRR e CRD: che cosa si misura

Il **TUB è il D.Lgs. 385/1993**; l'articolo 5 collega i poteri a sana e prudente gestione, stabilità, efficienza, competitività e osservanza delle regole. Il **CRR, regolamento UE 575/2013**, stabilisce requisiti prudenziali direttamente applicabili; la **CRD, direttiva 2013/36/UE**, disciplina fra l'altro accesso, governance e supervisione, con attuazione nazionale. Si studiano nelle versioni aggiornate, senza ridurre il sistema alla sola etichetta «Basilea».

| Concetto | Significato operativo |
| --- | --- |
| Fondi propri | Risorse ammissibili ad assorbire perdite; CET1, capitale primario di classe 1, è la componente di qualità più elevata. Non coincide con il saldo di cassa. |
| Attività/esposizioni ponderate per il rischio | Base regolamentare che riflette il rischio; non coincide con l'attivo contabile totale. |
| Minimi dell'articolo 92 CRR | CET1 4,5%, Tier 1 6%, fondi propri totali 8% sull'esposizione complessiva al rischio; sono minimi di primo pilastro, cui si aggiungono riserve e requisiti pertinenti. La leva usa invece una diversa base di esposizione. |
| LCR | Attività liquide di qualità elevata rispetto ai deflussi netti in uno scenario di stress di 30 giorni. Misura resistenza di breve periodo. |
| NSFR | Finanziamento stabile disponibile rispetto a quello richiesto su orizzonte di un anno. Affronta la sostenibilità della struttura di raccolta. |

**Calcolo didattico.** CET1 di 9 milioni ed esposizioni ponderate di 100 milioni danno un CET1 ratio del **9%**. Superare il 4,5% non dimostra il rispetto di ogni requisito complessivo: servono riserve, secondo pilastro e gli altri vincoli. Se attività liquide ammissibili e deflussi netti già calcolati secondo il metodo sono 12 e 10 milioni, LCR = **120%**; dopo una riduzione delle attività a 9 milioni, a parità di deflussi, è **90%**. Non si conclude che capitale e liquidità siano intercambiabili né si inventano i coefficienti con cui i deflussi sono stati determinati.

Lo **SREP** valuta quattro aree: sostenibilità del modello di attività, governance/gestione dei rischi, rischi per il capitale, rischi di liquidità e raccolta. Considera anche le valutazioni interne ICAAP e ILAAP e può condurre a misure quantitative o qualitative. Un incremento patrimoniale non elimina da solo una carenza grave nei controlli; una banca con patrimonio positivo può non disporre di cassa sufficiente per le scadenze imminenti.

### Crisi: risoluzione e liquidazione

La **risoluzione** non scatta a ogni perdita trimestrale. Richiede dissesto o rischio di dissesto, assenza di alternative ragionevoli capaci di evitarlo nei tempi pertinenti e interesse pubblico secondo la disciplina. Gli strumenti comprendono cessione, ente ponte, separazione di attività e bail-in alle condizioni previste. Il **Meccanismo di risoluzione unico** e Banca d'Italia quale autorità nazionale operano secondo i rispettivi compiti: vigilanza corrente e gestione della crisi restano funzioni distinte.

Se manca l'interesse pubblico alla risoluzione e ricorrono gli altri presupposti, opera la **liquidazione coatta amministrativa** del TUB, che conduce all'uscita dal mercato anche attraverso cessioni di attività/passività. Il bail-in assorbe perdite e ricapitalizza secondo gerarchia ed esclusioni; non è un prelievo indiscriminato su tutti i conti. I depositi protetti fino a **100.000 euro per depositante e banca**, e i maggiori importi nei casi speciali previsti, seguono la tutela di legge; titoli azionari o obbligazionari della banca non sono depositi garantiti.

'''+s[b:]
a=s.index('Solvency II organizza');b=s.index('DORA, applicabile',a)
s=s[:a]+'''**Solvency II**, direttiva 2009/138/CE attuata nel Codice delle assicurazioni private, D.Lgs. 209/2005, articola tre pilastri: requisiti quantitativi; governance e gestione dei rischi; informativa al supervisore e al pubblico. Il secondo include l'**ORSA**, valutazione interna prospettica di rischio e solvibilità integrata nelle decisioni dell'impresa; il terzo rende conoscibile la posizione attraverso reporting e disclosure. Non si riduce tutto al primo rapporto patrimoniale disponibile.

Il **SCR (Solvency Capital Requirement)** è il requisito patrimoniale di solvibilità sensibile ai rischi, calcolato con formula standard o modello interno autorizzato; il **MCR (Minimum Capital Requirement)** è il requisito minimo, la cui violazione attiva un livello più urgente di intervento. L'ORSA non è un terzo requisito fisso né una relazione con cui l'impresa si esonera dal controllo IVASS. Le riserve tecniche rappresentano invece obbligazioni assicurative valutate secondo le regole: non sono sinonimo di fondi propri.

**Esempio.** Fondi propri ammissibili per SCR pari a 150 milioni e SCR pari a 100 danno copertura **150%**. Se, dopo uno shock, i fondi scendono a 90 e il requisito resta 100, la copertura è **90%**: emerge un deficit SCR. Anche se il distinto MCR di 40 fosse coperto da fondi ammissibili sufficienti, ciò non cancellerebbe il deficit SCR. Nell'ORSA si valutano anche evoluzione del portafoglio, rischi e fabbisogno futuro; la verifica di un numero a una sola data non basta. I valori sono didattici, non coefficienti normativi.

'''+s[b:]
a=s.index('### Arbitro Assicurativo operativo');b=s.index('### Mappa BANDO',a)
s=s[:a]+'''### ABF, ACF e Arbitro Assicurativo: scegliere il percorso

Il soggetto commerciale «banca» non decide da solo l'ADR: un conto, una raccomandazione di investimento e una polizza distribuita allo sportello sollevano materie differenti. Il confronto è verificato al **3 ottobre 2026**.

| Sistema | Materia e limiti economici | Reclamo e accesso |
| --- | --- | --- |
| ABF | Operazioni e servizi bancari/finanziari, inclusi pagamenti; fino a 200.000 euro per richieste pecuniarie, senza tetto per mero accertamento. | Reclamo: risposta insoddisfacente o decorso del termine, ordinariamente 60 giorni; pagamenti 15 lavorativi, salve le disposizioni speciali. Ricorso entro 12 mesi, possibile nuovo reclamo; fatti non anteriori a sei anni dal ricorso. |
| ACF | Investitori retail: obblighi nei servizi di investimento/gestione collettiva; fino a 500.000 euro. | Reclamo insoddisfacente o senza risposta in 60 giorni; ricorso entro un anno, operazioni/condotte entro il decennio precedente. Si controlla anche l'assenza di altra ADR sugli stessi fatti. |
| AAS | Controversie da contratto assicurativo concluso: 300.000 euro per prestazioni esclusivamente in caso di decesso, 150.000 per altre vita, 25.000 danni; 2.500 per danneggiato con azione diretta. Nessun tetto per mero accertamento. | Reclamo a impresa/intermediario insoddisfacente o senza risposta in 45 giorni; regola ordinaria entro 12 mesi dal primo reclamo, non riattivabile ripetendolo. Fatti o loro conoscenza nei tre anni prima del reclamo. |

**Attenzione al primo anno AAS.** L'operatività è iniziata il **15 gennaio 2026**. Nel primo anno, sino al 15 gennaio 2027, la disciplina transitoria ammette reclami presentati **dal 15 gennaio 2025**: il termine ordinario non va applicato cancellando questa previsione. La segnalazione inviata solo a IVASS non sostituisce il reclamo all'impresa o all'intermediario.

ABF e AAS richiedono un contributo di **20 euro**, restituito nei casi di accoglimento previsti; ACF è gratuito. I tre sistemi decidono controversie, non sanzioni di vigilanza, e le loro decisioni non hanno la forza esecutiva di una sentenza; resta il giudice, mentre l'inadempimento è pubblicizzato. Ulteriori condizioni, incluse pendenze e categorie escluse, vanno controllate sul sistema pertinente.

Per AAS, l'istruttoria dura fino a **90 giorni**, seguita dalla decisione nei successivi **90**, prorogabili fino a ulteriori **90** per particolare complessità: il dato sintetico «180 + 90» va letto con questa scansione. Si decide su documenti; non si dispongono nuove perizie tecniche d'ufficio né testimonianze. Polizza, reclamo, risposta e documenti del sinistro sono quindi decisivi.

### Basi di diritto privato, commerciale e antiriciclaggio

Quando il bando comprende queste materie, il punto di partenza è distinguere **validità del contratto, inadempimento e vigilanza**. Il contratto richiede accordo, causa, oggetto e la forma prescritta a pena di nullità (articolo 1325 c.c.). La nullità riguarda i presupposti dell'articolo 1418, inclusa la contrarietà a norme imperative salvo diversa previsione; annullabilità per incapacità o vizi del consenso segue gli articoli 1425–1427 e le condizioni successive. Un investimento in perdita non dimostra da solo né nullità né annullabilità. L'inadempimento riguarda invece la mancata esatta prestazione: l'articolo 1218 pone la responsabilità risarcitoria salvo prova dell'impossibilità derivante da causa non imputabile. La sanzione dell'autorità non sostituisce l'accertamento della domanda civile.

Nella **società per azioni**, patrimonio sociale e patrimonio dei soci sono distinti: per le obbligazioni risponde la società, salve le specifiche eccezioni dell'articolo 2325, anche per il socio unico. Lo statuto sceglie fra i sistemi di amministrazione e controllo dell'articolo 2380: amministratori e collegio sindacale; consiglio di gestione e sorveglianza; consiglio di amministrazione e comitato interno per il controllo sulla gestione. Gli amministratori devono la diligenza dell'incarico e delle proprie competenze; deleghe e controlli non eliminano ogni responsabilità per fatti pregiudizievoli conosciuti (articolo 2392). Nelle imprese vigilate si aggiungono requisiti settoriali: il solo schema civilistico non esaurisce governance e idoneità degli esponenti.

L'**antiriciclaggio**, D.Lgs. 231/2007, impone un processo distinto dalla profilatura MiFID: identificazione e verifica di cliente, esecutore e **titolare effettivo**; scopo e natura del rapporto; controllo costante proporzionato al rischio. Una società cliente può avere un rappresentante firmatario diverso dalla persona fisica titolare effettiva: registrare soltanto il primo non risolve la verifica. La documentazione si conserva per **dieci anni** dalla cessazione del rapporto/prestazione o dall'operazione occasionale secondo l'articolo 31.

Se emergono conoscenza, sospetto o ragionevoli motivi di sospetto nei termini dell'articolo 35, il soggetto obbligato invia una **SOS alla UIF senza ritardo**, di regola prima dell'operazione, ferme le eccezioni previste. Non occorre già provare il reato; non basta però un automatismo privo di elementi. La SOS non coincide con la denuncia penale e non la sostituisce. L'articolo 39 vieta di informare cliente o terzi della segnalazione fuori dalle eccezioni: non si chiede al cliente di «autorizzare» la SOS. Banca d'Italia esercita i propri controlli AML, la UIF analizza i flussi segnaletici e coopera con gli organi competenti.

Queste basi permettono di risolvere i casi qui proposti. Se il bando richiede diritto societario o civile esteso, il percorso va completato sugli istituti elencati dal programma: fusioni, procedure concorsuali e singoli contratti non si esauriscono in questa sintesi.

## N-MF05-12-04 · Applicazione alla prova

'''+s[b:]
a=s.index('## N-MF05-12-05');s=s[:a]+'''## N-MF05-12-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Una banca è meno significativa. La BCE è estranea alla sua autorizzazione?

**Risposta corretta:** no. L'autorizzazione bancaria è una procedura comune anche per le LSI: autorità nazionale e BCE cooperano, con decisione conclusiva BCE. La vigilanza diretta ordinaria nazionale non equivale a competenza esclusiva su ogni atto.

**Quesito 2.** CET1 di 8 milioni su esposizioni ponderate di 100 milioni prova che ogni requisito prudenziale è rispettato?

**Risposta corretta:** il rapporto è 8%, ma la conclusione è prematura. Vanno verificati riserve, secondo pilastro, qualità degli altri fondi e vincoli di liquidità/leva. Il minimo CET1 di primo pilastro non è il requisito complessivo di ogni banca.

**Quesito 3.** Fondi ammissibili SCR pari a 90 e SCR pari a 100: la copertura di un MCR di 40 cancella la criticità?

**Risposta corretta:** no. La copertura SCR è 90%, dunque insufficiente. SCR e MCR hanno funzioni e conseguenze distinte; verificare anche l'ammissibilità dei fondi per ciascun requisito.

**Quesito 4.** A ottobre 2026 un beneficiario di polizza temporanea esclusivamente caso morte chiede 200.000 euro, dopo reclamo insoddisfacente del febbraio 2025. Valore e data escludono senz'altro l'AAS?

**Risposta corretta:** no. Per questa polizza il limite è 300.000 euro e nel primo anno il transitorio ammette reclami dal 15 gennaio 2025. Restano tutti gli altri presupposti, inclusi materia, fatti, documentazione e pendenze; non si applica meccanicamente il termine annuale ordinario.

**Quesito 5.** Un danneggiato con azione diretta chiede ancora 4.000 euro all'assicurazione: basta invocare il limite generale danni di 25.000 euro?

**Risposta corretta:** no. Per il danneggiato con azione diretta il limite AAS è 2.500 euro; la categoria specifica prevale sul richiamo generico al ramo danni. Si valutano gli altri percorsi di tutela.

**Quesito 6.** L'operazione non supera una soglia monetaria e non c'è già una prova penale. È esclusa una SOS?

**Risposta corretta:** no. L'articolo 35 guarda agli elementi del sospetto, indipendentemente dall'entità dei fondi. Occorre una valutazione motivata, non la prova completa del reato; la comunicazione al cliente della SOS è vietata fuori dalle eccezioni normative.

### Caso ragionato di chiusura

**Traccia.** Una banca meno significativa registra un CET1 ratio dell'8% e un LCR dell'85%; distribuisce inoltre una polizza danni per la quale il cliente contesta un diniego di 12.000 euro. Il reclamo alla compagnia è del 1° settembre 2026 e il diniego definitivo del 20 settembre. Il 3 ottobre chiede all'ABF di sanzionare la compagnia e alla BCE di garantire il capitale investito. Imposta i percorsi.

**Soluzione.** La LSI è vigilata direttamente dall'autorità nazionale nel quadro SSM; capitale e liquidità sono distinti e l'8% CET1 non chiude la valutazione prudenziale. LCR all'85% richiede analisi e interventi secondo la disciplina, senza dedurne automaticamente risoluzione o insolvenza. Per la polizza danni, si esaminano garanzia, esclusioni, documenti della distribuzione e sinistro. La domanda di 12.000 euro è entro la soglia AAS danni, salvo che si tratti della diversa azione diretta del danneggiato: il caso riguarda il contraente. Il diniego consente il ricorso senza attendere inutilmente 45 giorni, verificati gli altri presupposti. ABF non diventa competente per la sola distribuzione bancaria della polizza e non sanziona la compagnia. Un esposto IVASS può alimentare vigilanza sulla condotta; l'AAS tratta la controversia documentale. Nessuna vigilanza BCE garantisce il rendimento di un investimento.

**Autovalutazione:** un punto per SSM, uno per capitale/liquidità, uno per scelta e accesso AAS, uno per separazione vigilanza/rimedio.

**Riferimenti normativi e professionali.** TUB, D.Lgs. 385/1993, articoli 5, 53, 67, 80 e 128-bis; regolamenti UE 1024/2013, 468/2014 e CRR 575/2013, articolo 92; CRD 2013/36/UE; BRRD 2014/59/UE, D.Lgs. 180–181/2015; Codice delle assicurazioni, D.Lgs. 209/2005, e Solvency II 2009/138/CE; DORA 2022/2554 e D.Lgs. 23/2025; DM 215/2024 sull'AAS; codice civile, articoli 1218, 1325, 1418, 1425–1427, 2325, 2380, 2392; D.Lgs. 231/2007, articoli 18, 31, 35, 39. [ABF, verifiche preliminari](https://www.arbitrobancariofinanziario.it/presentare-ricorso/verifiche-preliminari/index.html); [AAS, FAQ](https://www.arbitroassicurativo.org/faq/index.html). Verifica al 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/'+note+'.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/'+note+'.md", "wiki/topics/authority-rettifiche-2026.md", ',1);p.write_text(s,encoding='utf8')
p=Path('wiki/sources/vol-05-aggiornamento-specialistico-2026-08-22.md');s=p.read_text(encoding='utf8').replace('2025/03/11/25G00031/sg','2025/03/11/25G00032/sg');p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,13));d['chaptersReadThisCycle']=list(range(1,13));d['findingsFullyApplied']+=['V05-22','V05-23'];d['findingsPartiallyApplied'].pop('V05-22',None);d['findingsPartiallyApplied']['V05-02']='Capitoli 1–12: 72 quesiti e 12 casi specifici';d['pending'][0]='Fonti e integrazioni capitoli 13–15';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][11]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'norme-vol05/private-manifest.json';d=json.loads(f.read_text(encoding='utf8'))
for r in d:r['readComplete']=True
f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Applied chapter 12.')
