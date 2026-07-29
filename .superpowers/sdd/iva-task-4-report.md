# Task 4 report - Governance IVA e adempimenti

## Status

DONE_WITH_REVIEW_FIXES

## Baseline verificata

- Commit di contesto dichiarati dal brief: source `7ecd2c8`, cap. 4 `df2791d`, contenuti coordinati `1a8c3c1`.
- Governance iniziale: 80 nuclei, 64 `completo`, 16 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`; giudizio `Non pubblicabile allo stato attuale`.
- Righe interessate: `IVA - Presupposti, operazioni, rivalsa, detrazione, liquidazione` e `Adempimenti - Dichiarazione, versamento e compensazione`.
- La riga distinta `Ciclo fatto-documento-dichiarazione-liquidazione-versamento` era gia `completo` e non e stata riclassificata.

## Mappa delle prove reali

### Nucleo IVA

- teoria -> cap. 4, `IVA: operazioni, soggetti, detrazione e adempimenti`, incluse `Neutralita' come meccanismo, non come risultato assoluto`, `I tre presupposti`, `Soggetto passivo, debitore e consumatore finale`, `Le quattro classi di operazioni`; cap. 6, `Operazioni IVA e ciclo degli adempimenti`;
- caso -> cap. 6, caso Alfa e `Caso comparativo: quattro operazioni, quattro esiti`;
- output concorsuale -> cap. 4, `Checklist operativa finale`, che verifica anche l'uso dell'IVA come mappa e non come elenco; cap. 6, risposta modello alla commissione e classificazione operativa;
- verifica -> cap. 4, verifiche su neutralita e classi; cap. 6, quiz ragionati, domande-trappola e checklist;
- source -> `[[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]`, stato `consolidated`, audit ufficiale D.P.R. 633/1972, D.P.R. 100/1998 e direttiva 2006/112/CE;
- review -> PASS didattico locale; restano review umana tributaria/UE e verifica datata dei dati mobili.

### Nucleo dichiarazione, versamento e compensazione

- teoria -> cap. 6, `Dichiarazioni, versamenti e compensazioni`, con originaria, correttiva, integrativa, tardiva/omessa, F24, compensazione verticale/orizzontale, credito IVA e correzione;
- caso -> quattro casi dichiarativi e due scenari risolti di compensazione;
- output concorsuale -> risposta modello su ciclo IVA/dichiarazione/pagamento e gate in sei controlli;
- verifica -> quiz ragionati, domande-trappola e checklist;
- source -> `[[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]`, stato `consolidated`, audit ufficiale D.P.R. 322/1998, D.Lgs. 241/1997 e disciplina futura D.Lgs. 33/2025;
- review -> PASS didattico locale; restano review umana tributaria e verifica di modelli, termini, soglie e canali mobili.

## Esito governance e conteggi

- IVA: `parziale` -> `completo`.
- Dichiarazione, versamento e compensazione: `parziale` -> `completo`.
- Conteggi finali verificati: 80 nuclei, 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`.
- Giudizio mantenuto: **Non pubblicabile allo stato attuale**.

## Blocker residui (14)

1. Autotutela e ulteriori strumenti amministrativi/deflativi.
2. Misure cautelari ed esecuzione forzata AdER.
3. Regimi doganali.
4. Debito doganale e garanzia.
5. Prodotti energetici, alcole e tabacchi.
6. Tutela del giocatore, illegalita, prelievi e controlli.
7. DOCFA, PREGEO e voltura.
8. Estimo e applicazioni OMI.
9. Conti e partita doppia.
10. Indici ed equilibri aziendali.
11. Utile civilistico e reddito imponibile.
12. Crisi d'impresa.
13. Comunicazione, front-office e privacy.
14. Schede e destinazioni cross-family per crisi, HR, gare e ICT.

## File e diffstat

Dal Task 4 sono stati modificati esclusivamente i tre file governance autorizzati:

- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`
- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`

Diffstat governance finale: 3 file, 33 inserimenti, 35 eliminazioni. Creato inoltre questo report richiesto. Nessun capitolo, source note o raw modificato; nessun commit eseguito.

## Controlli

- `rg -c "\| completo \|" .../02-matrice-copertura-didattica.md` -> `66`.
- `rg -c "\| parziale \|" .../02-matrice-copertura-didattica.md` -> `14`.
- Ricerca degli stati `solo-nominato`, `rinviato`, `mancante` nelle righe matrice -> nessuna occorrenza (`rg` exit 1, conteggio logico 0 per ciascuno).
- Ricerca report -> giudizio `Non pubblicabile`, `14 blocker` e `14 nuclei` presenti; vecchi due blocker IVA/adempimenti assenti dall'elenco residuo.
- `git diff --check` sui tre file governance -> PASS; soli warning informativi CRLF/LF di Git.
- Controllo reciproco: 66 + 14 = 80; elenco residuo numerato 1-14.
- Fix review: heading matrice corretto in `Il ciclo dell'adempimento fiscale`; prova cap. 4 ricondotta al heading reale `Checklist operativa finale`; formulazione del perimetro file distinta dal worktree preesistente.

## Note operative

Il richiamo tramite `LocalAgentMemory` e stato tentato prima dell'output, ma il runner diretto Node non ha risolto l'import TypeScript extensionless `src/server/config`; nessuna memoria parallela e stata creata. `apply_patch` e stato tentato per primo, ma il wrapper Windows ha rifiutato la preparazione del sandbox; come previsto dal brief e stato usato un fallback chirurgico sui soli file autorizzati.