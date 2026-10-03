# Revisione dell’impaginato corrente — VOL-09

## 1. Sintesi

Prova del 3 ottobre 2026: **267 pagine**, 14 capitoli e 73 nuclei. Interno tecnico revisionato; servizi digitali e dati editoriali comuni restano dipendenze aperte. Nessun signoff 24.

PDF SHA-256: `8dd41fc17e9e2cf638e8b1e3279a1f679b68243fb624853fa620ac9b99cb9097`.

## 2. Punti di forza

Il volume Appalti, PNRR e procurement conserva la progressione dei capitoli, gli apparati e i casi del freeze testuale. L’indice distingue capitoli e nuclei e porta alle pagine effettive. Le tabelle dense sono leggibili per gruppi collegati; nessuna riduzione del corpo è stata usata per accorciare il volume.

## 3. Interventi verificati

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P09-01 | Tabella, p. 13 | Formattazione | grave | Tabella Markdown non resa nella prova storica. | Tabella completa con nove righe, intestazioni e celle leggibili. | Corretto e verificato localmente |
| P09-02 | Quiz, pp. 106–107,157,212–213 | Gerarchia | medio | Titoli interferivano con le alternative. | Unità domanda/alternative/soluzione distinte e continue. | Corretto e verificato localmente |
| P09-03 | Sezione 13.1, p. 227 | Residui interni | medio | N-TR02-XX-04 visibile al lettore. | Titolo descrittivo e numerazione 13.1 nel PDF. | Corretto e verificato localmente |
| P09-04 | Kit 14.6, pp. 265–267 | Apparati | grave | Promesse di appendici non presenti. | Rinvii puntuali ai capitoli e schede effettive; promessa riallineata. | Corretto e verificato localmente |
| P09-05 | Indice, pp. 6–7 | Tipografia | medio | Indice troppo piccolo. | Corpo 9,5 pt e 87 destinazioni verificate. | Corretto e verificato localmente |
| P09-06 | Tabelle nel volume | Continuità | medio | Frammenti sulla stessa pagina. | Intestazioni regolari e gruppi semantici collegati senza perdita di righe. | Corretto e verificato localmente |
| P09-07 | Scheda affidamento, p. 266 | Refuso | medio | Segno+ univa Controlli svolti e Risorse. | Eliminato il segno e separati i due campi in paragrafi; delta verificato nel nuovo PDF. | Corretto e verificato localmente |

## 4. Macrostruttura e completezza

Presenti tutti i 14 master e i 73 nuclei attesi. Il payload esportabile, gli snapshot e gli hash del freeze sono conservati nel pacchetto. Confrontati 33 file del freeze con le sorgenti correnti: nessuna divergenza non registrata. La revisione testuale integrale e le correzioni sostanziali restano documentate nel rapporto VOL-09.md; questa fase non dichiara una nuova rilettura parola per parola dell’intero manuale.

## 5. Contenuti, figure e rinvii

Il kit 14.6 alle pp. 265–267 ricolloca gli strumenti necessari nei capitoli e aggiunge schede compilabili: non vengono dichiarate cinque appendici autonome inesistenti. Il Gantt a p. 240 distingue percorso critico A–B–D–F, nove giorni lavorativi e margine di un giorno per C/E; la tabella seguente esplicita i valori. Il delta finale corregge i due campi della scheda senza cambiare norme o casi.

La verifica grafica non certifica nuovamente ogni norma o fonte. I delta testuali di produzione sono tracciati separatamente con copie precedenti e confronto degli hash; quiz e casi restano quelli verificati dal responsabile testuale, salvo le correzioni puntuali esplicitate sopra.

## 6. Tipografia e geometria

Formato 6,69×9,61 pollici,481,92×691,92 pt. Corpo Garamond circa 11 pt; tabelle e indice circa 9,5 pt. Font incorporati; zero overflow DOM, testo oltre pagina, glifi sostitutivi e immagini mancanti. Conteggio DOM e PDF coincidente. Le continuazioni normali di tabella possono attraversare il foglio con intestazione ripetuta; non sono confuse con la frammentazione patologica storica.

## 7. Secondo controllo e copertura

Tutte le 17 tavole contatto della release (267 pagine) e 13 pagine ingrandite, elencate nel registro visuale. Tutte le 267 pagine confrontate a scala 1.8; 266 identiche alla release esaminata, sola 266 cambiata e vista ingrandita. Le tavole contatto verificano ritmo, densità, salti e geometria; non equivalgono alla lettura di ogni parola del raster a piena risoluzione. L’estrazione diretta del PDF conferma tutte le 87 destinazioni d’indice (14 capitoli+73 nuclei). Registri geometrici e DOM coprono ogni pagina. Nessuna perdita di contenuto osservata nelle verifiche dichiarate.

## 8. Giudizio finale

**Non pubblicabile allo stato attuale per dipendenze editoriali comuni aperte.** Il candidato interno supera i controlli locali descritti. La promessa digitale di pagina 1 non è stata collaudata; dati editoriali commerciali, copertina, prova fisica e accettazione KDP non sono attestati. Step 21 resta in corso; 22–24 non chiusi da questo rapporto.

## 9. Produzione e artefatti

Il conteggio di 267 pagine rientra nel limite 828 per questo formato in nero su carta bianca, documentato nel fascicolo KDP di VOL-02 ([specifica ufficiale](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6)). Non occorre dividere l’interno o ridurre il carattere. Pacchetto: `delivery/VOL-09/candidate-2026-10-03/README.md`, con PDF, payload, snapshot, verifiche, registri e immagini di controllo. Nessun upload o pubblicazione eseguito.

## 10. Priorità residue

Risoluzione delle dipendenze comuni sul digitale e sui dati editoriali; eventuale aggiornamento del front matter e nuova verifica del delta; copertina e prova fisica; completamento dei gate nell’ordine del CLI. Le fonti normative restano quelle consolidate nei dossier testuali. Il PDF è un candidato revisionabile, non un file approvato alla pubblicazione.

### Chiusura tecnica aggiuntiva del 3 ottobre 2026

Il Gantt di p. 240 è stato renderizzato a 1950 × 1410 pixel dall’originale PDF vettoriale, senza interpolazione del vecchio raster. La risoluzione effettiva supera 370 ppi. Le altre 266 pagine sono identiche nel rendering; dati, calcolo e testo conservati.

Candidato corrente SHA-256 `8dd41fc17e9e2cf638e8b1e3279a1f679b68243fb624853fa620ac9b99cb9097`. Prova e confronto sono in `publication-refinements/` del pacchetto. Le verifiche anteriori restano evidenze storiche; la verifica del delta completa la copertura del nuovo candidato. Il giudizio sui servizi digitali, i dati editoriali e la pubblicabilità complessiva non cambia.
