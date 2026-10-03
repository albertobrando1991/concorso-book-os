---
id: source-vol-05-economia-esempi-verifica-2026-10-03
type: source
title: "VOL-05 — Esempi economici e calcoli verificati"
status: consolidated
domain: economia della regolazione
topics: ["economia industriale", "econometria", "contabilità regolatoria"]
entities: ["ARERA", "AGCOM", "Commissione europea"]
source_refs: ["sources/economia-industriale-econometria-contabilita-regolatoria-authority-2026-07-24.md"]
book_refs: ["m-fc05-authority-indipendenti", "vol-05-authority-regolazione"]
confidence: 0.97
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["vol-05", "correzioni", "esempi-didattici"]
source_type: official_methodological_sources_and_original_examples
source_date: 2026-10-03
authority_level: methodological
---

# Distinzioni e calcoli

Price cap: limite del prezzo o indice/paniere, distinto dal revenue cap sui ricavi riconosciuti. Gli esempi P0=100, inflazione 3%, X=1%, R0=1.000 e volumi 10→11 sono costruzioni didattiche, senza correttivi e senza pretesa di replicare uno specifico metodo ARERA.

RAB e WACC: base degli attivi riconosciuta per la regolazione e costo medio ponderato del capitale. Formula didattica post-imposte con capitale proprio 60%, debito 40%, rendimenti 8%/4%, imposta 25%: 6%. Tutti valori convenzionali, nessun WACC corrente dichiarato. La formula tariffaria semplificata evita doppia remunerazione/interessi e distingue convenzioni nominali/reali e fiscali. Il riferimento istituzionale di contesto è [ARERA TIROSS](https://www.arera.it/schede-tecniche/dettaglio/it/schedetecniche/23/163-23st), già nella nota madre; i parametri applicativi restano settoriali.

Per il controfattuale: [JRC, policy impact evaluation](https://knowledge4policy.ec.europa.eu/microeconomic-evaluation/policy-impact-evaluation-methods-data_en); [Commissione, guida alla valutazione controfattuale](https://ec.europa.eu/regional_policy/sources/policy/evaluations/helpdesk/052018/4.Practicioners-guide-CIB.pdf); [EU CAP Network, difference in differences](https://eu-cap-network.ec.europa.eu/training/evaluation-learning-portal/learning-portal-difference-differences-method_en). Verificate le descrizioni ufficiali del metodo e dell'ipotesi di andamenti paralleli; non dichiarata lettura integrale dei manuali. Dataset didattico: trattati 20→12, confronto 15→13; differenza delle differenze −6 punti percentuali, non −6% relativo. Non si dichiara identificazione causale dimostrata dal solo calcolo.

Modello lineare illustrativo con coefficiente 0,5 e SE 0,2; intervallo normale approssimativo 0,108–0,892. Non è una regressione stimata su dati reali. Elasticità puntuale di Q=200−2P a P=50 e Q=100 pari a −1. Riparto di costi comuni secondo ore 60/40: 180.000/120.000 su 300.000. HHI originario 3.000→3.800 verificato e mantenuto.

Tutti i calcoli riproducibili in `artifacts/correzioni-collana-2026-10-02/VOL-05-economia-calculations.json`; script `apply-vol05-economia.py`. Nessuna fonte empirica fittizia: i numeri sono dichiarati originali e didattici.

Collegamenti: [[topics/authority-rettifiche-2026]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/07-economia-industriale-regolazione-econometria-contabilita]].
