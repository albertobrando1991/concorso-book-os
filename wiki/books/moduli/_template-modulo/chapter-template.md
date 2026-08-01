# Template capitolo modulo specialistico

Usare questo schema dentro `chapters/`. Ogni nuova scrittura o passaggio dagli step 08-12 usa il formato 2.

## Frontmatter capitolo

```yaml
type: book_chapter
book_id: <slug-modulo>
outline_section: <numero-capitolo>
title: <titolo senza numero>
module_code: <codice-modulo>
module_family: <famiglia>
format_version: 2
dati_operativi: []
source_refs: []
last_compiled_from: []
draft_stage: working
review_required: true
```

Non inserire il numero dentro `title` o nell'H1. La dashboard deriva il numero da `outline_section`.

## Schema contenuto

```markdown
# Titolo del capitolo

## Obiettivo del capitolo
## Mappa BANDO

## N-XX00-00-01 · Titolo del nucleo
Teoria essenziale, schema o tabella, applicazione al profilo.

## N-XX00-00-02 · Titolo del nucleo

> **Dato operativo — Titolo**
> Ambito: <ambito> · Livello: <nazionale/europeo>
> Fonte: <source note ufficiale> · Versione: <versione> · Verificata al: <YYYY-MM-DD>
> <contenuto non esecutivo ammesso dalla policy>
> Review: <REV-CODICE> (<competenza>)

## ▣ Verifica 00.A
Almeno 6 quiz con risposta commentata e 1 caso ragionato.

## Errori e trappole ricorrenti
## Checklist finale
## Riferimenti normativi e professionali
```

Minimi ordinari: 5 nuclei, 600 parole per nucleo, 3.000 parole per capitolo, 6 quiz commentati e 1 caso. Un blocco `▣ Verifica` ogni 5-7 nuclei. Soglie diverse devono essere dichiarate nella scheda pipeline.

Le schede di lavoro e le note di review sono artefatti interni: vanno in `wiki/reviews/`, non nel testo destinato al lettore.

Ogni box `Dato operativo` deve avere un ID in `dati_operativi`; la pipeline lo trasforma automaticamente in una riga obbligatoria del pacchetto di review umana dello step 15.
