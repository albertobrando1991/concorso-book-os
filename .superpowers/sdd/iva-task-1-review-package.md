# IVA Task 1 review package post-fix-2

## Git status
```text
?? wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni-akn-2026-07-20.xml
?? wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml
?? wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-100-1998-liquidazioni-iva-akn-2026-07-20.xml
?? wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali-akn-2026-07-20.xml
?? wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva-akn-2026-07-20.xml
?? wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
?? wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md
```

## Raw manifest
```text
normattiva-dlgs-241-1997-versamenti-compensazioni-akn-2026-07-20.xml | 237174 bytes | articles=42 | sha256=E89C8DFF010A03B21622395F2265BDF83F983BEC42D846E05969453DA5864B54
normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml | 1514465 bytes | articles=1 | sha256=D20152E0904998A57A5C8C698E076ED73EF82E47F67F463EC5ECAAABF823524A
normattiva-dpr-100-1998-liquidazioni-iva-akn-2026-07-20.xml | 23914 bytes | articles=2 | sha256=F35BF35E95D0EF4736AB862CC3EC5542931A800CFEEF55169A7621FB9D837D08
normattiva-dpr-322-1998-dichiarazioni-fiscali-akn-2026-07-20.xml | 225664 bytes | articles=12 | sha256=6AD5066623A8FAFB950C723A021633F3B5A451C142E044EC67CEEC74A97450C7
normattiva-dpr-633-1972-iva-akn-2026-07-20.xml | 1363594 bytes | articles=172 | sha256=3BD03FB841720EA471418FFCC928345DD72B40403B9289F53E8DE9E0D3C4FD81
```

## Implementer report
# Task 1 report â€” corpus ufficiale e conoscenza consolidata IVA

## Status

`DONE`

Implementazione completata senza commit, come richiesto dal controller. I due gate indipendenti restano di competenza del controller.

## Baseline e perimetro

Data audit: 20 luglio 2026.

Il worktree era giÃ  sporco: `.superpowers/sdd/` e varie source note estranee al Task 1 risultavano untracked. Sono state preservate. Nel perimetro raw M-FC02 non risultavano modifiche tracciate; i tre raw Normattiva e il raw EUR-Lex richiesto erano presenti.

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

Le pagine ufficiali Normattiva hanno confermato titolo, identificativi e ultimi aggiornamenti; EUR-Lex ha confermato CELEX, ELI, stato in vigore e versione corrente del 14 aprile 2025. I raw nazionali contengono segmenti/decorrenze ulteriori: non sono stati normalizzati nÃ© trasformati automaticamente in regole correnti. Non era necessario acquisire o sovrascrivere raw.

## File modificati

| File | Operazione | Righe | SHA-256 finale |
|---|---|---:|---|
| `wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md` | creato | 119 | `4D3E26B54FD5E7192B0CC836B53BEFC90B955158BDD88CC09E784599A57A4EFB` |
| `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md` | creato | 119 | `56756CEEEC607BBDCAFFB86D6BC6B3F2B9E3A9DD0E52129CB40DA67FC9022FC4` |
| `.superpowers/sdd/iva-task-1-report.md` | creato | report | da escludere dal commit editoriale se il controller non lo vuole versionare |

Nessun raw modificato.

## Mappa articoli â†’ claim consolidati

### IVA

| Nucleo | Sostegno nazionale | Sostegno UE |
|---|---|---|
| sistema, operazioni soggette | D.P.R. 633/1972, art. 1 | direttiva, artt. 1-2 |
| cessioni, prestazioni, soggetti | artt. 2-5 | artt. 9, 14, 24-26 |
| territorialitÃ  | artt. 7-7-septies | artt. 31-61 |
| effettuazione/esigibilitÃ  | art. 6 | artt. 62-71 |
| non imponibilitÃ /esenzione | artt. 8, 8-bis, 9, 10 | artt. 131 ss. |
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

## Scelte di qualitÃ  e routing

- Separati in modo espresso dato normativo e sintesi didattica.
- NeutralitÃ  IVA descritta come strutturale e condizionata, non assoluta.
- Distinte imponibilitÃ , non imponibilitÃ , esenzione, fuori campo ed esclusione dalla base imponibile.
- Detrazione, rimborso e compensazione non sono presentati come automatici o incondizionati.
- Nessuna aliquota, soglia, termine annuale, modello corrente o codice tributo Ã¨ stato cristallizzato.
- Capitolo 4 responsabile della teoria IVA; capitolo 6 della sequenza degli adempimenti.
- Capitoli 5, 5A, 5B e 7 restano responsabili, rispettivamente, di controllo/accertamento, sanzioni, riscossione e rimedi; la nota non ne duplica la disciplina.

## Controlli eseguiti

1. Baseline `git status` e SHA-256 dei quattro raw: completata.
2. Audit delle note esistenti con ricerca dei nuclei richiesti: confermata insufficienza articolo-specifica.
3. Verifica ufficiale Normattiva/EUR-Lex: completata; raw invariati perchÃ© riconciliabili.
4. Gate contenuti con `rg` su heading, atti, data/versione e routing: PASS.
5. Controllo claim mobili/automatismi con `rg`: PASS; occorrenze solo in esclusioni o cautele espresse.
6. `git diff --check` sulle due source note: PASS, nessun output.
7. Stato finale mirato: soltanto le due source note risultano nuove nel perimetro editoriale; nessun raw modificato.

## Diffstat

Due source note nuove, 238 righe complessive. PoichÃ© sono untracked, `git diff --stat` non le include prima dello staging; il conteggio Ã¨ stato verificato direttamente (119 + 119). Il report Ã¨ un terzo file di governance e non fa parte del corpus editoriale.

## Memoria locale

Il richiamo obbligatorio tramite `LocalAgentMemory` Ã¨ stato tentato prima della generazione. Il comando non ha potuto avviare il runner TypeScript perchÃ© `tsx` non era disponibile nella cache npm e l'ambiente impediva il recupero dalla rete (`ENOTCACHED`). Non Ã¨ stata creata memoria parallela. La cattura post-flusso va eseguita dal controller in un ambiente con runner disponibile.

## Dubbi residui e review richiesta

Nessun dubbio bloccante. Rimane obbligatoria review umana tributaria/UE prima della pubblicazione per territorialitÃ , esenzioni, reverse charge, detrazione, dichiarazioni integrative, crediti non spettanti/inesistenti e decorrenze future. Il controller deve ottenere i due verdetti indipendenti `SPEC COMPLIANCE` e `QUALITY` prima del commit.

## Fix obbligatorio dopo review â€” 20 luglio 2026

### Causa e correzione

La review ha individuato la causa dell'insufficienza probatoria: i tre HTML iniziali conservavano metadati e navigazione, ma il corpo integralmente esposto era limitato all'art. 1. Le mappe articolo â†’ claim non potevano quindi dirsi verificate su quei file. Sono stati acquisiti export AKN ufficiali, datati e separati, senza sovrascrivere i raw tracciati.

Il controllo AKN ha inoltre confermato due errori della prima versione: i primi due commi dell'art. 27 D.P.R. 633/1972 sono abrogati dal D.P.R. 100/1998; l'art. 30 disciplina conguaglio/rimborso dell'eccedenza e non Ã¨ la fonte generale della dichiarazione annuale. La fonte vigente usata ora Ã¨ D.P.R. 100/1998, art. 1, per la liquidazione periodica e D.P.R. 322/1998, art. 8, per la dichiarazione annuale IVA.

L'audit ha acquisito anche il D.Lgs. 33/2025. Il marker di abrogazione presente nell'AKN D.Lgs. 241/1997 e l'expression `ita@2026-01-10` non definiscono da soli la decorrenza sostanziale. Gli artt. 241 e 243 del testo unico, nel consolidato successivo ELI `20260523`, stabiliscono che le abrogazioni e l'applicazione del nuovo corpus operano dal 1Â° gennaio 2027. Al cutoff restano quindi vigenti gli artt. 17-24 del D.Lgs. 241/1997.

### Acquisizione AKN: metodo e output

Per ogni atto Ã¨ stata aperta una sessione separata:

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

Tutti i cinque file superano il parsing `[xml]`: `XML PASS`. Per il D.Lgs. 33/2025 Normattiva serializza i 243 articoli del testo unico come documenti allegati `Allegato-art. N`, oltre all'articolo del decreto approvativo; perciÃ² il conteggio strutturale Ã¨ `1 <article> + 243 attached articles`.

### Distinzione delle evidenze

- I vecchi HTML sostengono metadati di pagina: ELI, singola vigenza selezionata e ultimo aggiornamento dichiarato.
- Gli AKN integrali sostengono il contenuto articolo-specifico, le abrogazioni, gli identificativi FRBR e le expression.
- EUR-Lex sostiene la versione consolidata della direttiva 2006/112/CE al 14 aprile 2025.

Dopo questa separazione, `status: consolidated` Ã¨ giustificato per entrambe le source note, fermo `review_required: true` per fattispecie complesse e claim mobili.

### Esito del controllo puntuale delle mappe

**IVA:** confermati artt. 1-10, 13, 15, 17-19-bis.2, 21 e 23-25 del D.P.R. 633/1972 sui rispettivi nodi AKN. Rimossi art. 27 quale fonte vigente della liquidazione e art. 30 quale fonte generale della dichiarazione. Inseriti D.P.R. 100/1998, art. 1; D.P.R. 322/1998, art. 8; art. 30 mantenuto soltanto per conguaglio/rimborso dell'eccedenza.

**Dichiarazioni:** confermati D.P.R. 322/1998 artt. 1-3 e art. 8, inclusi comma 6 e commi 6-bis e seguenti. **Versamenti al cutoff:** D.Lgs. 241/1997 artt. 17 (versamento unitario/compensazione), 18 (termini), 19 (delega e saldo zero), 20 (rateazione); art. 24 riconosciuto come transitorio e non usato quale fonte generale. **Dal 1Â° gennaio 2027:** D.Lgs. 33/2025 artt. 3 e 5-10, in mappa separata, con decorrenza fondata sugli artt. 241 e 243.

### File del fix

- aggiunti cinque raw AKN sopra elencati;
- corretta `wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md`, SHA-256 `86359DC65A2B7C0E19819625565B2B42B4C24C017CD1AC36A1176ACB1B4B0964` al controllo precedente al gate finale;
- corretta `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md`, SHA-256 `75A07B1A1DCD221CA07F34F616C0B4B0B2EF932DB439053B24A94F82841FCAAD` dopo Fix loop 2;
- aggiornato questo report.

`apply_patch` Ã¨ stato tentato per le correzioni, ma il wrapper Windows ha restituito `cannot enforce split writable root sets`. Come autorizzato dal brief, Ã¨ stato usato un fallback chirurgico con `ReadAllText`/`WriteAllText` sui soli due file Task 1; i raw sono stati prodotti direttamente dal download ufficiale.
### Gate finale del fix

Comandi:

```powershell
[xml](Get-Content -Raw <ognuno dei cinque AKN>)
rg -n '<riferimenti abrogati o mapping vietati>' <due-source-note>
git diff --check -- <due-source-note> .superpowers/sdd/iva-task-1-report.md
git status --short -- <perimetro Task-1>
```

Output sintetico del primo fix: `XML_BAD=0`; nessun uso dell'art. 27 D.P.R. 633/1972 per la liquidazione nÃ© dell'art. 30 come fonte generale della dichiarazione; `git diff --check` senza output. La valutazione allora riportata sugli artt. 17-24 D.Lgs. 241/1997 Ã¨ superata dal Fix loop 2 seguente. Stato mirato: cinque nuovi AKN, due source note e report; vecchi raw invariati; nessun commit.
## Fix loop 2 â€” decorrenza del D.Lgs. 33/2025

Verifica diretta nell'AKN:

```powershell
rg -n -A 45 -B 8 'Allegato-art\. 241|Allegato-art\. 243|ART\. 241|ART\. 243' wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml
```

Output decisivo:

- art. 241, comma 1: Â«A decorrere dalla data di cui all'articolo 243Â» sono abrogate le disposizioni elencate; la lettera t) include gli artt. 17-28 e 30 del D.Lgs. 241/1997;
- art. 243, comma 1: il testo unico si applica dal `1Â° gennaio 2027`.

Riconciliazione: l'AKN del D.Lgs. 241/1997 reca expression `ita@2026-01-10` e marker di abrogazione, ma la decorrenza sostanziale va letta nel consolidato successivo del D.Lgs. 33/2025, alias ELI `20260523`. La FRBRExpression principale e quelle degli allegati del testo unico restano `ita@2025-03-27`; il markup successivo degli artt. 241 e 243 rinvia effetti e applicazione al 2027. Al 20 luglio 2026 gli artt. 17-24 del D.Lgs. 241/1997 sono quindi ancora la disciplina vigente.

La source note espone ora due mappe non commiste: vigente al cutoff (D.Lgs. 241/1997, artt. 17-20; artt. 35-39 per assistenza/visto) e futura dal 1Â° gennaio 2027 (D.Lgs. 33/2025, artt. 3, 5-10, 241 e 243). `status: consolidated` resta giustificato perchÃ© versione, conflitto apparente e decorrenza sono esplicitamente riconciliati.

File modificati nel Fix loop 2: soltanto `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md` e questo report. Nota IVA e raw invariati.

Gate Fix loop 2: `rg` diretto sugli artt. 241/243 conferma rinvio al `1Â° gennaio 2027`; controllo doppia mappa `VIGENTE_ROWS=9 FUTURE_ROWS=5`; `git diff --check` senza output.


## Source IVA
---
id: source-iva-dpr-633-1972-aggiornamento-2026-07-20
type: source
title: "IVA: sistema unionale e disciplina nazionale consolidata"
status: consolidated
domain: "concorsi pubblici italiani"
topics: ["IVA", "diritto tributario UE", "adempimenti IVA"]
entities: ["Unione europea", "Agenzia delle Entrate", "Normattiva", "EUR-Lex"]
source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02", "sources/adempimenti-contabilita-civile-commerciale-m-fc02", "sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18"]
book_refs: ["m-fc02-agenzie-fiscali"]
confidence: 0.94
updated_at: 2026-07-20T00:00:00+02:00
created_at: 2026-07-20T00:00:00+02:00
review_required: true
canonical: true
tags: ["source", "official-source", "iva", "module-code-m-fc02", "cutoff-2026-07-20"]
source_type: official_legal_corpus
source_url: "mixed:https://www.normattiva.it/eli/id/1972/11/11/072U0633/CONSOLIDATED/20260720|https://www.normattiva.it/eli/id/1998/04/16/098G0158/CONSOLIDATED/20260720|https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:02006L0112-20250414"
source_date: "2026-07-20"
audit_date: "2026-07-20"
latest_official_update_checked: "D.P.R. 633/1972: ultimo aggiornamento pubblicato 22/05/2026; D.P.R. 100/1998: ultimo aggiornamento pubblicato 05/08/2024; direttiva 2006/112/CE: consolidamento 14/04/2025"
authority_level: very_high
raw_refs:
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html"
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva-akn-2026-07-20.xml"
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-100-1998-liquidazioni-iva-akn-2026-07-20.xml"
  - "wiki/raw/m-fc02-agenzie-fiscali/eurlex-direttiva-2006-112-iva-consolidata-2025-04-14.html"
---

# IVA: sistema unionale e disciplina nazionale consolidata

## Esito dell'audit e versione

**Data di consultazione:** 20 luglio 2026. **D.P.R. 633/1972:** il vecchio HTML certifica ELI `072U0633`, singola vigenza 1Â° luglio 2026 e ultimo aggiornamento pubblicato 22 maggio 2026, ma visualizza integralmente soltanto l'art. 1. Il nuovo export AKN integrale richiesto al 20 luglio contiene 172 elementi `article`; la `FRBRExpression` principale Ã¨ `ita@2026-05-23`. I claim articolo-specifici nazionali sono stati verificati su questo AKN, non sul vecchio HTML. **D.P.R. 100/1998:** export AKN integrale di 2 articoli, expression `ita@2024-08-06`, ultimo aggiornamento dichiarato dalla pagina ufficiale 5 agosto 2024. **Versione unionale:** direttiva 2006/112/CE, CELEX `02006L0112-20250414`, ELI `dir/2006/112/2025-04-14`, consolidata al 14 aprile 2025 e indicata da EUR-Lex come versione corrente.

Gli AKN mostrano anche abrogazioni e decorrenze differite. In particolare, i primi due commi dell'art. 27 del D.P.R. 633/1972 sono abrogati dal D.P.R. 100/1998: l'art. 27 non Ã¨ usato come fonte vigente della liquidazione periodica. I raw sono prova di audit; questa nota Ã¨ la base consolidata dopo verifica puntuale dei nodi richiamati.

## Funzione dell'IVA e armonizzazione UE

**Dato normativo.** La direttiva configura un sistema comune nel quale l'IVA, proporzionale al prezzo, grava sui consumi attraverso applicazione e detrazione nelle diverse fasi (direttiva 2006/112/CE, art. 1). Delimita operazioni soggette e soggetto passivo (artt. 2 e 9), mentre il D.P.R. 633/1972 assoggetta all'imposta le cessioni di beni e le prestazioni di servizi effettuate nel territorio dello Stato nell'esercizio di imprese, arti o professioni, nonchÃ© le importazioni da chiunque effettuate (art. 1).

**Sintesi didattica.** L'IVA Ã¨ armonizzata ma applicata mediante la disciplina nazionale negli spazi e secondo le opzioni consentite. La neutralitÃ  riguarda, in via strutturale, l'operatore che realizza operazioni con diritto a detrazione; non Ã¨ assoluta: esenzioni, indetraibilitÃ , pro rata, requisiti e rettifiche possono lasciare l'onere sull'operatore.

## Presupposti e classificazione delle operazioni

### Profilo oggettivo

Le cessioni trasferiscono, di regola, la proprietÃ  o costituiscono/trasferiscono diritti reali su beni; la norma include e sottrae fattispecie specifiche (D.P.R. 633/1972, art. 2; direttiva, art. 14). Le prestazioni sono operazioni verso corrispettivo dipendenti da obbligazioni di fare, non fare o permettere, con assimilazioni ed esclusioni previste dalla legge (D.P.R. 633/1972, art. 3; direttiva, artt. 24-26).

### Profilo soggettivo

L'esercizio d'impresa e l'esercizio di arti e professioni delimitano l'abitualitÃ  e l'ambito delle attivitÃ  rilevanti (D.P.R. 633/1972, artt. 4 e 5). La nozione unionale di soggetto passivo Ã¨ autonoma e guarda all'esercizio indipendente di un'attivitÃ  economica (direttiva, art. 9).

### Profilo territoriale

Le regole di territorialitÃ  stabiliscono se la singola operazione si considera effettuata nel territorio dello Stato. Il rinvio responsabile Ã¨ agli artt. 7-7-septies del D.P.R. 633/1972 e, nel sistema unionale, ai titoli relativi al luogo delle operazioni (in particolare artt. 31-61 della direttiva). Non basta che cedente o cliente siano italiani.

### Imponibili, non imponibili, esenti ed escluse

- **Imponibile:** ricorrono i presupposti e l'operazione concorre all'applicazione dell'imposta secondo le regole ordinarie.
- **Non imponibile:** l'operazione Ã¨ rilevante nel sistema IVA, ma la legge non applica l'imposta, tipicamente per assicurare la tassazione nel luogo di destinazione; gli esempi nazionali principali sono le cessioni all'esportazione e operazioni assimilate (D.P.R. 633/1972, artt. 8, 8-bis e 9). In linea generale conserva il diritto a detrazione, da verificare sulla fattispecie.
- **Esente:** l'operazione rientra nel campo IVA ma beneficia di un'esenzione tipizzata (D.P.R. 633/1972, art. 10; direttiva, artt. 131 e seguenti). L'esenzione puÃ² limitare la detrazione degli acquisti: non equivale a non imponibilitÃ .
- **Esclusa/fuori campo:** manca un presupposto oppure una disposizione sottrae la fattispecie al campo applicativo (tra gli altri, artt. 2, 3 e 7-7-septies). Le somme escluse dal computo della base imponibile ai sensi dell'art. 15 non costituiscono, per ciÃ² solo, una quinta categoria di operazioni.

**Esempio ammesso.** Una cessione interna imponibile, un'esportazione non imponibile, una prestazione sanitaria esente se ricade nella previsione tipica e una prestazione priva di territorialitÃ  italiana producono conseguenze diverse su addebito e detrazione. L'esempio serve a classificare; aliquota, requisiti documentali e regime applicabile vanno verificati nel caso.

## Effettuazione, fatto generatore ed esigibilitÃ 

L'art. 6 del D.P.R. 633/1972 individua, per categorie di operazioni, il momento di effettuazione e disciplina anticipazioni collegate a pagamento o fatturazione. Nel quadro UE occorre distinguere fatto generatore ed esigibilitÃ  (direttiva, artt. 62-71). Didatticamente: prima si identifica la fattispecie, poi il momento rilevante, quindi quando l'Erario puÃ² esigere l'imposta. Non si estende la regola di una categoria a tutte le altre.

## Base imponibile, debitore e rivalsa

La base imponibile Ã¨ costruita sul corrispettivo complessivo secondo le condizioni contrattuali, inclusi oneri e spese accessorie previsti dalla norma (D.P.R. 633/1972, art. 13; direttiva, artt. 72-92). L'art. 15 elenca somme che non concorrono alla base: esclusione dal computo e operazione fuori campo sono concetti distinti.

L'art. 17 individua il debitore d'imposta e contiene ipotesi nelle quali gli obblighi ricadono sul cessionario o committente. L'art. 18 disciplina la rivalsa. **Sintesi didattica:** rivalsa e detrazione sono meccanismi diversi: la prima riguarda l'addebito dell'imposta al cliente, la seconda il recupero dell'imposta assolta sugli acquisti. Eventuali inversioni contabili richiedono la specifica fattispecie, non ammettono automatismi.

## Detrazione e limiti concettuali

Il diritto alla detrazione nasce e si esercita alle condizioni dell'art. 19; gli artt. 19-bis, 19-bis.1 e 19-bis.2 disciplinano, rispettivamente, percentuale di detrazione, ipotesi di indetraibilitÃ  e rettifica. Nel quadro UE rilevano gli artt. 167 e seguenti, con condizioni formali nell'art. 178.

La formula operativa Ã¨: acquisto inerente ad attivitÃ  economica, imposta dovuta/assolta, destinazione a operazioni che attribuiscono il diritto, documento e registrazione richiesti, assenza di limiti specifici. La detrazione non Ã¨ un rimborso automatico nÃ© un diritto incondizionato; va distinta dalla compensazione di crediti nel versamento unitario.

## Documentazione, registrazioni, liquidazione e dichiarazione

La sequenza nazionale collega fatturazione (D.P.R. 633/1972, art. 21 e disposizioni contigue), registrazione delle operazioni attive (artt. 23 e 24), registrazione degli acquisti (art. 25), liquidazione e versamento periodico (D.P.R. 100/1998, art. 1) e dichiarazione annuale IVA (D.P.R. 322/1998, art. 8). L'art. 30 del D.P.R. 633/1972 disciplina il versamento di conguaglio e il rimborso dell'eccedenza: non Ã¨ la fonte generale dell'obbligo dichiarativo. La direttiva disciplina fatturazione e obblighi dichiarativi, tra gli altri, agli artt. 217 e seguenti e 250 e seguenti.

**Sintesi didattica.** Il documento alimenta i registri; le registrazioni consentono di confrontare imposta a debito e detraibile; la liquidazione determina il saldo periodico; la dichiarazione rappresenta annualmente i dati e le risultanze. Questa Ã¨ una mappa funzionale, non un calendario: termini, modelli, specifiche telematiche e regimi speciali sono claim mobili da verificare per periodo.

## Routing editoriale responsabile

- **Capitolo 4 â€” diritto tributario e teoria dell'imposta:** funzione dell'IVA, armonizzazione, presupposti, categorie di operazioni, base imponibile, rivalsa, detrazione e neutralitÃ  non assoluta.
- **Capitolo 6 â€” adempimenti fiscali:** sola sequenza operativa IVA di documentazione, registrazione, liquidazione e dichiarazione, raccordata a [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]. Non deve duplicare accertamento, controlli, sanzioni, riscossione o contabilitÃ  aziendale affidati ai capitoli 5, 5A, 5B e 7.

## Claim mobili esclusi o da datare

Questa nota non consolida aliquote, soglie, termini di trasmissione o versamento, modelli, codici tributo, specifiche telematiche, regimi temporanei, percentuali di detrazione o requisiti quantitativi. Possono entrare nel testo solo se necessari, verificati su fonte ufficiale per il periodo e marcati con data di riferimento.

## Mappa articoli â†’ claim

| Claim | D.P.R. 633/1972 | Direttiva 2006/112/CE |
|---|---|---|
| sistema e operazioni soggette | art. 1 | artt. 1-2 |
| cessioni/prestazioni e soggetti | artt. 2-5 | artt. 9, 14, 24-26 |
| territorialitÃ  | artt. 7-7-septies | artt. 31-61 |
| effettuazione/esigibilitÃ  | art. 6 | artt. 62-71 |
| non imponibilitÃ /esenzione | artt. 8, 8-bis, 9, 10 | artt. 131 ss. |
| base ed esclusioni dal computo | artt. 13 e 15 | artt. 72-92 |
| debitore e rivalsa | artt. 17-18 | art. 193 ss. |
| detrazione, limiti, rettifica | artt. 19-19-bis.2 | artt. 167 ss., 178 |
| fatture e registri | artt. 21, 23-25 | artt. 217 ss. |
| liquidazione periodica | D.P.R. 100/1998, art. 1 | quadro di esigibilitÃ  e obblighi della direttiva |
| dichiarazione annuale IVA | D.P.R. 322/1998, art. 8 | artt. 250 ss. |
| conguaglio/rimborso dell'eccedenza | art. 30 | artt. 183 ss., secondo condizioni |

## Limiti e review

Il consolidamento sostiene la struttura concettuale, non certifica ogni regime o caso transfrontaliero. Prima della pubblicazione: review umana tributaria/UE per territorialitÃ , esenzioni, inversione contabile, detrazione e decorrenze; verifica articolo-specifica se si introducono dati mobili.

## Riferimenti consolidati

- [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
- [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]]
- [[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]]
- [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]


## Source adempimenti
---
id: source-dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20
type: source
title: "Dichiarazioni, versamenti unitari e compensazioni: quadro vigente consolidato"
status: consolidated
domain: "concorsi pubblici italiani"
topics: ["dichiarazioni fiscali", "versamenti unitari", "compensazione tributaria", "modello F24"]
entities: ["Agenzia delle Entrate", "Normattiva"]
source_refs: ["sources/adempimenti-contabilita-civile-commerciale-m-fc02", "sources/normativa-tributaria-tuir-iva-accertamento-m-fc02", "sources/iva-dpr-633-1972-aggiornamento-2026-07-20"]
book_refs: ["m-fc02-agenzie-fiscali"]
confidence: 0.93
updated_at: 2026-07-20T00:00:00+02:00
created_at: 2026-07-20T00:00:00+02:00
review_required: true
canonical: true
tags: ["source", "official-source", "dichiarazioni", "f24", "compensazioni", "module-code-m-fc02", "cutoff-2026-07-20"]
source_type: official_legal_corpus
source_url: "mixed:https://www.normattiva.it/eli/id/1998/09/07/098G0373/CONSOLIDATED/20260720|https://www.normattiva.it/eli/id/1997/07/28/097G0277/CONSOLIDATED/20260720|https://www.normattiva.it/eli/id/2025/03/26/25G00044/CONSOLIDATED/20260523"
source_date: "2026-07-20"
audit_date: "2026-07-20"
latest_official_update_checked: "D.P.R. 322/1998: ultimo aggiornamento pubblicato 17/06/2025; D.Lgs. 241/1997: disciplina vigente al 20/07/2026; D.Lgs. 33/2025: testo unico applicabile dal 01/01/2027"
authority_level: very_high
raw_refs:
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html"
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html"
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali-akn-2026-07-20.xml"
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni-akn-2026-07-20.xml"
  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml"
---

# Dichiarazioni, versamenti unitari e compensazioni: quadro vigente consolidato

## Esito dell'audit e versione

**Data di consultazione:** 20 luglio 2026. I vecchi HTML verificano i metadati ma visualizzano integralmente soltanto l'art. 1. **D.P.R. 322/1998:** ELI `098G0373`, HTML a singola vigenza 2 luglio 2026, ultimo aggiornamento pubblicato 17 giugno 2025; AKN integrale di 12 articoli, expression `ita@2025-06-18`. **D.Lgs. 241/1997:** ELI `097G0277`; AKN integrale di 42 articoli, expression `ita@2026-01-10`. Il markup di abrogazione rinvia al D.Lgs. 33/2025, ma non basta a fissarne la decorrenza. **D.Lgs. 33/2025:** AKN ufficiale, alias ELI consolidato `20260523`; la FRBRExpression principale e quelle degli allegati sono `ita@2025-03-27`, mentre il markup successivo degli artt. 241 e 243 stabilisce che le abrogazioni e l'applicazione del testo unico operano dal 1Â° gennaio 2027.

I claim su dichiarazioni sono verificati sui nodi dell'AKN D.P.R. 322/1998. Al cutoff, i claim vigenti su versamento e compensazione sono verificati sugli artt. 17-24 del D.Lgs. 241/1997; gli artt. 3 e 5-10 del D.Lgs. 33/2025 sono mappati separatamente come disciplina futura dal 1Â° gennaio 2027.

## Funzione della dichiarazione

**Dato normativo.** Il D.P.R. 322/1998 disciplina forma, sottoscrizione, presentazione e vicende delle dichiarazioni: l'art. 1 per redditi e IRAP, l'art. 2 per presentazione e dichiarazioni successive, l'art. 3 per modalitÃ  e soggetti della trasmissione; l'art. 8 contiene la disciplina della dichiarazione IVA. Le regole speciali prevalgono sulla mappa generale.

**Sintesi didattica.** La dichiarazione non Ã¨ il tributo: Ã¨ l'atto con cui il contribuente rappresenta dati, componenti e risultanze secondo il modello normativamente previsto. Produce effetti propri e alimenta liquidazione e controllo. Presentazione, pagamento e successivo controllo sono fasi collegate ma distinte.

## Presentazione e regole strutturali

Il candidato deve ricostruire la sequenza: soggetto obbligato; dichiarazione e periodo; modello e sottoscrizione; canale e intermediario; ricevuta/prova della presentazione; conservazione; eventuale dichiarazione successiva. Gli artt. 1-3 del D.P.R. 322/1998 sostengono la struttura generale; per l'IVA la fonte dell'obbligo annuale Ã¨ l'art. 8. L'art. 30 del D.P.R. 633/1972 riguarda conguaglio e rimborso dell'eccedenza, non fonda in generale la dichiarazione annuale.

Modelli, istruzioni, software e scadenze appartengono al livello attuativo e mobile. Questa nota non li cristallizza.

## Originaria, correttiva, integrativa e omessa

- **Originaria:** prima dichiarazione presentata per il periodo e il tributo considerati.
- **Correttiva nei termini:** espressione operativa per una nuova dichiarazione presentata entro il termine ordinario, che sostituisce la precedente; la qualificazione dipende dalle istruzioni ufficiali del modello applicabile, non Ã¨ una categoria generale autosufficiente inventata dal manuale.
- **Integrativa:** dichiarazione successiva oltre il termine ordinario nei casi e nei limiti previsti. Per redditi/IRAP rileva l'art. 2, commi 8 e 8-bis, D.P.R. 322/1998; per IVA l'art. 8, commi 6-bis e seguenti. Effetti sul debito, sul credito, sull'utilizzo e sul controllo non sono identici in ogni caso.
- **Tardiva/omessa:** l'art. 2, comma 7, conserva validitÃ  alla dichiarazione presentata entro la finestra legale successiva, ferma la sanzione; oltre tale finestra la dichiarazione Ã¨ considerata omessa, ma costituisce titolo per la riscossione delle imposte dovute in base agli imponibili indicati. Il regime IVA va coordinato con l'art. 8 e con la disciplina sanzionatoria vigente.

**Nota di prudenza.** Correzione favorevole, correzione sfavorevole, emendabilitÃ , rimborso e utilizzo del credito seguono condizioni e termini propri. Non Ã¨ corretto affermare che ogni errore si corregga sempre con lo stesso tipo di integrativa o che il credito diventi immediatamente spendibile.

## Versamento unitario e funzione del modello F24

**Disciplina vigente al 20 luglio 2026.** L'art. 17 del D.Lgs. 241/1997 disciplina versamento unitario e compensazione; l'art. 18 i termini, l'art. 19 la delega e l'art. 20 la rateazione. L'art. 24 appartiene alle disposizioni transitorie e non va usato come fonte generale del modello F24.

**Disciplina futura.** Il D.Lgs. 33/2025, art. 243, dispone che il testo unico si applica dal 1Â° gennaio 2027. L'art. 241 collega espressamente alla stessa data l'abrogazione degli artt. 17-28 e 30 del D.Lgs. 241/1997. Solo da quella data il routing passa agli artt. 3 (versamento unitario e compensazione), 5-7 (modalitÃ , limiti e controlli secondo fattispecie), 8 (termini), 9 (delega, anche a saldo zero) e 10 (rateazione) del testo unico.

**Sintesi didattica.** Il modello F24 Ã¨ lo strumento unitario con cui si espongono debiti, crediti utilizzabili e saldo e si conferisce la delega di pagamento. Non Ã¨ un repertorio da memorizzare per codici tributo. Un saldo nullo non rende irrilevante l'adempimento: trasmissione e controlli seguono le regole vigenti.

## Compensazione verticale e orizzontale

- **Verticale (interna):** il credito relativo a un tributo riduce un debito dello stesso tributo; la disciplina puÃ² operare nella liquidazione o dichiarazione del tributo.
- **Orizzontale (esterna):** il credito relativo a un'imposta o contributo Ã¨ usato, nel sistema del versamento unitario, contro debiti di diversa natura ammessi dall'art. 17 del D.Lgs. 241/1997.

La distinzione Ã¨ didattica e funzionale. Non autorizza l'uso di qualunque credito contro qualunque debito. Prima dell'utilizzo vanno verificati esistenza, spettanza, disponibilitÃ , esposizione dichiarativa quando richiesta, perimetro compensabile, eventuali adempimenti preventivi, canale e cause ostative.

**Esempio ammesso.** Un'eccedenza IVA puÃ² essere riportata, chiesta a rimborso o impiegata secondo le opzioni e condizioni applicabili; l'uso per ridurre un debito IVA e l'uso in F24 contro un debito diverso non sono la stessa operazione. L'esempio non afferma soglie o libera disponibilitÃ .

## Limiti e controlli senza automatismi

La compensazione Ã¨ soggetta a limiti quantitativi, temporali e procedurali e a controlli preventivi o successivi previsti dalla normativa vigente. Le condizioni possono dipendere da tipo e importo del credito, dichiarazione, visto o altra attestazione, situazione debitoria e canale telematico. Questa nota esclude valori numerici non verificati e non trasforma il controllo in diniego automatico.

Un credito **non spettante** e un credito **inesistente** non sono sinonimi; qualificazione, recupero, sanzione e termini competono alla disciplina vigente e al capitolo responsabile. Anche lo scarto o la sospensione di una delega non equivalgono, senza la norma del caso, a una decisione definitiva sull'intero rapporto tributario.

## Errore, correzione, rimborso e raccordo con controllo/sanzione

La catena corretta Ã¨: individuare errore e dichiarazione interessata; stabilire se il termine ordinario Ã¨ aperto; scegliere lo strumento previsto; rideterminare debito o credito; verificare pagamento, compensazione o rimborso; considerare controllo e sanzione separatamente. Dichiarazione integrativa, ravvedimento, istanza di rimborso e autotutela hanno funzioni diverse e non sono intercambiabili.

Questa nota consolida classificazione e routing, non la disciplina completa di controllo, recupero e sanzioni. Nessuna correzione cancella automaticamente interessi o sanzioni; nessun credito dichiarato genera automaticamente rimborso o compensabilitÃ .

## Routing editoriale responsabile

- **Capitolo 5 â€” accertamento, controlli e compliance:** selezione, liquidazione e controllo delle dichiarazioni; poteri e atti. Riceve il caso dopo la fase dichiarativa.
- **Capitolo 5A â€” sanzioni:** qualificazione della violazione, elemento soggettivo quando rilevante, ravvedimento e conseguenze sanzionatorie.
- **Capitolo 5B â€” riscossione:** recupero e riscossione delle somme risultanti, accertate o indebitamente compensate.
- **Capitolo 6 â€” adempimenti fiscali:** funzione, presentazione e correzione della dichiarazione; versamento unitario; F24; distinzione verticale/orizzontale; sequenza errore-correzione. Ãˆ il capitolo responsabile di questa nota.
- **Capitolo 7 â€” contenzioso/rimedi:** tutela contro atti e dinieghi secondo la disciplina processuale e amministrativa pertinente.

Il capitolo 6 non deve assorbire la disciplina completa dei capitoli 5, 5A, 5B e 7; questi ultimi non devono ripetere la meccanica ordinaria dell'adempimento.

## Claim mobili esclusi o da datare

Sono esclusi: scadenze annuali, calendario dei versamenti, soglie e massimali di compensazione o rimborso, codici tributo, modelli, campi, specifiche e canali telematici, importi per visto/attestazioni, sospensioni e cause ostative variabili. Se didatticamente necessari, vanno verificati su fonte ufficiale corrente e accompagnati dalla data di riferimento.

## Mappa vigente al 20 luglio 2026

| Claim | Fonte e articoli |
|---|---|
| forma e sottoscrizione | D.P.R. 322/1998, art. 1 |
| presentazione, tardiva/omessa, integrativa redditi/IRAP | D.P.R. 322/1998, art. 2, commi 7, 8 e 8-bis |
| trasmissione e intermediari | D.P.R. 322/1998, art. 3 |
| dichiarazione e integrativa IVA | D.P.R. 322/1998, art. 8, in particolare commi 1, 6 e 6-bis ss. |
| versamento unitario e compensazione | D.Lgs. 241/1997, art. 17 |
| termini del versamento | D.Lgs. 241/1997, art. 18 |
| delega di pagamento/F24, incluso saldo zero | D.Lgs. 241/1997, art. 19 |
| rateazione | D.Lgs. 241/1997, art. 20 |
| assistenza e visto di conformitÃ  | D.Lgs. 241/1997, artt. 35-39, secondo fattispecie |

## Mappa futura dal 1Â° gennaio 2027

| Claim | Fonte futura |
|---|---|
| decorrenza del testo unico | D.Lgs. 33/2025, art. 243 |
| abrogazione degli artt. 17-28 e 30 D.Lgs. 241/1997 | D.Lgs. 33/2025, art. 241, comma 1, lett. t), dalla data dell'art. 243 |
| versamento unitario e compensazione | D.Lgs. 33/2025, art. 3 |
| modalitÃ , limiti e controlli dei versamenti unitari | D.Lgs. 33/2025, artt. 5-7, secondo fattispecie |
| termini, delega e rateazione | D.Lgs. 33/2025, artt. 8-10 |

## Limiti e review

Lo stato `consolidated` sostiene le distinzioni e la sequenza, non certifica regole mobili o ogni effetto dell'emendabilitÃ . Prima della pubblicazione: review umana tributaria su dichiarazioni successive, crediti non spettanti/inesistenti, rimborso e raccordo sanzionatorio; verifica ufficiale datata per ogni termine, soglia o requisito operativo introdotto.

## Riferimenti consolidati

- [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]]
- [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
- [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]
