---
id: source-vol-09-project-management-esempi-2026-10-03
type: source
title: "PM² 3.1 e laboratorio originale WBS, Gantt e percorso critico"
status: consolidated
domain: project management pubblico
topics: ["project management", "WBS", "percorso critico"]
entities: ["Commissione europea"]
source_refs: []
book_refs: ["m-tr02-appalti-pnrr-fondi-ue"]
confidence: 0.98
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["correzioni-collana", "esempi-verificabili"]
source_type: official-guide-and-original-example
source_url: https://op.europa.eu/en/publication-detail/-/publication/97cc2f12-c648-11ee-95d9-01aa75ed71a1/language-en
source_date: 2023
authority_level: primary
---

# Fonte e lettura

Commissione europea, DG DIGIT, *The PM² Project Management Methodology Guide*, v3.1, 2023, DOI 10.2799/970188, ISBN 978-92-68-10314-2, licenza CC BY 4.0. PDF ufficiale acquisito via download-handler dell'Ufficio pubblicazioni: `wiki/raw/correzioni-collana-2026-10-02/pm2-guide-v31.pdf`, 148 pagine. Letti §2.1.3 p6 (PDF13), §6.4 pp46–47 (PDF53–54), appendice C §§C.5–C.13 pp102–103 (PDF109–110).

Output = prodotto/servizio; outcome = cambiamento conseguente; beneficio = miglioramento misurabile. Benefici e outcome possono manifestarsi dopo la chiusura del progetto. Work plan comprende scomposizione, stime e calendario. La guida ammette più convenzioni WBS, non solo deliverable: non dichiarare invalida qualunque organizzazione per fasi/uffici. Un semplice elenco di uffici senza lavoro/risultati non è comunque una scomposizione sufficiente. DBS identifica i prodotti, WBS il lavoro necessario; nel volume si adotta una WBS organizzata per deliverable, con pacchetti di lavoro sotto ciascuno.

CPM: cammino di durata massima dal principio alla fine, che determina la minima durata secondo vincoli e risorse assunte. Non è il cammino con più attività né la somma di tutti i tempi. Gantt visualizza il piano; baseline/change management mantengono tracciabilità.

# Esempio originale da applicare

Sportello digitale: output portale collaudato e personale formato; outcome adozione da utenti/uffici; beneficio obiettivo riduzione tempo medio pratica da20a12minuti su campione comparabile dopo3mesi, non giàdimostrato al collaudo.

WBS tre livelli: 1 servizio; 1.1 soluzione (A requisiti2giorni, B configurazione4d dopoA); 1.2 dati e verifica (C bonifica3d dopoA,D caricamento+test2d dopoB/C);1.3 adozione (E manuale+formazione1d dopoB,F accettazione+avvio1d dopoD/E). Si assume personale distinto per attività parallele, dipendenze fine-inizio, nessun ritardo aggiuntivo, calendario lunedì-venerdì, inizio6ottobre2026.

Passata avanti ES/EF su asse0: A0/2,B2/6,C2/5,D6/8,E6/7,F8/9. Passata indietro LS/LF: A0/2,B2/6,C3/6,D6/8,E7/8,F8/9. Margini A0,B0,C1,D0,E1,F0. Percorso critico A-B-D-F9giorni; alternativo A-C-D-F8,A-B-E-F8. Date A6–7ott,B8–13,C8–12,D14–15,E14,F16. Calendario è dato didattico, non deadline PNRR.

Se C dura4d, margine assorbito ma fine invariata; se C dura5d, finegiorno10 (19ott), percorsoA-C-D-F. Se Bslitta2d finegiorno11(20ott). Anticipare E rispetto alla fineD è consentito: formazione su ambiente stabile dopoB, distinta da accettazioneproduttivaF. Una specifica simulazione che imponga prima il verbaletest può invece richiedere D→E; dichiarare il vincolo, non farne regola universale.

[[topics/vol-09-appalti-pnrr-procurement]], [[books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters/13-project-management-pubblico]]. V09-32/33/34. Esempio, dataset e diagramma originali, non riproduzione grafica della guida.
