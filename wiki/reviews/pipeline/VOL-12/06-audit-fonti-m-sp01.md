---
id: pipeline-vol-12-06-audit-fonti-m-sp01
type: pipeline_review
title: "VOL-12 — Step 06: audit e consolidamento delle fonti M-SP01"
volume_code: VOL-12
step: "06"
phase: B
scope: module
module_code: M-SP01
domain: "concorsi pubblici italiani"
source_refs: ["sources/bandi-rappresentativi-m-sp01-forze-polizia-2026.md", "sources/ordinamento-forze-di-polizia-quadro-normativo-m-sp01.md"]
book_refs: ["m-sp01-forze-ordine", "vol-12-carriere-speciali-premium"]
cut_off_date: 2026-08-10
checked_at: 2026-08-11
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-06", "m-sp01", "audit-fonti"]
---

# VOL-12 — Step 06: audit e consolidamento delle fonti M-SP01

Data di controllo: **2026-08-10**. Struttura di riferimento: le 15 sezioni definite dall'audit dei bandi ([[reviews/pipeline/VOL-12/05-audit-bandi-m-sp01]]).

## Source notes consolidate in questo step

1. [[sources/bandi-rappresentativi-m-sp01-forze-polizia-2026]] — corpus dei sei bandi, con livello di verifica dichiarato per voce.
2. [[sources/ordinamento-forze-di-polizia-quadro-normativo-m-sp01]] — quadro normativo primario.

## Tabella dei nuclei

| Nucleo | Fonte consolidata | Autorità | Ultimo controllo | Rischio di aggiornamento | Capitolo impattato | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Ordinamento della pubblica sicurezza; corpi civili e militari | L. 121/1981 | alta — Normattiva, G.U. 100/1981 | 2026-08-10 | basso | 1 | ✅ pronto |
| Architettura dei ruoli; base contro ispettivo | D.lgs. 95/2017 e D.lgs. 126/2018 | alta — G.U. 22/06/2017 | 2026-08-10 | **medio-alto** (più correttivi) | 1, 2 | 🟡 verificare vigenza |
| Status dell'Arma dei Carabinieri; perimetro del modulo | D.lgs. 66/2010 (COM) e d.P.R. 90/2010 (TUOM) | alta — G.U., Ministero della Difesa | 2026-08-10 | basso | 1 | ✅ pronto |
| Ordinamento del personale della Guardia di Finanza | **assente** | — | — | — | 1, 2 | 🔴 **mancante** |
| Requisiti, limiti di età, contingenti e riserve | corpus bandi + d.m. 198/2003 | alta — Ministero dell'Interno | 2026-08-10 | **altissimo** | 4 | 🟡 parziale |
| Formati della prova scritta; banca dati ufficiale | corpus bandi (A1, A2 verificati) | alta — Polizia di Stato, inPA | 2026-08-10 | alto | 5 | ✅ pronto |
| Preselezione, componimento, tema lungo | corpus bandi (B2, C2) | **media** — fonti secondarie | 2026-08-10 | alto | 5 | 🟡 da riscontrare |
| Idoneità psico-fisica e accertamento attitudinale | d.m. 198/2003 + disposizioni procedurali PS | alta — Ministero dell'Interno, Polizia di Stato | 2026-08-10 | **altissimo** | 6 | 🟡 parziale |
| Disciplina delle prove di efficienza fisica | **assente** | — | — | — | 6, 7 | 🔴 **mancante** |
| Prova orale e colloquio | corpus bandi (A2, B1, B2, C2) | media/alta | 2026-08-10 | medio | 8 | 🟡 parziale |
| Valutazione dei titoli; lingua straniera facoltativa | corpus bandi (A1, B1, C2) | media/alta | 2026-08-10 | alto | 9 | 🟡 parziale |
| Materie comuni e rinvii al VOL-01 | VOL-01, capitoli esistenti | interna | 2026-08-11 | basso | 10 | ✅ pronto |
| Pubblica sicurezza e polizia amministrativa | [[sources/regio-decreto-18-giugno-1931-n-773-tulps-polizia-amministrativa]] | alta — TULPS | precedente | basso | 11 | 🟡 rileggere nel perimetro |
| Funzioni di polizia giudiziaria | [[sources/codice-procedura-penale-polizia-giudiziaria]] | alta — c.p.p. | precedente | basso | 11 | 🟡 rileggere nel perimetro |
| Bando Decoder di famiglia | corpus bandi | alta | 2026-08-10 | basso | 12 | ✅ pronto |

**Bilancio: 5 nuclei pronti, 8 parziali, 2 mancanti.** Nessuna sezione può essere scritta finché i due nuclei mancanti non sono colmati e i parziali non sono riscontrati.

## Difetto rilevato in una source note preesistente 🔴

**File:** `wiki/sources/corte-costituzionale-requisiti-concorsuali-polizia-di-stato-g-u-27-gennaio-2021.md`

Era stata individuata allo step 01 come fonte potenzialmente riutilizzabile per il nucleo dei requisiti di accesso. All'esame è risultata **inaffidabile per l'uso editoriale**:

| Problema | Rilievo |
| --- | --- |
| Titolo fuorviante | è intitolata «Corte costituzionale», ma il testo riportato è un'**ordinanza di rimessione del TAR Lazio, Sezione prima quater** — un atto di rinvio, non una decisione della Corte |
| `topics` non pertinenti | dichiara «piano 30/60/90 giorni», «enti locali», «contabilità pubblica», «contratti pubblici»: nessuno attinente ai requisiti concorsuali |
| `entities` non pertinenti | dichiara «Piano 30/60/90 giorni», «RUP», «Comune» |
| `authority_level: bassa` | in contrasto con il titolo, che evoca una pronuncia costituzionale |
| `review_required: false` | una nota con questi difetti non dovrebbe essere esente da review |
| Contenuto | la sintesi contiene il **nome di una parte privata del giudizio**, dato personale non necessario all'uso editoriale |

**Perché è grave:** un writer agent che cerchi «requisiti concorsuali Polizia di Stato» trova questa nota, ne legge il titolo e può attribuire alla Corte costituzionale il contenuto di un'ordinanza di rimessione — e per giunta senza conoscerne l'esito. È esattamente il tipo di errore che nessun lettore perdona in un volume premium.

**Intervento:** la nota **non viene usata** per M-SP01. Va corretta dal flusso che la possiede — retitolazione come ordinanza TAR, correzione di `topics` ed `entities`, `review_required: true`, rimozione del nominativo — oppure archiviata. **Segnalata, non modificata**: appartiene a un altro perimetro e la sua correzione richiede la verifica dell'esito del giudizio, che non è stata svolta.

## Parti mobili da non presentare come stabili

Confermano e ampliano l'elenco della source note dei bandi. Per M-SP01 il capitolo **non** deve riportare come valori stabili:

1. parametri antropometrici e sanitari di idoneità (altezza, peso, visus e simili);
2. limiti di età e relative elevazioni;
3. numero di posti, contingenti e riserve;
4. ampiezza e composizione della banca dati ufficiale;
5. presenza della preselezione, dell'orale, della prova facoltativa di lingua;
6. sedi, date e calendario;
7. articolazione dei ruoli, soggetta agli interventi correttivi del d.lgs. 95/2017.

## Conflitti fra fonti

Due, entrambi non risolti e da affidare a review umana:

1. **Fonti secondarie contro fonte ufficiale sui limiti di età** — documentato nell'audit dei bandi. Risolto a favore della fonte ufficiale: 29 anni non compiuti, non 26.
2. **d.m. 198/2003 contro giurisprudenza successiva sui requisiti di accesso** — il rapporto non è stato ricostruito. È l'area di rischio maggiore del modulo. Non risolvibile per deduzione: richiede verifica della vigenza su Normattiva e ricognizione delle pronunce.

## Da chiudere prima della fase C

- [x] 🔴 reperire l'ordinamento del personale della Guardia di Finanza — **fatto**: L. 189/1959 e d.lgs. 199/1995;
- [x] 🔴 reperire la disciplina delle prove di efficienza fisica — **fatto per Polizia di Stato e Arma dei Carabinieri**; resta scoperta la Guardia di Finanza;
- [x] 🟡 riscontrare sui PDF ufficiali i bandi classificati DA VERIFICARE — **fatto per tre su quattro**;
- [ ] 🟡 leggere il testo vigente degli atti individuati, articolo per articolo, su Normattiva;
- [ ] 🟡 ricostruire il rapporto fra d.m. 198/2003 e giurisprudenza successiva — **review umana**;
- [ ] 🟡 rileggere TULPS e c.p.p. nel perimetro M-SP01;
- [ ] 🟡 leggere integralmente i tre documenti PS sugli accertamenti psico-fisici e attitudinali;
- [ ] 🟡 reperire le norme tecniche delle prove fisiche della Guardia di Finanza e il bando GdF 69 allievi ufficiali;
- [ ] segnalare al flusso proprietario il difetto della source note sulla pronuncia del 2021.

---

# Aggiornamento 2026-08-11 — acquisizione delle fonti mancanti

## Documenti scaricati

Dodici documenti ufficiali, 34 MB complessivi, conservati in `wiki/raw/m-sp01-forze-ordine/`.

| Documento | Fonte | Esito |
| --- | --- | --- |
| `ps-bando-4400-allievi-agenti.pdf` | inPA | acquisito — **PDF immagine, testo non estraibile** |
| `cc-bando-3081-allievi-carabinieri-146-corso.pdf` | inPA | acquisito e riscontrato sul testo |
| `cc-ist16-bando-898-allievi-marescialli.pdf` | carabinieri.it | acquisito e riscontrato |
| `cc-ist16-decreto-modifica-bando.pdf` | carabinieri.it | acquisito |
| `gdf-bando-983-allievi-marescialli-98-corso.pdf` | inPA | acquisito e riscontrato |
| `cc-mo208-bando-65-allievi-ufficiali-accademia-militare.pdf` | carabinieri.it | acquisito — **documento diverso da quello atteso**, vedi sotto |
| `procedure-per-le-prove-di-efficienza-fisica.pdf` | poliziadistato.it | parametri delle tre prove estratti |
| `procedure-prove-efficienza-fisica.pdf` | poliziadistato.it | acquisito |
| `cc-norme-tecniche-prove-efficienza-fisica.pdf` | carabinieri.it | parametri estratti |
| `procedure-per-gli-accertamenti-psico-fisici.pdf` | poliziadistato.it | acquisito, non ancora letto integralmente |
| `disposizioni-svolgimento-accertamenti-psico-fisici.pdf` | poliziadistato.it | acquisito, non ancora letto integralmente |
| `disposizioni-per-lo-svolgimento-degli-accertamenti-attitudinali.pdf` | poliziadistato.it | acquisito, non ancora letto integralmente |

Nuova source note prodotta: [[sources/prove-efficienza-fisica-accertamenti-forze-di-polizia-m-sp01]].

## Errore commesso e corretto

Il bando dei 3.081 allievi carabinieri è stato cercato costruendo per tentativi un URL sul pattern `carabinieri.it/docs/default-source/concorsi/2026/<codice>/bando-di-concorso.pdf`. Il tentativo sul codice `mo208` ha restituito HTTP 200 e un PDF valido, che è stato inizialmente salvato con il nome del bando atteso.

Alla lettura dell'articolo 1 il documento è risultato essere un **altro concorso**: 65 allievi ufficiali del 208° corso dell'Accademia Militare, decreto del 21 novembre 2025. Il file è stato rinominato e riattribuito; il bando corretto è stato poi reperito su inPA e riscontrato sul testo.

**Regola che ne discende, da applicare a tutti i moduli:** un documento non va mai attribuito sulla base del percorso da cui è stato scaricato. L'attribuzione richiede la lettura del testo. Un HTTP 200 certifica che il file esiste, non che sia quello giusto.

## Correzioni di merito emerse dai testi ufficiali

1. **Sequenza delle prove GdF.** Le fonti secondarie descrivono la seconda prova come «tema di 6 ore». L'art. 1 comma 7 del bando la denomina **«prova scritta di cultura generale»**, in una sequenza di otto fasi da a) a h).
2. **Denominazione del bando CC 3.081.** Il testo dice «per **esami e titoli**»; le fonti secondarie riportano «per titoli ed esami».
3. **Instabilità dei bandi.** Il bando CC 898 ha subito **due decreti di modifica** in meno di due mesi, il 18 marzo e il 10 aprile 2026. Va usato come esempio nel capitolo del Bando Decoder.
4. **Terzo livello di ruolo.** Esiste un livello ufficiali, reclutato tramite Accademia Militare, che il modulo non contempla. Decisione di perimetro da sciogliere prima della fase C.

## Differenza strutturale fra i due corpi sulle prove fisiche

| | Polizia di Stato | Arma dei Carabinieri |
| --- | --- | --- |
| Terzo esercizio | **trazioni alla sbarra** (5 uomini / 2 donne) | **piegamenti sulle braccia** (soglia 25 / 20) |
| Logica di valutazione | soglia di ammissione + punteggio accessorio fino a 2 punti | prestazioni associate a punteggi graduati |
| Corsa 1000 m | 3'55" uomini / 4'55" donne | a punteggio |
| Salto in alto | 1,20 m / 1,00 m | 120 cm / 100 cm |

Due gesti atletici diversi, che si allenano in modo diverso: chi prepara entrambi i concorsi deve allenarli entrambi. È contenuto che il lettore non trova altrove in forma comparata, ed è esattamente ciò che giustifica il posizionamento premium del volume.

## Limite dichiarato

Il bando PS 4.400 è un **PDF immagine**: 15 MB, nessun testo estraibile. I dati di quel bando restano quelli verificati sulla pagina ufficiale della Polizia di Stato e sulla scheda inPA. La lettura dell'articolato richiede OCR o consultazione manuale, e non è stata svolta.

## Esito aggiornato

Audit **chiuso**. Il bilancio dei nuclei passa da «2 senza fonte, 8 parziali» a **nessun nucleo privo di fonte**, salvo la scopertura GdF sulle prove fisiche. I blocker di alta priorità residui non sono più di reperimento ma di **verifica**: leggere il testo vigente su Normattiva e sciogliere il rapporto fra d.m. 198/2003 e giurisprudenza successiva, che resta riservato a review umana.

La fase C **non è autorizzata**: il gate `coverage` continua a segnalare 26 nuclei `mancante`, perché nessun capitolo esiste.
