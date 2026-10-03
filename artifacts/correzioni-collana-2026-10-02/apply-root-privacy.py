import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
ref='sources/vol-01-accesso-privacy-correzioni-2026-10-03.md';u.REF=ref
for topic in ['anticorruzione-e-trasparenza','privacy-e-protezione-dati']:
 p=Path('wiki/topics')/(topic+'.md')
 assert p.exists(),p
 with p.open('a',encoding='utf8') as f:f.write('\n\n## Accesso e privacy — correzioni del 3 ottobre 2026\n\n[[sources/vol-01-accesso-privacy-correzioni-2026-10-03]] consolida termini FOIA e diritti GDPR, limiti tipizzati, canali whistleblowing, data breach e DPIA. Applicazione nei capitoli 7 e 10 del base, con casi risolti e distinzione tra accesso e pubblicazione sanitaria.\n')
s='trasparenza-anticorruzione-privacy';t=u.read(s)
a=t.index('Per i concorsi è utile conoscere la sequenza minima,');b=t.index('\nIl registro degli accessi',a)
t=t[:a]+'''L’istanza identifica i dati o documenti richiesti e non richiede motivazione. L’ufficio verifica se li detiene, individua eventuali controinteressati e applica i limiti dell’art. 5-bis. La decisione è espressa e motivata: il silenzio non vale come diniego tacito.

| Passaggio | Termine e decorrenza |
|---|---|
| Decisione sull’istanza | Entro 30 giorni dalla presentazione, con comunicazione al richiedente e agli eventuali controinteressati. |
| Opposizione dei controinteressati | Entro 10 giorni dalla ricezione della comunicazione; il termine del procedimento è sospeso secondo l’art. 5, comma 5. |
| Rilascio nonostante opposizione | Salva comprovata indifferibilità, non prima di 15 giorni dalla ricezione della comunicazione di accoglimento da parte del controinteressato. |
| Riesame del RPCT | Decisione motivata entro 20 giorni dalla richiesta nei casi previsti di diniego o mancata risposta. |
| Parere del Garante nel riesame per limiti privacy | Entro 10 giorni dalla richiesta: il termine del RPCT resta sospeso fino al parere e comunque non oltre 10 giorni. |

Il controinteressato non ha un potere di veto: la sua opposizione richiede una valutazione dell’ufficio. Contro la decisione è prevista la tutela davanti al TAR secondo l’art. 116 del Codice del processo amministrativo. Per atti di Regioni ed enti locali è previsto anche il ricorso al difensore civico territorialmente competente, ove costituito, secondo l’art. 5, comma 8.

**Caso:** un’associazione domanda dati aggregati sulle spese di un servizio. L’ufficio non risponde in 30 giorni e non risultano sospensioni. Non si presume un diniego: l’associazione può chiedere riesame al RPCT, che deve decidere entro 20 giorni. Se invece sono presenti controinteressati, ricostruisci le date delle comunicazioni prima di calcolare il termine.
''' +t[b:]
t=u.replace(t,'Tra gli interessi pubblici da proteggere possono rientrare:', 'L’art. 5-bis, comma 1, individua questi interessi pubblici:')
t=u.replace(t,'- politica e stabilità economico-finanziaria;\n- conduzione di indagini e attività ispettive;\n- regolare svolgimento di procedimenti sensibili.', '- politica e stabilità finanziaria ed economica dello Stato;\n- conduzione di indagini sui reati e loro perseguimento;\n- regolare svolgimento delle attività ispettive.')
t=u.replace(t,'Tra gli interessi privati possono rientrare:', 'Il comma 2 tutela i seguenti interessi privati:')
t=u.replace(t,'| Protezione dati | Non basta dire “privacy”: bisogna valutare pertinenza, necessità, minimizzazione e possibile oscuramento. | Bilanciamento caso per caso. |', '''
La protezione dei dati personali rientra nei limiti relativi del comma 2, salvo gli specifici divieti di conoscibilità stabiliti dalla legge. Non costituisce una terza categoria autonoma. Non basta definire una pratica “sensibile”: occorre indicare l’interesse tipizzato e il pregiudizio concreto. Il differimento si usa quando basta una limitazione temporanea; l’oscuramento quando la parte restante è ostensibile.''')
t=t.replace('Alla data dell’audit P4, il PNA 2025 e’ stato','Il PNA 2025 è stato')
t=u.replace(t,'- possono esistere canali interni all’amministrazione;', '- le amministrazioni pubbliche devono attivare canali interni conformi al D.Lgs. 24/2023, con tutela della riservatezza;')
anchor='Nel capitolo sul pubblico impiego hai visto il lato del dipendente. Qui devi memorizzare la funzione sistemica: il whistleblowing è una misura di prevenzione e controllo.'
t=u.replace(t,anchor,'''La tutela riguarda le persone individuate dal decreto nel contesto lavorativo, anche in situazioni anteriori o successive al rapporto alle condizioni previste. Non coincide con il reclamo dell’utente né con una controversia esclusivamente personale sul proprio rapporto di lavoro.

**Canale interno:** il gestore rilascia avviso di ricevimento entro **7 giorni** e fornisce riscontro entro **3 mesi** dall’avviso; se questo manca, i tre mesi decorrono dalla scadenza dei sette giorni dalla presentazione. Il riscontro informa sul seguito dato o previsto: non significa che l’intera indagine debba essere già conclusa.

**Canale esterno ANAC:** è utilizzabile quando ricorre almeno una condizione dell’art. 6: canale interno non previsto, non attivo o non conforme; precedente segnalazione interna rimasta senza seguito; fondati motivi di temere inefficacia o ritorsioni; fondato motivo di ritenere la violazione un pericolo imminente o palese per l’interesse pubblico. Non è necessario tentare prima il canale interno se ricorre un’altra di queste condizioni.

La **divulgazione pubblica**, per esempio tramite stampa, ha le ulteriori condizioni dell’art. 15: mancato riscontro nei percorsi previsti, pericolo imminente o palese, oppure specifici rischi di ritorsione o inefficacia del canale esterno. Non è una scelta liberamente equivalente alla segnalazione interna. Resta distinta la denuncia all’autorità giudiziaria o contabile.

**Caso:** una lavoratrice ha fondati elementi di ritenere che la segnalazione interna provocherebbe ritorsioni. Può ricorrere direttamente ad ANAC alle condizioni del decreto; non deve prima esporsi al rischio per poter accedere al canale esterno. La tutela presuppone ragionevoli motivi di ritenere vere e pertinenti le informazioni, non la prova definitiva dell’illecito.''')
t=u.replace(t,'- legittimo interesse, nei casi in cui è applicabile.', '- legittimo interesse, che non si applica al trattamento effettuato dalle autorità pubbliche nell’esecuzione dei loro compiti.')
anchor='Nel contesto PA, questi dati possono comparire in procedimenti sociali, sanitari, scolastici, disciplinari, concorsuali, di polizia amministrativa o di gestione del personale. La regola pratica è minimizzare: usare e pubblicare solo ciò che è necessario e consentito.'
t=u.replace(t,anchor,'''Nel contesto PA, questi dati possono comparire in procedimenti sociali, sanitari, scolastici, disciplinari, concorsuali o di gestione del personale. Occorrono le condizioni dell’art. 9 GDPR, oltre alla base giuridica generale; per condanne e reati opera l’art. 10.

**Divieto da ricordare:** dati genetici e relativi alla salute non possono essere diffusi, ai sensi dell’art. 2-septies, comma 8, del Codice privacy. Non basta considerarli “utili alla trasparenza”. Inoltre, l’art. 26, comma 4, del D.Lgs. 33/2013 esclude la pubblicazione degli identificativi dei beneficiari di aiuti quando se ne possano ricavare salute o disagio economico-sociale. La necessità di trattare un dato nel fascicolo non autorizza la sua pubblicazione online.''')
anchor='Questi diritti non sono assoluti. Possono incontrare limiti previsti dalla legge quando sono coinvolti interessi pubblici, obblighi normativi, sicurezza, controlli o altre esigenze legittime.'
t=u.replace(t,anchor,anchor+'''

Il titolare risponde **senza ingiustificato ritardo e comunque entro un mese** dalla richiesta. Può prorogare di altri **due mesi** se necessario per complessità o numero delle richieste, ma deve comunicarlo motivatamente entro il primo mese. Anche il mancato accoglimento va comunicato con motivi e rimedi. L’esercizio è normalmente gratuito; richieste manifestamente infondate o eccessive seguono le eccezioni dell’art. 12.

La portabilità riguarda dati forniti dall’interessato, trattati automaticamente sulla base di consenso o contratto; non opera per il trattamento necessario a un compito pubblico. La cancellazione non impone di eliminare atti che devono essere conservati per obbligo legale o compito pubblico, alle condizioni dell’art. 17. **Pseudonimizzare** sostituisce gli identificativi mantenendo una possibile riconduzione alla persona: i dati restano personali. **Anonimizzare** richiede invece che la persona non sia più identificabile con i mezzi ragionevolmente utilizzabili.''')
anchor='### 19. Comunicazione, diffusione e trasferimento dati'
t=u.replace(t,anchor,'''#### Data breach: tre obblighi da distinguere

| Obbligo | Presupposto e tempo |
|---|---|
| Documentare | Il titolare documenta ogni violazione, effetti e rimedi, anche se non la notifica. |
| Notificare al Garante | Senza ingiustificato ritardo e, ove possibile, entro 72 ore dalla conoscenza, salvo che sia improbabile un rischio per diritti e libertà. Se tardiva, si indicano i motivi. |
| Comunicare agli interessati | Senza ingiustificato ritardo quando il rischio è elevato, salve le eccezioni dell’art. 34, par. 3. |

Il responsabile del trattamento avvisa il titolare senza ingiustificato ritardo. Non attende che il DPO “autorizzi” la segnalazione. La notifica può essere completata per fasi alle condizioni dell’art. 33: la mancanza iniziale di ogni dettaglio non giustifica l’inerzia. Le eccezioni alla comunicazione individuale riguardano, per esempio, misure che rendono i dati incomprensibili ai non autorizzati, misure successive che eliminano la probabilità del rischio elevato o sforzi sproporzionati, nel qual caso occorre una comunicazione pubblica o misura equivalente efficace.

**Caso:** lunedì alle 10 il titolare viene a conoscenza dell’invio a un destinatario estraneo di un elenco nominativo con diagnosi. Attiva subito contenimento e valutazione; se la notifica è dovuta, il riferimento delle 72 ore è giovedì alle 10, senza trasformarlo in un tempo da attendere. Valuta separatamente la comunicazione agli interessati in base al rischio elevato e documenta le decisioni.

#### DPIA: valutare prima di iniziare

La valutazione d’impatto è preventiva quando un trattamento può presentare un rischio elevato. L’art. 35 la richiede in particolare per valutazioni sistematiche e globali automatizzate con decisioni di effetto giuridico o analogamente significativo, trattamento su larga scala di categorie particolari o dati penali, sorveglianza sistematica su larga scala di zone accessibili al pubblico. Vanno considerate anche le liste dell’autorità e le condizioni normative applicabili.

La DPIA descrive trattamento e finalità, verifica necessità e proporzionalità, valuta i rischi e indica misure e garanzie. Il titolare consulta il DPO se designato; se rimane un rischio elevato non attenuato, consulta preventivamente il Garante ai sensi dell’art. 36. Non basta redigere il documento dopo aver avviato il trattamento.

'''+anchor)
t=u.replace(t,'Terzo passaggio: valutare privacy e dati particolari. Dati sanitari, condizioni familiari e informazioni idonee a rivelare fragilità personali richiedono cautele rafforzate.', 'Terzo passaggio: applicare i divieti specifici. Le diagnosi non vanno diffuse online; per gli aiuti, gli identificativi che rivelano salute o disagio economico-sociale non sono pubblicabili ai sensi dell’art. 26, comma 4. Nell’accesso generalizzato valuta i limiti dell’art. 5-bis e impedisci che anche dettagli indiretti rendano identificabili le persone protette.')
t=u.replace(t,'| Un ufficio pubblica online graduatorie con dati sanitari non necessari. | Problema privacy/trasparenza. | Minimizzazione, oscuramento, base normativa. |', '| Un ufficio pubblica online una graduatoria con diagnosi dei candidati. | Illecita diffusione di dati sanitari. | Rimuovere i dati dalla pubblicazione e valutare la violazione; la presunta utilità non supera il divieto. |')
t=u.replace(t,'## Checkpoint finale','''### Verifica applicativa

1. **L’opposizione di un controinteressato blocca sempre il FOIA?** No: decide l’ufficio, motivando e rispettando le garanzie e i termini di rilascio.
2. **Il riscontro a un diritto GDPR deve sempre arrivare in 30 giorni?** La norma parla di un mese, con possibile proroga motivata di altri due: non sostituire automaticamente mese e trenta giorni.
3. **Ogni data breach deve essere notificato?** Tutti vanno documentati; la notifica segue il criterio di rischio dell’art. 33.
4. **La DPIA può essere rinviata dopo l’avvio per recuperare tempo?** No, quando dovuta precede il trattamento.
5. **Il nome di un beneficiario può essere pubblicato insieme alla diagnosi che giustifica l’aiuto?** No: opera il divieto di diffusione sanitaria e la tutela specifica dell’art. 26, comma 4.
6. **Il canale interno pubblico è facoltativo?** No; l’accesso diretto al canale esterno resta possibile nelle condizioni dell’art. 6.

## Checkpoint finale''')
u.save(s,t,['V01-16','V01-17','V01-18','V01-49'],ref)
s='informatica-pa-digitale-competenze-digitali';t=u.read(s)
anchor='### Data breach';a=t.index(anchor);b=t.index('\n### ',a+len(anchor))
section=t[a:b]
section+='''

Il titolare documenta ogni violazione e, salvo improbabilità del rischio per le persone, la notifica senza ingiustificato ritardo e ove possibile entro **72 ore dalla conoscenza**. La comunicazione agli interessati segue il distinto criterio del rischio elevato. Per presupposti, eccezioni, ruoli e caso con calcolo del termine, riprendi il Capitolo 7, sezione **«Data breach: tre obblighi da distinguere»**; per la valutazione preventiva, **«DPIA: valutare prima di iniziare»**. Un tecnico deve subito attivare il flusso previsto dall’ente, senza sostituirsi al titolare nelle decisioni giuridiche.
'''
t=t[:a]+section+t[b:];u.save(s,t,['V01-18'],ref)
u.record()
