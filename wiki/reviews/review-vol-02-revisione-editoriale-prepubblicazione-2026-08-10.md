---
id: review-vol-02-revisione-editoriale-prepubblicazione-2026-08-10
type: review
title: "VOL-02 - Revisione editoriale professionale pre-pubblicazione"
status: completed
domain: "concorsi pubblici italiani"
topics: ["revisione editoriale", "due diligence", "pubblicabilità", "vol-02", "enti locali", "polizia locale", "camere di commercio"]
entities: ["VOL-02", "M-FL01", "M-FL02", "M-FL03", "M-FL04", "Metodo BANDO", "Capitale Personale"]
source_refs: ["sources/legge-65-1986-polizia-locale.md", "sources/codice-strada-d-lgs-285-1992-dpr-495-1992.md", "sources/d-lgs-18-agosto-2000-n-267-enti-locali.md"]
book_refs: ["vol-02-enti-locali-polizia-locale", "m-fl01-comuni-unioni", "m-fl02-regioni-province-citta-metropolitane", "m-fl03-camere-commercio", "m-fl04-polizia-locale"]
confidence: 0.95
updated_at: "2026-08-10T00:00:00+02:00"
created_at: "2026-08-10T00:00:00+02:00"
review_required: true
canonical: true
issue_type: full_editorial_due_diligence
severity: critical
affected_pages: ["intero volume", "front matter generato", "46 capitoli", "impaginazione tabellare"]
tags: ["revisione-editoriale-totale", "vol-02", "pre-pubblicazione", "due-diligence"]
---

# Report editoriale finale — VOL-02

**Oggetto della revisione:** `delivery/VOL-02/candidate/vol-02-interior-kdp.pdf`
(830 pagine, 6,69 × 9,61 pollici, b/n, no bleed), versione `VOL-02-candidate-2026.08.09.1`,
commit sorgente `8662a13`.

**Metodo.** La revisione è stata condotta sull'artefatto realmente pubblicabile — il PDF —
e in parallelo sui 46 capitoli sorgente in `wiki/books/moduli/m-fl0{1,2,3,4}/chapters/`
e sul codice che genera le prime pagine (`src/server/book/book-preview.ts`,
`src/catalog/text-volumes.ts`). Ogni criticità riportata è stata verificata sul PDF
stampato, con indicazione della pagina. Le quattro fasi previste per i manoscritti lunghi
(analisi globale, revisione capitolo per capitolo, controllo incrociato, report) sono state
completate prima di formulare il giudizio.

**Nota metodologica importante.** Una parte rilevante delle criticità non nasce dalla
scrittura, che è di buon livello, ma dalla **catena di composizione**: il volume stampato
non coincide con il volume progettato. Questo va detto con chiarezza perché cambia
la natura degli interventi richiesti: molti sono correzioni di *build*, non di testo.

---

## 1. Executive summary

VOL-02 è un manoscritto **scritto bene e prodotto male**.

La prosa è la parte migliore dell'opera. È asciutta, orientata al problema, non
accademica, con una voce autoriale riconoscibile e una disciplina rara: quasi mai
divaga, quasi mai gonfia. Il controllo meccanico conferma il dato: **zero parole doppie**
in 256.000 parole, **una sola** riga con spaziatura difettosa, **sei sole** frasi identiche
ripetute in più di due capitoli (e sono intestazioni di apparato), **nessuna nota di
review o segnaposto** rimasta nei capitoli. Su questi indicatori il corpus è più pulito
di molti manuali pubblicati da editori strutturati.

Il problema è che questo testo è stato riversato in un libro che, così com'è, non può
andare in stampa. **816 pagine su 830 riportano nel piè di pagina il titolo di un altro
volume** — «Il Metodo BANDO», cioè VOL-01. Circa **448 pagine su 830 (54%)** contengono
tabelle spezzate in frammenti con l'intestazione ristampata due, tre o quattro volte
nella stessa pagina. Il libro **non ha una fine**: si interrompe a pagina 830 nel mezzo
del blocco di verifica del capitolo 46, su una riga che dice «Risposta corretta: B».
La simulazione finale e le otto appendici operative annunciate nell'indice redazionale
non esistono nel volume stampato. I quattro capitoli di orientamento già scritti —
compreso «Come usare VOL-02 insieme a VOL-01», che è la porta d'ingresso logica
dell'opera — non sono stati inclusi nella compilazione.

A questo si aggiunge un difetto didattico che, in un manuale da concorso, pesa quanto
un errore normativo: **nel 95% dei 232 quiz la risposta corretta è l'opzione più lunga**,
e la lettera corretta è B in 138 casi, C in 66, A in 28, **D in nessuno**. Un candidato
può rispondere correttamente a quasi tutto il volume senza aprire un capitolo. L'apparato
di verifica — che è la principale promessa commerciale di un libro-workbook — è, allo
stato, non funzionante.

Il modulo M-FL01, quattordici capitoli e circa 275 pagine dedicate al TUEL e alla
gestione comunale, **non cita nemmeno un articolo di legge**. Non compaiono l'art. 42,
l'art. 48, l'art. 50, l'art. 107, l'art. 183 del D.Lgs. 267/2000. Il modulo M-FL04, per
contrasto, cita correttamente novantadue articoli. Non è una scelta editoriale: è una
disomogeneità di lavorazione che lascia scoperta proprio la materia più frequente nei
bandi comunali.

Nessuna di queste criticità mette in discussione il valore del progetto. Il perimetro
editoriale è intelligente, la distinzione fra nucleo comune (VOL-01) e delta locale
(VOL-02) è la scelta più solida dell'intera collana, e i quaranta capitoli a struttura
nucleare reggono il confronto con la concorrenza. Ma tra il manoscritto e il libro
manca ancora un passaggio industriale che non è stato fatto.

**Il volume non è pubblicabile nello stato attuale.** Con gli interventi elencati nella
tabella master — quasi tutti circoscritti e molti automatizzabili — può diventarlo in
tempi ragionevoli.

---

## 2. Punti di forza

1. **Qualità della prosa.** Frasi brevi, ritmo controllato, nessuna sbavatura
   burocratica. Il registro «ti spiego come si ragiona in prova» è tenuto con costanza
   su 46 capitoli e non scivola mai nel didascalico.
2. **Impostazione editoriale del volume.** La regola «VOL-01 per il nucleo comune,
   VOL-02 per il delta locale» è dichiarata, rispettata e verificabile. È il vero
   elemento di differenziazione rispetto ai manuali generalisti.
3. **Pulizia meccanica del testo.** Zero parole doppie; zero refusi di spaziatura
   (tranne uno); accenti corretti nel corpo del testo salvo i casi elencati al § 7.
4. **Assenza di duplicazione letterale.** Solo sei frasi identiche in più di due
   capitoli, tutte di apparato. Il corpus non è stato costruito per copia e incolla.
5. **Nessun residuo redazionale nei capitoli.** A differenza di VOL-01 prima
   dell'intervento del 10 agosto, nei 46 capitoli non è rimasta alcuna «Nota di review»,
   alcun «TODO», alcun segnaposto.
6. **Prudenza normativa.** Il testo non inventa termini né conseguenze. Distingue con
   cura fatto, qualificazione e atto. È un pregio reale, che però al § 5 mostra anche
   il suo rovescio.
7. **Correttezza delle citazioni presenti.** I 121 riferimenti ad articoli sono stati
   verificati a campione e risultano corretti: art. 11 CdS (cinque servizi di polizia
   stradale), art. 189 CdS, art. 204-bis CdS, art. 19 L. 241/1990, artt. 27 e 31
   D.P.R. 380/2001, artt. 55, 57, 347 e 357 c.p.p., artt. 50, 54 e 107 TUEL,
   artt. 81, 97, 114, 117, 118, 119, 120 Cost. Unica eccezione al § 10.
8. **Casi guidati.** Dove ci sono, sono buoni: partono da una situazione concreta e
   chiudono su un output verificabile.

---

## 3. Criticità principali

Le sei che, da sole, impediscono la pubblicazione:

| # | Criticità | Estensione | Gravità |
|---|---|---|---|
| 1 | Piè di pagina «Il Metodo BANDO» in un volume intitolato VOL-02 | 816 pagine su 830 | 🔴 |
| 2 | Tabelle frammentate con intestazione ripetuta più volte nella stessa pagina | ~448 pagine (54%) | 🔴 |
| 3 | Il volume non ha conclusione: si interrompe su una risposta di quiz | p. 830 | 🔴 |
| 4 | Quiz risolvibili a vista: 95% risposta = opzione più lunga; mai D | 232 quiz | 🔴 |
| 5 | M-FL01 senza alcuna citazione di articolo | 14 capitoli, ~275 pp. | 🔴 |
| 6 | Apostrofi e virgolette dattilografici in tutto il volume | 5.848 + 1.000 occorrenze | 🔴 |

---

## 4. Problemi strutturali

### 4.1 🔴 Il volume stampato non è il volume progettato

Il PDF è costruito da `buildVolumeBookStudioData`, che carica **soltanto** i quattro
moduli elencati in `volume.bookIds` (`text-volumes.ts:39-44`) più sei sezioni di
front matter **generate da codice**. Ne discendono quattro conseguenze.

**a) Quattro capitoli redatti restano fuori.** In
`wiki/books/vol-02-enti-locali-polizia-locale/chapters/` esistono, finiti:
`01-come-usare-vol-02-insieme-a-vol-01.md`, `02-bando-decoder-territoriale.md`,
`03-piano-30-60-90-giorni-vol-02.md`, `50-simulazione-finale-vol-02.md`.
Nessuno dei quattro compare nel PDF (verificato per ricerca testuale: zero occorrenze
di «Come usare VOL-02», «Bando Decoder territoriale», «Simulazione finale»).
Il lettore apre il libro e trova immediatamente il TUEL, senza sapere come usare il
volume, e lo chiude senza la prova integrata.

**b) L'indice analitico redatto non viene stampato.**
`front-matter/06-indice.md` è un indice ragionato di ottima fattura, con tre voci per
capitolo, la partizione in Parte I / moduli / Parte finale e otto appendici operative.
Al suo posto viene stampato l'indice generato da `buildVolumeIndexBlocks`, che elenca
capitoli e sezioni senza descrizioni. **Le appendici A-H non esistono come file** e
quindi non sono nel volume, pur essendo promesse dall'indice redazionale.

**c) L'ordine dei moduli è invertito rispetto al progetto.**
Indice e sommario redatti: M-FL01, M-FL02, **M-FL04**, M-FL03.
Volume stampato (ordine di `text-volumes.ts`): M-FL01, M-FL02, **M-FL03**, M-FL04.
Di conseguenza tutta la numerazione dei capitoli del progetto (1-50) non corrisponde
a quella stampata (1-46).

**d) La premessa stampata parla al lettore della propria impaginazione.**
FM5 (p. 5) è generata da `buildVolumePrefaceMarkdown` e recita: «I moduli interni
(M-FL01, M-FL02, M-FL03, M-FL04) non sono libri separati per il lettore… La struttura
segue una regola precisa: prima le pagine comuni del volume, poi il sommario, la
premessa e l'indice completo…». È una nota di architettura editoriale interna.
La premessa vera — `front-matter/05-premessa.md`, che apre bene, parla di concorsi e
non di file — non viene stampata.

### 4.2 🔴 Il libro non ha una fine

Pagina 830, ultima del volume, contiene: «C. Firma, protocollo, scelta dell'atto. /
D. Correzione ortografica senza riesame del contenuto. / Risposta corretta: B.».
Il volume termina dentro il blocco di verifica del capitolo 46. Non c'è conclusione,
non c'è simulazione finale, non ci sono appendici, non c'è indice analitico finale,
non c'è colophon di chiusura. Un lettore che arriva in fondo non riceve alcun segnale
di completamento.

### 4.3 🔴 Due architetture di capitolo incompatibili

| | Capp. 1-7 (M-FL01 01-07) | Capp. 8-46 |
|---|---|---|
| Nuclei numerati `N-…` | assenti | presenti (5-7 per capitolo) |
| Sezioni numerate stampate (8.1, 8.2…) | assenti | presenti |
| Voci di secondo livello nell'indice | assenti | presenti |
| Blocco Quiz | assente | 6 quiz |

Il lettore attraversa circa 110 pagine con un impianto didattico, poi ne incontra un
altro senza alcuna spiegazione. Nell'indice stampato (p. 6) i capitoli 1-7 compaiono
come voci nude, mentre dal capitolo 8 in poi si aprono in sotto-voci: la differenza è
visibile a colpo d'occhio già sfogliando le prime pagine.

### 4.4 🔴 Salti nella numerazione delle sezioni

Nei sorgenti mancano nuclei intermedi, e la numerazione stampata li segue:

| Capitolo stampato | Sezioni stampate | Mancanti |
|---|---|---|
| 19 (`m-fl02/05`) | 19.1, 19.3, 19.4, 19.5, 19.6, 19.7 | 19.2 |
| 20 (`m-fl02/06`) | 20.1, 20.3, 20.4, 20.6, 20.7 | 20.2, 20.5 |
| 21 (`m-fl02/07`) | 21.1, 21.3, 21.5, 21.6, 21.7 | 21.2, 21.4 |
| 22 (`m-fl02/08`) | 22.1, 22.3, 22.5, 22.6, 22.7 | 22.2, 22.4 |

Verificato visivamente sull'indice stampato a p. 7 (19.1 → 19.3; 20.1 → 20.3).

### 4.5 🔴 Rinvii incrociati con la numerazione sbagliata

I capitoli rinviano l'uno all'altro con i numeri **interni al modulo**, mentre il libro
stampa i numeri **di volume**. Esempi:

- `m-fl03/01` (stampato come **capitolo 27**): «Nel capitolo 2 lavorerai sul Registro
  imprese… Nel capitolo 5 userai tutto questo per decodificare bandi». I capitoli
  richiamati sono, nel volume, il 28 e il 31.
- `m-fl01` usa «Capitolo 4 su atti», «Capitolo 12 su procurement», «Capitolo 5 su
  procedimento»: qui i numeri coincidono per caso, perché M-FL01 è il primo modulo.
- In M-FL02 e M-FL04 nessun rinvio interno è corretto.

Tutti i rinvii dei moduli 2, 3 e 4 puntano quindi a capitoli sbagliati.

### 4.6 🟡 Squilibrio di lunghezza

Da 3.881 parole (cap. 4) a 8.583 (cap. 13): rapporto 2,2×. Medie per modulo:
M-FL01 ≈ 5.700, M-FL02 ≈ 6.050, M-FL03 ≈ 4.840, M-FL04 ≈ 4.490 parole.
Lo squilibrio maggiore è interno a M-FL01, dove i capitoli 1-7 (media 4.400) e
i capitoli 8-14 (media 6.850) appartengono di fatto a due generazioni redazionali.

---

## 5. Problemi contenutistici

### 5.1 🔴 M-FL01: nessuna citazione di articolo in 275 pagine

| Modulo | Capitoli | Parole | Citazioni di articolo |
|---|---|---|---|
| M-FL01 Comuni e Unioni | 14 | 80.351 | **0** |
| M-FL02 Regioni e area vasta | 12 | 72.673 | 27 (8 capitoli a zero) |
| M-FL03 Camere di commercio | 5 | 24.634 | 2 |
| M-FL04 Polizia locale | 15 | 67.298 | 92 |

Il capitolo 1 spiega Consiglio, Giunta, Sindaco, Segretario e dirigenti senza mai
nominare gli artt. 42, 48, 50, 97 e 107 TUEL. Il capitolo 10 tratta impegno,
liquidazione, ordinazione e pagamento senza l'art. 183. Il capitolo 13 tratta i titoli
edilizi senza gli artt. 3, 10, 22 e 23 del D.P.R. 380/2001.

Nei bandi comunali i quesiti sono formulati *per articolo* («ai sensi dell'art. 107
TUEL…»). Un modulo di 275 pagine sul TUEL che non fornisce mai l'aggancio numerico
lascia il candidato senza lo strumento che gli serve in aula. Il problema non è
teorico: il capitolo 1 arriva a scrivere «Non cercare subito l'articolo», il che sarebbe
una scelta pedagogica difendibile *se* gli articoli comparissero altrove nel modulo.
Non comparendo mai, la scelta diventa una lacuna.

**Intervento consigliato.** Aggiungere in ciascun capitolo M-FL01 un blocco normativo
compatto (5-8 articoli con rubrica) e inserire il riferimento puntuale nelle tabelle
organo-competenza-atto, senza toccare il corpo discorsivo. Le fonti necessarie sono già
nel repository (`decreto-legislativo-104-2010`, `d-lgs-18-agosto-2000-n-267-enti-locali`).

### 5.2 🔴 L'apparato di verifica non verifica

Analisi automatica dei 232 quiz del volume:

| Indicatore | Valore |
|---|---|
| Quiz in cui la risposta corretta è l'opzione **più lunga** | **221 / 232 (95%)** |
| Risposta corretta = A | 28 (12%) |
| Risposta corretta = B | 138 (59%) |
| Risposta corretta = C | 66 (28%) |
| Risposta corretta = D | **0 (0%)** |

Un candidato che applichi la regola «scegli l'opzione più lunga, mai la D» supera il
95% delle verifiche del volume senza leggere una riga. Il difetto nasce dalla struttura
ricorrente delle domande: l'opzione corretta è sempre quella qualificata e articolata
(«No: ne ha riordinato organi e funzioni nel quadro degli enti di area vasta»), i
distrattori sono monosillabici o assurdi.

Esempi di distrattori che non insegnano nulla e segnalano immediatamente la risposta:

- Cap. 18, Quiz 1: «Qual è il primo controllo in un procedimento regionale?
  A. **Il colore del modulo.**»
- Cap. 23, Quiz 5: «…D. **Solo se gratuita.**»
- Cap. 26, Quiz: «A. **La materia preferita dal candidato.**»

**Intervento consigliato.** Riequilibrare i 232 quiz su tre assi: (a) pareggiare la
lunghezza delle quattro opzioni entro ±20% di caratteri; (b) redistribuire la lettera
corretta su A/B/C/D in modo approssimativamente uniforme; (c) sostituire i distrattori
paradossali con errori realmente commessi dai candidati (che il volume già censisce
nelle sezioni «Errore tipico» e «Diario errori»).

### 5.3 🟠 Evasione sistematica dei dati puntuali

Il corpus contiene **117 formule** del tipo «da verificare sul testo vigente»,
«termine vigente», «dato da verificare». La prudenza è corretta in linea di principio;
diventa una lacuna quando sostituisce l'informazione che il lettore ha comprato.

Il caso più evidente è il **capitolo 36** (`m-fl04/05`, «Accertamento, contestazione,
notificazione e ricorsi nel Codice della strada»), che contiene 14 di queste formule
e **non enuncia mai**:

- il termine di notificazione del verbale (art. 201 CdS);
- il termine per il ricorso al Prefetto (art. 203 CdS);
- il termine per il ricorso al Giudice di pace (art. 204-bis CdS);
- il pagamento in misura ridotta e la riduzione per pagamento anticipato (art. 202 CdS).

Il capitolo arriva a scrivere: «la domanda corretta non è subito "entro quanti giorni?"»
e «L'errore tipico è chiedere subito "quanti giorni?"». Sono termini stabili da decenni
e sono esattamente ciò che la commissione chiede a un candidato di Polizia locale.

Nell'intero volume le affermazioni con un termine procedimentale esplicito sono **otto**,
e riguardano tutte il piano di studio 30/60/90 giorni, non le procedure.

**Intervento consigliato.** Mantenere il richiamo alla verifica, ma affiancarlo al dato:
«Il termine ordinario è di novanta giorni (art. 201 CdS): verificane sempre la versione
vigente e le ipotesi speciali». Priorità sui capitoli 34-37, 41-44 (M-FL04) e 13-14
(M-FL01).

### 5.4 🔴 Il volume è privo di apparato iconografico

Dieci immagini in 830 pagine, concentrate su dieci pagine (290-298 e 552-560), cioè
in due soli capitoli su 46. Gli altri 44 capitoli non hanno alcuna figura, benché il
testo annunci ripetutamente una «Infografica pre-epilogativa» che non esiste.

In più, **le didascalie esistenti hanno la numerazione sbagliata**:

| File | Didascalie | Capitolo stampato | Corretto |
|---|---|---|---|
| `m-fl02/01` | Figura 18.1 – 18.5 | 15 | Figura 15.1 – 15.5 |
| `m-fl03/01` | Figura 45.1 – 45.5 | 27 | Figura 27.1 – 27.5 |

I numeri seguono la numerazione dell'indice redazionale (dove i due capitoli erano
il 18 e il 45), non quella del volume stampato.

---

## 6. Problemi stilistici

### 6.1 🟠 Apparato didattico non uniforme

La stessa funzione ha nomi diversi da un capitolo all'altro, e molte sezioni ricorrenti
mancano in una parte del volume. Conteggi su 46 capitoli:

| Funzione | Denominazioni usate | Copertura |
|---|---|---|
| Sintesi finale | «Da sapere in 5 righe» | 41/46 |
| Bibliografia | «Riferimenti normativi e professionali essenziali» (40) / «…e professionali» (6) | 46/46 |
| Errori | «Errore tipico» (34) / «Errori e trappole ricorrenti» (6) | 40/46 |
| Caso finale | «Caso ragionato finale» (26) / «Caso finale ragionato» (6) | 32/46 |
| Checklist | «Checklist finale» (18) / «Checklist operativa finale» (6) | **24/46** |
| Diario errori | «Diario errori del capitolo» (10) / «Diario errori» (8) | **18/46** |
| Obiettivo | «Obiettivo del capitolo» (21) / «Obiettivo operativo del capitolo» (8) / «Obiettivo del blocco» (9) / «Obiettivo didattico» (6) / «Obiettivo» (9) | 46/46 |
| Mappa BANDO | «Mappa BANDO del capitolo» (17) / «Mappa BANDO» (13) | 30/46 |
| Orale | «Come rispondere all'orale» (9) / «Come lo chiede la commissione» (8) | 17/46 |

«Caso ragionato finale» e «Caso finale ragionato» sono la stessa cosa scritta in due
ordini diversi: è il tipo di dettaglio che un lettore attento nota e che segnala
lavorazione non conclusa.

### 6.2 🟠 Intestazioni orfane e duplicate

Quindici intestazioni sono immediatamente seguite da un'altra intestazione di pari
livello, senza testo: in stampa appaiono come titoli appesi. Le principali:

| File | Riga | Intestazione orfana |
|---|---|---|
| `m-fl04/04`, `/05`, `/06`, `/08`, `/09` | 52-53 | `### Spiegazione teorica e applicazione` seguita da `### Apertura editoriale` |
| `m-fl02/01`, `/02`, `/06`, `/12` | 74-87 | `### Spiegazione teorica` |
| `m-fl02/06` | 113 | `### Qualità della regolazione e opzioni` |
| `m-fl02/07` | 118, 216 | `### Fondi e architettura istituzionale regionale`, `### Ammissibilità, attuazione e tracciabilità` |
| `m-fl02/08` | 125, 233 | `### Milestone, target, cronoprogramma e tracciabilità`, `### DNSH ex ante ed ex post` |

E una duplicazione vera e propria:

**Posizione:** `m-fl02/06-tecnica-legislativa-air-vir-drafting.md`, righe 226 e 228
**Testo originale:** `### Analisi tecnico-normativa e coordinamento` (due volte consecutive)
**Problema:** intestazione ripetuta a distanza di due righe.
**Gravità:** 🔴
**Intervento:** eliminare la prima occorrenza.

### 6.3 🟠 Ritmo: la chiusura a sentenza

In M-FL04 quasi ogni sotto-sezione termina con un paragrafo di una sola frase che
riassume quanto appena detto («Il controllo conclusivo distingue fatti osservati, dati
acquisiti e valutazioni giuridiche…», «Soggetti e momenti dell'intervento vanno
registrati separatamente…», «Ogni canale richiede quindi una verifica documentale
specifica…»). Prese singolarmente sono buone; ripetute con questa regolarità diventano
un tic percepibile e appesantiscono la lettura. È il punto in cui il testo suona più
meccanico (§ 23 del brief).

**Intervento:** alternare, sopprimendone circa una su tre, oppure trasformandone alcune
in una domanda o in un esempio.

---

## 7. Problemi grammaticali e tipografici ricorrenti

### 7.1 🔴 Apostrofi e virgolette dattilografici in tutto il volume

Conteggio nel PDF stampato:

| Segno | Occorrenze |
|---|---|
| Apostrofo dritto `'` | **5.848** |
| Apostrofo tipografico `’` | **0** |
| Virgolette dritte `"` | **1.000** |
| Caporali `« »` | 225 |
| Virgolette curve `“ ”` | 24 |

VOL-01 è stato normalizzato con il commit `3ccdf0a`; VOL-02 no. È un difetto visibile
su quasi ogni pagina e immediatamente riconoscibile come «non editato» da un lettore
esigente. Gli script `scripts/fix-italian-typography*.py` esistono già nel repository.

### 7.2 🔴 Refusi di accento nel front matter generato (pp. 1-8)

Il testo delle prime pagine è prodotto da codice, non da file di contenuto, e contiene
errori che compaiono tali e quali nel libro:

| Pagina | Testo stampato | Corretto | Origine |
|---|---|---|---|
| 1 | «Questo volume (VOL-02) **e** collegato ai servizi digitali» | è | `book-preview.ts:459` |
| 1 | «piano di studio e **priorita**.» | priorità | `book-preview.ts:465` |
| 3 | «ed **e** costruito come libro-workbook» | è | `book-preview.ts:493` |
| 3 | «non promette copertura totale di ogni bando, **ne** aggiornamento automatico» | né | `book-preview.ts:497` |
| 2, 4 | «Modulo standard per il bacino **piu** ricorrente» | più | `text-volumes.ts:46` |
| 2 | «Volume operativo Metodo BANDO per **comuni, unioni, regioni, province, cciaa e polizia locale**» | Comuni, Unioni, Regioni, Province, CCIAA e Polizia locale | `book-preview.ts:485` (`.toLowerCase()` applicato a nomi propri e a un acronimo) |
| 4, 7, 287 | «Regioni, Province e **Citta Metropolitane**» | Città metropolitane | `title:` in `m-fl02/index.md` |

### 7.3 🔴 Titoli di capitolo senza accento (stampati)

| Capitolo stampato | Titolo stampato | Corretto | File |
|---|---|---|---|
| 23 (p. 482, indice p. 8) | Province e **Citta** metropolitane dopo la L. 56/2014 | Città | `m-fl02/09`, campo `title:` |
| 24 (indice p. 8) | **Viabilita**, edilizia scolastica, territorio ed espropri | Viabilità | `m-fl02/10`, campo `title:` |
| 25 (p. 515, indice p. 8) | Contratti, servizi pubblici locali e **societa** partecipate | società | `m-fl02/11`, campo `title:` |

### 7.4 🔴 Capitolo 22 (PNRR): dodici «è» mancanti nel testo stampato

Il file `m-fl02/08-pnrr-territoriale-regis-dnsh-controlli.md` è sfuggito alla
normalizzazione. Tutte le occorrenze sono state verificate nel PDF:

| Riga file | Pagina PDF | Testo stampato | Corretto |
|---|---|---|---|
| 109 | 461 | «La **particolarita** del PNRR **e** il legame stretto» | particolarità … è |
| 175 | — | «ReGiS **e** il sistema informativo promosso dalla Ragioneria» | è |
| 198 | 465 | «Il tema più importante non **e** il caricamento del dato» | è |
| 236 | 466 | «Nel PNRR **e** un vincolo trasversale» | è |
| 245 | 466 | «protezione e ripristino di **biodiversita** ed ecosistemi» | biodiversità |
| 266 | — | «Deve dire che la checklist **e**…» | è |
| 294 | 468 | «la domanda non **e** solo "…". **E** anche: "…"» | è … È |
| 297 | 468 | «Il pagamento non **e** automatico dopo la fattura» | è |
| 318 | 469 | «se il pagamento non **e** collegabile al progetto» | è |
| 329 | 469 | «La stessa spesa non **e** finanziata due volte?» | è |
| 503 | 477 | «Il completamento materiale **e** necessario» | è |
| 503 | 477 | «il progetto **e** identificato dal CUP» | è |

### 7.5 🟠 Altre parole senza accento nel corpo del testo

Tutte verificate nel PDF stampato:

| File : riga | Pagina PDF | Parola | Corretto |
|---|---|---|---|
| `m-fl02/04` : 480 | — | sanabilita | sanabilità |
| `m-fl02/05` : 164, 485 | — | attendibilita | attendibilità |
| `m-fl02/05` : 347 | 398 | economicita | economicità |
| `m-fl02/06` : 269 | — | visibilita | visibilità |
| `m-fl02/06` : 271 | — | leggibilita | leggibilità |
| `m-fl02/07` : 177 | — | intensita | intensità |
| `m-fl02/09` : 84 | — | densita | densità |
| `m-fl02/10` : 244 | 508 | incidentalita | incidentalità |
| `m-fl02/11` : 186, 311 | 527 | soggettivita | soggettività |
| `m-fl03/01` : 89 | 551 | profondita | profondità |
| `m-fl03/01` : 178, 187 | — | competitivita | competitività |
| `m-fl04/01` : 252 | 636 | intensita | intensità |
| `m-fl04/03` : 129 | — | anziche**'** | anziché |
| `m-fl04/08` : 120 | 731 | vivibilita**'** | vivibilità |

### 7.6 🟠 Stili di citazione normativa non uniformi

| Forma | Occorrenze |
|---|---|
| `D.Lgs.` | 73 |
| `D.lgs.` / `d.lgs.` | 1 / 2 |
| `D.P.R.` | 52 |
| `DPR` | 1 |
| `L. <numero>` | 135 |
| `L. n. <numero>` | 8 |
| `legge n. <numero>` | 34 |
| `art.` | 96 |
| `Art.` | 7 |
| `Registro imprese` | 50 |
| `registro delle imprese` | 24 |

**Intervento:** fissare uno standard nel colophon (proposta: `D.Lgs. 267/2000`,
`D.P.R. 380/2001`, `L. 241/1990`, `art.` sempre minuscolo salvo a inizio periodo) e
applicarlo con una passata automatica.

---

## 8. Ripetizioni e ridondanze

### 8.1 Ripetizioni letterali — **utile / tollerabile**

Solo sei frasi identiche compaiono in più di due capitoli, e sono tutte intestazioni o
incipit di apparato («Obiettivo del blocco. Al termine del capitolo sai:» in 8 capitoli).
È una ricorrenza funzionale, non un difetto. **Nessun intervento.**

### 8.2 Ripetizioni strutturali — **migliorabile**

Quaranta capitoli su 46 seguono uno schema quasi identico: Guida al capitolo →
Apertura editoriale → Obiettivo → Come usare → Mappa BANDO → 5-7 nuclei → Verifica con
6 quiz → Caso ragionato → Da sapere in 5 righe → Riferimenti. La regolarità aiuta lo
studio, ma diventa monotona su 830 pagine, specialmente in M-FL04, dove quindici
capitoli consecutivi hanno esattamente cinque nuclei e sei quiz.
**Intervento facoltativo:** variare il numero di nuclei dove il contenuto lo giustifica
e alternare, ogni 4-5 capitoli, la Verifica standard con un formato diverso (caso
lungo, correzione di un atto sbagliato, esercizio a tempo).

### 8.3 Ridondanze globali fra moduli

| Concetto ripetuto | Prima occorrenza | Altre occorrenze | Valutazione | Intervento consigliato |
|---|---|---|---|---|
| SUAP | cap. 13 (44 occ.) | capp. 14, 27, 28, 29, 39, 41 | tollerabile: prospettive diverse (comunale, camerale, PL) | aggiungere rinvii espliciti fra i tre trattamenti |
| SCIA | cap. 13 (14 occ.) | capp. 28, 39, 41, 42 | tollerabile | idem |
| Fascicolo e tracciabilità documentale | cap. 5 | 24 capitoli | migliorabile: definizione ripetuta più volte | definire una volta nel cap. 5 e richiamarla |
| Protocollo | cap. 3 | capp. 5, 6, 12, 14, 18, 30, 46 | migliorabile | consolidare in cap. 5, rinviare altrove |
| PNRR / fondi UE | cap. 15 | capp. 19, 21, 22, 26 | utile: progressione voluta | nessuno |
| CIG e tracciabilità finanziaria | cap. 12 (29 occ.) | capp. 14, 21, 22, 25 | tollerabile | rinvio a cap. 12 come trattazione principale |
| Ordinanza | cap. 4 (23 occ.) | capp. 35, 37, 40, 42, 43 | utile: tipologie diverse | esplicitare in cap. 40 il rinvio al cap. 4 |

Nessuna ridondanza è da eliminare; **tutte sono da segnalare al lettore**, cosa che
oggi il volume non fa mai.

---

## 9. Incongruenze

1. 🔴 **Ordine dei moduli**: indice redatto M-FL01/02/**04**/03 vs volume stampato
   M-FL01/02/**03**/04.
2. 🔴 **Numerazione dei capitoli**: progetto 1-50, volume 1-46.
3. 🔴 **Rinvii interni**: numerazione di modulo nel testo, numerazione di volume
   nell'indice e nelle testatine (§ 4.5).
4. 🔴 **Didascalie delle figure**: Figura 18.x nel capitolo 15, Figura 45.x nel
   capitolo 27 (§ 5.4).
5. 🔴 **Testatina «CONTINUA»**: stampata sull'ultima pagina di **tutti e 46 i capitoli**,
   compresa la pagina 830, ultima del libro. La testatina afferma 46 volte che il
   capitolo continua quando è finito.
6. 🟠 **Rinvii ad altri volumi**: sommario e indice redatti promettono rinvii a VOL-09
   (appalti/PNRR) e VOL-11 (ambiente); nel corpo dei 46 capitoli compare solo VOL-10
   (8 volte). VOL-09 e VOL-11 non sono mai citati.
7. 🟠 **«Workbook finale»** (sommario redatto) vs **«Parte finale – Simulazione,
   appendici e strumenti»** (indice redatto): due nomi per una sezione che, in ogni
   caso, non esiste nel volume stampato.
9. 🟡 **Maiuscole**: «Citta **M**etropolitane» nel titolo del modulo (p. 4, 7, 287) vs
   «Città **m**etropolitane» nei titoli dei capitoli e nel testo.
10. 🟡 **Metadati**: `front-matter/05-premessa.md` ha ancora `status: structure`,
    `draft_stage: source-ready-outline` e `review_required: true` mentre l'index del
    volume dichiara `draft_stage: final-editorial-review`. Non incide sulla stampa ma
    falsa i gate della pipeline.

---

## 10. Elementi da verificare (fact-checking)

**VERIFICATO** — controllati e corretti:
art. 11 CdS (cinque servizi di polizia stradale), art. 12 CdS, art. 7 CdS, art. 189 CdS,
art. 204-bis CdS; art. 19 L. 241/1990 (SCIA); artt. 27 e 31 D.P.R. 380/2001;
artt. 55, 57, 347, 357 c.p.p.; artt. 50, 54, 107 D.Lgs. 267/2000; art. 9 L. 447/1995;
artt. 81, 97, 114, 117, 118, 119, 120 Cost.; D.P.R. 581/1995 come attuazione dell'art. 8
L. 580/1993; artt. 3, 5, 7 L. 65/1986.

**VERIFICATO — nessuna modifica necessaria (aggiornato dopo verifica su fonte primaria):**

**Posizione:** `m-fl04/03-qualifiche-poteri-dipendenze-organizzazione-servizio.md`, riga 131
**Testo:** «L'art. 4 della stessa legge rimette al regolamento comunale l'organizzazione
del servizio. Disciplina inoltre distacchi, comandi e attività fuori dal territorio
dell'ente con regole e condizioni specifiche.»
**Verifica:** il testo dell'art. 4 L. 65/1986 ("Regolamento comunale del servizio di
polizia municipale") conferma entrambe le affermazioni: impone al Comune un regolamento
per il servizio e ne disciplina distacchi, comandi e operatività fuori dal territorio
dell'ente (missioni di collegamento, flagranza, calamità). Non c'è contraddizione con
l'art. 7, che riguarda la costituzione del Corpo (contingente, gradi) per i Comuni con
almeno 7 addetti: sono due regolamenti/ambiti distinti e compatibili. Il rilievo del
16/8/2026 era un falso positivo dell'analisi automatica; nessuna modifica al testo.

**DA VERIFICARE — non dispongo di elementi sufficienti per confermarlo:**
il file `wiki/sources/legge-65-1986-polizia-locale.md` contiene solo una sintesi
redazionale e il raw HTML archiviato (`wiki/raw/.../legge-65-1986-polizia-municipale.html`)
è la sola pagina-guscio di Normattiva, senza il testo degli articoli. La verifica va
condotta sulla fonte viva.

**Osservazione trasversale.** Il volume non contiene statistiche, percentuali, date di
eventi né citazioni d'autore: la superficie fact-checkable è quasi interamente normativa.
Questo riduce il rischio, ma rende ancora più pesante l'assenza di riferimenti puntuali
descritta al § 5.1.

---

## 11. Parti da ampliare

| Priorità | Parte | Motivo |
|---|---|---|
| 🔴 | M-FL01, tutti i 14 capitoli | inserire i riferimenti agli articoli (§ 5.1) |
| 🔴 | Capp. 34-37, 41-44 (M-FL04) | inserire i termini procedimentali del CdS e della L. 689/1981 (§ 5.3) |
| 🔴 | Chiusura del volume | conclusione, simulazione finale, appendici A-H (§ 4.2) |
| 🟠 | Capp. 1-7 (M-FL01) | dotarli di nuclei numerati e blocco Verifica come gli altri 39 (§ 4.3) |
| 🟠 | Cap. 23 (`m-fl02/09`), 4.719 parole | il più corto dei capitoli a nucleo, su una materia (L. 56/2014) molto richiesta |
| 🟡 | M-FL03 | 5 capitoli per un modulo che l'indice segnala come «da validare»: se resta nel perimetro, va portato alla densità degli altri |

---

## 12. Parti da ridurre

| Parte | Motivo |
|---|---|
| Cap. 13 (`m-fl01/13`), 8.583 parole e 144 righe di tabella | il capitolo più lungo del volume su una materia dichiaratamente di «interfaccia», con rinvio a VOL-10 per la trattazione vera. Riducibile del 20-25% |
| Cap. 14 (`m-fl01/14`), 183 righe di tabella | il laboratorio è quasi interamente tabellare; alcune tabelle sono elenchi travestiti |
| Chiusure a sentenza in M-FL04 | § 6.3 |
| Sezione «Gli organi del Comune» (cap. 1, righe 141-146) | sezione puramente annunciativa: «Le tre sezioni che seguono li prendono uno per uno». Assorbibile nell'incipit della sezione successiva |

---

## 13. Parti eventualmente da eliminare

1. 🔴 Le voci non bibliografiche dalle sezioni «Riferimenti normativi e professionali
   essenziali». Nel libro stampato il lettore trova elencati come fonti (verificato alle
   pp. 24, 39, 55, 70): «VOL-02 - dossier redazionale Enti locali e Polizia locale» (×4),
   «Campione bandi inPA 2026 per VOL-02» (×4), «Struttura madre del Metodo BANDO»,
   «Enti locali», «Comune», «Metodo BANDO», «Procedimento amministrativo», «ANPR»,
   «PA digitale», «Privacy e protezione dati». Sono nodi interni della knowledge base,
   non fonti consultabili. Vanno rimossi o sostituiti con la fonte reale.
2. 🟠 L'intestazione duplicata di `m-fl02/06`, riga 226.
3. 🟠 Le 15 intestazioni orfane (§ 6.2), da eliminare o da dotare di testo.
4. 🔵 La sezione annunciativa del cap. 1 (§ 12).

---

## 14. Parti eventualmente da spostare

1. 🔴 I quattro capitoli di orientamento vanno **inseriti** (non spostati): capp. 1-3
   in apertura, prima di M-FL01; cap. 50 in chiusura, dopo M-FL04.
2. 🔴 L'ordine dei moduli va deciso una volta sola. Se si mantiene l'ordine progettuale
   (PL prima delle Camere di commercio, coerente con il peso dei due bacini), va
   modificato `text-volumes.ts:39-44`; altrimenti vanno riallineati indice redatto,
   sommario e didascalie delle figure.
3. 🟠 La premessa redatta (`front-matter/05-premessa.md`) va portata al posto di quella
   generata.
4. 🟡 Le sezioni «Riferimenti di base», presenti in 13 capitoli a inizio capitolo e in 40
   in coda, vanno unificate in una sola posizione.

---

## 15. Miglioramenti consigliati

1. Un **frontespizio di parte** per ciascun modulo che indichi anche l'intervallo di
   capitoli («M-FL02 · capitoli 15-26»), così da riconciliare la numerazione di volume
   con i rinvii interni.
2. Una **legenda dell'apparato** nelle prime pagine: che cosa sono Mappa BANDO, nuclei,
   Verifica, Diario errori, Da sapere in 5 righe. Oggi il lettore lo deduce.
3. Un **glossario** a fine volume: il testo introduce DUP, PEG, PIAO, FPV, FCDE, REA,
   ComUnica, ReGiS, DNSH, SCIA, CILA, SUE, SUAP senza un punto di consultazione unico.
4. **Rinvii incrociati espliciti** sui concetti che tornano in più moduli (§ 8.3).
5. Un **indice analitico per voci** (non solo per capitoli), che in un manuale da
   concorso è uno strumento di consultazione, non un ornamento.
6. Riequilibrare la **densità iconografica**: se le figure restano dieci, è preferibile
   toglierle del tutto piuttosto che averle in due capitoli su 46.

---

## 16. Errori obbligatori da correggere prima della pubblicazione

Sono i 🔴 della tabella master (§ 20): interventi 1-18. In sintesi:

1. Piè di pagina con il titolo corretto del volume (816 pagine) — stringa hardcodata in
   `app/components/book-studio-panel.tsx:868`.
2. Impaginazione delle tabelle senza ripetizione dell'intestazione (~448 pagine).
3. Testatina «CONTINUA» soppressa sull'ultima pagina di ogni capitolo (46 capitoli).
4. Inclusione dei quattro capitoli di orientamento e simulazione.
5. Chiusura del volume (conclusione + appendici o rimozione della promessa).
6. Allineamento dell'ordine dei moduli e della numerazione dei capitoli.
7. Correzione dei rinvii interni nei moduli 2, 3 e 4.
8. Premessa redatta al posto della premessa generata.
9. Refusi del front matter generato (7 stringhe in `book-preview.ts` e `text-volumes.ts`).
10. Accenti nei titoli di capitolo e di modulo (4 campi `title:`).
11. Capitolo 22: 12 «è» + 3 parole accentate.
12. Altri 14 refusi di accento nel corpo del testo.
13. Normalizzazione tipografica di apostrofi e virgolette (6.848 sostituzioni).
14. Colmatura dei salti di numerazione delle sezioni (7 nuclei mancanti).
15. Rimozione dell'intestazione duplicata e delle 15 orfane.
16. Ribilanciamento dei 232 quiz.
17. Riferimenti agli articoli in M-FL01.
18. Pulizia delle bibliografie dai nodi interni della knowledge base.

---

## 17. Migliorie facoltative

Interventi 19-29 della tabella master: uniformazione dei nomi delle sezioni ricorrenti,
stile di citazione normativa, riduzione delle chiusure a sentenza, riequilibrio delle
lunghezze, rinvii sulle ridondanze globali, glossario, indice analitico, legenda
dell'apparato, gestione delle 19 pagine con riempimento inferiore al 55%.

---

## 18. Valutazione numerica

| Dimensione | Voto | Motivazione |
|---|---:|---|
| Qualità complessiva | **5,5** | Testo forte, prodotto non finito: la distanza fra i due è il voto |
| Struttura | **4** | Volume stampato diverso dal progetto, quattro capitoli fuori, nessuna chiusura, due architetture di capitolo |
| Chiarezza | **8** | Il lettore capisce sempre dove si trova e che cosa deve produrre |
| Stile | **8** | Voce riconoscibile, misurata, mai burocratica |
| Grammatica | **6,5** | Corpo del testo pulitissimo, ma 30 refusi di accento stampati e un intero capitolo non normalizzato |
| Fluidità | **7** | Buona; penalizzata dalle chiusure a sentenza in M-FL04 |
| Coerenza | **4** | Numerazioni, rinvii, didascalie, ordine dei moduli e nomi delle sezioni non allineati |
| Approfondimento | **5** | M-FL04 approfondisce davvero; M-FL01 resta descrittivo e senza articoli; 117 rinvii a «verificare» al posto del dato |
| Autorevolezza | **5,5** | Le citazioni presenti sono corrette, ma un manuale che non cita gli articoli sul TUEL non può essere percepito come autorevole |
| Originalità | **8** | L'impianto «nucleo comune + delta locale» e il Bando Decoder territoriale sono un differenziale reale |
| Leggibilità | **4** | Le tabelle spezzate su 54% delle pagine dominano l'esperienza di lettura |
| Coinvolgimento | **6,5** | Buono nei casi guidati, debole nella ripetitività dei 15 capitoli finali |
| Qualità dell'introduzione | **3** | La premessa stampata parla dell'impaginazione del libro; la premessa buona non è nel volume |
| Qualità della conclusione | **1** | Non esiste: il libro finisce su «Risposta corretta: B» |
| Maturità editoriale | **4** | Manoscritto maturo, edizione no |
| Prontezza per la pubblicazione | **3** | Sei criticità bloccanti, tutte risolvibili |

**Media ponderata: 5,3 / 10.**

---

## 19. Giudizio finale sulla pubblicabilità

# C — NECESSARIA REVISIONE EDITORIALE

**Motivazione.**

Non è **D** perché il materiale non richiede una revisione strutturale nel senso proprio:
il perimetro editoriale è corretto, la sequenza dei moduli è logica, la scrittura è
già di livello pubblicabile e quaranta capitoli su 46 hanno un impianto didattico solido.
Non c'è nulla da riscrivere da capo.

Non è **B** perché le criticità non sono «alcune correzioni». Sei di esse sono bloccanti
e tre di queste — il piè di pagina di un altro volume su 816 pagine, le tabelle spezzate
su metà del libro, l'assenza di una conclusione — sarebbero rilevate da qualunque lettore
entro i primi minuti di consultazione, e da un recensore entro la prima pagina. Un
volume che si chiude su «Risposta corretta: B» non è un libro finito.

È **C** perché il lavoro che manca è identificabile, circoscritto e in larga parte
meccanico. Cinque dei sei problemi bloccanti si risolvono nella catena di composizione
(`book-preview.ts`, `text-volumes.ts`) e non richiedono di toccare il testo. Due
richiedono lavoro redazionale vero e non delegabile: il ribilanciamento dei 232 quiz e
l'inserimento dei riferimenti normativi in M-FL01. Il resto è normalizzazione.

**Una raccomandazione.** Lo step 24 del pacchetto di consegna è in stato
`humanConfirmation: pending-step-24`. Va mantenuto pendente. Il `REPORT-PUBBLICABILITA.md`
dello step 21 e il `PREFLIGHT.md` dello step 22 hanno lasciato passare difetti visibili
a occhio nudo sulla prima pagina del libro: prima di rigenerare il candidato conviene
aggiungere ai gate tre controlli automatici — testo del piè di pagina uguale al titolo
del volume, assenza di intestazioni di tabella ripetute nella stessa pagina, ultima
pagina del volume non appartenente a un blocco di verifica.

---

## 20. Tabella master delle correzioni

| N. | Capitolo / posizione | Categoria | Gravità | Problema | Intervento consigliato |
|---:|---|---|:--:|---|---|
| 1 | Tutte le pagine di contenuto (816/830) | Errore critico | 🔴 | Piè di pagina «Il Metodo BANDO» in VOL-02 | Il titolo è **hardcodato** in `app/components/book-studio-panel.tsx:868` (`<span>Il Metodo BANDO</span>`): sostituirlo con il titolo del volume corrente |
| 2 | ~448 pagine (es. 24, 30, 53) | Impaginazione | 🔴 | Tabelle spezzate in blocchi da 4 (o 2, o 1) righe, con intestazione ristampata fino a 4 volte nella stessa pagina | Alzare/rimuovere `DEFAULT_MAX_TABLE_ROWS_PER_PREVIEW_BLOCK` (`book-preview.ts:136-138`) e ripetere l'intestazione solo a cambio pagina |
| 3 | p. 830 e fine di tutti i 46 capitoli | Impaginazione | 🔴 | Testatina «CONTINUA» stampata anche sull'ultima pagina del capitolo e del libro | Sopprimere il marcatore sull'ultima pagina di ciascun capitolo |
| 4 | Struttura del volume | Struttura | 🔴 | I 4 capitoli di orientamento e la simulazione finale non sono nel PDF | Includere `books/vol-02-.../chapters/` nella compilazione del volume, prima e dopo i moduli |
| 5 | Chiusura del volume | Struttura | 🔴 | Il libro finisce su una risposta di quiz; mancano conclusione e appendici A-H | Aggiungere capitolo di conclusione; redigere le appendici o rimuoverne l'annuncio dall'indice |
| 6 | `text-volumes.ts:39-44` / indice redatto | Coerenza | 🔴 | Ordine dei moduli invertito (M-FL03 / M-FL04) e numerazione 1-50 vs 1-46 | Decidere un ordine unico e riallineare indice, sommario e didascalie |
| 7 | Tutti i capitoli di M-FL02, M-FL03, M-FL04 | Coerenza | 🔴 | Rinvii interni con numerazione di modulo anziché di volume | Riscrivere i rinvii con il numero di volume (o con il titolo del capitolo) |
| 8 | FM5, p. 5 | Contenuto | 🔴 | La premessa stampata descrive l'impaginazione del libro | Sostituire con `front-matter/05-premessa.md` |
| 9 | pp. 1-4 | Refuso | 🔴 | «e» per «è», «priorita», «ne» per «né», «piu», «cciaa» minuscolo | Correggere le 6 stringhe in `book-preview.ts:459,465,485,493,497` e `text-volumes.ts:46` |
| 10 | pp. 4, 7, 287, 482, 515 + indice | Refuso | 🔴 | «Citta Metropolitane», «Citta», «societa», «Viabilita» nei titoli | Correggere i campi `title:` in `m-fl02/index.md` e in `m-fl02/09`, `/10`, `/11` |
| 11 | Cap. 22, pp. 461-477 | Refuso | 🔴 | 12 «e» per «è» + particolarita, biodiversita, visibilita | Passata di normalizzazione su `m-fl02/08` (righe 109, 175, 198, 236, 245, 266, 294, 297, 318, 329, 503) |
| 12 | 14 punti in 9 file | Refuso | 🔴 | Parole senza accento nel corpo (§ 7.5), incluse `anziche'` e `vivibilita'` | Correzione puntuale |
| 13 | Intero volume | Tipografia | 🔴 | 5.848 apostrofi dritti, 1.000 virgolette dritte, 0 apostrofi tipografici | Applicare `scripts/fix-italian-typography*.py` come già fatto per VOL-01 |
| 14 | Capp. 19, 20, 21, 22 | Struttura | 🔴 | Sezioni numerate con salti (manca 19.2, 20.2, 20.5, 21.2, 21.4, 22.2, 22.4) | Rinumerare i nuclei in sequenza o inserire i nuclei mancanti |
| 15 | `m-fl02/06`:226-228 + 15 punti | Struttura | 🔴 | Intestazione duplicata e 15 intestazioni orfane | Eliminare la duplicazione; dotare di testo o rimuovere le orfane |
| 16 | 232 quiz, tutto il volume | Contenuto | 🔴 | Risposta corretta = opzione più lunga nel 95% dei casi; mai D | Pareggiare la lunghezza delle opzioni, redistribuire A/B/C/D, sostituire i distrattori paradossali |
| 17 | M-FL01, capp. 1-14 | Contenuto | 🔴 | Nessuna citazione di articolo in 275 pagine sul TUEL | Aggiungere un blocco normativo per capitolo e i riferimenti nelle tabelle organo-competenza-atto |
| 18 | pp. 24, 39, 55, 70 e altre | Apparato | 🔴 | Bibliografie con nodi interni della knowledge base («dossier redazionale», «Comune», «Metodo BANDO») | Filtrare le voci non bibliografiche o sostituirle con la fonte reale |
| 19 | Capp. 1-7 | Struttura | 🟠 | Nessun nucleo numerato, nessun quiz: architettura diversa dal resto | Portarli allo schema dei capitoli 8-46 |
| 20 | Capp. 15 e 27 | Apparato | 🟠 | Didascalie «Figura 18.x» e «Figura 45.x» in capitoli stampati come 15 e 27 | Rinumerare le 10 didascalie |
| 21 | 46 capitoli | Coerenza | 🟠 | Nomi diversi per la stessa sezione ricorrente (§ 6.1) | Fissare un lessico unico e applicarlo |
| 22 | Capp. 34-37, 41-44 e altri | Contenuto | 🟠 | 117 rinvii a «verificare sul testo vigente» al posto dei termini procedimentali | Affiancare il dato al richiamo alla verifica, a partire dal cap. 36 |
| 23 | `m-fl04/03`:131 | Fact-checking | ✅ | Verificato su fonte primaria: nessuna contraddizione, l'art. 4 tratta davvero di distacchi/comandi/territorio (v. § 10) | Nessuno |
| 24 | Intero corpus | Coerenza | 🟠 | Stili di citazione normativa non uniformi (§ 7.6) | Fissare lo standard e applicarlo con passata automatica |
| 25 | M-FL04, tutti i capitoli | Stile | 🟠 | Chiusura a sentenza di una riga a fine di quasi ogni sotto-sezione | Sopprimerne circa una su tre |
| 26 | Sommario e indice redatti | Coerenza | 🟠 | Promettono rinvii a VOL-09 e VOL-11 mai presenti nel corpo | Inserire i rinvii o rimuovere la promessa |
| 27 | Capp. 13, 14 | Ritmo | 🟡 | Capitoli più lunghi del 40-100% rispetto alla media, con 144 e 183 righe di tabella | Ridurre del 20-25%, convertire in prosa le tabelle che sono elenchi |
| 28 | 7 concetti trasversali | Ridondanza | 🟡 | SUAP, SCIA, protocollo, fascicolo, CIG ricorrono in più moduli senza rinvii | Aggiungere rinvii espliciti alla trattazione principale |
| 29 | pp. 3, 5, 70, 88, 224, 333, 385, 685 | Impaginazione | 🔵 | 19 pagine riempite sotto il 55%, di cui 6 sotto il 30% (p. 685 al 7%) | Verificare i salti di pagina a fine capitolo |

---

## 21. Errori individuati nel secondo controllo

Secondo passaggio indipendente, condotto cercando esclusivamente ciò che poteva essere
sfuggito. Risultati:

| Controllo | Esito |
|---|---|
| Parole doppie | **0 su 256.000 parole** |
| Spazi doppi / spazio prima di punteggiatura | **1** riga (`m-fl02/06`:341, dentro una citazione di testo normativo simulato) |
| Parole mancanti | nessuna rilevata |
| Numerazioni errate | 4 capitoli con salti di sezione (§ 4.4); 10 didascalie con numero di capitolo errato (§ 5.4) |
| Titoli incoerenti | 4 titoli senza accento (§ 7.3); «Citta **M**etropolitane» vs «Città **m**etropolitane» |
| Riferimenti interni sbagliati | tutti i rinvii di M-FL02, M-FL03, M-FL04 (§ 4.5) |
| Nomi scritti diversamente | «Polizia municipale» (16) / «Polizia locale» (299): differenza **corretta**, riflette L. 65/1986 vs leggi regionali. Nessun intervento |
| Date | nessuna data di evento nel corpus: nulla da verificare |
| Percentuali | nessuna percentuale nel corpus |
| Note | il volume non usa note a piè di pagina: nessuna incoerenza |
| Bibliografia | § 13, punto 1 |
| Formattazione | apostrofi e virgolette (§ 7.1); intestazioni orfane (§ 6.2); tabelle (§ 4, punto 2 della tabella master) |
| Conteggio pagine | PDF 830 pagine = `VERSION.json`; trim 6,69 × 9,61 pollici = dichiarato. **Corretti** |
| Markdown residuo nel PDF | nessun `[[wikilink]]`, nessun ID di nucleo `N-FL0…`, nessun percorso `wiki/`. **Pulito** |

**Nuovi elementi emersi solo nel secondo controllo:**

1. 🔴 La testatina «CONTINUA» sull'ultima pagina di tutti i 46 capitoli (§ 9, punto 5) —
   non rilevata nella prima analisi, che aveva controllato le testatine solo a campione.
2. 🟡 Nell'indice stampato (p. 6) i capitoli 1-7 non hanno sotto-voci mentre tutti gli
   altri le hanno: la disomogeneità del § 4.3 è visibile già nelle prime pagine e va
   citata come conseguenza, non solo come causa.
3. 🔵 Il piè di pagina «www.capitalepersonale.it» compare su 13 pagine (front matter) e
   «Il Metodo BANDO» su 816: anche risolvendo il punto 1, resta da decidere un piè di
   pagina unico per tutto il volume.

---

## 22. Checklist finale pre-pubblicazione

- [ ] Piè di pagina corretto su tutte le pagine
- [ ] Tabelle senza intestazione ripetuta nella stessa pagina
- [ ] «CONTINUA» assente sull'ultima pagina di ogni capitolo
- [ ] Capitoli di orientamento (1-3) presenti in apertura
- [ ] Simulazione finale presente in chiusura
- [ ] Conclusione del volume presente
- [ ] Appendici A-H presenti, oppure rimosse dall'indice
- [ ] Ordine dei moduli coerente fra `text-volumes.ts`, indice e sommario
- [ ] Numerazione dei capitoli coerente fra testo, indice e testatine
- [ ] Rinvii interni verificati uno per uno
- [ ] Premessa redazionale al posto di quella generata
- [ ] Front matter privo di refusi (pp. 1-8 rilette a stampa)
- [ ] Titoli di capitolo e di modulo con gli accenti corretti
- [ ] Capitolo 22 normalizzato
- [ ] Passata tipografica su apostrofi e virgolette completata
- [ ] Nessun salto nella numerazione delle sezioni
- [ ] Nessuna intestazione orfana o duplicata
- [ ] Quiz ribilanciati: lunghezza opzioni, distribuzione A/B/C/D, distrattori
- [ ] Riferimenti normativi puntuali presenti in M-FL01
- [ ] Bibliografie prive di nodi interni della knowledge base
- [ ] Didascalie delle figure rinumerate
- [ ] Lessico dell'apparato uniformato
- [ ] Rilettura a stampa di 20 pagine campione dopo la rigenerazione
- [ ] Gate automatici aggiunti al preflight (piè di pagina, tabelle, ultima pagina)
- [ ] `humanConfirmation` dello step 24 rilasciata solo dopo i punti precedenti
