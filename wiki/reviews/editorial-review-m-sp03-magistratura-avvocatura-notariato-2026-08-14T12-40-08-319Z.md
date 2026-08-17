---
id: review-editorial-m-sp03-magistratura-avvocatura-notariato-1786711208320
type: review
title: "Revisione editoriale - m-sp03-magistratura-avvocatura-notariato"
status: completed
issue_type: editorial_review
severity: high
affected_pages: []
created_at: 2026-08-14T12:40:08.319Z
updated_at: 2026-08-14T12:40:08.319Z
review_required: false
canonical: true
tags: [revisione-editoriale, pubblicabilita]
---

# Report editoriale — M-SP03 - Magistratura, Avvocatura e Notariato

## 1. Sintesi editoriale
- Genere editoriale: modulo specialistico/manuale-workbook per concorsi e selezioni giuridiche ad alta barriera.
- Pubblico target: laureati in giurisprudenza che valutano o preparano magistratura ordinaria, Avvocatura dello Stato o notariato.
- Perimetro di questa revisione: intero libro/modulo, inclusi index, 7 capitoli, piano editoriale, matrice e source note.
- Stato generale in una frase: il modulo ha buona prudenza normativa e corretta separazione dei binari, ma non è ancora pubblicabile per lacune di copertura, casi troppo generici e forte ripetizione editoriale.

## 2. Punti applicati della checklist
Applicati i punti 1-26 e 28-30 della checklist. Il punto 27, impaginazione, è stato applicato solo in modo indiretto sul Markdown: non era disponibile un PDF impaginato per verificare realmente H1 Arial Bold 18-20 pt, H2 14 pt, H3 12 pt, corpo Garamond 11 pt, interlinea 1,15-1,20 e resa di tabelle/box in Arial 9,5-10 pt.

Applicato anche il gate aggiuntivo di copertura didattica integrale e la regola di copertura ConcorsoBook: famiglia corretta `Carriere Speciali`; nessuna duplicazione pesante del B-PA rilevata; mancano però dichiarazione esplicita del limite dei rinvii a VOL-01, pacchetto minimo ed esclusioni.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Cap. 1, N-SP03-02-03 | Completezza spiegazioni / Gate copertura | grave | La matrice promette il confronto sull’incompatibilità di calendario 2026 tra notariato 17-19 giugno e magistratura 24-26 giugno, stessa sede; nel capitolo il nucleo tratta età e finestre, ma non chiude questo fatto strategico. | Inserire un box o sottosezione “Quando due binari si sovrappongono” con date, sede, carico di 3+3 prove da otto ore e criterio decisionale. | aperto |
| E02 | Cap. 1, N-SP03-06-01 | Coerenza globale / Architettura volumi | grave | Il piano promette “limite dei rinvii al VOL-01”; il capitolo sviluppa il Bando Decoder ma non esplicita cosa resta nel base, cosa è specialistico, pacchetto minimo, esclusioni e assenza di appendici/verticali necessari. | Aggiungere tabella: `VOL-01 copre`, `M-SP03 aggiunge`, `non serve acquistare`, `rinvio cross-family`, `pacchetto consigliato`. | aperto |
| E03 | Capp. 2-7, sezioni “Caso ragionato” | Esempi / Stile didattico | grave | Molti “casi ragionati” non sono casi: sono istruzioni generiche ripetute senza fatti, consegna, soluzione attesa e commento. Questo indebolisce l’autonomia didattica. | Sostituire almeno un caso per capitolo con scenario completo, dati, domanda, svolgimento guidato, errore atteso e soluzione commentata. | aperto |
| E04 | Capp. 5-7 | Ripetizioni / Qualità editoriale complessiva | grave | Interi paragrafi metodologici ricorrono quasi invariati in nuclei diversi, soprattutto nei capitoli 5, 6 e 7. La quantità c’è, ma parte della copertura è riempita da riuso meccanico. | Riscrivere ogni nucleo con funzione specifica: tema teorico, teorico-pratico, atto, pianificazione, errore, checklist. Conservare solo una cornice comune breve. | aperto |
| E05 | Cap. 7, N-SP03-15-02 | Note, box, schemi / Completezza | grave | La “Checklist finale di prontezza” è descritta, ma manca una checklist compilabile effettiva. Per un manuale-workbook questo è un output promesso non consegnato. | Inserire checklist tabellare per binario con campi: requisito, fonte, prova, logistica, simulazioni, correzioni, stato verde/giallo/rosso, firma/data. | aperto |
| E06 | Matrice copertura didattica | Coerenza tra apparato e testo | media | La matrice conserva ancora blocchi storici “0% / non pubblicabile / 23 mancanti” e poi dichiara “35 completi”. La compresenza può confondere gate e revisori. | Separare storico e stato corrente, lasciando una sola tabella finale di copertura valida per il gate. | proposto |
| E07 | Tutti i capitoli | Stile didattico / Verifiche | media | Ogni capitolo ha 5 blocchi di verifica brevi da 2-3 domande; non rispetta pienamente il formato canonico di verifica consolidata con almeno 6 quiz commentati ogni 5-7 nuclei. | Raggruppare a fine capitolo un blocco `▣ Verifica` con almeno 6 domande commentate e mantenere mini-domande solo se utili. | proposto |
| E08 | Cap. 3, N-SP03-08-01 | Errore normativo/contenutistico da verificare | media | La soglia degli scritti dell’Avvocatura è attribuita a “fonte secondaria consolidata”, non all’atto ufficiale. In un modulo giuridico pre-pubblicazione va evitata. | Verificare sull’articolato ufficiale o spostare in “da verificare”, senza presentarla come regola certa. | da verificare |
| E09 | Cap. 6 | Completezza spiegazioni / Strumenti | media | Il capitolo parla di roadmap, calendario minimo, recupero e delta di tornata, ma non consegna modelli compilabili. | Aggiungere 2-3 template: roadmap trimestrale, settimana minima, registro campi mobili. | proposto |
| E10 | Tutti i capitoli | Layout / Uniformità grafica | media | Il sistema canonico di box è poco usato: mancano box ricorrenti come `Da sapere in 5 righe`, `Domanda-trappola`, `Mini-esercizio`, `Checklist operativa`, `Fonti consolidate`. | Uniformare i box per capitolo, con nomi stabili e resa coerente nel renderer KDP. | proposto |
| E11 | Index + capitoli | Apparato / Stato editoriale | media | `index.md` è ancora `status: scaffold`, mentre i capitoli sono `status: draft`, `canonical: false`, `pilot-draft`. Non è coerente con una richiesta di pubblicabilità. | Aggiornare frontmatter dopo revisione: stato unico, review_required motivato, canonical solo quando approvato. | proposto |
| E12 | Capp. 5-7 | Sintassi / Chiarezza | lieve | Alcune formule ricorrono con ritmo artificiale: “il candidato ricostruisce…”, “non diagnostica…”, “dato ignoto…”. Il registro resta corretto ma diventa meccanico. | Alleggerire le ripetizioni e sostituire con esempi concreti o istruzioni operative più brevi. | proposto |
| E13 | Tutti i capitoli | Uniformità grafica | lieve | “Caso ragionato” è talvolta H3, talvolta solo grassetto; i blocchi `Verifica` sono formalmente ripetuti ma non sempre gerarchicamente omogenei. | Uniformare heading: `### Caso ragionato` e `### ▣ Verifica`, oppure schema unico a fine nucleo/capitolo. | proposto |

## 4. Osservazioni per capitolo
### Capitolo 1 — Mappa delle tre professioni e scelta del binario
- Punti di forza: separa bene magistratura, Avvocatura e notariato; corretta avvertenza sul notariato; buona logica “stabile/mobile/ignoto”.
- Criticità: mancano confronto calendario 2026, rinvio esplicito a VOL-01 e pacchetto minimo; il Bando Decoder è utile ma non abbastanza compilabile.

### Capitolo 2 — Magistratura ordinaria
- Punti di forza: accesso diretto del laureato trattato con prudenza; buona distinzione tra facoltà informatica e modalità di tornata.
- Criticità: casi troppo generici; verifiche brevi; serve un esempio completo di fascicolo requisiti o tema corretto.

### Capitolo 3 — Avvocatura dello Stato
- Punti di forza: ottima centralità del limite anagrafico e della funzione istituzionale; buona separazione da magistratura.
- Criticità: soglie valutative da ricondurre a fonte ufficiale; casi e controtesi restano più prescritti che mostrati.

### Capitolo 4 — Notariato
- Punti di forza: pratica notarile spiegata correttamente; chiara distinzione tra requisito, dichiarazione e certificato; buona prudenza sui testi.
- Criticità: manca una mini-linea temporale compilabile; i casi su atti e volontà delle parti vanno resi concreti.

### Capitolo 5 — Metodo per tema, atto e prova teorico-pratica
- Punti di forza: distinzione corretta tra tema teorico, teorico-pratico e atto.
- Criticità: è il capitolo più esposto al riuso meccanico; ogni nucleo ripete la stessa architettura invece di mostrare una prestazione diversa.

### Capitolo 6 — Piano pluriennale
- Punti di forza: rifiuta correttamente calendari inventati e promesse 30/60/90 giorni.
- Criticità: troppe frasi ripetute; mancano template reali di roadmap, settimana minima e registro delle incognite.

### Capitolo 7 — Errori tipici, casi integrati e checklist finale
- Punti di forza: impianto coerente con l’idea di correggere prodotti, non persone.
- Criticità: i cinque nuclei sono troppo simili; la checklist finale non è una checklist effettiva; il capitolo deve diventare più workbook.

## 5. Coerenza globale
- Terminologia: generalmente coerente (`binario`, `tornata`, `dato mobile`, `ignoto`, `fascicolo`, `output`). Il problema è l’eccesso di ripetizione, non l’incoerenza.
- Struttura vs indice: i 7 capitoli corrispondono all’indice reale; resta incoerenza con parti del piano/matrice che conservano lo storico a 9 sezioni e vecchi stati.
- Promesse dell’introduzione mantenute: parzialmente. Sono mantenute la separazione dei binari e la prudenza normativa; non sono pienamente mantenuti la copertura del calendario strategico, il limite dei rinvii a VOL-01, i casi guidati e la checklist finale.

## 6. Contenuto da verificare
- Soglia valutativa dell’Avvocatura dello Stato: il capitolo la presenta da fonte secondaria; va verificata sul bando ufficiale o marcata come incerta.
- Aggiornamento normativo finale su art. 2 d.lgs. 160/2006, art. 5 L. 89/1913, r.d. 1611/1933 e L. 1035/1966 prima del text freeze.
- Verifica web a campione eseguita il 14 agosto 2026: il Ministero conferma il concorso magistratura a 450 posti e il diario prove scritte 2026; il Ministero conferma la scheda del concorso notarile a 400 posti; la Gazzetta Ufficiale conferma il concorso Avvocatura a 7 posti; la Gazzetta conferma la L. 89/1913, ma il testo vigente dell’art. 5 va comunque ricontrollato su Normattiva prima della stampa. Fonti: Ministero Giustizia magistratura 450 posti ([giustizia.it](https://www.giustizia.it/giustizia/en/mg_1_8_1.page?contentId=SDC1476541&utm_source=openai)), diario prove magistratura ([giustizia.it](https://www.giustizia.it/giustizia/en/mg_1_8_1.page?contentId=SDC1495383&utm_source=openai)), notariato 400 posti ([giustizia.it](https://www.giustizia.it/giustizia/en/mg_1_6_1.page?contentId=SCE1485302&utm_source=openai)), G.U. Avvocatura ([gazzettaufficiale.it](https://www.gazzettaufficiale.it/eli/id/2025/06/13/25E03460/S4)), L. 89/1913 ([gazzettaufficiale.it](https://www.gazzettaufficiale.it/eli/id/1913/03/07/013U0089/sg)).

## 7. Suggerimenti facoltativi (non errori)
- Valutare un’apertura più incisiva con una tabella comparativa `Magistratura / Avvocatura / Notariato` già nel capitolo 1.
- Spostare alcune cautele ripetute su dati mobili in box ricorrenti, così il corpo resta più leggibile.
- Usare un solo lessico per il lettore: “scheda”, “fascicolo”, “decoder” e “registro” sono tutti utili, ma vanno distinti graficamente.

## 8. Priorità degli interventi
1. Correggere E01, E02, E03, E04, E05: sono i blocker di copertura e struttura.
2. Verificare E08 su fonte ufficiale.
3. Ripulire matrice/frontmatter: E06, E11.
4. Ristrutturare verifiche, box e template workbook: E07, E09, E10.
5. Rifinire stile e uniformità: E12, E13.

## 9. Giudizio di pubblicabilità
Non pubblicabile allo stato attuale

Motivazione: gli errori gravi E01-E05 riguardano promesse formative non mantenute, casi non realmente sviluppati, checklist finale assente e ripetizione strutturale diffusa. Il modulo ha base solida, ma richiede revisione sostanziale prima del nuovo giro di editing.

## 10. Limiti di questa revisione
Non ho verificato un PDF impaginato, quindi il controllo tipografico Arial/Garamond e la resa KDP restano da fare sul renderer. La verifica normativa esterna è stata a campione su fonti ufficiali raggiungibili; prima della pubblicazione serve audit completo delle norme vigenti e degli avvisi successivi al cut-off del 13 agosto 2026.