from pathlib import Path
import re,json,shutil,hashlib,datetime
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
p=next(B.glob('06-*.md'));t=p.read_text('utf-8');b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
before=hashlib.sha256(p.read_bytes()).hexdigest()
t=t.replace('In questo capitolo fissiamo la grammatica operativa; le indicazioni puntuali vanno controllate alla data del bando e della prova.','Le regole che seguono sono verificate al 3 ottobre 2026: per i procedimenti concreti occorre identificare anche il regime temporale applicabile, senza trasferire automaticamente la disciplina attuale alle cause più risalenti.')
t=t.replace("Il processo civile entra nell'ufficio attraverso un atto introduttivo. A seconda del rito, può assumere forme diverse, ma per il candidato M-FC04 il punto non è recitare tutte le differenze. Il punto è capire che l'atto introduttivo mette in moto un flusso.","L'atto introduttivo identifica parti, domanda, fatti, ragioni e richieste. Nella cognizione ordinaria la citazione è prima notificata al convenuto e indica l'udienza; l'attore poi si costituisce iscrivendo la causa a ruolo. Nei procedimenti introdotti con ricorso, invece, il ricorso è depositato e il giudice fissa l'udienza: ricorso e decreto vengono quindi notificati secondo il rito. Non invertire le due sequenze.")
start=t.index('Il capitolo non inserisce un elenco numerico di termini.');end=t.index('### Processo civile telematico',start)
t=t[:start]+'''### Cognizione ordinaria: costituzione e verifiche preliminari

Le seguenti regole riguardano il rito ordinario attuale davanti al tribunale. Tra notificazione della citazione e udienza devono intercorrere almeno **120 giorni liberi** se la notifica avviene in Italia, **150** se all'estero (art. 163-bis c.p.c.). Nei termini liberi non si contano né il giorno iniziale né quello finale. L'attore si costituisce entro dieci giorni dalla notificazione (art. 165); il convenuto almeno settanta giorni prima dell'udienza (art. 166).

La comparsa di risposta non è una presenza puramente formale: il convenuto espone le difese, prende posizione in modo chiaro e specifico sui fatti, indica prove e documenti e formula le conclusioni. Deve proporre tempestivamente, a pena di decadenza, le domande riconvenzionali e le eccezioni processuali e di merito che non sono rilevabili d'ufficio. La domanda riconvenzionale è una domanda del convenuto contro l'attore; la semplice contestazione della domanda avversaria non coincide con essa. La chiamata del terzo richiede la dichiarazione e gli adempimenti previsti dal codice.

Scaduto il termine per il convenuto, il giudice compie entro i successivi quindici giorni le **verifiche preliminari** dell'art. 171-bis: controlla d'ufficio la regolarità del contraddittorio. Se occorrono i provvedimenti indicati dalla norma, fissa una nuova udienza e procede nuovamente alle verifiche almeno cinquantacinque giorni prima. Altrimenti conferma l'udienza o la differisce fino a quarantacinque giorni, segnalando le questioni rilevabili d'ufficio da trattare, anche sulle condizioni di procedibilità. Se ricorrono i presupposti per tutte le domande, può disporre il passaggio al rito semplificato.

Il giudice provvede con decreto comunicato dalla cancelleria alle parti costituite. Nel testo vigente, i termini delle memorie integrative **iniziano a decorrere quando è pronunciato il decreto previsto dal terzo comma dell'art. 171-bis** e si computano rispetto all'udienza di riferimento. Una scheda che riporti soltanto «meno 40, meno 20, meno 10» senza verificare decreto e udienza è incompleta.

| Memoria ex art. 171-ter | Termine prima dell'udienza | Contenuto essenziale |
|---|---|---|
| Prima | Almeno 40 giorni | Domande ed eccezioni conseguenti alle difese indicate dalla norma; precisazione o modifica delle domande, eccezioni e conclusioni già proposte. |
| Seconda | Almeno 20 giorni | Repliche alle novità avverse, eccezioni conseguenti, indicazione delle prove e produzioni documentali. |
| Terza | Almeno 10 giorni | Repliche alle eccezioni nuove e indicazione della prova contraria. |

Le attività sono soggette alle decadenze previste dal codice. La cancelleria registra depositi e dati; l'UPP può ricostruire la sequenza e segnalare criticità; l'accertamento di una decadenza contestata compete al giudice. Accettazione tecnica del deposito e ammissibilità processuale non sono la stessa valutazione.

### Prima udienza e calendario istruttorio

All'udienza dell'art. 183 le parti devono comparire personalmente; l'assenza senza giustificato motivo è comportamento valutabile dal giudice. Il giudice richiede chiarimenti sui fatti allegati e tenta la conciliazione; adotta poi i provvedimenti consentiti dallo stato della causa. Quando procede sulle richieste istruttorie, predispone il calendario delle udienze successive, inclusa quella di rimessione in decisione. L'udienza per assumere le prove ammesse è fissata entro novanta giorni; se l'ordinanza è emessa fuori udienza, è pronunciata entro trenta giorni.

La scheda preparatoria deve quindi distinguere: fatti allegati, fatti contestati, documenti, richieste di prova e questioni da trattare. Un documento presente nel fascicolo non prova automaticamente ogni affermazione della parte che lo produce; una richiesta di prova non è ancora una prova ammessa.

### Computo: giorni liberi, sabato e sospensione

L'art. 155 esclude il giorno iniziale nei termini a giorni; i festivi intermedi si contano. Per un termine in avanti, la scadenza festiva slitta al primo giorno successivo non festivo; lo stesso vale per il sabato quando l'atto processuale si compie fuori udienza. Il sabato non diventa per questo festivo per ogni attività giudiziaria.

Per un termine **a ritroso** occorre conservare l'intervallo minimo prima dell'udienza: se la scadenza cade di sabato o festivo, si anticipa al giorno utile precedente, non si avvicina all'udienza. La regola vale anche per il deposito telematico, come ribadito dalla Cassazione n. 23634/2025. La disponibilità tecnica del sistema nel fine settimana non cambia il calcolo processuale.

La L. 742/1969 sospende ordinariamente i termini dal 1° al 31 agosto, ma prevede eccezioni: non applicare automaticamente la sospensione alle controversie di lavoro o alle altre materie escluse. Prima del calcolo annota rito, evento iniziale, durata, direzione del conteggio, eventuale carattere libero, festività e sospensioni applicabili.

### Caso svolto: calendario di una causa ordinaria

**Dossier fittizio.** Una citazione per una controversia contrattuale davanti a un tribunale diverso da Roma è notificata in Italia il 16 febbraio 2026 e indica l'udienza del 29 giugno 2026. Non vi sono discipline speciali o sospensioni applicabili al periodo. Il convenuto deposita la comparsa il 17 aprile. Il giudice, con decreto del 4 maggio, conferma l'udienza dopo le verifiche preliminari; la cancelleria comunica il decreto il 5 maggio. Occorre predisporre lo scadenzario.

| Controllo | Calcolo e risultato |
|---|---|
| Intervallo per comparire | Tra 16 febbraio e 29 giugno ci sono 132 giorni liberi: il minimo di 120 è rispettato. |
| Costituzione dell'attore | Dieci giorni dalla notifica: 26 febbraio 2026. |
| Costituzione del convenuto | 29 giugno meno 70 giorni: 20 aprile. Il deposito del 17 aprile è tempestivo. |
| Verifiche preliminari | Quindici giorni dopo il 20 aprile: entro 5 maggio. Il decreto del 4 maggio rientra nel termine. |
| Prima memoria | 29 giugno meno 40 giorni: 20 maggio. |
| Seconda memoria | Meno 20 giorni: 9 giugno. |
| Terza memoria | Meno 10 giorni: 19 giugno. |

**Soluzione operativa.** Lo scadenzario registra sia il decreto del 4 maggio sia la sua comunicazione, senza confonderne la funzione. Le tre scadenze si riferiscono all'udienza confermata; nessuna cade di sabato o in un festivo. L'UPP prepara la scheda delle questioni e dei depositi, mentre la cancelleria aggiorna gli eventi di competenza. Se l'udienza cambia, si verifica il nuovo provvedimento e si ricalcolano i termini secondo l'art. 171-bis: non basta sostituire la data dell'udienza lasciando le memorie alle vecchie scadenze.

**Variante da risolvere.** L'udienza di riferimento è lunedì 6 luglio 2026: quando scade la prima memoria? Quaranta giorni prima è mercoledì 27 maggio. Il calcolo va comunque collegato al decreto che fissa o conferma quella udienza; non è una scadenza autonoma dal fascicolo.

''' +t[end:]
start=t.index('### Riti e impugnazioni essenziali');end=t.index('### Esecuzione civile',start)
t=t[:start]+'''### Ordinario, semplificato e lavoro: scegliere il percorso

Il procedimento semplificato di cognizione non è una versione libera del rito ordinario. L'art. 281-decies lo prevede quando i fatti non sono controversi, oppure la domanda è fondata su prova documentale, è di pronta soluzione o richiede istruzione non complessa. Nelle cause monocratiche può essere scelto anche fuori da tali presupposti, ferma la valutazione del giudice sul percorso adeguato.

| Elemento | Semplificato di cognizione | Rito del lavoro |
|---|---|---|
| Ambito | Presupposti dell'art. 281-decies; possibile scelta nelle cause monocratiche. | Controversie dell'art. 409, compreso lavoro pubblico devoluto al giudice ordinario. |
| Avvio | Ricorso; decreto entro 5 giorni dalla designazione del giudice. | Ricorso con fatti, diritto, conclusioni e prove; decreto entro 5 giorni dal deposito. |
| Notifica e udienza | Ricorso e decreto: almeno 40 giorni liberi in Italia, 60 all'estero. | Notifica entro 10 giorni dal decreto; almeno 30 giorni tra notifica e udienza, 40 se all'estero. |
| Convenuto | Costituzione non oltre 10 giorni prima dell'udienza. | Costituzione almeno 10 giorni prima dell'udienza. |
| Difese e prove | Comparsa con contestazioni specifiche, prove e documenti; riconvenzionale ed eccezioni non d'ufficio a pena di decadenza. | Memoria difensiva con contestazioni precise; riconvenzionale, eccezioni non d'ufficio e indicazione delle prove secondo le decadenze dell'art. 416. |

Nel lavoro, tra deposito del ricorso e udienza non devono decorrere più di sessanta giorni, elevati a ottanta per la notifica all'estero. Non confondere questo intervallo con quello minimo tra notifica e udienza. Anche se due riti prevedono una costituzione del convenuto dieci giorni prima, non ne segue che abbiano identici atti e termini.

Nel semplificato, il giudice può disporre il passaggio al rito ordinario secondo l'art. 281-duodecies. Se l'esigenza nasce dalle difese della controparte e vi è richiesta, può concedere fino a venti giorni per le integrazioni previste e ulteriori dieci per repliche e prova contraria. Questi termini non sono tre memorie automatiche 40/20/10: dipendono dalla disciplina del rito e dal provvedimento.

### Sentenza, ordinanza e decreto

| Provvedimento | Caratteri essenziali | Conseguenza per l'ufficio |
|---|---|---|
| Sentenza | Contiene motivazione in fatto e diritto, dispositivo e sottoscrizione secondo l'art. 132. Può decidere il merito o una questione processuale nei casi previsti. | Pubblicazione mediante deposito telematico; comunicazione alle parti costituite ex art. 133. |
| Ordinanza | Succintamente motivata; in udienza inserita nel verbale, fuori udienza su documento separato. | Se fuori udienza viene comunicata, salvo che la legge prescriva notificazione. |
| Decreto | Pronunciato d'ufficio o su istanza; normalmente non motivato, salvo espressa previsione di legge. | Individuare la specifica disciplina, come nel decreto delle verifiche preliminari. |

Non dedurre dalla sola forma che un atto sia sempre definitivo, sempre revocabile o privo di effetti sui termini. Per esempio, l'ordinanza che fissa un calendario e un provvedimento che definisce un particolare procedimento richiedono controlli diversi. La scheda riporta tipo, data, contenuto dispositivo, comunicazione/notificazione e seguito previsto.

### Impugnazioni: termine breve e termine lungo

L'appello consente il riesame nei limiti dei motivi e delle regole del relativo giudizio; il ricorso per cassazione riguarda i vizi ammessi dalla legge e non apre un nuovo libero accertamento del fatto. Prima di calcolare il termine bisogna identificare il rimedio effettivamente consentito.

Per le impugnazioni ordinarie qui considerate, l'art. 325 prevede **30 giorni per l'appello** e **60 per il ricorso per cassazione**. La decorrenza è collegata alla notificazione della sentenza secondo l'art. 326. La comunicazione del deposito da parte della cancelleria, invece, non fa decorrere questi termini brevi: lo precisa l'art. 133.

Indipendentemente dalla notificazione, l'art. 327 prevede il limite di **sei mesi dalla pubblicazione** per appello, cassazione e i motivi di revocazione indicati dalla norma. Restano le eccezioni previste, compresa quella relativa alla parte contumace che dimostri mancata conoscenza del processo per le nullità indicate, oltre alle discipline speciali e alle sospensioni applicabili.

**Esempio.** Sentenza pubblicata e comunicata il 5 marzo 2026, notificata il 10 marzo. Per un appello soggetto al termine ordinario breve, escluso il giorno iniziale, trenta giorni portano al 9 aprile. Partire dal 5 marzo confonderebbe comunicazione e notificazione; ignorare la notifica e usare soltanto sei mesi sarebbe altrettanto errato. Il personale d'ufficio annota i distinti eventi, senza sostituire al giudice la decisione su una contestazione di tempestività.

''' +t[end:]
t=re.sub(r'### Quiz commentato\n.*?(?=### Checklist di ripasso)', '''### Quiz commentato

1. **Nel rito ordinario attuale, quando deve costituirsi il convenuto?**
   - A. Almeno venti giorni prima dell'udienza.
   - B. Almeno settanta giorni prima dell'udienza.
   - C. Entro dieci giorni dalla comunicazione del ruolo.
   **Risposta corretta: B.** L'art. 166 prevede settanta giorni; utilizzare il precedente termine di venti giorni senza verificare il regime temporale produce un errore.

2. **Quale sequenza riguarda le memorie integrative dell'art. 171-ter?**
   - A. 40, 20 e 10 giorni prima dell'udienza, con decorrenza collegata al decreto previsto dall'art. 171-bis.
   - B. 40, 20 e 10 giorni dopo l'udienza, indipendentemente da ogni decreto.
   - C. 30, 20 e 10 giorni dalla notificazione della citazione.
   **Risposta corretta: A.** Il conteggio è a ritroso rispetto all'udienza rilevante; il decreto delle verifiche preliminari deve essere controllato.

3. **Nel procedimento semplificato, quale intervallo minimo libero è previsto tra notifica in Italia e udienza?**
   - A. Trenta giorni.
   - B. Centoventi giorni.
   - C. Quaranta giorni.
   **Risposta corretta: C.** L'art. 281-undecies prevede quaranta giorni liberi, sessanta all'estero; centoventi riguarda la citazione ordinaria in Italia.

4. **La cancelleria comunica il deposito della sentenza. Questa comunicazione fa decorrere il termine breve ordinario per l'appello?**
   - A. Sì, perché equivale alla notificazione della sentenza.
   - B. No, l'art. 133 distingue la comunicazione dall'evento rilevante ai sensi degli artt. 325–326.
   - C. Sì, ma soltanto se avviene con modalità telematica.
   **Risposta corretta: B.** La modalità digitale non elimina la differenza tra i due atti.

5. **Un termine a ritroso per un deposito scade di sabato. Quale criterio conserva l'intervallo minimo?**
   - A. Anticipare al giorno utile precedente.
   - B. Spostare sempre al lunedì successivo.
   - C. Lasciare la scadenza invariata perché il sistema telematico è disponibile.
   **Risposta corretta: A.** Il rinvio in avanti accorcerebbe l'intervallo prima dell'udienza; la Cassazione conferma il criterio anche nel PCT.

6. **Quale affermazione su ordinanza e decreto è corretta?**
   - A. Entrambi sono sempre privi di motivazione.
   - B. Il decreto è sempre motivato e l'ordinanza non lo è mai.
   - C. L'ordinanza è succintamente motivata; il decreto è motivato quando la legge lo prescrive.
   **Risposta corretta: C.** Sono le regole generali degli artt. 134–135, da integrare con la disciplina del singolo provvedimento.

''',t,flags=re.S)
s='vol-04-processo-civile-verifica-2026-10-03'
t=t.replace('source_refs: [',f'source_refs: [\n  "sources/{s}.md",',1).replace('last_compiled_from: [',f'last_compiled_from: [\n  "wiki/sources/{s}.md",',1)
t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true')
p.write_text(t,'utf-8')
d=datetime.date(2026,6,29);assert (d-datetime.date(2026,2,16)).days-1==132
dates={n:(d-datetime.timedelta(days=n)).isoformat() for n in [70,40,20,10]}
assert dates=={70:'2026-04-20',40:'2026-05-20',20:'2026-06-09',10:'2026-06-19'}
assert datetime.date(2026,7,6)-datetime.timedelta(days=40)==datetime.date(2026,5,27)
assert datetime.date(2026,3,10)+datetime.timedelta(days=30)==datetime.date(2026,4,9)
(A/'VOL-04-civile-delta.json').write_text(json.dumps({'path':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'calendarChecked':dates,'quiz':6},indent=2),'utf-8')
print('Capitolo06 integrato; calendario e varianti verificati')
