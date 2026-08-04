# VOL-07 Step 19 KDP Book Studio Design

## Contesto e decisione

Lo step 19 della pipeline VOL-07 applica il master editoriale KDP al volume composito nel Book Studio. La scelta approvata esclude la generazione anticipata di un PDF: il risultato dello step è una preview completa, coerente e interamente renderizzata nel formato paperback 6,69 × 9,61 pollici. Lo step 20 resta proprietario dell'audit visivo pagina per pagina.

La direzione visuale è già fissata da `Precisione Vitale` e dal design system ConcorsoBook OS. Non viene riaperta la scelta estetica e non si modificano i venticinque capitoli congelati. L'intervento riguarda il builder del volume, il paginator, la resa del master condiviso, gli strumenti di verifica e il report di evidenza dello step 19.

## Obiettivi

- Renderizzare VOL-07 come libro unico con sei sezioni di front matter generate, quattro aperture di modulo e venticinque capitoli.
- Applicare pagina KDP 6,69 × 9,61 pollici, bianco e nero, senza bleed, colonna singola, Arial/Garamond e numerazione continua.
- Portare il gutter interno a 23 mm, come prescritto dal master canonico, mantenendo margini speculari recto/verso.
- Integrare nell'indice del volume i nuclei dotati di `Nucleo ID`, con numerazione decimale coerente con il numero del capitolo nel volume composito.
- Riconciliare i numeri dell'indice con le pagine effettivamente prodotte dalla paginazione misurata del Book Studio.
- Rendere i blocchi `▣ Verifica` riconoscibili in bianco e nero e impedire la separazione ambigua del titolo dal primo contenuto.
- Dimostrare che il volume è interamente renderizzato e privo di overflow strutturali prima di chiudere lo step 19.

## Non-obiettivi

- Non produrre un PDF in `output/pdf/` durante lo step 19.
- Non svolgere l'audit manuale dettagliato di ogni pagina, riservato allo step 20.
- Non riscrivere, ridurre o eliminare testo, tabelle, quiz o immagini per ottenere il riflusso.
- Non modificare i file dei capitoli, le matrici, gli indici di modulo o i manifest di text freeze.
- Non materializzare su disco il front matter già generato dal Book Studio.
- Non introdurre eccezioni hard-coded esclusivamente per VOL-07 quando una regola appartiene al renderer condiviso.

## Architettura

Il server continua ad assemblare il volume composito a partire dal catalogo e dai quattro moduli. `buildVolumeBookStudioData()` rimane il confine che produce front matter, aperture di modulo, capitoli e asset. `buildVolumeIndexBlocks()` viene esteso affinché emetta, oltre a parti e capitoli, una riga `index-row` per ogni heading di nucleo che possiede un numero decimale derivato dal `Nucleo ID`.

`MarkdownBlock` conserva il `nucleusId` tecnico quando il parser riconosce un heading conforme. Nel modulo standalone `N-SA02-05-04` continua a mostrarsi come `5.4`; nel volume composito il capitolo locale 05 è il capitolo globale 9, quindi lo stesso nucleo si mostra come `9.4`. Il progressivo finale deriva sempre dal `Nucleo ID`, mentre il prefisso usa il numero di capitolo assegnato al volume. L'ID sorgente non cambia e resta la chiave di matrice e gate.

Ogni voce di capitolo conserva il `path` del capitolo. Ogni voce di nucleo conserva lo stesso `path`, il `nucleusId` invariato e il numero decimale destinato al lettore; la coppia `path + nucleusId` è la chiave stabile con cui il client riconosce il nucleo senza esporre l'ID tecnico. Il server assegna numeri di pagina iniziali stimati per garantire una risposta completa anche prima della misurazione del DOM.

Il paginator del Book Studio resta proprietario della paginazione effettiva. Dopo `paginateMeasuredChapters()`, una funzione pura costruisce due mappe: pagina iniziale per `chapter.path` e pagina del primo heading per `chapter.path + block.nucleusId`. Una seconda funzione applica queste mappe alle voci `index-chapter` e `index-row` del front matter. La colonna dei numeri pagina mantiene larghezza fissa, così l'aggiornamento dei valori non cambia il riflusso dell'indice; è ammessa una sola riconciliazione deterministica, senza cicli di ripaginazione.

## Componenti e responsabilità

### Builder del volume

File principale: `src/server/book/book-preview.ts`.

- Riutilizza i venticinque capitoli già caricati dai quattro moduli.
- Genera le sei sezioni comuni: servizi digitali, frontespizio, copyright, sommario, premessa e indice completo.
- Genera una sola apertura per ciascuno dei quattro moduli.
- Inserisce nell'indice solo heading dotati di `nucleusId`; i capitoli legacy restano correttamente a livello capitolo.
- Non usa heading generici o apparati ricorrenti per inventare numeri di nucleo.
- Mantiene `path` e `nucleusId` come identità delle righe indicizzate e calcola separatamente il numero visibile del volume.

### Paginatore e riconciliazione

File principale: `app/components/book-studio-panel.tsx`.

- Misura il layout con le dimensioni fisiche della pagina KDP.
- Assegna numerazione continua a front matter, aperture di modulo e capitoli.
- Calcola la pagina reale di ogni capitolo e di ogni heading numerato.
- Aggiorna le voci dell'indice senza mutare il contenuto sorgente dei capitoli.
- Conserva il comportamento di fallback basato sui costi stimati se il DOM di misura non è disponibile.
- Mantiene un titolo con il blocco successivo e non forza un contenuto oltre il margine inferiore.

### Master visuale condiviso

File principale: `app/globals.css`.

- Pagina: 6,69 × 9,61 pollici, senza bleed.
- Corpo: Garamond 11 pt, interlinea 1,18, testo giustificato.
- H1/H2/H3: Arial Bold 20/14/12 pt.
- Tabelle, quiz, box e strumenti: Arial 9,5-10 pt.
- Gutter interno: 23 mm; margine esterno: 13 mm; margini alto e basso: 18 mm.
- Pagine verso con margini speculari.
- Tabelle a layout fisso e celle rifluibili; griglie verbose già suddivise dal parser, mai compresse oltre la scala canonica.

Il titolo `▣ Verifica` riceve una classe semantica nel renderer. La resa usa bordo scuro, fondo neutro chiaro, Arial Bold e contrasto verificabile in scala di grigi. Il paginator mantiene il titolo con il primo elemento successivo; liste, tabelle e callout conservano le regole `break-inside: avoid` già previste.

### Verifica automatica del Book Studio

Lo script `scripts/verify-book-studio-layout.mjs` viene reso parametrico tramite identificativi di libro e prefisso di output, preservando i casi predefiniti esistenti. Per lo step 19 viene eseguito sul `bookId` canonico `volumi/vol-07`.

Il report automatico registra:

- numero complessivo di pagine renderizzate;
- sei sezioni di front matter;
- quattro aperture di modulo;
- venticinque capitoli;
- numero di voci capitolo e righe di nucleo nell'indice;
- numerazione progressiva senza duplicati o salti;
- tipografia campionata per H1, H2, H3, corpo, tabella e callout;
- margini recto/verso;
- overflow e sovrapposizioni strutturali;
- presenza e resa dei blocchi `▣ Verifica`.

Gli artefatti diagnostici restano in `artifacts/` e non sono il prodotto editoriale finale. Lo step produce inoltre `wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md`, con esito, conteggi, comando di verifica, anomalie corrette e limiti rinviati allo step 20.

## Flusso dati

1. Il catalogo risolve VOL-07 e i quattro `bookId` di modulo.
2. Il server carica esclusivamente i capitoli pubblicabili e scarta documenti staff-only.
3. Il builder rinumera i capitoli da 1 a 25 nel volume composito senza alterare gli `outline_section` dei moduli.
4. Il front matter e le aperture di modulo vengono generati in memoria.
5. L'indice riceve parti, capitoli e nuclei numerati; i sette nuclei attuali di M-SA02/05 diventano `9.1–9.7` nel volume composito.
6. Il client esegue la paginazione misurata nell'ordine editoriale completo.
7. Le mappe di pagina riconciliano capitoli e nuclei nell'indice.
8. Il renderer applica master KDP, margini speculari e stili di verifica.
9. Lo script Playwright attraversa l'intero volume e produce il report diagnostico.
10. Il report Markdown dello step 19 conserva l'evidenza necessaria alla chiusura tramite CLI.

## Gestione degli errori

La chiusura dello step 19 è bloccata se si verifica una delle condizioni seguenti:

- uno dei quattro moduli non viene caricato;
- il volume non espone esattamente venticinque capitoli;
- una sezione di front matter o un'apertura di modulo manca;
- un heading con `nucleusId` non compare nell'indice o riceve un prefisso di capitolo incoerente con il volume;
- una voce dell'indice non può essere associata a una pagina renderizzata;
- la numerazione presenta duplicati, regressioni o salti non motivati;
- una pagina non viene renderizzata, eccede i margini o collide con il footer;
- font, dimensioni, formato pagina o gutter non rispettano il master;
- un titolo resta orfano o un blocco `▣ Verifica` perde il proprio primo contenuto sulla pagina successiva;
- il test o lo script Playwright termina con codice diverso da zero.

Timeout del browser, font non caricati o asset non decodificati sono errori tecnici, non esiti editoriali positivi. Il CLI non viene chiuso finché la verifica non termina regolarmente.

## Strategia di test

### Test server

`tests/book-preview.test.ts` viene esteso con un volume composito di fixture che contiene almeno un capitolo formato 2. Il test verifica:

- parti e capitoli nell'ordine atteso;
- presenza della riga di nucleo con numero decimale globale e `nucleusId` tecnico invariato;
- assenza di righe per heading generici o H3 non numerati;
- path e numero stabili sulle voci dell'indice;
- fallback di pagina valorizzato.

### Test paginator

La riconciliazione viene isolata in funzioni pure verificabili con una sequenza sintetica di pagine. I test coprono:

- pagina iniziale del capitolo;
- nucleo nella prima pagina e in una pagina successiva;
- trasformazione dello stesso `nucleusId` da numero locale nel modulo a numero globale nel volume;
- distinzione stabile delle righe tramite `path + nucleusId`;
- voce mancante lasciata esplicitamente non risolta e segnalata dalla verifica;
- nessuna modifica a blocchi diversi dall'indice.

### Test master

I test tipografici e di layout confermano dimensioni pagina, Garamond/Arial, gutter 23 mm, margini speculari, regole di stampa, titolo non orfano e stile in bianco e nero per `▣ Verifica`.

### Verifica integrata

La suite completa deve restare verde. Lo script Playwright carica VOL-07 in modalità Libro, attende font e immagini, misura ogni pagina e fallisce per overflow, collisioni, conteggi errati o indice incompleto. La verifica dettagliata di spazi bianchi, vedove, orfani e qualità pagina per pagina viene eseguita nello step 20, non dichiarata implicitamente nello step 19.

## Criteri di accettazione

- Stato iniziale: `19:VOL-07` in-progress e nessun blocked.
- Sei sezioni di front matter generate e quattro aperture di modulo.
- Venticinque capitoli presenti, nell'ordine M-SA01, M-SA02, M-SA03, M-SA04.
- Tutti e soli i sette heading attuali dotati di `Nucleo ID` compaiono nell'indice; `N-SA02-05-01`–`07` si mostrano come `9.1–9.7` nel volume e restano `5.1–5.7` nel modulo standalone.
- Numeri pagina dell'indice riconciliati con la paginazione misurata.
- Master KDP conforme a formato, font, scala, colonna, gutter, recto/verso e numerazione.
- Blocchi `▣ Verifica` distinguibili e non separati ambiguamente dal primo contenuto.
- Zero overflow strutturali, collisioni con footer o pagine non renderizzate.
- Test mirati e suite completa verdi.
- Report `19-vol-07-impaginazione-kdp.md` completo e senza placeholder.
- Chiusura del CLI eseguita senza `--accept` se il comando restituisce `passed: true`; accettazione manuale ammessa solo dopo un esplicito `gate-not-implemented` e verifica documentata.

## Handoff allo step 20

Lo step 19 consegna un volume interamente impaginato nel Book Studio, non ancora dichiarato perfetto pagina per pagina. Lo step 20 riceve il conteggio finale, il report di layout e gli artefatti diagnostici; controlla ogni pagina dalla prima all'ultima e registra problemi puntuali di vedove, orfani, spazi bianchi, tabelle, box, immagini, margini e coerenza recto/verso.
