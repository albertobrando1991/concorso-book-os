---
id: source-reti-sistemi-infrastrutture-fonti-tecniche
type: source
title: "Reti, sistemi operativi e infrastrutture — fonti tecniche primarie"
status: processed
domain: "informatica specialistica"
topics: ["reti", "protocolli", "sistemi operativi", "infrastrutture"]
entities: ["IETF", "RFC Editor", "Linux Kernel"]
source_refs: []
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.9
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: true
canonical: true
tags: ["source", "vol-08", "reti", "sistemi-operativi", "infrastrutture"]
source_type: technical_standards_and_official_documentation
source_url: "https://www.rfc-editor.org/"
source_date: 2026-07-29
authority_level: alta
---

# Reti, sistemi operativi e infrastrutture — fonti tecniche primarie

## Uso

Nota consolidata per il capitolo 5 di VOL-08. Integra la source note introduttiva con standard di rete e documentazione ufficiale sul kernel Linux. Sostiene indirizzamento, trasporto, servizi, memoria virtuale e file system; troubleshooting, ridondanza e disponibilità restano soggetti a review specialistica.

## Fonti primarie

- **RFC 8200 — Internet Protocol, Version 6 (IPv6) Specification**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc8200>. Specifica IPv6, intestazione di base ed extension header.
- **RFC 4632 — Classless Inter-domain Routing (CIDR)**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc4632>. Riferimento per prefissi e aggregazione degli indirizzi IPv4.
- **RFC 9293 — Transmission Control Protocol (TCP)**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc9293>. Specifica corrente di TCP.
- **RFC 768 — User Datagram Protocol**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc768>. Specifica essenziale di UDP.
- **RFC 2131 — Dynamic Host Configuration Protocol**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc2131>. Descrive l’assegnazione dei parametri di configurazione agli host.
- **RFC 1034 e RFC 1035 — Domain Names**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc1034> e <https://www.rfc-editor.org/rfc/rfc1035>. Architettura, concetti e implementazione del DNS.
- **RFC 9110 — HTTP Semantics**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc9110>. Semantica generale di HTTP.
- **Memory Management Documentation**, Linux Kernel documentation, consultata il 29 luglio 2026: <https://www.kernel.org/doc/html/latest/mm/index.html>.
- **Memory Management — Concepts overview**, Linux Kernel documentation, consultata il 29 luglio 2026: <https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html>. Documenta memoria virtuale, page table, page cache, memoria anonima, reclaim e swap.
- **Filesystems in the Linux kernel**, Linux Kernel documentation, consultata il 29 luglio 2026: <https://www.kernel.org/doc/html/latest/filesystems/index.html>. Raccoglie la documentazione VFS, pathname lookup, mount, inode e oggetti file.
- **The `/proc` Filesystem**, Linux Kernel documentation, consultata il 29 luglio 2026: <https://www.kernel.org/doc/html/latest/filesystems/proc.html>. Espone informazioni su processi, memoria e stato del sistema utili alla diagnosi.

## Decisioni editoriali

- Usare OSI come modello concettuale e TCP/IP come suite operativa, senza imporre una corrispondenza uno-a-uno.
- Distinguere indirizzo MAC, indirizzo IP, porta e nome DNS.
- Limitare il subnetting a prefissi e calcoli verificabili utili in prova.
- Spiegare TCP e UDP per proprietà e casi d’uso, evitando l’equazione semplicistica UDP = veloce e TCP = lento.
- Trattare processi, thread, memoria virtuale e file system a livello trasferibile fra sistemi.
- Presentare i comandi diagnostici solo come esempi; il metodo è sintomo → ipotesi → test → evidenza → azione → verifica.
- Distinguere ridondanza e backup; non attribuire disponibilità a un solo componente.

## Limiti e review

- Ethernet, VLAN, switching, RAID e metriche di disponibilità richiedono una fonte primaria o universitaria più granulare.
- I dettagli operativi cambiano fra Linux, Windows e apparati di rete.
- Gli esempi di subnetting, gli stati dei processi e i casi di troubleshooting devono essere verificati manualmente.
- I protocolli applicativi sono trattati per funzione; le specifiche complete restano fuori perimetro.

## Collegamenti

- [[sources/reti-web-protocolli-concorsi]]
- [[topics/reti-e-protocolli]]
- [[topics/sistemi-operativi-e-gestione-file]]
- [[books/moduli/m-tr01-ict-trasformazione-digitale/chapters/05-reti-sistemi-operativi-infrastrutture]]
