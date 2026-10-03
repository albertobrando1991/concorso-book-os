from pathlib import Path
import json
O=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');note='vol-05-anac-whistleblowing-verifica-2026-10-03'
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## ANAC: contratti e whistleblowing\n\n[[sources/'+note+']] distingue PNA e attuazione interna, attribuzione RPCT, perimetro pubblico/privato, motivi irrilevanti, termini dei canali e autonoma comunicazione di ritorsione; separa poteri ANAC e giudice.\n',encoding='utf8')
p=B/'chapters/14-anac-prevenzione-vigilanza-whistleblowing.md';s=p.read_text(encoding='utf8')
s=s.replace('Non può però sostituire organi di indirizzo, dirigenti, responsabili di procedimento, uffici di controllo o gestori dei canali di segnalazione.',"Non sostituisce organi di indirizzo, dirigenti, responsabili di procedimento e uffici di controllo nei loro compiti. Ha però una specifica attribuzione sul whistleblowing: nei soggetti pubblici tenuti a prevedere il RPCT, **a lui è affidata la gestione del canale interno** (articolo 4, comma 5, D.Lgs. 24/2023). La struttura lo supporta con personale formato e cautele di riservatezza; distinguere ruoli non significa escludere questa competenza.")
a=s.index('## N-MF05-14-02');s=s[:a]+'''Per le amministrazioni soggette al **PIAO**, rischi corruttivi e trasparenza confluiscono nella relativa sottosezione della programmazione integrata, coordinata con valore pubblico, obiettivi e organizzazione. Dove il PIAO non si applica, resta lo strumento anticorruzione prescritto, come il **PTPCT** o le misure integrative pertinenti. PNA, PIAO e PTPCT non sono tre piani da copiare in parallelo: il primo indirizza, gli altri collocano l'attuazione nel quadro dell'ente.

**Esempio compilato.** Processo: acquisti informatici ripetuti. Rischio: specifiche orientate a un fornitore. Misura: motivazione del fabbisogno e verifica indipendente delle specifiche prima della richiesta di offerta. Responsabile operativo: dirigente dell'ufficio acquisti; monitoraggio RPCT su campione trimestrale. Indicatore: fascicoli con verifica documentata/fascicoli campionati; obiettivo didattico 100%. Un indicatore raggiunto prova l'esistenza del presidio documentale, non l'assenza assoluta di corruzione.

'''+s[a:]
a=s.index('La **trasparenza**');s=s[:a]+'''### Contratti pubblici: attribuzioni da riconoscere

L'articolo **222 del D.Lgs. 36/2023** comprende vigilanza su affidamento ed esecuzione, atti generali come bandi-tipo, qualificazione delle stazioni appaltanti, funzioni sulla Banca dati nazionale, ispezioni e sanzioni nelle fattispecie attribuite. La vigilanza collaborativa si fonda su protocolli e supporta la procedura: non trasferisce ad ANAC la gestione della gara o la responsabilità del RUP.

L'articolo **220** distingue il **precontenzioso**, attivato dalle parti su questioni di gara e concluso con parere previo contraddittorio entro trenta giorni, dai poteri processuali dell'Autorità. La stazione appaltante che non intende conformarsi al parere motiva il dissenso entro quindici giorni e lo comunica alle parti e ad ANAC. Per gravi violazioni ANAC può adottare un parere motivato e, persistendo le condizioni, ricorrere al giudice amministrativo; è inoltre legittimata a impugnare gli atti dei contratti di rilevante impatto nei casi previsti. Non si risponde che ANAC «annulla la gara» come un giudice. Le scansioni e i soggetti dei diversi commi vanno tenuti distinti.

'''+s[a:]
s=s.replace('| Interesse | Mira all\'interesse pubblico o all\'integrità dell\'ente? | Confondere il canale con una vertenza individuale |',"| Oggetto | La violazione lede interesse pubblico o integrità dell'ente? | Valutare l'altruismo personale al posto dell'oggetto |")
a=s.index('Il sistema prevede canali');s=s[:a]+'''**Oggetto e motivazione personale sono distinti.** L'articolo 16, comma 2, rende irrilevanti i motivi che hanno spinto a segnalare. Un dipendente in conflitto con il dirigente può essere protetto se segnala, con fondati motivi e canale corretto, una violazione rientrante nel decreto. È esclusa invece la rivendicazione che attiene **esclusivamente** al suo rapporto individuale. Non si pretende la prova di un movente altruistico e non basta chiamare «interesse pubblico» una vertenza personale.

| Contesto | Violazioni e canali da distinguere |
| --- | --- |
| Settore pubblico | Perimetro dell'articolo 2(1)(a), con canali interni/esterni, denuncia o divulgazione alle rispettive condizioni; non soltanto reati di corruzione. |
| Privato con almeno 50 lavoratori medi, o settori UE indicati anche sotto soglia | Violazioni UE dei numeri 3–6: canali e tutele del decreto alle condizioni previste. Vanno verificati anche i regimi speciali esclusi dall'articolo 1. |
| Ente privato con modello 231 | Per condotte 231/violazioni del modello, canale interno; se raggiunge 50 lavoratori, anche i percorsi per le distinte violazioni UE nei termini dell'articolo 3. Non ogni illecito privato entra in ogni canale. |

Sono protetti, nei presupposti di legge, anche consulenti, autonomi, tirocinanti, volontari e altre categorie, non solo dipendenti. Le informazioni possono essere acquisite prima dell'inizio del rapporto, durante la prova o nel rapporto poi cessato. Ai soggetti collegati dell'articolo 3(5) si estendono misure protettive, ma non automaticamente le presunzioni riservate al segnalante.

'''+s[a:]
s=s.replace('tra le quali rientrano, in sintesi, assenza o non conformità del canale interno obbligatorio,','tra le quali rientrano, in sintesi, mancata previsione dell’obbligo di canale interno, oppure canale obbligatorio non attivo o non conforme,')
a=s.index('La **riservatezza**');s=s[:a]+'''### Termini e gestione dei canali

Il gestore interno dà avviso di ricevimento entro **sette giorni** e riscontro entro **tre mesi dall'avviso**, oppure, se manca, dalla scadenza dei sette giorni dalla presentazione. Mantiene interlocuzioni, può chiedere integrazioni e dà diligente seguito. Se la segnalazione arriva al soggetto interno sbagliato, questi la trasmette al competente entro sette giorni dando notizia al segnalante. Riscontro significa informazione sul seguito dato o previsto, non promessa di processo già concluso.

Per il canale esterno ANAC, avviso entro **sette giorni**, con le eccezioni previste a protezione del segnalante; riscontro entro **tre mesi**, o **sei** per giustificate e motivate ragioni, con analoghe decorrenze. L'esito finale è comunicato separatamente e può essere archiviazione, trasmissione all'autorità competente, raccomandazione o sanzione nei casi attribuiti. Le linee guida interne sono state approvate con delibera **478/2025**; quelle esterne 311/2023 sono state aggiornate dalla **479/2025**.

'''+s[a:]
a=s.index('### ANAC e le segnalazioni esterne');s=s[:a]+'''L'articolo 12 esclude la segnalazione dall'accesso documentale e civico e protegge anche le informazioni che identificano indirettamente il segnalante. Nel procedimento disciplinare fondato su accertamenti autonomi, l'identità resta riservata; se la contestazione poggia sulla segnalazione e conoscere l'identità è indispensabile alla difesa, l'utilizzo richiede il **consenso espresso** del segnalante, con comunicazione motivata delle ragioni della rivelazione. Procedimento penale e contabile hanno le proprie regole: non si promette segretezza assoluta in qualunque sede. Una segnalazione anonima può beneficiare delle tutele se il segnalante viene poi identificato e subisce ritorsioni, alle condizioni dell'articolo 16.

'''+s[a:]
a=s.index('Quando si allega una ritorsione');s=s[:a]+'''La **comunicazione di una ritorsione ad ANAC**, articolo 19, è distinta dalla **segnalazione esterna della violazione**, articolo 6. Chi ha segnalato internamente ed è poi trasferito per ritorsione può comunicarlo ad ANAC: non deve prima ripresentare la violazione all'esterno e dimostrare nuovamente una delle condizioni dell'articolo 6 per quella comunicazione. Restano da verificare i presupposti sostanziali di protezione e la condotta denunciata.

'''+s[a:]
s=s.replace("Quarto: **ritorsione**. L'esclusione dal gruppo di lavoro deve essere confrontata con il tempo della segnalazione, le motivazioni dell'ente, le prassi organizzative, i criteri di scelta e gli atti disponibili. Non basta la successione temporale; non basta neppure l'etichetta “esigenza organizzativa”.", "Quarto: **ritorsione**. La comunicazione dell'esclusione ad ANAC segue l'articolo 19 e non richiede una previa nuova segnalazione esterna ex articolo 6. Verificati i presupposti di protezione e allegata la misura ritorsiva, opera la presunzione dell'articolo 17 per il segnalante: chi ha deciso l'esclusione deve provare ragioni estranee. Si acquisiscono date, motivazioni, prassi, criteri e atti; la mera etichetta «esigenza organizzativa» non assolve tale onere. Per un facilitatore il regime probatorio è diverso.")
s=s.replace("e che sia effettuata nell'interesse pubblico o dell'integrità dell'ente attraverso il canale e con le condizioni applicabili.","che ledano interesse pubblico o integrità dell'ente, rispettando canale e condizioni. Il movente personale è irrilevante ai sensi dell'articolo 16(2).")
s=s.replace('### Mappa BANDO\n\n## N-MF05-14-04 · Applicazione alla prova','## N-MF05-14-04 · Applicazione alla prova\n\n### Mappa BANDO').replace('### Prova di trasferimento\n\n','')
a=s.index('## N-MF05-14-05');s=s[:a]+'''## N-MF05-14-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** In un ente pubblico obbligato a nominare il RPCT, questi deve restare estraneo alla gestione del canale interno?

**Risposta corretta:** no. L'articolo 4(5) gli affida la gestione. Restano distinte le responsabilità di dirigenti e uffici sui processi e le garanzie organizzative del canale.

**Quesito 2.** Un dipendente segnala una manipolazione degli affidamenti per ostilità personale verso il dirigente. Il movente elimina da solo la protezione?

**Risposta corretta:** no. I motivi personali sono irrilevanti. Occorrono oggetto pertinente, fondati motivi sulla verità e rispetto delle condizioni; una vertenza esclusivamente individuale resta fuori dal perimetro.

**Quesito 3.** Una segnalazione interna ha avviso di ricevimento il 10 ottobre. Il termine ordinario di riscontro decorre da quella data?

**Risposta corretta:** sì, tre mesi dall'avviso. Se manca l'avviso, decorre dalla scadenza dei sette giorni dalla presentazione. Non significa che ogni procedimento collegato debba essere concluso entro tre mesi.

**Quesito 4.** Dopo una segnalazione interna, il dipendente subisce una presunta ritorsione. Per comunicarla ad ANAC deve prima superare il filtro della segnalazione esterna della violazione?

**Risposta corretta:** no. La comunicazione di ritorsione è il percorso dell'articolo 19, distinto dall'articolo 6. Vanno comunque verificati i presupposti della tutela e i fatti allegati.

**Quesito 5.** Il facilitatore che lamenta ritorsione beneficia sempre della stessa presunzione del segnalante?

**Risposta corretta:** no. Le misure protettive si estendono ai soggetti dell'articolo 3(5), ma le presunzioni dell'articolo 17(2–3) hanno un ambito soggettivo distinto, riferito alle persone dei commi 1–4.

**Quesito 6.** ANAC accerta una ritorsione. Può dichiarare essa stessa la nullità del licenziamento e ordinare il risarcimento?

**Risposta corretta:** no. Accertamento e sanzioni amministrative competono ad ANAC nel suo ambito; dichiarazione di nullità, reintegrazione, danni e misure giudiziarie competono al giudice, secondo l'articolo 19.

### Caso ragionato di chiusura

**Traccia.** Una dipendente comunale trasmette al RPCT documenti datati che mostrano specifiche di acquisto copiate dal catalogo di un solo fornitore. È in conflitto personale con il dirigente. Riceve avviso del canale interno; due settimane dopo è esclusa dai progetti, mentre un collega che l'ha aiutata perde un incarico. L'ente nega protezione a entrambi per il movente personale e sostiene che ANAC può intervenire solo dopo una segnalazione esterna senza seguito. Risolvi.

**Soluzione.** Il RPCT è gestore del canale interno per l'ente obbligato. Si verificano contesto lavorativo, documenti, oggetto e fondati motivi; non si pretende l'accertamento già definitivo della manipolazione. Il movente personale non elimina la tutela. Dipendente e collega possono comunicare le presunte ritorsioni ad ANAC ex articolo 19, senza la sequenza inventata dall'ente. Per la dipendente, verificati i presupposti, opera la presunzione: il decisore deve provare ragioni estranee alla segnalazione. Il collega va qualificato come facilitatore o altro soggetto collegato; la tutela non gli trasferisce automaticamente la presunzione. Si conservano provvedimenti, cronologia, criteri e messaggi, proteggendo identità e contenuto. ANAC valuta e può sanzionare nel proprio perimetro; al giudice spettano nullità, ripristino e danni. Sul piano preventivo l'ente verifica specifiche, conflitti, controlli indipendenti e monitoraggio; sul piano contrattuale si applicano i pertinenti poteri, senza dichiarare ogni anomalia automaticamente reato.

**Autovalutazione:** un punto per RPCT e motivi, uno per distinzione articolo 6/19, uno per prova differenziata, uno per ANAC/giudice e prevenzione.

**Riferimenti normativi e professionali.** Legge 190/2012; D.Lgs. 33/2013; disciplina PIAO, articolo 6 del DL 80/2021 e DM 132/2022; PNA 2025, delibera ANAC 19 del 28 gennaio 2026; D.Lgs. 36/2023, articoli 220 e 222; D.Lgs. 24/2023, articoli 1–8, 12, 16–19; linee guida ANAC 478/2025 e 311/2023 aggiornate dalla 479/2025. [ANAC, whistleblowing](https://www.anticorruzione.it/en/-/whistleblowing). Verifica al 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/'+note+'.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/'+note+'.md", "wiki/topics/authority-rettifiche-2026.md", ',1);p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,15));d['chaptersReadThisCycle']=list(range(1,15));d['findingsFullyApplied']+=['V05-26','V05-27','V05-29'];d['findingsPartiallyApplied']['V05-28']='Capitolo 14 corretto, resta la simulazione del capitolo 15';d['findingsPartiallyApplied']['V05-02']='Capitoli 1–14: 84 quesiti e 14 casi specifici';d['pending'][0]='Integrazioni capitolo 15';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][13]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Applied chapter 14.')
