# Revisione trasversale — M-FC03 Enti pubblici non economici

## 1. Executive Summary

La revisione ha considerato indice, premessa, tredici capitoli, sei appendici, matrice di copertura, piani e fonti. Il modulo segue una progressione leggibile: inquadra la famiglia EPNE, distingue INPS e INAIL, sviluppa i processi comuni applicati, passa agli strumenti concorsuali e chiude con appendici realmente operative. La promessa iniziale è mantenuta: il lettore riceve il delta specialistico senza una duplicazione integrale del VOL-01.

Il corpus legacy presentava quattro problemi trasversali: assenza del Formato 2, appendici troppo brevi, richiami redazionali nel corpo e ortografia con apostrofi sostitutivi degli accenti. Tutti sono stati corretti. I 95 nuclei risultano completi nella matrice; ogni testo ha almeno 3.000 parole, cinque nuclei da almeno 600 parole, sei quiz commentati, un caso ragionato e una verifica. Non restano errori strutturali, contenutistici o linguistici bloccanti.

## 2. Punti di forza

- forte orientamento a quiz, orale, casi e lettura del bando;
- distinzione costante fra regola stabile e dato mobile;
- capitoli INPS e INAIL complementari, non sovrapposti;
- raccordo efficace fra governance, procedimenti, risorse, performance e personale;
- appendici ora autonome e proporzionate alla funzione;
- matrice atomica e numerazione stabile delle appendici 14-19;
- voce professionale preservata durante il retrofit.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| TR-01 | Intero modulo | Struttura | Critico | Testi legacy privi di Nucleo ID, verifica strutturata e tracciabilità Formato 2. | Retrofit dei 19 testi e matrice v2 con 95 nuclei. | Corretto |
| TR-02 | Appendici A-F | Contenuto | Critico | Le appendici, soprattutto F, non erano autonome né sufficientemente sviluppate. | Ampliare teoria, distinzioni, casi, applicazioni e verifiche senza duplicare il VOL-01. | Corretto |
| TR-03 | Capitoli 02, 04, 06, 07, 09 e appendici | Autonomia | Importante | Il corpo richiamava source note, fonti consolidate o wiki come supporto per il lettore. | Trasferire la tracciabilità nel frontmatter e sviluppare direttamente l'informazione necessaria. | Corretto |
| TR-04 | Intero modulo | Lingua | Importante | Apostrofi usati al posto degli accenti e parole tronche non accentate. | Normalizzazione controllata del solo corpo, con seconda scansione indipendente. | Corretto |
| TR-05 | Scheda pipeline e matrice | Coerenza | Importante | Le appendici non avevano numerazione compatibile con Nucleo ID e filtro CLI. | Numerarle 14-19, aggiornare la scheda e correggere il resolver con test di regressione. | Corretto |
| TR-06 | Indice e front matter | Stato editoriale | Importante | Metadati ancora `source_ready` e promessa di futura review umana. | Allineare a testo finale e descrivere i controlli della pipeline. | Corretto |
| TR-07 | Verifiche dei capitoli | Ripetizione strutturale | Lieve | Il blocco finale usa una griglia ricorrente. | Mantenerlo come apparato intenzionale del Metodo BANDO; concetti e casi cambiano per capitolo. | Corretto |

## 4. Struttura, contenuto e coerenza

Non risultano capitoli fuori posto. Il passaggio da ordinamento a enti guida, quindi a processi comuni e infine a workbook, riduce i salti logici. Le appendici restano dopo il percorso principale perché servono selezione, orientamento o recupero lessicale. L'appendice F non promette una formazione professionale completa per assistente sociale: delimita esplicitamente il proprio perimetro.

Le terminologie vincolanti sono registrate nella Bibbia del Modulo. Non emergono contraddizioni fra previdenza, assicurazione, prevenzione, prestazione e servizio. Gli esempi non trasformano bandi storici o dati annuali in regole universali.

## 5. Stile, grammatica e leggibilità

La sintassi privilegia forme attive e conseguenze operative. Tabelle e checklist interrompono i passaggi più densi senza sostituire la teoria. La normalizzazione ha eliminato `e'`, `puo'`, `perche'`, `piu'` e le principali parole tronche prive di accento. La scansione successiva non ha trovato residui delle forme bersaglio. Lint e densità sono verdi su tutti i testi.

## 6. Ripetizioni e ridondanze globali

| Concetto ripetuto | Prima occorrenza | Altre occorrenze | Valutazione | Intervento consigliato |
|---|---|---|---|---|
| regola stabile / dato mobile | cap. 01 | cap. 10, 13; appendici C-D | utile | conservare come criterio del metodo |
| competenza / procedimento / evidenza | cap. 02 | cap. 05, 11-12; appendice A | utile | conservare, variando l'applicazione |
| previdenza / assicurazione | cap. 03 | cap. 04; appendice B | utile | mantenere il confronto esplicito |
| attività / output / risultato / impatto | cap. 07 | cap. 13; appendice F | tollerabile | mantenere solo nei contesti di misurazione |
| verifica finale in sei domande | cap. 01 | tutti i testi | utile | trattare come apparato ricorrente, non come prosa |

## 7. Esperienza del lettore

La premessa chiarisce subito per chi è il modulo e che cosa aggiunge. I punti più densi — bilancio, PIAO, contratti e materie integrative — sono sostenuti da mappe, casi ed errori tipici. Il ritmo accelera nei capitoli 10-13, coerentemente con il passaggio dalla teoria alla prova. La conclusione operativa è affidata al piano 30/60/90 e alle appendici, senza introdurre nuovi nuclei non spiegati.

## 8. Valutazione numerica

| Area | Voto | Motivazione |
|---|---:|---|
| Qualità complessiva | 8.7 | modulo completo, pratico e coerente |
| Struttura | 9.0 | progressione e confini chiari |
| Chiarezza | 8.8 | definizioni e applicazioni ben raccordate |
| Stile e fluidità | 8.4 | voce stabile; apparati intenzionalmente ricorrenti |
| Grammatica | 9.2 | normalizzazione e seconda scansione completate |
| Coerenza | 9.0 | lessico e rinvii governati dalla Bibbia |
| Approfondimento | 8.6 | adeguato ai profili dichiarati |
| Autorevolezza | 8.5 | fonti tracciate; audit specialistico dedicato a valle |
| Originalità | 8.3 | forte integrazione fra ente, bando e workbook |
| Leggibilità | 8.8 | paragrafi brevi e apparati distribuiti |
| Introduzione | 8.7 | promessa e pubblico espliciti |
| Conclusione | 8.8 | piano e appendici chiudono il percorso |
| Maturità editoriale | 8.8 | pronto per correzione e audit di modulo |

## 9. Errori individuati nel secondo controllo

Il secondo controllo ha individuato e chiuso: richiami redazionali residui nei capitoli 02, 04, 06, 07 e 09; sezioni di riferimenti interni rimaste in tre testi; numerazione non risolvibile delle appendici nel CLI; stati legacy di indice e front matter; accenti mancanti. Non risultano ulteriori errori bloccanti.

## 10. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori.**

La revisione trasversale non lascia nuclei bloccanti né errori gravi aperti. Prima del text freeze restano i gate ordinari già previsti: applicazione del presente report, audit specialistico finale e manifest di congelamento. Sono controlli automatici/editoriali di processo e non attività rinviate a una futura revisione umana.
