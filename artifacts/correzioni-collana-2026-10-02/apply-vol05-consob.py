from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02');note='vol-05-consob-verifica-2026-10-03'
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## CONSOB e investimenti\n\n[[sources/'+note+']] distingue i tre test sul cliente e le conseguenze; integra prospetto, OPA aggiornata al D.Lgs. 47/2026, MAR dopo il 5 giugno 2026, riparto MiCAR e fine transitorio, condizioni ACF. Il transitorio TUF sanzionatorio resta nella nota dedicata.\n',encoding='utf8')
p=B/'chapters/11-consob-mercati-intermediari-tutela-investitore.md';s=p.read_text(encoding='utf8')
s=s.replace("### Intermediari e tutela dell'investitore: correttezza non significa rendimento garantito\n\n## N-MF05-11-02 · Istituti e distinzioni", "## N-MF05-11-02 · Istituti e distinzioni\n\n### Intermediari e tutela dell'investitore: correttezza non significa rendimento garantito")
s=s.replace('### Poteri, cooperazione e tutela stragiudiziale\n\n## N-MF05-11-03 · Poteri, procedura e conseguenze','## N-MF05-11-03 · Poteri, procedura e conseguenze\n\n### Poteri, cooperazione e tutela stragiudiziale')
a=s.index('MiFID II e MiFIR costituiscono');b=s.index('La firma di un documento',a)
s=s[:a]+'''La direttiva **MiFID II, 2014/65/UE**, e il regolamento **MiFIR, 600/2014**, hanno funzioni collegate: servizi, organizzazione e condotta da un lato; regole direttamente applicabili su mercati, trasparenza e negoziazione dall'altro. Il TUF, D.Lgs. 58/1998, e il regolamento intermediari CONSOB 20307/2018 completano il quadro nazionale. L'articolo 5 TUF attribuisce a Banca d'Italia contenimento del rischio, stabilità e sana e prudente gestione; alla CONSOB trasparenza e correttezza. La stessa banca può quindi essere vigilata per differenti finalità.

| Test | Servizio e informazioni | Conseguenza operativa |
| --- | --- | --- |
| Adeguatezza | Consulenza e gestione di portafogli: conoscenza/esperienza, situazione finanziaria e capacità di sostenere perdite, obiettivi e tolleranza al rischio; anche preferenze di sostenibilità nel quadro applicabile. | Senza informazioni necessarie non si raccomanda il servizio/strumento; non si raccomanda o esegue in gestione un investimento inadeguato. Nella consulenza retail si documenta perché la raccomandazione è adeguata. |
| Appropriatezza | Altri servizi: conoscenza ed esperienza sullo specifico prodotto/servizio. Non è una completa valutazione patrimoniale degli obiettivi. | Esito negativo: avvertire il cliente. Dati mancanti: avvertire dell'impossibilità di valutare. L'avvertenza non equivale al divieto automatico proprio della raccomandazione inadeguata. |
| Mera esecuzione, o execution only | Esecuzione/ricezione di ordini nelle condizioni cumulative dell'articolo 43: strumenti non complessi ammessi, iniziativa del cliente, chiara avvertenza sulla mancata valutazione, rispetto dei conflitti. | È possibile non svolgere il test di appropriatezza; restano gli altri obblighi. Un derivato complesso non diventa execution only perché comprato autonomamente online. |

**Conflitti, incentivi e miglior risultato.** L'intermediario deve identificare, prevenire e gestire i conflitti; una generica firma del cliente non sostituisce i presidi organizzativi. Per incentivi da terzi, fuori dai regimi più restrittivi, occorrono miglioramento della qualità, rispetto del migliore interesse e informativa: non basta dichiarare la commissione. Nella consulenza indipendente e nella gestione di portafogli i compensi monetari di terzi non possono essere trattenuti; vanno trasferiti integralmente al cliente. Restano ammissibili soltanto i benefici non monetari minori alle condizioni previste.

La **best execution** considera prezzo, costi, rapidità, probabilità di esecuzione e regolamento, dimensione e natura dell'ordine. Per il retail il riferimento è il corrispettivo totale, prezzo più costi, con le precisazioni della disciplina. Se due sedi offrono un titolo a 100 e 99,90 ma costi rispettivamente di 0,10 e 0,40, a parità degli altri fattori la prima costa 100,10 e la seconda 100,30: il prezzo nominale più basso non basta. La verifica riguarda misure e strategia efficaci; non garantisce il rendimento né il miglior prezzo osservabile a posteriori in ogni istante.

'''+s[b:]
a=s.index('### Mercati integri: MAR')
s=s[:a]+'''### Prospetto e OPA: informare e proteggere il disinvestimento

Il **prospetto**, nel regolamento UE 2017/1129 e nell'articolo 94 TUF, consente di valutare emittente, titoli e rischi nelle offerte/ammissioni soggette all'obbligo. L'approvazione CONSOB verifica completezza, coerenza e comprensibilità; non certifica la convenienza o l'assenza di rischio. Occorre distinguere obbligo, esenzioni e pubblicità: un messaggio commerciale non sostituisce il prospetto quando dovuto.

L'**OPA obbligatoria** tutela i titolari dei titoli quando si supera una soglia rilevante: non è un'offerta di nuova sottoscrizione. Nel testo dell'articolo 106 TUF modificato dal **D.Lgs. 47/2026**, vigente dal 29 aprile 2026, la regola generale considera una partecipazione **superiore al 30%**, o diritti di voto superiori al 30% a seguito di acquisti o maggiorazione, secondo la disciplina. L'offerta totalitaria è promossa entro **20 giorni** e, per ciascuna categoria, a un prezzo non inferiore al massimo pagato nei **sei mesi** precedenti dall'offerente o da chi agisce di concerto; in assenza di acquisti onerosi si applica il criterio della media ponderata previsto dalla norma. Eccezioni e fattispecie particolari richiedono verifica specifica. I vecchi riferimenti al 25% per determinate società e ai dodici mesi non descrivono questa versione dell'articolo.

**Esempio.** Un soggetto passa dal 28% al 31% dei diritti rilevanti di una quotata italiana e non emerge alcuna esenzione. Va verificata l'OPA, non semplicemente un'informativa di marketing; per determinare il prezzo servono acquisti propri e di concerto nel periodo pertinente. Il prospetto di un'altra operazione non assolve l'obbligo di offerta.

'''+s[a:]
a=s.index('L’**informazione privilegiata**') if 'L’**informazione privilegiata**' in s else s.index("L'**informazione privilegiata**")
b=s.index('| Ipotesi |',a)
s=s[:a]+'''L'**informazione privilegiata**, ai sensi dell'articolo 7 MAR, è precisa, non pubblica, riguarda direttamente o indirettamente uno o più emittenti o strumenti e, se resa pubblica, potrebbe incidere in modo significativo sui prezzi: conta l'informazione che un investitore ragionevole userebbe nelle proprie decisioni. Una vaga indiscrezione non è automaticamente precisa; anche una tappa intermedia può però soddisfare i requisiti. La manipolazione richiede invece di verificare operazioni, ordini o informazioni capaci di produrre segnali falsi o fuorvianti o un prezzo artificiale, secondo le fattispecie applicabili.

Dal **5 giugno 2026**, dopo il regolamento UE **2024/2809**, l'articolo 17 distingue la qualifica dell'informazione dall'obbligo di comunicarla: nei **processi prolungati** le tappe intermedie collegate all'evento finale non sono di per sé soggette a pubblicazione; vanno comunicate quanto prima le circostanze o l'evento finali. Restano riservatezza e divieti di abuso: non pubblicare ancora non significa poter negoziare sfruttando l'informazione. Se la riservatezza viene meno, anche attraverso voci sufficientemente accurate, la comunicazione va effettuata quanto prima ai sensi del paragrafo 7.

Il **ritardo della comunicazione** di un'informazione altrimenti da pubblicare è distinto: richiede cumulativamente probabile pregiudizio ai legittimi interessi, assenza di contrasto con le ultime informazioni o altre comunicazioni dell'emittente sulla stessa questione e capacità di mantenere la riservatezza. Richiede inoltre gli adempimenti verso l'autorità competente. Il vecchio richiamo al solo «non fuorviare il pubblico» non riproduce il testo vigente; la mancata pubblicazione della tappa intermedia non è, da sola, una decisione di ritardo del paragrafo 4.

'''+s[b:]
a=s.index('### MiCAR e riparto nazionale');b=s.index('### Mappa BANDO',a)
s=s[:a]+'''### MiCAR: token, soggetto e attività prima della competenza

Il regolamento **UE 2023/1114 (MiCAR)** si applica integralmente dal 30 dicembre 2024, con avvio anticipato delle disposizioni sui token stabili. Il **D.Lgs. 129/2024** attua il riparto nazionale. Uno strumento finanziario rappresentato digitalmente non esce dal TUF solo perché chiamato token.

| Oggetto | Regola e autorità da distinguere |
| --- | --- |
| ART, token collegato ad attività | Mira a mantenere valore stabile riferendosi ad altri valori/diritti o loro combinazioni. Autorizzazione dell'emittente specializzato da Banca d'Italia **d'intesa con CONSOB**; vigilanza prudenziale BI e condotta CONSOB. Restano i regimi per intermediari già vigilati e ART significativi sotto EBA. |
| EMT, token di moneta elettronica | Stabilità riferita a una sola valuta ufficiale; emissione riservata a banche e IMEL. Notifica alla BI, senza approvazione preventiva del white paper; BI vigila anche sulla condotta dell'emittente verso i possessori, ferme competenze EBA sui significativi. |
| Altre cripto-attività | Nei casi soggetti al regime, notifica del white paper alla CONSOB, senza formale approvazione. Non è un'autorizzazione generale dell'investimento né una garanzia sul valore. |
| CASP specializzato | Autorizzazione CONSOB **sentita Banca d'Italia**; condotta, mercati e clienti alla CONSOB, profili prudenziali alla BI. Per intermediari già vigilati l'articolo 60 permette servizi notificabili secondo soggetto e attività. |

La differenza tra **intesa** e **parere** non è terminologica: l'autorizzazione dell'emittente ART e quella del CASP specializzato non seguono lo stesso riparto. Anche la custodia di EMT da parte di un CASP è un servizio distinto dall'emissione di EMT: non si trasferisce alla BI ogni controllo di condotta sul servizio solo per il tipo di token custodito.

Al **3 ottobre 2026** il periodo transitorio dei precedenti operatori è concluso: dal **1° luglio 2026** la sola iscrizione OAM non abilita a continuare i servizi MiCAR. Occorre il titolo del regime europeo, mantenendo la distinzione fra autorizzazione CASP e notifica ammessa per specifici intermediari. La promessa «siamo iscritti, quindi ogni servizio è autorizzato» va verificata su registro, attività e titolo effettivo.

### ACF: dalla condotta al rimedio individuale

L'ACF riguarda controversie fra **investitori retail e intermediari** sugli obblighi nei servizi di investimento o nella gestione collettiva, entro il suo ambito. La richiesta non può superare **500.000 euro**. Occorre un previo reclamo sui medesimi fatti, con risposta insoddisfacente oppure senza risposta nei **60 giorni**; il ricorso va presentato entro **un anno dal reclamo**. Le operazioni o condotte devono rientrare nel decennio precedente il ricorso e non deve pendere altra procedura stragiudiziale sugli stessi fatti. Non si applica il perimetro ACF a qualsiasi controversia denominata finanziaria: conto corrente e mutuo appartengono ordinariamente all'ABF.

Il ricorso ACF è **gratuito**; non occorre presumere un risarcimento dalla sola perdita di borsa. Servono obbligo violato, documenti, danno e nesso pertinenti alla domanda. La decisione non è un titolo esecutivo giudiziale; l'inadempimento viene reso pubblico secondo la disciplina e resta accessibile il giudice. Vigilanza CONSOB, sanzione, ACF e azione civile perseguono funzioni diverse. Il capitolo 12 confronta questo percorso con ABF e Arbitro Assicurativo.

'''+s[b:]
a=s.index('## N-MF05-11-05');s=s[:a]+'''## N-MF05-11-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Un cliente non comunica reddito, patrimonio e obiettivi. Il consulente può raccomandargli un derivato complesso purché firmi un'avvertenza?

**Risposta corretta:** no. Mancano informazioni necessarie all'adeguatezza nella consulenza. L'avvertenza prevista quando non si può valutare l'appropriatezza in un altro servizio non sostituisce il test richiesto; neppure il canale online rende il derivato execution only.

**Quesito 2.** Nell'esecuzione non consigliata, un prodotto risulta non appropriato. La conseguenza è identica a una raccomandazione inadeguata?

**Risposta corretta:** no. L'appropriatezza negativa comporta l'avvertenza al cliente; la raccomandazione inadeguata non può essere resa. Restano da rispettare le altre regole applicabili, senza inventare una generale libertà da obblighi dopo la firma.

**Quesito 3.** Nell'ottobre 2026 una partecipazione rilevante passa dal 28% al 31%, senza esenzioni. Quali numeri base dell'OPA vanno ricordati?

**Risposta corretta:** soglia generale superiore al 30%, promozione entro 20 giorni, confronto del prezzo con il massimo pagato nei sei mesi precedenti secondo l'articolo 106. Non si applicano automaticamente il vecchio 25% o i dodici mesi; vanno verificati diritti di voto, concerto e disciplina del caso.

**Quesito 4.** Una tappa intermedia di una negoziazione complessa soddisfa l'articolo 7 MAR. Dal 5 giugno 2026 l'assenza di pubblicazione consente di negoziare sfruttandola?

**Risposta corretta:** no. La deroga all'obbligo di comunicare la tappa intermedia non elimina la natura privilegiata né i divieti di abuso. Occorre mantenerne la riservatezza; se viene meno, si applica la comunicazione tempestiva dell'articolo 17, paragrafo 7.

**Quesito 5.** Un CASP specializzato sostiene che l'iscrizione OAM gli consenta ancora di operare in ottobre 2026 senza titolo MiCAR. È sufficiente?

**Risposta corretta:** no. Il transitorio è terminato; per il CASP specializzato serve l'autorizzazione CONSOB sentita BI. La notifica dell'articolo 60 riguarda specifici intermediari già vigilati e servizi consentiti, non ogni operatore OAM.

**Quesito 6.** Un investitore retail chiede 600.000 euro all'ACF dopo un reclamo insoddisfacente. Il reclamo rende ammissibile la domanda?

**Risposta corretta:** no. Oltre al reclamo occorrono gli altri presupposti, incluso il limite di 500.000 euro. Il superamento del limite ACF non estingue l'eventuale diritto da far valere in giudizio.

### Caso ragionato di chiusura

**Traccia.** A ottobre 2026 una banca consiglia a una cliente un titolo subordinato destinandovi il 70% del patrimonio. Il dossier contiene solo un questionario sulle conoscenze, senza capacità di perdita e obiettivi; è presente una firma «operazione non appropriata». La cliente perde 40.000 euro, presenta reclamo e riceve risposta negativa. Chiede alla CONSOB di sanzionare la banca e ordinarle il rimborso tramite ACF. Quali passaggi sono corretti?

**Soluzione.** La raccomandazione impone adeguatezza, non il solo test di conoscenze/esperienza. Si acquisiscono contratto, profilatura, dichiarazione di adeguatezza, caratteristiche e rischi del titolo, costi/incentivi, comunicazioni e ordine. La firma sull'appropriatezza non sana la carenza. La concentrazione è un elemento rilevante ma non sostituisce l'analisi del cliente e del prodotto. Per la domanda ACF, 40.000 euro rientrano nel limite; risposta negativa permette di procedere senza attendere inutilmente 60 giorni, verificando termine annuale, perimetro e assenza di altra ADR. Vanno argomentati violazione, danno e nesso, non soltanto la perdita. La segnalazione alla CONSOB può alimentare vigilanza e procedimento sanzionatorio; l'ACF decide la distinta controversia individuale e non irroga la sanzione amministrativa. La banca resta inoltre soggetta ai controlli prudenziali BI per le rispettive finalità.

**Autovalutazione:** un punto per il test corretto, uno per i documenti, uno per l'accesso ACF, uno per la separazione fra sanzione e rimedio individuale.

**Riferimenti normativi e professionali.** TUF, D.Lgs. 58/1998, articoli 5, 21, 94 e 106, aggiornato dal D.Lgs. 47/2026; MiFID II, direttiva 2014/65/UE; MiFIR, regolamento UE 600/2014; regolamento delegato UE 2017/565, articoli 54–55; regolamento intermediari CONSOB 20307/2018, articoli 40–54; MAR, regolamento UE 596/2014, articoli 7 e 17, modificato dal regolamento UE 2024/2809; MiCAR, regolamento UE 2023/1114 e D.Lgs. 129/2024; regolamento ACF 19602/2016, modificato dalla delibera 21867/2021. [ACF, condizioni del ricorso](https://www.acf.consob.it/ricorso/quando-come-fare-ricorso). Verifica al 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/'+note+'.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/'+note+'.md", "wiki/topics/authority-rettifiche-2026.md", ',1);p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,12));d['chaptersReadThisCycle']=list(range(1,12));d['findingsFullyApplied']+=['V05-20','V05-21'];d['findingsPartiallyApplied']['V05-22']='ACF capitolo 11 completato; confronto ABF/AAS nel capitolo 12 da integrare';d['findingsPartiallyApplied']['V05-02']='Capitoli 1–11: 66 quesiti e 11 casi specifici';d['pending']=['Fonti e integrazioni capitoli 12–15','90 quesiti / 15 casi e 10 simulazioni complessivi','Matrice, indici, rinvii','Audit e freeze tramite CLI','Figure e PDF coordinatore'];f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][10]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Applied chapter 11.')
