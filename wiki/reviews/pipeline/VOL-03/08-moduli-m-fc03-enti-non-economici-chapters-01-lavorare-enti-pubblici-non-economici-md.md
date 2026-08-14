---
volume: VOL-03
step: 08
module: M-FC03
chapter: 01
status: chapter_plan_ready
date: 2026-08-10
target: wiki/books/moduli/m-fc03-enti-non-economici/chapters/01-lavorare-enti-pubblici-non-economici.md
gate: chapter-plan
---

# Piano operativo - M-FC03, capitolo 01

## Esito dello step 08

Il capitolo 01, `Lavorare negli enti pubblici non economici`, e' gia un `revised_draft` di circa 4.061 parole. Copre perimetro M-FC03, distinzione core/delta/profilo, enti guida, enti di orientamento, riconoscimento del bando, Bando Decoder iniziale, checklist, caso guidato, domanda da commissario, domanda-trappola, errore tipico, mini-esercizio e diario errori.

Il capitolo non e' ancora nel formato 2 richiesto dalla pipeline: manca `format_version: 2`, non usa Nucleo ID stabili nel formato `N-M-FC03-01-xx`, non ha nuclei misurabili da almeno 600 parole ciascuno e non contiene un blocco di verifica con almeno sei quiz commentati. Lo step 09 deve quindi essere un retrofit conservativo: preservare la voce e gli strumenti gia presenti, riorganizzando il testo in nuclei stabili, con verifica finale e tracciabilita corretta.

La scheda pipeline di VOL-03 non dichiara soglie personalizzate per il capitolo 01. Valgono quindi i default del formato 2 indicati da `wiki/AGENTS.md` e dalla skill pipeline: almeno 5 nuclei, almeno 600 parole per nucleo, almeno 3.000 parole complessive, almeno 6 quiz commentati e almeno un caso applicativo. Il capitolo supera gia la soglia complessiva, ma non ancora quella per nucleo/verifica.

## Consultazione mirata

Sono stati consultati:

- prompt renderizzato: `artifacts/pipeline/VOL-03/08/moduli-m-fc03-enti-non-economici-chapters-01-lavorare-enti-pubblici-non-economici-md/prompt.md`;
- istruzioni: `AGENTS.md`, `wiki/AGENTS.md`, `.agents/skills/pipeline-volume/SKILL.md`;
- stato pipeline: `npm run pipeline -- status VOL-03 --json`, che conferma lo step 08 del target in corso;
- memoria locale: `LocalAgentMemory` con scope pipeline, usata solo come continuita operativa e non come fonte normativa;
- capitolo target: `wiki/books/moduli/m-fc03-enti-non-economici/chapters/01-lavorare-enti-pubblici-non-economici.md`;
- capitolo successivo: `wiki/books/moduli/m-fc03-enti-non-economici/chapters/02-ordinamento-governance-epne.md`;
- planning modulo: `planning/00-piano-editoriale.md`, `planning/01-matrice-copertura-materie.md`, `planning/02-indice-analitico-2026.md`;
- planning volume: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/00-scheda-pipeline.md`, `00-piano-editoriale.md`, `01-indice-dettagliato-v4.md`, `02-matrice-copertura-didattica.md`, `02-indice-analitico-ricostruito-2026.md`;
- fonti/topic/entity trovati con `rg`: dossier M-FC03, fonti ufficiali EPNE, portali bandi, bando RIPAM-INAIL 308, corpus ufficiale integrativo M-FC03, fonti specialistiche VOL-03, topic EPNE, topic profili previdenza-lavoro-vigilanza, entity INPS-INAIL-EPNE;
- rinvii VOL-01 esistenti: `famiglie-concorsi-pubblici`, `mappe-profilo-cosa-resta-comune-cosa-cambia`, `scegliere-moduli-integrativi`, `anatomia-del-bando` e capitoli base sulle materie comuni;
- quiz: `rg` su `wiki/quizzes` non ha trovato quiz M-FC03/EPNE riutilizzabili; i sei quiz dello step 09 devono quindi essere originali e commentati, non copiati da bandi o banche dati.

## Nuclei assegnati con Nucleo ID stabili

| Nucleo ID stabile | Nucleo assegnato | Stato attuale | Azione prevista nello step 09 |
| --- | --- | --- | --- |
| `N-M-FC03-01-01` | Perimetro M-FC03 e criterio ente-profilo-materie | completo nel contenuto, non nel formato | Conservare apertura, obiettivi, tabella dentro/fuori e confini; trasformare in nucleo autonomo di almeno 600 parole. |
| `N-M-FC03-01-02` | Core VOL-01, delta specialistico EPNE e profilo concreto | completo nel contenuto, non nel formato | Conservare il modello a tre strati; inserire solo rinvii VOL-01 precisi e verificati, senza duplicare la teoria base. |
| `N-M-FC03-01-03` | Enti guida ed enti di orientamento | parziale | Rafforzare INPS/INAIL come enti guida; formulare con prudenza ACI, ENAC, ISTAT, ASI, ENEA, CONI e CRI, distinguendo orientamento, natura dell'ente, profilo e bando corrente. |
| `N-M-FC03-01-04` | Riconoscere un bando M-FC03 | completo nel contenuto, non nel formato | Conservare le tre letture su fonte, profilo e prova; evitare duplicazioni con il Bando Decoder completo del capitolo 10 e con VOL-01. |
| `N-M-FC03-01-05` | Decoder iniziale, rischi di perimetro e checklist | completo nel contenuto, non nel formato | Conservare tabella Decoder, checklist ed errori; rendere esplicita la distinzione fra bando, portale, allegati, avvisi e campione redazionale. |
| `N-M-FC03-01-06` | Decisione operativa, caso e verifica | parziale | Conservare caso, domanda da commissario, domanda-trappola, mini-esercizio e diario; aggiungere verifica finale con almeno sei quiz commentati e caso ragionato. |

## Nuclei gia completi

- `N-M-FC03-01-01`: il testo spiega in modo operativo quando il modulo e' pertinente e quando serve un altro percorso.
- `N-M-FC03-01-02`: il modello core/delta/profilo e' coerente con la logica di copertura v4 e con il principio `delta content` del volume.
- `N-M-FC03-01-04`: la lettura in tre passaggi del bando produce decisioni concrete senza fissare prove, soglie o dati mobili.
- `N-M-FC03-01-05`: Decoder, errori e checklist sono gia strumenti cartacei autonomi.

## Nuclei da sviluppare

1. `N-M-FC03-01-03`: completare la formula sugli enti di orientamento. Il testo deve evitare classificazioni assolute fondate sul solo nome dell'ente; per CONI e CRI serve particolare prudenza e rinvio alla fonte ufficiale aggiornata.
2. `N-M-FC03-01-06`: aggiungere almeno sei quiz commentati su perimetro, core/delta, INPS/INAIL, enti di orientamento, fonte del bando e rinvio ad altro modulo.
3. Inserire `format_version: 2` nel frontmatter del capitolo durante lo step 09.
4. Valutare `dati_operativi: []`: allo stato il capitolo dovrebbe restare senza dati operativi puntuali, perche non deve contenere posti, scadenze, punteggi o calendari.
5. Normalizzare il frontmatter: `source_refs` solo per source note; topic ed entity nei rispettivi campi.
6. Rimuovere dal corpo lettore sezioni interne come `Riferimenti consolidati` e `Note di review`, preservando tracciabilita nel frontmatter e nei report.
7. Riallineare o produrre la matrice canonica richiesta dallo step successivo solo quando il prompt/gate lo richiedera, senza modificare manualmente `run-state`.

## Sezioni da conservare

- Apertura editoriale, domanda guida e obiettivi.
- Istruzioni d'uso del capitolo e Mappa BANDO.
- Tabella `Dentro o fuori`.
- Modello dei tre strati: libro base, delta EPNE, profilo concreto.
- Distinzione fra INPS, INAIL e altri enti di orientamento.
- Tre letture del bando: fonte, profilo/area, prova che seleziona.
- Bando Decoder M-FC03 iniziale.
- Checklist iniziale e finale.
- Caso guidato, domanda da commissario, domanda-trappola, errore tipico, mini-esercizio e diario errori.
- Formulazioni che ricordano la verifica obbligatoria di bandi, allegati, portali, statuti, PIAO, bilanci, carte dei servizi e dati mobili.

Le sezioni finali di tracciabilita interna vanno conservate come informazioni editoriali, ma non come corpo destinato allo studente.

## Duplicazioni da evitare

| Contenuto | Destinazione completa | Trattamento nel capitolo 01 |
| --- | --- | --- |
| Anatomia generale del bando, requisiti, prove, punteggi e soglie | VOL-01, `anatomia-del-bando`; M-FC03 cap. 10 per Decoder EPNE completo | Solo applicazione ente-profilo-prova al perimetro EPNE. |
| Famiglie concorsuali e scelta dei moduli | VOL-01, `famiglie-concorsi-pubblici`, `mappe-profilo-cosa-resta-comune-cosa-cambia`, `scegliere-moduli-integrativi` | Solo decisione M-FC03 principale, M-FC03 di contesto o altro modulo. |
| Ordinamento, governance, organi, statuti e controlli EPNE | M-FC03 cap. 02 | Solo mappa introduttiva e rinvio ragionato. |
| Previdenza, servizi e prestazioni INPS | M-FC03 cap. 03 e appendice B | Solo funzione orientativa di INPS come ente guida. |
| Assicurazione, prevenzione e prestazioni INAIL | M-FC03 cap. 04, appendice B e appendice F quando il bando integra materie | Solo funzione orientativa di INAIL come ente guida. |
| Procedimenti, rapporto utenti, bilancio, PIAO, personale, contratti | M-FC03 cap. 05-09 | Solo elenco del delta specialistico e scelta dei capitoli da attivare. |
| Casi pratici, situazionali e piano 30/60/90 | M-FC03 cap. 11-13 | Un caso introduttivo, una decisione operativa e strumenti brevi. |
| Enti minori, confini cross-family e sottoprofili | Appendici A, C, D, E, F | Solo criterio per capire se restare nel modulo o rinviare. |
| Dati concorsuali su posti, prove, scadenze, calendari, soglie | Source note dedicata sul bando ufficiale corrente | Non stabilizzare dati del campione 2023-2026. |

## Esempi, casi, domande ed esercizi necessari

- Conservare e rendere piu verificabile il caso del bando INAIL amministrativo, lasciandolo come caso redazionale o anonimizzato se non si allega una source note aggiornata.
- Aggiungere un caso breve di bando multi-profilo: funzionario amministrativo EPNE, profilo ICT, profilo ricerca/tecnologo o profilo authority, con decisione fra M-FC03, M-TR01, M-IR03, M-FC05 e M-FC02.
- Conservare la domanda da commissario: perche un concorso INPS o INAIL non va preparato come concorso amministrativo generico?
- Conservare la domanda-trappola: pubblicazione su inPA o gestione Formez/RIPAM non determinano da sole la famiglia concorsuale.
- Rafforzare il mini-esercizio con cinque output obbligati: ente che assume, profilo, prova dominante, delta specialistico, fonte ufficiale da monitorare.
- Aggiungere sei quiz commentati, ciascuno con risposta corretta, spiegazione e distrattore tipico.
- Chiudere con una scheda compilabile che produca una decisione: `M-FC03 principale`, `M-FC03 di contesto`, `altro modulo`, `bando da verificare`.

## Fonti da usare

### Fonti M-FC03 e VOL-03

- `wiki/sources/m-fc03-dossier-redazionale-enti-pubblici-non-economici.md`: perimetro, confini, materie ad alta resa, regole di non duplicazione.
- `wiki/sources/m-fc03-fonti-ufficiali-enti-epne-2026.md`: canali istituzionali e uso prudente di INPS, INAIL ed enti di orientamento.
- `wiki/sources/m-fc03-portali-bandi-concorsi-2023-2026.md`: distinzione fra campione redazionale, avviso ufficiale, allegati e comunicazioni successive.
- `wiki/sources/m-fc03-bando-ripam-inail-308-funzionari-assistenti-sociali-2024.md`: esempio INAIL ad alta utilita, da non trasformare in regola universale.
- `wiki/sources/m-fc03-corpus-ufficiale-integrativo-2026-07-17.md`: profili ispettivi, CCNL, dati mobili e avvertenze su bandi/circolari.
- `wiki/sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md`: architettura VOL-03, principio di non duplicazione del VOL-01 e lacune da review.

### Topic, entity e quiz

- `wiki/topics/enti-pubblici-non-economici-concorsi.md`: nuclei da presidiare e rischio del concorso amministrativo generico.
- `wiki/topics/profili-previdenza-lavoro-vigilanza.md`: rischio di arrivare alla prova senza linguaggio specialistico.
- `wiki/entities/inps-inail-epne.md`: uso operativo di INPS, INAIL, EPNE di orientamento, profili ispettivi e amministrativi.
- `wiki/quizzes`: non sono stati trovati quiz M-FC03/EPNE pertinenti tramite `rg`; i quiz del capitolo devono essere prodotti nello step 09 e collegati al nucleo.

### Rinvii VOL-01 verificati

- `wiki/books/il-metodo-bando/chapters/famiglie-concorsi-pubblici.md#Famiglia 7 - Previdenza, lavoro e vigilanza`
- `wiki/books/il-metodo-bando/chapters/mappe-profilo-cosa-resta-comune-cosa-cambia.md#Mappa 7 - Previdenza, lavoro e vigilanza`
- `wiki/books/il-metodo-bando/chapters/scegliere-moduli-integrativi.md#Esempio A - Candidato INPS / INAIL`
- `wiki/books/il-metodo-bando/chapters/anatomia-del-bando.md#Il Bando Decoder`
- capitoli base per diritto amministrativo, pubblico impiego, trasparenza/privacy, contabilita pubblica, contratti pubblici, casi pratici e quesiti situazionali, da citare solo quando il rinvio e' preciso e utile.

Non usare `wiki/raw/` per produrre il testo finale. Le raw possono restare tracciate nelle source note, ma il capitolo deve derivare da wiki consolidato.

## Audit specialistici richiesti

1. Audit normativo introduttivo su legge 20 marzo 1975, n. 70; D.Lgs. 30 giugno 1994, n. 479; legge 9 marzo 1989, n. 88; D.P.R. 30 giugno 1965, n. 1124; D.Lgs. 23 febbraio 2000, n. 38, solo attraverso source note consolidate e con verifica di vigenza nello step 15.
2. Audit istituzionale sugli enti di orientamento: ACI, ENAC, ISTAT, ASI, ENEA, CONI, CRI e altri enti devono essere presentati con formula prudente, distinguendo natura giuridica, profilo e bando.
3. Audit bandi: ogni esempio puntuale deve distinguere bando, allegato, avviso, portale e fonte redazionale; nessun dato del campione 2023-2026 deve diventare dato stabile.
4. Audit dati operativi: il capitolo non deve contenere posti, scadenze, calendari, punteggi, soglie, requisiti mobili o PIAO/bilanci annuali senza fonte, ambito, versione e data.
5. Audit CCNL ARAN: se il capitolo cita aree, profili o Funzioni Centrali, rinviare il dettaglio al capitolo 08 e verificare CCNL vigente.
6. Audit rinvii: tutti i rinvii a VOL-01 e ad altri moduli devono avere file e heading esistenti; i rinvii generici sono bloccanti nella logica di copertura.
7. Audit di non duplicazione: il capitolo 01 deve restare ingresso e decisione di perimetro, non capitolo di ordinamento, previdenza, INAIL, governance o Bando Decoder completo.

## Struttura H1/H2/H3 proposta

1. `# Lavorare negli enti pubblici non economici`
2. `## Apertura editoriale`
3. `## Obiettivo e Mappa BANDO`
4. `## N-M-FC03-01-01 - Perimetro M-FC03 e confini`
   - `### Quando il modulo e' principale`
   - `### Quando e' solo contesto`
   - `### Quando serve un altro modulo`
5. `## N-M-FC03-01-02 - Core, delta EPNE e profilo concreto`
   - `### Core VOL-01`
   - `### Delta specialistico EPNE`
   - `### Profilo concreto e prova dominante`
6. `## N-M-FC03-01-03 - Enti guida ed enti di orientamento`
   - `### INPS`
   - `### INAIL`
   - `### Altri enti: criterio prudente`
7. `## N-M-FC03-01-04 - Riconoscere un bando M-FC03`
   - `### Fonte ed ente che assume`
   - `### Profilo e area`
   - `### Prova che seleziona davvero`
8. `## N-M-FC03-01-05 - Decoder iniziale, rischi e checklist`
   - `### Bando Decoder M-FC03`
   - `### Errori di perimetro`
   - `### Checklist di attivazione`
9. `## N-M-FC03-01-06 - Dalla classificazione alla decisione operativa`
   - `### Caso guidato`
   - `### Domanda, trappola ed esercizio`
   - `### Diario e decisione finale`
10. `## Verifica - perimetro e attivazione del modulo`
    - `### Sei quiz commentati`
    - `### Caso ragionato conclusivo`
    - `### Checklist finale`

## Blocchi 5-7 nuclei

Il capitolo deve usare un solo blocco di verifica dopo i sei nuclei: sei nuclei rientrano nella finestra 5-7 prevista dal formato 2. Non servono due blocchi di verifica per questo capitolo, salvo crescita oltre sette nuclei nello step 09.

| Blocco | Nuclei inclusi | Verifica richiesta |
| --- | --- | --- |
| Blocco unico capitolo 01 | `N-M-FC03-01-01` - `N-M-FC03-01-06` | Almeno 6 quiz commentati, un caso ragionato, checklist finale di decisione del modulo. |

## Budget parole, quiz e casi

La scheda pipeline VOL-03 non impone budget personalizzati per il capitolo 01. Budget operativo applicabile:

| Sezione | Budget parole | Quiz | Casi/esercizi |
| --- | ---: | ---: | --- |
| Apertura, obiettivo e Mappa BANDO | 350-450 | 0 | 0 |
| `N-M-FC03-01-01` | 650-750 | 1 | tabella perimetro |
| `N-M-FC03-01-02` | 650-750 | 1 | mappa core/delta/profilo |
| `N-M-FC03-01-03` | 650-750 | 1 | confronto INPS/INAIL/altro ente |
| `N-M-FC03-01-04` | 650-750 | 1 | lettura guidata di bando anonimo |
| `N-M-FC03-01-05` | 650-750 | 1 | Decoder e checklist |
| `N-M-FC03-01-06` + verifica | 850-1.000 | 1 | caso ragionato, domanda, trappola, mini-esercizio e diario |
| **Totale previsto** | **4.450-5.200** | **almeno 6** | **almeno 1 caso + 3 strumenti** |

Il testo attuale ha gia circa 4.061 parole. Dopo il retrofit e l'inserimento dei quiz commentati il target realistico e' 4.600-5.100 parole, compatibile con il capitolo introduttivo e con la leggibilita KDP.

## Criterio di completamento dello step 09

Lo step 09 sara completabile quando il capitolo:

- dichiara `format_version: 2`;
- usa i sei Nucleo ID stabili `N-M-FC03-01-01` - `N-M-FC03-01-06`;
- contiene almeno 600 parole per nucleo o segnala esplicitamente nella matrice ogni eventuale deviazione da sanare;
- conserva gli strumenti gia presenti senza trasformarli in report interno;
- contiene almeno sei quiz commentati e almeno un caso ragionato;
- rimuove dal corpo lettore riferimenti interni non destinati allo studente;
- mantiene rinvii VOL-01 e cross-family precisi, con file e heading esistenti;
- non presenta dati mobili come regole stabili;
- non modifica `pipeline/VOL-03/run-state.json` a mano.

## Limiti dello step 08

Questo report non modifica il capitolo e non chiude la copertura didattica. Non sostituisce lo step 09 di scrittura, lo step 10 di gate composito, lo step 12 di revisione del capitolo o lo step 15 di audit specialistico. La memoria locale e' stata richiamata prima dell'output, ma non e' stata aggiornata per rispettare il vincolo dell'utente: scrivere esclusivamente questo file di report.
