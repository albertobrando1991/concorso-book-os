---
id: review-vol-02-verifica-automatica-2026-07-24
type: review
title: "Report editoriale - VOL-02, verifiche automatiche 2026-07-24"
status: verified_automatic
domain: "concorsi pubblici italiani"
topics: ["vol-02", "revisione editoriale", "copertura didattica integrale", "verifica automatica"]
entities: ["Metodo BANDO", "Comune", "Regione", "Polizia locale", "Camera di commercio"]
source_refs: ["sources/principio-copertura-didattica-integrale-2026-07-17.md", "sources/logica-volumi-copertura-concorsobook-v4.md", "sources/verifica-automatica-vol-02-2026-07-24.md"]
book_refs: ["vol-02-enti-locali-polizia-locale"]
confidence: 0.95
created_at: 2026-07-24T17:30:00+02:00
updated_at: 2026-07-24T17:45:00+02:00
review_required: true
canonical: true
tags: ["revisione-editoriale", "vol-02", "verifica-automatica", "pre-pubblicazione"]
issue_type: editorial_review
severity: high
affected_pages: ["books/vol-02-enti-locali-polizia-locale", "books/moduli/m-fl01-comuni-unioni", "books/moduli/m-fl02-regioni-province-citta-metropolitane", "books/moduli/m-fl03-camere-commercio", "books/moduli/m-fl04-polizia-locale"]
---

# Report editoriale - VOL-02 - verifiche automatiche

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook specialistico per concorsi nelle funzioni locali.
- Pubblico target: candidati a Comuni, Unioni, Regioni, Province, Citta metropolitane, Polizia locale e Camere di commercio, con VOL-01 come base comune.
- Perimetro di questa revisione: tutti i controlli automatizzabili su copertura, fonte, collegamento, bando campione, preview A4 e verifiche tecniche; esclusa la validazione umana.
- Stato generale in una frase: il corpus e' verificato automaticamente e pronto alla validazione umana; la preview A4 non presenta contenuti tagliati o sovrapposti, ma le review umane restano obbligatorie.

## 2. Punti applicati della checklist

Applicati automaticamente: 1-30, incluso il punto 27 con la preview Book Studio. Sono stati inoltre controllati: cinquanta capitoli presenti con testo didattico, assenza di nuclei `mancante` o `solo-nominato`, riferimenti `sources/` risolti, fonti ufficiali per i cluster sensibili e prova di rendering del volume aggregato. La preview ha prodotto 412 pagine A4; il controllo puntuale dei blocchi rispetto al piede di pagina non rileva overflow reali. La validazione linguistica e normativa umana resta espressamente fuori dal perimetro.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| V02-A-01 | Preview A4 del volume aggregato | Layout | Lieve | La prima rilevazione ha segnalato due overflow. Il controllo puntuale ha escluso il contenitore nascosto di misurazione e ha verificato la distanza tra blocchi e piede di pagina: non ci sono contenuti eccedenti nelle pagine A4 effettive. | Mantenere il controllo puntuale nelle future verifiche, senza modificare capitoli o impaginazione. | Risolto |
| V02-A-02 | Nuclei normativi, bandi e fonti locali | Accuratezza normativa | Grave | Il controllo documentale ha confermato fonti primarie o istituzionali, ma non puo sostituire il giudizio umano su testi vigenti, prassi, regolamenti e caso concreto. | Eseguire la validazione umana per cluster, datarla e aggiornare la matrice solo a esito documentato. | Escluso dal ciclo |
| V02-A-03 | M-FL03 e laboratori di bando | Allineamento bando-profilo | Grave | Il campione ufficiale sostiene il metodo, non un programma unico per tutti i profili o tutte le procedure. | Confrontare ogni uso editoriale con bando, allegati, rettifiche, prove e criteri della procedura destinataria. | Da validare umanamente |

## 4. Osservazioni per capitolo

### Parte I - Capitoli 1-3

- Punti di forza: percorso completo da lettura del bando a piano di studio e simulazione.
- Criticita: nessun overflow effettivo; restano da validare le fonti mobili richiamate dai bandi.

### M-FL01 - Capitoli 1-14

- Punti di forza: corpus completo con teoria, casi e strumenti per profili diversi.
- Criticita: le fonti locali restano da validare.

### M-FL02 - Capitoli 1-12

- Punti di forza: sequenza completa da ordinamento a laboratorio.
- Criticita: restano da validare bandi regionali e di area vasta.

### M-FL03 - Capitoli 1-5

- Punti di forza: testi completi e laboratorio coerente con fonti istituzionali.
- Criticita: il campione non sostituisce il bando specifico.

### M-FL04 - Capitoli 1-15

- Punti di forza: fonti-base ufficiali ricontrollate e struttura workbook uniforme.
- Criticita: materia ad alta sensibilita normativa e locale, da validare umanamente.

### Parte finale - Capitolo 50

- Punti di forza: simulazione integrata e Diario degli errori.
- Criticita: durata, criteri e formato devono seguire il bando effettivo.

## 5. Coerenza globale

- Terminologia: coerente nella distinzione tra nucleo comune, delta locale, verticale e rinvio.
- Struttura vs indice: l'inventario coincide con cinquanta capitoli; la preview aggregata contiene sessanta sezioni, comprese aperture e front matter.
- Promesse dell'introduzione mantenute: si, per la presenza didattica; non ancora per la pubblicazione definitiva.

## 6. Contenuto da verificare

- Validazione umana dei testi vigenti, delle discipline regionali e locali e delle formule normative puntuali.
- Bandi, allegati, rettifiche, prove e criteri della singola procedura.
- Validazione umana delle norme, dei bandi e delle fonti locali.

## 7. Suggerimenti facoltativi (non errori)

- Separare le griglie piu dense in schede A4 compilabili.
- Usare il capitolo 50 come benchmark per ogni successiva simulazione di modulo.

## 8. Priorita degli interventi

1. Eseguire la validazione normativa e redazionale umana, esclusa da questo ciclo.
2. Ricalibrare ogni laboratorio sul bando destinatario.

## 9. Giudizio di pubblicabilita

Non pubblicabile allo stato attuale.

Motivazione: i controlli automatici di struttura, fonti e rendering sono stati svolti e non rilevano difetti A4 effettivi, ma resta la validazione umana obbligatoria. I nuclei `parziale` della matrice non possono essere promossi a `completo` senza tale chiusura.

## 10. Limiti di questa revisione

La verifica e' automatica e documentale; non equivale a parere legale, a proofreading umano, a validazione dei bandi o a collaudo di un PDF tipografico definitivo. La firma umana e' stata esclusa su richiesta dell'utente.
