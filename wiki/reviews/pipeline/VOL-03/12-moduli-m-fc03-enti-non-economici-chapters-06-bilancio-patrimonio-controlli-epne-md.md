# Report editoriale — Bilancio, patrimonio e controlli negli EPNE

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici.
- Pubblico target: candidati a profili amministrativi, economici e contabili negli enti pubblici non economici.
- Perimetro di questa revisione: capitolo 06 M-FC03, matrice didattica, indice e piano del modulo, con raccordo a VOL-01 e ai capitoli 02, 05 e 07.
- Stato generale in una frase: capitolo autonomo e didatticamente completo; applicate due correzioni testuali e una correzione di tracciabilità nella matrice.

## 2. Punti applicati della checklist
Applicati i punti 1-26 e 28-30: indice, struttura, progressione, gerarchia, pubblicabilità, autonomia, raccordi, terminologia, completezza, definizioni, accuratezza concettuale e normativa, esempi, tabelle, apparato delle fonti, sintassi, chiarezza, tono, didattica, ripetizioni, contraddizioni, grammatica, ortografia, punteggiatura, refusi, uniformità grafica, layout Markdown, leggibilità e qualità complessiva. Applicati inoltre copertura v4, test dello studente e gate di copertura didattica integrale sui sei Nuclei ID.

Il punto 27 non è applicabile: non era disponibile un PDF impaginato sul quale verificare margini, spezzature, pagine e resa tipografica.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | N-FC03-06-06, risposta modello | Accuratezza delle definizioni | Media | La formula “il bilancio rappresenta e autorizza” presentava l'effetto autorizzatorio come uniforme per ogni documento e ogni EPNE. | Subordinare l'effetto autorizzatorio alla disciplina applicabile. | Applicato |
| E02 | Matrice didattica, righe N-FC03-06-02..05 | Apparato delle fonti | Media | Quattro richiami usavano tre slug di source note inesistenti e quindi non garantivano tracciabilità verificabile. | Sostituirli con le source note consolidate effettivamente presenti e dichiarate dal capitolo. | Applicato |
| E03 | N-FC03-06-05, sistemi contabili | Coerenza terminologica | Lieve | La prima spiegazione usava “ricavi”, mentre il seguito adottava “proventi” per la stessa prospettiva economico-patrimoniale. | Uniformare il termine in “proventi”. | Applicato |

Non risultano errori oggettivi gravi residui. Le verifiche normative e i suggerimenti autoriali sono separati nelle sezioni 6 e 7.

## 4. Osservazioni per capitolo
### Capitolo 06 — Bilancio, patrimonio e controlli negli EPNE
- Punti di forza: progressione dai principi ai documenti dell'ente, quindi ciclo finanziario, patrimonio, sistemi contabili e controlli esterni; sei nuclei riconoscibili; esempi, tabelle, caso ragionato, esercizio e quiz coerenti con la teoria.
- Criticità: nessuna criticità grave o media residua dopo E01-E03. Le attribuzioni specifiche di Corte dei conti, RGS e amministrazioni vigilanti richiedono comunque l'audit specialistico previsto.
- Test dello studente: superato. Senza frontmatter e strumenti interni restano definizioni, funzioni, distinzioni, conseguenze, sequenze operative, casi e verifiche.
- Copertura didattica: N-FC03-06-01..06 completi; strumenti e quiz applicano contenuti già spiegati e non sostituiscono la teoria.

## 5. Coerenza globale
- Terminologia: coerente dopo E03. Preventivo, rendiconto, competenza, cassa, patrimonio, inventario, consegnatario, agente contabile, controllo interno, controllo esterno e vigilanza restano distinti.
- Struttura vs indice: coerente. Titolo e contenuto corrispondono all'indice studente e al piano editoriale del modulo.
- Promesse dell'introduzione mantenute: sì. I cinque obiettivi sono sviluppati nei nuclei e ripresi da mappa, caso, esercizio e verifica.
- Copertura v4: il capitolo applica al contesto EPNE la contabilità pubblica generale di VOL-01 senza duplicarla integralmente; contratti avanzati, PNRR specialistico e performance restano nei percorsi indicati.
- Rinvii: i richiami al libro base e ai capitoli adiacenti sono leggibili e circoscritti; non risultano dipendenze del corpo da wiki, dashboard, source note o report interni.

## 6. Contenuto da verificare
- Verificare allo step 15 l'applicabilità e il testo vigente del D.P.R. 27 febbraio 2003, n. 97, del D.Lgs. 31 maggio 2011, n. 91 e dei regolamenti contabili propri degli enti considerati.
- Verificare sulle fonti ufficiali vigenti le funzioni di controllo della Corte dei conti applicabili agli EPNE, distinguendole dagli istituti propri degli enti territoriali.
- Verificare sul portale RGS/MEF perimetro, poteri, flussi e terminologia relativi a vigilanza e controllo su enti e organismi pubblici.
- Verificare per INAIL denominazioni, collocazione e versioni correnti di PIAO, bilancio preventivo, bilancio consuntivo e relativi allegati.
- Verificare disciplina e qualifiche di economi, consegnatari e agenti contabili nel perimetro dei singoli enti, inclusi obblighi di conto e responsabilità.
- Verificare sul quadro vigente di contratti e tracciabilità l'uso delle formulazioni relative a CIG, CUP, fondi vincolati, PNRR e UE.

## 7. Suggerimenti facoltativi (non errori)
- In impaginazione, valutare la divisione delle tabelle più dense se le colonne risultano strette nel formato paperback.
- Nel giro finale di bozze, uniformare gli apostrofi usati al posto degli accenti secondo la convenzione tipografica del volume.
- Uniformare graficamente i blocchi “Micro-caso”, “Caso ragionato”, “Domanda da commissario”, “Domanda-trappola”, “Errore tipico” e “▣ Verifica” nella revisione trasversale.

## 8. Priorità degli interventi
1. Eseguire l'audit normativo specialistico dello step 15.
2. Verificare nello step 13 il raccordo con governance, procedimenti, performance e contratti.
3. Controllare la resa delle tabelle nel PDF impaginato.
4. Uniformare la superficie tipografica nell'ultimo giro di bozze.

## 9. Giudizio di pubblicabilità
Pubblicabile con correzioni minori.

Motivazione: E01-E03 sono applicati; non restano errori gravi, nuclei parziali, promesse formative scoperte o dipendenze da strumenti interni. Il giudizio resta subordinato all'audit specialistico e al preflight previsti dalla pipeline.

## 10. Limiti di questa revisione
La revisione ha riguardato il Markdown, non un PDF impaginato. Non è stata svolta una verifica web autonoma delle norme, dei regolamenti dei singoli enti o delle pagine istituzionali correnti: questi controlli appartengono allo step 15. La coerenza trasversale sarà nuovamente verificata quando tutti i capitoli e le appendici M-FC03 avranno completato il ciclo editoriale.
