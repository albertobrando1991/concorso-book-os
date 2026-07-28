---
id: workflow-editoriale-vol-01
type: editorial_workflow
title: "VOL-01 - Workflow editoriale e stati dei capitoli"
status: active
book_refs: ["il-metodo-bando"]
created_at: "2026-07-23T00:00:00+02:00"
updated_at: "2026-07-23T00:00:00+02:00"
canonical: true
---

# Workflow editoriale di VOL-01

`draft_stage` descrive la fase editoriale del file; `review_required` resta il gate indipendente che impedisce di dichiarare un capitolo pubblicabile.

| `draft_stage` | Significato | Condizione di uscita |
|---|---|---|
| `editorial-draft` | Testo scritto ma non ancora sottoposto a revisione editoriale strutturata. | Passaggio al Revisore Editoriale Totale. |
| `editorial-review` | Testo in revisione: correzioni, fonti, superficie e copertura didattica sono sotto controllo. | Tutte le issue pertinenti sono chiuse e la matrice non segnala blocker. |
| `publication-ready` | Testo approvato per l'impaginazione e la pubblicazione. | `review_required: false`, preview verificata e nessun gate normativo/editoriale aperto. |

## Regola applicata con P12

Il volume cartaceo principale (introduzione, Capitoli 1-24 e Appendici A-F) è uniformato a `editorial-review`: tutti i file hanno ancora `review_required: true` e nessuno può quindi essere anticipato a `publication-ready`.

Il Ricettario digitale mantiene il proprio stato fino alla sua revisione dedicata: non è stato usato per simulare la chiusura del cartaceo.

## Regola applicata con P34

Con P34 il gate viene aperto in modo selettivo e onesto: avanzano a `publication-ready` (`review_required: false`) solo i file **privi di dottrina giuridica aperta e privi di fonti mobili non ricontrollate** (bandi, catalogo, norme in evoluzione). Restano a `editorial-review` con `review_required: true` tutti i capitoli che dipendono da un gate giuridico o normativo umano non ancora eseguito.

**Avanzati a `publication-ready` (14 file):** Introduzione; Cap. 1 Il nuovo candidato; Cap. 3 Il Metodo BANDO; Cap. 11 Inglese; Cap. 12 Logica; Cap. 13 Metodo di studio; Cap. 14 La prova a quiz; Cap. 16 La prova orale; Cap. 22 Piano 30/60/90; Cap. 23 Diario degli errori; Cap. 24 Checklist operative; Appendici C, D, E.

Per Cap. 11 e Cap. 12 la review residua (linguistica madrelingua, metodologica/psicometrica) è **consigliata e non bloccante**: non è un gate giuridico.

**Mantenuti a `editorial-review` / `review_required: true` (17 file):** Cap. 2 Anatomia del bando (regole concorsuali mobili); Capp. 4-10 (diritto costituzionale, amministrativo, pubblico impiego e reati PA, trasparenza/privacy, contabilità, contratti, informatica/PA digitale); Cap. 15 Prova scritta (atto e norme); Cap. 17 Casi pratici (norme mobili); Cap. 18 Quesiti situazionali (codice di comportamento e framework competenze); Capp. 19-21 (bandi e catalogo mobili); Appendici A, B (voci con review normativa) e F (catalogo).

Il passaggio a `publication-ready` dei 17 file trattenuti avverrà **solo dopo** la review giuridica umana articolo per articolo e il ricontrollo delle fonti mobili con data di vigenza; non è delegabile all'agente.
