# Report editoriale - M-TR01, Capitolo 08: Cybersecurity operativa

## 1. Sintesi editoriale
- Genere editoriale: manuale specialistico per concorsi pubblici italiani.
- Pubblico target: candidati ICT che studiano senza documentazione interna.
- Perimetro di questa revisione: capitolo 08, matrice Format 2, confini con VOL-01 e capitoli 7, 9 e 12.
- Stato generale in una frase: sei nuclei autosufficienti insegnano il rischio cyber in modo difensivo, con caso, laboratorio e sei risposte commentate; i controlli tecnici mobili restano esplicitamente assegnati agli audit automatici successivi.

## 2. Punti applicati della checklist
Applicati i punti 1-5 per struttura e gerarchia; 6-15 per coerenza, completezza, definizioni, contenuto tecnico, caso, tabelle e riferimenti; 16-21 per sintassi, chiarezza, tono, stile e ripetizioni; 22-26 e 28-30 per lingua, uniformità grafica, leggibilità e qualità editoriale. Il punto 27 non è applicabile: non è disponibile un PDF impaginato. Eseguito anche il test dello studente e il controllo di copertura v4: nessuna promessa formativa dipende da wiki, report o materiali interni.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Domanda da commissario | Accuratezza concettuale | Media | La risposta modello accostava controlli e rischio inerente nella stessa fase. | Sequenza corretta in: rischio inerente, controlli, trattamento, rischio residuo, riesame. | Applicato |
| E02 | Gerarchia N-TR01-08-02 | Gerarchia Markdown | Media | Era presente l'heading spurio `### 0`. | Heading rimosso e struttura ricontrollata. | Applicato |
| E03 | Aggiunte retrofit, nuclei 01-06 | Ortografia e uniformità | Media | Le integrazioni omettevano in modo diffuso gli accenti italiani. | Eseguito proofread completo e ripristinati gli accenti senza modificare termini tecnici o fonti. | Applicato |
| V01 | N-TR01-08-04, NIST CSF | Quadro tecnico mobile | Media | Edizioni e indicazioni operative dei framework possono cambiare dopo il cut-off del volume. | Riesaminare fonte ufficiale e cut-off nello step 15. | Da verificare allo step 15 |
| V02 | N-TR01-08-05, CVE/CWE/CVSS e priorità | Tracciabilità tecnica | Media | Il testo distingue i ruoli correttamente, ma il lessico operativo e le versioni richiedono controllo specialistico al cut-off. | Rieseguire audit automatico su fonti primarie e termini vigenti. | Da verificare allo step 15 |
| V03 | N-TR01-08-06, secure SDLC e filiera | Tracciabilità tecnica | Media | Supply chain, attestazioni e pratiche di sviluppo possono variare per standard e contesto applicativo. | Rieseguire audit automatico application security e supply-chain security. | Da verificare allo step 15 |
| V04 | Quadro italiano ACN/NIS2 | Contenuto normativo mobile | Media | Il capitolo evita di trasformare NIST e OWASP in obblighi italiani, ma il raccordo italiano deve essere controllato alla data di pubblicazione. | Verificare le fonti ufficiali ACN e NIS2 nello step 15. | Da verificare allo step 15 |

## 4. Osservazioni per capitolo
### Capitolo 08 - Cybersecurity operativa
- Punti di forza: la progressione da asset e scenario a trattamento, controllo, vulnerabilità e filiera è coerente. I sei nuclei superano la soglia Format 2; la verifica contiene caso guidato, laboratorio e sei risposte commentate. La distinzione fra minaccia, vulnerabilità, evento, impatto e rischio resta costante.
- Criticità: le verifiche V01-V04 non sono errori didattici aperti. Sono debiti tecnici reali, registrati senza confonderli con lo stato di copertura della matrice, che dovranno essere chiusi dagli audit automatici degli step 13-18.

## 5. Coerenza globale
- Terminologia: coerente; rischio inerente e residuo, CVE/CWE/CVSS, controllo preventivo/detective/compensativo e SBOM restano distinti.
- Struttura vs indice: coerente con il capitolo 08; VOL-01 e capitoli 7, 9 e 12 sono usati come confini di materia, non come sostituti della spiegazione.
- Promesse dell'introduzione mantenute: sì, sul piano didattico e dell'output concorsuale.

## 6. Contenuto da verificare
- Quadro ACN/NIS2 vigente al cut-off del text freeze.
- Versioni e terminologia ufficiale di NIST CSF, SSDF, CVSS e OWASP Top 10.
- Fonti primarie e limiti di applicazione per vulnerability management, software supply chain e SBOM.

## 7. Suggerimenti facoltativi (non errori)
- Nell'impaginato finale, tenere la matrice 3x3 e il laboratorio su pagine con spazio sufficiente per la compilazione manuale.

## 8. Priorità degli interventi
1. Chiudere V01-V04 con gli audit automatici specialistici previsti dagli step 13-18.
2. Riesaminare i riferimenti mobili al nuovo cut-off prima del text freeze.
3. Eseguire l'audit visivo quando sarà disponibile il PDF impaginato.

## 9. Giudizio di pubblicabilità
Pubblicabile con correzioni minori.
Motivazione: il capitolo supera i controlli di struttura, densità, copertura e citazioni; non restano errori gravi aperti nel testo. Il giudizio non sostituisce gli audit specialistici, i gate successivi o la conferma umana obbligatoria dello step 24.

## 10. Limiti di questa revisione
La revisione ha esaminato Markdown, matrice e fonti già consolidate. Non ha verificato l'impaginazione PDF, non ha simulato una revisione umana e non ha chiuso gli audit automatici specialistici successivi.