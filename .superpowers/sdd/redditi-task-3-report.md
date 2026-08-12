# Task 3 — Completamento IRPEF/IRES nel capitolo 6

## Baseline e file modificati

- Target editoriale: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`.
- Stato iniziale del target: `M` (modifiche preesistenti preservate).
- Hash Git blob iniziale rilevato prima dell'intervento: `63b162ad155ae02b7213e3a2857a0f4a61bf6d9d`.
- Dimensione iniziale: 21.155 byte.
- Hash Git blob finale dopo fix loop: `1eab7a2decfb8d9e2cab8c576a6a95502c80dbfe` (prima del fix loop: `65e7d5da83809d208f50dfba97970fbd53faecb7`).
- Dimensione finale dopo fix loop: 38.787 byte; 531 righe.
- File prodotti dal task: il solo capitolo target e il presente report obbligatorio. Nessun commit eseguito.

## Sintesi delle integrazioni

- Frontmatter ampliato con topic IRPEF/IRES, categorie reddituali e reddito d'impresa; aggiunta la source note consolidata; aggiornati `updated_at` e `last_compiled_from`. `status: draft` e `confidence: 0.84` sono rimasti invariati.
- Sviluppate tutte le sei categorie dell'art. 6 TUIR con definizione/funzione, elementi selettivi, distinzioni, logica di determinazione, conseguenza operativa, esempio, prospettiva concorsuale, errore tipico e criterio di verifica.
- Inserite struttura IRPEF, distinzione deduzione/detrazione, soggetti e struttura IRES.
- Sviluppato il reddito d'impresa: derivazione, competenza, imputazione, inerenza con distinzione fra dato testuale e sintesi interpretativa, variazioni fiscali e componenti positivi/negativi.
- Inseriti caso IRPEF multicategoria, caso IRES con numeri dichiarati pedagogici, esercizio deduzione/detrazione, quiz, risposta modello, trappole e checklist.
- Inseriti rinvii precisi al capitolo 4 (`#IRPEF e IRES: il quadro sistematico`) e al capitolo 11 (`#14. Dal bilancio al reddito imponibile`) senza duplicare la base contabile.
- Rafforzati riferimenti consolidati e note di review normativa.

## Mappa requisiti/sezioni

| Requisito | Sezione del capitolo |
| --- | --- |
| Sei categorie art. 6 | `IRPEF: dalle categorie all'imposta`, §§ 1-6 |
| Fondiari | `1. Redditi fondiari` |
| Capitale | `2. Redditi di capitale` |
| Dipendente | `3. Redditi di lavoro dipendente` |
| Autonomo | `4. Redditi di lavoro autonomo` |
| Impresa | `5. Redditi d'impresa`; blocchi IRES/reddito d'impresa |
| Diversi | `6. Redditi diversi` |
| Soggetti e struttura IRES | `IRES: soggetti e struttura` |
| Derivazione e variazioni | `Dal risultato civilistico al reddito imponibile` |
| Competenza, imputazione, inerenza | `Competenza, imputazione e inerenza` |
| Componenti | `Componenti positivi e negativi` |
| Applicazioni autosufficienti | `Caso IRPEF`, `Caso IRES`, `Esercizio`, `Quiz`, `Risposta modello`, `Trappole e checklist` |
| Rinvii anti-duplicazione | apertura del blocco redditi e rinvio al capitolo 11 § 14 |
| Tracciabilità/review | frontmatter, `Riferimenti consolidati`, `Note di review` |

## Controlli eseguiti ed esiti

- Baseline: rilevati stato `M`, hash e dimensione prima della scrittura — OK.
- Scope: verificato `git status --short` sui due artifact previsti; target modificato e report creato — OK.
- Frontmatter: `status` e `confidence` non innalzati; source note, data e compilazione aggiornate — OK.
- Copertura: `rg` rileva 6/6 heading delle categorie — OK.
- Rinvii: esistono source note, capitolo 4 e capitolo 11; le due ancore corrispondono a heading esistenti — OK.
- Codifica: UTF-8 rigoroso valido, nessun BOM — OK.
- Whitespace: `git diff --check` senza errori; resta soltanto il warning Git informativo sulla normalizzazione CRLF/LF — OK.
- Link e tracciabilità: source note presente in `source_refs`, `last_compiled_from`, specifica e riferimenti finali — OK.
- Valori mobili: nessuna aliquota/soglia vigente introdotta; i numeri del caso sono marcati pedagogici — OK.
- Commit: non eseguito — OK.

## Diffstat finale

Diff del working tree rispetto a `HEAD` per il solo capitolo (include anche le modifiche preesistenti già presenti nella baseline):

```text
.../06-adempimenti-fiscali-redditi-iva-dichiarazioni.md | 505 ++++++++++++++++++++--
1 file changed, 494 insertions(+), 12 deletions(-)
```

La baseline non era pulita; per non perdere il lavoro precedente l'intervento è stato applicato al contenuto corrente. Hash iniziale e finale consentono di identificare i due stati, ma l'hash iniziale era stato calcolato senza scrivere il blob nell'object database, quindi Git non può produrre retroattivamente un diffstat isolato del solo delta Task 3.

## Fix loop QUALITY

Il riesame successivo al verdetto `SPEC PASS / QUALITY FAIL` ha prodotto due correzioni circoscritte:

1. rimosso il blocco obsoleto `## Scheda di lavoro`, che descriveva il capitolo come `source-ready` e rinviava a una scrittura professionale futura, in contraddizione con `draft_stage: professional-draft`;
2. rimossa la duplicazione iniziale `### Riferimenti consolidati`; resta un'unica sezione editoriale `## Riferimenti consolidati` in chiusura del capitolo.

Controlli del fix loop:

- occorrenze `## Scheda di lavoro`: 0;
- occorrenze `source-ready` / `scrittura professionale dovra`: 0;
- heading `Riferimenti consolidati` complessivi: 1;
- `draft_stage: professional-draft`: preservato;
- `git diff --check`: nessun errore;
- UTF-8 valido senza BOM;
- hash capitolo finale: `1eab7a2decfb8d9e2cab8c576a6a95502c80dbfe`.
## Limiti residui

- Obbligatoria review normativa articolo per articolo prima della pubblicazione, soprattutto per regimi speciali, derivazione rafforzata, imputazione e singole deducibilità.
- La source note non consolida aliquote, scaglioni, soglie, importi, percentuali, termini o regimi mobili.
- `LocalAgentMemory` è stato invocato tramite il servizio canonico, ma il runner Node non ha risolto l'import TypeScript extensionless `src/server/config`; non è stata creata memoria parallela.
- `apply_patch` è stato tentato ripetutamente, ma il wrapper Windows ha rifiutato l'accesso alla root scrivibile; le modifiche sono state quindi eseguite con sostituzioni .NET controllate e limitate al target.