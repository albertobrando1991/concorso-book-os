from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02')
Path('wiki/sources/vol-05-istruttoria-verifica-2026-10-03.md').write_text('''---
id: source-vol-05-istruttoria-verifica-2026-10-03
type: source
title: "VOL-05 — Istruttoria e ispezioni: verifica del 3 ottobre 2026"
status: consolidated
domain: diritto amministrativo della regolazione
topics: ["vigilanza", "istruttoria", "ispezioni", "diritti della difesa"]
entities: ["AGCM", "Garante", "Corte di giustizia UE"]
source_refs: ["sources/authority-indipendenti-leggi-istitutive.md"]
book_refs: ["m-fc05-authority-indipendenti", "vol-05-authority-regolazione"]
confidence: 0.97
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["vol-05", "correzioni", "fonti-primarie"]
source_type: official_legislation_and_judicial_sources
source_date: 2026-10-03
authority_level: primary_official
---

# Perimetro verificato

Letti integralmente gli articoli correnti seguenti, non le intere leggi:

- [L. 287/1990, art. 14](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-10-10;287~art14!vig=): avvio e difesa, proporzionalità delle richieste e non autoincriminazione; accessi aziendali e altri luoghi; decreto del procuratore per questi ultimi; sanzioni e penalità, con specifiche garanzie delle persone fisiche.
- [DPR 217/1998](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-04-30;217!vig=), artt. 6, 7, 9, 10, 12, 13 e 14, coordinati con DPR 214/2024: richiesta completa, proroga motivata prima della scadenza, assistenza senza sospensione automatica dell'ispezione, verbalizzazione, segreto/accesso. Art. 14 vigente: comunicazione risultanze almeno 45 giorni prima del termine, memorie sino a 10 giorni prima e richiesta di audizione entro 10 giorni dal ricevimento. Non usare i vecchi termini regolamentari.
- [D.Lgs. 196/2003, artt. 157–158](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196~art158!vig=): poteri informativi e ispettivi del Garante; privata dimora con assenso informato del titolare/responsabile oppure autorizzazione del presidente del tribunale. Il termine massimo di tre giorni riguarda l'indifferibilità documentata, non ogni ispezione.
- [CGUE, comunicato sulla sentenza Akzo Nobel, C-550/07 P, 14 settembre 2010](https://curia.europa.eu/site/upload/docs/application/pdf/2010-09/cp100090it.pdf): verificato testo ufficiale indicizzato relativo alla protezione della corrispondenza difensiva con avvocato indipendente e all'esclusione dell'avvocato dipendente nel contesto delle indagini della Commissione. Non dichiarata lettura integrale della sentenza; la regola UE non è trasformata in automatismo universale delle ispezioni nazionali.

Raw Normattiva immutabili in `wiki/raw/correzioni-vol05-2026-10-03/`; testi di lavoro e hash nei manifest `norme-vol05/manifest.json` e `procedure-manifest.json`. Articolo 14 della legge e articolo 14 del DPR sono fonti diverse: nel capitolo le citazioni le distinguono.

Le richieste esemplificative sono facsimili didattici con soggetti, date e dati fittizi. Il termine proposto non è un termine generale di legge. Il raccordo fra preistruttoria e istruttoria formale distingue valutazione iniziale della notizia e poteri specifici dell'art. 14 nel procedimento avviato; non afferma che qualsiasi acquisizione preliminare sia vietata.

Collegamenti: [[topics/authority-rettifiche-2026]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/05-vigilanza-istruttoria-ispezioni-dati-prova]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/06-sanzioni-impegni-rimedi-controllo-giurisdizionale]].
''',encoding='utf8')
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## Istruttoria e ispezioni\n\n[[sources/vol-05-istruttoria-verifica-2026-10-03]] coordina L. 287 e DPR 217 aggiornato nel 2024; distingue i decreti autorizzativi AGCM e Garante, assistenza, segreto difensivo, informazione e non autoincriminazione.\n',encoding='utf8')
p=B/'chapters/05-vigilanza-istruttoria-ispezioni-dati-prova.md';s=p.read_text(encoding='utf8')
s=s.replace("L'**istruttoria** è il percorso ordinato", "In senso generale, l'**istruttoria** è il percorso ordinato")
pos=s.index('Per impostare bene un’attività istruttoria') if 'Per impostare bene un’attività istruttoria' in s else s.index("Per impostare bene un'attività istruttoria")
s=s[:pos]+'''**Preistruttoria e istruttoria formale.** La valutazione iniziale di una segnalazione verifica attendibilità, competenza e necessità di approfondire; non equivale già all'accertamento di un illecito. Per l'antitrust AGCM l'avvio formale è deliberato dal Collegio e notificato, con elementi essenziali dell'ipotesi, responsabile, accesso agli atti e termini, secondo art. 6 DPR 217/1998. Le acquisizioni preliminari richiedono la propria base giuridica: non si usa una telefonata informale per anticipare senza garanzie i poteri dell'art. 14 L. 287 esercitati nell'istruttoria. Il titolo della nota non determina la fase; contano attività effettiva e fonte.

'''+s[pos:]
start=s.index("L'articolo 14 della legge n. 287/1990 attribuisce");end=s.index('Per il funzionario, la check-list',start)
s=s[:start]+'''### AGCM e Garante: autorizzazioni differenti

| Tipo di accesso | AGCM antitrust | Garante privacy |
| --- | --- | --- |
| Locali d'impresa / luoghi del trattamento | Art. 14, comma 2-quater, L. 287: locali, terreni e mezzi aziendali; libri e dati anche digitali, copie, sigilli e spiegazioni nei limiti di legge | Art. 158 Codice privacy: luoghi del trattamento o delle rilevazioni utili, banche dati e archivi |
| Altri luoghi, inclusa abitazione | Ragionevoli motivi di sospettare la presenza di documenti aziendali pertinenti; decreto motivato del **procuratore della Repubblica** del luogo, commi 2-quinquies e 2-sexies | Privata dimora e pertinenze: assenso informato del titolare o responsabile, oppure autorizzazione del **presidente del tribunale** territoriale |
| Documentazione e collaborazione | Provvedimento ispettivo notificato e, quando occorre, decreto autorizzativo; possibile collaborazione GdF; verbale delle attività | Personale dell'Ufficio e collaborazione di altri organi; garanzie dell'art. 158, incluso verbale in contraddittorio nell'acquisizione online presso il titolare |

Per il Garante, in caso di **indifferibilità documentata**, il presidente del tribunale provvede senza ritardo e al più tardi entro tre giorni dalla richiesta. Questo termine non è una licenza ad accedere senza assenso o decreto, né il termine generale di durata dell'ispezione. Per AGCM il decreto per luoghi non aziendali proviene dal procuratore: non si trasferisce il regime privacy all'antitrust.

**Assistenza e verbale.** Nell'ispezione AGCM i soggetti possono farsi assistere da consulenti di fiducia; l'esercizio della facoltà non sospende l'ispezione (art. 10 DPR 217). Si identificano funzionari, oggetto, documenti acquisiti e dichiarazioni; richieste, riserve e osservazioni vanno verbalizzate. Una prescrizione aziendale di riservatezza non impedisce l'acquisizione legittima. L'impresa può invece formulare richieste motivate di tutela dei segreti e proporre versioni non confidenziali ai fini dell'accesso, secondo art. 13.

**Difesa e non autoincriminazione.** La richiesta AGCM deve essere proporzionata e non può obbligare ad ammettere l'infrazione. Ciò non attribuisce all'impresa un rifiuto generale di produrre dati accessibili. Per la persona fisica, l'art. 14, commi 7–8, prevede il rifiuto motivato delle informazioni che potrebbero far emergere una propria responsabilità penale o per un illecito amministrativo punitivo. Non si nascondono documenti né si forniscono risposte false invocando genericamente il diritto di difesa.

Il **segreto delle comunicazioni difensive** va distinto dal segreto commerciale. Nel quadro delle indagini della Commissione UE, la sentenza Akzo Nobel, C-550/07 P, richiede l'indipendenza dell'avvocato ed esclude dalla corrispondente tutela la comunicazione con il legale dipendente dell'impresa. È una regola riferita a quel contesto: non va estesa senza verifica a ogni controllo nazionale. Operativamente, la pretesa difensiva si solleva in modo specifico, identificando documento, interlocutore e ragione della tutela, chiedendone verbalizzazione e trattamento secondo la procedura applicabile; l'etichetta «legale» nella cartella non basta.

## N-MF05-05-03 · Poteri, procedura e conseguenze

'''+s[end:]
s=s.replace("Per il funzionario, la check-list essenziale prima di un'attività ispettiva è questa:\n\n## N-MF05-05-03 · Poteri, procedura e conseguenze\n", "Per il funzionario, la check-list essenziale prima di un'attività ispettiva è questa:\n")
pos=s.index('### Mini-esercizio di consolidamento')
s=s[:pos]+'''### Richiesta di informazioni compilata

**Facsimile esclusivamente didattico, privo di valore di atto.** Procedimento antitrust I-ALFA; destinataria Alfa S.p.A.; richiesta del 6 ottobre 2026. L'avvio formale è stato notificato il 1° ottobre. Si verificano possibili condizioni discriminatorie di accesso a un servizio nel trimestre luglio–settembre 2026.

**Fondamento e scopo:** art. 14, comma 2, L. 287/1990 e art. 9 DPR 217/1998; ricostruire condizioni praticate a categorie omogenee di clienti, senza chiedere al destinatario di ammettere un abuso. **Documenti:** elenco dei contratti del trimestre, tariffa, sconti e criteri di ammissione; motivazione documentata delle deroghe. Dataset CSV con dizionario dei campi e identificativi pseudonimizzati; contratti campione in PDF, con collegamento al codice del dataset. Nessuna richiesta di dati sanitari o familiari estranei allo scopo.

**Termine e canale:** risposta entro il 20 ottobre 2026 tramite il canale indicato nel provvedimento; referente del procedimento per chiarimenti. I quattordici giorni sono una scelta motivata del caso, non un termine universale. Se preparare i dati richiede più tempo, presentare prima della scadenza un'istanza scritta e motivata di proroga; il nuovo termine dipende dall'accoglimento, non dalla sola domanda.

**Completezza e riservatezza:** specificare origine, periodo, eventuali lacune e criterio di estrazione; segnalare precisamente le parti riservate, le ragioni e la versione non confidenziale. Conservare gli originali e la traccia della trasmissione. L'accesso di altri partecipanti richiede il bilanciamento previsto dall'art. 13 DPR 217.

**Avvertenza settoriale:** per imprese e associazioni, risposte colposamente o dolosamente inesatte, incomplete o fuorvianti e mancato rispetto del termine possono ricadere nell'art. 14, comma 5, con sanzione fino all'1% del fatturato mondiale dell'esercizio precedente; il comma 6 consente penalità sino al 5% del fatturato medio giornaliero precedente per ogni giorno di ritardo nelle fattispecie previste. Le misure richiedono il provvedimento dell'Autorità; non sono una multa automatica calcolata dal funzionario. Persone fisiche e altre autorità hanno regimi differenti.

## N-MF05-05-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Una segnalazione dettagliata coincide con l'apertura dell'istruttoria antitrust?

**Risposta corretta:** no. Può giustificare approfondimenti; l'avvio formale richiede la deliberazione e le comunicazioni previste. Il sospetto deve ancora essere verificato e il segnalante non decide la misura finale.

**Quesito 2.** AGCM intende ispezionare l'abitazione di un dirigente dove si sospetta ragionevolmente siano custoditi documenti aziendali pertinenti. Quale autorizzazione occorre?

**Risposta corretta:** il decreto motivato del procuratore della Repubblica del luogo, ai sensi dell'art. 14, commi 2-quinquies e 2-sexies. Il provvedimento ispettivo del Collegio da solo non sostituisce questo requisito.

**Quesito 3.** Il Garante controlla una privata dimora senza assenso informato: basta il decreto del procuratore usato nell'antitrust?

**Risposta corretta:** no. L'art. 158 richiede l'autorizzazione del presidente del tribunale competente. Sono diversi fonte, autorità giudiziaria e presupposti; non esiste un'autorizzazione ispettiva unica per tutte le autorità.

**Quesito 4.** Nell'ispezione AGCM l'impresa chiama il proprio consulente. L'accesso deve restare sospeso fino al suo arrivo?

**Risposta corretta:** no. L'assistenza è consentita, ma l'art. 10 DPR 217 esclude la sospensione per il solo esercizio della facoltà. Restano da rispettare oggetto, poteri, verbalizzazione e le garanzie applicabili.

**Quesito 5.** La richiesta impone di produrre contratti pertinenti oppure, in alternativa, ammettere di avere commesso l'abuso. Le due richieste sono equivalenti?

**Risposta corretta:** no. Dati e documenti accessibili possono essere richiesti proporzionatamente; non si può obbligare il destinatario ad ammettere l'infrazione. Il diritto di difesa non autorizza falsità o occultamento di documenti.

**Quesito 6.** Alfa chiede proroga il 19 ottobre ma non riceve ancora risposta. Può considerare automaticamente spostata la scadenza del 20?

**Risposta corretta:** no. L'istanza deve essere motivata e anteriore alla scadenza; il nuovo termine è fissato dagli uffici se la accolgono. La sola presentazione non vale come accoglimento.

### Caso ragionato di chiusura

**Traccia.** Una tabella mostra 100 contratti con tariffa media di 20 euro per il gruppo A e 30 per B. Il dirigente chiede una sanzione immediata per discriminazione e l'accesso all'abitazione dell'amministratore senza altri atti. Quale nota predisponi?

**Soluzione.** La differenza di media è un indizio, non dimostra identità delle prestazioni o abuso. Acquisire durata, volumi, qualità, sconti e criteri di ammissione, verificando la base della competenza e dell'eventuale posizione dominante. Formulare richiesta proporzionata sul periodo utile e consentire difesa. Un accesso domestico antitrust richiede ragionevoli motivi sulla presenza di documenti pertinenti, provvedimento ispettivo e decreto del procuratore; la volontà del dirigente non li sostituisce. Una spiegazione economica documentata può mutare l'ipotesi: la nota separa fatti, inferenze e prove ancora da acquisire.

**Autovalutazione:** quattro punti per indizio distinto da prova, dati comparabili, richiesta proporzionata e garanzia dell'accesso; una conclusione affrettata sulla multa non completa nessuno dei passaggi mancanti.

**Riferimenti normativi e professionali.** L. 287/1990, art. 14; DPR 217/1998, artt. 6–7, 9–10 e 12–14, come aggiornato dal DPR 214/2024; D.Lgs. 196/2003, artt. 157–158; GDPR, art. 58. Testi vigenti in [Normattiva](https://www.normattiva.it/). CGUE, Akzo Nobel, C-550/07 P, 14 settembre 2010, sul segreto difensivo nel contesto UE. Verifica mirata del 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/vol-05-istruttoria-verifica-2026-10-03.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/vol-05-istruttoria-verifica-2026-10-03.md", "wiki/topics/authority-rettifiche-2026.md", ',1)
assert s.count('## N-MF05-05-03')==1
p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=[1,2,3,4,5];d['findingsFullyApplied']+=['V05-09'];f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'norme-vol05/procedure-manifest.json';d=json.loads(f.read_text(encoding='utf8'))
for r in d:r['readComplete']=True;r['verifiedAt']='2026-10-03'
f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('Applied chapter 5 and source; procedure articles read completely.')
