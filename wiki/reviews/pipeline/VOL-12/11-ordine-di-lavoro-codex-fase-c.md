---
id: pipeline-vol-12-11-ordine-di-lavoro-codex
type: pipeline_handover
title: "VOL-12 — Ordine di lavoro per Codex: fonti, scrittura, chiusura dei moduli"
volume_code: VOL-12
phase: C
scope: volume
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "handover", "codex", "fase-c"]
---

# VOL-12 — Ordine di lavoro per Codex

Documento eseguibile. Chi lo esegue scrive; chi lo ha scritto revisiona alla fine. Non è una traccia da interpretare: dove dice «scarica», si scarica; dove dice «non inventare», il gate lo verifica.

## 0. Divisione del lavoro

| | |
| --- | --- |
| **Esegue** | Codex: reperimento fonti, source note, scrittura dei capitoli, aggiornamento delle matrici, estensione della scheda di pipeline, esecuzione dei gate. |
| **Revisiona** | Claude Code, alla fine di ogni modulo e alla fine del volume: verità delle fonti, tenuta dei gate, coerenza fra matrice, capitoli e piano, assenza di contenuto inventato. |
| **Non fa nessuno dei due** | Forzare un gate, chiudere uno step con `--accept` senza la verifica manuale documentata, dichiarare `completo` un nucleo il cui capitolo non esiste. |

Lo stato di partenza è quello del 13 agosto 2026: **tre capitoli scritti su quaranta**, tutti in M-SP02, tutti conformi al formato 2 e verificati con i gate.

---

## 1. Il contratto del capitolo — la parte che è stata sbagliata una volta

I due capitoli pilota erano stati scritti dichiarando `format_version: 2` senza rispettarne la sintassi, e valevano zero su ogni metrica. La descrizione discorsiva del formato non basta: quello che conta è **la forma che il gate riconosce**. Ecco la forma, verificata sul codice dei gate.

### 1.1 Frontmatter obbligatorio

```yaml
id: m-spXX-cap-NN-slug
type: chapter
title: "Titolo leggibile"
book_id: m-spXX-...
module_code: M-SPXX
binario: comune | base | isp | op | dir | A | B | C
status: draft
format_version: 2
outline_section: NN
domain: "concorsi pubblici italiani"
nuclei: ["N-SPXX-NN-NN", ...]          # almeno 5, esistenti in matrice
source_refs: ["sources/....md", ...]    # almeno uno, obbligatorio
book_refs: [...]
cut_off_date: AAAA-MM-GG
updated_at: ...
created_at: ...
review_required: true
canonical: false
draft_stage: pilot-draft                # obbligatorio, blocca se manca
last_compiled_from: ["wiki/sources/....md", "wiki/raw/..."]   # warning se manca
tags: [...]
```

### 1.2 Struttura del corpo

1. Un solo `#` H1. Nessun salto di gerarchia: dopo un `##` non può venire un `####`.
2. Sezione `## Obiettivo del capitolo` — **obbligatoria**, il gate cerca la parola «obiettivo» fra i titoli.
3. Sezione `## Mappa BANDO del capitolo` — **obbligatoria**, tabella a cinque righe: B Bando, A Aree, N Nuclei, D Diario, O Output.
4. Almeno **cinque nuclei**, ciascuno con heading nella forma esatta:

   ```
   ## N-SP02-04-01 · Titolo del nucleo
   ```

   ID conforme a `N-XX00-00-00`, separatore **`·`** (punto mediano U+00B7) con spazi, titolo dopo. Un heading che comincia per `N-` ma non rispetta la forma è un **blocker** dedicato.
5. Ogni nucleo **almeno 600 parole**, contate dall'heading fino al successivo heading di pari o superiore livello. Oltre 1.800 parole scatta un warning; se il nucleo più lungo supera di tre volte il più breve, un altro warning.
6. Almeno un heading che comincia con `▣ Verifica` — carattere U+25A3. Convenzione del volume: `## ▣ Verifica NN.A · Quiz ragionati` e `## ▣ Verifica NN.B · Domande aperte`.
7. Almeno **sei quiz**: il gate conta le occorrenze di `Risposta corretta:`. Ogni quiz è quattro opzioni A-D più una riga `**Risposta corretta: X.**` con la spiegazione del perché le altre sono sbagliate.
8. Almeno **un caso**: il gate cerca `Caso ragionato` o `Caso guidato`. Va dentro un nucleo, come `###`.
9. Almeno **3.000 parole** di corpo. Nella pratica un capitolo conforme ne fa 4.500-6.000.
10. Fra un blocco di verifica e l'altro non più di sette nuclei consecutivi.

### 1.3 Contratto del lettore — cosa fa fallire il lint

- **Nessun link `[[...]]` a materiale interno** nel corpo: niente `sources/`, `topics/`, `entities/`, `reviews/`. La tracciabilità sta nel frontmatter.
- **Nessuna dipendenza dichiarata** da note di fonte, corpus, o strumenti interni. Il gate intercetta anche le formulazioni indirette («le risposte si trovano nel…»). Evita del tutto le parole `wiki`, `dashboard`, `report` nel corpo.
- Nessun segnaposto: `TODO`, `TBD`, `FIXME`, `[da completare]`.
- Nessun meta-commento da agente («ecco il capitolo», «aggiornamento generato»).
- Il rinvio al volume base si fa **per titolo di capitolo in corsivo**, mai per link: «il capitolo *La prova a quiz* del volume base».

### 1.4 Comando di verifica, da eseguire prima di dire che un capitolo è finito

Il gate di capitolo si esegue dalla pipeline quando il capitolo è dichiarato nella scheda (§ 7). Finché non lo è, si verifica con uno script temporaneo che importa i due gate:

```
src/pipeline/gates/didactic-density-gate.ts  → runDidacticDensityGate({ content, chapterPath })
src/pipeline/gates/chapter-lint-gate.ts      → runChapterLintGate({ content, chapterPath, requireFormatVersion2: true })
```

Entrambi devono restituire `passed: true`. Lo script va tenuto fuori dal repo o cancellato dopo l'uso.

### 1.5 La regola dei cinque nuclei — leggere prima di scrivere

Il gate chiede cinque nuclei da 600 parole. Le matrici, in molti casi, assegnano a un capitolo meno di cinque nuclei di copertura. **Non è un invito a gonfiare.** La regola, già applicata due volte in M-SP02:

1. Prima si esaurisce la fonte, articolo per articolo, allegato per allegato.
2. Se dalla fonte emergono distinzioni reali di protocollo, di regime o di metodo, **il nucleo di copertura si divide** e la matrice si aggiorna. È successo con la Prova 1 separata dalle Prove 2-3, e con le quattro tipologie della preselettiva diventate cinque nuclei.
3. Se la fonte è esaurita e i nuclei restano meno di cinque o le parole meno di 3.000, **il capitolo non deve esistere da solo**: si accorpa al capitolo adiacente e si aggiorna l'indice del piano editoriale.
4. Non si riempie mai. Il criterio di taglio del volume vieta il testo scritto per raggiungere una soglia.

Questa regola vale in particolare per i capitoli finali di ogni modulo — Bando Decoder, piano di studio, errori, checklist — dove le matrici assegnano un solo nucleo ciascuno. **Aspettati di doverne accorpare.** Ogni accorpamento va motivato per iscritto nel piano editoriale del modulo, con il criterio usato.

---

## 2. Regole di merito non negoziabili

1. **Niente norme, date, numeri o programmi inventati.** Ciò che la fonte non dice, il capitolo dichiara ignoto. Il modello è il capitolo 3 di M-SP02, che elenca esplicitamente le quattro informazioni che il bando tace e spiega perché non si può impostare la strategia di risposta prima di conoscerle.
2. **Niente testo finale ricavato da `wiki/raw/`.** I PDF si leggono, si schedano in una source note, e il capitolo si scrive dalla source note.
3. **Ogni dato mobile porta il box `> **Verifica sul bando.**`** con il riferimento esatto della tornata e l'invito a controllare l'articolo corrispondente del proprio bando. Sono mobili: posti, riserve, limiti di età, materie, soglie, tempi, punteggi, calendari.
4. **Avvertenza medica obbligatoria** in ogni capitolo che tratti prove fisiche o requisiti sanitari: il libro descrive prove e criteri, non prescrive allenamenti e non fornisce valutazioni mediche.
5. **Elenchi diagnostici mai riprodotti.** Precedente stabilito con l'allegato A del d.m. 166/2019: la fonte si cita, si indica dove leggerla, si rinvia al medico. Vale per qualunque tabella di cause di non idoneità dei tre corpi di polizia.
6. **Il notariato porta l'avvertenza** sul mancato accesso al pubblico impiego, in premessa di modulo.
7. **Doppio o triplo binario dichiarato in apertura** di ogni capitolo specialistico, con il callout `> **Binario …**` e il rinvio al capitolo dell'altro binario.
8. **Rinvii al VOL-01 precisi.** Un rinvio vale solo se la destinazione esiste ed è verificata. I capitoli disponibili e già usati: *La prova a quiz*, *Logica, comprensione del testo e ragionamento*, *Informatica, PA digitale e competenze digitali*, *Inglese concorsuale essenziale*, *Banca dati ufficiale: studiarla senza memorizzare male*, *Metodo di studio per concorsi*, *Il diario degli errori*, *Il giorno della prova: routine, logistica e lucidità operativa*, *Costituzione e ordinamento dello Stato*, *La prova orale*, *Prova scritta teorico-pratica*, *Casi pratici e problem solving amministrativo*, *Anatomia del bando*, *Diritto amministrativo per candidati*.
9. **Il delta va sempre esplicitato.** Il caso da tenere a mente: il volume base tratta l'informatica come amministrazione digitale, mentre M-SP02 chiede l'uso pratico degli strumenti. Stesso nome, programma diverso. Ogni rinvio deve dire che cosa si riusa e che cosa no.

---

## 3. Fonti da reperire, per modulo

Ogni fonte acquisita produce **due cose**: il file in `wiki/raw/<modulo>/` con nome parlante, e una sezione nella source note del modulo con livello di verifica (`VERIFICATO` = testo letto; `SCHEDATO` = solo metadati) e la data. Le fonti normative si leggono nel **testo vigente su Normattiva**, non su siti di raccolta.

### 3.1 M-SP01 — Forze di polizia

| Priorità | Fonte | Perché serve | Destinazione |
| --- | --- | --- | --- |
| **Alta** | Norme tecniche delle **prove di efficienza fisica della Guardia di Finanza** | È l'unica scopertura documentale residua del modulo: PS e CC sono coperti, la GdF no. Senza, il capitolo 4 non può trattare i tre corpi allo stesso livello. | `wiki/raw/m-sp01-forze-ordine/gdf-norme-tecniche-prove-efficienza-fisica.pdf` |
| **Alta** | **L. 121/1981** (nuovo ordinamento dell'amministrazione della pubblica sicurezza), testo vigente | Nuclei 01-01 e 01-02: atti individuati ma mai letti articolo per articolo. | source note ordinamento |
| **Alta** | **d.lgs. 66/2010**, parti su Arma dei Carabinieri; **d.lgs. 199/1995**; **L. 189/1959** | Stesso motivo: differenze di status fra i tre corpi. | source note ordinamento |
| **Alta** | **d.lgs. 95/2017** e **d.lgs. 126/2018** (correttivo), testo vigente | Nucleo 02-01, architettura dei ruoli: la vigenza dopo i correttivi non è verificata. È il nucleo su cui poggia l'intera scelta del binario. | source note ordinamento |
| **Alta** | **d.m. 198/2003** e giurisprudenza successiva sui requisiti di condotta | Nuclei 04-01 e 04-03. **Blocco che richiede review umana**: il rapporto fra decreto e giurisprudenza non è risolvibile per deduzione. Codex acquisisce e scheda; non scioglie il nodo da solo. | source note requisiti |
| Media | Bando **GdF 69 allievi ufficiali** | Completa il corpus dei bandi; serve alla decisione di perimetro sul livello ufficiali. | `wiki/raw/m-sp01-forze-ordine/gdf-bando-69-allievi-ufficiali.pdf` |
| Media | **TULPS r.d. 773/1931** e **c.p.p.**, artt. sulla polizia giudiziaria, nel perimetro M-SP01 | Nuclei 11-02 e 11-03: fonti già presenti nel volume, da rileggere nel perimetro di questo modulo. | source note materie |
| Media | Fonte autonoma su **contingenti e riserve** delle forze di polizia | Nucleo 04-02: oggi descritto solo dai bandi. | source note requisiti |
| Media | Rilettura **integrale** dei tre documenti procedurali PS già in `raw/` | Sono stati letti solo nella parte sulle prove fisiche; servono le parti su accertamenti psico-fisici e attitudinali (nuclei 06-02 e 06-03). | aggiornare source note esistente |

### 3.2 M-SP02 — Vigili del fuoco

| Priorità | Fonte | Perché serve | Destinazione |
| --- | --- | --- | --- |
| **Alta** | Bando per **vice direttore del ruolo ordinario** (non la specialità informatica) | Nucleo 08-01: oggi il binario direttivo poggia sul solo bando degli informatici, che è una specialità. Senza, il capitolo 5 descriverebbe l'eccezione come regola. | `wiki/raw/m-sp02-vigili-fuoco/vvf-bando-vice-direttori-ruolo-ordinario.pdf` |
| **Alta** | **d.lgs. 139/2006** — funzioni e compiti del Corpo nazionale, testo vigente | Nucleo 09-02, oggi senza alcuna fonte: organizzazione del soccorso pubblico e della difesa civile. Verificare gli estremi su Normattiva prima di citarli. | source note ordinamento |
| **Alta** | **d.lgs. 217/2005** — ordinamento del personale, testo vigente | Nucleo 09-01: individuato, non letto articolo per articolo. Serve per la mappa dei ruoli del capitolo 1 e per il capitolo 7. | source note ordinamento |
| Media | **d.m. Interno 29 marzo 2022, n. 49** e **d.m. 19 giugno 2019** sui titoli di studio | Richiamati dal bando ispettori tecnico-scientifici; utili al capitolo 6 sulle specializzazioni. | source note ordinamento |
| Media | **Avviso sulle modalità** della preselettiva 2026, quando pubblicato | Scioglie le quattro incognite dichiarate nel capitolo 3: numero di quesiti, durata, penalità, banca dati. **Se esce, il capitolo 3 va aggiornato**, non riscritto. | source note bandi |

### 3.3 M-SP03 — Magistratura, Avvocatura, notariato

È il modulo con il corpus più debole: **un solo PDF acquisito su tre bandi**.

| Priorità | Fonte | Perché serve | Destinazione |
| --- | --- | --- | --- |
| **Alta** | Bando **magistratura ordinaria, 450 posti** — PDF ufficiale | Binario A per intero. Oggi noto solo nel contenuto, non sull'articolato. | `wiki/raw/m-sp03-magistratura-avvocatura-notariato/magistratura-bando-450-posti.pdf` |
| **Alta** | Bando **notariato, 400 posti** — PDF ufficiale | Binario C per intero, comprese le soglie e la disciplina dei testi di consultazione (nucleo 05-02). | `wiki/raw/m-sp03-magistratura-avvocatura-notariato/notariato-bando-400-posti.pdf` |
| **Alta** | **L. 89/1913, art. 5, nn. 1-5**, testo vigente | Nucleo 02-02: il bando notarile vi rinvia direttamente per i requisiti, compresi i 18 mesi di pratica. Requisito d'accesso citato senza aver letto la norma = rischio inaccettabile. | source note ordinamenti |
| **Alta** | **d.lgs. 160/2006, art. 2**, testo vigente | Nucleo 03-01: va accertato comma per comma se le categorie storiche di accesso siano ancora vie autonome o un residuo redazionale del bando. Il dato certo — il laureato è ammesso senza ulteriori titoli — resta tale. | source note ordinamenti |
| **Alta** | **art. 33 del d.l. 144/2022**, conv. L. 175/2022 | Va accertato se la facoltà di svolgimento **informatizzato** della prova scritta sia stata esercitata per il concorso a 450 posti. Cambia il modo di prepararsi. | source note ordinamenti |
| Media | **L. 1035/1966** (Avvocatura) e **r.d. 1860/1925** | Nuclei 16-01 e 16-02: livello ordinamentale dei binari A e B. | source note ordinamenti |
| Media | Verifica sull'esistenza di un **limite ai tentativi per la magistratura ordinaria** | Accertato per notariato (cinque inidoneità) e Avvocatura (limite d'età); ignoto per il binario A. Se non esiste, va scritto che non esiste. | source note ordinamenti |

*La dichiarazione finale della matrice di M-SP03 è già stata rettificata il 13 agosto*: affermava «tre bandi su tre non acquisiti in PDF» in contraddizione con la nota sulla qualità del corpus. Il quadro corretto è nella matrice; non reintrodurre la versione vecchia.

### 3.4 M-SP04 — Prefettizia e diplomatica

| Priorità | Fonte | Perché serve | Destinazione |
| --- | --- | --- | --- |
| **Alta** | **d.i. 4 giugno 2002, n. 144**, come modificato dai d.i. 39/2007 e 80/2017 | È il regolamento del concorso prefettizio: contiene le materie analitiche delle cinque prove scritte (nucleo 03-03), oggi la parte più pesante della selezione e la meno documentata. | `wiki/raw/m-sp04-prefettizia-diplomatica/di-144-2002-regolamento-concorso-prefettizio.pdf` |
| **Alta** | **d.m. 29 luglio 1999, n. 357** | Nucleo 03-01: limiti di età richiamati dal bando, testo mai acquisito. | `wiki/raw/m-sp04-prefettizia-diplomatica/dm-357-1999-limiti-eta.pdf` |
| **Alta** | **Quesiti pubblicati** della preselettiva prefettizia | Nucleo 03-02: la preselettiva è a quesiti pubblicati. Se la raccolta è disponibile, cambia il metodo di studio del capitolo 2 — diventa lo studio di un insieme chiuso, con rinvio al capitolo *Banca dati ufficiale* del volume base. | `wiki/raw/m-sp04-prefettizia-diplomatica/quesiti-preselettiva-prefettizia.pdf` |
| Media | **artt. 11-12 del bando MAECI** | Nucleo 08-02: dettaglio delle lingue e disciplina delle prove facoltative. Il bando è già in `raw/`: va riletto in quella parte. | aggiornare source note |
| Media | Verifica sull'esistenza di un **limite ai tentativi per la prefettizia** | Accertato per la diplomatica (quattro tentativi falliti = preclusione). Ignoto per la prefettizia: se non esiste, va scritto. | source note bandi |
| Media | Scioglimento della **discrepanza sulla durata della formazione** | Fonti secondarie dicono un anno, il d.lgs. 139/2000 parla di durata minima di due anni. Il decreto è già in `raw/`: la discrepanza si scioglie leggendolo, non cercando altrove. | aggiornare source note |

*Il blocker 1 della matrice di M-SP04 è già stato rettificato il 13 agosto*: dichiarava il nucleo 14-01 «senza alcuna fonte» mentre `wiki/raw/m-sp04-prefettizia-diplomatica/` contiene già `dlgs-139-2000-carriera-prefettizia.pdf` e `dpr-18-1967-ordinamento-esteri.pdf`, cioè gli ordinamenti di entrambe le carriere. Non è un blocco di reperimento ma di **lettura**.

### 3.5 Nucleo 08-03 di M-SP04 — un caso da trattare come tale

Il «livello linguistico realmente necessario» non è desumibile da alcuna fonte documentale. Non va costruito per deduzione e non va omesso: va scritto **dichiarandolo come stima**, spiegando su che base è formulata e che cosa la renderebbe falsa. È lo stesso trattamento riservato alle quattro incognite della preselettiva in M-SP02.

---

## 4. I capitoli da scrivere

Struttura di riferimento: quella rivista nella nota `09-revisione-strutture-unita-di-lettura`. **Quaranta capitoli, tre scritti, trentasette da scrivere.**

Per ogni capitolo: nuclei assegnati dalla matrice, contenuto obbligatorio, trappole note. Dove i nuclei assegnati sono meno di cinque si applica la regola § 1.5.

### 4.1 M-SP02 — Vigili del fuoco (9 su 12 da scrivere)

Scritti e conformi: **02** (posizione prima della domanda), **03** (preselezione), **04** (prove d'esame e titoli).

**Capitolo 01 — Mappa della famiglia: ruoli e architetture di selezione a confronto**
`chapters/01-mappa-della-famiglia.md` · nuclei: 01-01 più i nuclei che si renderanno necessari dividendo la mappa.
Contenuto: i quattro insiemi di ruoli — operativi, ispettivi, direttivi, tecnico-professionali; le due architetture di selezione opposte (operativo motorio-attitudinale, direttivo scritto-orale); il **rilievo strutturale decisivo**, cioè che nel concorso base non esiste una prova scritta di materie come prova d'esame, e l'avvertimento esplicito a chi arriva da M-SP01; il terzo regime del d.m. 166/2019 come anticipazione della decisione di binario.
Trappola: è il capitolo di apertura e ha un solo nucleo in matrice. Va diviso attingendo al d.lgs. 217/2005 (ruoli) una volta letto, altrimenti resta sotto soglia.

**Capitolo 05 — Prova scritta e prova orale dei profili direttivi e tecnici**
`chapters/05-binario-direttivo-prove.md` · nuclei: 07-01 e successivi da dividere.
Contenuto: struttura scritta-orale; titoli valutati **solo a parità di punteggio**; accertamenti psico-fisici a valle e non a monte; l'avviso del 26 maggio 2026 sull'assenza di preselezione, da riportare per quello che è — informazione da fonte secondaria.
**Bloccato** finché non è acquisito il bando del ruolo ordinario: scriverlo sul solo bando informatico significherebbe descrivere una specialità come se fosse la regola.

**Capitolo 06 — Il percorso di specializzazione: ruoli, specialità e tecnico-professionali**
`chapters/06-percorso-specializzazione.md` · nuclei: 08-01 e derivati.
Contenuto: ruolo ordinario, ispettivo, specialità, ruoli tecnico-professionali; il d.m. 49/2022 sul concorso per ispettore tecnico-scientifico; i titoli di studio per le qualifiche iniziali.
Trappola: qui va ripreso e sviluppato il **terzo regime** dell'art. 2 del d.m. 166/2019 — chi è escluso dai ruoli operativi per un parametro numerico può essere idoneo qui. È il contenuto a più alto valore del modulo dopo le riserve.

**Capitolo 07 — Ordinamento del Corpo e organizzazione del soccorso pubblico**
`chapters/07-ordinamento-e-soccorso-pubblico.md` · nuclei: 09-01, 09-02.
**Bloccato** finché non sono letti d.lgs. 217/2005 e d.lgs. 139/2006 nel testo vigente.

**Capitolo 08 — Le materie: cosa riusi dal VOL-01 e cosa no**
`chapters/08-materie-riuso-vol-01.md` · nucleo: 10-01.
Contenuto: il delta qui è **minimo per il binario operativo** — il concorso base non ha materie giuridiche — e sostanziale per il direttivo. Il capitolo deve dirlo apertamente invece di simulare una copertura.
Trappola: un capitolo di soli rinvii non è un'unità di lettura. Se dopo aver esaurito il tema resta sotto soglia, **si accorpa** al capitolo 9 (Bando Decoder) e l'indice del modulo scende a 11 sezioni.

**Capitolo 09 — Bando Decoder della famiglia** · `chapters/09-bando-decoder.md` · nucleo 11-01.
**Capitolo 10 — Piano 30/60/90 per binario** · `chapters/10-piano-30-60-90.md` · nuclei 12-01, 12-02.
**Capitolo 11 — Errori frequenti e casi guidati** · `chapters/11-errori-e-casi.md` · nucleo 13-01.
**Capitolo 12 — Checklist finale del modulo** · `chapters/12-checklist-finale.md` · nucleo 14-01.

Su questi quattro si applica la regola § 1.5 con la massima attenzione: quattro capitoli con un nucleo ciascuno non reggono quattro capitoli. Il piano 30/60/90 ha materiale proprio (due binari, preparazione atletica dominante contro studio dominante) e regge; gli altri tre vanno valutati sul contenuto reale e, se necessario, accorpati a due.

### 4.2 M-SP01 — Forze di polizia (10 capitoli, nessuno scritto)

**Decisione di perimetro da prendere prima di scrivere i capitoli 1, 2 e 4.** L'acquisizione del bando per 65 allievi ufficiali dell'Accademia Militare ha rivelato un terzo livello di ruolo che il modulo non contempla. Le opzioni sono due: introdurre un terzo binario, o dichiarare l'esclusione motivata del livello ufficiali. **La decisione non spetta a Codex**: va portata alla review con le due ipotesi istruite e il costo di ciascuna. Nel frattempo si scrivono i capitoli 3, 5, 6, 7, che non ne dipendono.

**Capitolo 01 — Mappa della famiglia e struttura della selezione** · nuclei 01-01, 01-02, 01-03, 03-01.
Contenuto: pubblica sicurezza; ordinamento civile e militare; i tre corpi e le differenze di status; concorso pubblico e interno; **la sequenza invariante a quattro fasi** — scritta, efficienza fisica, psico-fisici, attitudinale — presente in tutti i bandi del corpus e spina dorsale del modulo.
Bloccato sul livello ordinamentale finché L. 121/1981 e le fonti sui Carabinieri non sono lette.

**Capitolo 02 — La tua posizione prima della domanda** · nuclei 02-01, 04-01, 04-02, 04-03.
Contenuto: ruoli base e ispettivi e conseguenze della scelta; requisiti, limiti di età ed elevazioni; contingenti (civili, VFP, bilinguisti), riserve, limite ai tentativi; cause di esclusione.
**Due avvertenze pesanti.** La prima: i limiti di età sono il punto in cui le fonti secondarie sbagliano — riportano «18-26 anni» per gli allievi agenti 2026 mentre la fonte ufficiale indica 29 anni non compiuti. Il capitolo usa la fonte ufficiale e segnala l'errore diffuso. La seconda: le cause di esclusione poggiano su un rapporto irrisolto fra d.m. 198/2003 e giurisprudenza successiva, che **richiede review umana**: il capitolo va scritto sul certo e va dichiarato il dubbio, non risolto per deduzione.
Modello di riferimento: il capitolo 02 di M-SP02, che tratta la stessa unità di lettura.

**Capitolo 03 — I formati della prova scritta** · nuclei 05-01, 05-02, 05-03.
Contenuto: è il capitolo che giustifica l'esistenza del modulo. Tre formati **incompatibili** allo stesso livello ispettivo: banca dati chiusa di 5.000 quesiti (Polizia di Stato), componimento di italiano (Carabinieri), tema di sei ore o prova di cultura generale (Guardia di Finanza). Tre preparazioni diverse che nessuna trattazione unitaria può servire. Più il ruolo della preselezione.
Delta VOL-01: il capitolo *Banca dati ufficiale* copre il metodo; il delta di M-SP01 è la **compressione temporale** — nel concorso per vice ispettori 2026 fra pubblicazione della banca dati e prova scritta è passato poco più di un mese.

**Capitolo 04 — Gli accertamenti e la preparazione** · nuclei 06-01, 06-02, 06-03, 07-01.
Contenuto: efficienza fisica per i tre corpi; idoneità psico-fisica; accertamento attitudinale; gesti atletici, trappole procedurali, rischio di esclusione in itinere.
**Bloccato** per la parte GdF finché le norme tecniche non sono reperite. Le parti psico-fisica e attitudinale richiedono la rilettura integrale dei tre documenti procedurali PS. Avvertenza medica obbligatoria; nessun elenco diagnostico riprodotto.

**Capitolo 05 — [isp] Prova orale, titoli e lingua facoltativa** · nuclei 08-01, 09-01.
Contenuto: struttura e criteri del colloquio; valutazione dei titoli; prova facoltativa di lingua straniera fra inglese, francese, tedesco, spagnolo.
Due nuclei soli: applicare § 1.5, con il precedente di M-SP02 dove i titoli da soli non reggevano un capitolo.

**Capitolo 06 — Le materie: riuso dal VOL-01 e specialistiche** · nuclei 10-01, 11-01, 11-02, 11-03.
Contenuto: delta di famiglia sul VOL-01; ordinamento dei corpi come materia d'esame; nozioni essenziali di diritto e procedura penale e polizia giudiziaria; pubblica sicurezza e polizia amministrativa.
Trappola: è il capitolo dove è più forte la tentazione di scrivere un manuale di diritto penale. Il perimetro è quello che il bando chiede, e il libro fornisce mappa e metodo, non la trattazione istituzionale.

**Capitolo 07 — Bando Decoder** · nucleo 12-01.
**Capitolo 08 — Piano 30/60/90 a doppio binario** · nuclei 13-01, 13-02, con la variante «banca dati pubblicata».
**Capitolo 09 — Errori frequenti e casi guidati** · nucleo 14-01.
**Capitolo 10 — Checklist finale** · nucleo 15-01.
Stessa avvertenza di M-SP02: valutare gli accorpamenti sul contenuto reale.

### 4.3 M-SP03 — Magistratura, Avvocatura, notariato (9 capitoli, nessuno scritto)

Modulo a **tre binari separati**: la matrice ha righe distinte per binario e i capitoli devono dichiararlo in apertura. Nessuna fusione dei tre concorsi.

**Capitolo 01 — Mappa, scelta del binario e limite dei rinvii al VOL-01** · nuclei 01-01, 02-01, 02-02, 02-03, 06-01.
Contenuto: tre concorsi, tre banditori, un solo impianto di studio; **le proporzioni reali** — 450 posti in magistratura, 400 nel notariato, 7 all'Avvocatura — che sono il dato con cui il lettore sceglie; i requisiti del notariato dell'art. 5 L. 89/1913, compresi i **18 mesi di pratica notarile**; l'**incompatibilità di calendario** fra notariato (17-19 giugno) e magistratura (24-26 giugno 2026), che rende impossibile una preparazione parallela seria; il limite del riuso dal VOL-01, qui quasi nullo.
Avvertenza obbligatoria: il notariato **non dà accesso al pubblico impiego**. Va in premessa di modulo e ripresa qui.

**Capitolo 02 — [A] Magistratura ordinaria: prove e materie** · nuclei 03-01, 03-02, 07-01, 16-01.
Contenuto: requisiti dopo l'art. 33 del d.l. 144/2022 — **la sola laurea in giurisprudenza**; struttura delle prove scritte, otto ore per materia, disciplina d'aula; civile, penale, amministrativo; orale ampio con colloquio in lingua straniera e soglie; ordinamento giudiziario.
Da accertare prima di scrivere: se la prova scritta si svolga in forma **informatizzata**.

**Capitolo 03 — [B] Avvocatura dello Stato: prove e materie** · nuclei 04-01, 08-01, 08-02, 16-02.
Contenuto: requisiti e **limite dei 35 anni**; tre temi teorico-pratici da otto ore; privato e processuale civile, penale e processuale penale, amministrativo sostanziale e processuale; orale su costituzionale, internazionale privato, diritto UE, tributario, lavoro, informatica giuridica; ordinamento dell'Avvocatura.
Il confronto con la magistratura — «cosa cambia davvero» — è il valore del capitolo: sette posti contro quattrocentocinquanta cambiano la natura della scelta.

**Capitolo 04 — [C] Notariato: prove, pratica e materie** · nuclei 05-01, 05-02, 09-01, 16-03.
Contenuto: le tre prove — testamento, atto tra vivi, atto tra vivi di contenuto commerciale; la compilazione dell'atto come gesto d'esame; soglie; **la disciplina dei testi di consultazione**, consegnati in identificazione e vietati nei giorni di prova; civile, commerciale e volontaria giurisdizione; ordinamento del notariato e degli archivi notarili; i 18 mesi di pratica.

**Capitolo 05 — La scrittura d'esame: tema, parere e atto** · nucleo 10-01.
Contenuto: tre formati distinti, con lo stesso trattamento comparativo che il capitolo 03 di M-SP01 riserva ai tre formati di prova scritta. Unità di lettura autonoma e trasversale ai tre binari. Rinvio con delta a *Prova scritta teorico-pratica* del volume base.

**Capitolo 06 — Bando Decoder per le tre selezioni** · nucleo 11-01.
**Capitolo 07 — Piano pluriennale e tenuta sulla distanza** · nuclei 12-01, 13-01.
Contenuto: **non** un piano 30/60/90 — sarebbe una promessa falsa per selezioni che si preparano in anni. Orizzonte pluriennale a cicli; il consumo dei tentativi come vincolo del piano — notariato: massimo cinque inidoneità dal 2009; Avvocatura: limite d'età; magistratura: da accertare. Carico, isolamento, criteri per fermarsi o cambiare binario, senza retorica motivazionale e senza sconfinare in consulenza psicologica: segnali e criteri di decisione, non terapie.
**Capitolo 08 — Errori frequenti e casi guidati per binario** · nucleo 14-01.
**Capitolo 09 — Checklist finale** · nucleo 15-01.

### 4.4 M-SP04 — Prefettizia e diplomatica (9 capitoli, nessuno scritto)

**Capitolo 01 — Mappa, scelta del binario e rinvii al VOL-01** · nuclei 01-01, 02-01, 02-02, 05-01, 14-01 (parte).
Contenuto: due carriere, due amministrazioni, un livello di ingresso dirigenziale; **le proporzioni** — 158 posti contro 35; il **limite di quattro tentativi falliti agli scritti** della diplomatica, che è una preclusione definitiva e va detta subito, non in fondo; il delta sul VOL-01; la vita professionale a valle come elemento della scelta.

**Capitolo 02 — [A] Carriera prefettizia: prove e materie** · nuclei 03-01, 03-02, 03-03, 06-01, 14-01 (parte).
Contenuto: requisiti e limiti di età del d.m. 357/1999; preselettiva a **quesiti pubblicati**, sei materie, divieti d'aula con esclusione immediata; **trentacinque ore di scritti** — tre elaborati da otto ore su amministrativo e/o costituzionale, civile, storia contemporanea e della PA; un **caso** giuridico-amministrativo o gestionale-organizzativo da sette ore; traduzione con vocabolario da quattro ore; orale con sociologia e scienza dell'organizzazione, scienza delle finanze, penale limitato a parti determinate, legislazione speciale del Viminale, contabilità di Stato e **verifica applicativa di informatica**.
Due precisazioni che il modulo trattava male e che vanno scritte esplicitamente: **la prova del caso non è un tema** — è una simulazione di problem solving dirigenziale che valuta l'attitudine alle funzioni di dirigenza, e non si allena scrivendo temi di diritto amministrativo; **la traduzione non è una prova di lingua nel senso ordinario** — è una traduzione scritta con vocabolario, e chi la prepara come un orale sta allenando la cosa sbagliata.
**Bloccato** per le materie analitiche finché il d.i. 144/2002 non è acquisito.

**Capitolo 03 — [B] Carriera diplomatica: prove e materie** · nuclei 04-01, 04-02, 04-03, 07-01, 07-02, 07-03.
Contenuto: requisiti e riserva di 5 posti a dipendenti MAECI con cinque anni di servizio; struttura completa — prova attitudinale, scritte, orali, facoltative, titoli; **la prova attitudinale** con criterio di valutazione non centesimale; storia delle relazioni internazionali dal Congresso di Vienna; diritto internazionale pubblico e dell'Unione europea; economia politica, politica economica, economia internazionale e finanziaria, commercio.

**Capitolo 04 — Le lingue straniere** · nuclei 08-01, 08-02, 08-03.
Contenuto: prefettizia — traduzione con vocabolario in quattro ore, inglese o francese, più orale facoltativa in seconda lingua; diplomatica — inglese obbligatorio e seconda lingua fra francese, spagnolo e tedesco; livello dichiarato contro livello realmente necessario **dichiarato come stima** (§ 3.5); piano di mantenimento misurabile, non raccomandazioni generiche.
È autonomo perché le regole divergono nei due binari: unico capitolo del modulo che tratta insieme i due binari senza fonderli.

**Capitolo 05 — La prova orale come valutazione di postura professionale** · nucleo 09-01.
**Capitolo 06 — Bando Decoder per le due carriere** · nucleo 10-01, con i quesiti pubblicati come pattern di volume.
**Capitolo 07 — Piano di preparazione e limite dei tentativi** · nuclei 11-01, 11-02.
Contenuto: orizzonte 6-12 mesi, che con trentacinque ore di scritti è **un minimo assoluto, non una stima**; il caso gestionale va allenato separatamente dai temi; il piano della diplomatica è vincolato dal limite dei quattro tentativi.
**Capitolo 08 — Errori frequenti e casi guidati** · nucleo 12-01.
**Capitolo 09 — Checklist finale** · nucleo 13-01.

---

## 5. Aggiornamento delle matrici — regole

Ogni capitolo chiuso comporta l'aggiornamento della matrice del modulo, nella stessa sessione, mai dopo:

1. Colonna **Collocazione**: da `§ N` a `cap. NN § N-SPXX-NN-NN`, cioè il riferimento al nucleo reale del capitolo.
2. Colonne **Copertura teorica**, **Applicazione**, **Verifica**: compilate con quello che il capitolo contiene davvero. La convenzione in uso è `Q:6 C:1 E:N` — quiz, casi, esercizi.
3. Colonna **Stato**: `completo` solo se il capitolo esiste, copre il nucleo e **supera entrambi i gate**. In ogni altro caso `parziale`, e va detto perché.
4. Se un nucleo si divide, le righe nuove si aggiungono con ID progressivo e la nota di divisione va nel paragrafo dei totali.
5. **Totali e dichiarazione finale vanno ricalcolati**, non lasciati indietro. Le matrici di M-SP03 e M-SP04 hanno già oggi frasi in contraddizione con le righe che le precedono: non aggiungerne altre.
6. La riga `mancante` non si tocca mai per compiacere un gate.

---

## 6. Piano editoriale del modulo

Ogni accorpamento o divisione decisa in corso di scrittura si registra in `planning/00-piano-editoriale.md` del modulo, con: che cosa è stato unito o diviso, **il sintomo** che lo ha imposto (duplicazione di un dato fra due capitoli, esaurimento della fonte sotto soglia, protocolli diversi nello stesso nucleo), e il conteggio risultante. È il formato già usato in M-SP02, che ha registrato tre note di struttura.

Non si accorpa mai per comodità di conteggio, e ogni nota deve poter essere verificata da chi revisiona.

---

## 7. Pipeline: estensione della scheda e comandi

La scheda `wiki/books/volumi/vol-12-carriere-speciali-premium/planning/00-scheda-pipeline.md` dichiara oggi le sole fasi A e B e **nessun capitolo**. Finché resta così, i gate di capitolo non sono eseguibili dalla CLI: `gate --step 10 --chapter …` risponde che lo step non è nel run-state.

Sequenza da eseguire **quando l'indice dei quaranta capitoli è stabile** — cioè dopo aver deciso gli accorpamenti dei capitoli finali di ciascun modulo, non prima:

1. Aggiornare il frontmatter della scheda: `phases: [A, B, C, D, E, F]`, `status`, `updated_at`.
2. Aggiungere una sezione `## Capitoli M-SPXX` per modulo, con la tabella nel formato in uso negli altri volumi:

   ```
   | # | Titolo | File | Matrice | Stato atteso | Note |
   ```

   `File` è il percorso relativo `chapters/NN-slug.md`; `Matrice` è `planning/02-matrice-copertura-didattica.md`.
3. `npm run pipeline -- sync VOL-12 --json` per aggiungere i target al run-state. **Il run-state non si modifica a mano in nessun caso.**
4. Da lì in avanti il ciclo normale, un capitolo alla volta:

   ```
   npm run pipeline -- status VOL-12 --json
   npm run pipeline -- next VOL-12 --json
   # eseguire il prompt scritto in artifacts/pipeline/VOL-12/<step>/<target>/prompt.md
   npm run pipeline -- complete VOL-12 --step 09 --module M-SPXX --chapter NN
   ```

Note operative:

- Lo step 11 (Humanizer) salva lo snapshot **prima** dell'intervento: non modificare il capitolo prima di aver eseguito `next`, altrimenti il gate blocca.
- Lo step 07 di M-SP01 è oggi `in-progress` e in carico a `info (claude-code)`: per subentrare serve `--force`, e solo dopo accordo. Il suo gate `coverage` non passerà finché esistono nuclei `mancante`, il che è corretto: si chiude quando il modulo è scritto, non prima.
- `--accept` richiede `--note` con la motivazione e si usa **solo** dopo aver eseguito a mano la verifica che il gate non automatizza.
- Aggiungere `--json` a ogni comando e leggere l'esito da lì, mai dal testo formattato.

---

## 8. Ordine di esecuzione consigliato

1. **Fonti prima di tutto.** Il blocco § 3 nella sua interezza, modulo per modulo. Nessun capitolo bloccato va scritto «in attesa» della fonte.
2. **M-SP02 fino in fondo.** È il modulo più avanti, ha tre capitoli conformi che fanno da modello e un corpus quasi completo. Chiuderlo per primo dà un modulo intero come riferimento e mette alla prova gli accorpamenti dei capitoli finali.
3. **M-SP04.** Corpus ben verificato, due binari, blocchi concentrati su due documenti reperibili.
4. **M-SP01.** Richiede prima la decisione di perimetro sul livello ufficiali e la chiusura di due blocchi di alta priorità, uno dei quali (d.m. 198/2003 e giurisprudenza) va portato in review.
5. **M-SP03 per ultimo.** È il più oneroso e ha il corpus più debole: due bandi su tre da acquisire e tre leggi di ordinamento da leggere.

Criterio di sospensione: se durante la scrittura emerge che una fonte è insufficiente per il nucleo che si sta trattando, **si ferma il capitolo e si segnala**, non si compensa con la deduzione. Un capitolo fermo è un problema; un capitolo che riempie un buco con contenuto plausibile è un danno.

---

## 9. Che cosa consegnare alla review

Per ciascun modulo, alla chiusura:

1. **I capitoli**, con esito dei due gate riportato esplicitamente per ognuno (parole, nuclei con conteggio, quiz, casi, verifiche, `passed`).
2. **La matrice aggiornata**, con totali ricalcolati e dichiarazione finale coerente con le righe.
3. **Le source note** delle fonti acquisite, con livello di verifica e data, e l'elenco di quelle **non** reperite con la ricerca effettuata.
4. **Le note di struttura** nel piano editoriale per ogni accorpamento o divisione, con il sintomo che l'ha imposta.
5. **L'elenco esplicito delle incognite dichiarate** nei capitoli: ogni punto in cui il testo dice «la fonte non lo dice». Sono i punti che la review controlla per primi, perché sono quelli in cui è più facile aver ceduto e aver scritto un numero plausibile.

La review verifica, in quest'ordine: che i gate passino davvero; che ogni dato normativo citato esista nella fonte dichiarata; che nessun elenco diagnostico sia stato riprodotto; che i rinvii al volume base abbiano destinazione esistente; che le matrici non contengano `completo` senza capitolo; che gli accorpamenti siano motivati e non di comodo.

---

## 10. Quello che questo documento non autorizza

- Dichiarare un modulo pubblicabile con nuclei `mancante`.
- Scrivere il capitolo 5 di M-SP02 sul solo bando degli informatici.
- Scrivere i requisiti del notariato senza aver letto l'art. 5 della L. 89/1913.
- Scrivere le materie delle cinque prove prefettizie senza il d.i. 144/2002.
- Risolvere il rapporto fra d.m. 198/2003 e giurisprudenza successiva senza review umana.
- Introdurre il livello ufficiali in M-SP01 senza decisione esplicita.
- Riprodurre l'allegato A del d.m. 166/2019 o qualunque elenco analogo.
- Toccare `pipeline/VOL-12/run-state.json` con un editor.
