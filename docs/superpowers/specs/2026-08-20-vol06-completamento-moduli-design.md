# Progetto di completamento editoriale VOL-06

## Obiettivo

Portare `VOL-06 — Scuola, Università, Ricerca e Cultura` da bozza modulare a pacchetto verificato e pubblicabile, senza saltare l'ordine dei gate del CLI.

## Perimetro

Il volume comprende quattro moduli: M-IR01 Scuola, M-IR02 Università e AFAM, M-IR03 Enti di ricerca e M-IR04 Cultura e MiC. Al 20 agosto 2026 esistono tutti i 13 capitoli di M-IR01 e i primi 8 di M-IR02; devono essere prodotti 29 capitoli, le appendici previste, le revisioni trasversali e gli artefatti finali di volume.

## Architettura del lavoro

1. Il CLI `npm run pipeline` governa ordine, ownership e gate; il run-state non viene mai modificato manualmente.
2. Ogni capitolo viene realizzato nel file reader-facing indicato dalla scheda pipeline, con frontmatter tracciabile e testo autosufficiente. La conoscenza deriva da source notes, topic pages, entity pages, matrice e piano del capitolo; le raw sources non entrano nel processo redazionale finale.
3. Ogni claim normativo, regolamentare o istituzionale con rischio di obsolescenza viene verificato su fonte primaria e, se necessario, consolidato nel wiki prima dell'uso nel capitolo.
4. Dopo le fasi capitolo, ciascun modulo passa revisione trasversale, correzioni, audit specialistico e text freeze. Solo allora diventano ammissibili i gate finali 21–24 di VOL-06.

## Criteri di qualità e pubblicabilità

- Ogni nucleo richiesto dalla matrice è classificato `completo`, oppure ha un rinvio preciso verso testo esistente e completo; `parziale`, `solo-nominato` e `mancante` sono bloccanti.
- I capitoli restano specialistici: nessuna duplicazione delle B-PA di VOL-01 e nessun rinvio generico.
- Ogni capitolo usa una progressione didattica, un caso operativo, verifiche, errore tipico e riferimenti leggibili; i contenuti interni non compaiono nel testo per il lettore.
- La revisione applica i 30 controlli, fact-check con fonti autorevoli, controllo di naturalezza, coerenza terminologica, sintassi, tipografia Markdown e ridondanze.
- Il report finale segue il template del Revisore Editoriale Totale e conserva errori, verifiche residue, limiti della revisione e decisione di pubblicabilità.

## Sequenza e confini

L'esecuzione è divisa in tre tranche dipendenti: (1) completamento e freeze M-IR02; (2) M-IR03; (3) M-IR04, seguito da preflight e revisione finale di VOL-06. Ogni tranche ha una verifica autonoma; una non promuove automaticamente la successiva.

## Dipendenze e rischi

La pipeline segnala Chromium assente per i gate visuali 20 e 22 e `.env.local` assente. Chromium sarà installato prima dei gate che lo richiedono; le variabili d'ambiente saranno richieste o configurate solo se il comando effettivo ne dimostrerà la necessità. Nessun dato normativo verrà dedotto da memoria o da fonti non consolidate.
