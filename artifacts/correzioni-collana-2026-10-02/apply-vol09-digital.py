from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-ciclo-digitale-verifica-2026-10-03.md'
slug='06-ecosistema-digitale-pad-pcp-bdncp-fvoe';t=u.read(slug)
t=u.replace(t,'`decisione amministrativa -> PAD -> dati della procedura -> PCP/BDNCP -> FVOE e verifiche -> pubblicità -> fascicolo -> controllo`','''`programmazione e progettazione → decisione e atti → pubblicazione del bando, se prevista → offerte e valutazione → verifica requisiti → aggiudicazione ed esito → contratto, esecuzione e chiusura`

**PAD, PCP e BDNCP accompagnano il ciclo; il fascicolo si forma durante tutte le fasi.** Questa sequenza illustra una gara: nell’affidamento diretto non si inventa un bando iniziale. Il controllo dei requisiti segue anche le regole speciali dell’art. 52 per i diretti sotto 40.000 euro e dell’art. 99, comma 3-bis, per determinati malfunzionamenti, illustrate nei capitoli 4 e 5.''')
anchor='### ▣ Verifica 1 - Sigle, funzioni e flusso minimo\n'
t=u.replace(t,anchor,'''### Regime digitale e certificazione

La disciplina digitale del Codice ha piena efficacia dal **1° gennaio 2024**. Gli artt. 21 e 25 richiedono piattaforme e servizi interoperabili per programmazione, progettazione, pubblicazione, affidamento ed esecuzione. Una PAD può coprire una o più attività; l’ente deve garantire la continuità dei dati attraverso gli strumenti utilizzati. Se non dispone di una propria piattaforma, può usare quelle messe a disposizione da altre amministrazioni, centrali o aggregatori.

La certificazione delle piattaforme è rilasciata da **AGID** secondo l’art. 26; **ANAC tiene il registro** delle piattaforme certificate. La qualificazione della stazione appaltante è un controllo diverso. Avere accesso a una PAD non attribuisce automaticamente la qualificazione necessaria per condurre la gara.

Il CIG è acquisito attraverso l’interoperabilità della PAD con i servizi ANAC, secondo il flusso pertinente; non viene rilasciato un nuovo SmartCIG nel regime dal 2024. In una procedura suddivisa in lotti occorre mantenere la corretta corrispondenza fra lotto e identificativo. Il CUP riguarda il progetto di investimento, quando dovuto: un progetto può comprendere più affidamenti e quindi più CIG. Il FVOE 2.0 non richiede il vecchio PassOE; autorizzazioni, documenti e loro validità si gestiscono secondo le regole del servizio.

**Sotto 5.000 euro non significa fuori dal ciclo digitale.** L’esenzione da uno specifico obbligo di ricorso al mercato elettronico, esaminata nel capitolo 7, non è un’esenzione generale da CIG, tracciabilità e trasmissione dei dati. Le modalità eccezionali messe a disposizione da ANAC hanno ambiti e condizioni propri: non autorizzano a sostituire stabilmente la PAD con messaggi email.

### Pubblicità legale, trasparenza, comunicazioni e conservazione

| Funzione | Dove e come | Quale prova conservare |
| --- | --- | --- |
| Pubblicità legale | Flusso PAD–BDNCP; trasmissione all’Ufficio delle pubblicazioni UE quando prevista | Ricezione, pubblicazione effettiva, identificativo dell’avviso e data |
| Trasparenza | Dati alla BDNCP e collegamento dalla sezione Amministrazione trasparente; documenti residui sul sito dell’ente | Collegamento funzionante alla procedura e documenti dovuti |
| Comunicazione | Comunicazione agli interessati secondo la disciplina della fase | Invio, destinatari, contenuto e ricevute |
| Conservazione | Fascicolo dell’ente con atti, offerte, verbali, verifiche ed evidenze | Integrità, reperibilità e corretta gestione documentale nel tempo |

Ai sensi degli artt. 27 e 85, gli effetti giuridici della pubblicazione nazionale decorrono dalla pubblicazione nella **BDNCP**. Per gli avvisi soggetti a pubblicazione europea, quella nazionale segue l’europea; può comunque avvenire se, trascorse quarantotto ore dalla conferma di ricezione dell’avviso, non è stata notificata la pubblicazione europea. I contenuti nazionali non devono divergere da quelli trasmessi all’Ufficio delle pubblicazioni UE. Gli **eForms** sono modelli elettronici strutturati per gli avvisi: non sono una procedura di scelta né un documento che sostituisce il capitolato.

L’art. 28 richiede l’invio tempestivo dei dati del ciclo e il collegamento da Amministrazione trasparente alla BDNCP. Restano sul sito gli atti e le informazioni non assolti con tale trasmissione secondo la disciplina applicabile, fra cui composizione e curricula della commissione e resoconti finanziari finali. Riservatezza, segreti e protezione dei dati limitano ciò che si rende pubblico: il FVOE non è un archivio da aprire indiscriminatamente ai cittadini.

### Caso svolto: la gara del Comune Alfa nel ciclo digitale

Riprendi il servizio da 234.000 euro del capitolo 4, procedura aperta sopra soglia UE subcentrale. Il RUP controlla la coerenza tra atti approvati e dati trasmessi, senza delegare al software la scelta giuridica.

| Momento | Adempimento del caso | Evidenza ed errore da intercettare |
| --- | --- | --- |
| Preparazione | Impostare procedura e lotto sulla PAD certificata, collegando programmazione e atti; acquisire CIG nel flusso previsto | Valore234.000, durata/opzioni coerenti; non inserire144.000 ignorando rinnovo e migrazione |
| Avvio della gara | Inviare avviso strutturato e dati per pubblicità UE/nazionale, rendere disponibili documenti | Esito della pubblicazione e accessibilità; una bozza salvata non è un bando pubblicato |
| Offerte | Ricevere nei termini, custodire e aprire secondo regole di gara | Tracciati e verbali; nessuna apertura anticipata |
| Valutazione e verifica | Applicare la griglia; verificare l’offerente tramite FVOE e dati/documenti pertinenti | Punteggi motivati, requisiti effettivi, date di validità; non limitarsi alla presenza di un file |
| Aggiudicazione | Adottare l’atto competente, comunicare e trasmettere l’esito dovuto | Coerenza tra aggiudicatario, prezzo e atto; non scambiare proposta e aggiudicazione |
| Esecuzione e chiusura | Trasmettere gli eventi richiesti, aggiornare dati di esecuzione, importi e conclusione | Verbali, controlli, pagamenti e dati finali; il flusso non termina con il CIG |

**Incidente risolto.** Il sistema restituisce uno scarto per campo obbligatorio assente: non si annota “pubblicato”. Si corregge il dato sulla base dell’atto, si ritrasmette e si verifica l’esito positivo. Se invece l’errore riguarda un requisito già pubblicato, serve valutarne gli effetti giuridici e l’eventuale rettifica con adeguamento dei termini: la sola modifica del campo non corregge la disciplina della gara.

In caso di **malfunzionamento comprovato** della PAD, l’art. 25 impone di assicurare la partecipazione, anche sospendendo il termine per ricevere offerte e prorogandolo in misura proporzionata alla gravità del guasto. Si conservano segnalazioni, intervallo dell’indisponibilità e provvedimenti adottati; non si ammette selettivamente un’offerta fuori termine con accordi informali. Il guasto del FVOE nella verifica dei requisiti segue invece la disciplina specifica dell’art. 99: sono due problemi distinti.

''' + anchor)
t=u.replace(t,'Nel manuale di studio usa questa sequenza:','Per ricordare le funzioni usa questo elenco, che non rappresenta un ordine temporale:')
u.save(slug,t,['V09-16'],u.REF);u.record()
p=Path('wiki/topics/vol-09-appalti-pnrr-procurement.md');p.write_text(p.read_text(encoding='utf8')+'\n- Ciclo digitale e pubblicità: [[sources/vol-09-ciclo-digitale-verifica-2026-10-03]].\n',encoding='utf8')
