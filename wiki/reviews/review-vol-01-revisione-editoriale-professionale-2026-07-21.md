---
id: review-vol-01-revisione-editoriale-professionale-2026-07-21
type: review
title: "VOL-01 - Revisione editoriale professionale e gate di pubblicabilita"
status: completed
domain: "concorsi pubblici italiani"
topics: ["copertura didattica integrale", "revisione editoriale", "pubblicabilita"]
entities: ["VOL-01", "Metodo BANDO"]
source_refs: ["sources/principio-copertura-didattica-integrale-2026-07-17.md", "sources/vol-01-il-metodo-bando-struttura-2026-07-14.md", "sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.9
updated_at: 2026-07-21T00:00:00+02:00
created_at: 2026-07-21T00:00:00+02:00
review_required: false
canonical: true
issue_type: editorial_review
severity: high
affected_pages: ["intero volume"]
tags: ["revisore-editoriale-totale", "vol-01", "gate-pubblicazione", "audit"]
---

# Report editoriale - Il Metodo BANDO (VOL-01)

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook per la preparazione ai concorsi pubblici italiani.
- Pubblico target: candidati generalisti e amministrativi che devono costruire un nucleo comune riutilizzabile e adattarlo al bando.
- Perimetro di questa revisione: volume principale completo, cioe' introduzione, capitoli 1-24 e appendici A-F; il Ricettario digitale 25-47 e' stato escluso dal giudizio sul cartaceo.
- Consistenza esaminata: 31 file principali, circa 116.740 parole e 104 source note distinte dichiarate nel frontmatter.
- Stato generale in una frase: impianto didattico robusto e ampio, ma non pubblicabile per 15 nuclei ancora `parziale`, 28 file con `review_required: true`, promesse specifiche non chiuse, sconfinamenti nel delta specialistico e apparato interno ancora visibile.
- Esito principale: e' stata creata la matrice conforme in `books/il-metodo-bando/planning/02-matrice-copertura-didattica.md`; la matrice non maschera i blocker e assegna solo 2 nuclei `completo` su 17.

## 2. Punti applicati della checklist

Sono stati applicati tutti i 30 punti della checklist del Revisore Editoriale Totale:

1. indice rispetto alla struttura reale;
2. completezza e bilanciamento della struttura;
3. progressione logica;
4. gerarchia di titoli e sottotitoli;
5. idoneita finale alla pubblicazione;
6. coerenza interna dei capitoli;
7. coerenza tra capitoli;
8. coerenza terminologica;
9. completezza delle spiegazioni;
10. accuratezza delle definizioni;
11. errori concettuali;
12. errori normativi o contenutistici;
13. qualita degli esempi;
14. tabelle, box, richiami e schemi;
15. apparato normativo e bibliografico;
16. sintassi;
17. chiarezza espositiva;
18. tono editoriale;
19. stile didattico;
20. ripetizioni;
21. contraddizioni;
22. grammatica;
23. ortografia;
24. punteggiatura;
25. refusi;
26. uniformita grafica;
27. impaginazione, limitatamente al Markdown e al comportamento noto di Book Studio: non era disponibile un PDF finale da stampa;
28. layout di tabelle, box ed elenchi;
29. leggibilita complessiva;
30. qualita editoriale complessiva.

E' stato applicato inoltre il gate di copertura didattica integrale: ogni promessa e' stata confrontata con teoria, distinzione, applicazione, verifica, fonte e review normativa. Il numero di parole e l'esistenza del file non sono stati usati come prova di completezza.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| E01 | Intero VOL-01 | Pubblicabilita e review normativa | Grave | La matrice rileva 15 nuclei `parziale`; 28 dei 31 file principali hanno ancora `review_required: true`. | Chiudere le review per blocchi omogenei, allegando fonte, data di vigenza e decisione editoriale; cambiare stato solo dopo controllo documentato. | Aperto |
| E02 | Cap. 11, B-PA08 | Promessa formativa non mantenuta | Grave | La struttura obbligatoria promette dieci mini-brani; il capitolo contiene cinque mini-reading. | Aggiungere cinque mini-brani graduati con domanda, soluzione e spiegazione oppure ridurre formalmente la promessa nella fonte canonica con motivazione editoriale. | Aperto |
| E03 | Cap. 17, B-PA11 | Promessa formativa non mantenuta | Grave | Sono promessi dieci casi guidati; il capitolo ne presenta otto. Mancano casi autonomi su conflitto di interessi ed errore procedimentale. | Integrare due casi completi con scenario, qualificazione, soluzione, errore da evitare e verifica; non limitarli a richiami dentro casi diversi. | Aperto |
| E04 | Cap. 24 | Completezza del kit | Grave | La specifica include checklist prima di iniziare lo studio e dopo la pubblicazione della graduatoria; le dieci checklist attuali non le coprono come strumenti autonomi. | Aggiungere due checklist compilabili e raccordarle a Bando Decoder, piano e diario errori. | Aperto |
| E05 | Cap. 8 | Perimetro e anti-duplicazione | Grave | Il capitolo tratta contabilita locale, armonizzazione, universita, economico-patrimoniale e PNRR oltre il livello essenziale escluso dalla specifica del base. | Conservare definizioni e differenze minime; trasferire l'approfondimento ai volumi/moduli pertinenti e sostituirlo con rinvii precisi verificati. | Proposto |
| E06 | Cap. 10 | Perimetro e anti-duplicazione | Grave | Il capitolo supera ampiamente il target e comprende reti, SQL, programmazione, NIS2 e temi ICT avanzati destinati al delta specialistico VOL-08. | Separare B-PA09 essenziale da approfondimenti; mantenere nel base solo le conoscenze ricorrenti e rinviare sezioni avanzate con destinazione puntuale. | Proposto |
| E07 | Cap. 9 | Accuratezza normativa | Grave | Il testo presenta D.Lgs. 36/2023 e correttivo 209/2024 come quadro aggiornato, ma Normattiva segnala ulteriori aggiornamenti pubblicati fino al 23 marzo 2026. | Aggiornare prima la source note consolidata dal testo vigente, quindi riesaminare ogni claim mobile del capitolo e datare la review. | Da verificare |
| E08 | 18 file principali | Superficie di pubblicazione | Grave | Le sezioni `## Note di review` sono contenuto redazionale interno; Book Studio filtra `Note editoriali` ma non questa variante, quindi le note possono comparire nel libro. | Uniformare la heading interna oppure aggiungerla alle heading staff-only; verificare poi l'anteprima completa e l'export. | Aperto |
| E09 | Appendice E | Coerenza struttura-fonte | Grave | La specifica originaria richiede tre formati (quiz ragionato, scritto, orale), mentre indice e file attuale definiscono unicamente lo schema orale. | Deliberare quale promessa e' canonica; se resta solo orale, aggiornare la source note di struttura; altrimenti integrare gli altri due formati senza duplicare i capitoli 14-16. | Aperto |
| E10 | Cap. 23 | Output promesso | Grave | La dashboard personale e' solo prospettata come sviluppo futuro e non esiste come strumento cartaceo completo, nonostante la promessa di autonomia dal digitale. | Inserire un cruscotto cartaceo compilabile con indicatori, prossima azione, data ripasso ed esito del secondo tentativo. | Aperto |
| E11 | Capp. 4-12 e apparato | Apparato normativo/bibliografico | Media | Le fonti sono tracciate nel frontmatter, ma il lettore trova apparati eterogenei: alcuni capitoli hanno `Fonti consolidate`, altri nessuna sezione finale leggibile. | Definire un formato unico di riferimenti finali, distinguendo fonti normative, fonti di metodo e data di aggiornamento. | Proposto |
| E12 | Intero volume | Workflow editoriale | Media | Sono presenti sette valori diversi di `draft_stage`; questo rende ambiguo il passaggio a review, impaginazione e pubblicazione. | Normalizzare gli stati a una macchina editoriale unica e documentare i criteri di transizione. | Proposto |
| E13 | Capp. 19-20 | Uniformita grafica | Lieve | Alcune heading usano iniziale minuscola, per esempio `sanita amministrativa`, mentre le altre famiglie sono trattate come titoli. | Uniformare maiuscole e stile delle heading durante il copy-edit finale. | Aperto |

## 4. Osservazioni per capitolo

### Introduzione - Perche questo libro e' diverso
- Punti di forza: promessa, priorita, capitale riutilizzabile e rapporto cartaceo-digitale sono chiari.
- Criticita: review ancora aperta; manca un apparato finale uniforme di riferimenti.

### Capitolo 1 - Il nuovo candidato pubblico
- Punti di forza: distingue bene candidato principiante e strategico, con mini-test azionabile.
- Criticita: fonti di posizionamento limitate e review editoriale ancora aperta.

### Capitolo 2 - Anatomia del bando
- Punti di forza: tre letture, Bando Decoder, classificazione materie e caso fittizio costruiscono autonomia pratica.
- Criticita: va uniformato l'obiettivo esplicito e chiusa la review sulle regole concorsuali mobili.

### Capitolo 3 - Il Metodo BANDO
- Punti di forza: le cinque lettere sono definite, distinte e applicate a due concorsi.
- Criticita: manca un caso guidato formalmente etichettato e il capitolo resta in stato di draft revisionato.

### Capitolo 4 - Costituzione e ordinamento dello Stato
- Punti di forza: ampia copertura B-PA01, caso, dieci domande e checkpoint.
- Criticita: `review_required: true`; riferimenti normativi solo nel frontmatter.

### Capitolo 5 - Diritto amministrativo operativo
- Punti di forza: copertura B-PA02 molto estesa e distinzioni ad alta resa ben evidenziate.
- Criticita: autotutela, termini e rimedi richiedono controllo normativo datato.

### Capitolo 6 - Pubblico impiego e organizzazione della PA
- Punti di forza: responsabilita e reati PA sono spiegati con confronti, casi e prudenza qualificatoria.
- Criticita: CCNL, PIAO, lavoro agile e disciplina penale impongono review specialistica.

### Capitolo 7 - Trasparenza, anticorruzione e privacy
- Punti di forza: tre accessi, PNA/PIAO/RPCT e ruoli GDPR sono distinti con efficacia.
- Criticita: raccordo con il capitolo 10 da rendere esplicito e datato.

### Capitolo 8 - Contabilita pubblica essenziale
- Punti di forza: fasi contabili, controlli e Corte dei conti sono chiari e applicati.
- Criticita: sconfinamento nel delta locale, universitario, economico-patrimoniale e PNRR; manca checkpoint autonomo.

### Capitolo 9 - Contratti pubblici essenziali
- Punti di forza: ciclo, soggetti, strumenti digitali e distinzioni sono didatticamente solidi.
- Criticita: source note da riallineare al testo vigente 2026 prima della certificazione normativa.

### Capitolo 10 - Informatica, PA digitale e competenze digitali
- Punti di forza: copertura ampia, molte distinzioni operative ed esercizi.
- Criticita: sovradimensionato rispetto a B-PA09; temi avanzati duplicano il perimetro ICT specialistico.

### Capitolo 11 - Inglese concorsuale essenziale
- Punti di forza: grammatica, lessico, email, orale e cloze sono ben organizzati.
- Criticita: cinque mini-reading anziche dieci; serve review linguistica finale.

### Capitolo 12 - Logica, comprensione del testo e ragionamento
- Punti di forza: metodo di classificazione, esercizi e soluzioni ragionate sostengono l'apprendimento.
- Criticita: review metodologica/psicometrica ancora aperta.

### Capitolo 13 - Metodo di studio per concorsi
- Punti di forza: active recall, ripasso distribuito, SQ3R e output sono tradotti in procedure.
- Criticita: le note interne di review restano sulla superficie pubblica.

### Capitolo 14 - La prova a quiz
- Punti di forza: distingue banca dati, rischio, tre giri, distrattori e correzione.
- Criticita: manca una sezione autonoma di errori tipici; note interne visibili.

### Capitolo 15 - La prova scritta e teorico-pratica
- Punti di forza: schema di risposta, tre lunghezze e atto guidato rendono concreto B-PA11.
- Criticita: l'apparato di esempi reali e la review normativa sono ancora aperti.

### Capitolo 16 - La prova orale
- Punti di forza: struttura della risposta, gestione del vuoto e simulazioni sono utili e progressive.
- Criticita: raccordo con Appendice E dichiarato come futuro; note interne visibili.

### Capitolo 17 - Casi pratici e problem solving amministrativo
- Punti di forza: griglia in otto domande e otto casi completi sono efficaci.
- Criticita: la promessa di dieci casi non e' mantenuta; mancano due casi autonomi.

### Capitolo 18 - Quesiti situazionali e soft skills
- Punti di forza: gerarchia di scelta e otto quesiti riducono il ricorso al semplice buon senso.
- Criticita: review metodologica e coerenza con i framework di competenze da chiudere.

### Capitolo 19 - Le famiglie dei concorsi pubblici
- Punti di forza: atlante ampio e coerente con la distinzione core/delta.
- Criticita: esempi e nomenclature dipendono dal catalogo e dai bandi correnti.

### Capitolo 20 - Mappe profilo: cosa resta comune e cosa cambia
- Punti di forza: tredici mappe e griglia semaforo rendono applicabile la tassonomia.
- Criticita: uniformita grafica e review dei bandi rappresentativi ancora aperte.

### Capitolo 21 - Come scegliere i moduli integrativi
- Punti di forza: cinque filtri, matrice decisionale e regola base piu un modulo evitano acquisti dispersivi.
- Criticita: verificare coerenza finale tra esempi, catalogo commerciale e 25 moduli.

### Capitolo 22 - Piano 30/60/90 giorni
- Punti di forza: include anche piano 15 giorni, esempi e calendario compilabile.
- Criticita: note interne visibili e review editoriale ancora aperta.

### Capitolo 23 - Il diario degli errori
- Punti di forza: tassonomia e protocollo in sei passaggi trasformano l'errore in azione.
- Criticita: il cruscotto personale promesso non e' ancora uno strumento cartaceo completo.

### Capitolo 24 - Checklist operative
- Punti di forza: dieci checklist e criteri di stop sono concretamente utilizzabili.
- Criticita: mancano le due checklist autonome indicate in E04.

### Appendice A - Glossario essenziale della PA
- Punti di forza: circa 140 termini, entro il target di 100-150, organizzati per area.
- Criticita: review normativa di tutte le voci ancora aperta.

### Appendice B - Le 100 parole chiave
- Punti di forza: cento voci effettive e funzione distinta dal glossario.
- Criticita: review linguistica e normativa ancora aperta.

### Appendice C - Template Bando Decoder
- Punti di forza: strumento cartaceo completo, esempio e confronto fra bandi.
- Criticita: verificare coerenza con procedure e portali correnti.

### Appendice D - Piano di studio personale
- Punti di forza: dodici pagine operative, tracker e piano di recupero.
- Criticita: review editoriale e test d'uso con candidati non documentati.

### Appendice E - Schema universale di risposta orale
- Punti di forza: formati 30 secondi, 2 minuti e 5 minuti con esempi e griglia.
- Criticita: conflitto con la promessa originaria dei tre formati di prova, E09.

### Appendice F - Matrice materie/profili
- Punti di forza: separa core, modulo, priorita e output con schede compilabili.
- Criticita: non sostituisce la nuova matrice di copertura didattica e necessita riallineamento al catalogo corrente.

## 5. Coerenza globale

- Terminologia: nel complesso coerente; criticita minori nelle heading e una criticita strutturale sull'uso di `Note di review` rispetto a `Note editoriali`.
- Struttura vs indice: introduzione, capitoli 1-24 e appendici A-F coincidono con l'outline canonico. Il Ricettario 25-47 e' correttamente separato e non e' stato usato per chiudere artificialmente i gap del cartaceo.
- Promesse dell'introduzione mantenute: la promessa metodologica e l'autonomia del cartaceo sono in gran parte mantenute; non sono ancora mantenute integralmente le promesse quantitative/operative di E02-E04 ed E10.
- Fonti: la tracciabilita interna e' buona, ma l'apparato per il lettore non e' uniforme e alcune fonti mobili devono essere riconsolidate.
- Anti-duplicazione: i capitoli 8 e 10 invadono il delta specialistico; il problema non e' la mancanza di testo, ma la collocazione editoriale.

## 6. Contenuto da verificare

- D.Lgs. 36/2023: verificare il testo vigente e gli aggiornamenti pubblicati dopo il D.Lgs. 209/2024 nella pagina ufficiale [Normattiva - Codice dei contratti pubblici](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=23G00044&atto.dataPubblicazioneGazzetta=2023-03-31&tipoDettaglio=vigente).
- Reati PA: il richiamo all'abrogazione dell'art. 323 c.p. e' coerente con la [Legge 9 agosto 2024, n. 114 su Normattiva](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=24G00122&atto.dataPubblicazioneGazzetta=2024-08-10&tipoDettaglio=multivigenza); resta da verificare l'intero quadro delle fattispecie e delle successioni normative.
- Anticorruzione: il riferimento al PNA 2025, Delibera n. 19 del 28 gennaio 2026, e' confermato dalla pagina ufficiale [ANAC - Piano Nazionale Anticorruzione 2025](https://www.anticorruzione.it/-/piano-nazionale-anticorruzione-2025); verificare l'impatto operativo su capitolo 7 e appendici.
- PA digitale: aggiornare la source note con il [Piano Triennale AgID 2024-2026, aggiornamento 2026](https://www.agid.gov.it/it/notizie/online-laggiornamento-2026-del-piano-triennale-linformatica-nella-pa) prima di certificare le sezioni mobili del capitolo 10.
- Contabilita pubblica: verificare i documenti di programmazione finanziaria 2025-2026, PNRR e riferimenti settoriali prima di decidere che cosa resta nel base.
- CCNL, PIAO, piattaforme digitali, soglie, termini e procedure: richiedono data di vigenza esplicita e review umana specialistica.

## 7. Suggerimenti facoltativi (non errori)

- Aggiungere all'inizio di ogni parte una pagina di navigazione con obiettivi, prerequisiti e output attesi.
- Inserire un codice visivo stabile per teoria, applicazione, verifica e rinvio specialistico.
- Usare la nuova matrice come cruscotto della dashboard, senza mostrarne le note redazionali nel libro.
- Testare appendici e checklist con un piccolo gruppo di candidati prima della chiusura grafica.

## 8. Priorita degli interventi

1. Chiudere E02, E03, E04, E09 ed E10: sono promesse formative esplicite non mantenute.
2. Riconsolidare le fonti mobili e svolgere review normativa dei blocchi B-PA01/B-PA07, con priorita a E07.
3. Correggere il perimetro anti-duplicazione di capitoli 8 e 10 (E05-E06).
4. Rimuovere dalla superficie pubblica le note interne e uniformare l'apparato fonti (E08, E11).
5. Normalizzare workflow, heading e copy-edit (E12-E13).
6. Rieseguire audit matrice, test, lint editoriale, preview completa e Revisore Editoriale Totale.

## 9. Giudizio di pubblicabilita

**Non pubblicabile allo stato attuale.**

Motivazione: E01 dimostra che il gate didattico e normativo non e' chiuso; E02-E04 ed E09-E10 sono promesse formative non mantenute; E05-E06 violano il perimetro anti-duplicazione; E07 impedisce la certificazione dell'aggiornamento normativo; E08 espone contenuto redazionale interno. L'impianto non richiede una riscrittura totale, ma una revisione sostanziale e tracciata prima di un nuovo giudizio.

## 10. Limiti di questa revisione

- Non e' stato ispezionato un PDF finale impaginato pagina per pagina; il giudizio di layout riguarda Markdown, struttura e comportamento noto di Book Studio.
- La review normativa e' stata campionata sulle aree piu mobili con fonti ufficiali; non sostituisce una verifica giuridica umana articolo per articolo.
- Non sono state applicate riscritture silenziose al manoscritto: il report propone interventi verificabili che l'autore/editore deve approvare.
- Non sono stati valutati i capitoli 25-47 del Ricettario come parte del cartaceo VOL-01.
