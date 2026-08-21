# VOL-04 — Revisione applicativa e chiusura pre-pubblicazione

## Stato e decisione approvata

Il report `wiki/reviews/pipeline/VOL-04/21-vol-04.md` ha classificato il volume come non pubblicabile allo stato attuale e ha definito una roadmap P0-P3. L'utente ha approvato esplicitamente l'applicazione dei punti elencati il 18 agosto 2026.

La scelta editoriale è conservativa sul valore e radicale sugli errori: mantenere i quattordici capitoli e la promessa specialistica, correggere i contenuti non vigenti, produrre le appendici e gli strumenti annunciati, separare il manoscritto dalle note di lavorazione e completare i controlli finali. Non si riduce l'indice per evitare il lavoro promesso.

## Approcci valutati

### Approccio A — Completamento integrale per fasi, scelto

Corregge prima i blocker normativi, poi il contratto del lettore, quindi copertura didattica, apparati, proofreading e preflight. Conserva il Metodo BANDO e crea davvero appendici e strumenti finali.

Vantaggi: mantiene la proposta commerciale, produce un libro autonomo e consente al gate di verificare rilievi realmente chiusi. Svantaggi: richiede interventi coordinati su tutti i capitoli e più cicli di audit.

### Approccio B — Riduzione della promessa

Eliminerebbe dall'indice appendici, strumenti e parti procedurali non complete, rinominando i capitoli 6, 7 e 11 come semplici mappe introduttive.

Vantaggi: tempi brevi. Svantaggi: riduce sensibilmente valore e differenziazione del volume. Non è coerente con l'ordine dell'utente di procedere con tutti i punti.

### Approccio C — Riscrittura totale in formato 2

Ricostruirebbe tutti i capitoli con nuclei da almeno 600 parole e nuovo apparato di verifica.

Vantaggi: massima uniformità col formato più recente. Svantaggi: distrugge o duplica lavoro valido, amplia il rischio normativo e non è richiesto dal gate del volume. È contrario alla regola di preservare il lavoro precedente.

## Perimetro

Sono inclusi:

- front matter, indici e wrapper commerciali del VOL-04;
- quattordici capitoli di M-FC04;
- cinque appendici, cinque strumenti finali e conclusione;
- fonte consolidata per le rettifiche normative del 2026;
- matrice di copertura, report dello step 21 e stato gestito dal CLI;
- export PDF KDP e artefatto digitale se supportati dagli strumenti esistenti;
- audit, proofreading, controllo dei link e seconda verifica “zero errori”.

Non sono inclusi:

- modifiche ai volumi diversi da VOL-04;
- correzione dell'incompatibilità ESM/CJS generale della suite su Node 22;
- creazione di servizi digitali esterni o di URL non esistenti;
- attribuzione di approvazioni umane prima dello step 24.

## Architettura editoriale

### 1. Livello delle fonti

Le rettifiche ad alta mobilità confluiscono in una source note 2026 collegata ai capitoli interessati. La nota registra fonte ufficiale, data, portata e conseguenza editoriale per:

- decadenza del D.L. 12 giugno 2026, n. 100;
- attuale articolazione del Ministero e ruolo del DIT;
- abolizione della formula esecutiva;
- trattamento dei dati giudiziari nei rapporti di lavoro;
- decorrenze del D.M. 26 giugno 2026, n. 114 e stato del certificato nazionale dei carichi pendenti.

### 2. Livello reader-facing

Ogni capitolo conserva frontmatter e tracciabilità interna, ma il corpo visibile inizia direttamente dal titolo e dal testo editoriale. Vengono rimossi dal corpo:

- `Specifica struttura madre`;
- `Scheda di lavoro`;
- doppi `Riferimenti consolidati` espressi come wikilink;
- `Note di review`;
- riferimenti al corpus, alle source notes o alla lavorazione interna.

I riferimenti necessari diventano leggibili: denominazione dell'atto, articolo pertinente quando utile, ente e data. I wikilink restano nel frontmatter e negli artefatti interni, non nel testo destinato allo studente.

### 3. Livello didattico

I quattordici capitoli restano legacy, senza promozione artificiale a `format_version: 2`. Ognuno riceve una verifica finale con almeno sei quiz commentati complessivi e un caso ragionato. Il capitolo 1 riceve il caso applicativo mancante. I capitoli 6, 7 e 11 vengono ampliati nei punti necessari a sostenere il termine “operativo”, senza trasformarsi in trattati processuali.

### 4. Apparati finali

Un capitolo autonomo raccoglie le appendici A-E e i cinque strumenti finali in forma stampabile. Un secondo file contiene la conclusione. La posizione nel modulo segue il pattern già usato dagli altri volumi specialistici:

- `15-appendici-strumenti-finali.md`;
- `16-conclusione-vol-04.md`.

Il volume resta autosufficiente anche senza servizi web. La pagina dei servizi digitali non promette QR o link finché non esiste una destinazione verificata.

### 5. Produzione e preflight

Il PDF usa il renderer condiviso KDP 6,69 × 9,61 pollici. L'export deve includere front matter, quattordici capitoli, appendici e conclusione. Il preflight verifica gerarchia, tabelle, font, margini, sommario, link e assenza di pagine o titoli orfani nei limiti degli strumenti disponibili.

## Norme editoriali

- Voce: professionale, diretta, orientata al candidato, non promozionale.
- Terminologia: “Ministero della giustizia”, “Ufficio per il processo” alla prima occorrenza, poi UPP; AUPP per l'addetto.
- Accenti: forme Unicode corrette; nessun `e'`, `puo'`, `piu`, `attivita` nel corpo.
- Fonti: primarie e ufficiali per norme, organizzazione, servizi e giurisprudenza.
- Prudenza: distinguere disciplina vigente, prassi locale ed esempio didattico.
- Autonomia: nessuna dipendenza del lettore da wiki, dashboard o report.
- Humanizer: variare ritmo e aperture senza eliminare la struttura workbook.

## Criteri di accettazione

1. Zero occorrenze che descrivono il D.L. 100/2026 come fonte vigente o ancora in conversione.
2. Zero descrizioni della formula esecutiva come requisito vigente.
3. Mappa ministeriale coerente con DAG, DOG, DIT, DAP e DGMC.
4. Appendici A-E, cinque strumenti e conclusione esistenti e indicizzati.
5. Zero sezioni redazionali e zero wikilink interni nel corpo dei sedici file reader-facing.
6. Almeno sei quiz commentati e un caso ragionato per ciascuno dei quattordici capitoli.
7. Capitoli 6, 7 e 11 con sequenze operative, competenze, termini o controlli sufficienti al titolo.
8. Zero forme ASCII note per accenti e apostrofi nel corpus.
9. Matrice aggiornata con evidenze reali; nessuna riga dichiarata completa senza verifica.
10. Registro errori aggiornato solo dopo riscontro delle correzioni.
11. Export PDF prodotto e sottoposto a preflight; formato digitale prodotto se il repository dispone di un comando stabile.
12. Gate e audit eseguiti senza forzature; ogni limite residuo resta dichiarato.

## Verifica e gestione dei rischi

La suite completa parte da una baseline di 504 test superati e 14 falliti. Tredici fallimenti dipendono dall'esecuzione Node 22 degli script ESM/CJS; uno è un timeout VOL-02. Questi errori non verranno corretti nel lavoro VOL-04. Le verifiche useranno test mirati, audit tramite `tsx`, `git diff --check`, scansioni del corpus, CLI del pipeline e preflight degli artefatti.

Il lavoro avviene nella branch `agent/sync-volumi-04-05-06-09-20260817`, in-place per rispettare il workspace condiviso indicato dall'utente. Le modifiche non correlate già presenti saranno preservate.
