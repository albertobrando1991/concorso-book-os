# Revisione dell’impaginato corrente — VOL-10

## 1. Sintesi

Prova del 3 ottobre 2026: **127 pagine**, 13 capitoli e 88 nuclei. Interno tecnico revisionato; servizi digitali e dati editoriali comuni restano dipendenze aperte. Nessun signoff 24.

PDF SHA-256: `411517d20e00cb3d077f04cde986b98a07d44d41c6955f830d8d4861605e425c`.

## 2. Punti di forza

Il volume Tecnico-ingegneristico conserva la progressione dei capitoli, gli apparati e i casi del freeze testuale. L’indice distingue capitoli e nuclei e porta alle pagine effettive. Le tabelle dense sono leggibili per gruppi collegati; nessuna riduzione del corpo è stata usata per accorciare il volume.

## 3. Interventi verificati

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P10-01 | Figure pp. 28,31,122–123; dossier pp. 121–126 | Completezza visuale | grave | Mancavano diagrammi e documenti effettivi del caso. | Quattro figure e dossier con dati, consegna, elaborato modello e griglia; corrispondenza figura/testo verificata. | Corretto e verificato localmente |
| P10-02 | Tabelle, pp. 79–80 e 125–126 | Continuità | medio | Frammenti e intestazioni ripetute nella prova storica. | Continuazioni regolari tra pagine con intestazione, contenuti integri e celle leggibili. | Corretto e verificato localmente |
| P10-03 | Tre tavole, pp. 28,31,122 | Risoluzione | medio | Prima rasterizzazione a 247,6 ppi effettivi. | Rendering dei PDF vettoriali a 371,4 ppi; composizione immutata e tre pagine ricontrollate. | Corretto e verificato localmente |

## 4. Macrostruttura e completezza

Presenti tutti i 13 master e i 88 nuclei attesi. Il payload esportabile, gli snapshot e gli hash del freeze sono conservati nel pacchetto. Confrontati 18 file del freeze con le sorgenti correnti: nessuna divergenza non registrata. La revisione testuale integrale e le correzioni sostanziali restano documentate nel rapporto VOL-10.md; questa fase non dichiara una nuova rilettura parola per parola dell’intero manuale.

## 5. Contenuti, figure e rinvii

Quattro immagini alle pp. 28,31,122,123. Le tre tavole sono state renderizzate da PDF realmente vettoriali, con 54/87/89 tracciati e zero bitmap: 1950 pixel, circa 371,4 ppi alla dimensione effettiva. La fotografia illustrativa conserva 292,6 ppi, valore dichiarato senza attestare 300 ppi o interpolare l’immagine. Planimetria e caso distinguono misure, discordanza documentale, zona non ispezionata e causa non accertata; la soluzione calcola 36 m²,864 euro e differenza 144 euro.

La verifica grafica non certifica nuovamente ogni norma o fonte. I delta testuali di produzione sono tracciati separatamente con copie precedenti e confronto degli hash; quiz e casi restano quelli verificati dal responsabile testuale, salvo le correzioni puntuali esplicitate sopra.

## 6. Tipografia e geometria

Formato 6,69×9,61 pollici,481,92×691,92 pt. Corpo Garamond circa 11 pt; tabelle e indice circa 9,5 pt. Font incorporati; zero overflow DOM, testo oltre pagina, glifi sostitutivi e immagini mancanti. Conteggio DOM e PDF coincidente. Le continuazioni normali di tabella possono attraversare il foglio con intestazione ripetuta; non sono confuse con la frammentazione patologica storica.

## 7. Secondo controllo e copertura

Tutte le 8 tavole contatto della release (127 pagine) e 12 pagine ingrandite, elencate nel registro visuale. 127 pagine confrontate a scala 1.8; 124 identiche alla release esaminata; 3 cambiate e viste ingrandite. Le tavole contatto verificano ritmo, densità, salti e geometria; non equivalgono alla lettura di ogni parola del raster a piena risoluzione. L’estrazione diretta del PDF conferma tutte le 101 destinazioni d’indice (13 capitoli+88 nuclei). Registri geometrici e DOM coprono ogni pagina. Nessuna perdita di contenuto osservata nelle verifiche dichiarate.

## 8. Giudizio finale

**Non pubblicabile allo stato attuale per dipendenze editoriali comuni aperte.** Il candidato interno supera i controlli locali descritti. La promessa digitale di pagina 1 non è stata collaudata; dati editoriali commerciali, copertina, prova fisica e accettazione KDP non sono attestati. Step 21 resta in corso; 22–24 non chiusi da questo rapporto.

## 9. Produzione e artefatti

Il conteggio di 127 pagine rientra nel limite 828 per questo formato in nero su carta bianca, documentato nel fascicolo KDP di VOL-02 ([specifica ufficiale](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6)). Non occorre dividere l’interno o ridurre il carattere. Pacchetto: `delivery/VOL-10/candidate-2026-10-03/README.md`, con PDF, payload, snapshot, verifiche, registri e immagini di controllo. Nessun upload o pubblicazione eseguito.

## 10. Priorità residue

Risoluzione delle dipendenze comuni sul digitale e sui dati editoriali; eventuale aggiornamento del front matter e nuova verifica del delta; copertina e prova fisica; completamento dei gate nell’ordine del CLI. Le fonti normative restano quelle consolidate nei dossier testuali. Il PDF è un candidato revisionabile, non un file approvato alla pubblicazione.
