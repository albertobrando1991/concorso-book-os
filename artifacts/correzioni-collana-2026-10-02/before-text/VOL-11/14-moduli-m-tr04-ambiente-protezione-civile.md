# Report di correzione editoriale — VOL-11 / M-TR04

## 1. Sintesi editoriale

Lo step 14 applica e ricontrolla tutte le correzioni obbligatorie del report trasversale. Gli interventi preservano voce, struttura didattica e riferimenti; non introducono nuove affermazioni normative. I passaggi ampliati hanno superato nuovamente copertura, Humanizer conservativo e micro-revisione.

## 2. Punti applicati della checklist

- Rimossi duplicati strutturali e blocchi seriali.
- Ripristinata la codifica UTF-8 e la gerarchia dei titoli.
- Uniformati titoli, termini vincolanti e confini cross-volume.
- Ricontrollati tutti i nuclei modificati con il gate di densità.
- Verificati ritmo, leggibilità, sintassi, punteggiatura e naturalezza dei nuovi passaggi.
- Preservati casi, quiz, riferimenti e source reference.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| S13-E01 | Cap. 01 | Struttura/ripetizioni | Grave | Seconda sequenza duplicata. | Eliminare la sola sequenza ripetuta. | risolto |
| S13-E02 | Cap. 03 | Codifica/gerarchia | Grave | Mojibake e livelli di titolo incoerenti. | Ripristinare UTF-8 e H1/H2. | risolto |
| S13-E03 | Indici e Bibbia | Perimetro | Grave | Appendici promesse ma non previste. | Allineare al perimetro effettivo di 14 capitoli. | risolto |
| S13-E04 | Cap. 02 | Gerarchia/copertura | Grave | Heading fuso e nucleo insufficiente. | Correggere heading e integrare teoria. | risolto |
| S13-E05 | Cap. 02 | Ripetizioni/stile | Importante | Paragrafi identici in nuclei diversi. | Sostituire le copie con approfondimenti specifici. | risolto |
| S13-E06 | Cap. 01 e indici | Rinvii | Importante | Rinvii di collana non abbastanza precisi. | Trasformarli in confini editoriali espliciti. | risolto |
| S13-E07 | Cap. 06-14 | Uniformità | Importante | H1 e titoli non canonici. | Uniformare a «Capitolo XX — Titolo». | risolto |
| S13-E08 | Cap. 01-14 | Tracciabilità | Importante | Metadata non omogenei. | Allineare lo stato editoriale al gate effettivamente raggiunto. | risolto allo step 15 |
| S13-E09 | Cap. 06 e 11 | Terminologia | Importante | Varianti `d.lgs.` e `IT-alert`. | Applicare `D.Lgs.` e `IT-Alert`. | risolto |

## 4. Registro operativo delle correzioni

| ID | file modificato | correzione | fonte/evidenza | stato finale |
|---|---|---|---|---|
| S13-E01 | `chapters/01-quattro-profili-mappa-sistema.md` | Rimossa la seconda sequenza dopo i riferimenti. | Cinque soli ID N-TR04-01; gate copertura superato. | risolto |
| S13-E02 | `chapters/03-via-vas-valutazioni-ambientali.md` | Riparazione UTF-8, un solo H1 e sei nuclei H2. | Ricerca mojibake negativa; gate copertura superato. | risolto |
| S13-E03 | index, indice analitico, Bibbia e matrice | Rimosse promesse prive di target. | Scheda pipeline: perimetro 01-14. | risolto |
| S13-E04 | `chapters/02-dlgs-152-mase-ispra-snpa.md` | Separato heading; sviluppata teoria autonoma. | Gate copertura superato. | risolto |
| S13-E05 | stesso capitolo 02 | Una sola spiegazione generale; riprese rese specifiche. | Nessun blocco identico residuo; sei nuclei sopra soglia. | risolto |
| S13-E06 | cap. 01 e indici | Rinvii resi confini di collana. | Nessuna destinazione o appendice inventata. | risolto |
| S13-E07 | capitoli 06-14 | Titoli e H1 canonici. | Corrispondenza con indice e scheda pipeline. | risolto |
| S13-E08 | frontmatter capitoli 01-14 | Stato finale aggiornato dopo audit specialistico. | Verifica frontmatter allo step 15. | risolto allo step 15 |
| S13-E09 | capitoli 06 e 11 | Terminologia normalizzata. | Ricerca finale delle varianti. | risolto |

## 5. Coerenza globale

La correzione non altera la progressione del modulo. I nuclei mantengono scopo distinto; le riprese di casi ricorrenti sono funzionali e non seriali; i confini con gli altri volumi sono chiari. Non risultano contraddizioni o rinvii interni irrisolti.

## 6. Contenuto da verificare

L’audit specialistico dello step 15 resta responsabile delle fonti mobili: RENTRI/FIR, IT-Alert, qualità dell’aria, CER/TIAD, incentivi, atti attuativi e varianti territoriali. Queste voci non sono errori editoriali aperti.

## 7. Suggerimenti facoltativi (non errori)

- Valutare eventuali diagrammi solo sul PDF, se conservano leggibilità.
- Non ampliare il perimetro con appendici non previste.

## 8. Priorità degli interventi

1. Audit specialistico documentato.
2. Freeze e manifest aggiornato.
3. Preflight del PDF di consegna.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori già applicate.** Tutti gli errori editoriali gravi e importanti rilevati sono chiusi. Le verifiche successive riguardano certificazione specialistica e produzione, non lacune ancora presenti nel manoscritto.

## 10. Limiti della revisione

Lo step 14 non sostituisce il fact-check specialistico né il controllo visivo dell’impaginato. Entrambi sono eseguiti nei gate successivi.
