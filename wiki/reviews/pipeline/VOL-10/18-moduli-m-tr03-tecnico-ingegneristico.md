# VOL-10 — Step 18: audit asset M-TR03, aggiornato al 3 ottobre 2026

| asset | problema | correzione | verifica nel Book Studio | esito |
| --- | --- | --- | --- | --- |
| Vincoli piani, p.28 | Figura assente nella prova storica; prima rasterizzazione a 247,6 ppi | Tavola didattica originale; rendering del PDF vettoriale a 371,4 ppi | Libertà e reazioni leggibili, nessun ritaglio; testo vicino distingue stabilità e conteggio | Verificato |
| Trave, p.31 | Diagrammi assenti; prima rasterizzazione a 247,6 ppi | Tavola con q=10 kN/m, L=4 m, R=20 kN; rendering a 371,4 ppi | V=20−10x e M=20x−5x²; massimo 20 kNm, segni e unità coerenti | Verificato |
| Planimetria D1, p.122 | Dossier storico senza documento effettivo; prima rasterizzazione a 247,6 ppi | Quote, percorso e zona non ispezionata; rendering a 371,4 ppi | Rettangolo 12×8, corridoio 12×2, aule 6×6; percorso P1–P3 leggibile | Verificato |
| F01, p.123 | Mancava immagine del caso | Illustrazione fotografica esplicitamente dichiarata, causa non accertata | 1536 px a 378 pt: 292,6 ppi effettivi; immagine e didascalia leggibili | Verificato visivamente; non attestati 300 ppi |
| Tabelle e formule native | Frammentazione e notazione storiche | Riflusso comune e tabelle collegate | pp.39, 79–80, 124–126 viste ingrandite | Verificato |

Seconda passata: tutte le otto tavole contatto della release di 127 pagine e dodici ingrandimenti. Nuovo PDF confrontato a scala 1,8: cambiano soltanto le pagine 28, 31, 122, tutte riviste ingrandite. Zero overflow e asset mancanti.

I tre PDF sorgenti contengono rispettivamente 54, 87 e 89 tracciati vettoriali, senza immagini raster. Il nuovo rendering preserva composizione e testi, senza interpolare bitmap; originali, hash e dimensioni sono documentati in VOL-10-vector-render-delta.json. La foto resta intatta, con risoluzione effettiva dichiarata. Non eseguite prova cartacea o accettazione KDP. Dipendenze editoriali comuni aperte.
