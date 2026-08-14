# Presa in carico — VOL-10

- Target: `VOL-10`, volume commerciale tecnico-ingegneristico composto dal modulo `M-TR03`.
- File canonici: `wiki/AGENTS.md`; architettura moduli; design system editoriale; scheda e indice VOL-10; indice, matrice, capitoli e planning M-TR03; run-state gestito esclusivamente dal CLI.
- Memoria richiamata: scope `VOL-10`, con esiti pertinenti degli step 12 dei capitoli e istruzione stabile su copertura, rinvii verificati e preservazione del lavoro.
- Skill in ordine: `pipeline-volume`; `concorso-book-professional-writer` per eventuali correzioni sostanziali; `humanizer` per riscritture; `revisore-editoriale-totale` per step 15 e 21; `canvas-design` per step 18; `verification-before-completion` prima della consegna.
- Stato Git: worktree già modificato all'avvio in memoria locale, log e report VOL-03; tali file sono estranei all'incarico e non vengono alterati intenzionalmente. Le modifiche VOL-10 e M-TR03 sono quelle prodotte dalla pipeline corrente.
- Rischi/collisioni: `doctor` non riconosce Git dall'interno del processo Node e non registra il merge driver per `spawn EPERM`; i comandi Git diretti funzionano. Nessun reset, checkout o cancellazione eseguito. Run-state modificato soltanto dal CLI.
- Piano limitato: completare in ordine i target pendenti; applicare gate e accettazioni manuali solo con evidenza; impaginare e preflightare nel Book Studio; fermarsi allo step 24 se richiede una conferma umana non delegabile.
