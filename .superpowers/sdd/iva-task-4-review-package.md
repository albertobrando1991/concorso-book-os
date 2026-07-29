# IVA Task 4 review package post-fix

## Git status
```text
 M wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md
 M wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
 M wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
```

## Diffstat
```text
 .../planning/02-indice-analitico-2026.md           |  4 +-
 .../planning/02-matrice-copertura-didattica.md     |  8 ++--
 ...c02-copertura-didattica-integrale-2026-07-17.md | 56 +++++++++++-----------
 3 files changed, 33 insertions(+), 35 deletions(-)
```

## Implementer report
# Task 4 report - Governance IVA e adempimenti

## Status

DONE_WITH_REVIEW_FIXES

## Baseline verificata

- Commit di contesto dichiarati dal brief: source `7ecd2c8`, cap. 4 `df2791d`, contenuti coordinati `1a8c3c1`.
- Governance iniziale: 80 nuclei, 64 `completo`, 16 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`; giudizio `Non pubblicabile allo stato attuale`.
- Righe interessate: `IVA - Presupposti, operazioni, rivalsa, detrazione, liquidazione` e `Adempimenti - Dichiarazione, versamento e compensazione`.
- La riga distinta `Ciclo fatto-documento-dichiarazione-liquidazione-versamento` era gia `completo` e non e stata riclassificata.

## Mappa delle prove reali

### Nucleo IVA

- teoria -> cap. 4, `IVA: operazioni, soggetti, detrazione e adempimenti`, incluse `Neutralita' come meccanismo, non come risultato assoluto`, `I tre presupposti`, `Soggetto passivo, debitore e consumatore finale`, `Le quattro classi di operazioni`; cap. 6, `Operazioni IVA e ciclo degli adempimenti`;
- caso -> cap. 6, caso Alfa e `Caso comparativo: quattro operazioni, quattro esiti`;
- output concorsuale -> cap. 4, `Checklist operativa finale`, che verifica anche l'uso dell'IVA come mappa e non come elenco; cap. 6, risposta modello alla commissione e classificazione operativa;
- verifica -> cap. 4, verifiche su neutralita e classi; cap. 6, quiz ragionati, domande-trappola e checklist;
- source -> `[[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]`, stato `consolidated`, audit ufficiale D.P.R. 633/1972, D.P.R. 100/1998 e direttiva 2006/112/CE;
- review -> PASS didattico locale; restano review umana tributaria/UE e verifica datata dei dati mobili.

### Nucleo dichiarazione, versamento e compensazione

- teoria -> cap. 6, `Dichiarazioni, versamenti e compensazioni`, con originaria, correttiva, integrativa, tardiva/omessa, F24, compensazione verticale/orizzontale, credito IVA e correzione;
- caso -> quattro casi dichiarativi e due scenari risolti di compensazione;
- output concorsuale -> risposta modello su ciclo IVA/dichiarazione/pagamento e gate in sei controlli;
- verifica -> quiz ragionati, domande-trappola e checklist;
- source -> `[[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]`, stato `consolidated`, audit ufficiale D.P.R. 322/1998, D.Lgs. 241/1997 e disciplina futura D.Lgs. 33/2025;
- review -> PASS didattico locale; restano review umana tributaria e verifica di modelli, termini, soglie e canali mobili.

## Esito governance e conteggi

- IVA: `parziale` -> `completo`.
- Dichiarazione, versamento e compensazione: `parziale` -> `completo`.
- Conteggi finali verificati: 80 nuclei, 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`.
- Giudizio mantenuto: **Non pubblicabile allo stato attuale**.

## Blocker residui (14)

1. Autotutela e ulteriori strumenti amministrativi/deflativi.
2. Misure cautelari ed esecuzione forzata AdER.
3. Regimi doganali.
4. Debito doganale e garanzia.
5. Prodotti energetici, alcole e tabacchi.
6. Tutela del giocatore, illegalita, prelievi e controlli.
7. DOCFA, PREGEO e voltura.
8. Estimo e applicazioni OMI.
9. Conti e partita doppia.
10. Indici ed equilibri aziendali.
11. Utile civilistico e reddito imponibile.
12. Crisi d'impresa.
13. Comunicazione, front-office e privacy.
14. Schede e destinazioni cross-family per crisi, HR, gare e ICT.

## File e diffstat

Dal Task 4 sono stati modificati esclusivamente i tre file governance autorizzati:

- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`
- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`

Diffstat governance finale: 3 file, 32 inserimenti, 34 eliminazioni. Creato inoltre questo report richiesto. Nessun capitolo, source note o raw modificato; nessun commit eseguito.

## Controlli

- `rg -c "\| completo \|" .../02-matrice-copertura-didattica.md` -> `66`.
- `rg -c "\| parziale \|" .../02-matrice-copertura-didattica.md` -> `14`.
- Ricerca degli stati `solo-nominato`, `rinviato`, `mancante` nelle righe matrice -> nessuna occorrenza (`rg` exit 1, conteggio logico 0 per ciascuno).
- Ricerca report -> giudizio `Non pubblicabile`, `14 blocker` e `14 nuclei` presenti; vecchi due blocker IVA/adempimenti assenti dall'elenco residuo.
- `git diff --check` sui tre file governance -> PASS; soli warning informativi CRLF/LF di Git.
- Controllo reciproco: 66 + 14 = 80; elenco residuo numerato 1-14.
- Fix review: heading matrice corretto in `Il ciclo dell'adempimento fiscale`; prova cap. 4 ricondotta al heading reale `Checklist operativa finale`; formulazione del perimetro file distinta dal worktree preesistente.

## Note operative

Il richiamo tramite `LocalAgentMemory` e stato tentato prima dell'output, ma il runner diretto Node non ha risolto l'import TypeScript extensionless `src/server/config`; nessuna memoria parallela e stata creata. `apply_patch` e stato tentato per primo, ma il wrapper Windows ha rifiutato la preparazione del sandbox; come previsto dal brief e stato usato un fallback chirurgico sui soli file autorizzati.

## Full diff
```diff
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md
index f0435c0..5a602b2 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md
@@ -26,22 +26,22 @@ draft_stage: revised-editorial-draft
 ## Blocco A - Ente, profilo e metodo
 
 1. Agenzie fiscali, funzioni e organizzazione.
 2. Bando Decoder AE, ADM e AdER.
 3. Piano tributario, doganale, ACFI e tecnico-catastale.
 
 ## Blocco B - Ciclo tributario
 
 4. Principi, fonti UE/nazionali e obbligazione tributaria — cap. 4.
 5. IRPEF e IRES: quadro sistematico e soggetti - cap. 4, `IRPEF e IRES: il quadro sistematico`; categorie reddituali, determinazione, reddito d'impresa, casi e verifiche - cap. 6, da `Imposte sui redditi: qualificare prima di calcolare` a `Trappole e checklist operativa sui redditi`; raccordo civilistico-contabile e variazioni fiscali - cap. 11, `14. Dal bilancio al reddito imponibile`.
-6. IVA e imposte indirette.
-7. Dichiarazioni, versamenti e adempimenti.
+6. IVA e imposte indirette - cap. 4, `IVA: operazioni, soggetti, detrazione e adempimenti` per funzione, presupposti, soggetti, rivalsa, detrazione e classi di operazioni; cap. 6, `Operazioni IVA e ciclo degli adempimenti` per qualificazione, documentazione, registrazione, liquidazione, dichiarazione, casi e verifiche.
+7. Dichiarazioni, versamenti e adempimenti - cap. 6, `Il ciclo dell'adempimento fiscale` e `Dichiarazioni, versamenti e compensazioni`, con dichiarazione originaria/correttiva/integrativa/omessa, F24, compensazione verticale e orizzontale, correzione, casi e verifiche.
 8. Accertamento, istruttoria e contraddittorio.
 9. Interpello, compliance, adempimento collaborativo e verticale ACFI: residenza, stabile organizzazione, convenzioni e doppia imposizione, transfer pricing, documentazione e operazioni infragruppo, rischio fiscale e Tax Control Framework - cap. 5.
 10. Riscossione e AdER.
 11. Sanzioni amministrative e reati tributari — intercalare 5A, sviluppato.
 12. Tutela e processo tributario secondo TU 175 vigente — intercalare 5B, sviluppato.
 
 ## Blocco C - Dogane e monopoli
 
 13. CDU: origine, valore, classificazione e obbligazione.
 14. Procedure doganali e D.Lgs. 141/2024.
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
index 1f5fc9c..143daeb 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
@@ -36,29 +36,29 @@ Audit semantico del testo reale dei 14 capitoli numerati e dei due intercalari 5
 | M-FC02/tutti | Organizzazione | Funzioni AE, ADM, AdER | alta | [[sources/assetti-organizzativi-ae-adm-ader-verifica-2026-07-17]] | cap. 3, `Le tre funzioni` e sezioni ente | funzioni spiegate | caso e risposta | orale/situazionale | esercizio | completo | aggiornare statuti/regolamenti | - |
 | M-FC02/tutti | Organizzazione | Strutture centrali/territoriali e organi | media | [[sources/assetti-organizzativi-ae-adm-ader-verifica-2026-07-17]] | cap. 3, `Organizzazione centrale` e `Organi` | modello spiegato, dettagli volutamente mobili | schema funzione/ufficio | orale | checklist | completo | review umana obbligatoria | - |
 | M-FC02/tutti | Orale | Risposta breve sull'organizzazione | alta | [[sources/agenzie-fiscali-organizzazione-ae-adm-ader]] | cap. 3, `Risposta modello da due minuti` | struttura della risposta esplicita | risposta completa | orale | domanda commissario | completo | aggiornare dati mobili | - |
 | M-FC02/tributario | Principi | Legalita, capacita contributiva, progressivita | alta | [[sources/costituzione-repubblica-italiana-testo-vigente]] | cap. 4, sezione omonima | principi definiti e distinti | esempi concorsuali | quiz/orale | quiz e caso | completo | review articolo-specifica | - |
 | M-FC02/tributario | Fonti | Gerarchia delle fonti tributarie | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4, `Le fonti` | livelli e funzione spiegati | lettura norma | orale | esercizio | completo | verifica vigenza | - |
 | M-FC02/tributario | Teoria imposta | Tributo, imposta, tassa, contributo | alta | [[topics/diritto-tributario-concorsi-agenzie-fiscali]] | cap. 4, sezione omonima | definizioni e distinzioni | tabella errori | quiz/orale | quiz | completo | stabile, review finale | - |
 | M-FC02/tributario | Teoria imposta | Presupposto e soggetto passivo | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4, sezioni omonime | definizione/funzione/conseguenze | caso guidato | quiz/orale | esercizio | completo | verifica fonti vigenti | - |
 | M-FC02/tributario | Teoria imposta | Base imponibile, aliquota, imposta dovuta | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4, sezione omonima | sequenza spiegata | esempio numerico semplice | quiz/orale | quiz | completo | non usare soglie mobili | - |
 | M-FC02/tributario | Rapporto tributario | Obbligazione e procedimento | alta | [[topics/diritto-tributario-concorsi-agenzie-fiscali]] | cap. 4, `Obbligazione tributaria` e `Rapporto` | nascita, funzione e interazione amministrativa | caso | orale | mini-esercizio | completo | review normativa | - |
 | M-FC02/tributario | IRPEF/IRES | Categorie reddituali, soggetti e reddito d'impresa | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]; [[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]] | cap. 4, `IRPEF e IRES: il quadro sistematico`; cap. 6, da `Imposte sui redditi: qualificare prima di calcolare` a `Trappole e checklist operativa sui redditi`; cap. 11, `14. Dal bilancio al reddito imponibile` | quadro sistematico, soggetti IRPEF/IRES, sei categorie, criteri di qualificazione e determinazione, reddito d'impresa e ponte utile-imponibile spiegati | esempi per categoria, caso IRPEF multi-componente, caso IRES e raccordo contabile con variazioni fiscali | classificazione motivata, risposta orale comparativa e ricostruzione del reddito imponibile | errori/verifiche per categoria, quiz dedicati, esercizio e checklist | completo | review TUIR vigente e disciplina articolo-specifica obbligatorie | - |
-| M-FC02/tributario | IVA | Presupposti, operazioni, rivalsa, detrazione, liquidazione | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4 `IVA`; cap. 6 `IVA: mappa essenziale` | architettura spiegata, casistica/esclusioni limitate | caso societa | quiz/orale | quiz | parziale | DPR 633/1972 vigente | - |
+| M-FC02/tributario | IVA | Presupposti, operazioni, rivalsa, detrazione, liquidazione | alta | [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]] | cap. 4, `IVA: operazioni, soggetti, detrazione e adempimenti`; cap. 6, `Operazioni IVA e ciclo degli adempimenti` | funzione, armonizzazione, presupposti, soggetti, quattro classi, base, rivalsa, detrazione, documentazione e liquidazione spiegati | caso Alfa e caso comparativo su quattro operazioni | caso/quiz/orale | verifiche, quiz e checklist | completo | review tributaria/UE; dati mobili esclusi | - |
 | M-FC02/tributario | Accertamento | Controllo automatico, formale, sostanziale | alta | [[sources/accertamento-contraddittorio-compliance-aggiornamento-2026-07-17]] | cap. 5, sezione omonima | differenze e funzione spiegate | caso | quiz/orale | quiz | completo | verificare articoli | - |
 | M-FC02/tributario | Accertamento | Selezione, istruttoria, contraddittorio, atto | alta | [[sources/accertamento-contraddittorio-compliance-aggiornamento-2026-07-17]] | cap. 5, sezioni `Dal dato`-`Atto finale` | sequenza, poteri, prova e motivazione spiegati | caso guidato | caso/orale | esercizio | completo | art. 6-bis e termini mobili | - |
 | M-FC02/tributario | Tutela amministrativa/deflativa | Condizioni ed effetti articolo-specifici di autotutela e ulteriori strumenti deflativi | alta | [[sources/accertamento-contraddittorio-compliance-aggiornamento-2026-07-17]], [[sources/processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18]] | cap. 5, `Autotutela, definizione e tutela giurisdizionale`; cap. 5B, sez. 1-2 | tutela giurisdizionale e processo coperti sistematicamente nel 5B; restano funzionali, non articolo-specifici, condizioni ed effetti dei singoli strumenti amministrativi/deflativi | caso Omega e raccordi | orale/caso | tabella tre piani e verifiche; manca batteria sui singoli strumenti | parziale | riforme recenti e disciplina specifica degli strumenti | - |
 | M-FC02/tributario | Compliance | Compliance ordinaria | alta | [[sources/adempimento-collaborativo-compliance-fiscale-m-fc02]] | cap. 5, `Compliance fiscale ordinaria` | funzione e strumenti spiegati | esempio comunicazione | orale/caso | checklist | completo | aggiornare strumenti | - |
 | M-FC02/ACFI | Compliance | Adempimento collaborativo e tax control framework | alta profilo | [[sources/adempimento-collaborativo-compliance-fiscale-m-fc02]] | cap. 5, sezione omonima | struttura, rischio e interlocuzione spiegati | caso | orale/caso | quiz | completo | soglie/requisiti mobili | - |
 | M-FC02/ACFI | Fiscalita internazionale | Residenza, stabile organizzazione, convenzioni e doppia imposizione, transfer pricing, documentazione e operazioni infragruppo, rischio fiscale e Tax Control Framework | alta profilo | [[sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18]] | cap. 5, `Profili ACFI e fiscalita internazionale`, da `Fonti e metodo operativo` a `Commissario, trappole, esercizio e quiz` | istituti, fonti e metodo operativo spiegati nel perimetro ACFI selettivo | caso completo ACFI e mini-esercizio risolto | domanda da commissario, checklist e mappa dei rischi | verifiche risolte e quiz dedicati | completo | review didattica ACFI superata il 2026-07-18; manutenzione normativa e verifica delle fonti vigenti ancora obbligatorie | - |
-| M-FC02/tributario | Adempimenti | Ciclo fatto-documento-dichiarazione-liquidazione-versamento | alta | [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]] | cap. 6, `Il ciclo dell'adempimento` | sequenza spiegata | caso societa | caso/orale | esercizio | completo | modelli e termini mobili | - |
-| M-FC02/tributario | Adempimenti | Dichiarazione, versamento e compensazione | alta | [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]] | cap. 6, sezione omonima | funzioni distinte, correttive/integrative e limiti non sviluppati | caso generico | orale | quiz | parziale | DPR 322 e DLgs 241 vigenti | - |
+| M-FC02/tributario | Adempimenti | Ciclo fatto-documento-dichiarazione-liquidazione-versamento | alta | [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]] | cap. 6, `Il ciclo dell'adempimento fiscale` | sequenza spiegata | caso societa | caso/orale | esercizio | completo | modelli e termini mobili | - |
+| M-FC02/tributario | Adempimenti | Dichiarazione, versamento e compensazione | alta | [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]] | cap. 6, `Dichiarazioni, versamenti e compensazioni` | originaria, correttiva, integrativa, tardiva/omessa, F24, compensazione verticale/orizzontale, credito IVA e correzione spiegati | quattro casi dichiarativi e due scenari di compensazione | caso/orale | quiz, domande-trappola e checklist | completo | review tributaria; modelli, termini, soglie e canali mobili | - |
 | M-FC02/servizi | Servizi fiscali | Assistenza e rapporto col contribuente | media | [[sources/m-fc02-dossier-redazionale-agenzie-fiscali]] | cap. 6, sezione omonima | ruolo, documenti e limiti spiegati | front-office | situazionale | checklist | completo | aggiornare servizi telematici | - |
 | M-FC02/AdER | Riscossione | Imposizione, accertamento, riscossione | alta | [[topics/riscossione-tributaria-ader]] | cap. 7, sez. 1-2 | fasi e competenze distinte | casi | quiz/orale | quiz | completo | review normativa | - |
 | M-FC02/AdER | Riscossione | Ruolo, cartella, pagamento | alta | [[sources/riscossione-ader-aggiornamento-istituzionale-2026-07-17]] | cap. 7, sez. 3 | sequenza e atti spiegati | caso cartella | caso/orale | esercizio | completo | DPR 602 vigente | - |
 | M-FC02/AdER | Riscossione | Accertamento esecutivo e presa in carico | alta | [[sources/riscossione-ader-aggiornamento-istituzionale-2026-07-17]] | cap. 7, sez. 4 | modello e differenze spiegati | raccordo con caso | quiz/orale | quiz | completo | verificare disciplina vigente | - |
 | M-FC02/AdER | Riscossione | Rateizzazione, sospensione, sgravio, ricorso | alta | [[sources/riscossione-ader-aggiornamento-istituzionale-2026-07-17]] | cap. 7, sez. 5-6 | funzioni e competenze distinte | caso pagamento gia eseguito | situazionale | quiz | completo | soglie/termini mobili | - |
 | M-FC02/AdER | Riscossione | Misure cautelari ed esecuzione forzata | alta | [[sources/riscossione-agenzia-entrate-riscossione-m-fc02]] | cap. 7, sez. 7 | categorie inquadrate, presupposti/limiti non sviluppati | nessun caso dedicato | orale introduttivo | quiz limitato | parziale | soglie/esclusioni da verificare | - |
 | M-FC02/AdER | Lavoro | Front-office/back-office, competenza e tracciabilita | alta profilo | [[sources/assetti-organizzativi-ae-adm-ader-verifica-2026-07-17]] | cap. 7, sez. 8-9 | condotta e limiti spiegati | caso utente | situazionale | checklist | completo | allineare avviso/CCNL | - |
 | M-FC02/ADM | Dogane | Fonti UE e complemento nazionale | alta | [[sources/codice-doganale-unione-procedure-adm-aggiornamento-2026-07-17]] | cap. 8, sez. 1 | gerarchia e funzione spiegate | mappa procedurale | quiz/orale | quiz | completo | CDU consolidato | - |
 | M-FC02/ADM | Dogane | Territorio doganale e status merci | alta | [[sources/dogane-accise-giochi-monopoli-adm-m-fc02]] | cap. 8, sez. 2 | definizioni e conseguenze spiegate | caso import | quiz/orale | glossario/quiz | completo | review UE | - |
 | M-FC02/ADM | Dogane | Dichiarazione, dichiarante e rappresentanza | alta | [[sources/codice-doganale-unione-procedure-adm-aggiornamento-2026-07-17]] | cap. 8, sez. 3-5 | soggetti e sequenza spiegati | caso | caso/orale | quiz | completo | sistemi telematici mobili | - |
@@ -98,11 +98,11 @@ Audit semantico del testo reale dei 14 capitoli numerati e dei due intercalari 5
 | M-FC02/tutti | Sanzioni | Sanzioni amministrative tributarie | alta da indice | [[sources/sanzioni-amministrative-tributarie-aggiornamento-2026-07-18]] | cap. 5A, sez. 1-9 | principi, autore, cause, concorsi, fattispecie, ravvedimento e procedimento spiegati | caso dichiarazione/ravvedimento | caso/quiz/orale | mini-esercizio, quiz e checklist | completo | review tributaria e disciplina temporale | - |
 | M-FC02/tutti | Reati | Reati tributari e raccordo reati contro PA | alta da piano | [[sources/reati-tributari-dlgs-74-2000-aggiornamento-2026-07-18]] | cap. 5A, sez. 10-16 | famiglie D.Lgs. 74/2000, dolo, pagamento, confisca e raccordi spiegati; PA con rinvio verificato | documenti inesistenti e sottrazione | caso/quiz/orale | esercizio, quiz e checklist | completo | review penal-tributaria; TU 173 dal 2027 | - |
 | M-FC02/tutti | Processo | Tutela e processo tributario | alta da indice | [[sources/processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18]] | cap. 5B, sez. 1-13 | tutela, organi, parti, atti, ricorso, prova, cautela, conciliazione, decisione, impugnazioni ed esecuzione spiegati | caso Omega atto-esito | caso/quiz/orale | esercizi, quiz e checklist PTT | completo | TU 175 vigente; review processuale | - |
 | M-FC02/tutti | UE | Diritto UE fiscale e doganale trasversale | media/alta | [[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]] | cap. 4, `Livello 3 - Quadro UE`; rinvio cap. 8, sez. 1 | competenze, fonti, regolamento/direttiva, IVA armonizzata e sistema CDU-2446-2447 spiegati | importazione e vendita interna | quiz/orale/caso | domanda-trappola, errori e verifica | completo | versioni EUR-Lex e attuazione nazionale | - |
 | M-FC02/front-office | Relazione | Comunicazione, data protection, contribuente/operatore | alta profilo | [[sources/regolamento-ue-2016-679-gdpr-protezione-dati-personali]] | cap. 14, appendice C solo prevista; frammenti cap. 7/13 | teoria privacy e comunicazione non sistematica | casi sparsi | situazionale previsto | nessuna verifica dedicata | parziale | GDPR e policy enti | - |
 | M-FC02/tutti | Lessico | Glossario fiscale-doganale-catastale 80-100 voci | media | [[sources/m-fc02-dossier-redazionale-agenzie-fiscali]] | cap. 14, appendice A | 80 voci uniche con definizione funzionale, distinzione e rinvio preciso | esempi incorporati negli strumenti | ripasso/orale | checklist e piano | completo | aggiornamento terminologico al cut-off | - |
 | M-FC02/tutti | Perimetro | Schede allerta crisi, HR, gare, ICT | media | [[sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026]] | cap. 14, appendice E solo prevista | criteri sparsi nei capp. 1-2, scheda promessa assente | rinvii generici di famiglia | tabella prevista | nessuna | parziale | verificare bandi | - |
 
 ## Totali
 
-La classificazione contiene 80 nuclei: 64 `completo`, 16 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. Il validatore rileva quindi 16 blocker editoriali.
+La classificazione contiene 80 nuclei: 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. Il validatore rileva quindi 14 blocker editoriali.
diff --git a/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md b/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
index ee23287..96d0378 100644
--- a/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
+++ b/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
@@ -19,37 +19,37 @@ severity: critical
 affected_pages: ["books/moduli/m-fc02-agenzie-fiscali"]
 ---
 
 # Report editoriale - M-FC02 Agenzie fiscali
 
 ## 1. Sintesi editoriale
 
 - Genere editoriale: manuale-workbook specialistico per concorsi nelle Agenzie fiscali.
 - Pubblico target: candidati AE, ADM, AdER e profili Territorio/SPI, con nucleo comune nel VOL-01.
 - Perimetro di questa revisione: index, piano, indice analitico, 14 capitoli numerati e intercalari 5A/5B; confronto con source/topic/entity consolidate.
-- Stato generale in una frase: sanzioni, reati, processo, quadro UE, perimetro selettivo ACFI e nucleo IRPEF/IRES sono ora sviluppati e tracciati, ma il modulo resta non pubblicabile per 16 blocker residui, tutti nuclei parziali.
+- Stato generale in una frase: sanzioni, reati, processo, quadro UE, perimetro selettivo ACFI, IRPEF/IRES, IVA e adempimenti sono ora sviluppati e tracciati, ma il modulo resta non pubblicabile per 14 blocker residui, tutti nuclei parziali.
 
 ## 2. Punti applicati della checklist
 
 Applicati i punti 1-15 e 17-21, 29-30, oltre al gate aggiuntivo di copertura integrale. I punti 16 e 22-26 sono stati osservati solo quando incidenti sulla chiarezza della promessa, poiche il perimetro non era una correzione microtestuale. I punti 27-28 non sono applicabili: non e' stato fornito un impaginato finale. Ogni promessa e' stata confrontata con spiegazione, esempio, output, verifica e fonti reali; lunghezza e presenza del file non sono state usate come prova di completezza.
 
 ## 3. Tabella errori
 
 | ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato |
 | --- | --- | --- | --- | --- | --- | --- |
 | E01 | Cap. 12, intero | Completezza spiegazioni/gate | Grave | Il precedente stato `source_ready` e' superato: civile, contratti, impresa e societa sono sviluppati con casi e verifiche. La crisi resta deliberatamente parziale. | Mantenere chiuso il gap strutturale; consolidare una source ufficiale dedicata prima di ampliare la crisi d'impresa. | Chiuso per civile/commerciale; crisi aperta |
 | E02 | Cap. 14, intero | Completezza spiegazioni/gate | Grave | Il precedente placeholder e' superato: il capitolo e' un workbook autonomo con glossario di 80 voci, tavole, scadenziario, schemi, canvas, orale e ripasso. Non sostituisce i nuclei teorici mancanti o parziali. | Mantenere chiuso il gap workbook; sviluppare separatamente privacy e destinazioni cross-family, senza attribuire al workbook funzioni teoriche ulteriori. | Chiuso per workbook; nuclei teorici aperti |
 | E03 | Cap. 5A | Promessa didattica | Grave | Sanzioni amministrative e reati tributari sono ora sviluppati con fonti vigenti, casi, quiz e verifiche. | Mantenere review tributaria/penal-tributaria e controllo del passaggio al TU 173 dal 2027. | Chiuso |
 | E04 | Cap. 5B | Promessa didattica | Grave | Tutela e processo tributario sono ora sviluppati autonomamente secondo il TU 175 vigente, con cautela, prova, impugnazioni ed esecuzione. | Mantenere verifica articolo-specifica e review processual-tributaria. | Chiuso |
 | E05 | Cap. 5, `Profili ACFI e fiscalita internazionale` | Copertura selettiva ACFI | Grave | Il perimetro ACFI sviluppa residenza, stabile organizzazione, convenzioni e doppia imposizione, transfer pricing, documentazione e operazioni infragruppo, rischio fiscale e TCF, con fonti consolidate, caso, verifiche e quiz dedicati. | Mantenere il perimetro selettivo e la review normativa/editoriale; non estendere la promessa all'intera fiscalita internazionale. | Chiuso |
 | E06 | Capp. 4, 6 e 11, redditi | Completezza spiegazioni | Grave | Il cap. 4 inquadra soggetti e architettura IRPEF/IRES; il cap. 6 sviluppa le sei categorie, qualificazione e determinazione, reddito d'impresa, soggetti e struttura IRES con casi, quiz e orale; il cap. 11 completa il raccordo civilistico-contabile e le variazioni fiscali. | Mantenere review TUIR articolo-specifica e aggiornare le discipline mobili senza riaprire il nucleo didattico. | Chiuso |
-| E07 | Capp. 4 e 6, IVA | Completezza spiegazioni | Grave | Architettura IVA presente, ma casistica, esclusioni e applicazione sono troppo sintetiche per autonomia specialistica. | Ampliare presupposti/operazioni, detrazione, documentazione e liquidazione con casi graduati. | Aperto |
+| E07 | Capp. 4 e 6, IVA e adempimenti | Completezza spiegazioni | Grave | Funzione, presupposti, soggetti, classi di operazioni, rivalsa, detrazione, documentazione e liquidazione sono sviluppati; dichiarazioni successive, F24, compensazioni e correzioni hanno casi e verifiche dedicate, con fonti ufficiali consolidate al 20 luglio 2026. | Mantenere review tributaria/UE e verificare soltanto i dati mobili prima della pubblicazione. | Chiuso |
 | E08 | Capp. 5 e 5B, tutela amministrativa/deflativa | Progressione/completezza | Grave | Il cap. 5B copre sistematicamente tutela giurisdizionale e processo. Restano parziali le condizioni e gli effetti articolo-specifici di autotutela e degli ulteriori strumenti amministrativi/deflativi richiamati nei capp. 5 e 5B. | Sviluppare per ciascuno strumento amministrativo/deflativo presupposti, competenza, procedimento ed effetti, senza riaprire il nucleo processuale gia coperto. | Aperto, perimetro delimitato |
 | E09 | Cap. 7, misure cautelari/esecutive | Completezza | Grave | Categorie presenti, ma presupposti, limiti e distinzioni non raggiungono autonomia didattica. | Integrare schema comparativo e caso, dopo verifica delle soglie vigenti. | Aperto |
 | E10 | Cap. 8, regimi e debito doganale | Completezza | Grave | Regimi, debito e garanzia sono corretti come mappa ma insufficienti per il peso ADM. | Sviluppare condizioni, effetti, responsabilita e casi distinti con CDU consolidato. | Aperto |
 | E11 | Cap. 9, settori accise e giochi | Completezza | Grave | Prodotti, prelievi e controlli sono volutamente sintetici; l'output specialistico resta parziale. | Integrare nucleo stabile e rinviare solo dati mobili a fonti vive precise. | Aperto |
 | E12 | Cap. 10, DOCFA/PREGEO/estimo | Completezza tecnica | Grave | Le funzioni sono spiegate, ma procedura e applicazione estimativa richiedono maggiore profondita e review specialistica. | Aggiungere casi procedurali e applicazioni validate da revisore tecnico. | Aperto |
 | E13 | Cap. 11, partita doppia/indici/fisco | Completezza tecnica | Grave | La teoria e' leggibile, ma esercizi svolti e applicazione numerica non sono proporzionati alla promessa contabile. | Aggiungere registrazioni, riclassificazioni, indici e raccordi civilistico-fiscali svolti. | Aperto |
 | E14 | Cap. 14/7/13, privacy e front-office | Coerenza tra capitoli | Grave | Frammenti applicativi esistono, ma manca teoria unitaria su comunicazione, riservatezza e protezione dati. | Consolidare nel cap. 14 e rinviare dai casi con destinazione precisa. | Aperto |
 | E15 | Capp. 1-2 e cap. 14/E | Rinvii | Grave | I rinvii cross-family indicano il modulo, ma non una destinazione verificata a capitolo/paragrafo completo. | Trasformarli in destinazioni precise solo dopo verifica del contenuto ricevente. | Aperto |
 | E16 | Tutti i capitoli tecnici | Accuratezza normativa | Grave | Numerose note dichiarano norme, assetti, soglie, sistemi e procedure mobili da verificare. | Eseguire review umana normativa/tecnica prima di qualunque stato pubblicabile. | Da verificare |
 
@@ -62,36 +62,36 @@ Applicati i punti 1-15 e 17-21, 29-30, oltre al gate aggiuntivo di copertura int
 ### Capitolo 2 - Bando Decoder fiscale
 - Punti di forza: trasforma sistematicamente ente, profilo, prove e materie in output.
 - Criticita: valgono i limiti sui rinvii; denominazioni e prove richiedono sempre bando vivo.
 
 ### Capitolo 3 - Ordinamento e organizzazione
 - Punti di forza: distingue natura, funzioni, MEF e livelli organizzativi con caso e orale.
 - Criticita: assetti e regolamenti sono mobili e correttamente marcati per review.
 
 ### Capitolo 4 - Diritto tributario e teoria dell'imposta
 - Punti di forza: nucleo teorico di base, quadro sistematico IRPEF/IRES e Livello 3 UE completi, con competenze, fonti, IVA armonizzata e sistema CDU tracciati.
-- Criticita: l'IVA non raggiunge ancora la profondita specialistica promessa dai capitoli successivi; il quadro dei redditi resta soggetto a review normativa articolo-specifica.
+- Criticita: IVA e quadro dei redditi restano soggetti a review normativa articolo-specifica e alla verifica dei dati mobili, senza gap didattico locale aperto.
 
 ### Capitolo 5 - Accertamento, controlli e compliance
 - Punti di forza: ciclo del controllo, contraddittorio e compliance sono ben strutturati; il blocco ACFI tratta con metodo operativo gli istituti internazionali selezionati, fino a caso, verifiche e quiz.
 - Criticita: la tutela resta parziale; il blocco ACFI richiede manutenzione normativa sulle fonti e convenzioni vigenti, senza promettere una trattazione integrale della fiscalita internazionale.
 
 ### Capitolo 5A - Sanzioni amministrative e reati tributari
 - Punti di forza: distingue tributo, interessi, sanzione e reato; sviluppa parte generale, fattispecie, ravvedimento e D.Lgs. 74/2000 con casi e verifiche.
 - Criticita: soglie, pene e disciplina temporale richiedono review umana; il TU 173 resta applicabile dal 2027.
 
 ### Capitolo 5B - Tutela e processo tributario
 - Punti di forza: percorso autonomo dal riesame all'ottemperanza secondo TU 175, con prova, cautela, PTT, conciliazione e impugnazioni.
 - Criticita: termini, specifiche telematiche e singoli articoli richiedono controllo sulla versione coordinata vigente.
 ### Capitolo 6 - Adempimenti fiscali
 - Punti di forza: sequenza economica-documentale-dichiarativa chiara e applicata; categorie IRPEF, determinazione, reddito d'impresa e struttura IRES sono sviluppati con esempi, casi, quiz, orale e checklist.
-- Criticita: IVA, dichiarazioni correttive/integrative e compensazioni richiedono espansione; i redditi richiedono manutenzione normativa sul TUIR vigente.
+- Criticita: IVA, dichiarazioni e compensazioni richiedono manutenzione normativa sui dati mobili; i redditi richiedono manutenzione sul TUIR vigente.
 
 ### Capitolo 7 - Riscossione e AdER
 - Punti di forza: competenze, sequenze, front-office e principali alternative sono chiare.
 - Criticita: misure cautelari/esecutive e dati mobili non sono ancora sufficienti per pubblicazione.
 
 ### Capitolo 8 - Dogane
 - Punti di forza: progressione dall'arrivo allo svincolo e triade classificazione/origine/valore efficace.
 - Criticita: regimi, debito e garanzia richiedono maggiore profondita e fonte UE consolidata vigente.
 
 ### Capitolo 9 - Accise, giochi e monopoli
@@ -114,63 +114,61 @@ Applicati i punti 1-15 e 17-21, 29-30, oltre al gate aggiuntivo di copertura int
 - Punti di forza: casi differenziati, quiz, orale, diario e piano 30/60/90 formano un laboratorio autonomo.
 - Criticita: casi e quiz devono essere riesaminati dopo gli aggiornamenti normativi dei capitoli tecnici.
 
 ### Capitolo 14 - Appendici operative
 - Punti di forza: workbook autonomo con 80 voci di glossario, tavole comparative, scadenziario, checklist, schemi, canvas, orale e piano 1-3-7-14-30; rinvii verificati ai capitoli.
 - Criticita: i presidi su privacy, crisi e rinvii cross-family restano parziali e non vanno scambiati per teoria validata.
 
 ## 5. Coerenza globale
 
 - Terminologia: generalmente coerente; distinzione accertamento/riscossione ben presidiata.
-- Struttura vs indice: coerente per sanzioni, reati, processo, quadro UE, perimetro ACFI e IRPEF/IRES, collocati nei capp. 4, 5, 5A, 5B, 6 e 11; restano i 16 blocker parziali censiti.
-- Promesse dell'introduzione mantenute: solo in parte. Orientamento, performance, civile/commerciale, sanzioni/processo, quadro UE, perimetro ACFI, IRPEF/IRES e workbook sono forti; i 16 blocker impediscono ancora la copertura integrale.
+- Struttura vs indice: coerente per sanzioni, reati, processo, quadro UE, perimetro ACFI, IRPEF/IRES, IVA e adempimenti, collocati nei capp. 4, 5, 5A, 5B, 6 e 11; restano i 14 blocker parziali censiti.
+- Promesse dell'introduzione mantenute: solo in parte. Orientamento, performance, civile/commerciale, sanzioni/processo, quadro UE, perimetro ACFI, IRPEF/IRES, IVA, adempimenti e workbook sono forti; i 14 blocker impediscono ancora la copertura integrale.
 
 ## 6. Contenuto da verificare
 
 - Vigenza di statuti, regolamenti e assetti AE/ADM/AdER.
 - TUIR, IVA, accertamento, contraddittorio, riscossione e processo tributario vigenti.
 - CDU, regolamenti delegato/esecutivo, D.Lgs. 141/2024 e sistemi ADM.
 - TUA, EMCS/e-AD, riordino giochi, concessioni e prelievi.
 - DOCFA, PREGEO, Voltura Web, Sister, OMI e procedimenti estimativi.
 - Codice civile/OIC, TUIR d'impresa, scritture e indici.
 - Sanzioni, reati tributari, privacy e crisi d'impresa.
 
 ## 7. Suggerimenti facoltativi (non errori)
 
 - Mantenere i glossari locali anche dopo la creazione del glossario unitario, usandoli come ripasso di capitolo.
 - Usare una sola simulazione trasversale aggiornata dopo la chiusura dei gap, invece di duplicare batterie simili.
 
 ## 8. Priorita degli interventi
 
-1. Chiudere i 16 nuclei parziali senza usare capitoli operativi o rinvii generici come sostituti della teoria.
+1. Chiudere i 14 nuclei parziali senza usare capitoli operativi o rinvii generici come sostituti della teoria.
 2. Mantenere aggiornato e sottoposto a review il perimetro selettivo ACFI, senza ampliarlo implicitamente all'intera fiscalita internazionale.
 3. Consolidare le fonti mancanti per crisi, privacy e verticali tecnici e svolgere review specialistiche.
 4. Riesaminare casi, quiz e laboratorio dopo la chiusura dei nuclei tecnici.
 5. Validare le destinazioni cross-family prima di trasformare i gap in rinvii editoriali.
 
 ## 9. Giudizio di pubblicabilita
 
-**Non pubblicabile allo stato attuale.** La matrice registra 80 nuclei: 64 `completo`, 16 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. I blocker editoriali sono quindi 16.
-
-I 16 nuclei `parziale` restano:
-
-1. IVA, casistica ed esclusioni;
-2. condizioni ed effetti articolo-specifici di autotutela e degli ulteriori strumenti amministrativi/deflativi;
-3. dichiarazione, versamento, compensazione e correzioni;
-4. misure cautelari ed esecuzione forzata AdER;
-5. regimi doganali;
-6. debito doganale e garanzia;
-7. prodotti energetici, alcole e tabacchi;
-8. tutela del giocatore, illegalita, prelievi e controlli;
-9. DOCFA, PREGEO e voltura;
-10. estimo e applicazioni OMI;
-11. conti e partita doppia;
-12. indici ed equilibri aziendali;
-13. utile civilistico e reddito imponibile;
-14. crisi d'impresa;
-15. comunicazione, front-office e privacy;
-16. schede e destinazioni cross-family per crisi, HR, gare e ICT.
-
-Il perimetro selettivo della fiscalita internazionale ACFI e' chiuso didatticamente nel cap. 5; non equivale a una promessa di copertura integrale della materia. Non restano nuclei `solo-nominato` o `mancante`: sanzioni, reati, processo, quadro UE, ACFI e IRPEF/IRES sono stati chiusi didatticamente nei capp. 4, 5, 5A, 5B, 6 e 11. Restano 16 blocker parziali e il modulo non e' pubblicabile. E16 mantiene obbligatoria la review normativa e tecnica prima della pubblicazione.
+**Non pubblicabile allo stato attuale.** La matrice registra 80 nuclei: 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. I blocker editoriali sono quindi 14.
+
+I 14 nuclei `parziale` restano:
+
+1. condizioni ed effetti articolo-specifici di autotutela e degli ulteriori strumenti amministrativi/deflativi;
+2. misure cautelari ed esecuzione forzata AdER;
+3. regimi doganali;
+4. debito doganale e garanzia;
+5. prodotti energetici, alcole e tabacchi;
+6. tutela del giocatore, illegalita, prelievi e controlli;
+7. DOCFA, PREGEO e voltura;
+8. estimo e applicazioni OMI;
+9. conti e partita doppia;
+10. indici ed equilibri aziendali;
+11. utile civilistico e reddito imponibile;
+12. crisi d'impresa;
+13. comunicazione, front-office e privacy;
+14. schede e destinazioni cross-family per crisi, HR, gare e ICT.
+
+Il perimetro selettivo della fiscalita internazionale ACFI e' chiuso didatticamente nel cap. 5; non equivale a una promessa di copertura integrale della materia. Non restano nuclei `solo-nominato` o `mancante`: sanzioni, reati, processo, quadro UE, ACFI, IRPEF/IRES, IVA e adempimenti sono stati chiusi didatticamente nei capp. 4, 5, 5A, 5B, 6 e 11. Restano 14 blocker parziali e il modulo non e' pubblicabile. E16 mantiene obbligatoria la review normativa e tecnica prima della pubblicazione.
 
 ## 10. Limiti di questa revisione
 Audit eseguito sul markdown e sulle note consolidate presenti nel wiki, senza usare `raw/` e senza ricerca web. Non sono stati verificati layout impaginato, vigenza articolo-per-articolo, correttezza specialistica contabile/estimativa o aggiornamento dei sistemi telematici. Lo stato `completo` indica completezza didattica rispetto alla promessa locale osservata, non certificazione normativa finale.

```