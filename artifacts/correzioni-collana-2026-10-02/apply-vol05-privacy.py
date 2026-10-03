from pathlib import Path
import json
O=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');note='vol-05-garante-procedimenti-verifica-2026-10-03'
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## Garante: competenza e procedimento\n\n[[sources/'+note+']] chiarisce esclusione dello sportello unico per i trattamenti pubblici ex articolo 55(2), poteri correttivi, legittimazione e termini del reclamo, difesa e giudice ordinario.\n',encoding='utf8')
p=B/'chapters/13-garante-privacy-poteri-procedimenti-cooperazione.md';s=p.read_text(encoding='utf8')
for title,n in [('Poteri: indagare, correggere, autorizzare, indirizzare',2),('Istruttoria, ispezione e misura: dalla criticità al provvedimento',3)]:
 marker=next(x for x in s.splitlines() if x.startswith('## N-MF05-13-0'+str(n)))
 s=s.replace('### '+title+'\n\n'+marker,marker+'\n\n### '+title)
a=s.index('L’elenco non va studiato') if 'L’elenco non va studiato' in s else s.index("L'elenco non va studiato")
s=s[:a]+'''La distinzione fra **avvertimento** e **ammonimento** dipende dal fatto: il primo riguarda un trattamento previsto che può violare il GDPR; il secondo una violazione già commessa (articolo 58, paragrafo 2, lettere a e b). Un progetto non ancora avviato e una pubblicazione illecita già avvenuta non sono quindi la stessa situazione.

Le sanzioni dell'articolo 83 hanno due principali fasce massime: **10 milioni di euro o 2%** del fatturato mondiale annuo precedente per l'impresa, e **20 milioni o 4%**, applicando il maggiore importo, per le categorie rispettivamente indicate. Non sono importi fissi: gravità, durata, dolo/colpa, misure di attenuazione, precedenti, cooperazione e altri criteri guidano la decisione. Per esempio, violazioni degli obblighi di sicurezza e violazioni dei principi fondamentali ricadono in categorie differenti. Anche le autorità pubbliche possono essere destinatarie del procedimento e delle sanzioni in Italia, secondo l'articolo 166 del Codice; la natura pubblica non è un'immunità generale.

'''+s[a:]
a=s.index("L'interessato che ritenga");b=s.index('### Istruttoria, ispezione',a)
# Preserve figure and next nucleus while replace conceptual section only.
b=s.rfind('## N-MF05-13-03',a,b+1)
s=s[:a]+'''Il **reclamo** dell'articolo 77 GDPR è la tutela dell'interessato che ritiene violata la disciplina nel trattamento dei dati che lo riguardano. Può rivolgersi in particolare all'autorità dello Stato della residenza abituale, del lavoro o della presunta violazione. Il reclamo è sottoscritto dall'interessato, anche con rappresentanza debitamente documentata; è possibile il mandato a un ente del terzo settore attivo nella tutela dei dati secondo l'articolo 142. Non è un'azione popolare indistinta.

L'atto indica fatti, date, trattamento, titolare/responsabile se conosciuto, disposizioni asseritamente violate, misure richieste e recapito; si allegano documenti utili e l'eventuale mandato. È **gratuito**, salve le eccezioni per richieste manifestamente infondate o eccessive. Per reclami esclusivamente relativi ai diritti degli articoli 15–22, il regolamento Garante 1/2019 disciplina il previo esercizio verso il titolare e le fondate ragioni che ne giustifichino l'omissione: non si trasforma questo percorso particolare in un obbligo identico per ogni reclamo.

La **segnalazione**, articolo 144 del Codice, può invece essere presentata da chiunque per sollecitare un controllo. Deve offrire elementi comprensibili; non comporta necessariamente un provvedimento individuale. Il Garante può inoltre agire d'ufficio. Una segnalazione di un'associazione non mandataria non diventa automaticamente il reclamo personale di tutti gli utenti.

### Le fasi e i termini: non esiste un unico orologio

| Passaggio | Regola e funzione |
| --- | --- |
| Verifica preliminare | Si controllano regolarità, materia, elementi e misure richieste; può seguire archiviazione motivata o apertura del procedimento. |
| Informazione al reclamante | Entro tre mesi, informazione sullo stato o sull'esito. Non è il termine universale per irrogare una sanzione. |
| Decisione del reclamo | Articolo 143: entro nove mesi; fino a dodici per esigenze istruttorie motivate e comunicate. Il termine è sospeso durante la cooperazione dell'articolo 60. |
| Contestazione e difesa | Le presunte violazioni vengono comunicate nei termini e con le eccezioni di legge. Entro trenta giorni dal ricevimento si possono presentare difese/documenti e chiedere audizione (articolo 166). |
| Esito | Archiviazione o misura fondata su fatto e potere: conformazione, limitazione, ordine o sanzione secondo i presupposti; nessun automatismo. |

**Giudice e danni.** L'articolo 78 GDPR garantisce ricorso contro una decisione vincolante dell'autorità e quando questa non tratti il reclamo o non informi entro tre mesi. In Italia la controversia spetta al **Tribunale ordinario**, nel rito disciplinato dall'articolo 10 del D.Lgs. 150/2011: contro il provvedimento, trenta giorni dalla comunicazione, sessanta per il ricorrente residente all'estero. Non si applica il generico ricorso al TAR perché il Garante è un'autorità amministrativa. Per il mancato riscontro opera la specifica previsione del comma 4, distinta dall'impugnazione di un atto ricevuto.

L'articolo 140-bis del Codice pone l'alternatività fra reclamo e domanda giudiziaria **tra le stesse parti e sul medesimo oggetto**, salve le tutele espressamente previste. Non va letto come rinuncia a ogni tutela giudiziaria: restano impugnazione dell'atto e rimedi GDPR. Il **risarcimento dell'articolo 82** è richiesto al giudice, dimostrando i presupposti; il Garante non liquida il danno al reclamante. Nell'esame si tengono distinti ordine di cancellazione, sanzione pubblica e risarcimento individuale.

'''+s[b:]
a=s.index('### Trasparenza amministrativa e privacy')
s=s[:a]+'''**L'eccezione decisiva per le autorità pubbliche.** L'articolo **55, paragrafo 2**, attribuisce i trattamenti delle autorità pubbliche, e quelli dei privati fondati sull'articolo 6(1)(c) o (e), all'autorità dello Stato membro interessato: **l'articolo 56 sullo sportello unico non si applica**. Un Comune italiano che gestisce un concorso resta soggetto al Garante per tale trattamento anche se usa un responsabile stabilito in un altro Stato. Se il fornitore riusa i dati per proprie autonome finalità commerciali, si analizza separatamente quel trattamento e si verificano gli eventuali presupposti transfrontalieri. Non si trasferisce al fornitore l'intera responsabilità dell'ente con una clausola contrattuale.

'''+s[a:]
s=s.replace("Un eventuale trattamento transfrontaliero richiede, in più, di accertare i suoi presupposti: il semplice uso della stessa tecnologia in altri Stati non basta, da solo, a individuare un'autorità capofila o a sottrarre il caso alla competenza ordinaria.","Per il trattamento del concorso da parte dell'ente italiano opera l'articolo 55(2): è competente il Garante e non si applica lo sportello unico dell'articolo 56. Il fornitore estero non sposta questa competenza. Un suo eventuale riuso autonomo per finalità commerciali costituisce invece un trattamento distinto, da qualificare e valutare separatamente anche ai fini della cooperazione europea.")
s=s.replace('### Laboratorio di qualificazione\n\n','')
a=s.index('## N-MF05-13-05');s=s[:a]+'''## N-MF05-13-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Un Comune italiano gestisce candidature tramite un responsabile francese. Lo sportello unico trasferisce automaticamente il reclamo contro il trattamento comunale alla Francia?

**Risposta corretta:** no. Il trattamento dell'autorità pubblica ricade nell'articolo 55(2); l'articolo 56 non si applica. Si esamina separatamente un eventuale autonomo riuso commerciale del fornitore.

**Quesito 2.** Un progetto non ancora avviato presenta una probabile violazione. Avvertimento e ammonimento sono sinonimi?

**Risposta corretta:** no. L'avvertimento riguarda il trattamento previsto che può violare il GDPR; l'ammonimento riguarda una violazione già avvenuta. Nessuno dei due è una tappa obbligatoria prima di ogni sanzione.

**Quesito 3.** Una persona estranea al trattamento segnala una pubblicazione illecita. Il Garante deve ignorarla perché non è interessata?

**Risposta corretta:** no. Chiunque può segnalare ai sensi dell'articolo 144. La segnalazione può alimentare il controllo; non equivale al reclamo dell'interessato e non impone un esito individuale favorevole.

**Quesito 4.** Dopo tre mesi il Garante comunica che il reclamo è ancora in istruttoria. È già violato per questo il termine per decidere?

**Risposta corretta:** no. Tre mesi riguardano l'informazione; il termine dell'articolo 143 è nove mesi, estendibile a dodici per esigenze motivate comunicate, con la sospensione prevista per cooperazione. La durata di una distinta fase sanzionatoria non si deduce da questo solo dato.

**Quesito 5.** La contestazione ricevuta ieri concede trenta giorni per difese. È corretto inviare documenti e chiedere audizione?

**Risposta corretta:** sì. Sono garanzie dell'articolo 166(6) e del regolamento 1/2019. Non presentare difese non impedisce di proseguire il procedimento; una contestazione non è ancora una condanna.

**Quesito 6.** Il Garante irroga una sanzione a una società. Il reclamo dell'utente gli attribuisce automaticamente un risarcimento pari alla sanzione?

**Risposta corretta:** no. Sanzione e risarcimento hanno destinatari e presupposti diversi. Il danno si fa valere davanti al giudice; contro il provvedimento del Garante il rimedio nazionale è davanti al Tribunale ordinario, non al TAR.

### Caso ragionato di chiusura

**Traccia.** Il 3 ottobre 2026 una candidata scopre che il Comune pubblica, insieme alla graduatoria, il suo documento di identità. Il portale è gestito da un fornitore spagnolo, che dichiara di riutilizzare i curriculum per una propria banca dati commerciale. La candidata chiede al Garante cancellazione, multa fissa di 20 milioni e risarcimento; un vicino, non candidato, invia una segnalazione. Qualifica competenze e richieste.

**Soluzione.** Si conservano URL, schermate datate, informativa, contratto e istruzioni al fornitore. Per la pubblicazione comunale il Garante è competente ex articolo 55(2), senza sportello unico; si verifica la base normativa e la necessità dei singoli dati. Il documento di identità non diventa pubblicabile per la sola esigenza di trasparenza della graduatoria. Il riuso commerciale del fornitore richiede una separata analisi di finalità, base, ruoli e presupposti transfrontalieri; non è automaticamente coperto dalle istruzioni comunali. La candidata presenta un reclamo circostanziato; il vicino può segnalare. Il Garante valuta ordini o limitazioni pertinenti e, se ricorrono i presupposti, una sanzione proporzionata, anche verso il soggetto pubblico. Venti milioni sono un massimo di una categoria, non un importo fisso. La domanda risarcitoria va al giudice con i relativi presupposti. Tre mesi segnano l'obbligo informativo, non la promessa di una multa già definitiva.

**Autovalutazione:** un punto per articolo 55(2), uno per separazione dei trattamenti, uno per reclamo/segnalazione, uno per ordine–sanzione–danni.

**Riferimenti normativi e professionali.** GDPR, articoli 55–58, 60–65, 77–83; Codice privacy, D.Lgs. 196/2003, articoli 140-bis, 142–144, 152, 157–158 e 166; D.Lgs. 150/2011, articolo 10; regolamento Garante 1/2019 nel testo aggiornato al 15 aprile 2026. [Garante, come presentare reclamo](https://www.garanteprivacy.it/diritti/come-agire-per-tutelare-i-tuoi-dati-personali/reclamo/). Verifica al 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/'+note+'.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/'+note+'.md", "wiki/topics/authority-rettifiche-2026.md", ',1);p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,14));d['chaptersReadThisCycle']=list(range(1,14));d['findingsFullyApplied']+=['V05-24','V05-25'];d['findingsPartiallyApplied']['V05-02']='Capitoli 1–13: 78 quesiti e 13 casi specifici';d['pending'][0]='Fonti e integrazioni capitoli 14–15';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][12]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Applied chapter 13.')
