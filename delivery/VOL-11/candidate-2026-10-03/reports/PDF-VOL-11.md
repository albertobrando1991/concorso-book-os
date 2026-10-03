# Revisione dell’impaginato corrente — VOL-11

## 1. Sintesi

Prova del 3 ottobre 2026: **253 pagine**, 14 capitoli e 90 nuclei. Interno tecnico revisionato; servizi digitali e dati editoriali comuni restano dipendenze aperte. Nessun signoff 24.

PDF SHA-256: `eb67bedb161968004879438a2dad8ce37d86f4deb7d53d40f7e8db9d2c41b425`.

## 2. Punti di forza

Il volume Ambiente, protezione civile e sostenibilità conserva la progressione dei capitoli, gli apparati e i casi del freeze testuale. L’indice distingue capitoli e nuclei e porta alle pagine effettive. Le tabelle dense sono leggibili per gruppi collegati; nessuna riduzione del corpo è stata usata per accorciare il volume.

## 3. Interventi verificati

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P11-01 | Matrici, pp. 149,167,184,206–207,225,227 | Tabelle | grave | Nove/undici colonne spezzavano parole e sigle. | Gruppi collegati fino a quattro colonne; intestazione Responsabile / funzione ora va a capo tra parole. | Corretto e verificato localmente |
| P11-02 | Dati operativi, pp. 91,179–180,191 | Residui interni | medio | ID e istruzioni audit apparivano nel testo pubblico. | ID conservati nel frontmatter strutturato e rimossi dal corpo; fonti, date e limiti leggibili. | Corretto e verificato localmente |
| P11-03 | Appendici A–E, pp. 247–250 | Apparati | grave | Appendici promesse assenti nella prova storica. | Inserite schede operative di protezione civile, energia, ambiente locale, registri e toolkit; esaminate tutte. | Corretto e verificato localmente |
| P11-04 | Indice, pp. 6–8 | Tipografia | medio | Indice a 6,75 pt. | Corpo minimo 9,5 pt e 104 destinazioni verificate. | Corretto e verificato localmente |
| P11-05 | Matrice conclusiva, p. 149 | Continuità | medio | Frammentazione patologica e parole troncate. | Due proiezioni semantiche collegate dalla colonna Fatto; righe e intestazioni integre. | Corretto e verificato localmente |
| P11-06 | Appendice B, p. 248 | Calcolo e unità | medio | 30.000×0,25=7,5 t ometteva la conversione kg/t. | Esplicitati kWh,kg/kWh e divisione per 1.000; formula ricalcolata e PDF ricontrollato. | Corretto e verificato localmente |

## 4. Macrostruttura e completezza

Presenti tutti i 14 master e i 90 nuclei attesi. Il payload esportabile, gli snapshot e gli hash del freeze sono conservati nel pacchetto. Confrontati 30 file del freeze con le sorgenti correnti: nessuna divergenza non registrata. La revisione testuale integrale e le correzioni sostanziali restano documentate nel rapporto VOL-11.md; questa fase non dichiara una nuova rilettura parola per parola dell’intero manuale.

## 5. Contenuti, figure e rinvii

Le appendici A–E sono realmente presenti alle pp. 247–250 come schede operative nel capitolo 14. Le matrici dense sono suddivise in gruppi collegati per la stessa chiave. Due codici DO sono stati tolti dalla pagina pubblica e conservati nei metadati audit con fonte, ambito, versione, data e posizione. L’appendice B esplicita il divisore 1.000 nella conversione 7.500 kg=7,5 t.

La verifica grafica non certifica nuovamente ogni norma o fonte. I delta testuali di produzione sono tracciati separatamente con copie precedenti e confronto degli hash; quiz e casi restano quelli verificati dal responsabile testuale, salvo le correzioni puntuali esplicitate sopra.

## 6. Tipografia e geometria

Formato 6,69×9,61 pollici,481,92×691,92 pt. Corpo Garamond circa 11 pt; tabelle e indice circa 9,5 pt. Font incorporati; zero overflow DOM, testo oltre pagina, glifi sostitutivi e immagini mancanti. Conteggio DOM e PDF coincidente. Le continuazioni normali di tabella possono attraversare il foglio con intestazione ripetuta; non sono confuse con la frammentazione patologica storica.

## 7. Secondo controllo e copertura

Tutte le 16 tavole contatto della release (253 pagine) e 17 pagine ingrandite, elencate nel registro visuale. 253 pagine confrontate a scala 1.8: 246 identiche alla release esaminata,7 cambiate e tutte viste ingrandite. Le tavole contatto verificano ritmo, densità, salti e geometria; non equivalgono alla lettura di ogni parola del raster a piena risoluzione. L’estrazione diretta del PDF conferma tutte le 104 destinazioni d’indice (14 capitoli+90 nuclei). Registri geometrici e DOM coprono ogni pagina. Nessuna perdita di contenuto osservata nelle verifiche dichiarate.

## 8. Giudizio finale

**Non pubblicabile allo stato attuale per dipendenze editoriali comuni aperte.** Il candidato interno supera i controlli locali descritti. La promessa digitale di pagina 1 non è stata collaudata; dati editoriali commerciali, copertina, prova fisica e accettazione KDP non sono attestati. Step 21 resta in corso; 22–24 non chiusi da questo rapporto.

## 9. Produzione e artefatti

Il conteggio di 253 pagine rientra nel limite 828 per questo formato in nero su carta bianca, documentato nel fascicolo KDP di VOL-02 ([specifica ufficiale](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6)). Non occorre dividere l’interno o ridurre il carattere. Pacchetto: `delivery/VOL-11/candidate-2026-10-03/README.md`, con PDF, payload, snapshot, verifiche, registri e immagini di controllo. Nessun upload o pubblicazione eseguito.

## 10. Priorità residue

Risoluzione delle dipendenze comuni sul digitale e sui dati editoriali; eventuale aggiornamento del front matter e nuova verifica del delta; copertina e prova fisica; completamento dei gate nell’ordine del CLI. Le fonti normative restano quelle consolidate nei dossier testuali. Il PDF è un candidato revisionabile, non un file approvato alla pubblicazione.
