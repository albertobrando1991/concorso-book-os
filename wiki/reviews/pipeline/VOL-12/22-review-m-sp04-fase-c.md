---
id: pipeline-vol-12-22-review-m-sp04
type: pipeline_review
title: "VOL-12 — M-SP04: review editoriale di chiusura fase C"
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp04-prefettizia-diplomatica
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-14T00:20:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp04", "review", "fase-c"]
---

# VOL-12 — M-SP04: review editoriale di chiusura fase C

Review della consegna in `wiki/reviews/pipeline/VOL-12/17-consegna-m-sp04-fase-c.md`, secondo il mandato di `11-ordine-di-lavoro-codex-fase-c.md` § 9: verità delle fonti, tenuta dei gate, coerenza matrice-capitoli-piano, assenza di contenuto inventato.

**Nota di chiusura (2026-08-14T00:20).** L'unico rilievo di questa review (E01) è stato applicato: `binario: AB` è stato uniformato a `binario: comune` nei capitoli 04-07, coerentemente con il capitolo 01 e con la matrice. I due gate automatici sono stati rieseguiti dopo la modifica e restano verdi su tutti e sette i capitoli. Il modulo non ha più rilievi aperti.

## 1. Sintesi editoriale

- Genere editoriale: modulo specialistico per concorso pubblico (carriera prefettizia e carriera diplomatica), formato 2 a nuclei.
- Pubblico target: candidato laureato che usa già Il Metodo BANDO e punta a un ingresso diretto in carriera dirigenziale.
- Perimetro di questa revisione: i sette capitoli di M-SP04, la source note, la matrice di copertura, il piano editoriale e l'indice del modulo.
- Stato generale in una frase: modulo solido, tracciabile e pronto per la chiusura fase C; nessun errore bloccante rilevato, un'unica incoerenza di metadato non bloccante.

## 2. Punti applicati della checklist

Applicati: struttura e indice (punti 1-2 dei 4 livelli), coerenza di capitolo, accuratezza contenutistica/normativa, chiarezza didattica, coerenza globale su terminologia e cifre ricorrenti (posti, soglie, tempi), gate di copertura didattica integrale (§27 della skill).

Non applicati: correzione di superficie riga per riga (ortografia/punteggiatura) — il testo è stato letto integralmente ma non passato a un controllo ortografico automatizzato dedicato; verifica del layout impaginato (non esiste ancora un file di impaginazione per questo modulo).

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Cap. 04-07, frontmatter `binario` | Coerenza terminologica | Lieve | I capitoli 04, 05, 06, 07 dichiaravano `binario: AB`, valore assente sia dall'enum del contratto (`comune \| base \| isp \| op \| dir \| A \| B \| C`) sia dalla matrice, che classifica gli stessi nuclei come `comune` (righe N-SP04-08-xx, 09-xx, 11-xx, 12-xx, 13-xx). Il capitolo 01, sugli stessi contenuti condivisi, usa correttamente `comune`. | Uniformato a `comune` nei quattro capitoli, per coerenza con la matrice e con il resto del volume (M-SP02 usa `comune` per i capitoli trasversali ai binari). Gate rieseguiti dopo la modifica: verdi su tutti e sette i capitoli. | **Corretto** (2026-08-14) |

Nessun errore di categoria grave o media rilevato. Non risultano norme, date, numeri o programmi inventati; non risultano elenchi diagnostici riprodotti; non risultano link interni o dipendenze dichiarate da fonti/wiki nel corpo dei capitoli (confermato anche dal gate automatico).

## 4. Osservazioni per capitolo

### Capitolo 01 — Mappa, scelta del binario e Bando Decoder
- Punti di forza: le proporzioni 158/35, il limite dei quattro tentativi diplomatici e il rinvio condizionato alla *Banca dati ufficiale* sono riportati con gli stessi dati e le stesse cautele della source note; il Bando Decoder comparato non media i due bandi, tiene le schede separate.
- Criticità: nessuna.

### Capitolo 02 — Carriera prefettizia: prove, materie e ordinamento
- Punti di forza: punteggio asimmetrico della preselettiva (90 quesiti, +1,10/+1,30/+1,70 e penalità corrispondenti), le trentacinque ore di scritti e le soglie 70/60 sono riportati esattamente come nella source note; il d.lgs. 139/2000 è citato con perimetro dichiarato (natura unitaria, funzioni, durata biennale della formazione, correzione esplicita del dato "un anno" diffuso ma errato).
- Criticità: nessuna.

### Capitolo 03 — Carriera diplomatica: prove, materie e ordinamento
- Punti di forza: prova attitudinale (50 quesiti, 60 minuti, +1/-0,25/0, soglia 60%), le ventuno ore di scritti e le soglie 70/70/60 sono corrette; il d.P.R. 18/1967 è citato per articoli (99, 99-bis, 100-103, 105-110-bis) nel perimetro dichiarato, senza promettere sede o carriera individuale.
- Criticità: nessuna.

### Capitolo 04 — Le lingue straniere
- Punti di forza: tratta correttamente il livello QCER come stima dichiarata e non come requisito normativo (regola esplicita del § 3.5 del mandato Codex, rispettata alla lettera); distingue con precisione i due regimi (vocabolario ammesso in prefettizia, vietato in diplomatica).
- Criticità: nessuna.

### Capitolo 05 — La prova orale e la postura professionale
- Punti di forza: tiene separati i due programmi orali senza fonderli; il trattamento della gestione dell'incertezza (non inventare il numero di un articolo dimenticato) è coerente con la regola di merito del mandato Codex sul divieto di contenuto inventato.
- Criticità: nessuna.

### Capitolo 06 — Piano di preparazione, carico e tentativi
- Punti di forza: dichiara esplicitamente l'orizzonte 6-12 mesi come minimo condizionato e non come promessa, coerentemente con la nota della source note sulle trentacinque ore di scritti; il registro dei tentativi diplomatici è trattato come dato giuridico da documentare, non da stimare a memoria.
- Criticità: nessuna.

### Capitolo 07 — Errori, casi e checklist finali
- Punti di forza: l'accorpamento di Bando Decoder (nel cap. 01) e di checklist+errori (in questo capitolo) è motivato per iscritto nel piano editoriale con il sintomo che lo ha imposto, come richiesto dal mandato; le checklist restano operative senza duplicare il corpo teorico dei capitoli 2-3.
- Criticità: nessuna. (E01 era un rilievo di metadato, ora corretto.)

## 5. Coerenza globale

- Terminologia: coerente in tutto il modulo per le cifre ricorrenti (158/35 posti, 90/50 quesiti, soglie 70-60, limite dei quattro tentativi, durata biennale/nove mesi delle formazioni iniziali) e, dopo la correzione E01, anche per il valore `binario` in frontmatter.
- Struttura vs indice: l'indice del modulo elenca esattamente e nell'ordine corretto i sette capitoli con i titoli che compaiono nei rispettivi frontmatter; nessun capitolo orfano, nessun link rotto.
- Promesse dell'introduzione mantenute: sì. Il piano editoriale promette due binari sdoppiati su mappa, prove, materie e piano, con lingue e orale trattati come sezioni condivise: la struttura consegnata rispetta esattamente questo disegno.

## 6. Contenuto da verificare

Le seguenti voci sono già dichiarate come incognite esplicite nei capitoli stessi (corretto, non è un difetto) e restano da monitorare quando escono le tornate future, non da correggere ora:
- pubblicazione della banca dei quesiti della preselettiva prefettizia (assente alla data di verifica, correttamente dichiarata);
- livello QCER realmente richiesto nelle due carriere (fonte non lo indica; trattato come stima dichiarata);
- eventuale limite ai tentativi della carriera prefettizia (non rinvenuto nelle fonti esaminate; assenza documentata, non affermata come certezza definitiva).

Non ho eseguito una nuova ricerca normativa esterna: la verifica si è basata sul confronto fra capitoli, source note e file PDF effettivamente presenti in `wiki/raw/m-sp04-prefettizia-diplomatica/` (8 documenti, coerenti con quelli citati).

## 7. Suggerimenti facoltativi (non errori)

Nessuno. La struttura a sette capitoli con i due accorpamenti motivati è già la soluzione più snella compatibile con la regola dei cinque nuclei del mandato Codex; non vedo margini di ulteriore snellimento che non tolgano contenuto.

## 8. Priorità degli interventi

Nessun intervento residuo. L'unico rilievo (E01) è stato applicato in questa stessa review.

## 9. Giudizio di pubblicabilità

**Pubblicabile.**

Motivazione: entrambi i gate automatici (`didactic-density-gate`, `chapter-lint-gate`) passano su tutti e sette i capitoli, anche dopo la correzione E01; la matrice è sincronizzata 1:1 con i capitoli (37 nuclei, 0 parziali, 0 mancanti); le fonti citate esistono in `wiki/raw/` e sono riscontrate dalla source note con livello di verifica dichiarato; non risultano norme, cifre o fatti non riconducibili a una fonte dichiarata; le incognite sono sempre dichiarate come tali, mai riempite per deduzione; i rinvii al VOL-01 puntano a capitoli realmente esistenti nell'elenco autorizzato dal mandato; il rilievo di metadato rilevato in prima battuta è stato corretto e riverificato.

## 10. Limiti di questa revisione

Non ho svolto una nuova ricerca normativa autonoma sulle fonti primarie (d.i. 144/2002, d.lgs. 139/2000, d.P.R. 18/1967, d.m. 357/1999, bandi): ho verificato che i PDF dichiarati esistano nel corpus e che i dati riportati nei capitoli coincidano con quelli già trascritti e datati nella source note, che dichiara i propri livelli di verifica (VERIFICATO/SCHEDATO) fonte per fonte. Non ho eseguito un controllo ortografico/grammaticale di superficie automatizzato sull'intero corpo (circa 28.000 parole); la lettura integrale non ha segnalato refusi, ma un secondo passaggio dedicato resta possibile. Non ho ispezionato un file di impaginazione, perché non esiste ancora per questo modulo.

## Esito per la pipeline

Il modulo M-SP04 può considerarsi chiuso per la fase C. Non essendo la scheda pipeline di VOL-12 ancora estesa ai capitoli (§ 7 del mandato Codex), non esiste uno step CLI da completare con `npm run pipeline -- complete`: la chiusura di questa review è la condizione dichiarata dal mandato per procedere al modulo successivo nell'ordine consigliato (M-SP01, già in-progress sullo step 07, poi M-SP03 se non già coperto dai file 18-21 già presenti in questa cartella).
