from pathlib import Path
import re,shutil,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
delta=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):
 p=next(B.glob(f'{n:02}-*.md'));b=A/'before-text/VOL-04/first'/p.name
 b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copyfile(p,b)
 return p,p.read_text('utf-8')
def save(p,t):
 s='vol-04-organizzazione-upp-verifica-2026-10-03'
 if s not in t:
  t=t.replace('source_refs: [',f'source_refs: [\n  "sources/{s}.md",',1)
  t=t.replace('last_compiled_from: [',f'last_compiled_from: [\n  "wiki/sources/{s}.md",',1)
 t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true')
 before=sha(p);p.write_text(t,'utf-8');delta.append(dict(path=p.as_posix(),before=before,after=sha(p)))
def quiz(t,new):return re.sub(r'### Quiz commentato\n.*?(?=### Checklist di ripasso)',new+'\n\n',t,flags=re.S)
p,t=read(1)
t=t.replace("| Funzione giurisdizionale | Decisione delle controversie, esercizio dell'azione penale, provvedimenti del giudice o del pubblico ministero. | Non è esercitata dal candidato amministrativo; va capita per servire correttamente l'ufficio. |", "| Funzione giudiziaria | Comprende la funzione giudicante, esercitata dai giudici, e quella requirente del pubblico ministero, che esercita l'azione penale e le altre attribuzioni di legge. | Distinguere il giudice che decide dal PM che formula richieste e sostiene l'accusa; il personale amministrativo non assume queste funzioni. |")
t=t.replace("Per UNEP diventa notificazione o esecuzione. Per DAP diventa esecuzione penale, trattamento e misure. Per DGMC diventa minorile, comunità, messa alla prova e progetto.","Per UNEP il processo civile si collega a notificazione ed esecuzione. Cambiando settore, per DAP il processo penale si collega all'esecuzione della pena, al trattamento e alle misure; per DGMC rilevano il procedimento minorile, la comunità, la messa alla prova e il progetto.")
t=t.replace('Il corpus di bandi raccolto per VOL-04 comprende','I bandi rappresentativi comprendono').replace('La lezione editoriale è chiara:','La conseguenza per lo studio è precisa:')
t=quiz(t,'''### Quiz commentato

1. **Il pubblico ministero chiede il rinvio a giudizio e il giudice decide sulla richiesta. Quale distinzione descrive le due attività?**
   - A. Funzione requirente e funzione giudicante.
   - B. Funzione amministrativa ministeriale e funzione requirente.
   - C. Due attività di cancelleria, diverse soltanto per il documento prodotto.
   **Risposta corretta: A.** Entrambe appartengono alla funzione giudiziaria, ma il PM non diventa giudice perché presenta una richiesta. Il Ministero organizza i servizi e la cancelleria cura gli adempimenti di propria competenza.

2. **Un bando richiede un caso di notificazione ed esecuzione. Quale percorso specialistico è più pertinente?**
   - A. Casellario e rilascio di certificati.
   - B. Trattamento penitenziario e osservazione della personalità.
   - C. UNEP: richiesta, competenza, atto ed esito.
   **Risposta corretta: C.** L'UNEP ha un nucleo specifico su notificazioni ed esecuzioni. Le altre attività appartengono al sistema Giustizia ma non rispondono alla consegna.

3. **Il programma di un concorso UPP comprende processo civile. Come si determina la profondità dello studio?**
   - A. Limitandosi al pubblico impiego perché l'addetto non decide.
   - B. Collegando programma e prova a fasi, atti, termini e lavoro sul fascicolo.
   - C. Adottando automaticamente il programma completo del concorso in magistratura.
   **Risposta corretta: B.** Il limite della funzione non elimina la conoscenza processuale richiesta. Il programma concreto stabilisce estensione e approfondimento.

4. **Quale coppia distingue correttamente materia comune e applicazione specialistica?**
   - A. Pubblico impiego nel manuale base; registri e servizi di cancelleria nel volume Giustizia.
   - B. Ordinamento UPP nel manuale base; inglese generale nel volume Giustizia.
   - C. Notificazioni UNEP nel manuale base; metodo generale dei quiz nel volume Giustizia.
   **Risposta corretta: A.** La preparazione comune sostiene il percorso; il volume specialistico sviluppa attività e istituti propri della famiglia.

5. **Il programma comprende ordinamento penitenziario e trattamento. Quale collegamento di studio è coerente?**
   - A. Processo civile, fase di cognizione e certificato del casellario.
   - B. Esecuzione penale, istituti, persona detenuta e misure.
   - C. Controversie di lavoro, ruolo civile e tentativo di conciliazione.
   **Risposta corretta: B.** Il contesto DAP richiede il collegamento tra pena, trattamento e diritti. Le altre sequenze appartengono ad ambiti diversi.

6. **Il titolo sintetico del profilo e gli allegati del bando sembrano indicare priorità diverse. Quale documento guida il piano definitivo?**
   - A. L'indice del manuale già acquistato.
   - B. Il programma di una precedente selezione con titolo simile.
   - C. Il bando vigente con allegati e rettifiche ufficiali.
   **Risposta corretta: C.** La somiglianza del titolo non prova l'identità di programma, mansioni o prove; occorre ricostruire il perimetro effettivo della selezione.''')
save(p,t)
p,t=read(2)
t=t.replace('Il primo piano è la giurisdizione. Riguarda giudici, pubblici ministeri, processi, provvedimenti e decisioni. È il cuore costituzionale della funzione giudiziaria.',"Il primo piano è la funzione giudiziaria: i giudici esercitano la funzione giudicante, mentre i pubblici ministeri svolgono quella requirente, con l'azione penale e le altre attribuzioni di legge. Richiesta del PM e decisione del giudice non coincidono.")
t=t.replace('| Giurisdizione | Magistrati, giudici, pubblici ministeri, provvedimenti, udienze, decisioni |','| Funzione giudiziaria | Giudici: funzione giudicante; pubblici ministeri: funzione requirente |')
t=t.replace('Nel corpus del VOL-04 sono state consolidate fonti come','Le fonti organizzative comprendono').replace('fissato al 18 agosto 2026','fissato al 3 ottobre 2026')
anchor='### DOG e uffici giudiziari: il ponte con cancellerie e UPP'
addition='''### Le direzioni essenziali: attribuzioni da riconoscere

Un dipartimento coordina una grande area; le direzioni generali ne articolano i compiti. Non sono organi giudicanti e non costituiscono gradi del processo. La mappa seguente descrive l'organigramma ministeriale verificato al 3 ottobre 2026.

| Dipartimento e direzione | Ambito da riconoscere |
|---|---|
| DAG — Affari interni | Servizi e affari di giustizia interni, compresi settori delle spese di giustizia e del casellario secondo le attribuzioni organizzative. |
| DAG — Affari internazionali e cooperazione giudiziaria | Rapporti e cooperazione giudiziaria internazionale nell'ambito delle competenze ministeriali. |
| DAG — Affari giuridici e legali | Affari giuridici e contenzioso di competenza del dipartimento. |
| DOG — Personale e formazione | Gestione e formazione del personale amministrativo degli uffici giudiziari. |
| DOG — Risorse materiali e tecnologie | Beni, dotazioni e servizi materiali per il funzionamento degli uffici. |
| DOG — Bilancio e contabilità | Programmazione e gestione contabile delle risorse del dipartimento. |
| DOG — Magistrati | Gestione amministrativa relativa al personale di magistratura nei limiti delle attribuzioni ministeriali; non decisione delle cause né sostituzione del CSM. |

L'Ufficio centrale degli archivi notarili è distinto dai cinque dipartimenti. Cura il settore degli archivi notarili secondo la relativa disciplina; non va contato come sesto dipartimento. Anche gli uffici di diretta collaborazione del Ministro hanno collocazione propria: non diventano direzioni di un dipartimento soltanto perché compaiono nello stesso organigramma.

**Esempio di classificazione.** Una questione sul fabbisogno di personale amministrativo richiama DOG e la direzione del personale; una richiesta di cooperazione giudiziaria internazionale richiama DAG e la direzione competente; un problema dell'applicativo processuale richiama il versante DIT. La classificazione individua l'area: il destinatario operativo concreto va poi determinato con l'atto organizzativo e il canale previsto, evitando di inviare ogni richiesta al capo dipartimento.

'''
t=t.replace(anchor,addition+anchor)
t=re.sub(r'### DIT, DGSIA e supporto digitale\n.*?(?=### Schema dipartimento)', '''### DIT e direzioni del digitale

Il Dipartimento per l'innovazione tecnologica della giustizia, DIT, è uno dei cinque dipartimenti. Nel suo assetto corrente si distinguono quattro direzioni generali:

| Direzione | Funzione da collegare al lavoro d'ufficio |
|---|---|
| DGSAP — Servizi applicativi | Sviluppo, evoluzione e gestione del versante applicativo dei servizi digitali della giustizia. |
| DGINFRA — Infrastrutture digitali e assistenza all'utenza | Infrastrutture, funzionamento tecnico e assistenza agli utenti dei sistemi. |
| DGSTAT — Statistica e analisi organizzativa | Dati statistici e analisi del funzionamento degli uffici. |
| DGCOE — Coordinamento delle politiche di coesione | Programmi e interventi delle politiche di coesione attribuiti al dipartimento. |

DGSIA, Direzione generale per i sistemi informativi automatizzati, è una denominazione di precedenti assetti. Rimane nei documenti tecnici storici e in alcuni recapiti, ma non va aggiunta come quinta direzione attuale del DIT. Leggere una specifica tecnica firmata dalla DGSIA significa identificare l'autorità e la data dell'atto, non dedurre che l'organigramma sia rimasto invariato.

PCT, processo penale telematico, registri e fascicolo informatico collegano queste funzioni al lavoro quotidiano. Un errore nel contenuto di un atto, un'anomalia applicativa e un problema di accesso alla rete richiedono diagnosi diverse: non tutto ciò che compare sullo schermo è un guasto tecnico. Il capitolo 12 sviluppa depositi, ricevute e controlli; la profondità tecnica da studiare dipende dal programma del concorso.

''',t,flags=re.S)
t=t.replace('la DGSIA va collocata correttamente nel versante tecnico-amministrativo.','DGSIA è una denominazione storica da distinguere dalle quattro direzioni attuali del DIT.')
t=t.replace('So spiegare perché DIT e DGSIA non sono sinonimi?','So distinguere DGSAP, DGINFRA, DGSTAT e DGCOE, qualificando DGSIA come denominazione storica?')
t=quiz(t,'''### Quiz commentato

1. **Quale elenco corrisponde ai cinque dipartimenti al 3 ottobre 2026?**
   - A. DAG, DOG, DAP, DGMC e Ufficio centrale archivi notarili.
   - B. DAG, DOG, DIT, DAP e DGMC.
   - C. DAG, DOG, DGSAP, DAP e DGMC.
   **Risposta corretta: B.** DIT è dipartimento; DGSAP è una sua direzione. L'Ufficio centrale archivi notarili ha collocazione distinta.

2. **Una specifica tecnica storica reca la sigla DGSIA. Che cosa è corretto dedurre?**
   - A. La sigla coincide con il dipartimento DIT.
   - B. DGSIA è una quinta direzione da aggiungere all'organigramma attuale.
   - C. Occorre distinguere l'autorità dell'atto storico dall'assetto attuale DGSAP, DGINFRA, DGSTAT e DGCOE.
   **Risposta corretta: C.** Una denominazione presente in un documento precedente non dimostra la persistenza dell'articolazione organizzativa.

3. **Quale dipartimento comprende la direzione del personale e della formazione per gli uffici giudiziari?**
   - A. DOG.
   - B. DAG.
   - C. DIT.
   **Risposta corretta: A.** Il DOG riguarda organizzazione giudiziaria, personale e servizi. DAG e DIT hanno compiti differenti.

4. **Una questione di cooperazione giudiziaria internazionale richiama in primo luogo quale area?**
   - A. DOG, risorse materiali e tecnologie.
   - B. DAG, affari internazionali e cooperazione giudiziaria.
   - C. DIT, statistica e analisi organizzativa.
   **Risposta corretta: B.** La classificazione segue la competenza materiale, non il mezzo digitale eventualmente usato per trasmettere gli atti.

5. **Quale abbinamento è corretto?**
   - A. DAP: istituti penitenziari adulti; DGMC: minorile e giustizia di comunità.
   - B. DAP: esecuzione penale esterna; DGMC: gestione generale degli istituti adulti.
   - C. DAP: cooperazione internazionale; DGMC: personale delle cancellerie.
   **Risposta corretta: A.** Esecuzione esterna e servizi di comunità si collegano al DGMC; non vanno confusi con il governo dell'amministrazione penitenziaria adulta.

6. **Quale distinzione riguarda due direzioni del DIT?**
   - A. DAG cura gli applicativi; DOG cura i dati statistici.
   - B. DGCOE esercita la funzione giudicante; DGSTAT quella requirente.
   - C. DGSAP riguarda i servizi applicativi; DGINFRA le infrastrutture e l'assistenza all'utenza.
   **Risposta corretta: C.** Sono aree tecniche e amministrative del dipartimento; nessuna di esse decide controversie.''')
save(p,t)
p,t=read(4)
start=t.index('Accanto a questo riferimento vanno considerati')
end=t.index('### Il progetto organizzativo',start)
t=t[:start]+'''Il D.L. 12 giugno 2026, n. 100 è stato convertito senza modificazioni dalla L. 7 agosto 2026, n. 145, pubblicata l'8 agosto ed entrata in vigore il 9 agosto. Non è decaduto: le sue modifiche vanno lette nel testo coordinato. Per i compiti del personale è intervenuto successivamente anche l'art. 7 del D.L. 7 agosto 2026, n. 144. Il quadro qui descritto è verificato al 3 ottobre 2026; per disposizioni ancora in corso di conversione va controllato l'esito legislativo prima della prova.

### Sedi, composizione e responsabilità

L'art. 1 D.Lgs. 151/2022 prevede UPP presso tribunali ordinari, tribunali per i minorenni, corti d'appello e tribunali di sorveglianza, oltre alle strutture presso la Corte di cassazione e alle specifiche strutture presso la sua Procura generale. Non istituisce, per questa sola previsione, un UPP ordinario in ogni Procura della Repubblica. Il supporto amministrativo al PM nella Procura del tribunale si colloca nella segreteria e nell'organizzazione di quell'ufficio.

La disciplina del futuro tribunale per le persone, per i minorenni e per le famiglie richiede di distinguere testo della riforma ed efficacia differita: il DL 100/2026 ha ulteriormente rinviato l'operatività del nuovo assetto attraverso l'art. 49 D.Lgs. 149/2022. Non descrivere come già costituito un ufficio soltanto perché compare nella disposizione novellata.

L'art. 4 consente l'assegnazione di più categorie: magistrati onorari nei casi previsti, tirocinanti, personale di cancelleria o segreteria, personale che ha prestato servizio come addetto ai sensi dell'art. 11 DL 80/2021 e altre figure ammesse dalla legge. La composizione effettiva dipende dall'ufficio e dalle assegnazioni. **UPP indica la struttura; AUPP una figura personale.** Un addetto amministrativo non acquista le funzioni del magistrato onorario eventualmente inserito nella stessa struttura.

| Piano | Regola da applicare |
|---|---|
| Costituzione e progetto | Il capo dell'ufficio, sentiti i presidenti di sezione e il dirigente amministrativo, organizza gli UPP secondo l'art. 3. |
| Analisi e obiettivi | Il progetto considera flussi, criticità, priorità, obiettivi e azioni; deve essere coerente con il programma annuale dell'art. 4 D.Lgs. 240/2006. |
| Personale amministrativo | Individuazione di concerto con il dirigente amministrativo; compiti nel rispetto di profilo e disciplina contrattuale. |
| Coordinamento | Il capo dell'ufficio assicura direzione, coordinamento e formazione secondo la disciplina organizzativa. |
| Accesso e riservatezza | Accesso funzionale a fascicoli, udienze e camere di consiglio nei limiti legali e salvo diversa decisione del giudice; obblighi di riservatezza e incompatibilità per le categorie previste. |

Gli artt. 5–6 disciplinano il supporto negli uffici di merito: studio dei fascicoli, ricerca, preparazione dell'udienza, bozze, controlli e gestione dei flussi secondo l'ambito. Gli artt. 7–9 riguardano i contesti specialistici indicati dalla legge. Per il personale dell'art. 4, comma 1, lettera f, il testo vigente dall'8 agosto 2026 prevede le attività delle lettere a–d degli artt. 5–6, le altre attività contrattuali e, **in via residuale, il presidio delle attività di cancelleria**. È quindi errato affermare che un addetto non possa mai svolgere tali attività; occorre verificare assegnazione, profilo e disciplina applicabile. Resta fermo che non decide il processo al posto del magistrato.

''' +t[end:]
t=t.replace('Fascicolo, udienza, notifiche, depositi, termini, raccordi con segreteria','Fascicolo, udienza, notifiche, depositi, termini, raccordi con cancelleria dell’ufficio giudicante')
t=t.replace('attenzione a dati sensibili e contesto','attenzione ai dati personali, anche relativi a reati o salute, e al contesto')
t=t.replace('il D.L. 100/2026 non convertito non costituisce base normativa attuale.','il DL 100/2026 è convertito dalla L. 145/2026 e il DL 144/2026 interviene ulteriormente sui compiti.')
t=t.replace("**L'addetto UPP può sostituire il magistrato nella decisione o la cancelleria negli adempimenti?**", "**La vicinanza dell'addetto UPP al fascicolo gli attribuisce poteri decisori? E sono escluse tutte le attività di cancelleria?**")
t=t.replace("Risposta: no. L'addetto UPP opera in una struttura di supporto e può svolgere attività preparatorie, conoscitive, organizzative e di raccordo, ma non esercita la funzione giurisdizionale. Non decide il fascicolo, non assume la responsabilità del provvedimento e non diventa automaticamente titolare degli adempimenti propri della cancelleria.","Risposta: non acquista poteri decisori. Studio e bozza restano attività preparatorie, mentre il magistrato assume il provvedimento. L'esclusione assoluta delle attività di cancelleria sarebbe però errata: per il personale dell'art. 4, comma 1, lettera f, gli artt. 5–6 prevedono anche il presidio residuale di tali attività, nel rispetto dell'assegnazione e della disciplina contrattuale.")
t=t.replace("l'UPP non decide e non sostituisce magistrato o cancelleria.","l'addetto non assume la decisione del magistrato; le eventuali attività di cancelleria richiedono assegnazione e rispetto delle regole del profilo.")
t=t.replace('"decreto non convertito usato come fonte vigente"','"conversione ignorata", "compiti di cancelleria esclusi in assoluto"')
t=quiz(t,'''### Quiz commentato

1. **Quale affermazione descrive correttamente la composizione dell'UPP?**
   - A. Coincide necessariamente con i soli addetti assunti per il PNRR.
   - B. Comprende esclusivamente magistrati togati e dirigenti amministrativi.
   - C. Può comprendere diverse categorie previste dall'art. 4 D.Lgs. 151/2022, ciascuna con il proprio ruolo.
   **Risposta corretta: C.** Struttura e qualifica individuale non coincidono; la presenza di un magistrato onorario non trasferisce le sue funzioni agli addetti amministrativi.

2. **Chi organizza gli UPP secondo l'art. 3 D.Lgs. 151/2022?**
   - A. Il capo dell'ufficio, sentiti i presidenti di sezione e il dirigente amministrativo.
   - B. Il dirigente amministrativo senza coinvolgere il capo dell'ufficio.
   - C. Ciascun addetto, scegliendo autonomamente fascicoli e priorità.
   **Risposta corretta: A.** Il progetto è responsabilità organizzativa del capo; per l'individuazione del personale è previsto il concerto con il dirigente amministrativo.

3. **L'art. 1 D.Lgs. 151/2022 istituisce un UPP ordinario in ogni Procura della Repubblica?**
   - A. Sì, perché ogni ufficio requirente è anche giudicante.
   - B. No; distingue gli uffici previsti e le specifiche strutture presso la Procura generale della Cassazione.
   - C. Sì, ma soltanto quando la Procura esercita l'azione penale.
   **Risposta corretta: B.** Il supporto nella Procura del tribunale non può essere qualificato UPP sulla sola base di quella norma; vanno identificate struttura e disciplina effettive.

4. **Qual è lo stato del DL 100/2026 al 3 ottobre 2026?**
   - A. Convertito senza modificazioni dalla L. 145/2026.
   - B. Decaduto l'11 agosto per mancata conversione.
   - C. Ancora provvisoriamente efficace in attesa della prima deliberazione parlamentare.
   **Risposta corretta: A.** La legge del 7 agosto è stata pubblicata l'8 agosto ed è entrata in vigore il 9. Le novità successive richiedono lettura del testo coordinato.

5. **Il personale dell'art. 4, comma 1, lettera f può svolgere attività di cancelleria secondo gli artt. 5–6 vigenti?**
   - A. No, sono incompatibili in assoluto con la qualifica.
   - B. Sì, assumendo per questo anche i poteri decisori del giudice.
   - C. Sì, in via residuale, nel quadro dei compiti e della disciplina applicabili.
   **Risposta corretta: C.** Il DL 144/2026 ha esplicitato il presidio residuale di tali attività. Nessun automatismo trasforma l'addetto in titolare della decisione giudiziaria.

6. **Una scheda UPP propone due possibili soluzioni e indica i precedenti pertinenti. Chi assume il provvedimento?**
   - A. L'autore della scheda, se ha usato il modello dell'ufficio.
   - B. Il magistrato competente, dopo la propria valutazione.
   - C. Il dirigente amministrativo che ha assegnato il personale.
   **Risposta corretta: B.** La scheda prepara la valutazione; modello e assegnazione organizzativa non trasferiscono competenze giurisdizionali.''')
save(p,t)
(A/'VOL-04-first-delta.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps({'chapters':len(delta),'quizReplaced':18}))
