# Report editoriale — Capitolo 12: Logica, comprensione del testo e ragionamento

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook per concorsi pubblici italiani.
- Pubblico target: candidati generalisti, inclusi lettori con prerequisiti aritmetici da recuperare.
- Perimetro: integrazione aritmetica/frazioni/percentuali/proporzioni/medie, 18 quesiti A1–C6, tutte le 25 domande della mini-simulazione e coerenza dei passaggi collegati.
- Revisione indipendente in sola lettura svolta il 2 ottobre 2026. Tre rilievi comunicati all'autore sono stati corretti da quest'ultimo; la versione aggiornata è stata ricontrollata.
- Esito: le 43 chiavi di risposta sono corrette; nessun errore contenutistico o matematico residuo rilevato nel perimetro.
- Lint capitolo legacy e gate rinvii superati dopo correzione del titolo. Le sei source_refs esistono. Nessuna modifica di capitolo, matrice o run-state eseguita dal revisore.

## 2. Punti applicati della checklist

Applicati i punti 1–26 e 28–30 al perimetro testuale e ai collegamenti esaminati: struttura e progressione, autonomia, teoria prima degli esercizi, correttezza di definizioni/formule, casi, alternative, soluzioni, chiarezza, lessico, stile e superficie.

Punto 12: controllati i contenuti matematici e logici; non sono state introdotte nuove verifiche normative perché le aggiunte esaminate sono aritmetiche e attitudinali. Gli esempi amministrativi delle domande sono premesse di esercizi e non descrizioni certificate del diritto vigente.

Punto 27 non verificabile su Markdown: mancano in questa revisione un nuovo PDF impaginato e un controllo visivo pagina per pagina. I punti 1, 5, 7 e 30 sono valutati limitatamente al capitolo, ai rinvii e al topic pertinente, senza estendere il giudizio all'intero volume.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| C12-01 | Proporzioni, esempio delle scatole | 10 Accuratezza delle definizioni; 13 Esempi | Media | La sola uguaglianza delle capienze non garantiva che quattro e sette scatole contenessero quantità proporzionali: mancava l'ipotesi di riempimento. | Specificare quattro e sette scatole piene della stessa capienza. Verificato nel testo aggiornato: risultato 210. | Risolto |
| C12-02 | Checklist finale | 8 Coerenza terminologica | Lieve | La formula storica «vero, falso e non deducibile» non manteneva la distinzione, appena precisata nel corpo e nel quesito 19, fra contraddetto e indeterminato. | Usare «affermazioni confermate, contraddette e non determinabili». | Risolto |
| C12-03 | Titolo Logica essenziale | 4 Titoli; controllo automatico del contratto studente | Lieve | Il lint non riconosceva la presenza della teoria perché verifica parole chiave nei titoli. La teoria era già sostanzialmente presente. | Titolo ora «Logica essenziale: principi e parole che decidono il risultato». Lint rieseguito con esito positivo. | Risolto |

## 4. Osservazioni per capitolo

### Capitolo 12 — Logica, comprensione del testo e ragionamento

La progressione aggiunta è autosufficiente: precedenze, segni e decimali; significato ed equivalenza delle frazioni; confronto; quattro operazioni; parte e totale; percentuali e punti percentuali; rapporti e proporzioni; medie e unità; resto e scelta del risultato pertinente. Il caso dei tre turni applica frazioni, base variabile e produttività, ricostruendo correttamente il totale finale.

Verifiche aritmetiche indipendenti: 26 espressioni ricalcolate, nessuna discordanza. Controllate anche le diagnosi dei distrattori, inclusi A2 (9/12 equivalente ma non ridotta), A3 (somma impropria 4/10=2/5), B3 (140 come quantità trattata nell'errore), B6 (25 ottenuto scambiando i pesi) e C4 (900 ignorando il tempo iniziale). Le alternative sono distinte e non forniscono una seconda risposta corretta.

Chiavi delle 18 domande, ricavate indipendentemente e confrontate con quelle stampate:

| Livello | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| A | B | C | D | A | B | C |
| B | D | A | B | C | D | A |
| C | C | B | D | A | C | B |

Chiavi della mini-simulazione, tutte verificate:

| Domande | Risposte in ordine |
|---|---|
| 1–5 | B, B, C, C, C |
| 6–10 | B, B, C, C, B |
| 11–15 | C, C, B, B, A |
| 16–20 | B, C, C, C, B |
| 21–25 | C, B, B, A, B |

Le correzioni pregresse richieste risultano efficaci:

- Q3: la conversione dell'esistenziale congiuntivo autorizza C; l'appartenenza al settore A non è necessaria per quella conclusione.
- Q6: enumerazione delle 24 permutazioni conferma un solo ordine, D-A-B-C, quindi B.
- Q15: la relazione documento/evento è dichiarata; riunione è l'unica alternativa coerente.
- Q17: la richiesta dell'elenco completo elimina l'ambiguità di una risposta parziale; Elena precede Marco, che precede Sara, che precede Luca.
- Q19: le tre categorie sono definite nella consegna; C individua l'indeterminatezza in entrambe le direzioni.
- C6: enumerazione delle sei permutazioni conferma un solo ordine, A-C-B.
- Serie alfabetiche: l'alfabeto di 26 lettere è dichiarato prima delle prove; B-D-G-K conduce a P, e 2A-4C-6E-8G conduce a 10I.

## 5. Coerenza globale

Le nuove promesse negli obiettivi e nella checklist trovano spiegazioni ed esercizi. Il topic `wiki/topics/ragionamento-concorsuale.md` contiene un delta consolidato coerente con le regole e gli esempi. Le source notes preesistenti sostengono la tassonomia e il metodo; il capitolo dichiara correttamente originali gli esercizi, senza attribuirli a INVALSI o RIPAM. Non sono emerse duplicazioni con contenuti sanitari o materia territoriale.

Tracciabilità: le sei source_refs del frontmatter esistono; `last_compiled_from` include il topic aggiornato. Il gate rinvii passa; questo capitolo non introduce rinvii wikilink verso capitoli del base, quindi il controllo non implica verifica di riferimenti esterni o delle figure.

La matrice di volume letta durante l'audit conserva ancora la riga storica B-PA10: il suo aggiornamento con il delta aritmetico e le 18 nuove verifiche resta parte della chiusura dello step 14 affidata all'agente principale. Non è stato falsamente attestato come già effettuato da questa revisione.

## 6. Contenuto da verificare

Nessun calcolo o chiave residua da verificare nei 43 quesiti esaminati. La coerenza dell'impaginato e delle immagini già presenti con il nuovo testo richiede la successiva revisione visiva. Non è stata eseguita validazione psicometrica su candidati reali e non è implicata dall'esattezza delle soluzioni.

## 7. Suggerimenti facoltativi (non errori)

Si può aggiungere «in questo esempio, con medie diverse» prima dell'affermazione secondo cui la media semplice delle due medie richiede gruppi ugualmente numerosi: rende esplicito che, quando le medie coincidono, qualsiasi numerosità restituisce lo stesso valore. Nel contesto attuale 24/28 la frase e il risultato sono corretti.

Si può alleggerire l'elevata frequenza delle chiavi B/C nella mini-simulazione rimescolando le opzioni in una futura edizione. Non altera la correttezza, non è requisito per la chiusura e comporterebbe ricontrollo delle chiavi: non è stato applicato.

## 8. Priorità degli interventi

1. Tre rilievi editoriali individuati: già risolti e ricontrollati.
2. Completare aggiornamento della matrice e report 14/15 a cura dell'agente principale, includendo le evidenze di questa revisione.
3. Verificare il nuovo impaginato nelle fasi successive, senza ereditare automaticamente il precedente esito visivo.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori**, limitatamente al testo del capitolo e al perimetro esaminato. Le tre correzioni proposte sono state applicate; non restano errori oggettivi nei calcoli o nelle chiavi. Il giudizio non certifica l'impaginato né la chiusura della pipeline del volume.

## 10. Limiti di questa revisione

Revisione di Markdown e fonti/topic locali: nessuna ispezione delle sette immagini né del PDF, nessuna verifica web delle fonti concorsuali preesistenti, nessun test psicometrico. I controlli automatici sono stati invocati direttamente senza promozione al formato 2 e senza modificare run-state. Esito finale: `lint.passed=true`, zero blocker/warning; `referrals.passed=true`, zero blocker/warning; sei fonti presenti; `git diff --check` sul capitolo e sul topic senza errori.
