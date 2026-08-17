# Report editoriale — Diritto tributario e teoria dell'imposta

## 1. Sintesi editoriale
- Genere editoriale: manuale professionale e workbook per concorsi pubblici.
- Pubblico target: candidati ai profili di AE, ADM e AdER.
- Perimetro di questa revisione: capitolo 4 M-FC02, inclusi struttura, copertura v4, rinvii, fonti e asset.
- Stato generale in una frase: capitolo didatticamente completo e ben strutturato, pubblicabile dopo la rimozione di un marcatore editoriale interno e la review normativa già prevista.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: struttura; progressione; gerarchia; pubblicabilità; autonomia e coerenza del capitolo; coerenza con indice, matrice e capitoli richiamati; terminologia; completezza; definizioni; contenuto normativo; esempi; tabelle, box e schemi; fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente e sulla presenza fisica degli asset, poiché non era disponibile un PDF KDP renderizzato.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | `Livello 3 - Quadro UE fiscale, IVA e dogane` | Gerarchia e titolazione | Media | Il titolo introduce un “Livello 3” senza che nel capitolo esistano livelli 1 e 2. La numerazione appare come un marcatore di lavorazione e interrompe la gerarchia editoriale. | Rinominare il titolo in `Quadro UE fiscale, IVA e dogane`, salvo che i livelli 1-3 siano una classificazione esplicitata e applicata in modo coerente nell'intero modulo. | Proposto |
| V01 | Sezioni IRPEF/IRES, IVA e quadro UE; `Note di review` | Accuratezza normativa e fattuale | Media | Il capitolo dichiara correttamente che residenza, disciplina IVA, efficacia delle direttive e dati mobili richiedono controllo sul testo vigente e review specialistica. Tale verifica non risulta ancora chiusa nel frontmatter. | Eseguire la review umana tributaria/UE sulle fonti ufficiali al cut-off del volume e registrare data, perimetro ed esito; aggiornare poi `review_required`. | Da verificare |

## 4. Osservazioni per capitolo
### Capitolo 4 — Diritto tributario e teoria dell'imposta
- Punti di forza: progressione chiara dal fondamento costituzionale alla struttura del tributo; distinzione rigorosa tra presupposto, soggetto, base imponibile e obbligazione; quadro IRPEF/IRES e IVA autosufficiente al livello promesso; teoria UE e doganale ben raccordata; casi, quiz ed esercizi applicano concetti già spiegati; cinque figure presenti e collocate accanto alle sezioni pertinenti.
- Criticità: un titolo conserva una numerazione non spiegata; la review normativa specialistica resta aperta per scelta esplicita del capitolo.

## 5. Coerenza globale
- Terminologia: coerente con la matrice M-FC02, il Metodo BANDO e i capitoli specialistici richiamati.
- Struttura vs indice: coerente per contenuti e progressione; E01 riguarda soltanto la titolazione interna della sezione UE.
- Promesse dell'introduzione mantenute: sì. I nove nuclei assegnati risultano completi; esempi e verifiche non sostituiscono la teoria.
- Copertura v4 e rinvii: nessuna duplicazione impropria del nucleo comune; i rinvii ai capitoli 5, 5A, 5B, 6, 7, 8 e 11 sono specifici e le destinazioni risultano presenti. Non è necessario aggiornare la matrice.

## 6. Contenuto da verificare
- Testo vigente del D.P.R. 917/1986 e disciplina applicabile a soggetti, residenza, categorie reddituali e formazione del reddito.
- Testo vigente del D.P.R. 633/1972 e disciplina UE applicabile a territorialità, esenzioni, detrazione, inversione contabile e decorrenze.
- Condizioni ed effetti dell'eventuale efficacia diretta delle direttive nella formulazione destinata alla pubblicazione.
- Dati mobili eventualmente introdotti nelle fasi successive: aliquote, soglie, scaglioni, importi, termini e regimi.
- Resa delle cinque figure e delle tabelle nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare nel text freeze se uniformare il titolo `Neutralita' come meccanismo, non come risultato assoluto` al registro nominale degli altri sottoparagrafi.
- Conservare fuori dal nucleo stabile aliquote, soglie e termini soggetti a variazione, come già previsto dal capitolo.

## 8. Priorità degli interventi
1. Chiudere la review normativa tributaria/UE sulle fonti ufficiali al cut-off.
2. Risolvere la titolazione segnalata in E01.
3. Ispezionare figure, tabelle, box e rinvii nel render KDP.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: la struttura e la copertura didattica sono solide e non presentano nuclei parziali, ma V01 richiede la review specialistica dichiarata dallo stesso capitolo prima della pubblicazione. E01 è un intervento editoriale circoscritto.

## 10. Limiti di questa revisione
La revisione ha coperto il testo, la matrice, i rinvii e la presenza fisica degli asset. Non ha svolto una nuova ricerca normativa esterna articolo per articolo e non ha ispezionato un PDF KDP renderizzato; il comando `chapter-lint` non è disponibile tra gli script del progetto, quindi la verifica locale è stata effettuata sul Markdown e sulle destinazioni dei collegamenti.
