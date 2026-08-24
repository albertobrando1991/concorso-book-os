# VOL-10 — Censimento sicuro del lavoro staff

Controllo eseguito il 21 agosto 2026 senza integrazioni, checkout o sovrascritture. Branch locale: `codex/publish-volumes-01-03-05-10-11`; base `fedfb0f`; `origin/main` acquisito e non più avanti del ramo. Il ramo staff `origin/agent/sync-volumi-04-05-06-09-20260817` è avanzato a `349f632c` e contiene nuovo lavoro soprattutto su VOL-06: resta separato perché VOL-06 è escluso dall'incarico corrente.

| Volume | Modulo | File | Autore/branch se rilevabile | Stato contenuto | Stato fonti | Stato immagini | Possibile collisione | Azione proposta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VOL-01 | B-PA01/B-PA11 | volume base, delivery e PDF recuperato | ramo locale/base staff già integrata | da consolidare | da verificare | PDF esistente | nessun run-state | inizializzare e completare dopo VOL-10 |
| VOL-02 | M-FL01-04 | perimetro completo | main | utilizzabile | consolidato | verificato | nessuna | nessuna azione |
| VOL-03 | M-FC01-03 | M-FC01 capp. 11-15 e M-FC03 | ramo locale/base staff | da completare | presenti ma da auditare | da verificare | 40 step pendenti | completare dopo VOL-01 |
| VOL-04 | M-FC04 | candidato e report | main | utilizzabile | consolidato | verificato | solo step umano 24 | nessuna azione automatica |
| VOL-05 | M-FC05 | 15 capitoli, fonti e report storico | ramo locale/base staff | da consolidare | presenti | da verificare | nessun run-state | inizializzare e completare |
| VOL-06 | M-IR01-04 | nuovi capp. M-IR02 e M-IR03, planning e report | branch staff `349f632c` | in completamento staff | in aggiornamento | da verificare | alta se integrato ora | escluso: non toccare né integrare |
| VOL-07 | M-SA01-04 | candidato e report | main | utilizzabile | consolidato | verificato | solo step umano 24 | nessuna azione automatica |
| VOL-08 | M-TR01 | volume completo | main | utilizzabile | consolidato | verificato | nessuna | nessuna azione |
| VOL-09 | M-TR02 | volume completo | main e branch staff divergente | utilizzabile | consolidato | verificato | branch staff contiene versioni concorrenti | non integrare nel flusso VOL-10 |
| VOL-10 | M-TR03 | 13 capitoli, planning, fonti e report | ramo corrente | utilizzabile dopo audit | consolidato al 21-08-2026 | nessun asset reader-facing | nessuna collisione rilevata | proseguire pipeline corrente |
| VOL-11 | M-TR04 | candidato 225 pp. e report | ramo corrente | utilizzabile | consolidato al 21-08-2026 | verificato | branch staff contiene versione precedente concorrente | preservare candidato corrente; solo step umano 24 |
| VOL-12 | M-SP01-04 | candidato e report | main | utilizzabile | consolidato | verificato | solo step umano 24 | nessuna azione automatica |

## File locali e versioni concorrenti

- Modifiche e nuovi file di VOL-10 e VOL-11 appartengono al lavoro corrente.
- `wiki/log.md` e `wiki/memory/agent/` contengono memoria operativa condivisa e non vengono usati come sorgenti editoriali.
- I log `.dashboard-dev.*`, le tavole di contatto e le directory `tmp/pdfs/` sono diagnostici e devono restare fuori dai pacchetti di consegna.
- Il ramo staff remoto contiene versioni concorrenti di VOL-09 e VOL-11 e nuovo lavoro VOL-06; nessuna di queste è stata integrata in questo step.
- VOL-01 e VOL-05 non hanno ancora run-state; non sono considerati completi anche se possiedono file e PDF/report preesistenti.

## Elementi non presenti in `origin/main`

Il nuovo lavoro staff su VOL-06 rilevato nel ramo `origin/agent/sync-volumi-04-05-06-09-20260817` non risulta incorporato nel ramo corrente né in `origin/main`. Anche i candidati e le correzioni correnti di VOL-10 e VOL-11 non sono ancora su main perché l'utente non ha richiesto commit o push in questo incarico.
