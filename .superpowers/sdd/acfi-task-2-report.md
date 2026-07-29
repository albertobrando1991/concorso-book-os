# ACFI Task 2 — report

## Stato

DONE_WITH_REVIEW_NOTES

## Baseline e preservazione del diff

Prima dell'intervento il capitolo 5 risultava gia modificato nel worktree:

- stato: M;
- diff rispetto a HEAD: 280 inserimenti, 25 rimozioni;
- SHA-256 del file di lavoro: 65DC0766B3AF0A85F7762F95E27AF062621D4FBA3E278C397DE60FD9BD9ED675;
- struttura iniziale: blocco ACFI nominale di due paragrafi alle righe 170-175, dentro una revisione editoriale piu ampia.

L'intervento e' stato delimitato al frontmatter pertinente, al blocco “Profili ACFI e fiscalita internazionale”, ai riferimenti consolidati e alle note di review. Le revisioni preesistenti delle altre sezioni sono state conservate. Non e' stato eseguito alcun reset, checkout o commit.

## Sezioni implementate

Il blocco ACFI e' ora autonomo e articolato in sezioni di livello 3:

1. fonti e metodo operativo;
2. residenza di persone, societa ed enti;
3. stabile organizzazione materiale e personale;
4. convenzioni e doppia imposizione;
5. transfer pricing e libera concorrenza;
6. operazioni infragruppo, Masterfile, Documentazione Nazionale e comparabilita;
7. rischio internazionale e Tax Control Framework;
8. caso completo ACFI;
9. risposta da commissario, trappole, mini-esercizio risolto, quiz e checklist.

Sono stati inseriti raccordi precisi ai capitoli 4, 6 e 11 senza duplicarne la trattazione generale. Non e' stata creata una sezione 5C e non e' stata modificata la matrice di copertura.

## Fonti usate

Fonte editoriale principale:

- [[sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18]]

Contesto consolidato gia presente nel capitolo:

- [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
- [[sources/adempimento-collaborativo-compliance-fiscale-m-fc02]]
- [[sources/accertamento-contraddittorio-compliance-aggiornamento-2026-07-17]]
- [[topics/accertamento-compliance-fiscale]]
- capitoli 4, 6 e 11 del modulo M-FC02.

Non sono stati aperti o letti file in wiki/raw.

## Frontmatter

Aggiornati topics, entities, source_refs, updated_at e last_compiled_from. Conservati status, confidence, review_required e canonical. Aggiunto companion_to: il-metodo-bando. La fonte ACFI compare anche nei riferimenti consolidati.

## Correzioni S1/S2/Q1

- Residenza: esplicitate funzione e conseguenza prudente della distinzione residente/non residente, con raccordo necessario alla convenzione.
- Stabile organizzazione: esplicitate potesta impositiva dello Stato della fonte e attribuzione del solo reddito pertinente; completata la forma personale con il ruolo principale che conduce abitualmente alla conclusione senza modifiche sostanziali.
- Inserite verifiche risolte specifiche per residenza e stabile organizzazione.
- I rinvii ai capitoli 4, 6 e 11 puntano ora agli heading reali verificati: “Le fonti: una gerarchia da usare, non da recitare”, “Il ciclo dell'adempimento fiscale” e “15. Contabilita e controllo fiscale”.

## Controlli eseguiti

- presenza e ordine delle sezioni;
- assenza di sezione 5C;
- assenza di riferimenti raw nel capitolo;
- assenza di soglie, aliquote, scadenze, elenchi di Stati o requisiti mobili;
- raccordi ai capitoli 4, 6 e 11;
- controllo frontmatter e riferimenti;
- ricerca di mojibake e sequenze spurie;
- git diff --check;
- confronto diff/stat e hash finale;
- verifica che il capitolo resti revised_draft e review_required.

Esito definitivo del diff del capitolo rispetto a HEAD: 351 inserimenti e 25 rimozioni. SHA-256 definitivo: 803E39A7E7E54E75F8682C26D539F9CBB552BA9157D606E9E7C3BDCD2C234754.

Il delta autorizzato di Task 2 si innesta sulla baseline gia modificata: la baseline era 280 inserimenti e 25 rimozioni rispetto a HEAD; il file definitivo e' 351 inserimenti e 25 rimozioni. La differenza numerica e' quindi di 71 inserimenti nel diff aggregato rispetto a HEAD, senza cancellazioni aggiuntive rispetto alla baseline. Questa misura descrive il delta Git aggregato e non attribuisce a Task 2 le 280 inserzioni preesistenti.

## Self-review

Copertura sostanziale: completa nel perimetro selettivo del brief. Ogni nucleo contiene definizione/funzione, elementi o distinzione, conseguenza, esempio, errore e verifica, con maggiore concisione nei nuclei documentali e TCF. Il caso segue fatti, qualificazione, fonti, rischio/istruttoria e output. Il testo evita automatismi probatori e distingue norma interna, convenzione e riferimenti OCSE.

Qualita editoriale: il blocco e leggibile come unita autonoma, mantiene lessico coerente con il capitolo e offre output concorsuali. Non sono stati arbitrariamente elevati stato o confidence.

## Rilievi residui

- Prima della pubblicazione restano necessarie review normativa ed editoriale indipendenti, gia richiamate nel capitolo.
- La singola convenzione, i protocolli e le modifiche applicabili vanno verificati sul caso concreto.
- Git segnala la normale futura normalizzazione CRLF/LF del file; git diff --check non rileva errori di whitespace.