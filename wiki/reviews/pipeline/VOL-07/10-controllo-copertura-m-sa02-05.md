---
id: vol-07-step-10-copertura-m-sa02-cap-05
type: review
title: "VOL-07 step 10 - Controllo copertura M-SA02 capitolo 05"
status: complete
domain: "concorsi pubblici italiani"
source_refs: ["sources/sicurezza-cure-responsabilita-consenso-leggi-24-219", "sources/sicurezza-terapia-triage-assistenza-infermieristica-ministero", "sources/deterioramento-clinico-news2-sepsi-regioni", "sources/arresto-cardiaco-bls-iss-snlg-2026", "sources/als-adulto-erc-irc-2025", "sources/puerperio-neonato-supporto-vitale-oms-irc-iss", "sources/emergenze-ostetriche-eclampsia-sepsi-tromboembolia-itoss", "sources/emergenze-ostetriche-distocia-spalla-prolasso-funicolo-protocolli-italiani"]
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-08-01T23:50:00+02:00
created_at: 2026-07-31T20:00:00+02:00
review_required: false
automatic_audit_required: true
canonical: true
tags: ["pipeline", "vol-07", "step-10", "m-sa02", "chapter-05", "coverage", "format-v2"]
issue_type: coverage
severity: none
affected_pages: ["chapter-05"]
---

# Controllo di copertura — M-SA02, capitolo 05

Target: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/05-valutazione-clinica-triage-urgenza-emergenza.md`.

Matrice: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`.

## Sintesi misurabile

Il capitolo in formato 2 conta 6.634 parole e sviluppa sette nuclei stabili. I nuclei contano rispettivamente 752, 854, 669, 764, 613, 618 e 659 parole: tutti superano la soglia minima. Sono presenti un blocco `▣ Verifica`, sette quiz commentati e tre casi ragionati.

Il gate `didactic-density` non rileva blocker. Il gate `coverage` non rileva blocker sulle sette righe assegnate al capitolo.

## Delta per nucleo

| Nucleo | Stato prima | Intervento | Stato dopo | Evidenza |
| --- | --- | --- | --- | --- |
| `N-SA02-05-01` | riga aggregata legacy | sviluppati valutazione, priorità e rivalutazione | completo | H2 omonimo; caso 1; checklist |
| `N-SA02-05-02` | riga aggregata legacy | sviluppati deterioramento, NEWS2 e sepsi con dato operativo versionato | completo | H2 omonimo; `DO-SA02-05-NEWS2-ER-2024`; quiz 1 |
| `N-SA02-05-03` | riga aggregata legacy | sviluppati finalità, processo, priorità e rivalutazione del triage | completo | H2 omonimo; quiz 2 |
| `N-SA02-05-04` | riga aggregata legacy | sviluppati équipe, comunicazione, sicurezza e fattori umani | completo | H2 omonimo; quiz 4 |
| `N-SA02-05-05` | riga aggregata legacy | distinti BLS, ALS e continuità post-evento | completo | H2 omonimo; quiz 3 e 5 |
| `N-SA02-05-06` | riga aggregata legacy | sviluppati preparazione e supporto vitale neonatale | completo | H2 omonimo; quiz 6 |
| `N-SA02-05-07` | riga aggregata legacy | sviluppati allarmi ostetrici e risposta multidisciplinare | completo | H2 omonimo; caso 2; quiz 7 |

## Checklist dimensionale

La matrice contiene per ciascun Nucleo ID evidenze puntuali per:

- definizione;
- funzione;
- inquadramento;
- elementi;
- distinzioni;
- conseguenze;
- esempio o caso;
- uso nella prova;
- errore tipico;
- verifica;
- tracciabilità.

Non risultano dimensioni applicabili vuote o negative. Casi, quiz e checklist sono conteggiati come applicazione e verifica, mai come sostituti della teoria.

## Dati operativi

Il box NEWS2 dichiara ID, fonte ufficiale, ambito, versione, data di ricontrollo e area `clinico-assistenziale` dell'audit automatico. Il parser riconosce il box e lo inserisce nel pacchetto obbligatorio dello step 15 senza assegnarlo a una persona.

## Esito

Copertura e sufficienza didattica sono complete e verificabili a macchina. Non vi sono lacune da rinviare: lo step 15 eseguirà l'audit specialistico automatico e lo step 24 resterà l'unica conferma umana, esclusivamente conclusiva.
