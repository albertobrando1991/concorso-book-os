from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli');S=Path('wiki/sources')
def chapter(m,n):return next((B/m/'chapters').glob(f'{n:02}-*.md'))
def save(p,s):
 s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M);s=re.sub(r'^review_required:.*$','review_required: true',s,flags=re.M);s=re.sub(r'^draft_stage:.*$','draft_stage: revision-in-progress',s,flags=re.M);p.write_text(s,encoding='utf-8')
def source(n,t):
 p=S/(n+'.md');save(p,p.read_text(encoding='utf-8')+'\n## Riscontro del 3 ottobre 2026\n\n'+t+'\n')
m='m-sa03-dirigenza-medica-sanitaria';m2='m-sa02-professioni-sanitarie';m4='m-sa04-tecnici-sanitari-prevenzione'
source('dirigenza-sanitaria-concorsi-ccnl-2026','Consultati nella [GU del D.P.R. 483/1997](https://www.gazzettaufficiale.it/eli/id/1998/01/17/098G0004/sg) gli artt. 14, 27, 35, 43 e 55: medico, farmacista, biologo e psicologo hanno quadro ordinario 20 titoli e 80 prove (30 scritta, 30 pratica, 20 orale); titoli 10 carriera, 3 accademici/studio, 3 pubblicazioni/scientifici, 4 curriculum. Soglie 21/30 scritta/pratica, 14/20 orale. Non si generalizza a incarichi di struttura complessa o procedure speciali. Art. 37 D.Lgs. 165/2001: obbligo di accertamento delle conoscenze informatiche diffuse e inglese, distinguendolo da modalità, livello ed eventuali ulteriori lingue del bando. Il quadro si coordina con il regolamento sanitario speciale.')
source('dpr-220-2001-concorsi-personale-non-dirigenziale-ssn','Consultati gli artt. 8 e 14 nella [GU del D.P.R. 220/2001](https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.codiceRedazionale=001G0275&atto.dataPubblicazioneGazzetta=2001-06-12): tre prove 30 titoli + 30 scritta + 20 pratica + 20 orale, soglie 21/30 e 14/20; per i concorsi con due prove 40 titoli + 30 pratica + 30 orale, soglia 21/30 in entrambe. Riparto dei titoli fra categorie stabilito dal bando. Art. 37 D.Lgs. 165/2001: obbligo generale di verifica informatica e inglese distinto dalle modalità concrete. Non ricavare la disciplina OSS automaticamente dal quadro delle professioni sanitarie laureate.')
p=chapter(m,1);s=p.read_text(encoding='utf-8');s=s.replace("Informatica e lingua inglese compaiono con frequenza diversa nei bandi esaminati e vanno preparate solo nella forma prevista dalla procedura concreta.","L'art. 37 del D.Lgs. 165/2001 richiede l'accertamento della conoscenza delle applicazioni informatiche diffuse e della lingua inglese; altre lingue possono essere previste in relazione al profilo. L'obbligo generale va coordinato con la disciplina concorsuale sanitaria: il bando specifica modalità, livello e collocazione della verifica, non rende l'inglese una materia meramente facoltativa.")
s=s.replace('la presenza e la modalità vanno verificate','obbligo generale ex art. 37; verificare modalità e livello').replace("Presenza dell'inglese all'orale","Modalità e livello della verifica di inglese").replace('calendario, inglese e sede sono dati `M`','calendario, modalità/livello della verifica di inglese e sede sono dati `M`; l’obbligo generale di accertamento dell’inglese e dell’informatica è un ancoraggio normativo `S`')
pos=s.index('\n## ',s.index('## Mappa BANDO')+4)
block='''
## Punteggi ordinari: distinguere dirigenza e comparto

Per i profili centrali di questo modulo, il D.P.R. 483/1997 stabilisce il seguente quadro dei concorsi ordinari per titoli ed esami.

| Profilo | Articolo sul punteggio | Titoli | Scritta | Pratica | Orale |
| --- | --- | --- | --- | --- | --- |
| Medico | 27 | 20 | 30 | 30 | 20 |
| Farmacista | 35 | 20 | 30 | 30 | 20 |
| Biologo | 43 | 20 | 30 | 30 | 20 |
| Psicologo | 55 | 20 | 30 | 30 | 20 |

Nei quattro casi i 20 punti dei titoli si dividono in 10 per carriera, 3 per titoli accademici e di studio, 3 per pubblicazioni e titoli scientifici, 4 per curriculum formativo e professionale. L'art. 14 richiede almeno **21/30 nella scritta e nella pratica e 14/20 nell'orale**. I titoli non compensano una prova insufficiente: 20 punti nei titoli non rendono idonea una pratica da 20/30.

Il contenuto delle prove e la valutazione dei singoli titoli restano specifici del profilo. Questo schema non va trasferito automaticamente agli incarichi di struttura complessa, a procedure speciali o ad altri ordinamenti. Nel bando si controllano fonte applicata, eventuali deroghe e modalità concrete; una difformità merita verifica, non una correzione personale del bando.
''';s=s[:pos]+block+s[pos:];save(p,s)
common='''
## Il quadro ordinario del D.P.R. 220/2001

Nei concorsi per titoli ed esami con tre prove, l'art. 8 ripartisce 100 punti in **30 per i titoli, 30 per la scritta, 20 per la pratica e 20 per l'orale**. L'art. 14 richiede almeno 21/30 nella scritta e 14/20 sia nella pratica sia nell'orale. Nei concorsi per i quali sono previste soltanto pratica e orale, il quadro è diverso: 40 punti ai titoli, 30 a ciascuna prova e soglia di 21/30 per entrambe.

Il bando ripartisce i punti dei titoli fra carriera, titoli accademici e di studio, pubblicazioni/titoli scientifici e curriculum. Occorre identificare la procedura e le norme speciali applicabili: il medesimo nome di una prova non implica il medesimo punteggio. Esempio: una pratica da 15/20 supera la soglia del concorso a tre prove, mentre una pratica da 20/30 non supera quella del concorso a due prove. I titoli non compensano l'insufficienza.

L'art. 37 del D.Lgs. 165/2001 prevede l'accertamento delle conoscenze informatiche diffuse e dell'inglese; modalità e livello si ricavano dalla disciplina e dal bando. Altre lingue possono essere aggiunte in relazione al profilo. Per gli OSS si identifica prima la disciplina di accesso effettivamente applicata, evitando di trasferire automaticamente le regole delle professioni sanitarie laureate.
'''
for mod in [m2,m4]:
 p=chapter(mod,1);s=p.read_text(encoding='utf-8');pos=s.index('\n## ',s.index('## Mappa BANDO')+4);s=s[:pos]+common+s[pos:];s=s.replace('eventuale preselezione, lingua, informatica, banca dati','eventuale preselezione, modalità delle verifiche linguistiche e informatiche, banca dati').replace('informatica o lingua, quando previste','informatica e inglese secondo le modalità previste');save(p,s)
# NSG official PDF replaces blocked captures as evidence.
p=S/'governo-clinico-appropriatezza-hta-qualita-accreditamento.md';s=p.read_text(encoding='utf-8');s=s.replace("questa nota non attiva claim su indicatori NSG, dati impiegati o dimensioni di monitoraggio finché non sarà consolidata una fonte primaria valida.","la cattura bloccata resta esclusa. Il riscontro aggiunto il 3 ottobre 2026 utilizza invece la relazione ministeriale NSG 2022 disponibile sul sito della Camera, come indicato sotto.").replace('I contenuti NSG restano esclusi fino all’acquisizione di una fonte primaria valida.','').replace("I contenuti NSG restano esclusi fino all'acquisizione di una fonte primaria valida.",'')
s+='''
## Fonte NSG e strumenti di rischio acquisiti il 3 ottobre 2026

Il [Ministero della Salute, relazione NSG 2022, pubblicata nel 2024](https://www.camera.it/temiap/2024/09/23/OCD177-7562.pdf) è disponibile come PDF ufficiale sul sito della Camera: 97 pagine, copia valida in `wiki/raw/correzioni-collana-2026-10-02/ministero-nsg-relazione-2022-camera.pdf`. Lette per questi claim introduzione e metodologia (pp. 5–6 e 9–20 del PDF): DM12 marzo2019, macro-aree prevenzione/distrettuale/ospedaliera, sottoinsieme CORE, punteggi 0–100, soglia 60 per ciascuna area senza compensazione. Il NSIS fornisce flussi, mentre il NSG è il sistema di monitoraggio/valutazione; non sono sinonimi. Il documento 2022 è usato per metodologia, non per descrivere risultati regionali del 2026. Il cruscotto editoriale è originale, con target esplicitamente didattici, non indicatori NSG ufficiali.

Il [Ministero, monitoraggio degli eventi sentinella](https://www.salute.gov.it/new/it/tema/governo-clinico-e-sicurezza-delle-cure/monitoraggio-eventi-sentinella/) e il [sistema SIMES](https://www.salute.gov.it/new/it/sistema-informativo/monitoraggio-errori-sanita-ed-eventi-sentinella-simes/) documentano segnalazione e monitoraggio; [manuale RCA ministeriale](https://www.salute.gov.it/imgs/C_17_newsAree_1330_listaFile_itemName_0_file.pdf) per analisi retrospettiva di cause/fattori. FMEA è analisi proattiva dei modi di guasto del processo: il confronto e l'esempio del capitolo non sono una scala di rischio validata né una procedura di segnalazione aziendale.
''';save(p,s)
p=chapter(m,2);s=p.read_text(encoding='utf-8');pos=s.index('\n## ',s.index('## Mappa BANDO')+4);block='''
## Dai LEA al cruscotto di servizio

Per il quadro di SSN, aziende, distretto e flussi riprendi «SSN, aziende sanitarie, atti e flussi informativi» di M-SA01. Qui il passaggio ulteriore è usare le informazioni per decidere. Il **NSIS** organizza flussi informativi sanitari; il **Nuovo Sistema di Garanzia**, introdotto dal D.M. 12 marzo 2019 e operativo dal 2020, monitora i LEA. Il sottoinsieme CORE consente la valutazione delle macro-aree prevenzione, assistenza distrettuale e ospedaliera. Nel metodo NSG la sufficienza richiede almeno 60 punti in ciascuna area: un risultato alto nell'ospedaliera non compensa una prevenzione insufficiente.

Il cruscotto seguente è un **esempio didattico originale**, non una riproduzione degli indicatori o dei target ufficiali NSG. Periodo, popolazione ed esclusioni devono essere fissati prima del calcolo.

| Indicatore di servizio | Numeratore / denominatore | Dato simulato | Target didattico |
| --- | --- | --- | --- |
| Completezza delle consegne | dimissioni eleggibili con campi obbligatori completi / tutte le dimissioni eleggibili nel mese | 180/200 = 90% | almeno 95% |
| Presa in carico entro il tempo concordato | persone eleggibili prese in carico entro il termine del percorso / persone eleggibili inviate con documentazione completa | 72/80 = 90% | almeno 90% |
| Riammissioni non programmate | persone dimesse vive con riammissione non programmata entro 30 giorni / persone dimesse vive con follow-up osservabile per 30 giorni | 8/160 = 5% | non oltre 5% |

Il primo indicatore suggerisce di verificare dove manchino le informazioni. Il secondo richiede di controllare anche quanti invii restino esclusi per documentazione incompleta: un buon valore può nascondere una barriera d'accesso. Il terzo non dimostra da solo la qualità delle dimissioni: gravità, casistica e completezza del follow-up influenzano il risultato. Il dirigente associa quindi al numero una fonte, un responsabile, una periodicità e un'azione verificabile, evitando di premiare un miglioramento ottenuto restringendo artificiosamente il denominatore.
''';s=s[:pos]+block+s[pos:];save(p,s)
p=chapter(m,3);s=p.read_text(encoding='utf-8').replace('Questa spiegazione non autorizza a scegliere autonomamente una terapia: insegna come argomentare il rapporto tra prove e decisione.','Il manuale concorsuale insegna ad argomentare il rapporto fra prove e decisione. Nel caso reale la scelta clinica resta responsabilità del professionista abilitato, che esercita la propria autonomia entro competenze, evidenze, condizioni della persona e obblighi professionali.');save(p,s)
p=chapter(m,4);s=p.read_text(encoding='utf-8');pos=s.index('\n## ',s.index('## Mappa BANDO')+4);block='''
## Riconoscere gli eventi e scegliere lo strumento di analisi

Un **evento avverso** produce un danno correlato all'assistenza; non ogni evento avverso deriva da errore. Un **near miss** è un incidente che non determina danno, perché intercettato o per circostanze favorevoli. Un **evento sentinella** è particolarmente grave, potenzialmente evitabile e indicativo di un possibile problema di sistema: richiede analisi e azioni appropriate anche se osservato una sola volta. La lista e il protocollo ministeriale guidano la segnalazione attraverso **SIMES**, il sistema informativo nazionale per il monitoraggio degli errori in sanità. L'incident reporting interno e il flusso SIMES hanno funzioni collegate, ma non sono intercambiabili.

| Strumento | Quando parte | Domanda e risultato |
| --- | --- | --- |
| RCA, analisi delle cause | dopo un evento o criticità selezionata | quali fattori hanno consentito l'accaduto e quali barriere vanno rafforzate? |
| FMEA, analisi dei modi di guasto | prima dell'evento, su un processo | dove può fallire il processo, con quali effetti e quali controlli preventivi? |

**Applicazione.** In una somministrazione è stato selezionato il paziente sbagliato e il doppio controllo ha intercettato l'errore: è un near miss, non un danno da presumere. La RCA ricostruisce sequenza, identificatori, interfaccia, interruzioni e comunicazioni, senza fermarsi a «disattenzione». Prima di introdurre un nuovo sistema, la FMEA scompone prescrizione, selezione, preparazione e somministrazione; per ciascuna fase identifica possibili errori, effetti e capacità di intercettazione. Si può scegliere di rendere visibili due identificatori e impedire selezioni ambigue, quindi verificare errori e tempi. Un punteggio di priorità locale aiuta il confronto, ma non dimostra una probabilità clinica universale. Per il caso tecnologico e il collegamento fra evento, dispositivo e azione correttiva, riprendi «Tecnologie, dispositivi, apparecchiature e rischio» di M-SA04.
''';s=s[:pos]+block+s[pos:];save(p,s)
source('metodo-evidenze-sistema-nazionale-linee-guida-iss','Per il solo caso illustrativo di dispnea/dolore toracico SA03/06 sono stati confrontati [NICE NG158, valutazione della sospetta embolia polmonare](https://www.nice.org.uk/guidance/ng158/chapter/Recommendations), [NICE CG95, dolore toracico](https://www.nice.org.uk/guidance/cg95/resources/full-guideline-pdf-245282221) e [RCUK, circostanze speciali 2025](https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/special-circumstances-guidelines), limitatamente al riconoscimento dell’anafilassi. Fonti professionali internazionali, non registrazione SNLG italiana. Sostengono confronto delle ipotesi e verifiche discriminanti, non una prescrizione terapeutica per il paziente reale.')
p=chapter(m,6);s=p.read_text(encoding='utf-8');anchor='**Decisione.** Interrompo';block='''Il confronto può essere reso esplicito senza fingere una diagnosi certa:

| Ipotesi | Elementi che la sostengono o la rendono urgente | Dati che servono a discriminarla |
| --- | --- | --- |
| Embolia polmonare | dispnea acuta, ipossiemia, tachicardia e dolore; possibili conseguenze gravi | fattori di rischio, segni di trombosi, probabilità clinica e percorso diagnostico appropriato; un D-dimero isolato non conferma la diagnosi |
| Sindrome coronarica acuta | dolore toracico, variazione pressoria e dispnea | caratteri del dolore, ECG e biomarcatori nel percorso previsto; un primo ECG normale non basta a escluderla |
| Pneumotorace, anche iperteso se instabile | esordio acuto e compromissione respiratoria | asimmetria dei reperti e valutazione immediata; nell'instabilità il riconoscimento di una minaccia non deve attendere una routine diagnostica |
| Reazione anafilattica alla terapia | rapporto temporale con una dose e compromissione respiratoria/circolatoria | tempo dall'ultima esposizione, edema, broncospasmo e segni cutanei, che possono anche mancare; avere iniziato un farmaco tre giorni prima non dimostra il nesso |
| Infezione respiratoria con possibile sepsi | ipossiemia e compromissione generale possono essere compatibili | febbre o altri segni infettivi, reperti toracici, andamento e disfunzioni d'organo; la temperatura mancante non è temperatura normale |

Non sono ipotesi equiprobabili né un elenco esaustivo. Il dato disponibile non permette di escluderle; la gerarchia cambia quando arrivano anamnesi, esame e verifiche. La nuova terapia è una pista da esaminare, non una spiegazione che chiuda il caso.

''';s=s.replace(anchor,block+anchor);s=re.sub(r' Ogni nuovo claim clinico sostanziale riapre i gate di copertura, Humanizer e revisione\.','',s);save(p,s)
p=S/'deontologia-biologo-farmacista-psicologo-2026.md';s=p.read_text(encoding='utf-8').replace('nella revisione entrata in vigore il 1° dicembre 2023','nel testo vigente nuovamente applicabile dal 24 dicembre 2024, successivo alla decisione del Consiglio di Stato sul referendum 2023');s+='''
## Correzione della vigenza CNOP — 3 ottobre 2026

Confrontato il [testo attualmente indicato come vigente dal CNOP](https://www.psy.it/la-professione-psicologica/codice-deontologico-degli-psicologi-italiani/codice-deontologico-vigente/) con le proposizioni recepite: artt. 3–7 responsabilità, dignità, competenza, autonomia e attendibilità; 11–17 segreto e documentazione; 24 informazione/consenso; 25 strumenti diagnostici; 32 committenza e destinatario. I principi sintetizzati restano sostenuti dal testo vigente, senza recepire la premessa etica del codice 2023. Il [riscontro dell'Ordine siciliano](https://www.oprs.it/per-la-professione/codice-deontologico/) documenta il ritorno del precedente testo dal 24 dicembre 2024. Il PDF 2023 resta storico e non è fonte di vigenza.
''';save(p,s)
p=chapter(m,7);s=p.read_text(encoding='utf-8');s=s.replace('revisione entrata in vigore il 1° dicembre 2023','testo vigente indicato dal CNOP e nuovamente applicabile dal 24 dicembre 2024, verificato il 3 ottobre 2026');s=re.sub(r' Ogni nuovo verticale sostanziale riapre i gate di copertura, Humanizer e revisione\.','',s);s=re.sub(r'[^\n]*Humanizer[^\n]*\n','',s);save(p,s)
batch={}
for n,desc,files in [(28,'Distinti obbligo generale di inglese/informatica e modalità mobili; corretti esercizio, soluzione e rinvii SA04.',[chapter(m,1),chapter(m4,1)]),(29,'Inseriti punteggi e soglie nazionali DPR483 per quattro profili e DPR220 nei due moduli di comparto.',[chapter(m,1),chapter(m2,1),chapter(m4,1)]),(30,'Acquisita relazione ministeriale NSG valida, riconciliate esclusioni della source, aggiunto cruscotto originale e raccordo SA01.',[chapter(m,2),S/'governo-clinico-appropriatezza-hta-qualita-accreditamento.md']),(31,'Chiarita autonomia e responsabilità del medico abilitato distinta dai limiti del manuale.',[chapter(m,3)]),(32,'Definiti eventi, SIMES, RCA/FMEA e applicazione originale con rinvio SA04.',[chapter(m,4)]),(33,'Completato differenziale illustrativo con ipotesi, dati e verifiche discriminanti.',[chapter(m,6)]),(34,'Corretta vigenza CNOP e confrontati gli articoli pertinenti con il testo ufficiale attuale.',[chapter(m,7),S/'deontologia-biologo-farmacista-psicologo-2026.md'])]:
 batch[f'V07-{n:02}']={'change':desc,'files':[p.as_posix() for p in files],'evidence':'Rilettura del delta e riscontri ufficiali descritti nelle source; controlli step 15 e PDF pendenti.','status':'applicato'}
Path('artifacts/correzioni-collana-2026-10-02/VOL-07-batch06.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf-8')
