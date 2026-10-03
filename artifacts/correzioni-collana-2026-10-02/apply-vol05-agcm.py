from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02')
note='vol-05-agcm-verifica-2026-10-03'
Path('wiki/sources/'+note+'.md').write_text('''---
id: source-vol-05-agcm-verifica-2026-10-03
type: source
title: "VOL-05 — Antitrust, consumatori e competenze AGCM"
status: consolidated
domain: autorità indipendenti
topics: ["concorrenza", "consumatori", "rating", "conflitti di interessi"]
entities: ["AGCM", "Commissione europea"]
source_refs: ["sources/vol-05-istruttoria-verifica-2026-10-03.md", "sources/vol-05-sanzioni-giurisdizione-verifica-2026-10-03.md"]
book_refs: ["m-fc05-authority-indipendenti", "vol-05-authority-regolazione"]
confidence: 0.98
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["vol-05", "correzioni", "agcm"]
source_type: official_legislation_and_authority
source_date: 2026-10-03
authority_level: primary
---

# Perimetro verificato

Lettura integrale degli articoli 101–102 TFUE nell'EPUB ufficiale del Consiglio già archiviato (estrazione `norme-vol05/tfue-epub.txt`); legge 287/1990 artt. 2, 3, 6, 15-bis, 16; Codice del consumo artt. 20–27, 37-bis; legge 215/2004 artt. 1, 2, 3, 6 nei testi correnti Normattiva. Raw e URL/hash nei manifest principale e `agcm-specific-manifest.json`, cartella `wiki/raw/correzioni-vol05-2026-10-03`. Non dichiarata lettura integrale dei testi unici.

## Concorrenza

Articolo 101: oggetto ed effetto sono alternativi; i quattro requisiti del paragrafo 3 sono cumulativi. Articolo 102: dominanza distinta dall'abuso, quattro gruppi esemplificativi di condotte. Legge 287/1990 art. 6: SIEC, non limitato alla creazione/rafforzamento di dominanza. Articolo 15-bis: clemenza per cartelli segreti, tempestività/prova e cooperazione condizionano immunità o riduzione; coercizione esclude immunità. [AGCM, programma di clemenza](https://www.agcm.it/competenze/tutela-della-concorrenza/intese-e-abusi/programma-di-clemenza), [aggiornamento del 2025](https://www.agcm.it/media-e-comunicazione/dettaglio-notizia?id=a1200b3d-1395-4ce6-bdd3-aab387104d6b&parent=News&parentUrl=%2Fmedia-e-comunicazione%2Fnews): delibera 31467 del 25 febbraio 2025, applicazione dal 10 marzo ai procedimenti successivi. Non confondere con impegni o transazione.

[Soglie AGCM](https://www.agcm.it/per-le-imprese/Concorrenza/concentrazioni/soglie-di-fatturato): 595 milioni complessivi in Italia e 36 milioni individuali italiani per almeno due imprese, cumulativi, dal 16 marzo 2026, delibera 31873 del 10 marzo. Art. 16, comma 1-bis, potere sotto soglia con condizioni e sei mesi dal perfezionamento, richiesta di notifica entro trenta giorni. [Commissione, procedure concentrazioni](https://competition-policy.ec.europa.eu/mergers/procedures_en), letta la sezione dimensione UE: regolamento 139/2004 art. 1, prima e seconda combinazione, eccezione due terzi; non dichiarata lettura integrale del regolamento.

## Consumatore

La pubblicità «gratis» è articolo 23, comma 1, **lettera v)**, non p): quest'ultima riguarda sistemi promozionali piramidali. Si rettifica anche la proposta inesatta nel rilievo V05-15 originario. Articoli 23 e 26: pratiche considerate in ogni caso ingannevoli/aggressive, senza ripetere la prova della clausola generale, verificando comunque tutti i fatti della fattispecie.

D.Lgs. 20 febbraio 2026 n. 30, GU 56 del 9 marzo: entrata 24 marzo, **applicazione 27 settembre 2026**, art. 2 e nota di aggiornamento 57 degli artt. 21–23. Letta la nota nel raw art. 23; riscontro [GU ufficiale](https://www.gazzettaufficiale.it/eli/gu/2026/03/09/56/sg/pdf). Inserite solo due nuove fattispecie lette: asserzioni ambientali generiche senza prestazione riconosciuta dimostrabile e affermazioni climatiche sul prodotto fondate su compensazione delle emissioni. Non retrodatare l'applicazione.

[Regolamento AGCM 31356 del 5 novembre 2024](https://agcm.it/per-le-imprese/imprese-e-consumatori/regolamento-agcm-sulle-procedure-istruttorie-in-materia-di-tutela-del-consumatore): letti integralmente artt. 5–10, art. 17 comma 1. Chiusura ordinaria 180 giorni dal protocollo avvio, 240 nei casi previsti, proroghe/sospensioni; impegni 45 giorni, controdeduzioni almeno 20 giorni. Art. 27 commi 7, 9 e 9-bis: limiti impegni, 5.000–10 milioni regime ordinario e diverso massimo 4% nel coordinamento UE; nessun massimo universale. Art. 37-bis: accertamento, pubblicazione e sanzioni; validità clausola e danni restano al giudice ordinario.

## Rating e conflitti

[FAQ regolamento rating 2026](https://www.agcm.it/competenze/rating-di-legalita/FAQ-Regolamento-Rating-2026): lette sezioni I e II. Sede operativa italiana, almeno due milioni di fatturato nel periodo definito, almeno due anni iscrizione; punteggio una–tre stelle; durata tre anni per rating rilasciati dal 16 marzo 2026. Non estesa retroattivamente ai precedenti rating. Fonte regolamentare 31812 del 27 gennaio 2026.

Legge 215/2004 distingue incompatibilità, conflitto collegato ad atto/omissione e poteri AGCM: l'Autorità promuove i provvedimenti dell'amministrazione competente e riferisce al Parlamento, non «revoca il Governo». I due rami dell'art. 3 vanno conservati: incompatibilità dell'art. 2 oppure incidenza patrimoniale specifica/preferenziale con danno pubblico. [Pagina AGCM](https://www.agcm.it/competenze/conflitto-di-interessi/) di orientamento, testo decisivo nei quattro articoli letti.

Collegamenti: [[topics/authority-rettifiche-2026]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/08-agcm-concorrenza-consumatore-pratiche-scorrette]].
''',encoding='utf8')
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## Antitrust e consumatori\n\n[[sources/'+note+']] consolida fattispecie, soglie 2026, novità verdi applicabili dal 27 settembre, procedura consumer, rating e conflitti. Corretto il rinvio sulla gratuità: articolo 23, lettera v).\n',encoding='utf8')
p=B/'chapters/08-agcm-concorrenza-consumatore-pratiche-scorrette.md';s=p.read_text(encoding='utf8')
pos=s.index('![Figura 8.3')
s=s[:pos]+'''### Intese: oggetto, effetti ed efficienze

L'articolo **101 TFUE** riguarda accordi fra imprese, decisioni di associazioni e pratiche concordate che possano incidere sugli scambi fra Stati membri. L'articolo **2 della legge 287/1990** considera il mercato nazionale o una sua parte rilevante. Il coordinamento può essere orizzontale fra concorrenti oppure verticale fra livelli della filiera: non occorre un contratto scritto, ma il solo parallelismo dei prezzi non prova un'intesa.

La restrizione **per oggetto** rivela, nel contesto giuridico ed economico, un sufficiente grado di dannosità concorrenziale: un cartello di fissazione dei prezzi o ripartizione dei clienti è l'esempio tipico. Una volta dimostrato l'oggetto restrittivo, non è necessario provare anche effetti concreti. Se manca tale qualificazione si verificano gli **effetti**, considerando il funzionamento del mercato e il confronto con ciò che accadrebbe senza l'accordo. «Oggetto o effetto» non significa «oggetto ed effetto» e non autorizza a dedurre la restrizione dalla sola intenzione dichiarata delle parti.

L'articolo 101, paragrafo 3, richiede **quattro condizioni cumulative** per l'inapplicabilità del divieto: miglioramento della produzione/distribuzione o progresso tecnico/economico; congrua partecipazione degli utilizzatori ai benefici; restrizioni indispensabili; concorrenza non eliminata per una parte sostanziale dei prodotti. Un accordo che riduce i costi ma trasferisce ogni vantaggio alle imprese non soddisfa il secondo requisito. L'impresa deve dimostrare le condizioni: «produce efficienze» è l'inizio della valutazione, non una deroga automatica.

La **clemenza**, disciplinata dall'articolo 15-bis e seguenti e dalla comunicazione AGCM del 2025, incentiva chi rivela la propria partecipazione a un cartello segreto. L'immunità richiede priorità, elementi probatori qualificati e le ulteriori condizioni di cooperazione; chi ha costretto altre imprese a partecipare non può ottenerla. Una collaborazione successiva può consentire una riduzione secondo le condizioni previste. Non è l'impegno a cambiare condotta del capitolo 6 e non cancella automaticamente responsabilità o diritti risarcitori in altri ambiti.

### Abuso: il potere di mercato non basta

L'articolo **102 TFUE** e l'articolo **3 della legge 287/1990** vietano lo sfruttamento abusivo di una posizione dominante. La dominanza è la capacità di comportarsi in misura apprezzabile indipendentemente da concorrenti, clienti e consumatori: quote e loro stabilità, barriere, ingresso, sostituibilità e potere contrattuale della domanda vanno letti insieme. Nessuna percentuale isolata sostituisce l'analisi.

Le fattispecie comprendono prezzi o condizioni inique, limitazioni di produzione o sviluppo tecnico a danno dei consumatori, condizioni discriminatorie per prestazioni equivalenti che producono svantaggi concorrenziali e vendite abbinate prive del nesso richiesto. In un caso di accesso alla rete, differenze di costo o rischio possono spiegare condizioni diverse: occorre verificare equivalenza delle prestazioni e giustificazioni obiettive, senza presumere che ogni differenza sia discriminazione. Non ogni tutela del concorrente coincide con tutela della concorrenza.

### Concentrazioni: test sostanziale e competenza

Fusione e acquisizione di controllo modificano stabilmente la struttura del mercato. Il test **SIEC** domanda se l'operazione ostacoli in modo significativo la concorrenza effettiva: la creazione o il rafforzamento di dominanza è un caso importante, ma non esaurisce il test dell'articolo 6 della legge 287/1990. L'AGCM considera anche concorrenza potenziale, ingresso, scelta di fornitori e utenti, innovazione ed efficienze favorevoli ai consumatori. Può vietare o autorizzare con misure idonee; non deve dimostrare un illecito già commesso come in un procedimento per abuso.

**Soglie nazionali verificate al 3 ottobre 2026.** Dal 16 marzo 2026 la notifica ordinaria richiede entrambe le condizioni: fatturato complessivo italiano delle imprese interessate **superiore a 595 milioni di euro** e fatturato italiano individuale **superiore a 36 milioni** per almeno due imprese. Sono parametri aggiornabili annualmente, non soglie eterne. Nel caso didattico A = 570 milioni e B = 40 milioni, entrambi realizzati in Italia, il totale 610 supera 595 e ciascuna supera 36: salvo competenza UE o altre condizioni, le soglie nazionali sono soddisfatte.

Essere sotto soglia non garantisce l'assenza di controllo. L'articolo 16, comma 1-bis, consente la richiesta di notifica entro trenta giorni quando è superata una sola soglia nazionale oppure il fatturato mondiale complessivo supera 5 miliardi, vi sono concreti rischi per la concorrenza nazionale o una sua parte rilevante e non sono trascorsi oltre sei mesi dal perfezionamento. Vanno verificati insieme i presupposti, non soltanto il numero dei milioni.

La dimensione **UE** segue invece il regolamento 139/2004. La prima combinazione richiede oltre 5 miliardi di fatturato mondiale complessivo e oltre 250 milioni di fatturato UE per ciascuna di almeno due imprese. La combinazione alternativa richiede oltre 2,5 miliardi mondiali; oltre 100 milioni complessivi in ciascuno di almeno tre Stati membri; oltre 25 milioni per ciascuna di almeno due imprese in ciascuno di quei tre Stati; oltre 100 milioni UE per ciascuna di almeno due imprese. In entrambi i casi opera l'eccezione se ogni impresa realizza oltre due terzi del proprio fatturato UE in un unico e medesimo Stato membro. La Commissione è il riferimento ordinario per la dimensione UE, salvi i meccanismi di rinvio: non si sommano automaticamente due notifiche nazionali e UE per lo stesso titolo.

'''+s[pos:]
pos=s.index('## N-MF05-08-03')
s=s[:pos]+'''### Le liste nere precedono il test generale

Gli articoli **23 e 26 del Codice del consumo** elencano pratiche considerate in ogni caso rispettivamente ingannevoli e aggressive. Bisogna provarne gli elementi concreti, ma non ripetere ogni volta il test generale sull'alterazione del consumatore medio. Esempi: falsa disponibilità per un tempo molto limitato per forzare la scelta immediata; recensioni falsamente attribuite a consumatori; esortazioni pubblicitarie dirette ai bambini affinché comprino o convincano gli adulti. Le ultime rientrano nell'articolo 26, lettera e).

Per l'offerta «gratis» o «senza costi», la disposizione specifica è **articolo 23, comma 1, lettera v)**: è vietato descrivere così il prodotto quando il consumatore deve pagare somme ulteriori rispetto al costo inevitabile per rispondere all'offerta e ritirare o ricevere il prodotto. Un canone mensile obbligatorio è diverso da quei costi. Se la gratuità riguarda davvero un periodo o una componente distinti, occorre ricostruire la promessa effettiva e le condizioni, senza scegliere una qualificazione dalla sola parola isolata. Restano possibili profili di azioni od omissioni ingannevoli degli articoli 21–22.

Dal **27 settembre 2026** si applicano le modifiche del D.Lgs. 30/2026 sulle informazioni ambientali e sulla durabilità. Fra le nuove pratiche vietate in ogni caso figurano asserzioni ambientali generiche non sostenute dalla dimostrazione della prestazione ambientale eccellente riconosciuta pertinente e affermazioni secondo cui un prodotto avrebbe impatto climatico neutro, ridotto o positivo sulla base della compensazione delle emissioni. Per giudicare una campagna bisogna acquisire messaggio, fondamento della dichiarazione e data: entrata in vigore del decreto e data di applicazione non coincidono.

'''+s[pos:]
pos=s.index('### Competenze vicine:')
s=s[:pos]+'''### Procedura consumer: termini e rimedi distinti

Il regolamento AGCM **31356 del 5 novembre 2024** prevede un termine ordinario di 180 giorni dal protocollo della comunicazione di avvio; diventano 240 nei casi dell'articolo 8, fra cui professionista con sede all'estero o infrazioni del regolamento UE sulla cooperazione consumeristica. Proroghe e sospensioni richiedono i presupposti previsti. Non sono i tre mesi per proporre impegni antitrust: nel consumer gli impegni si presentano entro **45 giorni** dalla ricezione dell'avvio. L'Autorità può rifiutarli, fra l'altro, per grave e manifesta scorrettezza o per interesse all'accertamento. La contestazione conclusiva degli addebiti deve lasciare almeno **20 giorni** per controdeduzioni.

L'articolo 27 prevede, nel regime ordinario, una sanzione da 5.000 a 10 milioni di euro; per le fattispecie coordinate UE indicate nel comma 9-bis il massimo è invece il 4% del fatturato annuo rilevante. Non si applica indistintamente il massimo antitrust del 10% mondiale. Nei settori regolati l'AGCM esercita la competenza sulle pratiche scorrette acquisendo il parere del regolatore competente, che conserva i propri poteri sulle violazioni della regolazione. Il consumatore può chiedere al giudice ordinario i rimedi individuali previsti, inclusi, quando applicabili, danni, riduzione del prezzo o risoluzione.

'''+s[pos:]
pos=s.index('Queste distinzioni consentono')
s=s[:pos]+'''L'articolo 37-bis non attribuisce soltanto un potere informativo: l'accertamento della vessatorietà comporta pubblicazione ed è assistito dalle sanzioni previste. La validità della clausola nel rapporto e il risarcimento individuale restano invece al giudice ordinario. L'interpello preventivo non elimina la responsabilità dell'impresa verso i consumatori.

Per il rating, il regolamento **31812 del 27 gennaio 2026**, applicabile dal 16 marzo, richiede cumulativamente sede operativa in Italia, almeno due milioni di euro di fatturato nel periodo individuato dalla disciplina e iscrizione nel registro delle imprese da almeno due anni. Il punteggio va da una a tre stelle, secondo requisiti di legalità e premiali. I rating rilasciati dal 16 marzo 2026 durano **tre anni** e sono rinnovabili: non si estende automaticamente questa durata ai rating precedenti. Il riconoscimento può rilevare nell'accesso a credito e finanziamenti; non sostituisce requisiti di gara o controlli sull'impresa.

### Conflitti di interessi dei titolari di Governo

La **legge 215/2004** riguarda Presidente del Consiglio, ministri, viceministri, sottosegretari e i commissari straordinari del Governo indicati dalla legge. L'incompatibilità dell'articolo 2 attiene al cumulo con incarichi e attività vietati, per esempio compiti di gestione in società lucrative. La mera proprietà di una partecipazione non va equiparata a un incarico gestorio.

L'articolo 3 collega il conflitto alla partecipazione a un atto, anche alla proposta, o all'omissione di un atto dovuto: rileva la situazione di incompatibilità oppure l'incidenza specifica e preferenziale sul patrimonio del titolare, coniuge, parenti entro il secondo grado o imprese controllate, con danno all'interesse pubblico. Perciò una misura generale vantaggiosa per un intero settore non prova da sola il secondo tipo di conflitto; servono i suoi elementi specifici.

L'AGCM accerta e vigila, promuove presso i soggetti competenti rimozione, decadenza o sospensione previste, e riferisce al Parlamento. Nei confronti dell'impresa che consapevolmente si avvantaggia dell'atto in conflitto può diffidare e, in caso di inottemperanza, sanzionare nei limiti dell'articolo 6. Non revoca direttamente la carica di Governo e non sostituisce il giudice penale. Questo procedimento non coincide con le incompatibilità dei componenti delle authority studiate nel capitolo 2.

'''+s[pos:]
s=s.replace('La prima operazione non è scegliere subito l\'etichetta più grave. La condotta descritta presenta, anzitutto, un possibile profilo di pratica commerciale ingannevole:',"La prima verifica riguarda la fattispecie specifica dell'articolo 23, lettera v): il canone obbligatorio contraddice la promessa di gratuità e non è un mero costo inevitabile di risposta, ritiro o consegna. Vanno provati contenuto e portata della promessa; si valutano inoltre gli articoli 21–22:")
a=s.index('### Prova di trasferimento');s=s[:a]+'''## N-MF05-08-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** È dimostrato un cartello di ripartizione dei clienti restrittivo per oggetto. Per applicare l'articolo 101 occorre provare anche effetti concreti?

**Risposta corretta:** no: oggetto ed effetto sono alternativi, ferma la verifica degli altri presupposti, incluso l'incidenza potenziale sugli scambi UE. Un'intesa con efficienze non è automaticamente lecita: il paragrafo 3 richiede tutte e quattro le condizioni.

**Quesito 2.** A e B realizzano in Italia 570 e 40 milioni. Quali soglie nazionali del 2026 superano?

**Risposta corretta:** il totale è 610, superiore a 595; entrambe superano 36. Le due condizioni cumulative sono soddisfatte. Si controllano ancora natura di concentrazione, calcolo del fatturato e competenza UE: il dato non decide la compatibilità sostanziale.

**Quesito 3.** Un'impresa dominante applica prezzi differenti a due clienti. L'abuso è già provato?

**Risposta corretta:** no. Occorre verificare equivalenza delle prestazioni, svantaggio concorrenziale e possibili giustificazioni, come differenze effettive di costo. Dominanza e differenza di prezzo non sostituiscono la prova della condotta abusiva.

**Quesito 4.** Un servizio è definito «gratis», ma impone da subito un canone. Quale norma specifica si controlla per prima?

**Risposta corretta:** articolo 23, comma 1, lettera v), del Codice del consumo. Un canone non è il costo inevitabile per rispondere, ritirare o ricevere il prodotto. La fattispecie è nella lista delle pratiche in ogni caso ingannevoli; vanno provati i fatti che la integrano, senza limitarla al test generale dell'articolo 20.

**Quesito 5.** Un professionista propone impegni consumeristici dopo sessanta giorni dall'avvio, richiamando il termine antitrust di tre mesi. Il richiamo è corretto?

**Risposta corretta:** no. Nel regolamento consumer 31356/2024 il termine di presentazione è quarantacinque giorni dalla ricezione dell'avvio. Istituti simili mantengono termini e condizioni propri; l'Autorità non è comunque obbligata ad accettare la proposta.

**Quesito 6.** Il possesso di quote societarie da parte di un ministro equivale sempre a incompatibilità e autorizza AGCM a revocarlo?

**Risposta corretta:** no. Proprietà e gestione si distinguono; si verificano le attività vietate e gli elementi dell'atto od omissione in conflitto. L'AGCM esercita i poteri della legge 215/2004 e riferisce al Parlamento, senza un generale potere di revoca della carica di Governo.

### Caso ragionato di chiusura

**Traccia.** A acquisisce il controllo di B: fatturati italiani 570 e 40 milioni, nessun altro fatturato mondiale. Il nuovo gruppo annuncia «abbonamento gratis», imponendo da subito 12 euro mensili. Un concorrente chiede all'AGCM di vietare la concentrazione perché il messaggio prova la dominanza e di rimborsare personalmente tutti gli utenti. Redigi una nota in tre punti.

**Soluzione.** 1. Le soglie nazionali sono entrambe superate; quelle UE, dati i fatturati dichiarati, no. Si esamina l'operazione con il test SIEC: il messaggio pubblicitario non dimostra l'ostacolo significativo alla concorrenza. 2. La pubblicità richiede verifica specifica dell'articolo 23, lettera v), acquisendo campagna, condizioni e percorso di adesione; può integrare una pratica in ogni caso ingannevole. L'eventuale abuso richiederebbe un'analisi autonoma, non deducibile dalla gratuità fittizia. 3. L'AGCM può esercitare poteri consumeristici e sanzionatori, ma il risarcimento o gli altri rimedi individuali spettano alle sedi competenti; non si promette un rimborso liquidato dall'Autorità.

**Autovalutazione:** un punto per le soglie calcolate, uno per SIEC distinto dall'abuso, uno per articolo 23, lettera v), uno per la separazione dei rimedi.

**Riferimenti normativi e professionali.** Articoli 101–102 TFUE; legge 287/1990, articoli 2–6, 14–16; regolamento CE 139/2004; Codice del consumo, articoli 20–27 e 37-bis, come modificato dal D.Lgs. 30/2026; legge 215/2004; regolamenti AGCM 31356/2024 e 31812/2026; comunicazione clemenza 31467/2025; delibera soglie 31873/2026. [AGCM, soglie vigenti](https://www.agcm.it/per-le-imprese/Concorrenza/concentrazioni/soglie-di-fatturato). Verifica al 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/'+note+'.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/'+note+'.md", "wiki/topics/authority-rettifiche-2026.md", ',1);p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,9));d['chaptersReadThisCycle']=list(range(1,9));d['findingsFullyApplied']+=['V05-14','V05-15'];d['findingsPartiallyApplied']['V05-02']='Capitoli 1–8: 48 quesiti e 8 casi specifici';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][7]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('Applied chapter 8, source/topic first; six specific questions and case.')
