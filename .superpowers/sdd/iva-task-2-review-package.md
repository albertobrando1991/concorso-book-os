# IVA Task 2 review package post-fix

## Git status
```text
 M wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
```

## Diffstat
```text
 .../04-diritto-tributario-teoria-imposta.md        | 69 +++++++++++++++++++---
 1 file changed, 60 insertions(+), 9 deletions(-)
```

## Implementer report
# IVA Task 2 report â€” architettura IVA nel capitolo 4

## Esito

**DONE_WITH_CONCERNS**

- SPEC COMPLIANCE: PASS
- QUALITY: PASS
- Concern non bloccante per questo task: l'anchor di destinazione `#Operazioni IVA e ciclo degli adempimenti` non esiste ancora nel capitolo 6 corrente; e' l'interfaccia prevista dal Task 3 del piano e il link e' gia' predisposto.

## Baseline

File: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`

- SHA-256 iniziale del file su disco: `3565DB22EF3FF2A928AB4288D00EE4F99059F40CDFEC9923E054280D4CDE2555`.
- SHA-256 della rappresentazione baseline `HEAD` normalizzata LF: `3ACBE96292F165CD82D2EF1A72266DF48FE97587EECF663E42063A27B8CAAA5F`.
- Diff iniziale del capitolo: assente.
- Stato iniziale: il capitolo non risultava modificato; il worktree conteneva modifiche estranee, lasciate intatte.
- Promesse IVA iniziali: operazione, soggetto passivo, rivalsa, detrazione, liquidazione, dichiarazione, fatturazione, registrazione e controllo erano nominati; risultava spiegata soltanto una sequenza operativa generica. Armonizzazione/consumo, neutralita' condizionata, tre presupposti, ruoli distinti e quattro classi non erano sviluppati nel blocco responsabile.

## Fonti consolidate consumate

Esclusivamente:

- `[[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]`;
- `[[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]`;
- `[[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]]`.

Nessun raw e nessuna ricerca web sono stati usati per la scrittura.

## Mappa requisiti â†’ sezioni

| Requisito | Sezione implementata |
|---|---|
| IVA armonizzata sui consumi | apertura di `## IVA: operazioni, soggetti, detrazione e adempimenti` |
| neutralita' come meccanismo e limiti | `### Neutralita' come meccanismo, non come risultato assoluto` |
| tre presupposti | `### I tre presupposti: oggettivo, soggettivo e territoriale` |
| soggetto passivo/debitore/consumatore | `### Soggetto passivo, debitore e consumatore finale` |
| rivalsa â†’ detrazione â†’ liquidazione | schema nel blocco neutralita' |
| quattro classi e conseguenze | `### Le quattro classi di operazioni` |
| rinvio preciso al capitolo 6 | `### Dalla teoria agli adempimenti: rinvio responsabile` |
| definizione, funzione, distinzione, conseguenza, esempio, errore, verifica | integrate in ciascun nucleo, con verifica finale cumulativa |
| tracciabilita' e data | `source_refs`, `last_compiled_from`, riferimenti, note review; `updated_at` 2026-07-21 |

`status: revised_draft` e `confidence: 0.95` non sono stati aumentati.

## Controlli

- Presenza nuclei richiesti: PASS.
- Assenza di aliquote, soglie, termini, modelli, codici o regole telematiche mobili introdotti nel blocco: PASS.
- Distinzione non imponibile/esente/esclusa: PASS.
- Detrazione e neutralita' non descritte come incondizionate: PASS.
- Casistica applicativa del capitolo 6 non duplicata: PASS; presente soltanto la mappa funzionale.
- Routing verso capitoli 5, 5A, 5B e 7 preservato: PASS.
- UTF-8 senza BOM e nessun carattere sostitutivo rilevato: PASS.
- `git diff --check -- <capitolo>`: PASS, nessun output sostanziale (solo warning CRLF/LF del client Git).
- Blocco IRPEF/IRES: PASS; SHA-256 del segmento baseline e finale identico: `7BEEB06F7A9ECBAC8E5B55C88904FCC73BACA6D0375BDA4D62DADD01AE001780`.
- Diff finale capitolo: `56` inserimenti, `9` eliminazioni.
- SHA-256 finale su disco: `B8BA23F23765F7EFD973828D327BE10799B2305FCBAEF3F231945088B8E8B56F`.

## Review separate

### SPEC COMPLIANCE: PASS

Tutti i nuclei richiesti dal brief sono spiegati nel blocco responsabile; frontmatter e riferimenti includono le due nuove source note e la source UE; nessuno status/confidence e' stato promosso; nessun file editoriale estraneo e' stato toccato.

### QUALITY: PASS

Progressione leggibile: funzione â†’ meccanismo â†’ presupposti â†’ ruoli â†’ classificazione â†’ routing. Gli esempi sono classificatori, non sostituiscono la verifica della fattispecie; errori e verifiche sono specifici; non sono presenti automatismi su neutralita', detrazione o compensazione.

## Concern e note operative

1. L'anchor del capitolo 6 e' un forward contract del Task 3: al controllo odierno il relativo heading non e' ancora presente. Il Task 3 dovra' creare esattamente `## Operazioni IVA e ciclo degli adempimenti` o aggiornare contestualmente il link.
2. `LocalAgentMemory` e' stato individuato e il deposito canonico e' rimasto attivo, ma non era disponibile un runner TypeScript (`tsx`) installato per invocare il servizio senza modificare dipendenze. Il tentativo e il limite sono documentati; non e' stata creata memoria parallela.
3. `apply_patch` e' stato tentato due volte (percorso assoluto e relativo) e bloccato prima della lettura dal wrapper Windows: `cannot enforce split writable root sets`. In conformita' al brief e' stato usato un fallback chirurgico tramite `System.IO` sui soli due file autorizzati.
4. Nessun commit e' stato creato, come richiesto dal task delegato.
## Fix review â€” raccordo direttiva/norma nazionale

Finding Important risolto con un'integrazione circoscritta all'apertura del blocco IVA:

- mini-esempio sul percorso direttiva 2006/112/CE â†’ D.P.R. 633/1972;
- errore-trappola sulla falsa equivalenza tra direttiva e regolamento e sull'omissione di primato/interpretazione conforme;
- verifica in tre passaggi: tipo/funzione della fonte UE, norma nazionale pertinente, compatibilita' unionale.

Test di presenza: PASS per le stringhe `Mini-esempio di raccordo`, `Errore-trappola`, `primato e interpretazione conforme` e `Verifica` nel blocco IVA.

`git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md .superpowers/sdd/iva-task-2-report.md`

Output: vuoto; exit code `0` (PASS).

Controlli di non regressione: blocco IRPEF/IRES invariato; `status: revised_draft` e `confidence: 0.95` invariati; forward anchor del Task 3 mantenuto; nessun commit.

## Full diff
```diff
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
index e1de011..a807f0b 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
@@ -1,39 +1,39 @@
 ---
 id: chapter-m-fc02-diritto-tributario-teoria-imposta
 type: book_chapter
 title: "Diritto tributario e teoria dell'imposta"
 status: revised_draft
 domain: "concorsi pubblici italiani"
 topics: ["diritto tributario","teoria imposta","agenzie fiscali","obbligazione tributaria","imposte sui redditi","IRPEF","IRES","categorie reddituali","reddito complessivo","reddito d'impresa","iva","diritto tributario UE","IVA armonizzata","diritto doganale UE"]
 entities: ["Agenzia delle Entrate","Agenzia delle Dogane e dei Monopoli","Agenzia delle Entrate-Riscossione","Normattiva","Unione europea","Commissione europea","EUR-Lex"]
-source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","sources/costituzione-repubblica-italiana-testo-vigente.md","sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
+source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md","sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md","sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","sources/costituzione-repubblica-italiana-testo-vigente.md","sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
 book_refs: ["m-fc02-agenzie-fiscali","il-metodo-bando"]
 asset_refs:
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/01-mappa-bando-diritto-tributario.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/02-sequenza-nascita-tributo.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/03-categorie-del-tributo.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/04-presupposto-base-aliquota.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/05-tuir-iva-accertamento-riscossione.png"
 confidence: 0.95
-updated_at: 2026-07-20T00:00:00+02:00
+updated_at: 2026-07-21T00:00:00+02:00
 created_at: 2026-07-01T21:00:00+02:00
 review_required: true
 canonical: true
 tags: ["book-chapter","module-code-m-fc02","professional-draft","revised-draft","illustrated"]
 book_id: m-fc02-agenzie-fiscali
 companion_to: il-metodo-bando
 outline_section: 4
 draft_stage: revised-editorial-draft
 module_code: M-FC02
 module_family: funzioni-centrali
-last_compiled_from: ["wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","wiki/entities/agenzia-delle-entrate.md","wiki/topics/diritto-tributario-concorsi-agenzie-fiscali.md","wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/02-bando-decoder-fiscale.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/03-ordinamento-organizzazione-ae-adm-ader.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md","wiki/sources/costituzione-repubblica-italiana-testo-vigente.md","wiki/sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","wiki/sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","wiki/sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
+last_compiled_from: ["wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md","wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md","wiki/entities/agenzia-delle-entrate.md","wiki/topics/diritto-tributario-concorsi-agenzie-fiscali.md","wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/02-bando-decoder-fiscale.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/03-ordinamento-organizzazione-ae-adm-ader.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md","wiki/sources/costituzione-repubblica-italiana-testo-vigente.md","wiki/sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","wiki/sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","wiki/sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
 ---
 
 # Diritto tributario e teoria dell'imposta
 
 ## Apertura editoriale
 
 Nel modulo Agenzie fiscali il diritto tributario non e' una materia da studiare come un blocco astratto. E' il linguaggio di lavoro dell'amministrazione fiscale. Serve a capire perche' nasce un'imposta, chi deve pagarla, su quale base si calcola, quale adempimento viene richiesto, quali controlli puo' svolgere l'amministrazione e come si passa dalla regola generale al caso concreto.
 
 Il candidato che prepara un concorso dell'Agenzia delle Entrate, dell'Agenzia delle Dogane e dei Monopoli o dell'Agenzia delle Entrate-Riscossione non deve diventare un commentatore del TUIR. Deve pero' saper usare le categorie fondamentali senza confonderle. "Tributo", "imposta", "presupposto", "base imponibile", "soggetto passivo", "obbligazione tributaria", "dichiarazione", "accertamento" e "riscossione" non sono parole intercambiabili. Sono passaggi di una sequenza.
 
@@ -351,33 +351,81 @@ Questo capitolo spiega perche' il raccordo esiste. La meccanica contabile e gli
 **Caso.** Una persona fisica riceve nello stesso periodo un compenso da lavoro dipendente, il provento di un investimento e una somma per una prestazione occasionale. Da quale importo deve partire per calcolare subito l'IRPEF?
 
 **Soluzione.** Non si parte dalla somma aritmetica degli incassi ne' dall'aliquota. Si identificano fonte e causa di ciascun provento, si verifica la categoria applicabile, si determina ogni reddito con le regole proprie e solo dopo si forma il reddito complessivo nei limiti previsti. Seguono oneri deducibili, imponibile, imposta lorda, detrazioni e altri scomputi. La prestazione occasionale non diventa lavoro autonomo abituale per il solo fatto di essere remunerata e neppure confluisce automaticamente nei redditi diversi senza verificare la fattispecie normativa.
 
 ### Errore tipico
 
 Confondere il denaro ricevuto con il reddito imponibile. L'incasso e' un fatto finanziario; il reddito e' una grandezza qualificata e determinata dalla disciplina tributaria. Prima di calcolare occorre rispondere, nell'ordine: chi e' il soggetto, quale fonte ha prodotto il provento, in quale categoria rientra, quale criterio di determinazione e imputazione si applica.
 
 ## IVA: operazioni, soggetti, detrazione e adempimenti
 
-L'IVA richiede un ragionamento diverso dalle imposte sui redditi. Il candidato deve spostare l'attenzione sulle operazioni, sui soggetti e sul meccanismo applicativo dell'imposta.
+L'IVA e' un'imposta armonizzata sui consumi: la direttiva 2006/112/CE costruisce il sistema comune, mentre il D.P.R. 633/1972 ne disciplina l'applicazione nazionale negli spazi consentiti. Non e' quindi soltanto una percentuale aggiunta al prezzo. La sua funzione e' far gravare il prelievo, attraverso applicazione e detrazione nelle diverse fasi, sul consumo finale. Una direttiva, tuttavia, non opera come un regolamento: nel caso concreto occorre raccordare istituto unionale e norma nazionale di attuazione.
 
-Nel modulo M-FC02 l'IVA va studiata in modo operativo. Le parole guida sono: operazione, soggetto passivo, rivalsa, detrazione, liquidazione, dichiarazione, fatturazione, registrazione, controllo. Non serve anticipare qui tutto il capitolo sugli adempimenti, ma serve capire che l'IVA non si riduce a "una percentuale sul prezzo".
+**Mini-esempio di raccordo.** Per qualificare una cessione, il candidato riconosce prima la categoria armonizzata nella direttiva 2006/112/CE e verifica poi come il D.P.R. 633/1972 la disciplina nell'ordinamento nazionale: la direttiva orienta il quadro comune, la norma interna governa l'applicazione del caso negli spazi consentiti.
 
-La logica base e':
+**Errore-trappola:** trattare la direttiva come un regolamento direttamente applicabile in modo identico, oppure ignorare primato e interpretazione conforme. **Verifica:** indica tipo e funzione della fonte UE, individua la disposizione nazionale pertinente e controlla che la lettura interna sia compatibile con il quadro unionale, senza attribuire automaticamente alla direttiva gli effetti propri di un regolamento.
+
+### Neutralita' come meccanismo, non come risultato assoluto
+
+Per l'operatore economico la neutralita' deriva dalla combinazione tra **rivalsa** e **detrazione**. Con la rivalsa il cedente o prestatore addebita l'imposta al cliente; con la detrazione recupera, alle condizioni previste, l'imposta dovuta o assolta sugli acquisti destinati a operazioni che attribuiscono tale diritto. La liquidazione confronta poi imposta a debito e imposta detraibile.
 
 ```text
-operazione rilevante -> soggetto -> applicazione dell'imposta -> documentazione -> detrazione/liquidazione -> dichiarazione -> controllo
+rivalsa sulle operazioni attive -> detrazione sugli acquisti ammessi -> liquidazione del saldo
 ```
 
-Questa sequenza aiuta a risolvere quiz e casi. Se una domanda riguarda l'IVA, chiediti sempre: qual e' l'operazione? chi e' il soggetto? quale documento entra in gioco? quale adempimento segue? quale controllo potrebbe svolgere l'amministrazione?
+La neutralita' non e' incondizionata: esenzioni, indetraibilita', percentuale di detrazione, requisiti documentali e rettifiche possono lasciare l'onere, in tutto o in parte, sull'operatore. La detrazione non e' ne' un rimborso automatico ne' una compensazione liberamente utilizzabile.
+
+**Mini-esempio.** Un professionista acquista un bene per l'attivita' e presta un servizio imponibile. L'imposta sull'acquisto puo' entrare nel confronto con quella addebitata al cliente soltanto se ricorrono inerenza, destinazione, documento, registrazione e gli altri requisiti applicabili.
+
+**Errore tipico:** affermare che l'IVA e' sempre neutrale per chiunque eserciti un'attivita'. **Verifica:** indica almeno una condizione della detrazione e un limite capace di interrompere o ridurre la neutralita'.
+
+### I tre presupposti: oggettivo, soggettivo e territoriale
+
+Una normale operazione interna entra nel campo IVA quando si coordinano tre profili:
+
+- il **presupposto oggettivo**, cioe' una cessione di beni o prestazione di servizi riconducibile alle fattispecie legali;
+- il **presupposto soggettivo**, cioe' l'esercizio abituale di impresa, arte o professione da parte del soggetto che effettua l'operazione;
+- il **presupposto territoriale**, cioe' la localizzazione dell'operazione nel territorio dello Stato secondo le regole proprie della fattispecie.
+
+Le importazioni sono assoggettate dall'art. 1 del D.P.R. 633/1972 da chiunque effettuate e richiedono quindi una lettura distinta dalla sequenza ordinaria delle operazioni interne. Anche il momento di effettuazione e l'esigibilita' sono passaggi ulteriori: non vanno confusi con la verifica dei tre presupposti.
+
+**Mini-esempio.** Una prestazione resa nell'esercizio abituale di una professione soddisfa il profilo soggettivo, ma non basta per concludere: occorre ancora qualificare la prestazione e applicare la regola di territorialita' pertinente.
+
+**Errore tipico:** ritenere territoriale ogni operazione solo perche' una parte e' italiana. **Verifica:** davanti a un caso, formula tre domande separate: che operazione e', chi la compie e dove si considera effettuata?
+
+### Soggetto passivo, debitore e consumatore finale
+
+Il **soggetto passivo** esercita in modo indipendente un'attivita' economica rilevante e partecipa al meccanismo IVA. Il **debitore d'imposta** e' invece il soggetto sul quale, nella specifica operazione, ricadono gli obblighi verso l'Erario: normalmente coincide con chi effettua l'operazione, ma la legge puo' porre gli obblighi sul cessionario o committente. Il **consumatore finale** sopporta economicamente l'imposta senza inserirla, di regola, in una successiva catena di detrazione.
+
+**Mini-esempio.** Nella vendita al consumatore, l'impresa e' soggetto passivo e normalmente debitore; il cliente finale paga il prezzo comprensivo dell'imposta e ne resta inciso economicamente. Una specifica inversione degli obblighi puo' mutare il debitore, non trasformare automaticamente il cliente in consumatore finale.
+
+**Errore tipico:** usare come sinonimi soggetto passivo, debitore e soggetto inciso. **Verifica:** per ciascuna figura indica rispettivamente posizione nel sistema, obbligo verso l'Erario e incidenza economica.
+
+### Le quattro classi di operazioni
+
+| Classe | Definizione e funzione | Conseguenza essenziale |
+|---|---|---|
+| **Imponibile** | Ricorrono i presupposti e si applica il regime ordinario. | L'imposta e' addebitata secondo le regole applicabili e l'operazione alimenta il meccanismo di detrazione-liquidazione. |
+| **Non imponibile** | L'operazione resta rilevante nel sistema, ma la legge non applica l'imposta, tipicamente nella logica della tassazione a destinazione. | In linea generale conserva il diritto a detrazione, da verificare sulla fattispecie. |
+| **Esente** | L'operazione e' nel campo IVA ma beneficia di un'esenzione tipizzata. | Non comporta addebito dell'imposta e puo' limitare la detrazione sugli acquisti. |
+| **Esclusa o fuori campo** | Manca un presupposto o una norma sottrae la fattispecie al campo applicativo. | Non segue il regime delle operazioni imponibili; gli effetti documentali e sulla detrazione dipendono dalla ragione dell'esclusione. |
+
+**Mini-esempio comparativo.** Una vendita interna imponibile, un'esportazione non imponibile, una prestazione sanitaria che ricade nell'esenzione tipica e una prestazione priva di territorialita' italiana appartengono a classi diverse. L'esempio serve a classificare, non a sostituire la verifica dei requisiti del caso.
+
+**Errore tipico:** trattare non imponibilita', esenzione ed esclusione come tre modi equivalenti di dire "IVA non addebitata". **Verifica:** spiega quale delle tre categorie resta normalmente collegata al diritto a detrazione e quale presuppone che l'operazione sia fuori dal campo applicativo. Le somme escluse dal computo della base imponibile ai sensi dell'art. 15 non formano, per cio' solo, una quinta classe di operazioni.
+
+### Dalla teoria agli adempimenti: rinvio responsabile
+
+La mappa teorica termina qui con la catena **fatturazione -> registrazione -> liquidazione -> dichiarazione annuale**. La funzione, l'ordine e le regole operative di documentazione, registrazione delle operazioni attive e degli acquisti, liquidazione periodica e dichiarazione IVA sono sviluppati nel [[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni#Operazioni IVA e ciclo degli adempimenti|capitolo 6, sezione "Operazioni IVA e ciclo degli adempimenti"]]. Il rinvio non comprende accertamento, sanzioni, riscossione o rimedi, affidati ai rispettivi capitoli 5, 5A, 5B e 7.
+
+**Verifica finale.** In novanta secondi ricostruisci: funzione dell'IVA; tre presupposti; differenza tra soggetto passivo, debitore e consumatore; rivalsa, detrazione e liquidazione; quattro classi e conseguenza essenziale. Se inizi da aliquota o calendario, stai saltando l'architettura.
 
-L'errore tipico e' studiare l'IVA solo come aliquota. L'aliquota conta, ma nel concorso conta anche il meccanismo. L'amministrazione fiscale non guarda solo al numero finale; guarda al comportamento del soggetto, alla documentazione, alla liquidazione, alla coerenza dei dati e agli adempimenti.
 
 ## Livello 3 - Quadro UE fiscale, IVA e dogane
 
 ### Attribuzione e principi di esercizio
 
 L'Unione europea agisce soltanto nei limiti delle competenze che gli Stati membri le hanno attribuito. Il principio di attribuzione risponde quindi alla prima domanda: l'Unione puo' intervenire in questa materia e con quale fondamento? Nelle competenze non esclusive opera anche la sussidiarieta: l'intervento unionale deve risultare giustificato rispetto a obiettivi che gli Stati non possono conseguire in misura sufficiente. La proporzionalita impone inoltre che contenuto e forma dell'azione non eccedano quanto necessario per raggiungere gli obiettivi dei Trattati.
 
 La cooperazione leale completa il quadro: Unione e Stati membri devono assistersi reciprocamente nell'adempimento dei compiti derivanti dai Trattati. Per il candidato questi principi non sono formule isolate. Servono a spiegare perche' una materia possa essere disciplinata in modo uniforme, armonizzata oppure lasciata, entro determinati limiti, alla normativa nazionale.
 
 ### Competenze: unione doganale, mercato interno e imposte indirette
@@ -652,34 +700,37 @@ Prima di passare al capitolo 5, verifica questi punti.
 - Ho registrato nel diario almeno un errore reale.
 
 Se manca uno di questi punti, il rischio e' portare nei capitoli successivi una confusione di base. Meglio correggerla qui.
 
 ## Riferimenti consolidati
 
 Questo capitolo e' costruito sulle note e sulle pagine consolidate del wiki del progetto:
 
 - [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
 - [[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]
+- [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]
+- [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]
 - [[topics/diritto-tributario-concorsi-agenzie-fiscali]]
 - [[entities/agenzia-delle-entrate]]
 - [[sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026]]
 - [[sources/costituzione-repubblica-italiana-testo-vigente]]
 - [[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]]
 - [[sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo]]
 - [[sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/02-bando-decoder-fiscale]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/03-ordinamento-organizzazione-ae-adm-ader]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco]]
 
 Le fonti consolidate sostengono il nucleo teorico e concorsuale del capitolo. Per citazioni articolo-per-articolo e per dettagli su TUIR, IVA, accertamento, riscossione, riforma fiscale e decreti attuativi, resta necessaria una verifica su Normattiva e sulle fonti istituzionali aggiornate prima della pubblicazione.
 
 ## Note di review
 
 - Verificare su Normattiva il testo vigente del D.P.R. 917/1986, del D.P.R. 633/1972, del D.P.R. 600/1973 e della L. 111/2023 prima di inserire articoli, commi, soglie, date o esempi numerici.
 - Il quadro IRPEF/IRES consolida l'architettura stabile, non aliquote, scaglioni, soglie, importi, percentuali, termini o regimi mobili: verificarli sulla fonte ufficiale vigente prima della pubblicazione.
+- Il quadro IVA e' compilato sulle source note consolidate con audit al 20 luglio 2026; sottoporre a review umana tributaria/UE territorialita', esenzioni, inversione contabile, detrazione e decorrenze prima della pubblicazione.
 - Sottoporre a review normativa articolo per articolo soggetti, residenza, categorie, formazione del reddito complessivo e raccordo civilistico-fiscale; verificare separatamente derivazione rafforzata ed eccezioni quando il bando richiede dettaglio.
 - Coordinare la terminologia con i capitoli 5, 6 e 7, cosi' che accertamento, adempimenti e riscossione mantengano lo stesso significato in tutto il modulo.
 - Integrare eventuali riferimenti allo Statuto dei diritti del contribuente solo dopo una source note consolidata dedicata, per evitare richiami non tracciati.
 - I quiz presenti in questa bozza sono didattici e non articolo-specifici; prima dell'export finale possono essere ampliati con quesiti normativi puntuali dopo review umana.
 - Il capitolo ha taglio concorsuale e non costituisce consulenza fiscale.

```