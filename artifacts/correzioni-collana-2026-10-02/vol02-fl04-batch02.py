from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl04-polizia-locale/chapters');art=Path('artifacts/correzioni-collana-2026-10-02');source='sources/vol-02-pl-pg-verifica-2026-10-03'
p=next(base.glob('07-*.md'));backup=art/'before-fl04'/p.name
if backup.exists():raise RuntimeError('Capitolo 07 già modificato')
t=p.read_text(encoding='utf-8');backup.write_text(t,encoding='utf-8')
def add(anchor,body):
 global t
 assert t.count(anchor)==1,anchor
 t=t.replace(anchor,body.strip()+'\n\n'+anchor)
t=t.replace('nel territorio dell’ente e nei limiti delle attribuzioni.', 'nel territorio dell’ente e nei limiti delle attribuzioni, tenendo conto della condizione di servizio prevista dall’art. 57 c.p.p.')
t=t.replace('L’espressione «senza ritardo» impone di non trattenere la notizia in attesa di un fascicolo perfetto. La gestione concreta della tempestività dipende anche dalle circostanze, dalla natura del fatto e dalle regole applicabili; non va tradotta in un termine inventato. Se intervengono atti urgenti o situazioni particolari, si verificano immediatamente le disposizioni specifiche e le direttive dell’autorità giudiziaria.', '''L'espressione «senza ritardo» impone di non trattenere la notizia in attesa di un fascicolo perfetto. L'art. 347 distingue tre regole:

- **Regola ordinaria:** comunicazione scritta senza ritardo, indicando anche giorno e ora di acquisizione della notizia.
- **Atto al quale il difensore ha diritto di assistere:** comunicazione al più tardi entro quarantotto ore dal compimento dell'atto, salvi i termini speciali. È un limite massimo, non un permesso di aspettare inutilmente.
- **Urgenza o reati indicati dal comma 3:** comunicazione immediata, anche orale, seguita senza ritardo da quella scritta con documentazione. Tra i casi tipizzati rientrano i delitti espressamente richiamati di violenza domestica e sessuale.

**Esempio temporale.** Un accertamento urgente con diritto di assistenza difensiva termina lunedì alle 10: la CNR segue senza ritardo e comunque non oltre mercoledì alle 10, salvo regole più stringenti. Se la situazione è urgente, si comunica immediatamente, anche oralmente: non si attende mercoledì. Il termine della CNR e quelli della convalida di un eventuale sequestro hanno presupposti propri, anche quando corrono contemporaneamente.''')
add('## N-FL04-07-04', '''### Quale atto, quale soggetto, quali garanzie

| Atto | Presupposto e soggetto competente | Garanzie e seguito |
|---|---|---|
| Identificazione, art. 349 | PG identifica indagato e persone utili alle indagini; accompagnamento solo nei presupposti di rifiuto o sospetta falsità previsti dal codice | Tempo strettamente necessario, massimo 12 ore; 24 nelle ipotesi qualificate, previo avviso al PM. Comunicazione immediata dell'accompagnamento e dell'ora, controllo del PM e notizia del rilascio |
| Informazioni dall'indagato, art. 350 | Ufficiale di PG; persona non arrestata, fermata o allontanata ex art. 384-bis | Necessaria assistenza del difensore e avvisi dell'art. 64; le eccezioni non sono un colloquio libero sostitutivo |
| Informazioni da persone informate, art. 351 | PG raccoglie circostanze utili; disciplina particolare per persone indagate in procedimento connesso | Posizione processuale verificata, tutela di minori e vulnerabili, avviso della facoltà di registrazione fonografica |
| Accertamenti e sequestro urgente, art. 354 | Ufficiale di PG: pericolo di alterazione o dispersione; PM non può intervenire tempestivamente o non ha ancora assunto la direzione | Difensore può assistere senza preavviso; avvertimento all'indagato presente; motivazione, verbale, custodia e controllo del PM |
| Convalida del sequestro, art. 355 | Verbale al PM senza ritardo e comunque entro 48 ore | PM nelle 48 ore successive convalida motivatamente oppure dispone restituzione; riesame entro 10 giorni, senza sospensione automatica |

L'accompagnamento per identificazione non coincide con arresto o fermo. Il limite ordinario è di dodici ore e l'attività cessa prima, se l'identificazione è completata. Il prolungamento fino a ventiquattro ore richiede particolare complessità o necessità di interprete o autorità consolare; è preceduto dall'avviso al PM e comporta la facoltà di chiedere che siano avvisati un familiare o un convivente. Il PM può ordinare il rilascio se mancano i presupposti.

L'art. 350 distingue le informazioni assunte con difensore dalle dichiarazioni realmente spontanee. Non si evita l'assistenza chiamando «spontanea» una risposta a domande investigative. Gli avvisi dell'art. 64 riguardano utilizzabilità delle dichiarazioni contro la persona, facoltà di non rispondere salvo l'identificazione e possibile assunzione dell'ufficio di testimone sui fatti altrui, nei limiti del codice. La loro omissione può rendere inutilizzabili le dichiarazioni.

Il comma 5 dell'art. 350, nel testo vigente, consente agli ufficiali informazioni sul luogo o nell'immediatezza anche senza difensore soltanto nelle condizioni tassative: evitare un imminente pericolo per libertà, integrità fisica o vita, oppure impedire una grave compromissione delle indagini. Di queste informazioni il comma 6 vieta documentazione e utilizzazione. Non è una scorciatoia per costruire il verbale d'interrogatorio. Le dichiarazioni spontanee del comma 7 hanno invece una disciplina distinta e limiti di utilizzazione dibattimentale.

Per l'art. 351 la persona informata sui fatti deve essere avvisata della facoltà di ottenere, su richiesta, la registrazione fonografica, salvo contingente indisponibilità degli strumenti o del personale tecnico. Per minori nei reati indicati e persone offese particolarmente vulnerabili si applicano le cautele e l'ausilio dell'esperto nominato dal PM previsti dalla norma. L'art. 357 aggiunge regole di documentazione rafforzata: per dichiarazioni di minori, infermi di mente o persone particolarmente vulnerabili, riproduzione audiovisiva o fonografica integrale, salvo la specifica eccezione di indisponibilità contingente unita a urgenza che impedisce il rinvio.

**Cambio di posizione.** Un testimone, parlando, espone fatti che fanno emergere indizi contro di lui: la PG interrompe l'esame, lo avverte e lo invita a nominare un difensore, ai sensi dell'art. 63. Le dichiarazioni precedenti non sono utilizzabili contro di lui. Se avrebbe dovuto essere sentito come indagato fin dall'inizio, opera la più ampia inutilizzabilità del comma 2. Continuare come se fosse un semplice testimone viola le garanzie.

Nel sequestro urgente si indicano cose, legame con il fatto, pericolo di alterazione o dispersione e ragioni dell'intervento. La copia del verbale va alla persona presso cui il sequestro è eseguito; l'originale segue il termine di trasmissione al PM. L'art. 113 delle disposizioni di attuazione permette anche agli agenti gli atti urgenti indicati negli artt. 352 e 354, commi 2 e 3, **nei casi di particolare necessità e urgenza**: l'eccezione non cancella la distinzione fra agente e ufficiale. Il difensore può assistere senza diritto al preavviso; l'indagato presente va avvisato della facoltà di farsi assistere dal difensore di fiducia, come richiede l'art. 114 delle disposizioni di attuazione.
''')
t=t.replace('Le garanzie difensive non sono formalità da aggiungere alla fine. Alcuni atti richiedono avvisi, assistenza del difensore o modalità particolari; la loro omissione può incidere sull’utilizzabilità o sulla regolarità dell’attività. Il capitolo non elenca formule operative perché esse dipendono dall’atto e dal testo vigente. In prova bisogna però dichiarare che posizione del soggetto e natura dell’atto vanno riconosciute prima di procedere.', 'Le garanzie difensive si applicano prima e durante l’atto, secondo la tabella precedente. Nel verbale non basta scrivere «rispettate le garanzie»: si documentano gli avvertimenti effettivamente dati, la presenza o le modalità di intervento del difensore e gli altri adempimenti richiesti dall’atto concreto.')
add('## ▣ Verifica', '''### Annotazione svolta: primi rilievi e conservazione dei luoghi

**Scenario interamente simulato.** La pattuglia, in servizio nel Comune Alfa, interviene presso un deposito comunale per una porta forzata e beni apparentemente mancanti. Non sono presenti persone sospettate; una custode ha chiesto l'intervento. L'esempio documenta le prime attività, senza sostituire il verbale di informazioni alla custode né un eventuale verbale di sequestro.

**Comune Alfa — Corpo di polizia locale. Annotazione di PG, esercizio didattico n. 7.**

**Oggetto:** intervento presso deposito comunale, via Beta 4. **Operatori:** agente A e agente B, pattuglia in servizio. **Data simulata:** 3 ottobre 2026.

Alle ore 8.15, su segnalazione della centrale, gli scriventi raggiungono il deposito. Alle ore 8.20 osservano la porta esterna socchiusa e una deformazione presso la serratura. La custode C, identificata con documento i cui estremi sono riportati nel fascicolo didattico, riferisce di avere trovato la porta in tale stato e di non avere visto l'autore. Questa circostanza è dichiarata dalla custode, non direttamente osservata dagli operatori.

Gli scriventi delimitano l'accesso per evitare modifiche dei luoghi, documentano la porta e l'esterno con quattro fotografie numerate e chiedono alla centrale il raccordo con il responsabile di servizio per gli accertamenti ulteriori. Non vengono mossi oggetti né raccolte cose senza il pertinente atto. Alle ore 8.35 viene acquisita la notizia del possibile reato; la comunicazione al PM viene predisposta senza ritardo con i fatti disponibili. L'eventuale elenco dei beni mancanti dovrà essere verificato con inventario e informazioni verbalizzate della custode.

**Allegati:** fotografie 1–4 con data, ora e autore; scheda dell'intervento. **Seguito:** CNR e ulteriori atti previsti dal codice, distintamente documentati. **Chiusura:** ore 8.50. **Sottoscrizioni:** agenti A e B.

**Controllo della soluzione.** L'annotazione distingue ciò che gli agenti vedono da ciò che viene riferito, non dichiara già provato il furto e non attribuisce responsabilità. La notizia non aspetta la chiusura dell'inventario. Se si compiono informazioni ex art. 351 o un sequestro, occorrono i rispettivi verbali e garanzie: il titolo «annotazione» non li assorbe.
''')
t=t.replace('Alle ore 8.35 viene acquisita la notizia del possibile reato;','La notizia del possibile reato è acquisita alle ore 8.20; alle ore 8.35 si organizza il seguito documentale e')
# Every existing quiz gets a fourth, distinct and plausible distractor.
ds=['La qualifica dipende esclusivamente dal grado indicato nel regolamento comunale.','trasmettere soltanto dopo l’identificazione dell’autore.','Sono equivalenti quando il destinatario finale è la Procura.','Per applicare le garanzie soltanto dopo la redazione del verbale.','Il procedimento amministrativo resta sempre sospeso fino alla sentenza penale.','riportare come direttamente osservate anche le circostanze riferite da terzi.']
parts=t.split('### Quiz ')
for i in range(1,7):parts[i]=parts[i].replace('\n\n**Risposta corretta:', '\nD. '+ds[i-1]+'\n\n**Risposta corretta:',1)
t='### Quiz '.join(parts)
t=t.replace('- Codice di procedura penale, art. 347 sulla comunicazione della notizia di reato.', '- Codice di procedura penale, artt. 63–64, 347, 349–351 e 354–356: comunicazioni, atti, difesa e controlli.\n- D.Lgs. 271/1989, artt. 113 e 114: urgenza e avviso sul difensore.')
for k,v in [('source_refs',source),('last_compiled_from','wiki/'+source+'.md')]:t=re.sub(r'^'+k+r': \[(.*)\]$',lambda m:k+': ['+m.group(1)+', "'+v+'"]',t,count=1,flags=re.M)
t=re.sub(r'^volume_chapter:.*$','volume_chapter: 41',t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
p.write_text(t,encoding='utf-8')
p5=next(base.glob('05-*.md'));s=p5.read_text(encoding='utf-8').replace('contestata al conducente in servizio il giorno zero','contestata al conducente il giorno zero');p5.write_text(s,encoding='utf-8')
statepath=art/'VOL-02-changes.json';s=json.loads(statepath.read_text(encoding='utf-8'));s['changes']['V02-44']={'files':[p.as_posix()],'change':'Presupposti, soggetti, difesa e termini artt.349/350/351/354/355; CNR ordinaria e urgente; annotazione completa con attività e fonti distinte.','evidence':'Quattordici articoli processuali letti integralmente; tabella e caso temporale 48+48; sei quiz con quattro opzioni.','status':'Applicato; riesame trasversale e gate 15 ancora aperti'};statepath.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('FL04/07 applicato, V02-44')
