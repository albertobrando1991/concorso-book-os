---
id: pipeline-vol-12-05-handover-audit-bandi
type: pipeline_review
title: "VOL-12 — Step 05: consegna e requisiti dell'audit dei bandi"
volume_code: VOL-12
step: "05"
phase: B
scope: module
domain: "concorsi pubblici italiani"
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-05", "handover"]
---

# VOL-12 — Step 05: consegna e requisiti dell'audit dei bandi

**Questo non è il verbale di un audit eseguito.** È la consegna dello step 05, aperto e non completato, con la specifica di ciò che serve per chiuderlo.

## Perché lo step si ferma qui

Gli step 00-04 sono stati completati perché operano su materiale interno al repository: censimento, catalogo, impianto editoriale. Lo step 05 cambia natura: richiede **5-6 bandi reali per cluster, da fonti ufficiali o istituzionali, con data di controllo 2026-08-10**.

Non è un lavoro che possa essere svolto per deduzione. Un audit dei bandi costruito su requisiti ricordati o plausibili produrrebbe tabelle di requisiti, limiti di età e strutture di prova false, che verrebbero poi ereditate da ogni capitolo a valle e da ogni quiz. È esattamente il rischio che la Bibbia del Volume vieta e che la regola «non inventare norme, articoli, date, dati o fonti» esclude.

Lo step resta quindi `in-progress` sul run-state: preso in carico, non chiuso.

## Cosa serve per chiudere lo step 05 su M-SP01

### Corpus dei bandi

Tre cluster, 5-6 bandi ciascuno, da fonte ufficiale:

| Cluster | Fonti istituzionali di riferimento |
| --- | --- |
| Polizia di Stato | portale ufficiale della Polizia di Stato; Gazzetta Ufficiale 4ª serie speciale; portale inPA |
| Arma dei Carabinieri | portale ufficiale dell'Arma; Gazzetta Ufficiale 4ª serie speciale |
| Guardia di Finanza | portale ufficiale della Guardia di Finanza; Gazzetta Ufficiale 4ª serie speciale |

Per ogni bando vanno registrati: ente, profilo e sottoprofilo, requisiti, materie, peso o ricorrenza delle materie, tipologia delle prove, output richiesti, competenze specialistiche, elementi mobili da ricontrollare.

### Policy di ingest da rispettare

1. raw immutabile del bando, se necessario;
2. source note consolidata per ciascun bando o famiglia di bandi;
3. topic ed entity page aggiornate;
4. collegamento ai capitoli impattati;
5. log append-only.

Nessun testo di bando va trasferito direttamente nel capitolo.

### Output attesi

- corpus dei bandi;
- tabella delle ricorrenze delle materie;
- differenze tra profili;
- lacune dell'indice attuale;
- data di controllo `2026-08-10`.

## Lo stesso vale per gli altri tre moduli

| Step | Modulo | Cluster da coprire |
| --- | --- | --- |
| 05 | M-SP02 | profili operativi VVF · profili direttivi e tecnici VVF |
| 05 | M-SP03 | magistratura ordinaria · Avvocatura dello Stato · notariato |
| 05 | M-SP04 | carriera prefettizia · carriera diplomatica |

Complessivamente: **circa 24-30 bandi ufficiali** da reperire, schedare e analizzare prima che la fase B possa dirsi conclusa.

## Vuoti di fonti da colmare allo step 06

Lo step 01 ha accertato che su 321 source notes del wiki nessuna è stata prodotta per questa famiglia. Sono riutilizzabili dopo rischedatura, e solo in parte:

| Fonte esistente | Modulo | Copertura |
| --- | --- | --- |
| `corte-costituzionale-requisiti-concorsuali-polizia-di-stato-g-u-27-gennaio-2021.md` | M-SP01 | parziale |
| `codice-procedura-penale-polizia-giudiziaria.md` | M-SP01 | parziale |
| `regio-decreto-18-giugno-1931-n-773-tulps-polizia-amministrativa.md` | M-SP01 | parziale |
| `avvocatura-stato-organizzazione-funzioni.md` | M-SP03 binario B | parziale |
| `rd-30-ottobre-1933-n-1611-avvocatura-stato.md` | M-SP03 binario B | parziale |
| `ministero-interno-dait-anpr-finanza-locale.md` | M-SP04 binario A | marginale |

**Nessuna fonte esiste** per: Corpo nazionale dei vigili del fuoco, ordinamento giudiziario e accesso alla magistratura, notariato, carriera diplomatica, disciplina delle prove linguistiche. Sono cinque delle dieci competenze obbligatorie per l'audit specialistico definite nella Bibbia del Volume.

## Come riprendere

```
npm run pipeline -- status VOL-12 --json
npm run pipeline -- next VOL-12 --json          # ripresenta il prompt dello step 05 su M-SP01
npm run pipeline -- complete VOL-12 --step 05 --module M-SP01
```

Se lo step risulta in carico a un altro proprietario, subentrare con `--force`.

## Stato del volume alla consegna

| Fase | Step | Stato |
| --- | --- | --- |
| A | 00 presa in carico | ✅ completato |
| A | 01 censimento staff | ✅ completato |
| A | 02 consolidamento contributi | ✅ completato |
| A | 03 riconciliazione catalogo | ✅ completato |
| B | 04 scheda di apertura e Bibbia del Volume | ✅ completato |
| B | 05 audit bandi M-SP01 | 🟡 in carico, non chiuso |
| B | 05-07 sui restanti moduli | ⬜ da eseguire |
| C-F | 08-23 | ⬜ non ancora dichiarati nella scheda |
| — | 24 conferma umana | ⬜ |
