# Report editoriale — M-TR03 Tecnico-ingegneristico

## 1. Sintesi editoriale
- Genere editoriale: manuale-workbook specialistico per concorsi tecnici nella Pubblica Amministrazione.
- Pubblico target: candidati ingegneri, architetti/urbanisti, geometri/istruttori tecnici e specialisti di infrastrutture.
- Perimetro di questa revisione: intero modulo, comprendente indice, piano editoriale, 13 capitoli, matrice v4 e report individuali dello step 12.
- Stato generale in una frase: i capitoli presentano una progressione didattica coerente e una copertura senza nuclei bloccanti, ma l'apparato d'accesso del modulo è rimasto allo stato pre-scrittura e deve essere riallineato prima della pubblicazione.

## 2. Punti applicati della checklist
Applicati i punti 1-26 e 28-30: indice e struttura; progressione; gerarchia; idoneità; coerenza interna e trasversale; terminologia; completezza; definizioni; contenuto tecnico e normativo; esempi; box, tabelle e rinvii; fonti; sintassi, chiarezza, tono e stile; ripetizioni e contraddizioni; grammatica, ortografia, punteggiatura, refusi e uniformità grafica; layout testuale e leggibilità; qualità complessiva. Applicato inoltre il gate di copertura didattica integrale e la logica v4 comune/specialistico/verticale/rinvio. Il punto 27, impaginazione reale, non è applicabile in modo conclusivo perché non era disponibile un PDF impaginato da ispezionare.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | `index.md`, sezioni Perimetro, Capitoli di lavoro, Fonti da consolidare e Prossimo passo | Indice e corrispondenza struttura reale | Grave | L'indice dichiarava ancora il modulo `source-ready`, affermava che fonti e bandi erano da consolidare e non elencava i 13 capitoli effettivi. | Inserito l'indice ordinato 1-13, separato l'apparato editoriale e aggiornati stato e prossimo passo senza anticipare il text freeze. | Risolto |
| E02 | `chapters/00-piano-editoriale.md`, Struttura prevista e Testo editoriale | Promesse, completezza e struttura | Grave | Il file era presentato dall'indice come capitolo, sebbene fosse una specifica pre-scrittura con intenzioni non tutte confluite nel manoscritto. | Rimosso dall'indice pubblico e riclassificato come `editorial_plan`, `superseded`, `canonical: false`, `planning-snapshot`; aggiunta nota esplicita. Il contenuto storico è stato preservato. | Risolto |
| E03 | `index.md`, frontmatter e testo | Coerenza metadati | Media | `status`, `module_status`, `draft_stage`, tag e descrizione testuale erano fermi a `source-ready`. | Allineati a `editorial-review` e `module-review`, mantenendo aperte correzioni, review umana e preflight. | Risolto |
| E04 | Capp. 7-12, Note di review e rinvii interni | Richiami incrociati e coerenza temporale | Media | Più note dichiarano ancora che capitoli 9-12 “andranno consolidati dopo il completamento”, sebbene ora esistano. Nel corpo molti rinvii usano il solo numero di capitolo; sono comprensibili, ma meno robusti di titolo e heading. | Verificare tutte le destinazioni ora disponibili; sostituire le note temporanee e, nei passaggi critici, usare titolo e heading o wikilink puntuale. | Risolto |
| E05 | Cap. 1, profili e confini con VOL-02, VOL-09, VOL-11 e VOL-12 | Rinvii cross-family | Media | I confini di famiglia sono concettualmente corretti, ma alcuni rinvii esterni indicano soltanto il codice del volume. Non soddisfano ancora lo standard di destinazione precisa richiesto per un rinvio formativo. | Collegare ogni rinvio necessario a modulo/capitolo/sezione verificati; se la destinazione non è completa, formulare il passaggio come confine editoriale e non come rinvio didattico sostitutivo. | Risolto |
| E06 | Capp. 3-13 e report individuali step 12 | Accuratezza normativa e tecnica | Media | Restano aperte verifiche professionali e di vigenza su NTC, edilizia, urbanistica, Codice dei contratti, sicurezza, contabilità, ponti, BIM/GIS, catasto e casi integrati. Il testo è prudente e non presenta soglie inventate, ma tali verifiche sono espressamente richieste prima della pubblicazione. | Eseguire la review umana per competenza, fissare una data di cut-off normativa e chiudere ogni voce “da verificare” con fonte, esito e responsabile. | Da verificare |
| E07 | Tabelle e checklist nei capp. 4, 6-13 | Layout e impaginazione | Lieve | Le tabelle sono leggibili in Markdown, ma densità, larghezze e spezzature non sono state verificate nel formato KDP 6,69 × 9,61 in. | Eseguire il preflight PDF; convertire le tabelle troppo larghe in schede verticali senza ridurre il corpo tipografico. | Da verificare |

## 4. Osservazioni per capitolo
### Capitolo 1 — Il concorso tecnico nella PA: profili, enti e prove
- Punti di forza: introduce profili, bando, prove e confini di collana; orienta correttamente l'intero percorso.
- Criticità: i rinvii cross-family devono diventare destinazioni puntuali (E05).

### Capitolo 2 — Ufficio tecnico pubblico, responsabilità e atti tecnici
- Punti di forza: collega fatto, istruttoria, documento e decisione senza duplicare il diritto amministrativo generale.
- Criticità: verificare in chiusura il rinvio puntuale a VOL-01 e i modelli dell'ente (E06).

### Capitolo 3 — Scienza e tecnica delle costruzioni per concorsi
- Punti di forza: costruisce il lessico necessario prima di NTC e sismica; distingue resistenza, rigidezza, stabilità, duttilità e durabilità.
- Criticità: formule, segni, unità ed esercizi richiedono validazione strutturale (E06).

### Capitolo 4 — NTC, sismica, geotecnica e sicurezza strutturale
- Punti di forza: progressione prestazionale chiara e raccordo corretto con il capitolo 3 e il collaudo.
- Criticità: vigenza del pacchetto normativo e procedure territoriali restano da verificare (E06); controllare le tavole nel layout (E07).

### Capitolo 5 — Urbanistica e governo del territorio
- Punti di forza: distingue livelli di piano, conformità, vincoli, espropriazione e paesaggio.
- Criticità: la disciplina regionale e locale impone review dedicata e data di cut-off (E06).

### Capitolo 6 — Edilizia, SUE, titoli e vigilanza
- Punti di forza: mantiene il confine urbanistica-edilizia e usa rinvii interni già strutturati.
- Criticità: categorie, regimi, tolleranze, regolarizzazioni e modulistica richiedono verifica vigente (E06); tabelle da provare in pagina (E07).

### Capitolo 7 — Progettazione delle opere pubbliche
- Punti di forza: sequenza bisogno–DIP–PFTE–esecutivo–verifica–validazione leggibile e terminologicamente coerente.
- Criticità: rinvii e note temporanee da consolidare (E04); contenuti mobili del Codice da verificare (E06).

### Capitolo 8 — Direzione lavori, esecuzione e cantieri
- Punti di forza: distingue RUP, DL e CSE e collega tecnica, contabilità, modifiche e sicurezza.
- Criticità: attribuzioni puntuali e iniziative in materia di sicurezza richiedono validazione; note sui capitoli futuri sono superate (E04, E06).

### Capitolo 9 — Collaudo, verifica, manutenzione e gestione dell'opera
- Punti di forza: separa correttamente ultimazione, collaudo tecnico-amministrativo, regolare esecuzione, collaudo statico e gestione.
- Criticità: soglie, incompatibilità, effetti e periodicità devono essere verificati; rinvii temporanei da aggiornare (E04, E06).

### Capitolo 10 — Computi, capitolati e contabilità dei lavori
- Punti di forza: ricostruisce il flusso dalla lavorazione al conto finale e distingue i documenti.
- Criticità: prezzari, sicurezza, riserve e documenti contabili richiedono cut-off; il rinvio al capitolo 12 è ormai consolidabile (E04, E06).

### Capitolo 11 — Infrastrutture, viabilità, ponti e monitoraggio
- Punti di forza: collega opera, rete, rischio, ispezione, monitoraggio e decisione senza inventare soglie.
- Criticità: atti ANSFISA, classificazioni e poteri cautelari richiedono review specialistica; aggiornare il rinvio al capitolo 12 (E04, E06).

### Capitolo 12 — BIM, GIS, rilievi, catasto e patrimonio pubblico
- Punti di forza: usa il ciclo del dato come filo unitario e mantiene distinti catasto, pubblicità immobiliare e stato legittimo.
- Criticità: disciplina BIM, standard geomatici, procedure catastali e raccordi contabili restano mobili (E06).

### Capitolo 13 — Laboratorio delle prove tecniche
- Punti di forza: integra otto forme di output e una simulazione finale, applicando teoria già insegnata.
- Criticità: casi, calcoli, profili e condizioni della singola procedura richiedono validazione professionale; densità visuale da verificare (E06, E07).

## 5. Coerenza globale
- Terminologia: sostanzialmente coerente; la Bibbia del Modulo fissa RUP, responsabile del procedimento, DL, CSE, verifica, validazione, collaudo e stato dei luoghi. Non sono emerse contraddizioni centrali fra capitoli.
- Struttura vs indice: la progressione reale 1-13 è logica, ma non è rappresentata dall'indice pubblico (E01). Il piano 00 non deve essere confuso con un capitolo editoriale finito (E02).
- Promesse dell'introduzione mantenute: profili, prove, materie specialistiche, casi, checklist e laboratorio sono coperti. Non risulta invece sviluppata come strumento autonomo la promessa “Piano 30/60/90 giorni specifico” del piano pre-scrittura (E02).
- Copertura v4: 16 nuclei censiti, 15 `completo` e 1 `rinviato` con destinazioni precise in VOL-01; nessun `parziale`, `solo-nominato` o `mancante`.
- Duplicazioni: il modulo applica il nucleo comune e non replica sistematicamente VOL-01. I confini con VOL-08, VOL-09 e VOL-11 sono corretti nell'impianto; i rinvii devono essere resi puntuali (E05).
- Equilibrio teoria/workbook: equilibrato nei capitoli 1-12; il capitolo 13 svolge correttamente la funzione di integrazione e allenamento.

## 6. Contenuto da verificare
- Vigenza e campo di applicazione di NTC, Circolare, emendamenti e disciplina delle costruzioni esistenti.
- Disciplina nazionale, regionale e locale di urbanistica, edilizia, titoli, tolleranze, regolarizzazioni e vigilanza.
- D.Lgs. 36/2023 e allegati applicabili a progettazione, verifica, esecuzione, contabilità e collaudo.
- Titolo IV del D.Lgs. 81/2008, attribuzioni e iniziative dei soggetti della sicurezza.
- Codice della strada, norme geometriche, Linee guida ponti e istruzioni ANSFISA.
- BIM, standard e interoperabilità; RNDT/INSPIRE; procedure catastali; inventario e contabilità patrimoniale.
- Realismo professionale, calcoli, unità e adeguatezza dei casi ai quattro profili.
- Corrispondenza dei rinvii esterni con destinazioni complete e aggiornate.

## 7. Suggerimenti facoltativi (non errori)
- Inserire nell'indice una mappa visuale delle quattro traiettorie di profilo, purché resti leggibile in bianco e nero.
- Aggiungere una pagina finale “Quale capitolo ripassare dopo ogni errore” collegata al Diario degli errori del capitolo 13.
- Valutare una breve legenda unica degli acronimi tecnici per la versione cartacea.

## 8. Priorità degli interventi
1. Riallineare indice e piano editoriale al manoscritto reale, risolvendo E01 ed E02.
2. Correggere metadati e rinvii temporanei o generici, risolvendo E03-E05.
3. Eseguire e documentare la review normativa e professionale indicata in E06.
4. Effettuare il preflight PDF/KDP e risolvere E07.

## 9. Giudizio di pubblicabilita
Pubblicabile dopo intervento medio.
Motivazione: E01 ed E02, inizialmente gravi, sono stati risolti preservando il documento storico di pianificazione. La copertura didattica non presenta nuclei bloccanti. Restano da correggere rinvii e note temporanee (E04-E05), da chiudere le verifiche normative e professionali diffuse (E06) e da eseguire il preflight visuale (E07); il modulo non è quindi ancora pronto per la consegna finale.

## 10. Limiti di questa revisione
La revisione ha esaminato i file Markdown, la matrice e i report individuali; non ha ispezionato un PDF impaginato né verificato articolo per articolo tutte le fonti normative alla data di pubblicazione. Le verifiche specialistiche elencate nella sezione 6 richiedono professionisti competenti e fonti ufficiali vigenti. Non sono state simulate prove su un bando specifico diverso dal corpus consolidato.
