# Report editoriale — M-TR01 ICT e trasformazione digitale

## 1. Sintesi editoriale
- Genere editoriale: manuale specialistico-workbook per concorsi pubblici.
- Pubblico target: candidati a profili ICT, cyber, cloud/DevOps e data/AI nella PA.
- Perimetro di questa revisione: indice, premessa, matrice, capitoli 01-13 e coerenza trasversale.
- Stato generale in una frase: struttura, progressione e copertura risultano coerenti dopo le correzioni; restano interventi medi e le verifiche umane previste dagli step successivi.

## 2. Punti applicati della checklist
Applicati i punti 1-26 e 28-30, oltre al gate di copertura didattica integrale. Il punto 27 non è applicabile perché manca il PDF impaginato. La verifica normativa e specialistica finale resta assegnata allo step 15 e al text freeze.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | `index.md` | Indice/struttura | Grave | L'indice scaffold non rappresentava i 13 capitoli. | Ricostruito indice con cinque parti, 13 capitoli, premessa, confini e planning. | Risolto |
| E02 | ex `chapters/00-piano-editoriale.md` | Struttura | Grave | Il piano di lavoro compariva come falso capitolo 00. | Spostato in `planning/01-piano-editoriale.md`; `chapters/` contiene ora soltanto 01-13. | Risolto |
| E03 | Premessa | Promesse introduttive | Grave | Mancava una premessa editoriale verificabile. | Creata `front-matter/FM5-premessa.md` con promessa, percorso, confini e uso BANDO. | Risolto |
| E04 | Frontmatter capp. 01-13 | Coerenza metadati | Media | Gli stati storici dei capitoli non usano ancora un valore uniforme, benché i gate individuali siano conclusi. | Normalizzare nello step 14 senza rimuovere `review_required` prima della review umana. | Aperto |
| E05 | Capp. 06-12 | Verifica normativa/specialistica | Media | Le fonti sono consolidate e gli step 12 sono conclusi, ma la verifica di vigenza e specialistica resta necessaria prima del freeze. | Eseguire lo step 15 sulle fonti ufficiali e registrare esito e data. | Da verificare |
| E06 | Cap. 12 e indice | Rinvio cross-family | Media | M-TR02 è ancora incompleto e non può fungere da copertura sostitutiva. | Il nuovo indice lo qualifica espressamente come instradamento di catalogo; il cap. 12 resta autonomo sul delta ICT. | Risolto |
| E07 | Intero modulo | Coerenza terminologica | Media | Mancava una Bibbia che assegnasse i concetti trasversali ai capitoli proprietari. | Creata `planning/03-bibbia-modulo.md`. | Risolto |
| E08 | Capp. 01-13 | Uniformità apparati | Media | Le funzioni didattiche sono presenti con heading non sempre identici. | Uniformare dove utile nello step 14, preservando gli adattamenti funzionali. | Proposto |
| E09 | `index.md` | Stato editoriale | Media | Lo stato del modulo era fermo allo scaffold. | Aggiornato a `reviewed-draft` / `cross-reviewed`, mantenendo la review richiesta. | Risolto |
| E10 | Tabelle, SQL, checklist | Layout | Lieve | La resa paperback non è verificabile dal Markdown. | Eseguire il gate visuale sul composito KDP. | Da verificare |

## 4. Osservazioni per capitolo
### Capitolo 1 — Lavorare come ICT nella PA
- Punti di forza: orienta da profilo, bando e output.
- Criticità: nessuna grave residua.
### Capitolo 2 — Informatica specialistica
- Punti di forza: delimita correttamente il delta dal VOL-01.
- Criticità: normalizzare il frontmatter con gli altri capitoli.
### Capitolo 3 — Programmazione, algoritmi e strutture dati
- Punti di forza: prepara le dipendenze dei capitoli successivi.
- Criticità: validazione specialistica finale prevista allo step 15.
### Capitolo 4 — Basi dati, SQL/NoSQL e qualità
- Punti di forza: progressione completa da modello a controlli.
- Criticità: il confine con cap. 10 è ora fissato nella Bibbia.
### Capitolo 5 — Reti, sistemi e infrastrutture
- Punti di forza: basi funzionali a cloud e cyber.
- Criticità: verificare esercizi e resa grafica.
### Capitolo 6 — Software, API e interoperabilità PA
- Punti di forza: catena requisito-test-API-e-service coerente.
- Criticità: verifica vigente ModI/PDND allo step 15.
### Capitolo 7 — Cloud PA, container e DevOps
- Punti di forza: collega migrazione, operabilità e continuità.
- Criticità: verifica Cloud PA/ACN allo step 15.
### Capitolo 8 — Cybersecurity operativa
- Punti di forza: rischio, controlli e software supply chain ben distinti.
- Criticità: review cyber specialistica finale.
### Capitolo 9 — IAM e incident response
- Punti di forza: sequenza identità-accessi-evidenze-risposta.
- Criticità: verifica NIS2/CSIRT/privacy allo step 15.
### Capitolo 10 — Data governance e open data
- Punti di forza: distingue apertura, accesso, qualità e interoperabilità.
- Criticità: verifica versioni AgID/UE allo step 15.
### Capitolo 11 — AI/ML nella PA
- Punti di forza: integra dati, metriche, controllo umano e governance.
- Criticità: verifica AI Act e calendario applicativo allo step 15.
### Capitolo 12 — Procurement ICT
- Punti di forza: rende verificabili requisiti, SLA, sicurezza ed exit.
- Criticità: M-TR02 resta solo instradamento; review contratti allo step 15.
### Capitolo 13 — Laboratorio prove ICT
- Punti di forza: integra teoria e output in una simulazione mista.
- Criticità: validare soluzioni e rubriche prima del freeze.

## 5. Coerenza globale
- Terminologia: coerente; la Bibbia assegna definizioni primarie e applicazioni.
- Struttura vs indice: coerente dopo la ricostruzione dell'indice e lo spostamento del piano.
- Promesse dell'introduzione mantenute: sì; la premessa promette selezione dal bando, teoria specialistica e output presenti nei capp. 01-13.
- Copertura: la matrice registra 14 nuclei completi e un rinvio puntuale valido al VOL-01; nessun `parziale`, `solo-nominato` o `mancante`.
- Duplicazioni: il nucleo B-PA non è duplicato; M-TR02 non è usato come sostituto didattico.

## 6. Contenuto da verificare
- Vigenza di CAD/ModI/PDND, Cloud PA/ACN, NIS2, open data, AI Act e contratti pubblici.
- Accuratezza specialistica di query, pseudocodice, subnetting, metriche ML, quiz e rubriche.
- Resa del composito KDP e leggibilità di tabelle e blocchi tecnici.

## 7. Suggerimenti facoltativi (non errori)
- Aggiungere mappe di dipendenza per i lettori che seguono un percorso per sottoprofilo.
- Preparare nel capitolo 13 simulazioni distinte per generalista, cyber, cloud e data/AI.

## 8. Priorità degli interventi
1. Normalizzare metadati e apparati nello step 14.
2. Eseguire e registrare la review umana normativa e specialistica nello step 15.
3. Applicare il text freeze soltanto dopo la chiusura delle verifiche.
4. Controllare il composito paperback nei gate visuali.

## 9. Giudizio di pubblicabilità
**Pubblicabile dopo intervento medio.**
Motivazione: gli errori strutturali E01-E03 sono risolti e non restano errori gravi aperti. E04-E05 ed E08 richiedono gli interventi già previsti dagli step 14-15; il modulo non è ancora al text freeze.

## 10. Limiti di questa revisione
Revisione svolta sui Markdown e sulle evidenze dei gate individuali. Non sostituisce la review umana specialistica/normativa dello step 15 né l'ispezione del PDF impaginato. La memoria locale è stata usata come continuità operativa, non come fonte normativa.
