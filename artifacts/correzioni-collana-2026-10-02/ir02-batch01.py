from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-ir02-universita-afam/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
def add(n,k,txt):
 p=next(B.glob(f'{n:02}-*.md'));t=p.read_text();h=re.search(rf'^### N-IR02-{n:02}-{k:02}[^\n]*\n',t,re.M);assert h
 t=t[:h.end()]+'\n'+txt.strip()+'\n\n'+t[h.end():];t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8');return str(p).replace('\\','/')
files=[]
files.append(add(2,3,'''La L. 240/2010, art. 2, fissa un quadro per le **università statali** che va conosciuto prima di aprire lo statuto. L’autonomia non rende tutte le attribuzioni indeterminate. Le istituzioni a ordinamento speciale e quelle non statali richiedono attenzione al proprio regime; la tabella seguente non viene estesa automaticamente a ogni soggetto che offre formazione superiore.

| Organo | Funzione nazionale essenziale | Atto o distinzione da ricordare |
| --- | --- | --- |
| Rettore | Rappresentanza legale, indirizzo e coordinamento scientifico-didattico | Propone programmazione, bilanci e incarico del direttore generale; non approva da solo ogni atto |
| Senato accademico | Proposte e pareri in didattica, ricerca e servizi agli studenti | Parere obbligatorio sui bilanci; regolamenti didattici e di ricerca con il raccordo previsto con il CdA |
| Consiglio di amministrazione | Indirizzo strategico, programmazione e sostenibilità finanziaria | Approva bilanci e regolamento di amministrazione e contabilità; conferisce l’incarico al DG |
| Direttore generale | Organizzazione e gestione di servizi, risorse e personale tecnico-amministrativo | Opera sulla base degli indirizzi del CdA; vi partecipa senza voto |
| Collegio dei revisori | Controllo amministrativo-contabile | Non si sostituisce alla gestione o al giudizio scientifico |
| Nucleo di valutazione | Verifica di qualità ed efficacia e funzioni valutative previste | Distinto dal presidio che sostiene operativamente l’assicurazione della qualità |

Il rettore ha un mandato unico di **sei anni**, non rinnovabile. Il senato ha al massimo **35 componenti**, con il rettore e rappresentanza elettiva degli studenti: almeno due terzi sono docenti di ruolo e almeno un terzo di questi sono direttori di dipartimento. Il CdA ha al massimo **11 componenti**, compresi rettore e rappresentanza studentesca; almeno tre sono esterni ai ruoli dell’ateneo se il consiglio è di undici membri, almeno due se è più piccolo, secondo i requisiti temporali della legge. Non si sceglie il numero concreto copiando lo statuto di un altro ateneo.

Il **dipartimento** integra ricerca, didattica e attività esterne correlate; le eventuali scuole o strutture di raccordo coordinano più dipartimenti nei termini statutari. La **commissione paritetica docenti-studenti (CPDS)** monitora offerta formativa, qualità didattica e servizi, individua indicatori e formula pareri su attivazione e soppressione dei corsi. Non coincide con un organo che approva il bilancio generale.

**Caso di competenza.** Un ufficio riceve una bozza di bilancio e scrive che sarà approvata dal senato. La sequenza va corretta: proposta del rettore, parere del senato per gli aspetti di competenza e approvazione del CdA, nel quadro della legge e degli atti dell’ateneo. Il ruolo istruttorio dell’ufficio non gli trasferisce il potere deliberativo. La soluzione non può fermarsi a «controllerei lo statuto», perché la distinzione fondamentale è già nella norma nazionale.

**Verifica.** Il direttore generale può votare nel CdA per far prevalere la propria proposta? No: la L. 240 ne prevede la partecipazione senza diritto di voto. È invece responsabile della gestione attribuita alla sua funzione; assenza di voto non significa assenza di responsabilità.'''))
p=next(B.glob('02-*.md'));t=p.read_text();a=t.find("Il candidato deve resistere alla tentazione di compilare un catalogo universale");
if a>=0:
 e=t.find('\n\n',a);t=t[:a]+"Il quadro nazionale appena esposto orienta la lettura dello statuto. Quest’ultimo definisce l’assetto concreto nel rispetto della legge: composizioni effettive, articolazione delle strutture e competenze integrative devono essere riferite all’ateneo del bando. Il candidato distingue quindi il vincolo nazionale dal dato organizzativo locale, senza lasciare indeterminato ciò che la legge già stabilisce."+t[e:]
p.write_text(t,encoding='utf8')
files.append(add(3,2,'''Il **credito formativo universitario (CFU)** misura il lavoro richiesto allo studente, non soltanto le ore di lezione e non il voto conseguito. Il D.M. 270/2004, art. 5, attribuisce ordinariamente **25 ore complessive** a un CFU, con possibili variazioni ministeriali entro il 20% per specifiche classi; il carico medio annuale a tempo pieno è **60 CFU**. Studio individuale, lezioni, laboratori e altre attività contribuiscono al carico secondo il percorso.

Una laurea richiede **180 CFU**; una laurea magistrale ordinaria **120 CFU**. I corsi magistrali a ciclo unico hanno ordinamenti specifici: non si descrivono tutti come una triennale seguita da un biennio. I master universitari richiedono almeno **60 CFU** aggiuntivi rispetto al titolo di accesso; primo e secondo livello seguono rispettivamente laurea e laurea magistrale. Un master di primo livello non è una laurea magistrale, anche se entrambi possono essere frequentati dopo una laurea. Specializzazioni e dottorati hanno finalità e disciplina proprie.

I crediti sono acquisiti superando l’esame o la verifica prevista; il voto esprime la valutazione del profitto. Due studenti che superano lo stesso esame da 6 CFU con voti diversi acquisiscono entrambi 6 CFU. Il riconoscimento di crediti nel passaggio ad altro corso compete alla struttura ricevente secondo criteri predeterminati: non deriva automaticamente dall’identità del nome dell’insegnamento.

**Esempio risolto.** Un’attività da 6 CFU corrisponde ordinariamente a 150 ore complessive. Se il piano prevede 48 ore di lezione, restano 102 ore per lo studio e le altre attività incluse nel carico; non si aggiungono altre 150 ore alle 48. Un percorso annuale da 60 CFU corrisponde convenzionalmente a 1.500 ore, non a 1.500 ore tutte in aula. Il calcolo serve a distinguere carico, erogazione didattica e frequenza, che non sono sinonimi.'''))
add(3,4,'''**AVA** significa Autovalutazione, Valutazione e Accreditamento. L’**assicurazione della qualità (AQ)** comprende progettazione, attuazione, monitoraggio e miglioramento; l’accreditamento verifica i requisiti per la sede o il corso secondo la procedura nazionale. Il Ministero adotta i provvedimenti di accreditamento nel quadro della valutazione ANVUR: il presidio interno non “accredita” autonomamente un corso.

Nel modello AVA3, il **Presidio della qualità (PQA)** fornisce strumenti e supporto metodologico ai processi interni; il **Nucleo di valutazione (NdV)** valuta sistema e risultati; le **CPDS** portano il contributo paritetico di docenti e studenti al monitoraggio e alle proposte. Corsi di studio e dipartimenti analizzano i propri risultati e attuano le azioni di miglioramento. Un ufficio raccoglie e organizza evidenze, senza sostituire le responsabilità accademiche.

La **SUA-CdS**, Scheda unica annuale del corso di studio, documenta caratteristiche e organizzazione del corso. La **Scheda di monitoraggio annuale** analizza gli indicatori; il **Rapporto di riesame ciclico** sviluppa un esame più ampio dell’adeguatezza e dei cambiamenti necessari. Relazioni CPDS, opinioni degli studenti ed esiti occupazionali aggiungono punti di osservazione differenti. Compilare moduli senza usare i risultati non chiude il ciclo della qualità.

**Caso.** Diminuisce la quota di studenti che acquisiscono i crediti attesi nel primo anno. Il corso verifica dati e composizione delle coorti, ascolta gli studenti e individua un problema documentato di sovrapposizione dei laboratori. Propone un nuovo calendario, assegna un responsabile e una data di controllo, poi confronta gli esiti. Il PQA sostiene il processo; il NdV ne valuta l’efficacia; non si può dedurre la causa dal solo indicatore né dichiarare risolto il problema perché il calendario è stato pubblicato.''')
files.append(add(4,2,'''Le variazioni principali devono essere distinte anche prima di leggere i moduli locali:

| Evento | Effetto da distinguere | Controllo necessario |
| --- | --- | --- |
| Passaggio | Cambio di corso nello stesso ateneo | Ammissione, riconoscimenti e piano del nuovo corso |
| Trasferimento | Prosecuzione presso un altro ateneo | Procedure in uscita e ingresso e riconoscimento della carriera |
| Rinuncia | Atto volontario formale di chiusura della carriera | Forma, effetti e possibili regole di nuova immatricolazione |
| Decadenza | Impossibilità di proseguire quella carriera per condizioni previste dalla disciplina | Decorrenze, atti di carriera rilevanti ed eccezioni |
| Interruzione | Mancata prosecuzione delle iscrizioni secondo le regole del corso | Ripresa, ricognizione, contributi ed effetti sul decorso della carriera |
| Sospensione | Pausa ammessa in situazioni disciplinate | Presupposti, richiesta o documentazione, durata ed effetti |

Per esempio, il portale dell’**Università di Bologna**, consultato il 3 ottobre 2026, distingue la rinuncia formale irrevocabile dalla pausa degli studi e precisa che gli anni di sospensione non entrano nel computo della decadenza, mentre quelli di interruzione vi entrano. È un esempio locale identificato, non una regola da estendere senza verifica a ogni ateneo.

**Caso risolto.** Uno studente scrive: «Non pago più e considero sospesa la carriera». L’ufficio non registra una sospensione basandosi sulla frase: verifica se esiste un presupposto ammesso e se sono stati svolti gli adempimenti richiesti. Spiega la differenza rispetto a interruzione e rinuncia, chiarisce gli effetti sulla ripresa e lascia allo studente una scelta informata. Non confonde l’assistenza procedimentale con la decisione accademica sul riconoscimento degli esami.'''))
add(4,3,'''Il quadro del D.Lgs. 68/2012 collega diritto allo studio, servizi e benefici a condizioni economiche e di merito; la disciplina attuativa del beneficio specifica requisiti, procedure e controlli. **ISEE** è l’indicatore della situazione economica equivalente; **ISPE** è quello della situazione patrimoniale equivalente. Per le prestazioni universitarie occorre l’attestazione pertinente, non un valore economico informale comunicato allo sportello.

**Esempio datato: ER.GO, bando benefici 2026/2027, art. 7, pagina 35.** Per la borsa di studio il bando indica soglie di 25.000 euro ISEE e 50.000 euro ISPE. Si controllano entrambi, insieme agli altri requisiti: la verifica economica favorevole non equivale all’assegnazione.

La candidata A dichiara ISEE 24.000 e ISPE 51.000 euro: supera la soglia patrimoniale. Il candidato B presenta 23.000 e 49.000 euro: soddisfa questo controllo economico, ma occorre ancora verificare merito, iscrizione, domanda e altre condizioni. L’ufficio non “compensa” un indicatore sopra soglia con l’altro più basso. Questi numeri valgono per il bando identificato; per un anno o un ente diverso si sostituisce la fonte prima di rifare il calcolo.''')
batch={'V06-09':{'change':'Inseriti quadro nazionale degli organi L.240, CFU/titoli e calcoli D.M.270, attori/documenti AVA3, distinzione delle variazioni di carriera e caso economico ER.GO2026/2027 con fonte identificata.','files':files+['wiki/sources/fonti-ufficiali-m-ir02-universita-afam-2026-07-24.md'],'evidence':'Consolidati L.240 art.2 e D.M.270 artt.3/5/7 letti; ANVUR AVA3 pp.19–20; ER.GO art.7 p.35 e portale UniBo. Calcoli150/102/1500 e doppia soglia risolti.','status':'applicato'}}
(A/'VOL-06-batch05.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('V06-09 applicato')
