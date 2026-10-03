---
id: source-architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche
type: source
title: "Architettura, sistemi, rappresentazione e prestazioni — fonti tecniche primarie"
status: processed
domain: "informatica specialistica"
topics: ["architettura elaboratori", "rappresentazione dati", "sistemi operativi", "prestazioni"]
entities: ["RISC-V International", "IEEE", "Linux Kernel", "Unicode Consortium", "SPEC"]
source_refs: []
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.88
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: true
canonical: true
tags: ["source", "vol-08", "architettura", "sistemi-operativi", "prestazioni"]
source_type: official_technical_standards_and_documentation
source_url: "https://docs.riscv.org/reference/home/index.html"
source_date: 2026-07-29
authority_level: alta
---

# Architettura, sistemi, rappresentazione e prestazioni — fonti tecniche primarie

## Uso

Nota consolidata per il capitolo 2 di VOL-08. Sostiene il livello concettuale su istruzioni e architettura, rappresentazione numerica e testuale, interrupt, gestione della memoria e metriche di prestazione. Non sostituisce un manuale universitario completo né autorizza dettagli dipendenti da una singola implementazione.

## Fonti ufficiali consolidate

### RISC-V International

- **RISC-V Ratified Specifications Library**, consultata il 29 luglio 2026: <https://docs.riscv.org/reference/home/index.html>
- **The RISC-V Instruction Set Manual, Volume I — Unprivileged Architecture**, consultato il 29 luglio 2026: <https://docs.riscv.org/reference/isa/unpriv/unpriv-index.html>

La libreria raccoglie le specifiche ratificate e distingue architettura non privilegiata, architettura privilegiata, modalità di esecuzione e controllo del sistema. È usata per sostenere la distinzione fra istruzioni, interfaccia visibile al software e dettagli di microarchitettura. Il capitolo mantiene intenzionalmente un modello didattico generale e non presenta RISC-V come unica architettura possibile.

### IEEE

- **IEEE 754-2019 — Standard for Floating-Point Arithmetic**, consultato il 29 luglio 2026: <https://standards.ieee.org/ieee/754/6210/>

Lo standard definisce formati e metodi per l’aritmetica in virgola mobile binaria e decimale, oltre alle condizioni eccezionali e alla loro gestione. Nel capitolo è richiamato soltanto per il principio che una rappresentazione finita comporta intervallo, precisione e arrotondamento; non vengono attribuiti allo standard dettagli non verificati.

### Unicode Consortium

- **The Unicode Standard**, consultato il 29 luglio 2026: <https://www.unicode.org/standard/standard.html>
- **Unicode Character Encoding Model, UTR #17**, consultato il 29 luglio 2026: <https://www.unicode.org/reports/tr17/>

Le fonti distinguono carattere, valore numerico e forma di codifica. Sostengono l’affermazione che una sequenza di bit acquista significato mediante regole condivise e che lo scambio di testo richiede interpretazioni compatibili.

### Linux Kernel

- **Core API Documentation**, consultata il 29 luglio 2026: <https://docs.kernel.org/core-api/index.html>
- **Linux generic IRQ handling**, consultata il 29 luglio 2026: <https://docs.kernel.org/core-api/genericirq.html>
- **Memory Management Documentation**, consultata il 29 luglio 2026: <https://docs.kernel.org/mm/index.html>

La documentazione ufficiale del kernel descrive astrazioni per interrupt, memoria, concorrenza e gestione hardware. È usata come riscontro tecnico per il ruolo del sistema operativo e degli interrupt. Il capitolo astrae dai dettagli specifici delle API Linux per conservare trasferibilità concettuale.

### Standard Performance Evaluation Corporation

- **SPEC CPU 2026 Result File Fields**, consultato il 29 luglio 2026: <https://www.spec.org/cpu2026/Docs/result-fields.html>

La documentazione distingue le metriche orientate alla velocità da quelle orientate al throughput e definisce quest’ultimo come lavoro per unità di tempo. Sostiene la regola didattica secondo cui una valutazione di prestazione deve dichiarare metrica e carico.

## Claim sostenuti

- un’architettura di istruzioni definisce un’interfaccia osservabile senza coincidere con tutti i dettagli della microarchitettura;
- la rappresentazione digitale dipende da formati e codifiche condivisi;
- l’aritmetica in virgola mobile opera con formati finiti e regole di arrotondamento;
- interrupt e gestione della memoria richiedono meccanismi e astrazioni del sistema operativo;
- velocità di una singola esecuzione e throughput sono metriche differenti;
- nessuna singola metrica descrive ogni carico o ogni comportamento del sistema.

## Limiti e review

- La sequenza prelievo-decodifica-esecuzione è una semplificazione didattica generale: validarla nella revisione specialistica senza attribuirla integralmente a una specifica ISA.
- Gerarchia di memoria, cache, buffering e colli di bottiglia richiedono revisione di uno specialista di architettura, perché le implementazioni concrete variano.
- Non usare i risultati SPEC per confronti commerciali nel manuale senza applicare le regole d’uso e senza definire ambiente, carico e configurazione.
- Verificare periodicamente versione e stabilità dei collegamenti ufficiali.

## Collegamenti

- [[topics/hardware-e-architettura-pc]]
- [[topics/informatica]]
- [[topics/sistemi-operativi-e-gestione-file]]
- [[books/moduli/m-tr01-ict-trasformazione-digitale/chapters/02-informatica-specialistica-oltre-vol-01]]
