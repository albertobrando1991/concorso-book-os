---
id: source-vol-10-tecnico-rettifiche-2026-10-03
type: source
title: "VOL-10 — riscontri tecnici e normativi del 3 ottobre 2026"
status: consolidated
domain: concorsi tecnici pubblici
topics: ["topics/tecnico-ingegneristico-rettifiche-2026"]
entities: ["D.Lgs. 36/2023", "D.P.R. 380/2001", "NTC 2018", "D.Lgs. 81/2008"]
source_refs: ["sources/vol-09-esecuzione-verifica-2026-10-03", "sources/vol-02-edilizia-somma-urgenza-verifica-2026-10-02", "sources/ntc-2018-circolare-2019-emendamenti-2023-fonti-ufficiali"]
book_refs: ["m-tr03-tecnico-ingegneristico", "vol-10-tecnico-ingegneristico-territorio-lavori-pubblici"]
confidence: 0.96
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: [source, official, vol-10, rettifiche]
source_type: official_normative_and_technical_bundle
source_url: "https://www.normattiva.it/"
source_date: 2026-10-03
authority_level: alta
---

# Riscontri per le rettifiche del volume tecnico

## Evidenza e perimetro

Riscontri puntuali sui testi ufficiali, non certificazione dell'intero corpus normativo. Raw immutabili in `wiki/raw/correzioni-vol10-2026-10-03/`; URL, hash e acquisizioni nell'artifact `artifacts/correzioni-collana-2026-10-02/norme-vol10/manifest.json`. I file denominati `edilizia-art6-bis`, `34-bis`, `36-bis` hanno risolto l'articolo base: **non sono prova del bis**. Usare esclusivamente `edilizia-art6bis`, `34bis`, `36bis`. Le prime acquisizioni `civile-art822/823/826/828` contengono il decreto di approvazione, non gli articoli del Codice: escluse. Pagine di sessione scaduta escluse dai riscontri. La validità deriva dal contenuto verificato, non dal nome del file.

## NTC e statica

[D.M. 17 gennaio 2018, allegati ufficiali in GU](https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg), capitoli 2 e 8: raw `ntc-cap2.pdf`, `ntc-cap8.pdf`. Letti §2.4, §2.5.3 e §§8.3–8.4.3. Vita nominale minima 10 anni per costruzioni temporanee/provvisorie, 50 per prestazioni ordinarie, 100 per elevate; la classe d'uso è un asse distinto. Classi I/II/III/IV e coefficienti 0,7/1/1,5/2; V_R=V_N×C_U. Non trasferire automaticamente il minimo di 35 anni della precedente formulazione NTC al testo 2018. Le combinazioni fondamentale, caratteristica, frequente, quasi permanente, sismica ed eccezionale hanno funzioni e coefficienti diversi. Le azioni variabili accompagnatrici vengono ridotte con ψ, non sommate tutte al massimo.

NTC §8.3 consente valutazione delle esistenti ai soli SLU, salvo SLE del §7.3.6 per classe IV con possibili livelli ridotti. §8.4: intervento locale senza sostanziale modifica globale e senza ridurre la sicurezza; miglioramento aumenta la sicurezza, senza necessariamente raggiungere l'adeguamento; adeguamento nelle condizioni a–e del §8.4.3 (sopraelevazione, ampliamento strutturalmente connesso significativo, variazione d'uso con incremento carichi globali verticali in fondazione oltre 10%, trasformazione strutturale, passaggio a classe III scolastica/IV). Miglioramento e adeguamento richiedono collaudo statico. ζ_E: miglioramento classi III scolastica/IV almeno 0,6, classi II/restanti III incremento almeno 0,1, salvo disciplina dei beni culturali; adeguamento a/b/d almeno 1 e c/e almeno 0,8.

Esempio di statica derivato dalle equazioni di equilibrio, non da valori prescrittivi: trave piana semplicemente appoggiata, L=4 m, q=10 kN/m, cerniera A e carrello B. ΣF_x=0, ΣF_y=0, ΣM_A=0 danno R_Ax=0, R_Ay=R_By=20 kN. Con x da A, V=20−10x kN e M=20x−5x² kN·m; M massimo 20 kN·m a x=2 m, nullo agli estremi. Calcoli e figure tracciati in `artifacts/correzioni-collana-2026-10-02/figure-vol10-scientifiche.json`.

## Urbanistica ed edilizia

[D.M. 1444/1968, testo Camera](https://www.camera.it/temiap/2014/12/09/OCD177-705.pdf), artt. 2–5: zone A–F; minimo generale residenziale 18 m²/abitante, ordinariamente 4,5 istruzione, 2 interesse comune, 9 verde/sport, 2,5 parcheggi, escluse sedi viarie. Art. 4 differenzia A/B, C nei piccoli comuni e altre ipotesi, E e F; non insegnare 18 come numero universale. A/B: dimostrazione dell'impossibilità e soluzioni previste; aree per standard computate al doppio dell'effettivo. C con popolazione prevista non superiore a 10.000: 12 m², di cui 4 scolastici; C in rapporto visuale con particolari connotati naturali/storici: verde 15 m², salvo contiguità a porti nazionali. E: 6 m² per istruzione/interesse comune; F per territorio servito 1,5 istruzione superiore (università escluse), 1 sanità, 15 parchi. D industriale: 10% superficie insediamento. Nuovo commerciale/direzionale: 80 m² ogni 100 m² di superficie lorda, almeno metà parcheggi; A/B riduzione a metà con attrezzature integrative. Coordinare sempre disciplina regionale e piano; non è una procedura per autorizzare opere.

D.P.R. 327/2001 artt. 9 e 39, testi correnti Normattiva acquisiti: vincolo preordinato all'esproprio cinque anni; entro il termine dichiarazione di pubblica utilità. Decadenza se manca; reiterazione motivata con rinnovo procedimento e indennità per danno effettivamente prodotto.

D.P.R. 380/2001 artt. 3, 6-bis, 20, 22, 23, 34-bis, 36 e 36-bis, testo corrente acquisito. Art. 3 distingue finiture/impianti esistenti, manutenzione straordinaria, conservazione dell'organismo, trasformazione edilizia, nuova costruzione e sostituzione del tessuto urbanistico. La categoria non basta da sola a scegliere il titolo. CILA residuale rispetto agli artt. 6/10/22 e senza interessamento strutturale secondo asseverazione; SCIA art. 22 include straordinaria strutturale o prospetti, restauro strutturale, ristrutturazione non pesante. SCIA ordinaria: avvio dalla presentazione quando completa dei presupposti, controllo ordinario edilizio 30 giorni ex art. 19, comma 6-bis, L. 241/1990. SCIA alternativa art. 23: almeno 30 giorni prima, termine massimo efficacia 3 anni, specifiche ipotesi 01; assensi di tutela necessari conservano il proprio regime.

Art. 20, comma 8, come modificato da L. 182/2025 art. 40: silenzio-assenso del permesso alle condizioni procedimentali; con vincoli idrogeologici, ambientali, paesaggistici/culturali conferenza, salvo assensi formali già acquisiti, validi, per medesimo intervento ed elaborati. Non produce un assenso tacito dell'autorità di tutela. Riscontro parallelo [[sources/vol-02-edilizia-somma-urgenza-verifica-2026-10-02]].

Art. 36: assenza/totale difformità dal PdC o SCIA alternativa; doppia conformità urbanistica ed edilizia a realizzazione/domanda, risposta entro 60 giorni con silenzio-rifiuto. Art. 36-bis: parziali difformità, assenza/difformità SCIA art. 37, variazioni essenziali; urbanistica vigente alla domanda ed edilizia alla realizzazione, possibili condizioni tecniche; PdC 45 giorni con silenzio-assenso, SCIA termine 30 giorni, sospensioni/istruttoria e vincoli secondo norma. Tolleranze 34-bis: regola 2%; per interventi entro 24 maggio 2024, fasce 2/3/4/5/6% per superfici utili assentite >500/300–500/100–300/<100/<60 m², specifiche cautele tecniche e diritti terzi. Non sono sanatoria; evitare casi sui confini sovrapposti della formulazione normativa.

## Conferenza, esecuzione e sicurezza

L. 241/1990 art. 14: istruttoria facoltativa per esame contestuale interessi; decisoria obbligatoria se conclusione positiva richiede plurimi assensi di amministrazioni diverse; preliminare facoltativa su motivata richiesta con studio di fattibilità per progetti complessi o insediamenti produttivi, per conoscere condizioni prima dell'istanza definitiva. Distinguere funzione e modalità di svolgimento.

D.Lgs. 36/2023 art. 17, commi 8–9: avvio prima della stipula per motivate ragioni, sempre se ricorre urgenza tipizzata (eventi imprevedibili/pericoli o grave danno all'interesse pubblico, compresa perdita fondi UE). Art. 50, comma 6: sotto soglia dopo verifica requisiti. Non equivale a libera anticipazione su scelta dell'impresa. Art. 41, commi 13–14: prezzari aggiornati, identificazione/scorporo manodopera e sicurezza dall'importo ribassabile, possibilità di giustificare ribasso complessivo mediante organizzazione efficiente; art. 108, comma 9: indicazione offerta di manodopera e oneri aziendali sicurezza, salvo eccezioni previste.

Artt. 116, 120, 121, 125 e allegati: riuso del riscontro puntuale [[sources/vol-09-esecuzione-verifica-2026-10-03]]. Distinguere anticipazione esecuzione, anticipo prezzo e SAL; non trasferire regole storiche art. 106 del D.Lgs. 50/2016. Revisione prezzi lavori: nuovo regime TOL per procedure avviate dal 27 aprile 2026, D.D. 743 del 30 marzo 2026, non numero 730.

D.Lgs. 81/2008 artt. 90 e 92 acquisiti: più imprese esecutrici anche non contemporanee → CSP all'affidamento progettazione, CSE prima affidamento lavori; nomina CSE anche quando pluralità sopravviene. Eccezione art. 90, comma 11, lavori privati senza PdC e sotto 100.000 euro: funzioni CSP al CSE, non esenzione dalla sicurezza. Art. 92, comma 1, lett. f: CSE sospende singole lavorazioni per pericolo grave e imminente direttamente riscontrato fino a verifica adeguamenti. Distinguere questo potere dalla sospensione contrattuale DL/RUP.

## Strade, ponti e dati

D.Lgs. 285/1992 art. 2 corrente: A autostrade, B extraurbane principali, C extraurbane secondarie, D urbane scorrimento, E urbane quartiere, E-bis urbane ciclabili, F locali, F-bis itinerari ciclopedonali. Classificazione tecnico-funzionale distinta da amministrativa/proprietà. E-bis: limite non superiore a 30 km/h e priorità velocipedi.

[Linee guida ponti D.M. 204/2022, allegato CSLP](https://cslp.mit.gov.it/sites/default/files/ALL_DM_204_Allegato_A_-_LL.GG_._Ponti_e_V.pdf), §1.3 pp. 8–10: livelli 0 censimento, 1 ispezioni visive e rilievo speditivo, 2 classe attenzione, 3 valutazioni preliminari, 4 valutazioni accurate NTC, 5 rilevanza trasportistica/rete (non esplicitamente trattato dalle LG). Cinque classi da bassa ad alta; quattro rischi strutturale-fondazionale, sismico, frane e idraulico da combinare secondo metodo, non con una media inventata. Classe alta indirizza al livello 4, monitoraggio non sostitutivo. Nessuna formula quantitativa delle frequenze introdotta senza ulteriore riscontro.

Art. 43 corrente: dal 1 gennaio 2025 obbligo BIM per nuova costruzione/interventi esistenti con costo presunto lavori superiore a 2 milioni; per edifici culturali art. 10, comma 1, D.Lgs. 42/2004 soglia lavori UE art. 14, comma 1, lett. a; esclusa manutenzione ordinaria/straordinaria, salvo opere già eseguite con tali metodi. Adozione facoltativa subordinata misure I.9; formati aperti e interoperabilità.

Catasto: funzioni ufficiali AE consolidate in [[sources/catasto-cartografia-estimo-pubblicita-immobiliare-aggiornamento-2026-07-18]] e [assistenza AE](https://assistenzaipocat.agenziaentrate.gov.it/): PREGEO atti geometrici terreni, DOCFA nuove costruzioni/variazioni unità urbane, voltura intestazioni. Non citare versioni software non verificate. GIS: vettori punti/linee/poligoni; raster celle; CRS e unità da dichiarare. Esempio didattico di coordinate metriche nel medesimo CRS: differenze 30 m e 40 m → distanza piana 50 m; non applicare la stessa formula a gradi geografici.

## Integrazione probatoria: allegati e beni pubblici

Acquisiti e letti integralmente gli articoli specifici, con URL/hash in `norme-vol10/manifest-extra.json`: I.7 artt. 5, 27 e 31; I.9 art. 1; II.14 artt. 7 e 28; Codice civile artt. 822, 823, 826 e 828. Esempio di URL persistente: [II.14 art. 7 vigente](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:2023;36:29~art7!vig=). Raw validi con suffisso `-urn.html`, tranne art. 826 `-urn-complete.html`; file `-valid` e `-session` sono risposte di errore e non sostengono claim. `civile-codice-art826-urn.html` è un download interrotto, non usato.

I.7 art. 31: nuove analisi con quantità unitarie di materiali, manodopera, noli e trasporti e prezzi elementari; aggiunta spese generali 13–17% in base all'intervento; infine utile 10%. Esempio autonomo: costo diretto 100, SG 15 → 115, utile 11,50 → 126,50; non 125. Art. 5 distingue lavori, sicurezza e somme a disposizione: IVA, rilievi, spese tecniche, collaudi, imprevisti ecc. Art. 27 prevede, salvo diversa motivata indicazione, manuale d'uso, manuale di manutenzione e programma; sottoprogrammi prestazioni, controlli, interventi.

II.14 art. 7: riserva sul primo atto idoneo successivo all'insorgenza/cessazione del fatto e anche registro alla firma immediatamente successiva, con decadenza; precisa motivazione e quantificazione, definitiva salvo fatti continuativi; conferma sul conto finale. Firma del conto finale entro 30 giorni dall'invito RUP; nuove domande per oggetto/importo non ammesse, salvo quanto già consentito dalla norma. Mancata firma o mancata conferma comportano accettazione/rinuncia previste. Non tutte le pretese sono riserve: elenco esclusioni comma 1, inclusi interessi moratori. Non introdurre un generico termine di 15 giorni preso dalla disciplina storica.

II.14 art. 28: CRE entro 3 mesi dall'ultimazione, emesso DL e immediatamente trasmesso al RUP, che prende atto e conferma completezza. Facoltà sotto o pari a 1 milione; sopra 1 milione e sotto soglia UE escluse le categorie elencate, comprese classi III/IV salvo manutenzione, complessità strutturali, miglioramento/adeguamento sismico e RUP anche progettista/DL. Il CRE non sostituisce il collaudo statico dovuto.

I.9 art. 1: piano formazione, piano strumenti, atto organizzativo. Nomina gestore ambiente condivisione, almeno un gestore processi digitali, coordinatore flussi per ogni intervento nel supporto RUP. CI della stazione appaltante: requisiti, produzione/gestione/scambio/archiviazione, ambiente, accesso/proprietà/validità, interoperabilità. OGI concorrente nelle procedure OEPV in risposta al CI; PGI aggiudicatario, sulla base OGI, dopo contratto e prima esecuzione, aggiornabile; possibile richiesta anticipata in esecuzione urgente. Consegne tramite ambiente, modelli aggiornati al realizzato e relazione specialistica per collaudo. Non confondere requisiti di ente e incarichi dell'appaltatore.

Codice civile: demanio art. 822 e inalienabilità/diritti terzi nei limiti di legge art. 823; patrimonio indisponibile art. 826 include edifici per uffici pubblici e altri beni destinati a pubblico servizio; art. 828 vincola sottrazione alla destinazione ai modi di legge. Patrimonio disponibile: regime civilistico residuale con discipline speciali e procedure pubbliche pertinenti. Esempi: spiaggia demaniale, edificio statale in effettivo uso come ufficio indisponibile, appartamento pubblico privo di destinazione al servizio disponibile, salvo qualificazioni speciali.

## CAM edilizia, soglia UE e modifiche NTC

[D.M. 24 novembre 2025, GU 281 del 3 dicembre 2025](https://www.gazzettaufficiale.it/eli/id/2025/12/03/25A06516/sg): verificati artt. 1–4 sul PDF GU integrale già acquisito in `artifacts/correzioni-collana-2026-10-02/gu-2025-281-legge182.pdf`, pagine stampate 85–86, SHA-256 `d7372a1e2e6e06c5418fcbfc5251dbd64f0b63e82216b15fbbb9366434aeecad`. Efficacia dopo 60 giorni dalla pubblicazione: 2 febbraio 2026. Si applica ai nuovi affidamenti di servizi indicati, ai lavori basati su progetti validati in vigenza e alla progettazione interna non ancora validata. Il precedente D.M. 256/2022, modificato nel 2024, conserva applicazione nei casi dell'art. 2: PFTE per integrato o esecutivo per soli lavori validati nel precedente regime, con pubblicazione bando/avviso o invio invito entro tre mesi dalla validazione. Non letto integralmente l'allegato tecnico CAM separato; nessuna sua percentuale prestazionale introdotta.

[Commissione europea, soglie 2026–2027](https://single-market-economy.ec.europa.eu/single-market/public-procurement/legal-rules-and-implementation/thresholds_en?prefLang=fr): tabella della direttiva 2014/24/UE letta il 3 ottobre 2026, lavori 5.404.000 euro, rinvio al regolamento delegato (UE) 2025/2152. Il tentativo raw `reg-ue-2025-2152.pdf` ha prodotto un file vuoto; escluso dalle prove, non dichiarato letto. La cifra è corroborata dalla pagina ufficiale della Commissione, non dal download fallito.

[D.M. 9 marzo 2023, GU 69 del 22 marzo 2023, articolo 1](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=23A01847&atto.dataPubblicazioneGazzetta=2023-03-22&atto.tipoProvvedimento=DECRETO): letti transitorio di sette anni e sospensioni dei punti 11.4.2 e 11.5.2 fino al 22 marzo 2025. Non modifica i valori dei capitoli 2 e 8 utilizzati negli esempi. Riscontro puntuale, non attestazione di lettura integrale della circolare applicativa.

## Riscontri aggiuntivi circoscritti

Art. 4 D.M. 1444/1968: il limite mancante nella copia Camera per i nuovi complessi in comuni oltre 10.000 abitanti è 1 m³/m² di densità fondiaria. Riscontro nel testo ufficiale indicizzato del [D.D.G. Sicilia 73/2022](https://www.regione.sicilia.it/sites/default/files/2022-03/ddg%2073%202022.pdf) e nell'[allegato del Comune di Monte San Pietrangeli](https://monte-san-pietrangeli-api.cloud.municipiumapp.it/system/attachments/attachment/attachment/1/1/5/6/0/linee_guida_aree.pdf). Il download del primo restituisce la pagina “non trovata”, non il decreto: raw escluso, verifica limitata agli estratti ufficiali indicizzati, concordanti. Non è una lettura integrale dei due allegati.

Letto integralmente anche II.14 art. 12: documenti contabili, firme e cronologia, SAL e certificato RUP, conto finale; sommario facoltativo, contabilità digitale con formati aperti, autenticità e provenienza. Il termine per la firma del conto è non superiore a trenta giorni; la regola dell’art. 7 è esposta insieme al termine assegnato, non come facoltà di ignorarlo.

## Procedimento espropriativo: raccordo verificato

La fonte consolidata [[sources/vol-02-scuole-espropri-spl-verifica-2026-10-03]] verifica DPR 327 artt. 8, 9, 12, 13, 23 e 24. Riletti anche gli estratti correnti di 13, 23 e 24: termine della PU espresso o, se assente, cinque anni dall'efficacia; proroghe prima della scadenza, per forza maggiore o giustificate ragioni, complessivamente non oltre quattro anni. Decreto entro efficacia PU, trasferimento condizionato a notifica ed esecuzione; preavviso ordinario di sette giorni, notifica contestuale ammessa dal comma 3. Immissione entro termine perentorio di due anni; verbale e consistenza in contraddittorio, due testimoni non dipendenti del beneficiario se assenza/rifiuto. I termini hanno presupposti e decorrenze distinti.

## Collegamenti

- [[topics/tecnico-ingegneristico-rettifiche-2026]]
- [[entities/codice-dei-contratti-pubblici]]
- [[books/moduli/m-tr03-tecnico-ingegneristico/index]]
