from pathlib import Path
import importlib.util,re
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-accesso-rimedi-verifica-2026-10-03.md'
slug='09-rimedi-precontenzioso-contenzioso';t=u.read(slug)
t=t.replace('Costruire una timeline del fascicolo, lasciando da verificare i termini numerici quando dipendono dalla disciplina vigente.','Costruire una timeline del fascicolo applicando termini e decorrenze, senza confondere accesso, ricorso e stipula.')
anchor='## N-TR02-09-02 · Schema operativo'
insert='''### Accesso digitale: chi vede che cosa e quando

Gli artt. 35 e 36 del D.Lgs. 36/2023 rendono l’accesso parte del procedimento digitale. Contestualmente alla comunicazione dell’aggiudicazione, tutti i candidati e offerenti **non definitivamente esclusi** ricevono disponibilità, sulla PAD, dell’offerta dell’aggiudicatario, dei verbali e degli atti, dati e informazioni presupposti all’aggiudicazione. Non occorre presentare ogni volta una domanda per ottenere ciò che la legge rende direttamente disponibile.

Ai primi cinque classificati sono rese reciprocamente disponibili anche le rispettive offerte. Il sesto ha dunque accesso diretto all’offerta vincitrice e agli atti comuni; non beneficia per ciò solo dello scambio automatico di tutte le offerte dei primi cinque. Per documenti ulteriori resta possibile l’accesso nei rispettivi presupposti, anche difensivi. La disponibilità ai partecipanti non coincide con pubblicazione indiscriminata su internet.

Prima dell’aggiudicazione operano i differimenti dell’art. 35: gli elenchi dei partecipanti non sono conoscibili prima della scadenza delle offerte nei casi previsti; domande e requisiti, offerte e valutazioni, verifica dell’anomalia sono differiti fino all’aggiudicazione. Il differimento è temporaneo; l’esclusione dell’accesso protegge invece interessi individuati dalla legge, come determinati pareri legali e relazioni riservate.

L’offerente che invoca un segreto tecnico o commerciale deve motivarlo e provarlo. Una generica dicitura «riservato» sull’intera offerta non basta. La stazione appaltante decide sulle richieste di oscuramento e comunica la decisione insieme all’aggiudicazione. Anche informazioni protette possono essere accessibili al concorrente quando indispensabili per la difesa in giudizio dei suoi interessi relativi alla gara, secondo l’art. 35, comma 5: occorre dimostrare quel nesso, non una generica curiosità commerciale.

### Il termine speciale di dieci giorni

La decisione sull’oscuramento si impugna con il rito dell’art. 116 CPA, secondo la disciplina speciale dell’art. 36: ricorso **notificato e depositato entro 10 giorni** dalla comunicazione digitale dell’aggiudicazione. Gli intimati possono costituirsi entro 10 giorni dalla notifica nei loro confronti; la sentenza semplificata è pubblicata entro 5 giorni dall’udienza. Il rito e i termini speciali valgono anche per le impugnazioni.

Se la stazione appaltante nega la segretezza richiesta, attende la scadenza del termine per impugnare prima di mostrare le parti interessate. Non si deve quindi caricare immediatamente un’offerta integrale ignorando il tempo di tutela del suo autore. Viceversa, l’oscuramento non può impedire l’accesso agli atti estranei al segreto.

**Esempio.** Alfa è seconda, Beta prima e Gamma sesta. Alfa può consultare gli atti comuni e le offerte dei primi cinque nei limiti legali; Gamma vede direttamente l’offerta di Beta e gli atti comuni, ma per l’offerta di Alfa deve far valere il titolo pertinente. Se Alfa contesta l’oscuramento di una parte della soluzione di Beta, il termine speciale è 10 giorni. Se contesta il punteggio e l’aggiudicazione, deve invece presidiare il termine di 30 giorni del rito appalti. Un’istanza di accesso non concede automaticamente altri 30 giorni per impugnare.

'''
t=t.replace(anchor,insert+anchor)
anchor='### Come impostare una nota di precontenzioso'
t=t.replace(anchor,'''### Il parere ANAC dell’art. 220

La stazione appaltante, l’ente concedente o una o più parti possono chiedere ad ANAC un parere su questioni sorte durante la gara. ANAC lo esprime entro 30 giorni dalla richiesta, previo contraddittorio. L’operatore che lo ha chiesto o vi ha aderito può impugnarlo soltanto per violazione delle regole di diritto relative al merito. La stazione appaltante che non intende conformarsi adotta entro 15 giorni un provvedimento motivato e lo comunica alle parti e ad ANAC; l’Autorità può esercitare la propria legittimazione ad agire.

Non è corretto descrivere il parere come un annullamento della gara o come una semplice opinione senza conseguenze. La richiesta, però, non sospende per sé i termini del ricorso e non blocca automaticamente la procedura. Un eventuale provvedimento di sospensione deve avere una propria base e motivazione. Il candidato deve distinguere il precontenzioso richiesto dalle parti dal diverso parere motivato per gravi violazioni e dall’azione di ANAC disciplinati dai commi 2 e 3.

'''+anchor)
t=t.replace("B. Chiedere l'accesso ai documenti pertinenti, motivando il collegamento con la propria posizione.","B. Verificare la disponibilità digitale dovuta ai sensi dell’art. 36 e, per ulteriori documenti, chiedere accesso motivato, presidiando i termini di tutela.")
t=t.replace("Prima di costruire una contestazione sul punteggio occorre conoscere i documenti rilevanti, rispettando oggetto, interesse, limiti e eventuali controinteressati. Il ricorso o il precontenzioso possono essere valutati dopo avere ricostruito il fascicolo e verificato termini ed effetti.","L’art. 36 prevede disponibilità diretta per i soggetti aventi titolo. Se questa manca o occorrono altri documenti, si attiva la tutela dell’accesso senza lasciar decorrere il termine per contestare l’aggiudicazione.")
t=t.replace('## N-TR02-09-03 · Quiz 3\n\n','')
t=t.replace('Controversie in esecuzione, accordo bonario e arbitrato\n','## N-TR02-09-03 · Controversie in esecuzione, accordo bonario e arbitrato\n',1)
start=t.index("L'accordo bonario è uno strumento")
end=t.index('### Tabella di orientamento',start)
t=t[:start]+'''### Accordo bonario e transazione

Per i lavori, l’art. 210 collega l’accordo bonario alle riserve sui documenti contabili che possono determinare una variazione fra il 5% e il 15% dell’importo contrattuale. Il DL comunica le riserve al RUP con relazione riservata; il RUP ne valuta ammissibilità e non manifesta infondatezza. Non si sommano pretese chiaramente inammissibili per raggiungere artificialmente la soglia.

Entro 15 giorni dalla comunicazione il RUP può chiedere alla Camera arbitrale una lista di cinque esperti, scegliendo d’intesa con l’impresa quello che formulerà la proposta; in mancanza di intesa provvede la Camera nei modi previsti. L’esperto formula la proposta entro 90 giorni dalla nomina. Se non lo nomina, il RUP propone entro 90 giorni dalla comunicazione del DL. L’istruttoria avviene in contraddittorio e verifica anche la disponibilità delle risorse.

L’accettazione delle parti entro 45 giorni dal ricevimento conduce a un verbale di accordo, che ha natura di transazione. In caso di rifiuto o mancata accettazione restano arbitrato, se consentito, o giudice ordinario. Prima dell’approvazione del collaudo o del CRE il RUP attiva il procedimento sulle riserve iscritte qualunque ne sia l’importo: il 5% non è quindi una soglia assoluta per ogni momento della vita contrattuale. L’art. 211 estende le regole, in quanto compatibili, a servizi e forniture continuative o periodiche per controversie sull’esatta esecuzione.

**Caso.** Lavori da 2 milioni di euro, riserve ammissibili e non manifestamente infondate da 160.000 euro: incidenza 8%, compresa nella fascia. Si attiva l’istruttoria, senza riconoscere automaticamente l’intera somma. Se l’esame documentale conduce a una proposta da 90.000 euro, questa deve essere motivata e sostenibile; il solo vantaggio di evitare una causa non prova la fondatezza delle riserve.

La transazione dell’art. 212 è residuale quando non è possibile esperire altri rimedi alternativi al giudizio: riguarda diritti soggettivi nell’esecuzione, richiede forma scritta a pena di nullità e, oltre i valori di concessione o rinuncia previsti dalla norma, il parere competente. I limiti sono 100.000 euro, elevati a 200.000 per lavori pubblici; la funzione consultiva varia fra amministrazioni centrali e subcentrali.

### Arbitrato: autorizzazione e limiti

L’art. 213 consente arbitri per diritti soggettivi derivanti dall’esecuzione, anche dopo il mancato accordo bonario. Non serve a chiedere l’annullamento dell’aggiudicazione, che appartiene al giudice amministrativo. La clausola compromissoria nei documenti di gara richiede preventiva autorizzazione motivata dell’organo di governo; senza autorizzazione è nulla. L’aggiudicatario può rifiutarla entro 20 giorni dalla conoscenza dell’aggiudicazione. La legge consente inoltre alle parti di compromettere la lite in arbitrato durante l’esecuzione: non va ripetuto un divieto generale non più corrispondente al testo vigente.

Il collegio è di tre membri e opera nell’ambito della Camera arbitrale per i contratti pubblici, con designazioni di parte, presidente e nomine secondo il Codice. Indipendenza e incompatibilità impediscono, ad esempio, che chi ha progettato o diretto l’opera giudichi la relativa lite. Il lodo diventa efficace con deposito presso la Camera; è impugnabile per nullità e violazione delle regole di diritto sul merito entro 90 giorni dalla notifica, e comunque non oltre 180 giorni dal deposito. Il CCT illustrato nel capitolo 8 ha funzione e disciplina diverse: non è automaticamente questo collegio arbitrale.

'''+t[end:]
anchor='### Ricorso e tutela giurisdizionale'
start=t.index(anchor);end=t.index('Il ricorso può mirare',start)
t=t[:start]+'''### Ricorso, giudice e termini

Le controversie sulla procedura di affidamento spettano al giudice amministrativo nella giurisdizione esclusiva dell’art. 133 CPA; gli atti si impugnano al TAR competente con il rito speciale dell’art. 120. Rientrano anche risarcimento e, nei casi previsti, inefficacia del contratto dopo annullamento dell’aggiudicazione. Le controversie sui diritti nell’esecuzione spettano normalmente al giudice ordinario, salvo materie riservate e situazioni da qualificare, come la revisione prezzi: la sola data successiva alla stipula non decide sempre la giurisdizione.

Il ricorso e i motivi aggiunti si propongono entro **30 giorni**. L’art. 120, comma 2, collega la decorrenza alla comunicazione dell’art. 90 o alla disponibilità degli atti dell’art. 36; quest’ultimo, al comma 9, fissa la decorrenza per aggiudicazione e valutazione delle altre offerte dalla comunicazione. La regola operativa è controllare subito comunicazione e accessibilità effettiva: non assumere che una successiva richiesta di documenti sospenda il termine. Se gli atti non sono disponibili, si documenta l’impedimento e si attiva tempestivamente la tutela, senza inventare una proroga fissa.

Per un bando autonomamente lesivo il termine decorre dalla pubblicazione prevista dal Codice, senza attendere l’esito della gara. In mancanza di pubblicità del bando operano le condizioni particolari dell’art. 120, comma 3, su avviso di aggiudicazione, conoscibilità degli atti e limite massimo: non si applica a ogni caso il termine ordinario di 60 giorni del processo amministrativo. I nuovi atti della stessa gara si contestano con motivi aggiunti. Il CIG identifica la procedura anche negli atti processuali.

### Due divieti di stipula distinti

Lo **standstill sostanziale** dell’art. 18, comma 3, impedisce di stipulare prima che siano trascorsi **32 giorni dall’invio dell’ultima comunicazione di aggiudicazione**. Non significa che l’aggiudicazione sia inefficace per 32 giorni. Non si applica a contratti sotto soglia UE, appalti basati su accordi quadro, appalti specifici in SDA e al caso di unica offerta presentata o ammessa con le ulteriori condizioni sulle impugnazioni del bando indicate dalla norma.

Lo **standstill processuale** del comma 4 nasce dalla notifica alla stazione appaltante di un ricorso contro l’aggiudicazione con contestuale domanda cautelare. Impedisce la stipula fino alla pubblicazione del provvedimento cautelare di primo grado o del dispositivo/sentenza quando il merito è deciso nell’udienza cautelare, salve le cessazioni tipizzate. Non occorre attendere che il giudice emetta un ordine di sospensione perché sorga questo specifico divieto legale.

Per i contratti sotto soglia UE l’art. 55, comma 2, esclude entrambi i termini dilatori dell’art. 18, commi 3 e 4; resta la tutela cautelare del giudice. AQ e SDA, invece, sono eccezioni al solo termine sostanziale sulla base del comma 3: non estendere senza norma ogni eccezione all’altro regime. La stipula ordinaria è entro 60 giorni dall’efficacia dell’aggiudicazione, salve le eccezioni; sotto soglia il termine è 30 giorni dall’aggiudicazione.

Il divieto di stipulare è diverso dalla sospensione dell’aggiudicazione o della procedura: questa dipende dal rimedio e dalla decisione del giudice. Una richiesta di riesame o un’istanza ANAC non producono da sole gli effetti dell’art. 18, comma 4.

'''+t[end:]
t=t.replace("Il ricorso può contenere una domanda cautelare, ma serve una valutazione dell'autorità competente.","Il ricorso contro l’aggiudicazione con contestuale domanda cautelare può produrre il divieto legale di stipula dell’art. 18, comma 4, mentre una sospensione della procedura richiede la pertinente decisione cautelare; resta l’eccezione sotto soglia dell’art. 55.")
t=t.replace("Un altro errore è fissare a memoria termini, soglie o istruzioni operative. Nello studio puoi conoscere la struttura generale; nella risposta professionale devi dire che i dati mobili vanno controllati sul bando, sul disciplinare, sul contratto, sulla disciplina vigente e sui canali istituzionali aggiornati.","Un errore è confondere termini che hanno funzioni diverse: 10 giorni per la decisione sull’oscuramento, 30 per il ricorso appalti, 32 per lo standstill sostanziale. Si studiano insieme alla decorrenza e alle eccezioni, verificando l’eventuale regime temporale della procedura.")
start=t.index('### Mini-esercizio');end=t.index('### Checklist',start)
t=t[:start]+'''### Mini-esercizio: tre orologi sulla stessa gara

Caso didattico: gara aperta sopra soglia con più offerte, estranea ad AQ e SDA. Al giorno 0 sono inviate tutte le comunicazioni di aggiudicazione e resi disponibili gli atti. Beta, seconda, contesta il punteggio e la decisione che oscura un passaggio dell’offerta vincitrice. Si ragiona in giorni relativi; per una scadenza reale occorre applicare anche le regole del calendario processuale.

| Evento | Termine o effetto | Documento da conservare |
| --- | --- | --- |
| Comunicazione e disponibilità | Giorno 0: decorrenze individuate nel caso. | Ricevute e registri di accessibilità PAD. |
| Contestazione dell’oscuramento | Ricorso speciale notificato e depositato entro 10 giorni. | Decisione contestata e atti processuali. |
| Contestazione aggiudicazione | Ricorso entro 30 giorni. L’accesso non sospende da solo questo termine. | Provvedimento, verbali, censure e prove. |
| Possibile stipula ordinaria | Attendere il decorso dei 32 giorni dall’ultima comunicazione. | Verifica delle comunicazioni e delle eccezioni. |
| Ricorso con cautelare notificato al giorno 20 | Opera anche il distinto divieto processuale fino all’esito previsto dalla legge. | Notifica alla stazione appaltante e provvedimento del giudice. |

**Soluzione.** Presentare una sola istanza di accesso al giorno 9 e attendere la risposta non protegge automaticamente entrambe le tutele. Occorre distinguere il ricorso sull’oscuramento dalla contestazione dell’aggiudicazione. Se il ricorso con cautelare viene notificato al giorno 20, il fatto che in seguito scadano i 32 giorni non elimina il divieto processuale ancora operante. Se lo stesso caso riguardasse un contratto sotto soglia, l’art. 55 escluderebbe i due dilatori legali, ferma la possibilità di ottenere tutela cautelare dal giudice.

**Nota da consegnare in prova.** «Individuo comunicazione e atti effettivamente disponibili. Presidio separatamente il termine speciale sull’oscuramento e il termine del rito appalti; l’istanza di accesso non è una sospensione generale. Per la stipula verifico importo, tipo di procedura, ultima comunicazione ed eventuale notifica di ricorso con cautelare. Documento ogni decorrenza e applico l’eccezione soltanto al regime che la prevede».

'''+t[end:]
t+='\n### Riferimenti essenziali\n\nD.Lgs. 36/2023, artt. 18, 35–36, 55, 210–213 e 220; D.Lgs. 104/2010, allegato 1, artt. 116, 120 e 133. Quadro verificato al 3 ottobre 2026.\n'
u.save(slug,t,['V09-23','V09-24'],u.REF);u.record()
