# Report editoriale — Informatica specialistica: cosa serve oltre il VOL-01

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale specialistico per concorsi pubblici.
- Pubblico target: candidati a profili di funzionario ICT nella pubblica amministrazione.
- Perimetro di questa revisione: capitolo 02, matrice di copertura e rinvii pubblicabili.
- Stato generale in una frase: capitolo autosufficiente e didatticamente completo; i due rilievi oggettivi emersi sono stati corretti.

## 2. Punti applicati della checklist
Sono stati applicati i punti 1-26 e 28-30 della checklist: gerarchia e coerenza con il piano del modulo; progressione; autonomia del capitolo; terminologia; completezza e accuratezza; esempi, tabelle, quiz e riferimenti; sintassi, chiarezza, tono, ripetizioni e contraddizioni; grammatica, ortografia, punteggiatura, refusi, uniformità grafica, layout Markdown, leggibilità e qualità complessiva. È stato applicato anche il gate di copertura didattica integrale sui sei Nucleo ID.

Il punto 27 non è applicabile: non era disponibile un PDF impaginato da ispezionare. Il punto 1 è stato verificato nel perimetro osservabile, confrontando titolo, collocazione del capitolo e piano editoriale; non costituisce un nuovo audit dell'intero indice di volume.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | N-TR01-02-02, «Dal bit all'informazione» | Uniformità grafica e chiarezza | Media | Le espressioni `(n)`, `(2^n)` e `(2^4=16)` apparivano come parentesi ordinarie e rendevano ambigua la notazione. | Usare notazione monospaziata: `n`, `2^n`, `2^4 = 16`. | risolto |
| E02 | «Riferimenti professionali essenziali» | Apparato bibliografico | Media | La formula «documentazione tecnica istituzionale» non permetteva al lettore di riconoscere i riferimenti effettivamente usati. | Nominare RISC-V ISA Manual, IEEE 754-2019, Unicode Standard/UTR #17, documentazione Linux e SPEC CPU. | risolto |

## 4. Osservazioni per capitolo
### Capitolo 02 — Informatica specialistica: cosa serve oltre il VOL-01
- Punti di forza: sei nuclei con progressione coerente; distinzione netta dai prerequisiti del VOL-01; esempi tecnici comprensibili; diagnosi guidata; verifica unica ben collocata; quiz commentati che controllano concetti già spiegati.
- Criticità: nessuna criticità grave o media residua nel testo. Le semplificazioni tecniche su ciclo di istruzione, cache, interrupt e parallelismo restano correttamente demandate agli audit specialistici successivi della pipeline.

## 5. Coerenza globale
- Terminologia: coerente per CPU, registri, bus, codifica, cache, latenza, throughput, processo e sistema operativo.
- Struttura vs indice: il capitolo occupa la collocazione prevista e rispetta il formato 2 con sei nuclei.
- Promesse dell'introduzione mantenute: sì. Le sette capacità dichiarate nell'obiettivo trovano spiegazione nei nuclei e controllo nella verifica.

## 6. Contenuto da verificare
- Nessuna voce normativa da verificare: il capitolo non contiene norme, scadenze o soglie giuridiche.
- Gli audit specialistici successivi dovranno confermare le semplificazioni tecniche e la stabilità delle edizioni documentali indicate nel frontmatter.

## 7. Suggerimenti facoltativi (non errori)
- Valutare in fase di impaginazione se la tabella sulla gerarchia di memoria richieda una larghezza colonna dedicata.
- Valutare nel test finale con lettori se mantenere entrambi gli esercizi oltre ai sei quiz; i due formati verificano abilità diverse e non sono ridondanti sul piano didattico.

## 8. Priorità degli interventi
1. Nessun errore grave o medio residuo.
2. Eseguire l'audit specialistico automatico previsto dalla pipeline.
3. Controllare resa della tabella e dei box sul PDF impaginato.

## 9. Giudizio di pubblicabilita
Pubblicabile con correzioni minori.

Motivazione: i rilievi E01 ed E02 sono risolti; la copertura dei sei nuclei è completa, il capitolo supera il test dello studente e non presenta dipendenze dal wiki nel corpo. Restano soltanto controlli specialistici e di impaginazione previsti dagli step successivi.

## 10. Limiti di questa revisione
La revisione riguarda il Markdown e la coerenza con matrice e piano del modulo. Non è stato ispezionato un PDF impaginato. Non sono stati rieseguiti confronti esterni sulle versioni correnti delle fonti tecniche, perché lo step usa le fonti consolidate del repository; la loro stabilità sarà controllata negli audit successivi.
