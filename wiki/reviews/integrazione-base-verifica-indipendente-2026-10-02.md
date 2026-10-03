---
id: integrazione-base-verifica-indipendente-2026-10-02
type: editorial_review
title: Revisione indipendente integrazioni VOL-01 capitoli 5 e 6
review_date: 2026-10-02
review_required: false
scope: delta-INT01-INT03
canonical: true
---

# Revisione indipendente — VOL01 capitoli 5 e 6, delta INT01–INT03

Data: 2 ottobre 2026. Revisore: audit_sanita, diverso dall'autore audit_base. Perimetro: aggiunte sulla documentazione amministrativa, ricorsi, inconferibilità/incompatibilità e incarichi extraistituzionali. Applicata la skill Revisore Editoriale Totale, con checklist e template; richiamata LocalAgentMemory in sola lettura. Nessuna modifica a capitoli, fonti, memoria, CLI o stato editoriale.

## 1. Sintesi editoriale

Nessun errore normativo sostanziale rilevato nelle integrazioni esaminate. I testi distinguono correttamente i regimi, accompagnano la teoria con casi e verifiche e non estendono regole speciali a tutti i dipendenti. Rilevato un difetto di tracciabilità dei metadati, comunicato subito all'autore e al coordinatore; corretto dall'autore e verificato nuovamente.

La valutazione riguarda il delta nazionale del 2 ottobre, non la vigenza integrale dell'intero VOL01 né di tutte le norme menzionate nei capitoli preesistenti.

## 2. Punti applicati della checklist

- Punti 3, 4, 6–14 e 16–26, 28–30: applicati alle sezioni aggiunte e ai raccordi immediati; nessun rilievo residuo obbligatorio.
- Punto 15: controllo fonte → claim e tracciabilità dei campi canonici; un rilievo chiuso.
- Punti 1, 2, 5 e 7: limitati al corretto inserimento nei capitoli esistenti e alla coerenza fra i due delta. Non riesaminati indice generale, intero volume e tutti i rinvii esterni.
- Punto 27: non applicabile; nessun PDF impaginato nuovo disponibile.
- Copertura didattica del delta: documentazione con caso a tre pratiche, sei quiz commentati ed esercizio; ricorsi con spiegazione dei rimedi, tre controlli ragionati ed esercizio; incarichi con due casi, quattro quiz commentati ed esercizio. Le verifiche applicano concetti già spiegati.

## 3. Tabella degli errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| RB01 | Frontmatter di entrambi i capitoli, campi source_refs / last_compiled_from | Tracciabilità | Media | Nella prima versione le nuove fonti e pagine erano registrate soltanto nei campi integration_source_refs / integration_compiled_from. I consumatori del progetto leggono i campi canonici: src/server/book/book-preview.ts:212, src/server/wiki/graph.ts:73, src/server/agents/manual-writer-agent.ts:321. | Aggiungere i riferimenti anche nei campi canonici, conservando quelli del delta. | Corretto dall'autore; ricontrollato con il parser del repository: entrambi i mapping completi e nessun percorso mancante. |

Nessun altro errore certo emerso nel perimetro controllato. Non sono trasformate in errori le omissioni di casistiche processuali o professionali dichiaratamente escluse.

## 4. Osservazioni per capitolo

### Capitolo 5 — Diritto amministrativo operativo

Esaminate integralmente le aggiunte alla sezione 8 e la revisione della sezione 14 nel diff del file `wiki/books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md`.

La distinzione certificato/dichiarazione/acquisizione d'ufficio è corretta; artt. 46 e 47 non sono sovrapposti. Corretti limiti sulla conoscenza diretta, documenti sanitari, categorie di copie ex art. 19, firma ex artt. 38–39 e identificazione digitale. La regola sui privati recepisce il 2020 senza promettere sostituibilità universale. Art. 71 distingue campioni, dubbio ragionevole, controlli successivi, regolarizzazione non falsa e consenso per la richiesta del privato. Il caso del titolo mai conseguito resta distinto da quello conseguito dopo la scadenza. Ricontrollate anche le ultime aggiunte dell'autore: ambito soggettivo ex art. 3; effetti ulteriori dell'art. 75 comma 1-bis con eccezioni; aumento della sanzione ex art. 76. Il divieto biennale non è impropriamente esteso alla partecipazione a qualsiasi concorso.

La parte sui rimedi separa atto definitivo e atto non più contestabile; non confonde opposizione tipizzata con autotutela. Termini 30/90/120 giorni correttamente associati ai rispettivi istituti. Riforma 2026 correttamente attribuita al Presidente del Consiglio di Stato, non al Presidente del Consiglio dei ministri. Corretta la distinzione tra annullamento ordinario, silenzio-inadempimento, accesso e ottemperanza; nessuna sospensione automatica dedotta dalla presentazione del ricorso.

### Capitolo 6 — Pubblico impiego e organizzazione della PA

Esaminate integralmente le aggiunte alla sezione 4 nel diff del file `wiki/books/il-metodo-bando/chapters/pubblico-impiego-e-organizzazione-pa.md`.

Art. 53 e D.Lgs. 39 sono tenuti distinti. L'ambito degli incarichi tipizzati evita l'erronea estensione dell'inconferibilità a qualsiasi assunzione. Corretti nullità ex art. 17, decorrenza dei quindici giorni dalla contestazione ex art. 19 e distinzione fra dichiarazione iniziale e annuale ex art. 20. Per l'attività esterna, divieto/autorizzabilità/esclusione sono presentati prima del caso pratico. Compenso modesto, occasionalità e fuori-orario non diventano esenzioni generali. Part-time ≤50% e deroghe professionali restano delimitati. Sanzioni disciplinari, versamento del compenso e responsabilità erariale non sono confusi con un licenziamento automatico.

## 5. Coerenza globale

Terminologia coerente fra i due delta: dichiarazione dell'interessato non equivale a controllo dell'amministrazione né a sanatoria. Casi nazionali trasferibili anche alle aziende sanitarie, senza introdurre regole della Campania o di Caserta. Nessun capitolo nuovo, nessuna ristrutturazione del corpus. Conservati i raccordi con le sezioni preesistenti.

## 6. Contenuti verificati e limiti delle fonti

| Nucleo | Riscontro indipendente effettivamente letto | Esito e limite |
| --- | --- | --- |
| Decisione e denominazione del ricorso straordinario | [GU 41/2026](https://www.gazzettaufficiale.it/eli/gu/2026/02/19/41/sg/pdf), art. 6 commi 4–6, pagina PDF 13; art. 32, pagina PDF 36. Conferma nel [coordinato GU 101/2026](https://www.gazzettaufficiale.it/eli/gu/2026/05/04/101/sg/pdf), pagine PDF 66–67. | Confermati autorità decidente e vigore dal 20 febbraio. Nessuna dipendenza dalla vecchia denominazione presente nel PDF storico. |
| Gerarchico, opposizione, termine straordinario | [DPR 1199 sul sito Presidenza del Consiglio](https://presidenza.governo.it/USRI/magistrature/norme/dpr1199_1971.pdf), artt. 1–9. | Fonte storica usata per questi nuclei, non per attribuire oggi il decreto al Presidente della Repubblica. |
| Azioni amministrative | [GU 156/2010, supplemento 148](https://www.gazzettaufficiale.it/eli/gu/2010/07/07/156/so/148/sg/pdf), artt. 29, 31, 112, 116, pagine PDF 14, 30–31. | Riscontrati nuclei descritti. Non certificata lettura integrale del CPA vigente; nessuna verifica esaustiva di riti speciali, depositi o notifiche. |
| Autocertificazione ai privati | [Art. 30-bis DL 76/2020 coordinato](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.codiceRedazionale=20A04921&art.dataPubblicazioneGazzetta=2020-09-14&art.flagTipoArticolo=0&art.idArticolo=30&art.idGruppo=7&art.idSottoArticolo=2&art.idSottoArticolo1=10&art.progressivo=0&art.versione=1). | Confermata soppressione della condizione di consenso del destinatario negli artt. 2 e 71 comma 4; distinto dal consenso del dichiarante per il controllo chiesto dal privato. |
| Controlli e regolarizzazione | [GU 101/2026](https://www.gazzettaufficiale.it/eli/gu/2026/05/04/101/sg/pdf), riproduzione artt. 71–72, pagina PDF 117. | Confermati controlli proporzionali, anche dopo benefici; omissioni non false; conferma al privato; mancata risposta entro trenta giorni. |
| Dichiarazioni, copie e responsabilità | [DPR 445 sul sito Parlamento](https://www.parlamento.it/parlam/leggi/deleghe/00443dla.htm), nuclei artt. 19, 38–49, 75–76; ulteriore riscontro MEF indicato sotto. | Fonte storica coordinata con i riscontri successivi sopra indicati. Confermata distinzione decadenza/conseguenze penali. Nessuna ricognizione esaustiva della giurisprudenza e delle pene dei singoli reati. |
| D.Lgs. 39: categorie e conseguenze | [GU 92/2013](https://www.gazzettaufficiale.it/eli/gu/2013/04/19/92/sg/pdf), art. 1 e artt. 15–20, pagine PDF 5 e 10. | Confermati nuclei effettivamente esposti. Non svolto censimento aggiornato di ogni combinazione di cariche e durata; il testo non lo promette. |
| Art. 53: conflitto potenziale e omesso versamento | [L. 190/2012 in GU](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.codiceRedazionale=012G0213&art.dataPubblicazioneGazzetta=2012-11-13&art.flagTipoArticolo=0&art.idArticolo=1&art.idGruppo=0&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.progressivo=0&art.versione=1), art. 1 comma 42 e note art. 53. | Riscontrati controllo sul conflitto anche potenziale e comma 7-bis. Non attestata lettura integrale dell'art. 53 consolidato al 2 ottobre. |
| Incarichi esterni: uso della fonte istituzionale | [FAQ Difesa, attività extraistituzionali](https://www.difesa.it/sgd/staff/dg/persociv/faq/attivita-extraistituzionali/33212.html), quesiti 3–6, 13 e seguenti. | Controllato che il capitolo non importi periodicità annuali ministeriali, modelli locali o soglie fiscali datate. FAQ aggiornata al 2022, non fonte di attestazione generale della vigenza 2026. |

L'ultima versione del delta è stata ulteriormente controllata leggendo integralmente i tre PDF di una pagina del repertorio MEF Giustizia tributaria:

- [Art. 3 DPR 445](https://def.giustiziatributaria.gov.it/DocTribFrontend/executePrintArticolo.do?articolo=Articolo+3&codiceOrdinamento=0000000000000030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7BEECE6580-2CAB-47EB-8D5D-6742D39943EB%7D), versione in vigore dal 28 dicembre 2024: confermati cittadini italiani/UE, limite sui fatti certificabili da soggetti pubblici italiani per non UE regolarmente soggiornanti, clausola settoriale e convenzioni.
- [Art. 75 DPR 445](https://def.giustiziatributaria.gov.it/DocTribFrontend/executePrintArticolo.do?articolo=Articolo+75&codiceOrdinamento=0000000000000750000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7BEECE6580-2CAB-47EB-8D5D-6742D39943EB%7D), versione in vigore dal 19 maggio 2020: confermati comma 1 e comma 1-bis, decorrenza biennale dall'atto di decadenza e salvaguardia degli interventi per minori/disagio.
- [Art. 76 DPR 445](https://def.giustiziatributaria.gov.it/DocTribFrontend/executePrintArticolo.do?articolo=Articolo+76&codiceOrdinamento=0000000000000760000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7BEECE6580-2CAB-47EB-8D5D-6742D39943EB%7D), versione in vigore dal 19 novembre 2020: confermato aumento da un terzo alla metà della sanzione ordinariamente prevista dal codice penale. Il capitolo non fissa una pena unica per ogni dichiarazione falsa.

Le source notes esaminate dichiarano coerentemente questi limiti e mantengono review_required. Le difficoltà di accesso ad alcune pagine GU puntuali non sono state trattate come verifiche riuscite: usati PDF e altri documenti primari accessibili.

## 7. Suggerimenti facoltativi

Nessun ampliamento necessario per chiudere questo delta. Eventuali tavole esaustive di cause ex D.Lgs. 39 o procedure processuali dettagliate richiederebbero un nuovo perimetro di verifica, non una correzione redazionale automatica.

## 8. Priorità degli interventi

RB01 già chiuso. Nessuna correzione normativa obbligatoria residua rilevata. Conservare review_required e i gate editoriali del coordinatore: questa revisione non produce freeze né autorizza pubblicazione autonoma.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori**, limitatamente ai delta INT01–INT03 esaminati. La correzione concreta emersa è già stata applicata e ricontrollata; il giudizio non sostituisce la verifica finale del prodotto impaginato o della restante parte del volume.

## 10. Limiti e controlli tecnici

Audit del diff e dei raccordi, non revisione integrale di tutti i capitoli. Nessuna attestazione generale di aggiornamento dell'ordinamento. Nessun controllo visivo di un PDF del libro.

`git diff --check` sui due capitoli: nessuna anomalia. Parsing in sola lettura con `src/server/wiki/frontmatter.ts`: entrambi review_required=true, draft_stage=editorial-review; nuove fonti mappate in source_refs e nuovi consolidamenti in last_compiled_from; nessun percorso mancante. Un primo tentativo con gray-matter non disponibile è stato abbandonato senza installare dipendenze; controllo ripetuto con successo col parser canonico del progetto. Nessun comando CLI di pipeline, modifica di stato o cattura di memoria eseguito dal revisore.
