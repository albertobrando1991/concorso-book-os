---
id: pipeline-vol-12-05-audit-bandi-m-sp01
type: pipeline_review
title: "VOL-12 — Step 05: audit dei bandi rappresentativi M-SP01"
volume_code: VOL-12
step: "05"
phase: B
scope: module
module_code: M-SP01
domain: "concorsi pubblici italiani"
source_refs: ["sources/bandi-rappresentativi-m-sp01-forze-polizia-2026.md"]
book_refs: ["m-sp01-forze-ordine", "vol-12-carriere-speciali-premium"]
cut_off_date: 2026-08-10
checked_at: 2026-08-11
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-05", "m-sp01", "audit-bandi"]
---

# VOL-12 — Step 05: audit dei bandi rappresentativi M-SP01

**Data di controllo: 2026-08-10.** Corpus in [[sources/bandi-rappresentativi-m-sp01-forze-polizia-2026]].

## Corpus

Sei bandi su tre cluster, più lo stato del portale concorsi della Guardia di Finanza.

| # | Cluster | Bando | Ruolo | Posti | Verifica |
| --- | --- | --- | --- | ---: | --- |
| A1 | Polizia di Stato | 4.400 allievi agenti, D.C.P. 29/04/2026 | base | 4.400 | ✅ ufficiale |
| A2 | Polizia di Stato | 1.000 allievi vice ispettori, decreto 19/01/2026 | ispettivo | 1.000 | ✅ ufficiale |
| B1 | Carabinieri | 3.081 allievi carabinieri f.q., 146° corso | base | 3.081 | 🟡 secondaria |
| B2 | Carabinieri | 898 allievi marescialli, 16° corso triennale | ispettivo | 898 | 🟡 secondaria |
| C1 | Guardia di Finanza | stato del portale concorsi al 2026-08-10 | — | — | ✅ ufficiale |
| C2 | Guardia di Finanza | 983 allievi marescialli, 98° corso | ispettivo | 983 | 🟡 secondaria |

**Copertura del corpus: 3 cluster su 3, 2 livelli di ruolo su 2.** Due bandi su sei sono verificati su fonte ufficiale; quattro richiedono riscontro sul PDF del bando prima dell'uso in capitolo.

**Lacuna del corpus:** manca un bando pubblico GdF di livello base recente. Alla data di controllo il portale GdF espone in prevalenza procedure interne, e l'unica procedura pubblica aperta è la selezione straordinaria per allievi finanzieri **atleti**, che non è rappresentativa. Va colmata alla prossima tornata.

## Tabella delle ricorrenze

Presenza di ciascuna fase nei sei bandi del corpus.

| Fase | A1 agenti PS | A2 v.isp. PS | B1 all.car. | B2 mar. CC | C2 mar. GdF | Ricorrenza |
| --- | :---: | :---: | :---: | :---: | :---: | ---: |
| Preselezione | no | — | — | sì | sì | 2/5 |
| Prova scritta | sì | sì | sì | sì | sì | **5/5** |
| Efficienza fisica | sì | sì | sì | sì | sì | **5/5** |
| Accertamenti psico-fisici | sì | sì | sì | sì | sì | **5/5** |
| Accertamento attitudinale | sì | sì | sì | sì | sì | **5/5** |
| Valutazione dei titoli | sì | — | sì | — | sì | 3/5 |
| Prova orale / colloquio | **no** | **sì** | sì | **sì** | **sì** | 4/5 |
| Lingua straniera facoltativa | — | — | — | — | sì | 1/5 |

**Il nucleo invariante è di quattro fasi**, presenti in tutti i bandi del corpus: prova scritta, efficienza fisica, accertamenti psico-fisici, accertamento attitudinale. È la spina dorsale del modulo ed è la sequenza che il lettore deve interiorizzare.

## Differenze tra profili — il rilievo principale dell'audit

L'audit smentisce l'assunto su cui era costruito il piano editoriale di M-SP01.

**Assunto precedente:** il modulo ha binario unico e confronta tre corpi (Polizia di Stato, Carabinieri, Guardia di Finanza).

**Evidenza dei bandi:** la differenza fra i tre corpi è molto minore della differenza fra i due **livelli di ruolo**, e quest'ultima attraversa tutti e tre i corpi.

| Dimensione | Livello base (agenti · carabinieri · finanzieri) | Livello ispettivo (vice ispettori · marescialli) |
| --- | --- | --- |
| Età massima | 24-29 non compiuti secondo il corpo | 26 non compiuti (CC e GdF); requisiti d'art. per PS |
| Titolo di studio | diploma | diploma, con requisito di accesso universitario per GdF |
| Prova scritta | quiz su banca dati ufficiale (PS 4.400) | **formati radicalmente diversi**: banca dati di 5.000 quesiti (PS), componimento di italiano (CC), tema di 6 ore (GdF) |
| Prova orale | **assente** in A1 | **presente** in A2, B2, C2 |
| Preselezione | assente in A1 | presente in B2 e C2 |
| Esito | ferma o immissione in ruolo | corso pluriennale di scuola, con percorso universitario (CC: Firenze, indirizzo giuridico-amministrativo) |
| Riserve | contingenti VFP e bilinguismo | riserve interne al Corpo e categorie protette |

Il fatto più significativo: **allo stesso livello di ruolo, la prova scritta ha tre formati incompatibili**. Un candidato ispettore della Polizia di Stato studia una banca dati chiusa di 5.000 quesiti; un aspirante maresciallo dei Carabinieri scrive un componimento di italiano; un aspirante maresciallo della Guardia di Finanza scrive un tema in sei ore. Sono tre preparazioni diverse che nessuna trattazione unitaria può servire.

**Conseguenza sull'architettura del modulo:** M-SP01 richiede due binari — **base** e **ispettivo** — e, dentro il binario ispettivo, tre percorsi di scrittura distinti per corpo. Il confronto fra i tre corpi resta, ma come dimensione secondaria.

## Secondo rilievo — il peso della banca dati ufficiale

Due dei bandi verificati fondano la prova scritta su una banca dati ufficiale pubblicata in anticipo: 5.000 quesiti per i vice ispettori PS, pubblicati il 22 aprile 2026 per una prova del 25-28 maggio. Il fattore decisivo non è la conoscenza della materia ma **il metodo di studio di un insieme chiuso e ampio in tempi brevi**.

Il VOL-01 ha già un capitolo dedicato: `banca-dati-ufficiale-studiarla-senza-memorizzare-male.md`. Per la logica di copertura v4 questo è un **rinvio con delta**, non contenuto nuovo. Il delta di M-SP01 è la compressione temporale: poche settimane fra pubblicazione della banca dati e prova.

## Terzo rilievo — pubblico contro interno

Alla data di controllo il portale della Guardia di Finanza espone in prevalenza procedure **interne**: il 27° corso allievi marescialli (~410 posti) è riservato a sovrintendenti e ruoli inferiori del Corpo; i 28 sottotenenti del comparto speciale sono anch'essi interni.

È una distinzione che il candidato civile confonde sistematicamente e che determina l'ammissibilità della domanda. Va trattata esplicitamente.

## Quarto rilievo — divergenza sistematica delle fonti secondarie

Per il bando A1 le fonti secondarie di settore riportano concordemente un limite di età di «18-26 anni». La pagina ufficiale della Polizia di Stato indica **29 anni non compiuti** per civili e bilinguisti e 28 per i VFP, con elevazione fino a tre anni per servizio militare prestato.

Un modulo costruito sulla stampa di settore avrebbe pubblicato un requisito sbagliato su un dato che determina l'ammissione. È la giustificazione operativa della regola della Bibbia del Volume: ogni claim risale alla fonte ufficiale, e ogni tabella di requisiti porta il box **Verifica sul bando**.

## Lacune dell'indice attuale

Confronto fra le 11 sezioni del piano editoriale di M-SP01 e l'evidenza dei bandi.

| # | Lacuna | Gravità | Intervento |
| --- | --- | --- | --- |
| L1 | Architettura a binario unico, smentita dai bandi | 🔴 | introdurre i binari **base** e **ispettivo** |
| L2 | Nessuna sezione sulla **prova orale**, presente in 4 bandi su 5 | 🔴 | sezione dedicata nel binario ispettivo |
| L3 | Nessuna sezione sui **formati della prova scritta**, che divergono per corpo | 🔴 | sezione con i tre formati: banca dati, componimento, tema |
| L4 | Nessuna sezione sulla **valutazione dei titoli**, presente in 3 bandi su 5 | 🟠 | sezione breve nel nucleo |
| L5 | Nessuna trattazione della **preselezione**, presente in 2 bandi su 5 | 🟠 | assorbire nella sezione sui formati |
| L6 | Nessuna distinzione fra procedura **pubblica** e **interna** | 🟠 | box o paragrafo nella mappa della famiglia |
| L7 | **Prova facoltativa di lingua straniera** non prevista | 🟡 | menzione nella sezione sui titoli |
| L8 | Il piano 30/60/90 non tiene conto della compressione della banca dati | 🟡 | variante «banca dati pubblicata» nel piano di studio |
| L9 | Contingenti VFP, civili e bilinguisti trattati solo come «riserve» | 🟡 | ampliare: sono procedure distinte con requisiti diversi |

## Struttura rivista di M-SP01

Applicando L1-L9. Le sezioni marcate **[base]** e **[isp]** appartengono ai due binari; **[nucleo]** è impostazione condivisa con gli altri moduli della famiglia.

1. **[nucleo]** Mappa della famiglia: tre corpi, due livelli di ruolo, procedure pubbliche e interne.
2. Scegliere il binario: base o ispettivo, e cosa cambia davvero.
3. **[nucleo]** Profili tipici e prove ricorrenti: la sequenza invariante a quattro fasi.
4. Requisiti, limiti di età, contingenti (civili · VFP · bilinguisti), riserve e cause di esclusione.
5. I formati della prova scritta: banca dati ufficiale, componimento di italiano, tema lungo, preselezione.
6. La catena degli accertamenti: efficienza fisica, idoneità psico-fisica, accertamento attitudinale.
7. Preparazione atletica e gestione del rischio di esclusione in itinere.
8. **[isp]** La prova orale e il colloquio: struttura e criteri.
9. La valutazione dei titoli e la prova facoltativa di lingua straniera.
10. **[nucleo]** Materie comuni da riusare dal VOL-01, con delta esplicitato.
11. Materie specialistiche: ordinamento dei corpi, nozioni essenziali di diritto e procedura penale, pubblica sicurezza.
12. **[nucleo]** Bando Decoder adattato alla famiglia.
13. Piano 30/60/90 a doppio binario, con variante «banca dati pubblicata».
14. Errori frequenti, tagli da evitare e casi guidati per binario.
15. **[nucleo]** Checklist finale del modulo.

Da 11 a 15 sezioni. L'incremento è interamente giustificato dall'evidenza dei bandi.

## Da chiudere prima della fase C

- [ ] riscontro sul PDF ufficiale dei quattro bandi classificati DA VERIFICARE (B1, B2, C2 e il concorso 69 allievi ufficiali GdF);
- [ ] reperimento di un bando pubblico GdF di livello base rappresentativo;
- [ ] step 06 — audit delle fonti normative: ordinamento dei tre corpi, disciplina dei requisiti psico-fisici e attitudinali;
- [ ] step 07 — matrice di copertura didattica sulla struttura a 15 sezioni.

## Esito

Audit **chiuso**. Il corpus copre tutti i cluster e tutti i livelli di ruolo, con due bandi verificati su fonte ufficiale e quattro tracciati con livello di verifica dichiarato. L'architettura del modulo è stata corretta sulla base dell'evidenza raccolta, non su assunti.
