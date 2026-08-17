# Task 1 report — corpus ufficiale e conoscenza consolidata IVA

## Status

`DONE`

Implementazione completata senza commit, come richiesto dal controller. I due gate indipendenti restano di competenza del controller.

## Baseline e perimetro

Data audit: 20 luglio 2026.

Il worktree era già sporco: `.superpowers/sdd/` e varie source note estranee al Task 1 risultavano untracked. Sono state preservate. Nel perimetro raw M-FC02 non risultavano modifiche tracciate; i tre raw Normattiva e il raw EUR-Lex richiesto erano presenti.

| File baseline | SHA-256 |
|---|---|
| `normattiva-dpr-633-1972-iva.html` | `3F5C698DC0ACDC3E172F5E8AC54F74549E6928C834246CBF0EEE83F6D78DD883` |
| `normattiva-dpr-322-1998-dichiarazioni-fiscali.html` | `0DDE0049315D5D024CDA7635209DB602949A7F2427FAB6517BF6C8596E5B9231` |
| `normattiva-dlgs-241-1997-versamenti-compensazioni.html` | `DD707CACC944B6DF6EB96FF9F0E606BFC3860C53F0331F169081A9BA6B3D061B` |
| `eurlex-direttiva-2006-112-iva-consolidata-2025-04-14.html` | `F431FD040162DAC5A86EBA4FD988A851B46AD75B6636BCC89B01AD7E1D569F77` |

Le note preesistenti `normativa-tributaria-tuir-iva-accertamento-m-fc02` e `adempimenti-contabilita-civile-commerciale-m-fc02` offrivano solo nuclei generali: non distinguevano con articoli specifici le categorie IVA, le dichiarazioni successive e la compensazione. La nota UE consolidava correttamente la cornice armonizzata ma rinviava alla verifica nazionale articolo per articolo.

## Riconciliazione delle versioni

| Atto | Identificativo/versione | Evidenza locale | Ultimo aggiornamento dichiarato | Esito |
|---|---|---|---|---|
| D.P.R. 633/1972 | ELI `072U0633`; consultazione ufficiale al 20/07/2026 | singola vigenza 01/07/2026 | pubblicato 22/05/2026 | raw sufficiente, non sostituito |
| D.P.R. 322/1998 | ELI `098G0373`; consultazione ufficiale al 20/07/2026 | singola vigenza 02/07/2026 | pubblicato 17/06/2025 | raw sufficiente, non sostituito |
| D.Lgs. 241/1997 | ELI `097G0277`; consultazione ufficiale al 20/07/2026 | singola vigenza 02/07/2026 | pubblicato 26/03/2025 | raw sufficiente, non sostituito |
| Direttiva 2006/112/CE | CELEX `02006L0112-20250414`; ELI `dir/2006/112/2025-04-14` | consolidamento 14/04/2025 | EUR-Lex la indica come versione corrente | raw riusato |

Le pagine ufficiali Normattiva hanno confermato titolo, identificativi e ultimi aggiornamenti; EUR-Lex ha confermato CELEX, ELI, stato in vigore e versione corrente del 14 aprile 2025. I raw nazionali contengono segmenti/decorrenze ulteriori: non sono stati normalizzati né trasformati automaticamente in regole correnti. Non era necessario acquisire o sovrascrivere raw.

## File modificati

| File | Operazione | Righe | SHA-256 finale |
|---|---|---:|---|
| `wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md` | creato | 119 | `4D3E26B54FD5E7192B0CC836B53BEFC90B955158BDD88CC09E784599A57A4EFB` |
| `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md` | creato | 119 | `56756CEEEC607BBDCAFFB86D6BC6B3F2B9E3A9DD0E52129CB40DA67FC9022FC4` |
| `.superpowers/sdd/iva-task-1-report.md` | creato | report | da escludere dal commit editoriale se il controller non lo vuole versionare |

Nessun raw modificato.

## Mappa articoli → claim consolidati

### IVA

| Nucleo | Sostegno nazionale | Sostegno UE |
|---|---|---|
| sistema, operazioni soggette | D.P.R. 633/1972, art. 1 | direttiva, artt. 1-2 |
| cessioni, prestazioni, soggetti | artt. 2-5 | artt. 9, 14, 24-26 |
| territorialità | artt. 7-7-septies | artt. 31-61 |
| effettuazione/esigibilità | art. 6 | artt. 62-71 |
| non imponibilità/esenzione | artt. 8, 8-bis, 9, 10 | artt. 131 ss. |
| base ed esclusioni dal computo | artt. 13 e 15 | artt. 72-92 |
| debitore/rivalsa | artt. 17-18 | art. 193 ss. |
| detrazione, limiti, rettifica | artt. 19-19-bis.2 | artt. 167 ss., 178 |
| fatture, registri, liquidazione, dichiarazione | artt. 21, 23-25, 27, 30 | artt. 217 ss., 250 ss. |

### Dichiarazioni, versamenti e compensazioni

| Nucleo | Sostegno |
|---|---|
| forma/sottoscrizione | D.P.R. 322/1998, art. 1 |
| presentazione, tardiva/omessa, integrativa redditi/IRAP | D.P.R. 322/1998, art. 2, commi 7, 8, 8-bis |
| trasmissione/intermediari | D.P.R. 322/1998, art. 3 |
| dichiarazione e integrativa IVA | D.P.R. 322/1998, art. 8, commi 6-bis ss.; D.P.R. 633/1972, art. 30 |
| versamento unitario/compensazione | D.Lgs. 241/1997, art. 17 |
| termini e rateazione | D.Lgs. 241/1997, artt. 18 e 20 |
| delega di pagamento/F24 | D.Lgs. 241/1997, artt. 19 e 24 |
| assistenza/attestazioni/controlli connessi | D.Lgs. 241/1997, artt. 35-39, con verifica di fattispecie |

## Scelte di qualità e routing

- Separati in modo espresso dato normativo e sintesi didattica.
- Neutralità IVA descritta come strutturale e condizionata, non assoluta.
- Distinte imponibilità, non imponibilità, esenzione, fuori campo ed esclusione dalla base imponibile.
- Detrazione, rimborso e compensazione non sono presentati come automatici o incondizionati.
- Nessuna aliquota, soglia, termine annuale, modello corrente o codice tributo è stato cristallizzato.
- Capitolo 4 responsabile della teoria IVA; capitolo 6 della sequenza degli adempimenti.
- Capitoli 5, 5A, 5B e 7 restano responsabili, rispettivamente, di controllo/accertamento, sanzioni, riscossione e rimedi; la nota non ne duplica la disciplina.

## Controlli eseguiti

1. Baseline `git status` e SHA-256 dei quattro raw: completata.
2. Audit delle note esistenti con ricerca dei nuclei richiesti: confermata insufficienza articolo-specifica.
3. Verifica ufficiale Normattiva/EUR-Lex: completata; raw invariati perché riconciliabili.
4. Gate contenuti con `rg` su heading, atti, data/versione e routing: PASS.
5. Controllo claim mobili/automatismi con `rg`: PASS; occorrenze solo in esclusioni o cautele espresse.
6. `git diff --check` sulle due source note: PASS, nessun output.
7. Stato finale mirato: soltanto le due source note risultano nuove nel perimetro editoriale; nessun raw modificato.

## Diffstat

Due source note nuove, 238 righe complessive. Poiché sono untracked, `git diff --stat` non le include prima dello staging; il conteggio è stato verificato direttamente (119 + 119). Il report è un terzo file di governance e non fa parte del corpus editoriale.

## Memoria locale

Il richiamo obbligatorio tramite `LocalAgentMemory` è stato tentato prima della generazione. Il comando non ha potuto avviare il runner TypeScript perché `tsx` non era disponibile nella cache npm e l'ambiente impediva il recupero dalla rete (`ENOTCACHED`). Non è stata creata memoria parallela. La cattura post-flusso va eseguita dal controller in un ambiente con runner disponibile.

## Dubbi residui e review richiesta

Nessun dubbio bloccante. Rimane obbligatoria review umana tributaria/UE prima della pubblicazione per territorialità, esenzioni, reverse charge, detrazione, dichiarazioni integrative, crediti non spettanti/inesistenti e decorrenze future. Il controller deve ottenere i due verdetti indipendenti `SPEC COMPLIANCE` e `QUALITY` prima del commit.

## Fix obbligatorio dopo review — 20 luglio 2026

### Causa e correzione

La review ha individuato la causa dell'insufficienza probatoria: i tre HTML iniziali conservavano metadati e navigazione, ma il corpo integralmente esposto era limitato all'art. 1. Le mappe articolo → claim non potevano quindi dirsi verificate su quei file. Sono stati acquisiti export AKN ufficiali, datati e separati, senza sovrascrivere i raw tracciati.

Il controllo AKN ha inoltre confermato due errori della prima versione: i primi due commi dell'art. 27 D.P.R. 633/1972 sono abrogati dal D.P.R. 100/1998; l'art. 30 disciplina conguaglio/rimborso dell'eccedenza e non è la fonte generale della dichiarazione annuale. La fonte vigente usata ora è D.P.R. 100/1998, art. 1, per la liquidazione periodica e D.P.R. 322/1998, art. 8, per la dichiarazione annuale IVA.

L'audit ha acquisito anche il D.Lgs. 33/2025. Il marker di abrogazione presente nell'AKN D.Lgs. 241/1997 e l'expression `ita@2026-01-10` non definiscono da soli la decorrenza sostanziale. Gli artt. 241 e 243 del testo unico, nel consolidato successivo ELI `20260523`, stabiliscono che le abrogazioni e l'applicazione del nuovo corpus operano dal 1° gennaio 2027. Al cutoff restano quindi vigenti gli artt. 17-24 del D.Lgs. 241/1997.

### Acquisizione AKN: metodo e output

Per ogni atto è stata aperta una sessione separata:

```powershell
curl.exe -L --fail --silent --show-error --max-time 60 -c <cookie> <caricaDettaglioAtto-url> -o <detail-temp>
curl.exe -L --fail --silent --show-error --max-time 60 -b <cookie> -e <caricaDettaglioAtto-url> <caricaAKN-url> -o <raw-datato>
```

Il precedente tentativo diretto con `Invoke-WebRequest` senza sessione era rimasto senza output ed era stato abortito dopo circa 348 secondi. Il flusso con cookie ha completato ogni coppia di richieste in meno di sei secondi.

| Export ufficiale | Byte | Articoli | Expression principale | SHA-256 |
|---|---:|---:|---|---|
| `normattiva-dpr-633-1972-iva-akn-2026-07-20.xml` | 1.363.594 | 172 | `ita@2026-05-23` | `3BD03FB841720EA471418FFCC928345DD72B40403B9289F53E8DE9E0D3C4FD81` |
| `normattiva-dpr-322-1998-dichiarazioni-fiscali-akn-2026-07-20.xml` | 225.664 | 12 | `ita@2025-06-18` | `6AD5066623A8FAFB950C723A021633F3B5A451C142E044EC67CEEC74A97450C7` |
| `normattiva-dlgs-241-1997-versamenti-compensazioni-akn-2026-07-20.xml` | 237.174 | 42 | `ita@2026-01-10` | `E89C8DFF010A03B21622395F2265BDF83F983BEC42D846E05969453DA5864B54` |
| `normattiva-dpr-100-1998-liquidazioni-iva-akn-2026-07-20.xml` | 23.914 | 2 | `ita@2024-08-06` | `F35BF35E95D0EF4736AB862CC3EC5542931A800CFEEF55169A7621FB9D837D08` |
| `normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml` | 1.514.465 | 1 atto + 243 articoli allegati | ELI consolidato `20260523`; TU in allegati | `D20152E0904998A57A5C8C698E076ED73EF82E47F67F463EC5ECAAABF823524A` |

Tutti i cinque file superano il parsing `[xml]`: `XML PASS`. Per il D.Lgs. 33/2025 Normattiva serializza i 243 articoli del testo unico come documenti allegati `Allegato-art. N`, oltre all'articolo del decreto approvativo; perciò il conteggio strutturale è `1 <article> + 243 attached articles`.

### Distinzione delle evidenze

- I vecchi HTML sostengono metadati di pagina: ELI, singola vigenza selezionata e ultimo aggiornamento dichiarato.
- Gli AKN integrali sostengono il contenuto articolo-specifico, le abrogazioni, gli identificativi FRBR e le expression.
- EUR-Lex sostiene la versione consolidata della direttiva 2006/112/CE al 14 aprile 2025.

Dopo questa separazione, `status: consolidated` è giustificato per entrambe le source note, fermo `review_required: true` per fattispecie complesse e claim mobili.

### Esito del controllo puntuale delle mappe

**IVA:** confermati artt. 1-10, 13, 15, 17-19-bis.2, 21 e 23-25 del D.P.R. 633/1972 sui rispettivi nodi AKN. Rimossi art. 27 quale fonte vigente della liquidazione e art. 30 quale fonte generale della dichiarazione. Inseriti D.P.R. 100/1998, art. 1; D.P.R. 322/1998, art. 8; art. 30 mantenuto soltanto per conguaglio/rimborso dell'eccedenza.

**Dichiarazioni:** confermati D.P.R. 322/1998 artt. 1-3 e art. 8, inclusi comma 6 e commi 6-bis e seguenti. **Versamenti al cutoff:** D.Lgs. 241/1997 artt. 17 (versamento unitario/compensazione), 18 (termini), 19 (delega e saldo zero), 20 (rateazione); art. 24 riconosciuto come transitorio e non usato quale fonte generale. **Dal 1° gennaio 2027:** D.Lgs. 33/2025 artt. 3 e 5-10, in mappa separata, con decorrenza fondata sugli artt. 241 e 243.

### File del fix

- aggiunti cinque raw AKN sopra elencati;
- corretta `wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md`, SHA-256 `86359DC65A2B7C0E19819625565B2B42B4C24C017CD1AC36A1176ACB1B4B0964` al controllo precedente al gate finale;
- corretta `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md`, SHA-256 `75A07B1A1DCD221CA07F34F616C0B4B0B2EF932DB439053B24A94F82841FCAAD` dopo Fix loop 2;
- aggiornato questo report.

`apply_patch` è stato tentato per le correzioni, ma il wrapper Windows ha restituito `cannot enforce split writable root sets`. Come autorizzato dal brief, è stato usato un fallback chirurgico con `ReadAllText`/`WriteAllText` sui soli due file Task 1; i raw sono stati prodotti direttamente dal download ufficiale.
### Gate finale del fix

Comandi:

```powershell
[xml](Get-Content -Raw <ognuno dei cinque AKN>)
rg -n '<riferimenti abrogati o mapping vietati>' <due-source-note>
git diff --check -- <due-source-note> .superpowers/sdd/iva-task-1-report.md
git status --short -- <perimetro Task-1>
```

Output sintetico del primo fix: `XML_BAD=0`; nessun uso dell'art. 27 D.P.R. 633/1972 per la liquidazione né dell'art. 30 come fonte generale della dichiarazione; `git diff --check` senza output. La valutazione allora riportata sugli artt. 17-24 D.Lgs. 241/1997 è superata dal Fix loop 2 seguente. Stato mirato: cinque nuovi AKN, due source note e report; vecchi raw invariati; nessun commit.
## Fix loop 2 — decorrenza del D.Lgs. 33/2025

Verifica diretta nell'AKN:

```powershell
rg -n -A 45 -B 8 'Allegato-art\. 241|Allegato-art\. 243|ART\. 241|ART\. 243' wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml
```

Output decisivo:

- art. 241, comma 1: «A decorrere dalla data di cui all'articolo 243» sono abrogate le disposizioni elencate; la lettera t) include gli artt. 17-28 e 30 del D.Lgs. 241/1997;
- art. 243, comma 1: il testo unico si applica dal `1° gennaio 2027`.

Riconciliazione: l'AKN del D.Lgs. 241/1997 reca expression `ita@2026-01-10` e marker di abrogazione, ma la decorrenza sostanziale va letta nel consolidato successivo del D.Lgs. 33/2025, alias ELI `20260523`. La FRBRExpression principale e quelle degli allegati del testo unico restano `ita@2025-03-27`; il markup successivo degli artt. 241 e 243 rinvia effetti e applicazione al 2027. Al 20 luglio 2026 gli artt. 17-24 del D.Lgs. 241/1997 sono quindi ancora la disciplina vigente.

La source note espone ora due mappe non commiste: vigente al cutoff (D.Lgs. 241/1997, artt. 17-20; artt. 35-39 per assistenza/visto) e futura dal 1° gennaio 2027 (D.Lgs. 33/2025, artt. 3, 5-10, 241 e 243). `status: consolidated` resta giustificato perché versione, conflitto apparente e decorrenza sono esplicitamente riconciliati.

File modificati nel Fix loop 2: soltanto `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md` e questo report. Nota IVA e raw invariati.

Gate Fix loop 2: `rg` diretto sugli artt. 241/243 conferma rinvio al `1° gennaio 2027`; controllo doppia mappa `VIGENTE_ROWS=9 FUTURE_ROWS=5`; `git diff --check` senza output.

## Final integration fix — routing capitoli 5B e 7

Verifica dei heading canonici:

```powershell
rg -n '^title:|^# ' wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/05b-tutela-processo-tributario.md wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/07-riscossione-nazionale-lavoro-ader.md
```

Output: capitolo 5B = `Tutela e processo tributario`; capitolo 7 = `Riscossione nazionale e lavoro in AdER`. Il routing della source note è stato allineato: 5B per tutela giurisdizionale, contenzioso e rimedi; 7 per recupero e riscossione. Nessun altro contenuto è stato modificato.

Controllo link/heading:

```text
93:- **Capitolo 5B — tutela e processo tributario:** tutela giurisdizionale, contenzioso e rimedi contro atti e dinieghi.
95:- **Capitolo 7 — riscossione nazionale e lavoro in AdER:** recupero e riscossione delle somme risultanti, accertate o indebitamente compensate.
SOURCE_DIFF_CHECK=PASS
```

SHA-256 finale della source note: `6966B04E40D7899CBB52DF3275AA72B965DC74FDC70870A9DC7C90EA13DD5840`.

`apply_patch` è stato tentato ma respinto dal wrapper Windows già documentato; fallback chirurgico limitato alle due righe autorizzate. Nessun commit.