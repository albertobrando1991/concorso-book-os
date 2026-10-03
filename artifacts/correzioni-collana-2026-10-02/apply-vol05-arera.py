from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02');note='vol-05-arera-verifica-2026-10-03'
Path('wiki/sources/'+note+'.md').write_text('''---
id: source-vol-05-arera-verifica-2026-10-03
type: source
title: "VOL-05 — ARERA: ruoli tariffari, qualità e tutela"
status: consolidated
domain: servizi pubblici regolati
topics: ["tariffe", "qualità", "unbundling", "conciliazione"]
entities: ["ARERA", "Acquirente Unico"]
source_refs: ["sources/arera-energia-gas-acqua-rifiuti-tariffe-2026-07-24.md", "sources/vol-05-reti-ue-verifica-2026-10-03.md"]
book_refs: ["m-fc05-authority-indipendenti", "vol-05-authority-regolazione"]
confidence: 0.98
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["vol-05", "correzioni", "arera"]
source_type: official_regulation_and_guidance
source_date: 2026-10-03
authority_level: primary
---

# Verifiche e limiti

[Delibera 397/2025/R/rif](https://www.arera.it/fileadmin/allegati/docs/25/397-2025-R-rif.pdf), MTR-3 2026–2029: acquisito PDF 48 pagine, letto art. 7 alle pp. 42–45; non lettura integrale di premesse/allegato tecnico. Gestore predispone; ETC valida con terzietà, assume determinazioni e trasmette; ARERA verifica coerenza regolatoria e approva. Art. 7.11 definitività di specifici parametri ETC nei limiti del metodo, 7.12 termine 180 giorni salvo ulteriori informazioni, 7.13 approvazione diretta 90 giorni con requisiti, 7.14 applicazione nel frattempo dei massimi locali. Non confondere approvazione della predisposizione con deliberazione di ogni aliquota TARI. [Raccolta 2026](https://www.arera.it/comunicati-operatore/dettaglio/raccolta-dati-tariffa-rifiuti-pef-aggiornamento-2026-2029) identifica ETC: EGA operativo o altri enti individuati dalla disciplina, incluso Comune nei casi pertinenti.

[MTI-4 e qualità tecnica](https://www.arera.it/en/comunicati-stampa/dettaglio/acqua-nuovo-metodo-tariffario-mti-4-e-nuove-regole-per-la-qualita-tecnica): 639/2023/R/idr, periodo 2024–2029; aggiornamento RQTI 637/2023. [Servizio idrico, informazioni generali](https://www.arera.it/single-digital-gateway-acqua) conferma risposta al reclamo 30 giorni lavorativi. RQSII 655/2015 e RQTI 917/2017 successive modifiche: distinzione standard di prestazione/indicatori infrastrutturali. L'esempio numerico del capitolo è interamente didattico e non riproduce il MTR-3: 1.120.000 − 80.000 = 1.040.000; tetto convenzionale 1.000.000 × 1,03 = 1.030.000; differenza 10.000; unità equivalenti 10.000 → 103 euro. Nessun coefficiente vigente inventato.

[Conciliazione ARERA](https://www.arera.it/consumatori/conciliazione/servizio-conciliazione-domande-e-risposte), verificati i quesiti su natura, accesso, partecipazione, durata ed esiti. Reclamo scritto e risposta insoddisfacente oppure 40 giorni, 50 idrico, 60 rifiuti. Non sono termini di risposta al reclamo. Tentativo obbligatorio nei settori previsti da TICO, rifiuti transitoriamente facoltativo e alternativo a seconda istanza Sportello; partecipazione gestore rifiuti facoltativa. Durata 90 giorni solari dalla domanda completa, proroga massima 60; accordo rifiuti transattivo, distinto dal titolo esecutivo degli altri casi previsti. Esclusi, fra l'altro, soli profili tributari e qualità dell'acqua. Non dichiarata lettura completa del TICO.

[TIUF 296/2015](https://www.arera.it/atti-e-provvedimenti/dettaglio/15/296-15), [TIUC 137/2016](https://www.arera.it/allegati/schede/137-16st.pdf), schede istituzionali lette nei passaggi definitori: separazione contabile, funzionale e proprietaria non equivalenti; non estendere obblighi delle imprese verticalmente integrate a tutti i settori. [Telecalore](https://www.arera.it/area-operatori/teleriscaldamento/teleriscaldamento-e-teleraffrescamento): letta sezione dei poteri attribuiti dal D.Lgs. 102/2014, incluse continuità, tariffe, trasparenza e misurazione.

Raw/hash in `norme-vol05/arera-manifest.json`. Rinvii: [[topics/authority-rettifiche-2026]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/09-arera-energia-gas-acqua-rifiuti-tariffe]].
''',encoding='utf8')
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## ARERA: istruttoria tariffaria e tutela\n\n[[sources/'+note+']] distingue predisposizione/validazione/approvazione, MTR-3 e MTI-4, qualità, tre separazioni e termini di accesso alla conciliazione. Caso numerico dichiarato didattico.\n',encoding='utf8')
p=B/'chapters/09-arera-energia-gas-acqua-rifiuti-tariffe.md';s=p.read_text(encoding='utf8').replace('occorre a loro volta distinguere','occorre a sua volta distinguere')
pos=s.index('In un concorso, il candidato')
s=s[:pos]+'''Il perimetro include inoltre **teleriscaldamento e teleraffrescamento**, secondo il D.Lgs. 102/2014: reti che distribuiscono energia termica o frigorifera a più edifici. ARERA interviene, nei limiti attribuiti, su continuità, sicurezza, qualità, allacciamento e scollegamento, trasparenza dei prezzi, tariffe, contabilizzazione e fatturazione. Non si tratta della regolazione di ogni singolo impianto termico domestico.

'''+s[pos:]
pos=s.index('![Figura 9.3')
s=s[:pos]+'''### Dal PEF rifiuti alla decisione: chi fa che cosa

Il **piano economico-finanziario (PEF)** rappresenta costi, ricavi e fabbisogni del servizio per il periodo regolatorio; non è la fattura della singola famiglia. Nell'articolo 7 della delibera **397/2025/R/rif**, che approva MTR-3 per il 2026–2029, la sequenza è precisa:

1. Il **gestore** predispone il PEF e i documenti a supporto: dati contabili, dichiarazione di veridicità e relazione di riconciliazione.
2. L'**ente territorialmente competente (ETC)** valida completezza, coerenza e congruità, con i necessari profili di terzietà rispetto al gestore; può integrare o modificare motivatamente dopo confronto con quest'ultimo. L'ETC è l'ente di governo d'ambito operativo oppure il diverso soggetto competente per legge, anche il Comune nei casi previsti: non una sigla attribuibile liberamente al gestore.
3. L'organismo competente assume le determinazioni tariffarie e trasmette la predisposizione ad **ARERA**; per gli impianti indicati dalla delibera opera il soggetto competente individuato, Regione o altro ente da essa designato.
4. ARERA verifica la **coerenza regolatoria** e approva, eventualmente con modifiche ed effetti conseguenti. Specifici parametri decisi dall'ETC nei limiti del metodo hanno l'efficacia prevista dal comma 7.11; fino all'approvazione si applicano i massimi determinati dagli organismi competenti secondo il comma 7.14.

Quindi è inesatto dire sia «ARERA non approva nulla» sia «ARERA delibera ogni aliquota TARI comunale». La predisposizione regolatoria e l'articolazione dei corrispettivi all'utenza sono passaggi distinti; il Comune conserva le competenze che la disciplina tributaria e tariffaria gli attribuisce. Né l'approvazione del PEF trasforma ogni costo di bilancio in costo riconoscibile.

### Un calcolo tariffario trasparente

**Esempio esclusivamente didattico:** si usa un metodo semplificato, non la formula MTR-3. Le entrate precedenti sono 1.000.000 euro. Il gestore presenta 1.120.000 euro; la verifica esclude 80.000 di costi estranei o già conteggiati. Restano **1.040.000 euro** giustificati nel modello. Un limite convenzionale del 3% dà **1.030.000 euro**: il fabbisogno supera il tetto di 10.000. Non basta dichiarare «costi +12%» per applicare +12% agli utenti; la decisione deve risolvere lo scostamento secondo il metodo applicabile, senza inventare una deroga.

Assumendo 10.000 unità equivalenti, tutte identiche soltanto nell'esercizio, il ricavo medio coerente con 1.030.000 è **103 euro per unità**, contro 100 precedenti. Nella realtà unità domestiche/non domestiche, quote fisse/variabili, categorie e criteri di riparto non sono uniformi: 103 euro non è la TARI di ogni utenza. Il calcolo verifica tre competenze separate: ammissibilità dei costi, limite alle entrate e articolazione all'utente.

Per l'acqua il riferimento è **MTI-4, delibera 639/2023/R/idr, periodo 2024–2029**. Non si applica MTR-3 al servizio idrico. Il metodo tariffario si coordina con RQSII, qualità contrattuale, e RQTI, qualità tecnica: una perdita di rete e un reclamo senza risposta richiedono indicatori e rimedi differenti. Il programma degli interventi collega risorse e obiettivi, mentre la validazione verifica che i dati permettano di misurarli.

'''+s[pos:]
pos=s.index('![Figura 9.4')
s=s[:pos]+'''### Reclamo e conciliazione: soglie temporali diverse

Il **reclamo scritto** va prima all'operatore o gestore, identifica utenza, fatti, documenti e richiesta. Per esempio, nel servizio idrico la risposta motivata è dovuta entro **30 giorni lavorativi** dal ricevimento. Questo termine non va confuso con il periodo per accedere alla conciliazione in assenza di risposta.

Al Servizio Conciliazione si accede dopo una risposta scritta insoddisfacente oppure, senza risposta, dopo **40 giorni dall'invio** del reclamo per energia e telecalore, **50 per l'idrico**, **60 per i rifiuti urbani**. La risposta insoddisfacente può consentire l'accesso prima della scadenza indicata. Si allegano reclamo, prova dell'invio, risposta se disponibile, fatture e documenti pertinenti. I termini qui riportati sono verificati al 3 ottobre 2026.

Il TICO prevede il tentativo obbligatorio come condizione per l'azione giudiziaria nelle controversie comprese nel suo ambito per energia, idrico e telecalore. Nei **rifiuti urbani**, nella disciplina transitoria verificata, è facoltativo e alternativo al reclamo di seconda istanza presso lo Sportello; anche la partecipazione del gestore è facoltativa. Non si trasferisce ai rifiuti l'obbligo di partecipazione degli altri operatori. Sono esclusi, fra l'altro, i soli profili tributari/fiscali e le controversie sulla qualità dell'acqua: una contestazione del tributo non diventa conciliabile soltanto perché compare sulla bolletta rifiuti.

La procedura dura ordinariamente al massimo **90 giorni solari** dalla domanda completa, prorogabili fino a 60 nei casi previsti. Il conciliatore facilita l'accordo e può proporre una soluzione su richiesta concorde; le parti restano libere di accettare. L'accordo ha l'efficacia prevista dal settore: nel regime transitorio rifiuti è una transazione, mentre nei casi ordinari previsti dal TICO il verbale costituisce titolo esecutivo. Un indennizzo automatico per mancato standard, quando previsto, non presuppone la prova dell'intero danno e non ne coincide con il risarcimento: prima si identifica prestazione, ritardo, cause di esclusione e misura settoriale.

'''+s[pos:]
pos=s.index('Il Testo Integrato Unbundling Contabile')
s=s[:pos]+'''La parola *unbundling* comprende però separazioni diverse:

| Separazione | Oggetto e funzione |
| --- | --- |
| Contabile | Costi, ricavi, attività e transazioni riconoscibili separatamente; consente di controllare sussidi incrociati. |
| Funzionale | Autonomia delle decisioni e della gestione dell'attività regolata nei confronti delle altre attività del gruppo; tutela la neutralità della rete e delle informazioni. |
| Proprietaria | Assetto del controllo e della proprietà separato secondo il modello richiesto dalla normativa; non si ottiene aprendo soltanto conti distinti. |

Un gruppo che conserva la stessa direzione commerciale ma contabilizza separatamente rete e vendita ha introdotto una separazione contabile, non necessariamente quella funzionale o proprietaria. Obblighi, esenzioni e modelli consentiti dipendono da attività e settore: il **TIUF 296/2015/R/com** per energia e gas non si applica indistintamente a ogni gestore idrico o rifiuti. La contabilità separata serve comunque a controllare l'origine dei costi, non ad approvarne automaticamente il recupero tariffario.

'''+s[pos:]
s=s.replace('La risposta è incompleta. Occorre prima individuare',"L'affermazione è errata: confonde la deliberazione locale con l'approvazione regolatoria e presume il recupero di tutti i costi. Il gestore predispone, l'ETC valida e assume le determinazioni, ARERA verifica e approva secondo l'articolo 7. Occorre individuare")
a=s.index("### Checklist per una nota d'ufficio");s=s[:a]+'''## N-MF05-09-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Chi predispone e chi valida il PEF nel procedimento MTR-3?

**Risposta corretta:** il gestore predispone e documenta; l'ETC valida con terzietà, assume le determinazioni e trasmette ad ARERA, che verifica coerenza e approva secondo il metodo. L'ETC non è automaticamente il gestore e ARERA non delibera ogni aliquota comunale.

**Quesito 2.** Nel modello del capitolo, richiesta 1.120.000, esclusioni 80.000 e tetto 1.030.000: quale importo supera il limite e di quanto?

**Risposta corretta:** il costo giustificato di 1.040.000 supera il tetto di 10.000. La crescita dichiarata del 12% non determina la tariffa; a 10.000 unità equivalenti il tetto darebbe 103 euro medi, nel solo modello didattico.

**Quesito 3.** MTI-4 e MTR-3 sono due nomi del medesimo metodo?

**Risposta corretta:** no. MTI-4 riguarda l'idrico 2024–2029; MTR-3 i rifiuti 2026–2029. Periodi e filiere restano diversi e i coefficienti non si trasferiscono.

**Quesito 4.** Conti separati rete/vendita provano separazione proprietaria?

**Risposta corretta:** no. Rendono leggibili le attività contabili; l'autonomia delle decisioni attiene alla separazione funzionale, mentre proprietà e controllo appartengono alla separazione proprietaria secondo il modello legale.

**Quesito 5.** Un reclamo idrico è senza risposta da 35 giorni solari. Basta applicare il termine energetico di 40 giorni per programmare l'accesso alla conciliazione?

**Risposta corretta:** no. Senza risposta la soglia idrica è 50 giorni dall'invio; una risposta insoddisfacente consente l'accesso prima. I 30 giorni lavorativi per rispondere al reclamo sono un termine diverso, con diversa unità di computo.

**Quesito 6.** Nel regime rifiuti verificato, conciliazione e partecipazione del gestore sono obbligatorie come nell'energia?

**Risposta corretta:** no, sono facoltative nella disciplina transitoria; l'accordo ha valore transattivo. La conciliazione non è una sentenza e non è il canale per soli profili tributari.

### Caso ragionato di chiusura

**Traccia.** Il gestore rifiuti propone un incremento del 12% sulla base dei dati del modello. L'ETC dichiara che non può modificare i costi. Un utente presenta un reclamo sul servizio, senza risposta da 65 giorni, e sostiene che il conciliatore debba condannare il gestore assente. Correggi le tre proposizioni.

**Soluzione.** Il controllo esclude 80.000: restano 1.040.000, contro il tetto convenzionale di 1.030.000; nessun aumento del 12% è automatico. L'ETC deve validare e può integrare o modificare motivatamente dopo procedura partecipata, poi trasmettere per la verifica ARERA. Il reclamo supera i 60 giorni richiesti per l'accesso senza risposta, purché ricorrano gli altri presupposti e non sia pendente il canale alternativo incompatibile. Nel regime transitorio la partecipazione del gestore è facoltativa: il conciliatore non pronuncia una condanna per contumacia, ma gestisce l'esito previsto dalla procedura.

**Autovalutazione:** un punto per ciascun ruolo corretto, uno per il calcolo di 10.000 euro, uno per accesso e natura della conciliazione.

**Riferimenti normativi e professionali.** Legge 481/1995; legge 205/2017, articolo 1, comma 527; D.Lgs. 102/2014; MTR-3, delibera 397/2025/R/rif, articolo 7; MTI-4, delibera 639/2023/R/idr; RQSII 655/2015/R/idr e RQTI 917/2017/R/idr, successive modifiche; TIUC 137/2016/R/com; TIUF 296/2015/R/com; TICO 209/2016/E/com, successive modifiche; [ARERA, condizioni del Servizio Conciliazione](https://www.arera.it/consumatori/conciliazione/servizio-conciliazione-domande-e-risposte), verificate il 3 ottobre 2026. Per REMIT, regolamento UE 1227/2011 come modificato dal regolamento UE 2024/1106.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/'+note+'.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/'+note+'.md", "wiki/topics/authority-rettifiche-2026.md", ',1);p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,10));d['chaptersReadThisCycle']=list(range(1,10));d['findingsFullyApplied']+=['V05-16','V05-17'];d['findingsPartiallyApplied']['V05-02']='Capitoli 1–9: 54 quesiti e 9 casi specifici';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][8]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Applied chapter 9.')
