# Report editoriale — Accertamento, controlli e compliance fiscale

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici, modulo specialistico M-FC02.
- Pubblico target: candidati ai profili Agenzia delle Entrate e ACFI.
- Perimetro di questa revisione: capitolo 05, matrice di copertura M-FC02 e VOL-03, rinvii interni, fonti consolidate e asset dichiarati.
- Stato generale in una frase: capitolo didatticamente completo e strutturalmente solido, pubblicabile dopo la verifica normativa al cut-off e il ripristino o la rimozione degli asset mancanti.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: struttura; progressione; gerarchia; pubblicabilità; autonomia e coerenza interna; coerenza con capitoli collegati e matrici; terminologia; completezza; definizioni; contenuto normativo; esempi; tabelle, box e schemi; apparato delle fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente Markdown: non era disponibile un PDF KDP renderizzato. È stato applicato anche il gate di copertura didattica integrale e la verifica v4 dei rinvii cross-family.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Frontmatter, `asset_refs` | Note, richiami, tabelle, box e schemi | Media | I cinque file PNG dichiarati in `asset_refs` non risultano presenti nei percorsi indicati. Il capitolo promette quindi un apparato visivo che il repository non può attualmente rendere. | Generare o recuperare i cinque asset nei percorsi dichiarati; in alternativa rimuovere i riferimenti se l'apparato visivo non appartiene più al progetto editoriale. | Aperto |
| V01 | Contraddittorio, autotutela, adempimento collaborativo e profili ACFI | Accuratezza normativa e fattuale | Media | Il capitolo contiene correttamente richiami alla verifica del testo vigente, ma la review normativa finale al cut-off non risulta chiusa nel frontmatter. | Verificare sulle fonti ufficiali vigenti art. 6-bis L. 212/2000, D.P.R. 600/1973, D.Lgs. 128/2015, disciplina dell'autotutela e fonti ACFI; registrare data, perimetro ed esito della review. | Da verificare |
| E02 | Prima di `Profili ACFI` e `Caso guidato` | Layout Markdown | Lieve | Due titoli H2 seguivano il paragrafo precedente senza riga vuota, riducendo la robustezza del rendering Markdown. | Inserire una riga vuota prima dei due titoli. | Applicato |

## 4. Osservazioni per capitolo
### Capitolo 05 — Accertamento, controlli e compliance fiscale
- Punti di forza: progressione chiara dal dato alla selezione, dall'istruttoria all'atto e dalla tutela alla riscossione; distinzione efficace tra compliance ordinaria e adempimento collaborativo; raccordo completo tra bilancio, dichiarazione e audit fiscale; blocco ACFI selettivo ma autosufficiente; casi, quiz, griglie e checklist applicano nozioni già spiegate.
- Criticità: gli asset del frontmatter sono assenti; la natura mobile della disciplina richiede la review normativa finale già prevista dalle note del capitolo.

## 5. Coerenza globale
- Terminologia: coerente con M-FC02, con la matrice del modulo e con il registro del Metodo BANDO.
- Struttura vs indice: coerente; la gerarchia H1/H2/H3 è regolare e le due separazioni Markdown mancanti sono state corrette.
- Promesse dell'introduzione mantenute: sì. I sette obiettivi trovano spiegazione, applicazione e verifica nel capitolo.
- Copertura v4 e rinvii: i nuclei su accertamento, garanzie, tutela, compliance, ACFI e audit fiscale risultano completi o rinviati con destinazioni precise. Le sezioni di destinazione nei capitoli 4, 5B, 6 e 11 esistono. Non emergono duplicazioni improprie del VOL-01 né nuclei `parziale`, `solo-nominato` o `mancante` attribuibili a questo capitolo; non è necessario aggiornare le matrici.

## 6. Contenuto da verificare
- Testo vigente dell'art. 6-bis della L. 212/2000, atti esclusi, termini ed effetti dell'omissione del contraddittorio.
- Disposizioni applicabili del D.P.R. 600/1973 sui poteri istruttori e sui metodi di accertamento.
- Presupposti e limiti dell'autotutela obbligatoria e facoltativa e disciplina vigente degli strumenti deflativi richiamati.
- Requisiti, soglie, certificazioni ed effetti del regime disciplinato dal D.Lgs. 128/2015.
- Testi vigenti di TUIR, convenzioni applicabili, decreto MEF e riferimenti OCSE per residenza, stabile organizzazione e transfer pricing.
- Resa editoriale di tabelle e box nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare, durante il text freeze, se distribuire il blocco ACFI in più pagine o box per evitare eccessiva densità nel formato paperback.
- Se gli asset saranno prodotti, collocarli accanto alle sezioni didattiche corrispondenti e verificarne leggibilità in bianco e nero.

## 8. Priorità degli interventi
1. Chiudere la review normativa tributaria e ACFI sulle fonti ufficiali al cut-off.
2. Ripristinare i cinque asset dichiarati oppure riallineare il frontmatter.
3. Ispezionare tabelle, box, rinvii e immagini nel render KDP.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: struttura, progressione e copertura didattica non presentano lacune bloccanti; tuttavia V01 richiede la verifica normativa finale e E01 lascia incompleto l'apparato visivo dichiarato. E02 è già stato risolto.

## 10. Limiti di questa revisione
La revisione ha coperto il capitolo, le matrici, l'esistenza delle fonti consolidate, le destinazioni dei rinvii e la presenza fisica degli asset. Non ha eseguito una nuova verifica normativa esterna articolo per articolo e non ha ispezionato un PDF KDP renderizzato. Il giudizio sull'impaginazione resta quindi limitato al Markdown.
