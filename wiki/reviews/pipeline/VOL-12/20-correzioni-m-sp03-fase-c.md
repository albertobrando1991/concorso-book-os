---
id: pipeline-vol-12-20-correzioni-m-sp03
type: pipeline_review
title: "VOL-12 — M-SP03: correzione da applicare prima della chiusura del modulo"
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp03-magistratura-avvocatura-notariato
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp03", "review", "correzioni"]
---

# VOL-12 — M-SP03: correzione da applicare prima della chiusura del modulo

Review della consegna in `19-consegna-m-sp03-fase-c.md`. I due gate sono stati rieseguiti su tutti e sette i capitoli e passano davvero. La sostanza è verificata con cura — in particolare la gestione dell'art. 5 della L. 89/1913 (il PDF locale storico manca delle pagine iniziali e non contiene l'articolo: il capitolo 4 lo dichiara esplicitamente e verifica il dato altrove) è un modello di rigore da conservare così com'è.

**Un solo difetto, ma presente in tutti e sette i capitoli e non dichiarato nella consegna.**

## Sezioni finali identiche in tutti i capitoli — bloccante

Ogni capitolo termina con tre heading — `## Spiegazione teorica`, `## Applicazione e caso`, `## Errori e trappole` — il cui contenuto è **letteralmente identico, parola per parola, in tutti e sette i file**:

```
## Spiegazione teorica

I nuclei precedenti espongono il quadro necessario e ne delimitano le fonti.

## Applicazione e caso

I casi ragionati trasformano ogni regola in una decisione osservabile e correggibile.

## Errori e trappole

Gli errori sono descritti sul testo o sul fascicolo, senza etichette diagnostiche.
```

Sono posizionate esattamente dove il `chapter-lint-gate` cerca le parole chiave «spiegazione/inquadramento», «caso/applicazione», «errore/trappola» per riconoscere le sezioni didattiche richieste. Non portano contenuto: sono una chiave nella serratura, e la stessa identica chiave in ogni porta.

È lo stesso difetto già corretto due volte in M-SP02 (vedi `13-correzioni-m-sp02-fase-c.md` e `15-correzione-residua-capitolo-01.md`), nonostante fosse stato esplicitamente indicato di usare i capitoli corretti di M-SP02 e M-SP04 come modello — che non hanno queste sezioni separate, perché il contenuto teorico, gli errori e le applicazioni sono già dentro i nuclei.

**Da fare, per ciascuno dei sette capitoli:** rimuovere le tre sezioni. Se contengono un'idea reale che manca al capitolo, quell'idea confluisce nel nucleo pertinente — non resta come sezione a sé con una frase sola. Il capitolo 01 ha anche una quarta sezione dello stesso tipo, `## Inquadramento` (una frase, 31 parole): stessa correzione.

Non toccare il resto: il `### ▣ Verifica ...` distribuito nucleo per nucleo, i «Caso ragionato» dentro ogni nucleo, il trattamento dell'art. 5 della L. 89/1913, e tutto il contenuto normativo verificato restano confermati.

## Nota di qualità, non bloccante

Il formato dei quiz in M-SP03 è diverso da quello usato in M-SP02 e M-SP04: qui sono due domande brevi per nucleo (dieci per capitolo, spesso a risposta sì/no), mentre negli altri due moduli è un blocco unico di sei domande a quattro opzioni con distrattori motivati. Il gate passa in entrambi i casi perché conta solo le occorrenze di «Risposta corretta:». Non è un blocco, ma è un'incoerenza di formato fra i moduli dello stesso volume: se c'è tempo, valutare se allineare almeno un blocco di verifica per capitolo al formato a quattro opzioni già usato altrove, per coerenza di lettura fra i moduli. Non è richiesto per chiudere il modulo.

## Da fare dopo la correzione

Rieseguire i due gate su tutti e sette i capitoli e riportare l'esito capitolo per capitolo nella consegna aggiornata, come da § 9 dell'ordine di lavoro originale.
