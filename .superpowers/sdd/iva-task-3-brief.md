# Task 3 brief — M-FC02 IVA e adempimenti nel capitolo 6

Plan: `docs/superpowers/plans/2026-07-20-m-fc02-iva-adempimenti.md`

## Global constraints

## Global Constraints

- Seguire `wiki/AGENTS.md` e usare `LocalAgentMemory`; se il runner non Ã¨ disponibile, documentare l'errore senza creare memorie parallele.
- Applicare `concorso-book-professional-writer` e l'Integral Didactic Coverage Gate.
- Il testo editoriale deriva soltanto da `wiki/sources/`, `wiki/topics/`, `wiki/entities/` e conoscenza consolidata; non scrivere dai raw.
- Preservare tutte le modifiche preesistenti del worktree e usare `apply_patch` per le modifiche; se il wrapper Windows lo impedisce, registrare il fallimento prima di un fallback chirurgico sul solo file autorizzato.
- Usare struttura normativa stabile; aliquote, soglie, termini, modelli, codici e regole telematiche soltanto se ufficialmente verificati, datati e didatticamente necessari.
- Non presentare l'IVA come neutrale in modo assoluto; non confondere non imponibilitÃ , esenzione ed esclusione; non descrivere detrazione o compensazione come incondizionate.
- Non duplicare nei capitoli 4 e 6 la disciplina responsabile dei capitoli 5, 5A, 5B e 7.
- Ogni task richiede implementazione, SPEC COMPLIANCE review, QUALITY review, fix loop e commit isolato.
- Governance attesa dopo approvazione: 80 nuclei, 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`, 14 blocker; giudizio globale ancora `Non pubblicabile allo stato attuale`.

### Task 3: Operazioni IVA e ciclo degli adempimenti nel capitolo 6

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`
- Create: `.superpowers/sdd/iva-task-3-report.md`

**Interfaces:**
- Consumes: source note approvate, quadro teorico del Task 2 e anchor esistenti dei capitoli 5, 5A, 5B e 7.
- Produces: trattazione teorico-operativa autosufficiente che sostiene la chiusura dei due blocker.

- [ ] **Step 1: Registrare baseline e proteggere il blocco redditi**

Rilevare stat/hash e salvare la mappa delle sezioni IRPEF/IRES giÃ  approvate. Il diff finale deve dimostrare che il nuovo intervento Ã¨ circoscritto a IVA, adempimenti, apparato applicativo condiviso, riferimenti e review.

- [ ] **Step 2: Sviluppare le operazioni IVA a Livello 3**

Integrare progressivamente:

```text
cessioni / prestazioni
soggettivitÃ  IVA
territorialitÃ  essenziale
imponibile / non imponibile / esente / esclusa
effettuazione / esigibilitÃ 
base imponibile / aliquota
rivalsa / detrazione
documentazione / registrazione / liquidazione
```

Ogni nucleo deve includere teoria, conseguenza operativa, esempio, errore e controllo dell'apprendimento.

- [ ] **Step 3: Sviluppare dichiarazioni, versamenti e compensazioni**

Usare la sequenza canonica:

```text
fattispecie â†’ documentazione â†’ registrazione â†’ liquidazione â†’ dichiarazione â†’ versamento o compensazione â†’ controllo â†’ eventuale correzione
```

Spiegare dichiarazione originaria, correttiva, integrativa e omessa; versamento unitario/F24; compensazione verticale e orizzontale; limiti e controlli; errore, correzione e rimborso; rinvii precisi alle sedi responsabili.

- [ ] **Step 4: Costruire l'apparato applicativo**

Inserire con soluzione motivata:

```text
caso IVA completo
caso comparativo sulle quattro classi di operazioni
caso correttiva vs integrativa
esercizio debiti-crediti-compensazione con dati pedagogici
quiz ragionati
risposta modello alla commissione
domande-trappola
errori frequenti
checklist e diario degli errori
```

Gli esempi numerici devono dichiarare la natura pedagogica dei valori.

- [ ] **Step 5: Aggiornare frontmatter, riferimenti e note di review**

Registrare le nuove source note; mantenere `status` e `confidence` prudenti; indicare le verifiche pre-pubblicazione per dati mobili e sistemi telematici.

- [ ] **Step 6: Eseguire il gate del capitolo 6**

Controllare tutte le promesse della specifica, anchor verso capitoli 4/5/5A/5B/7, assenza di scaffold redazionali, preservazione IRPEF/IRES, UTF-8 e:

```powershell
git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

- [ ] **Step 7: Review indipendente e commit**

Ottenere entrambi i PASS, correggere rilievi e committare:

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
git commit -m "docs: complete M-FC02 VAT and filing coverage"
```

---

