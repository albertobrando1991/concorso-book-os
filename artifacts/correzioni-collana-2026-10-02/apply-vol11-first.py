from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile/chapters')
SOURCE='sources/vol-11-ambiente-rettifiche-2026-10-03'
def get(n):
 p=next(B.glob(f'{n:02d}-*.md'));return p,p.read_text(encoding='utf8')
def save(p,t):
 for key,val in [('source_refs',SOURCE),('last_compiled_from','wiki/'+SOURCE+'.md'),('topics','topics/ambiente-rettifiche-2026')]:
  m=re.search(r'^'+key+r': (\[.*\])$',t,re.M);a=json.loads(m[1]);a.append(val) if val not in a else None;t=t[:m.start(1)]+json.dumps(a,ensure_ascii=False)+t[m.end(1):]
 t=re.sub(r'^updated_at: .*$', 'updated_at: 2026-10-03',t,flags=re.M);t=re.sub(r'^draft_stage: .*$', 'draft_stage: revision-in-progress',t,flags=re.M);t=re.sub(r'^review_required: .*$', 'review_required: true',t,flags=re.M)
 p.write_text(t,encoding='utf8')
def add(t,n,c,x):
 pattern=rf'(^## N-TR04-{n:02d}-{c:02d}[^\n]*\n)';assert re.search(pattern,t,re.M);return re.sub(pattern,lambda m:m[1]+'\n'+x.strip()+'\n\n',t,count=1,flags=re.M)

p,t=get(2)
t=add(t,2,1,'''### Parti e principi da collegare ai casi

La mappa completa distingue la Parte prima, dedicata ai principi; la seconda, a VAS, VIA e AIA; la terza, a difesa del suolo, acque e risorse idriche; la quarta, a rifiuti e bonifiche; la quinta, a emissioni e tutela dell'aria; la quinta-bis, a particolari installazioni; la sesta, al danno ambientale; la sesta-bis, all'estinzione di determinate contravvenzioni. Una bonifica non coincide con la riparazione del danno ambientale: può intervenire sul medesimo fatto ma ha presupposti e procedimento propri.

Gli artt. 3-bis–3-sexies rendono operativi i principi. La **precauzione** guida la gestione di un rischio plausibile in condizioni di incertezza scientifica; la **prevenzione** mira a evitare un danno conosciuto; la **correzione alla fonte** privilegia l'intervento sull'origine dell'inquinamento; **chi inquina paga** attribuisce al responsabile i costi secondo la disciplina applicabile, senza creare un diritto a inquinare. Lo sviluppo sostenibile considera anche generazioni future, risorse ed ecosistemi e richiede prioritaria considerazione di ambiente e patrimonio culturale nelle scelte discrezionali. La sussidiarietà distribuisce l'intervento tra livelli territoriali; l'accesso alle informazioni ambientali e la partecipazione permettono di conoscere e discutere le decisioni.

**Esempio:** per un serbatoio deteriorato, prevenzione significa evitare la perdita; dopo una fuoriuscita, correzione alla fonte significa arrestarla e contenere la diffusione; il recupero dei costi richiede individuazione del responsabile e base normativa. Non basta citare insieme quattro principi senza associare a ciascuno un effetto.''')
t=add(t,2,3,'''### La base costituzionale

L'art. 117, secondo comma, lettera s), della Costituzione attribuisce allo Stato la legislazione esclusiva in materia di tutela dell'ambiente, dell'ecosistema e dei beni culturali. Questo riparto legislativo non concentra tutti i procedimenti nel Ministero: tutela della salute, governo del territorio, protezione civile e altre competenze possono interagire con l'ambiente. Occorre distinguere materia, funzione e attribuzione amministrativa.

L'art. 118 colloca le funzioni amministrative presso i Comuni, salvo conferirle a livelli superiori per assicurarne l'esercizio unitario secondo sussidiarietà, differenziazione e adeguatezza. La disciplina settoriale e quella regionale individuano quindi il soggetto concreto. Il principio non autorizza il Comune a rilasciare una VIA statale. L'art. 3-quinquies del Codice ammette tutele regionali più restrittive per particolari situazioni territoriali, nel rispetto dei limiti normativi e senza discriminazioni arbitrarie o aggravi ingiustificati.''')
t=add(t,2,4,'''### Che cosa sono i LEPTA

La L. 28 giugno 2016, n. 132, art. 9, definisce i **Livelli essenziali delle prestazioni tecniche ambientali** come il minimo omogeneo che il SNPA deve garantire sul territorio nazionale nelle attività attribuitegli. Comprendono parametri funzionali, operativi, programmatici, strutturali, quantitativi e qualitativi; il Catalogo nazionale dei servizi ne organizza prestazioni e aspetti gestionali. La legge prevede determinazione mediante DPCM, su proposta ministeriale, con coinvolgimento del sistema e intesa territoriale, e aggiornamento almeno quinquennale.

La distinzione utile è fra **livello della prestazione** e **limite ambientale**. Il primo riguarda, per esempio, l'omogeneità del servizio tecnico e della sua programmazione; il secondo la concentrazione o altra condizione che un'attività deve rispettare. Un LEPTA non autorizza lo scarico e non è una concentrazione massima di inquinante. ISPRA esercita indirizzo e coordinamento tecnico ai sensi dell'art. 6; agenzie regionali e provinciali autonome partecipano al sistema mantenendo le attribuzioni definite dalle fonti.''')
# Remove exactly repeated methodological paragraphs from the second occurrence, replace with concrete applications.
for start in ['In pratica, la qualità della risposta dipende','Nella correzione annota anche il livello di certezza.','Un controllo finale rende la risposta più precisa.']:
 lines=t.splitlines();seen=False;out=[]
 for line in lines:
  if line.startswith(start):
   if seen:continue
   seen=True
  out.append(line)
 t='\n'.join(out)+'\n'
t=add(t,2,6,'''### Due mappe compilate da confrontare

**Caso A, progetto:** la traccia specifica che il progetto appartiene all'allegato II della Parte seconda del Codice e richiede la VIA statale. La mappa parte dal proponente che presenta progetto e studio d'impatto; passa all'autorità statale, ai contributi delle amministrazioni e del pubblico; termina con il provvedimento motivato e la verifica delle condizioni ambientali. Il rapporto di un'agenzia può alimentare l'istruttoria, ma non sostituisce il provvedimento di VIA. Il candidato allega alla risposta una scheda delle condizioni e dei soggetti cui compete verificarle.

**Caso B, impianto in esercizio:** la traccia consegna un'AUA provinciale rilasciata tramite SUAP e una segnalazione di odori. La mappa inizia dal titolo e dalle prescrizioni esistenti; distingue la segnalazione del residente, gli accertamenti tecnici, il confronto con le condizioni e la decisione dell'autorità individuata. Non si apre automaticamente una nuova VIA perché la segnalazione riguarda un impianto. Occorre qualificare l'anomalia e l'eventuale modifica, acquisendo dati e atti.

**Confronto risolto:** nel primo caso il presupposto è un progetto da valutare; nel secondo è l'esercizio di un'attività già autorizzata. Il documento principale cambia da studio d'impatto e provvedimento valutativo a titolo vigente, rapporto di controllo e decisione conseguente. La parola «ambiente» resta comune, ma non determina né la procedura né l'autorità. Valuta la tua mappa su quattro punti: presupposto esatto, fonte pertinente, distinzione tra supporto e decisione, controllo finale. Assegna un punto a ogni elemento corretto; un nome istituzionale senza funzione non ottiene il punto.''')
t=t.replace('La risposta è completa quando chiarisce anche come conservare l’evidenza:', '**Soluzione del primo esercizio:** occorrono parametro e unità, durata del campionamento, punto, metodo, condizioni di esercizio, meteo pertinente, incertezza e validazione. Il rapporto tecnico allega risultati e limiti di confrontabilità. Non è ancora possibile dichiarare un superamento, perché manca il parametro giuridico pertinente e la verifica della comparabilità dei dati.\n\nLa risposta è completa quando chiarisce anche come conservare l’evidenza:')
t=t.replace('La nota istruttoria deve separare fatti accertati, ipotesi e dati mancanti.', '**Soluzione del secondo esercizio:** il Comune acquisisce segnalazione e classificazione acustica; il gestore produce dati su sorgente e orari; ARPA, nel quadro applicabile, effettua misure e rapporto; l’autorità competente valuta il risultato e adotta l’atto motivato. La legge regionale e l’organizzazione locale vanno verificate per individuare competenza, richiesta e modalità del controllo. Il rapporto fonometro non equivale al provvedimento.\n\nLa nota istruttoria deve separare fatti accertati, ipotesi e dati mancanti.')
t=t.replace('rapporto fonometro','rapporto fonometrico')
t=t.replace('sistema nazionale a rete che collega ISPRA e agenzie regionali','sistema nazionale a rete che comprende ISPRA, agenzie regionali e agenzie delle province autonome')
t=t.replace('rete e coordinamento del sistema di agenzie','sistema formato da ISPRA e ARPA/APPA')
save(p,t)

p,t=get(3)
t=t.replace('l’autorità può esprimere un giudizio unitario','l’autorità esprime un giudizio unitario')
t=t.replace('Lo screening è una verifica preliminare.','Lo screening è una verifica di assoggettabilità, distinta dalla valutazione preliminare dell’art. 6, comma 9.')
t=t.replace('La verifica preliminare serve a evitare automatismi e a valutare il caso concreto.','La verifica di assoggettabilità serve a evitare automatismi e a valutare il caso concreto.')
t=add(t,3,4,'''### Tre procedimenti distinti, tre domande

**Valutazione preliminare, art. 6, comma 9.** Riguarda modifiche, estensioni o adeguamenti tecnici migliorativi dei progetti elencati, nei limiti della norma. Il proponente presume l'assenza di impatti significativi negativi e può presentare liste di controllo. Entro 30 giorni l'autorità comunica se occorre screening, VIA oppure se l'intervento non ricade nelle categorie indicate. La richiesta facoltativa serve a individuare l'iter: non è un'autorizzazione alla realizzazione.

**Screening VIA, art. 19.** Riguarda progetti nelle categorie pertinenti: studio preliminare ambientale, controllo iniziale di completezza entro 5 giorni, eventuali integrazioni entro 15, pubblicazione e osservazioni entro 30. La decisione segue entro 60 giorni dalla scadenza della consultazione, oppure entro 45 dal ricevimento delle integrazioni del comma 6. Nei casi eccezionali motivati è possibile una sola proroga fino a 20 giorni. L'esito assoggetta o esclude dalla VIA, con motivazione ed eventuali condizioni nei presupposti previsti.

**Screening VAS, art. 12.** Riguarda piani e programmi nei casi dell'art. 6, commi 3 e 3-bis. L'autorità procedente trasmette un rapporto preliminare di assoggettabilità; i soggetti ambientali rendono contributi entro 30 giorni; l'autorità competente decide entro 90 giorni dalla trasmissione. La domanda è se quel piano o programma possa avere impatti significativi, non se autorizzare una singola opera.

**Caso risolto:** la traccia dichiara che una modifica migliorativa di un progetto elencato non supera autonomamente una soglia di VIA e che il proponente chiede di chiarire la procedura. L'iter da esaminare è l'art. 6, comma 9; la conclusione non può essere «esente per decisione del gestore». Se invece la traccia dichiara una categoria dell'allegato IV soggetta a verifica, il procedimento è lo screening VIA. Un piccolo piano comunale non diventa automaticamente screening VAS: occorre controllare il campo dell'art. 6 e la significatività, senza usare la sola dimensione come esenzione.''')
t=add(t,3,5,'''### Competenza, partecipazione e provvedimenti unici

Nella ripartizione ordinaria dell'art. 7-bis, l'allegato II individua i progetti soggetti a VIA statale e il II-bis quelli a screening statale; gli allegati III e IV individuano rispettivamente VIA e screening regionali, ferme le disposizioni speciali. Perciò servono categoria, capacità, localizzazione e natura della modifica. Un progetto posto in un Comune non è per questo di competenza comunale.

Nel procedimento di VAS gli artt. 13–15 distinguono consultazione preliminare, ordinariamente di 45 giorni, con contributi dei soggetti ambientali entro 30; consultazione pubblica sulla proposta e rapporto ambientale, di 45 giorni; parere motivato, entro 45 giorni dalla scadenza dei termini della consultazione. L'autorità procedente adegua il piano tenendo conto del parere prima dell'approvazione. I termini decorrono da atti diversi e non esprimono una durata unica garantita.

Il **PUA**, art. 27, è il provvedimento unico in materia ambientale per una VIA statale, richiesto dal proponente e comprensivo dei titoli ambientali previsti e richiesti. Il **PAUR**, art. 27-bis, coordina la VIA regionale e i titoli per realizzazione ed esercizio indicati nell'istanza; la determinazione conclusiva della conferenza li elenca espressamente. La conferenza si conclude entro 90 giorni dalla prima riunione, ma questo termine non comprende automaticamente tutte le fasi precedenti. I titoli mantengono le proprie regole di rinnovo, controllo e sanzione.

La **VIncA**, valutazione di incidenza dell'art. 5 DPR 357/1997, tutela habitat e specie dei siti Natura 2000 rispetto a piani e interventi con possibili incidenze significative, anche cumulative. Un intervento esterno al sito può incidere sui suoi obiettivi di conservazione. Quando pertinente, la VIncA si integra nella VIA; lo studio deve però contenere l'analisi specifica. Una VIA favorevole non consente di saltarla. In caso di esito negativo le eccezioni richiedono i rigorosi presupposti normativi, comprese alternative, motivi imperativi e compensazioni; per habitat o specie prioritari valgono condizioni ulteriori.''')
t=t.replace('| Opera già definita da realizzare in un sito specifico | VIA | La valutazione riguarda impatti concreti del progetto. |','| Opera definita, ma senza categoria, dimensioni e localizzazione ambientale | Dati insufficienti per scegliere l’iter | Acquisire categoria degli allegati, capacità, vincoli e modifiche; la sola parola «opera» non impone la VIA. |')
t=t.replace('| Intervento progettuale con impatti incerti e da selezionare | Screening | La domanda è se serva la VIA completa. |','| Progetto che la traccia dichiara incluso nell’allegato IV e soggetto a verifica | Screening VIA | La categoria normativa, non la sola incertezza, determina l’accesso alla verifica. |')
t=t.replace('| Variante urbanistica che cambia la destinazione di un’area | VAS | La decisione incide sulla cornice pianificatoria. |','| Variante urbanistica che cambia la destinazione di un’area | VAS o screening VAS secondo art. 6 | Acquisire natura e portata della variante; non tutte le varianti seguono lo stesso iter. |')
save(p,t)

p,t=get(4)
t=t.replace('Il SUAP è il punto di accesso per il gestore e adotta o trasmette il provvedimento conclusivo secondo la disciplina applicabile.','Il SUAP è il punto di accesso per il gestore: l’autorità competente adotta l’AUA e la trasmette al SUAP, che rilascia il titolo e cura il raccordo con il procedimento conclusivo.')
t=t.replace("L'elenco è tassativo e non autorizza a inserire nell'AUA qualunque atto ambientale.","Nel testo vigente al 3 ottobre 2026 si aggiungono le lettere g-bis e g-ter: autorizzazione e notifica di pratica degli artt. 26 e 24 del D.Lgs. 101/2020 in materia di radioprotezione. Inoltre il comma 2 consente a Regioni e Province autonome di individuare ulteriori atti ambientali, nel rispetto della disciplina europea e nazionale. Non è quindi corretto trattare i sette titoli tradizionali come elenco chiuso, né includere un atto senza verificarne la base normativa.")
t=add(t,4,2,'''### Campo AIA e riesame

Il campo dell'AIA si controlla sulle attività e sulle soglie dell'allegato VIII alla Parte seconda; l'allegato XII individua le installazioni di competenza statale. Le altre competenze discendono dalla disciplina applicabile. Il nome dell'attività economica o la dimensione dell'impresa, da soli, non risolvono la classificazione.

L'art. 29-octies distingue riesame BAT e riesame periodico. Entro **4 anni** dalla pubblicazione delle conclusioni BAT relative all'attività principale occorre riesaminare le condizioni e verificare l'adeguamento dell'installazione. Il termine periodico ordinario è **10 anni** dal rilascio o ultimo riesame complessivo, elevato alle condizioni di legge a **12 anni** per ISO 14001 e **16 anni** per EMAS. Queste estensioni non rinviano il termine BAT né impediscono un riesame anticipato per inquinamento, sicurezza o nuove norme.

**Esercizio risolto:** AIA rilasciata nel 2024, installazione già EMAS; nuove conclusioni BAT per l'attività principale pubblicate nel 2026. Il gestore non può attendere il 2040: la verifica delle condizioni e della conformità interviene entro il 2030 in relazione a quelle BAT, salvi altri presupposti anticipatori. Gli anni del caso sono didattici; il termine si calcola dalla data effettiva di pubblicazione.

**Aggiornamento europeo:** la direttiva (UE) 2024/1785 modifica la disciplina delle emissioni industriali. Alla verifica del 3 ottobre 2026, la documentazione parlamentare italiana acquisita riguarda lo schema di recepimento, Atto del Governo 420, con pareri di settembre. Le regole nazionali qui esposte derivano dal testo corrente del D.Lgs. 152/2006, non dallo schema: una proposta di modifica non va usata come norma già applicabile.''')
t=add(t,4,3,'''### Durata e calendario AUA

L'AUA dura **15 anni dal rilascio**; l'istanza di rinnovo va presentata almeno **6 mesi prima** della scadenza, con documentazione aggiornata, potendo richiamare quella già disponibile se immutata. La prosecuzione in attesa del rinnovo tempestivo segue l'art. 5 e le eventuali diverse disposizioni settoriali.

Nel procedimento dell'art. 4, il controllo iniziale di correttezza formale si conclude entro 30 giorni. Se tutti i titoli sostituiti hanno un termine non superiore a 90 giorni, l'autorità adotta l'AUA entro **90 giorni** dalla domanda. Se almeno un termine è superiore, il percorso prevede **120 giorni**, oppure **150** con le integrazioni nel caso previsto. Vanno considerati conferenza, richieste documentali e sospensioni: i 30 giorni iniziali non producono un'autorizzazione tacita allo scarico o alle emissioni.

**Caso:** un'AUA rilasciata il 1° ottobre 2026 scade il 1° ottobre 2041; il gestore programma il rinnovo almeno sei mesi prima, dunque entro il 1° aprile 2041, salvo fatti che impongano un aggiornamento anticipato. Il calendario non esonera dagli autocontrolli e non permette modifiche sostanziali senza il procedimento necessario.''')
t=add(t,4,4,'''### Regime ordinario e regimi dell'art. 272

L'autorizzazione ordinaria dell'art. 269 dura **15 anni** e il rinnovo va chiesto almeno **un anno prima** della scadenza. Nell'art. 272, comma 1, le attività scarsamente rilevanti individuate nell'allegato IV, Parte I, sono escluse dall'autorizzazione del titolo, restando applicabili le disposizioni e comunicazioni previste. Non sono attività libere da qualunque tutela.

I commi 2–3 disciplinano invece le autorizzazioni generali: il gestore verifica categorie, soglie, sostanze, condizioni e prescrizioni e presenta adesione almeno **45 giorni prima** dell'installazione. L'adesione vale 15 anni e quella di rinnovo va presentata almeno 45 giorni prima della scadenza. La presenza di impianti non compresi nel regime generale può richiedere il regime ordinario. Nel confronto aggrega gli impianti della medesima categoria presenti nello stabilimento: frammentare una linea produttiva non consente di aggirare la soglia.''')
save(p,t)

p,t=get(5);t=t.replace('\u00ad','')
t=add(t,5,1,'''### Qualità del corpo idrico e pianificazione

Il limite imposto a uno scarico riguarda la pressione esercitata da quella fonte; lo stato del corpo idrico riguarda la qualità complessiva del recettore. Molti scarichi singolarmente conformi possono concorrere a una pressione cumulativa che richiede misure di pianificazione. Per le acque superficiali si distinguono stato ecologico e chimico; per le sotterranee stato quantitativo e chimico, secondo la disciplina di classificazione applicabile.

Il piano di gestione del distretto idrografico, art. 117, costituisce articolazione del piano di bacino e coordina obiettivi e misure alla scala del distretto. Il piano regionale di tutela delle acque, art. 121, organizza tutela qualitativa e quantitativa, priorità, interventi, verifica dell'efficacia e risorse. Entrambi seguono cicli di aggiornamento sessennali. Il titolo del singolo scarico deve inserirsi in questo quadro: il rispetto del limite non rende irrilevante l'obiettivo ambientale del recettore.''')
t=add(t,5,3,'''### Durata, rinnovo e recapiti vietati

Nell'autorizzazione settoriale dell'art. 124 la durata ordinaria è **4 anni**, con richiesta di rinnovo **un anno prima** della scadenza. La domanda tempestiva permette la prosecuzione alle condizioni del titolo precedente fino al nuovo provvedimento; per gli scarichi contenenti le sostanze pericolose dell'art. 108 il rinnovo deve però essere espresso entro sei mesi dalla scadenza, altrimenti lo scarico cessa. L'AUA, quando applicabile, ha invece durata di 15 anni e domanda di rinnovo almeno sei mesi prima: non trasferire i due calendari da un regime all'altro.

Gli scarichi domestici in fognatura sono ammessi nel rispetto dei regolamenti del gestore approvati dall'ente d'ambito; la regola non vale indistintamente per reflui industriali. Salvo diversa disciplina regionale, la domanda settoriale è presentata alla Provincia oppure all'ente di governo dell'ambito se il recapito è in pubblica fognatura; l'art. 124 prevede decisione entro 90 giorni.

L'art. 103 vieta lo scarico sul suolo e negli strati superficiali salvo le eccezioni tipizzate. L'impossibilità tecnica o eccessiva onerosità del recapito in acque superficiali non basta da sola: vanno accertati presupposti e limiti della specifica deroga. L'art. 104 vieta lo scarico diretto in falda e sottosuolo, con deroghe puntuali, per esempio per determinate reiniezioni previa indagine. Una superficie permeabile non è un recettore liberamente utilizzabile.''')
t=add(t,5,4,'''### Caso numerico: solidi sospesi in fognatura

**Dati didattici:** lo scarico industriale S1 è autorizzato in pubblica fognatura con limite di solidi sospesi totali pari a **200 mg/L**. Il valore è coerente con il riferimento della Tabella 3, allegato 5 alla Parte terza, riprodotto nel regolamento del servizio idrico CAP; la relativa colonna per acque superficiali indica **80 mg/L**. Nel caso il titolo non prevede deroghe o limiti diversi e prescrive il campione medio di tre ore; il laboratorio usa il metodo APAT CNR IRSA 2090B, citato nel regolamento, e documenta campione, condizioni e validazione. Il risultato è 240 mg/L, con incertezza estesa dichiarata di 10 mg/L.

**Soluzione:** si confronta 240 con 200, non con 80, perché il recapito assegnato è la fognatura. Lo scostamento è 40 mg/L, pari al 20% del limite. Anche il valore 230 mg/L, ottenuto sottraendo l'incertezza indicata, supera 200; questa osservazione non inventa una regola universale di sottrazione dell'incertezza. Il rapporto applica la regola decisionale pertinente e documenta la non conformità da valutare nel procedimento. Il candidato non può dedurre automaticamente una specifica sanzione senza qualificare norma, condotta e responsabilità.

**Controprova:** se il laboratorio consegnasse un solo campione istantaneo, mentre il titolo del caso richiede una media di tre ore, il dato potrebbe segnalare un'anomalia ma non soddisferebbe automaticamente la prescrizione di campionamento. Prima della conclusione servirebbe chiarire rappresentatività e disciplina del controllo. Il metodo, la durata e il punto fanno parte del giudizio, non sono dettagli accessori.''')
t=t.replace('gli indicatori distinguono perdite idriche, interruzioni, qualità dell\'acqua erogata, adeguatezza del sistema fognario, gestione dei fanghi e qualità dell\'acqua depurata.',"i macro-indicatori sono M0 resilienza idrica, M1 perdite idriche, M2 interruzioni del servizio, M3 qualità dell'acqua erogata, M4 adeguatezza del sistema fognario, M5 smaltimento dei fanghi in discarica e M6 qualità dell'acqua depurata. M0 comprende M0a, relativo alla gestione del servizio idrico, e M0b, riferito alla scala sovraordinata. Il macro-indicatore organizza una valutazione regolatoria che può utilizzare più indicatori semplici: non è sinonimo di singola misura di laboratorio.")
save(p,t)
print('Capitoli 02–05 integrati; revisione ancora in corso.')
