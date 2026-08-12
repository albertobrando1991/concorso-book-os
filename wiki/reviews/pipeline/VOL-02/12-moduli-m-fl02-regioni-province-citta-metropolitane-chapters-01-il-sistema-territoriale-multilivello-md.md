# Report editoriale — Il sistema territoriale multilivello

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici.
- Pubblico target: candidati a profili amministrativi, legislativi, tecnici e fondi di Regioni ed enti di area vasta.
- Perimetro di questa revisione: M-FL02, capitolo 01, con confronto su indice, capitolo 02, matrice didattica e contratto di volume.
- Stato generale in una frase: capitolo autonomo, completo nel perimetro introduttivo e pubblicabile con le verifiche normative e visive previste dagli step successivi.

## 2. Punti applicati della checklist
Applicati i punti 1-26 e 28-30 della checklist: indice e gerarchia, struttura, progressione, coerenza interna e trasversale, terminologia, completezza, definizioni, correttezza concettuale e normativa per quanto verificabile sulle fonti consolidate, esempi, tabelle, apparato normativo, sintassi, chiarezza, tono, stile didattico, ripetizioni, contraddizioni, grammatica, ortografia, punteggiatura, refusi, uniformità grafica, layout markdown e leggibilità. Applicato anche il gate di copertura didattica integrale sui sette Nucleo ID.

Il punto 27, impaginazione reale, non è applicabile: in questo step è disponibile il markdown, non il PDF impaginato. La resa delle cinque immagini è verificabile solo in preflight o nel Book Studio.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E12-01 | N-FL02-01-02 | Ortografia | Lieve | «disparita» era privo dell'accento finale. | Correggere in «disparità». | risolto |
| E12-02 | N-FL02-01-02, Figura 18.3 | Layout/richiamo | Lieve | Il link usava uno slug accentato non corrispondente al file ASCII presente negli asset. | Usare `03-sussidiarieta-differenziazione-adeguatezza.png`. | risolto |

## 4. Osservazioni per capitolo
### Capitolo 01 — Il sistema territoriale multilivello
- Punti di forza: sette nuclei con progressione chiara; distinzione efficace tra ente, livello, ufficio, funzione e competenza; strumenti operativi coerenti con il Metodo BANDO; sei quiz commentati e due casi; cinque figure distribuite accanto ai contenuti pertinenti.
- Criticità: nessuna criticità grave o media aperta. Gli esempi restano volutamente generali e devono essere adattati al bando concreto senza inventare competenze o atti territoriali.
- Test dello studente: superato. Senza frontmatter e senza accesso agli strumenti interni, il testo conserva definizioni, distinzioni, conseguenze, applicazioni, errori tipici, esercizi e riferimenti normativi leggibili.
- Copertura integrale: N-FL02-01-01/07 risultano `completo`; la matrice corrisponde al testo e non usa quiz o casi al posto della teoria.

## 5. Coerenza globale
- Terminologia: coerente nell'uso di autonomia, competenza, funzione, area vasta, programmazione, gestione e controllo.
- Struttura vs indice: titolo e funzione corrispondono all'indice dettagliato v4; il capitolo prepara i capp. 02, 03 e 09 senza duplicarne il contenuto analitico.
- Promesse dell'introduzione mantenute: sì. Il lettore può distinguere i livelli, applicare sussidiarietà/differenziazione/adeguatezza, leggere un bando M-FL02 e costruire una mappa livello-funzione-atto-controllo.
- Copertura v4: rispettato il delta specialistico M-FL02; il testo non replica la trattazione comunale di M-FL01 e non invade altre famiglie.

## 6. Contenuto da verificare
- Ricontrollare automaticamente, nello step 15, il testo vigente della Costituzione e della legge 7 aprile 2014, n. 56.
- Per un bando riferito a un territorio specifico, verificare statuto, legge regionale, regolamenti e assetto organizzativo dell'ente prima di attribuire una competenza o un atto puntuale.
- Ispezionare nel preflight la leggibilità delle Figure 18.1-18.5 nel formato editoriale di collana.

## 7. Suggerimenti facoltativi (non errori)
- Nessuno in questo ciclo: ulteriori esempi territoriali avrebbero senso soltanto se collegati a un bando target ufficiale e aggiornato.

## 8. Priorità degli interventi
1. Eseguire l'audit normativo automatico del modulo nello step 15.
2. Verificare la resa delle figure nel preflight del volume.
3. Evitare modifiche stilistiche non necessarie che possano riaprire i gate di densità o citazione.

## 9. Giudizio di pubblicabilità
Pubblicabile con correzioni minori.
Motivazione: i due errori lievi E12-01 ed E12-02 sono risolti; non restano errori gravi o medi, tutti i nuclei sono completi e i gate di densità e citazione passano. Restano le verifiche normative automatiche e il controllo visivo previsti a valle dalla pipeline.

## 10. Limiti di questa revisione
La revisione ha esaminato il markdown e gli asset path, non un PDF impaginato. Non sostituisce l'audit specialistico automatico dello step 15 né la verifica trasversale del modulo. Non sono state introdotte valutazioni su discipline regionali specifiche, perché il capitolo non è legato a un singolo bando territoriale.
