from pathlib import Path
import importlib.util,re
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-governance-contratti-verifica-2026-10-03.md'
slug='01-quattro-profili-ciclo-integrato';t=u.read(slug)
t=u.replace(t,'Il pagamento riguarda la liquidazione della spesa secondo evidenze e controlli.','Nell’ordinamento contabile degli enti locali, la liquidazione determina la somma certa e liquida da pagare dopo la verifica del diritto del creditore e della prestazione; l’ordinazione dispone il pagamento mediante mandato al tesoriere; il pagamento estingue materialmente il debito. Non sono sinonimi: artt. 184–185 TUEL. Nella mappa, la voce pagamento riassume questo tratto del ciclo, senza fonderne le competenze.')
t=u.replace(t,'| Pagamento | Quali evidenze permettono la liquidazione? | fascicolo di pagamento |','| Liquidazione, ordinazione e pagamento | La prestazione è verificata, il mandato è emesso e il debito è pagato? | atto di liquidazione, mandato, quietanza |')
t=u.replace(t,'| WBS | Quali attività compongono il lavoro? |','| WBS | Quali prodotti e pacchetti di lavoro compongono il progetto? |')
t=u.replace(t,'Non troverai qui soglie, istruzioni minuto per minuto sulle piattaforme o regole specifiche di singole misure PNRR. Quei dati cambiano, dipendono dal bando e vanno controllati su fonti ufficiali aggiornate. Qui impari il telaio: profilo, fase, rischio, output, verifica.','Questo capitolo introduce profili e ciclo del progetto. Il capitolo 2 sviluppa ruoli e qualificazione; i capitoli 3–9 applicano le regole degli affidamenti; i capitoli 10–12 trattano PNRR, controlli e sostenibilità; il capitolo 13 svolge gli strumenti di progetto. Le condizioni di una specifica misura finanziata si leggono insieme alla sua documentazione: non si ricavano dal solo nome PNRR.')
u.save(slug,t,['V09-05','V09-33'],u.REF)
slug='02-governance-rup-fasi-team-qualificazione';t=u.read(slug)
t=u.replace(t,'Il capitolo usa un criterio prudente: non fissa soglie, termini, classi di qualificazione, istruzioni di piattaforma o dettagli soggetti ad aggiornamento. Per questi dati devi controllare la versione vigente del Codice dei contratti pubblici, dell\'Allegato I.2, degli atti ANAC applicabili e delle regole interne dell\'ente.','Il quadro normativo qui applicato è quello verificato al 3 ottobre 2026. Le soglie europee richiamate valgono per il biennio 2026–2027 e per i settori ordinari. Nei casi si distinguono la capacità dell’ente di svolgere la procedura, i requisiti della persona nominata RUP e le condizioni di partecipazione degli operatori economici.')
anchor='### Responsabili di fase e supporti'
t=u.replace(t,anchor,'''### Nomina e requisiti: una verifica distinta per ogni incarico

L’art. 15 del d.lgs. 36/2023 colloca la nomina del RUP **nel primo atto di avvio dell’intervento**, per programmazione, progettazione, affidamento ed esecuzione. Il RUP è scelto fra i dipendenti, anche a tempo determinato, preferibilmente dell’unità titolare del potere di spesa, nel rispetto di inquadramento, mansioni e requisiti dell’allegato I.2. L’accertata carenza di personale interno qualificato consente la nomina di un dipendente di un’altra amministrazione pubblica. Non basta affidare una consulenza esterna per trasformare il consulente in RUP.

L’ufficio è obbligatorio e non può essere rifiutato. Se il primo atto non nomina il RUP, le funzioni spettano al responsabile dell’unità organizzativa competente per l’intervento. Il nome deve risultare dal bando o avviso, oppure dall’invito o dall’atto di affidamento diretto. La nomina deve consentire di verificare competenza, requisiti e assenza delle cause ostative: l’allegato I.2 richiama, fra l’altro, le condanne anche non definitive considerate dall’art. 35-bis del d.lgs. 165/2001.

| Contratto | Requisiti essenziali del RUP nell’allegato I.2 |
| --- | --- |
| Lavori e servizi di architettura/ingegneria | Figura tecnica; abilitazione quando richiesta. Esperienza in attività analoghe: almeno 1 anno sotto 1 milione, 3 anni da 1 milione a meno della soglia UE lavori, 5 anni dalla soglia UE. L’art. 4 disciplina anche il tecnico senza abilitazione e i lavori particolarmente complessi. |
| Servizi e forniture | Titolo adeguato, formazione aggiornata ed esperienza nel settore: almeno 1 anno sotto soglia UE, 3 anni dalla soglia UE. Per prestazioni con caratteristiche tecniche particolari possono essere richiesti laurea magistrale e competenze specifiche. |

Nei lavori particolarmente complessi servono anche laurea magistrale o specialistica pertinente, esperienza almeno quinquennale e competenze di project management. Il cumulo RUP/progettista/DL incontra i limiti dell’art. 4: non è ammesso nei lavori complessi, nelle altre ipotesi qualificate indicate e negli interventi almeno pari alla soglia UE. Non dedurre dal cumulo consentito in un piccolo intervento una regola generale.

L’allegato I.2, art. 2, comma 3, disciplina il caso di requisiti carenti: nei lavori, se manca la figura tecnica, interviene il dirigente o responsabile del servizio competente; negli altri casi può essere individuato un dipendente privo di tutti i requisiti, **con supporto qualificato** per quelli mancanti. Il supporto va affidato a dipendenti competenti o, se mancano, a soggetti esterni con le competenze richieste e assicurazione professionale. Una nomina priva di mezzi non risolve la carenza.

''' + anchor)
old='Il responsabile di fase presidia un segmento del ciclo. Può occuparsi, secondo le regole applicabili, di attività legate alla programmazione, alla progettazione, all\'affidamento o all\'esecuzione.'
t=u.replace(t,old,'L’art. 15, comma 4, consente un responsabile di procedimento per il gruppo di fasi **programmazione, progettazione ed esecuzione** e un responsabile di procedimento per **l’affidamento**. Le responsabilità seguono i compiti svolti; resta un unico RUP con supervisione, indirizzo e coordinamento. Questa articolazione non equivale a nominare quattro RUP indipendenti.')
t=u.replace(t,'Il DEC, direttore dell\'esecuzione del contratto, opera in particolare nei contratti di servizi e forniture quando la disciplina e l\'organizzazione lo prevedono.','Nei contratti di servizi e forniture la funzione di direttore dell’esecuzione (DEC) è svolta di norma dal RUP, ai sensi dell’art. 114, comma 7. Nei contratti di particolare importanza il DEC deve essere una persona diversa: l’allegato II.14, art. 32, comprende importi superiori a 500.000 euro e, indipendentemente dall’importo, complessità tecnologica, pluralità di competenze, innovazione e altre condizioni organizzative indicate. La funzione di controllo esiste anche quando manca un incarico separato.')
start=t.index('Per studiare la qualificazione, ragiona per indizi.')
end=t.index('RACI e segregazione dei compiti',start)
t=t[:start]+'''**Autonomia di acquisto e qualificazione.** L’art. 62 consente a tutte le stazioni appaltanti di operare autonomamente per servizi e forniture entro il limite del comma 1, collegato a quello degli affidamenti diretti, e per lavori fino a 500.000 euro. Restano gli obblighi di utilizzare gli strumenti di acquisto previsti dalla legislazione di contenimento della spesa. Il limite di qualificazione non sceglie la procedura: lavori da 300.000 euro possono essere gestiti autonomamente ma non affidati direttamente; si applica la procedura pertinente dell’art. 50.

L’affidamento diretto richiede un importo **inferiore** a 140.000 euro per servizi/forniture e a 150.000 euro per lavori. Esattamente 140.000 euro non consente quindi l’affidamento diretto di un servizio, anche se l’art. 62, comma 1, usa “non superiore” nel diverso ambito dell’autonomia. Per un’amministrazione centrale, inoltre, 140.000 euro coincide nel biennio 2026–2027 con la soglia UE ordinaria di servizi/forniture.

Sopra i limiti di autonomia occorre verificare il livello di qualificazione e le forme ammesse di ricorso a soggetti qualificati. Le non qualificate possono anche utilizzare autonomamente strumenti telematici di negoziazione di centrali qualificate per servizi/forniture sotto la pertinente soglia UE e per lavori di manutenzione ordinaria sotto 1 milione, ai sensi dell’art. 62, comma 6, lettera c). Possono effettuare ordini su strumenti di acquisto delle centrali qualificate e dei soggetti aggregatori. Queste ipotesi non autorizzano una gara autonoma ordinaria di qualsiasi importo su un portale qualsiasi.

| Livello per progettazione e affidamento | Lavori | Servizi e forniture |
| --- | --- | --- |
| Base: L3 / SF3 | Fino a 1 milione | Fino a 750.000 euro |
| Intermedio: L2 / SF2 | Fino alla soglia UE lavori: 5.404.000 euro nel 2026–2027 | Fino a 5 milioni |
| Avanzato: L1 / SF1 | Senza limite di importo | Senza limite di importo |

L’ordine delle sigle è controintuitivo: **1 indica il livello più alto**. L’allegato II.4 richiede AUSA, struttura organizzativa stabile e disponibilità di PAD. A questi presupposti si aggiungono i punteggi, calcolati con le tabelle dell’allegato su personale, competenze, formazione ed esperienza: almeno 30 punti per L3/SF3, 40 per L2/SF2, 50 per L1/SF1. Le facilitazioni transitorie fino al giugno 2024 non sono la regola del 2026. L’iscrizione nell’elenco ANAC deve riguardare settore, ambito e livello adeguati; una checklist interna non sostituisce la qualificazione.

La qualificazione per esecuzione va controllata separatamente. Dal 2025 chi è qualificato per progettazione e affidamento lo è anche per l’esecuzione entro i corrispondenti livelli. Per livelli ulteriori e per le non qualificate valgono le condizioni dell’art. 8 dell’allegato II.4, che considerano anche tempi di pagamento, comunicazioni ANAC e formazione. Restano le specifiche possibilità di eseguire contratti affidati ai sensi dell’art. 62, comma 6, lettere c) e d), e sotto i limiti del comma 1.

**Caso svolto.** Un Comune non qualificato deve acquisire un servizio standard di 180.000 euro, IVA esclusa, senza opzioni o rinnovi, senza interesse transfrontaliero certo; la prestazione è disponibile su uno strumento telematico di negoziazione di una centrale qualificata. Nel 2026 il contratto è sotto la soglia UE subcentrale di 216.000 euro, ma sopra il limite dell’affidamento diretto. Il Comune può usare l’art. 62, comma 6, lettera c), nel rispetto degli obblighi di acquisto applicabili; la procedura è la negoziata dell’art. 50, comma 1, lettera e), con almeno cinque operatori ove esistenti. Il solo fatto che il Comune sia piccolo non consente un affidamento diretto. Se lo stesso servizio valesse 250.000 euro, questa eccezione sotto UE non basterebbe: servirebbe una stazione o centrale qualificata per la procedura, salva un’altra distinta modalità ammessa dalla legge.

Per un’opera ordinaria da 800.000 euro, non di manutenzione ordinaria, la non qualificata non può invocare il limite di 500.000 né l’eccezione manutentiva. Ricorre a un soggetto qualificato, per esempio L3. Il rapporto è formalizzato con accordo o convenzione. L’art. 62, comma 10, prevede che la richiesta sia accolta in assenza di diniego entro dieci giorni; dopo un rifiuto la richiesta passa ad ANAC, che provvede all’assegnazione entro quindici giorni. L’ente mantiene la responsabilità delle attività proprie e del fabbisogno.

''' + t[end:]
start=t.index('| Attività | R | A | C | I |');end=t.index('La matrice va adattata',start)
t=t[:start]+'''**Modello assunto:** Comune con dirigente del servizio competente, RUP distinto dal dirigente, commissione per valutazione qualità/prezzo e DEC separato quando richiesto. La tabella distingue l’esecutore dell’attività e il titolare del relativo atto; C e I sono indicati in una colonna di raccordo per conservarne la leggibilità.

| Attività | R: esegue | A: risponde dell’atto | Raccordo C / I |
| --- | --- | --- | --- |
| Istruttoria del fabbisogno | Ufficio richiedente e RUP | Dirigente del servizio | C: tecnico e finanza; I: ufficio gare |
| Preparazione dei documenti | RUP con team | Dirigente, per approvazione e decisione di contrarre | C: uffici competenti; I: gara |
| Verifica dei requisiti | RUP con ufficio gare | RUP per esito istruttorio; dirigente per eventuale provvedimento di competenza | C: supporti; I: commissione per quanto necessario |
| Valutazione tecnica/economica | Commissione | Commissione per valutazioni e verbali | C: RUP nei limiti del ruolo; I: ufficio gare |
| Aggiudicazione | Ufficio competente istruisce sulla proposta | Dirigente competente, dopo verifica dei presupposti | C: RUP; I: concorrenti tramite comunicazioni previste |
| Controllo della prestazione | DEC | DEC per attestazioni di competenza | C: supporti tecnici; I: RUP |
| Liquidazione | Servizio che ha gestito la prestazione | Responsabile competente ex art. 184 TUEL | C: RUP/DEC; I: finanza per controlli contabili e seguito |
| Ordinazione e pagamento | Servizio finanziario / tesoriere | Ciascuno per gli atti di propria competenza | I: servizio competente e monitoraggio |

L’aggiudicazione non è la valutazione tecnica della commissione: l’art. 17 distingue proposta, verifica dei requisiti e decisione dell’organo competente. Per un servizio complesso da 650.000 euro, il DEC deve essere distinto dal RUP; nominare un DEC non trasferisce al servizio finanziario la valutazione tecnica della prestazione.

''' + t[end:]
t=t.replace('Questa mappa usa il formato operativo 2: ogni nucleo ha un codice, un contenuto da padroneggiare e un output verificabile. I codici servono a studiare in modo ordinato, non a sostituire la spiegazione.','La mappa collega ogni funzione a un risultato di studio verificabile.')
u.save(slug,t,['V09-06','V09-07','V09-08'],u.REF);u.record()
