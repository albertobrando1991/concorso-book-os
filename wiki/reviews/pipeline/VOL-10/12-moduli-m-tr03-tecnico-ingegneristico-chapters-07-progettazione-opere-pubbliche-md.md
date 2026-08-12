# Report editoriale — Capitolo 07, Progettazione di opere pubbliche

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook specialistico per concorsi pubblici tecnici.
- Pubblico target: candidati ingegneri, geometri, funzionari tecnici e specialisti di infrastrutture.
- Perimetro di questa revisione: capitolo 07 in Formato 2, indice del modulo, Bibbia M-TR03, matrice e delta di copertura, piano, fonti consolidate e raccordi con i capitoli 02, 05-06 e 08-12.
- Stato generale in una frase: capitolo autosufficiente, completo nel perimetro specialistico assegnato e pubblicabile; nessun errore resta aperto.

## 2. Punti applicati della checklist

Applicati tutti i punti 1-26 e 28-30: corrispondenza con indice e Bibbia; struttura, gerarchia e progressione; autonomia; coerenza interna e trasversale; terminologia; completezza; definizioni; accuratezza concettuale e normativa; casi, tabelle e apparato; sintassi, chiarezza, tono, stile, ripetizioni, grammatica, ortografia, punteggiatura, refusi, uniformità grafica, layout Markdown e leggibilità. Applicati anche copertura v4, gate di copertura didattica integrale e test dello studente senza frontmatter né accesso al wiki. Il punto 27 non è applicabile: il PDF sarà controllato negli step di produzione.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Struttura complessiva | Copertura didattica | Grave | La versione legacy non rispettava nuclei, densità, quiz e verifiche del Formato 2. | Sviluppare sei nuclei autosufficienti, sei quiz commentati, verifiche vicine e casi applicativi. | Risolto step 09-10 |
| E02 | Nuclei 01-06 | Stile e sintassi | Lieve | Restavano contrasti meccanici, simmetrie e formule enfatiche. | Applicare una doppia passata Humanizer preservando significato e riferimenti. | Risolto step 11 |
| E03 | Raccordi con capitoli 08-12 | Coerenza tra capitoli | Media | Il report legacy considerava provvisorie le destinazioni successive. | Verificare esistenza, titolo e perimetro dei capitoli richiamati. | Risolto: destinazioni presenti e coerenti |
| E04 | Frontmatter | Stato editoriale | Lieve | Lo stato dichiarava ancora scrittura in corso e revisione richiesta. | Allineare `draft_stage` e `review_required` all'esito del presente controllo. | Corretto |

Non restano errori oggettivi aperti.

## 4. Osservazioni per capitolo

### Capitolo 07 — Progettazione di opere pubbliche

- Punti di forza: architettura chiara dal bisogno alla validazione; distinzione netta fra quadro esigenziale e DIP, PFTE ed esecutivo, verifica, validazione e approvazione; elaborati letti per funzione e coerenza, non come elenco; casi realistici senza soglie inventate; confini precisi con affidamento, esecuzione, contabilità e gestione informativa.
- Criticità: nessuna criticità testuale residua. I sei nuclei superano la soglia di densità; verifiche, quiz e casi applicano teoria già spiegata.

## 5. Coerenza globale

- Terminologia: coerente con la Bibbia M-TR03 per RUP, quadro esigenziale, DIP, PFTE, progetto esecutivo, verifica, validazione e approvazione.
- Struttura vs indice: titolo, collocazione e perimetro coincidono con l'indice; i sei Nucleo ID corrispondono alla checklist Format 2 della matrice.
- Promesse dell'introduzione mantenute: sì. Il capitolo insegna a ricostruire il percorso dal fabbisogno all'esecutivo, distinguere i documenti, riconoscere i soggetti e separare controllo, atto del RUP e approvazione.
- Copertura v4: completa nel delta specialistico M-TR03. Non duplica il procedimento generale del capitolo 02 né la disciplina di affidamento di VOL-09; i raccordi con urbanistica, edilizia, esecuzione, collaudo, computi e BIM restano interfacce dichiarate.
- Test dello studente: superato. Rimosso il frontmatter, il lettore dispone di definizioni, funzioni, inquadramento, distinzioni, conseguenze, esempi, metodo di verifica e strumenti per la prova.

## 6. Contenuto da verificare

Nessuna voce aperta nel perimetro didattico trattato. La source note specialistica, verificata editorialmente il 29 luglio 2026 sul testo ufficiale consolidato del D.Lgs. n. 36/2023, sostiene gli articoli 15, 37 e 41-43 e gli Allegati I.2, I.5, I.7 e I.9 richiamati. Il capitolo evita soglie, deroghe, requisiti quantitativi ed elenchi analitici mobili. Il controllo automatico di vigenza e del riparto funzionale resta previsto allo step 15 prima del text freeze.

## 7. Suggerimenti facoltativi (non errori)

- Valutare nell'appendice dei lavori pubblici una scheda verticale `documento → domanda → controllo → output`, senza duplicare la teoria.
- Nell'impaginazione, mantenere vicini la domanda-trappola e il passaggio che distingue verifica e validazione.

## 8. Priorità degli interventi

1. Nessun intervento testuale obbligatorio.
2. Eseguire l'audit automatico specialistico previsto dalla pipeline prima del text freeze.
3. Verificare tabelle, spezzature e leggibilità nel PDF di produzione.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori.** Le attività residue appartengono agli audit automatici e al preflight del volume, non alla revisione del contenuto. Copertura Format 2, densità, citation guard, autonomia didattica e coerenza dei raccordi sono superate; la tabella errori non contiene rilievi aperti.

## 10. Limiti della revisione

La revisione riguarda Markdown, matrice, delta, piano, Bibbia e fonti nazionali consolidate. Non certifica un progetto concreto né sostituisce l'applicazione del Codice, degli allegati e delle discipline settoriali al singolo intervento. Il PDF non è ancora disponibile; impaginazione, overflow, contrasto e resa KDP saranno verificati negli step successivi.
