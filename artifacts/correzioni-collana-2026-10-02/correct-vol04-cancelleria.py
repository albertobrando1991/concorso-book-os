from pathlib import Path
import re,json,shutil,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
p=next(B.glob('08-*.md'));t=p.read_text('utf-8');b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
before=hashlib.sha256(p.read_bytes()).hexdigest()
t=t.replace('La finalità non è memorizzare moduli, importi o formule. La finalità è ragionare come un candidato che comprende il lavoro dell’ufficio.','Il capitolo unisce le regole ai controlli del servizio, distinguendo quanto compete alla cancelleria dalle decisioni riservate all’autorità giudiziaria.')
at=t.index('### Fascicolo e archivi')
t=t[:at]+'''### Registri civili e penali: mappa essenziale

Un registro è una raccolta organizzata di dati; un applicativo può gestire più registri. Il numero di ruolo generale identifica una posizione insieme ad anno, ufficio e tipo di registro: «1250/2026» senza queste informazioni può corrispondere a fascicoli diversi. Il ruolo d'udienza è invece l'elenco delle trattazioni fissate per una determinata udienza.

| Sistema o registro | Ambito | Esempio di utilizzo |
|---|---|---|
| SICID — Sistema Informativo Contenzioso Civile Distrettuale | Contenzioso civile, lavoro, volontaria giurisdizione. | Ricerca di una causa contrattuale, aggiornamento dell'udienza e degli eventi. |
| SIECIC — Sistema Informativo per le Esecuzioni Civili Individuali e Concorsuali | Esecuzioni mobiliari, immobiliari, presso terzi e procedure concorsuali. | Individuazione di una procedura esecutiva e dei relativi provvedimenti. |
| SICP — Sistema Informativo della Cognizione Penale | Gestione dei dati della cognizione penale, compresi registri e informazioni sulle misure cautelari. | Collegamento tra notizia di reato, soggetti e successive fasi. |
| SIC — Sistema Informativo del Casellario | Iscrizioni e servizi del casellario. | Certificato secondo titolo del richiedente e contenuti menzionabili: capitolo 10. |

Le sigle non sono intercambiabili. Il Portale Deposito atti Penali è un canale di deposito, non il nome del casellario; un fascicolo visibile nell'applicativo non è per questo liberamente consultabile da qualsiasi dipendente.

| Modello penale | Contenuto essenziale | Distinzione da mantenere |
|---|---|---|
| 21 | Notizie di reato relative a persone note. | L'iscrizione nominativa non è una condanna. |
| 44 | Notizie di reato contro ignoti. | Il fatto può avere rilevanza penale anche se l'autore non è identificato. |
| 45 | Atti non costituenti notizia di reato. | Non è un contenitore alternativo per ritardare indagini su una notizia già delineata. |
| 45-bis | Annotazione preliminare del nome in presenza dell'evidente causa di giustificazione prevista dall'art. 335, comma 1-bis.1. | Disciplina del 2026, distinta dal modello 45; restano le garanzie dell'art. 335-quinquies. |

La scelta giuridica dell'iscrizione è del PM. La segreteria esegue gli adempimenti e aggiorna i dati sulla base delle determinazioni competenti. La circolare dell'11 novembre 2016 descrive i modelli 21, 44 e 45; va letta insieme alle successive modifiche del codice e alla circolare del 7 maggio 2026 sul modello 45-bis. La sua autorizzazione iniziale alla tenuta cartacea fino alla predisposizione dei modelli informatizzati è una regola transitoria, non prova che tutte le sedi usino sempre carta.

### Caso svolto: iscrizione ed errore anagrafico

**Dossier fittizio.** Nel fascicolo civile RG 1250/2026 del Tribunale di Bologna, la citazione notificata il 16 febbraio e depositata il 24 indica la società «Beta Servizi S.r.l.». Il dato acquisito nel registro riporta «Beta Servizi S.p.A.». Il codice fiscale presente nell'atto e quello inserito nel registro coincidono; l'atto originario è corretto. Il 4 maggio il giudice conferma l'udienza del 29 giugno.

| Campo della nota | Compilazione corretta |
|---|---|
| Identificazione | Tribunale di Bologna, contenzioso civile, RG 1250/2026. |
| Errore riscontrato | Forma societaria nel dato di registro diversa da quella dell'atto depositato. |
| Riscontro | Citazione e dati identificativi concordanti; non semplice omonimia. |
| Intervento | Segnalazione e rettifica del dato secondo abilitazioni e procedura dell'ufficio, conservando autore, data, ragione e riferimento documentale. |
| Dati da conservare | Atto originario, data effettiva di deposito e storia degli eventi. |
| Evento successivo | Registrare il decreto del 4 maggio, l'udienza confermata e la comunicazione effettivamente eseguita. |

**Soluzione.** Si corregge il dato trascritto, non la citazione. Non si crea una nuova causa soltanto per correggere la forma societaria e non si sposta la data di iscrizione a quella della rettifica. Se fosse errato il documento della parte o fosse dubbia l'identità, occorrerebbe un diverso percorso: l'operatore non riscriverebbe l'atto per renderlo coerente con il registro.

**Variante penale.** Un procedimento iscritto contro ignoti riceve una nuova informativa che identifica l'autore. Il personale sottopone l'atto al PM e cura gli aggiornamenti disposti, collegando i riferimenti precedenti; non decide da sé il passaggio di registro e non cancella la precedente cronologia. Il capitolo 7 illustra effetti e garanzie dell'iscrizione nominativa.

''' +t[at:]
t=t.replace('cautele ulteriori per dati sensibili, riservatezza','cautele ulteriori per dati relativi a reati, eventuali categorie particolari di dati, riservatezza')
t=t.replace('dati spesso sensibili e limiti collegati alla fase e al rito','dati personali di diversa natura e limiti collegati alla fase e al rito')
t=t.replace('Indagini, persona offesa, imputato, misure, dati sensibili','Indagini, persona offesa, imputato, misure e possibili dati relativi alla salute')
t=t.replace('una copia attestata conforme all\'originale: non prevede più','una copia attestata conforme all\'originale o un duplicato informatico: non prevede più')
t=t.replace('Copia attestata conforme all\'originale richiesta dall\'art. 475 c.p.c.','Copia attestata conforme all\'originale o duplicato informatico previsti dall\'art. 475 c.p.c.')
t=t.replace('Semplice, autentico, esecutivo, digitale','Copia semplice, copia conforme o duplicato informatico nei casi previsti')
t=t.replace('riproduzione semplice, autentica o esecutiva','riproduzione semplice o con attestazione di conformità; per il titolo, anche duplicato informatico nei casi previsti')
at=t.index('### Certificazioni e attestazioni')
t=t[:at]+'''La forma documentale non basta a creare un titolo esecutivo. Un duplicato informatico di un provvedimento privo di efficacia esecutiva non consente per questo di iniziare un pignoramento. Il capitolo 11, nella parte dedicata a titolo e precetto, collega l'art. 475 ai presupposti dell'esecuzione. Quando il documento è un duplicato informatico, va mantenuta la distinzione dalla copia attestata conforme: sono le due alternative contemplate dalla disposizione.

''' +t[at:]
at=t.index('### Servizi digitali e cancelleria')
t=t[:at]+'''### Accesso processuale: due discipline da applicare

Nel civile, l'**art. 76 delle disposizioni di attuazione del c.p.c.** consente alle parti e ai difensori muniti di procura di esaminare atti e documenti nei fascicoli cartacei dell'ufficio e delle altre parti e di ottenerne copia, osservando le disposizioni sui diritti. L'accesso al fascicolo informatico segue limiti e modalità della normativa sul processo telematico. Identità, procura e relazione con il procedimento devono essere verificate: le credenziali professionali da sole non dimostrano che il difensore sia incaricato in quella causa.

Nel penale, l'**art. 116 c.p.p.** consente a chiunque vi abbia interesse di chiedere, a proprie spese, copie, estratti o certificati di singoli atti, durante il procedimento e dopo la definizione. Decide il PM o il giudice che procede al momento della domanda; dopo la definizione, il presidente del collegio o il giudice che ha emesso l'archiviazione o la sentenza. Non è quindi un'autorizzazione generalizzata alla cancelleria a consegnare l'intero fascicolo a ogni terzo.

La richiesta individua atto e interesse; l'ufficio verifica dati, fase, competenza e limiti e la sottopone all'autorità competente quando occorre. Il rilascio della copia **non elimina il divieto di pubblicazione** dell'art. 114. Le copie delle intercettazioni non pubblicabili ai sensi del comma 2-bis incontrano inoltre la specifica restrizione dell'art. 116 per soggetti diversi dalle parti e dai difensori, salvo la richiesta motivata per l'utilizzo in altro procedimento specificamente indicato.

| Richiesta | Regola di riferimento | Esito del controllo |
|---|---|---|
| Difensore costituito chiede copia della sentenza civile | Art. 76 disp. att. c.p.c. | Verifica procura, procedimento, atto, forma della copia e diritti. |
| Terzo chiede un singolo atto penale per tutelare un proprio diritto | Art. 116 c.p.p. | Identificazione e motivazione; valutazione dell'autorità competente e limiti specifici. |
| Persona offesa chiede se il suo procedimento sia iscritto e a che punto sia | Art. 335 c.p.p., nei suoi presupposti | Non sostituire automaticamente la richiesta con una copia integrale degli atti di indagine. |
| Richiesta su acquisti o gestione amministrativa del Ministero | Disciplina amministrativa pertinente | Non confondere l'atto amministrativo con un atto del fascicolo processuale. |

### Categorie di dati e disciplina applicabile

La parola «sensibile», usata genericamente, non basta per una risposta corretta. Nel campo del GDPR, le **categorie particolari dell'art. 9** comprendono, per esempio, salute, convinzioni religiose, opinioni politiche, dati genetici e biometrici per identificazione univoca. I **dati relativi a condanne penali, reati e connesse misure di sicurezza** sono invece regolati dall'art. 10. Un certificato penale e una perizia medica possono essere entrambi riservati, ma non appartengono per questo alla stessa categoria normativa.

L'art. 9 prevede condizioni che consentono il trattamento, tra cui la necessità di accertare, esercitare o difendere un diritto in giudizio e l'esercizio delle funzioni giurisdizionali. L'art. 10 richiede il controllo dell'autorità pubblica o un'autorizzazione normativa con garanzie. Non si chiede un consenso universale come se fosse il presupposto di ogni atto giudiziario.

Per i trattamenti svolti dalle **autorità competenti per finalità di prevenzione, indagine, accertamento e perseguimento di reati o esecuzione di sanzioni penali**, la disciplina specifica è il **D.Lgs. 51/2018**, attuativo della direttiva UE 2016/680. Conta la combinazione tra autorità e finalità: il fatto che un documento sia conservato in un ufficio giudiziario non sottrae automaticamente al GDPR ogni trattamento amministrativo. La gestione ordinaria del personale e il trattamento per un'indagine penale richiedono un inquadramento distinto.

Il D.Lgs. 51 richiede, tra l'altro, dati pertinenti, non eccedenti, esatti, aggiornati e protetti; per le categorie particolari l'art. 7 impone stretta necessità e adeguate garanzie nelle condizioni previste. Sul piano operativo: si consulta ciò che serve al compito, si corregge l'inesattezza con procedura tracciata, si usano i canali consentiti e si evita di estrarre copie personali del fascicolo. Riservatezza non significa negare ogni accesso legittimo; efficienza non significa comunicare senza titolo.

### Laboratorio: tre richieste, tre risposte

**Dati fittizi.** Il 6 ottobre 2026 arrivano tre richieste: R1, avvocata della parte convenuta con procura presente nel fascicolo civile, chiede copia conforme di un'ordinanza; R2, un vicino dell'indagato, chiede «tutto quello che avete» per curiosità; R3, un terzo indica un preciso verbale penale e motiva la necessità di usarlo in una controversia individuata. Per R3 il procedimento è in fase dibattimentale e l'atto non riguarda intercettazioni; non è ancora intervenuta autorizzazione.

| Richiesta | Risposta lavorata |
|---|---|
| R1 | Verificati identità, procura e atto, si applica l'art. 76 e si gestisce la copia con forma e diritti pertinenti. Il documento non si qualifica come titolo esecutivo senza verificarne natura ed effetti. |
| R2 | La sola curiosità non dimostra un titolo al rilascio. Si spiega la necessità di una richiesta individuata e giuridicamente pertinente, senza rivelare il contenuto degli atti. |
| R3 | Si acquisiscono domanda, identità, atto e motivazione; si sottopone la richiesta al giudice che procede ai sensi dell'art. 116. Il personale non anticipa l'autorizzazione. |

**Nota di servizio per R3.** «Richiesta del 6 ottobre, documento individuato, interesse dichiarato all'utilizzo nella controversia specificata. Procedimento in fase dibattimentale. Istanza trasmessa al giudice procedente per decisione ex art. 116 c.p.p.; nessuna copia rilasciata prima del provvedimento. In caso di autorizzazione, rilascio nei limiti disposti e con tracciamento; restano i divieti di pubblicazione applicabili».

**Autovalutazione.** Cinque controlli, due punti ciascuno: corretta identità/procura per R1, assenza di automatismo esecutivo, diniego di divulgazione per curiosità, individuazione del giudice competente per R3, distinzione copia/pubblicazione. Un punto per un controllo corretto ma non spiegato. La risposta che consegna R3 prima della decisione va rielaborata anche se il totale degli altri punti è alto.

''' +t[at:]
at=t.index('### Punti di controllo del servizio di cancelleria')
t=t[:at]+'''La distinzione funzionale non va trasformata in un divieto assoluto collegato alla sola qualifica. Gli artt. 5–6 del D.Lgs. 151/2022, nel testo verificato al 3 ottobre 2026, prevedono per il personale dell'art. 4, comma 1, lettera f, anche attività di cancelleria **in via residuale**, oltre ai compiti specifici e contrattuali. Occorre verificare mansioni, attribuzione concreta e competenza: ciò non conferisce a ogni addetto un generale potere di decidere sull'accesso o di certificare qualsiasi dato.

''' +t[at:]
t=re.sub(r'### Quiz commentato\n.*?(?=### Checklist di ripasso)', '''### Quiz commentato

1. **In quale ambito si colloca SIECIC?**
   - A. Esecuzioni civili individuali e procedure concorsuali.
   - B. Certificazioni del casellario giudiziale.
   - C. Deposito degli atti di indagine penale.
   **Risposta corretta: A.** È distinto da SICID, da SIC e dai canali di deposito penale; il nome dell'applicativo non sostituisce il tipo di registro.

2. **Il modello 45-bis è equivalente al modello 45?**
   - A. Sì, cambia soltanto la modalità cartacea o digitale.
   - B. Sì, entrambi attestano che il giudice ha archiviato.
   - C. No: il 45-bis riguarda l'annotazione preliminare prevista dall'art. 335, comma 1-bis.1.
   **Risposta corretta: C.** Il modello 45 riguarda atti non costituenti notizia di reato; l'annotazione preliminare del 2026 ha presupposti e garanzie specifici.

3. **L'art. 475 c.p.c. vigente, salvo diversa disposizione, prevede quale forma documentale?**
   - A. Sempre una copia con la tradizionale formula esecutiva.
   - B. Copia attestata conforme all'originale o duplicato informatico.
   - C. Una qualsiasi stampa, purché il richiedente dichiari che gli serve per eseguire.
   **Risposta corretta: B.** La formula tradizionale non è richiesta; la forma della copia non sostituisce la verifica dell'efficacia esecutiva del titolo.

4. **Un terzo presenta una richiesta motivata di copia di un atto penale ex art. 116 durante il dibattimento. Chi decide?**
   - A. Il giudice che procede, secondo la norma e i limiti applicabili.
   - B. Sempre il dirigente amministrativo, senza coinvolgere il giudice.
   - C. Il sistema informatico, se trova il documento.
   **Risposta corretta: A.** L'ufficio istruisce e attua il rilascio consentito; la disponibilità tecnica dell'atto non vale come autorizzazione.

5. **Nel campo GDPR, una condanna penale è per questo solo una categoria particolare dell'art. 9?**
   - A. Sì, ogni dato riservato appartiene all'art. 9.
   - B. Sì, ma soltanto se comunicato a un datore di lavoro.
   - C. No: condanne, reati e connesse misure di sicurezza sono disciplinati dall'art. 10.
   **Risposta corretta: C.** La riservatezza non elimina la distinzione normativa; una perizia sanitaria può contenere anche dati dell'art. 9.

6. **Quando rileva il D.Lgs. 51/2018?**
   - A. Per qualsiasi trattamento effettuato dentro un edificio giudiziario.
   - B. Per i trattamenti delle autorità competenti diretti alle finalità penali e di sicurezza pubblica previste dal decreto.
   - C. Soltanto se l'interessato ha prestato consenso scritto.
   **Risposta corretta: B.** Si verificano autorità e finalità del trattamento; non basta la collocazione del documento e non serve un consenso universale.

''',t,flags=re.S)
for s in ['vol-04-cancelleria-verifica-2026-10-03','vol-04-processo-penale-verifica-2026-10-03','vol-04-organizzazione-upp-verifica-2026-10-03']:
 t=t.replace('source_refs: [',f'source_refs: [\n  "sources/{s}.md",',1).replace('last_compiled_from: [',f'last_compiled_from: [\n  "wiki/sources/{s}.md",',1)
t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true')
p.write_text(t,'utf-8')
keys=re.findall(r'Risposta corretta: ([ABC])',t);assert keys==list('ACBACB')
assert 'o esecutiva' not in t
(A/'VOL-04-cancelleria-delta.json').write_text(json.dumps({'path':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'quizKeys':keys,'reviewRequired':True},indent=2),'utf-8')
print('Capitolo08 integrato; 6quiz controllati')
