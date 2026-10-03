# Allineamento staff — revisione collana, 3 ottobre 2026

Questo checkpoint condivide le modifiche editoriali già effettuate sui dodici volumi e lo stato reale della revisione digitale. **Non costituisce un via libera alla pubblicazione.** Il branch di consegna è `codex/revisione-collana-2026-10-03`.

## Materiale da usare

- [Indice della consegna revisionata](../delivery/COLLANA-REVISIONATA-2026-10-03.md): sorgenti, tredici interni PDF (volume 2 in due tomi), copertine, manifest e rapporti dei dodici pacchetti correnti.
- [Registro delle correzioni](../wiki/reviews/correzioni-collana-2026-10-02/registro-applicazione-consolidato-2026-10-03.md): 582 rilievi originari, 577 verificati, con questioni parziali e migliorie facoltative distinte.
- [Revisione del percorso digitale](../wiki/reviews/correzioni-collana-2026-10-02/DIGITALE.md): dodici candidati online, 348 unità, 251 asset e differenze rispetto al perimetro PDF.
- [Avanzamento Ricettario](../artifacts/correzioni-collana-2026-10-02/ricettario-review/working-notes.md): lettura integrale del testo di R1–R11; R12–R23 ancora da leggere. I rilievi annotati durante questa lettura sono da correggere e verificare. Le tre precedenti correzioni ai rinvii interni in R4/R11/R20 sono già applicate.

La priorità richiesta dall'utente è la correttezza e completezza dei volumi digitali sul sito. Il Ricettario contiene 23 moduli esterni alla precedente revisione integrale dei volumi principali. Restano da completare questa revisione, il controllo delle immagini effettivamente usate online e il collaudo del lettore del sito. Gli stati dei gate non sono stati promossi in massa; nessun signoff finale viene concesso da questo commit.

## Interventi software inclusi

Esportazione senza troncamento silenzioso dei capitoli; conservazione delle sezioni didattiche; gestione di tabelle, didascalie e gruppi di blocchi nella paginazione; aggiornamenti del catalogo e degli audit; invalidazione della conferma finale dopo riapertura in cascata. Sono inclusi i relativi test. Il generatore di piani di studio presente nel workspace appartiene a un lavoro separato e non fa parte del checkpoint.

## Verifiche ripetute per la consegna Git

- `npm run typecheck`: superato nel workspace.
- Undici file di test mirati a export, paginazione e pipeline: 123 test superati.
- `verify-register-packages.py`: dodici pacchetti e 2.580 file verificati, nessuna difformità rispetto ai manifest.
- `verify-digital-candidates.py`: nessuna difformità nelle fonti e negli asset dei candidati digitali, nessun blocco vuoto o riferimento a immagine mancante; nessun residuo dei pattern interni cercati. Non è una certificazione della correttezza di ogni frase.
- `scripts/verify-editorial-staff-sync.py`: corrispondenza esatta tra indice Git e 3.229 file verificati, senza difformità; nessuna occorrenza dei pattern di credenziali cercati.

Il controllo globale `git diff --cached --check` resta non superato: segnala spazi finali e righe vuote negli apparati testuali, nelle acquisizioni e negli snapshot, comprese interruzioni Markdown intenzionali. Nessuna segnalazione nei file applicativi o nei test modificati. Gli snapshot identificati dagli hash non sono stati ripuliti alterando le evidenze; il controllo non viene dichiarato verde.

I controlli su hash richiedono gli stessi byte verificati: le regole `.gitattributes` preservano i ritorni a capo dei capitoli e dei pacchetti. I manifest storici conservano il commit di riferimento originario e la provenienza dalla working tree; non vanno riscritti per attribuire retroattivamente un commit inesistente al momento della verifica.

Le fonti ufficiali acquisite, le note consolidate, i registri e gli script editoriali sono inclusi. Cache, cookie, log temporanei e copie intermedie delle tavole di controllo visivo rimangono locali; i pacchetti correnti in `delivery/` conservano le evidenze di consegna. Alcuni rinvii storici a prove intermedie possono pertanto riguardare artefatti disponibili solo nel workspace originario.

Per proseguire, usare questo branch e i sorgenti correnti. Non sostituire i pacchetti PDF verificati con esportazioni generiche senza confronto e non equiparare il push su GitHub a una pubblicazione sul sito.
