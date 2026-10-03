from pathlib import Path
import re
B=Path('wiki/books/moduli/m-sp02-vigili-fuoco/chapters');A=Path('wiki/reviews/correzioni-collana-2026-10-02/archive')
for no in ['01','05']:
 p=next(B.glob(no+'-*.md'));t=p.read_text(encoding='utf8');a=A/f'pre-correzioni-sp02-{no}.md'
 if not a.exists():a.write_text(t,encoding='utf8')
 if no=='01':
  t=t.replace('Il decreto ministeriale 49 del 2022, per esempio, disciplina modalità concorsuali per l\'accesso a qualifiche iniziali di ispettore tecnico-scientifico in specifici settori.','Occorre separarlo dall’**ispettore tecnico-scientifico**, che appartiene a un diverso ruolo: è per quest’ultimo che il D.M. 49/2022 disciplina i concorsi di accesso. Quel decreto non è la disciplina di accesso dell’ispettore antincendi.').replace('Qui compare il cosiddetto terzo regime del decreto ministeriale 166 del 2019.','Qui rileva l’articolo 2 del decreto ministeriale 166 del 2019.').replace('Il bando ordinario acquisito per questa edizione consente finalmente un confronto corretto.','Il confronto parte dal bando ordinario del 2025.').replace('Questo controllo è obbligatorio.','Conserva l’esito della verifica nella scheda personale.')
 else:
  t=t.replace('è il riferimento che mancava per descrivere il binario direttivo senza usare una specialità come regola.','permette di descrivere il binario direttivo senza usare una specialità come regola.').replace('Il programma ufficiale è parte del corpus:','Il programma ufficiale accompagna il bando:').replace('Nel corpus attuale non sono necessari bandi per ogni possibile specialità per spiegare il principio; se il lettore punta a una di esse, dovrà acquisire il relativo bando.','Per una specialità diversa da quelle confrontate occorre acquisire il relativo bando.').replace('non confondere i corpus','non confondere i programmi')
  start=t.index('La norma contempla il caso di chi, escluso dai ruoli operativi');end=t.index('Questo terzo regime cambia',start)
  t=t[:start]+'''L’articolo 2 richiede idoneità funzionale e un profilo sanitario compatibile con la qualifica, secondo la valutazione medico-legale. Non trasferisce automaticamente le soglie numeriche dell’articolo 1 e non riconosce idoneità a chi è stato escluso da un altro ruolo. Gli esiti delle due valutazioni possono differire, ma ciascuno richiede il proprio accertamento.

Il manuale aiuta a individuare disciplina e passaggio procedurale; non formula diagnosi o strategie per modificare parametri. Chi ha un dubbio raccoglie documentazione e lo approfondisce con i professionisti competenti, senza sospendere terapie o attribuirsi da solo un esito.

'''+t[end:]
  t=t.replace('Questo terzo regime cambia','Questa distinzione cambia').replace('Ispettori e tecnico-professionali: il terzo regime','Ispettori e tecnico-professionali: requisiti distinti').replace('Il terzo regime produce idoneità automatica?','Il regime tecnico-professionale produce idoneità automatica?')
  marker='## N-SP02-08-01'
  addition='''### Prevenzione incendi: funzione, fonti e sequenza

La prevenzione incendi è la funzione pubblica diretta a evitare l’insorgenza degli incendi e a limitarne le conseguenze, proteggendo vita, persone, beni e ambiente. Questa definizione dell’articolo 13 del D.Lgs. 139/2006 distingue la prevenzione dall’intervento di estinzione: comprende conoscenza, regole, misure e controlli prima che l’evento si produca. Non assorbe le competenze di tutte le altre amministrazioni coinvolte nella sicurezza.

Per orientare una risposta concorsuale separa tre livelli. Il D.Lgs. 139/2006 colloca la funzione e i compiti del Corpo. Il D.P.R. 151/2011 individua le attività soggette e i procedimenti. Le regole tecniche applicabili traducono gli obiettivi di sicurezza nelle condizioni da esaminare per il progetto concreto. Un articolo sul procedimento non contiene da solo la soluzione progettuale; una soluzione tecnica non sostituisce l’adempimento amministrativo.

La prima decisione riguarda l’attività: occorre identificarla nell’allegato I del D.P.R. 151/2011 e stabilire la categoria applicabile. Per le categorie **B e C**, l’articolo 3 richiede la valutazione del progetto di nuovi impianti o costruzioni e delle modifiche che aggravano le condizioni di sicurezza preesistenti. Il Comando può chiedere integrazioni entro trenta giorni e si pronuncia entro sessanta dalla documentazione completa. I termini vanno associati all’atto che li fa decorrere, non sommati indiscriminatamente.

Prima dell’esercizio delle attività soggette, l’articolo 4 prevede la **SCIA antincendio** corredata dai documenti richiesti. La verifica formale e il rilascio della ricevuta non significano che ogni requisito materiale sia stato definitivamente accertato. Il responsabile dell’attività e i soggetti che attestano la conformità conservano le rispettive responsabilità; il procedimento comprende i controlli successivi.

Per le categorie **A e B** i controlli mediante visite tecniche sono disposti anche a campione o per programmi settoriali e situazioni di pericolo. Per la **C** la visita tecnica è prevista entro sessanta giorni e, in caso di esito positivo, il certificato di prevenzione incendi è rilasciato entro quindici giorni dalla visita. La categoria A non è quindi esente da ogni obbligo o controllo soltanto perché non segue la valutazione preventiva del progetto prevista per B e C.

Se sono accertate carenze dei requisiti e presupposti, il Comando adotta i provvedimenti motivati di divieto di prosecuzione e rimozione degli effetti dannosi, salvo la possibilità di conformazione nei termini previsti, fino a quarantacinque giorni. Non è una sanatoria automatica. Inoltre una modifica delle condizioni di sicurezza può richiedere il nuovo avvio della procedura; quando comporta aggravio, si considera anche la valutazione progettuale dell’articolo 3.

### Caso procedurale: un ampliamento di categoria B

La traccia specifica già che un’attività appartiene alla categoria B e che l’ampliamento aggrava le condizioni di sicurezza. Il responsabile sostiene: «Ho una vecchia ricevuta, posso procedere senza altro». Imposta la risposta in quattro passaggi. **Dati:** categoria e aggravio sono elementi forniti, non supposizioni. **Regola:** articolo 3 per il progetto della modifica; articolo 4 per il nuovo avvio richiesto dalle mutate condizioni. **Conseguenza:** la vecchia ricevuta non copre automaticamente il nuovo assetto. **Limite:** la traccia non contiene dati sufficienti per redigere o attestare un progetto antincendio.

Una risposta insufficiente si limita a dire «serve il CPI». La risposta ordinata distingue progetto, segnalazione, controlli e atto eventualmente rilasciato, evitando di trasferire la disciplina della categoria C alla B. Nel colloquio questa distinzione dimostra il collegamento fra funzione, procedimento e responsabilità senza improvvisare una soluzione tecnica.

**Domanda-trappola.** L’assenza di valutazione preventiva del progetto per la categoria A equivale ad assenza di SCIA? **No:** progetto e SCIA sono fasi differenti; l’articolo 4 riguarda le attività soggette dell’allegato I. **Mini-esercizio:** riscrivi il caso come risposta di novanta secondi e verifica che ogni termine sia riferito al procedimento corretto.

'''
  assert marker in t;t=t.replace(marker,addition+marker,1)
 t=t.replace('review_required: false','review_required: true');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
print('SP02/01 e /05 integrati')
