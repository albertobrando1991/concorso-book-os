from pathlib import Path
import json,math
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02')
calculations={'priceCap':100*(1+.03-.01),'revenueCap':1000*(1+.03-.01),'revenueCapUnitPriceAt11':1020/11,'priceCapRevenueAt11':102*11,'elasticityAt50':-2*50/100,'wacc':.6*.08+.4*.04*(1-.25),'allowedRevenue':200000+50000+1000000*.06,'allocationRegulated':300000*.6,'allocationOther':300000*.4,'did':(12-20)-(13-15),'ols95CI':[.5-1.96*.2,.5+1.96*.2],'hhiBefore':40**2+30**2+20**2+10**2,'hhiAfter':50**2+30**2+20**2}
assert calculations['priceCap']==102 and calculations['did']==-6 and math.isclose(calculations['wacc'],.06)
(O/'VOL-05-economia-calculations.json').write_text(json.dumps({'type':'invented didactic examples, not observed data','calculations':calculations},ensure_ascii=False,indent=2),encoding='utf8')
Path('wiki/sources/vol-05-economia-esempi-verifica-2026-10-03.md').write_text('''---
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
''',encoding='utf8')
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## Economia applicata\n\n[[sources/vol-05-economia-esempi-verifica-2026-10-03]] rende verificabili price cap, revenue cap, elasticità, regressione, controfattuale, RAB/WACC e allocazione. I parametri sono didattici, distinti da quelli regolatori vigenti.\n',encoding='utf8')
p=B/'chapters/07-economia-industriale-regolazione-econometria-contabilita.md';s=p.read_text(encoding='utf8')
a=s.index('Gli strumenti di regolazione incentivante');b=s.index('\n\nL’esempio ARERA',a) if '\n\nL’esempio ARERA' in s[a:] else s.index("\n\nL'esempio ARERA",a)
s=s[:a]+'''Il **price cap** limita il prezzo unitario o un indice/paniere di prezzi; il **revenue cap** limita i ricavi riconosciuti. Il volume venduto li distingue: con un tetto al prezzo, un aumento dei volumi può aumentare i ricavi; con un tetto ai ricavi, il prezzo medio deve essere ricalibrato o i ricavi riconciliati secondo la disciplina. I metodi reali possono prevedere conguagli, qualità e altri correttivi.

**Esempio didattico senza correttivi.** La formula del price cap è P1 = P0 × (1 + inflazione − X), dove X è il recupero di produttività. Con P0 = 100 euro, inflazione 3% e X = 1%, P1 = **102 euro**. Non si sottrae «1 euro» al tasso d'inflazione: entrambi sono percentuali della base.

Un revenue cap con R0 = 1.000 euro e gli stessi fattori dà R1 = **1.020 euro**. Se i volumi passano da 10 a 11 unità, il prezzo medio coerente con quel ricavo è 1.020 / 11 = **92,73 euro circa**. Con il price cap di 102 euro, invece, 11 unità producono 1.122 euro. Per questo «tetto di prezzo» e «tetto di ricavo» non sono sinonimi.

Il **benchmark** confronta costi o prestazioni con operatori omogenei: un'impresa di montagna non è confrontabile con una rete urbana senza considerare densità e condizioni del servizio. Gli obiettivi di qualità evitano che il recupero di efficienza premi soltanto tagli alla manutenzione. Formule e coefficienti effettivi dipendono dalla disciplina del settore: quelli qui usati servono a risolvere l'esercizio.''' +s[b:]
pos=s.index('## N-MF05-07-02')
s=s[:pos]+'''### Strutture di mercato: quattro confronti

| Struttura | Meccanismo essenziale | Domanda per il regolatore |
| --- | --- | --- |
| Concorrenza perfetta, modello limite | Molti operatori, prodotto omogeneo, ciascuno prende il prezzo come dato | Quali ipotesi del modello sono assenti nel mercato concreto? |
| Monopolio | Un solo fornitore; con potere di mercato può restringere la quantità rispetto all'esito competitivo | Esistono sostituti, ingresso credibile o potere degli acquirenti? |
| Oligopolio | Pochi operatori interdipendenti; ogni scelta dipende dalla risposta attesa degli altri | Il parallelismo deriva da vincoli comuni o da una condotta coordinata da provare? |
| Monopolio naturale | Un unico produttore può servire la domanda a costo complessivo inferiore a più produttori | Come conciliare accesso, efficienza, qualità e investimenti senza presumere la necessità di duplicare la rete? |

Con costo didattico C(Q) = 1.000 + 10Q, servire 100 unità con una sola impresa costa 2.000; due imprese che ne servono 50 ciascuna costano complessivamente 3.000. È un esempio di vantaggio della produzione unificata per quel volume. Non dimostra che ogni filiera del settore debba essere monopolistica: rete e vendita possono avere assetti differenti. Un costo fisso alto, da solo, non prova ogni presupposto della regolazione.

'''+s[pos:]
pos=s.index('## N-MF05-07-04')
s=s[:pos]+'''### Elasticità e regressione: un calcolo per volta

L'elasticità della domanda al prezzo è il rapporto fra variazioni percentuali; quella puntuale si scrive ε = (dQ/dP) × P/Q. Per Q = 200 − 2P, a P = 50 si ha Q = 100 ed ε = −2 × 50 / 100 = **−1**. Vicino al punto, +1% di prezzo corrisponde circa a −1% di quantità, a parità degli altri fattori. Il coefficiente −2 della retta misura unità per euro, non è direttamente un'elasticità. A prezzi diversi cambia il rapporto P/Q e quindi l'elasticità puntuale.

Per un modello lineare y = α + βx + u, y è la variabile da spiegare, x il regressore, u raccoglie fattori non osservati e disturbi. In un risultato **interamente didattico**, y è il tempo medio di attesa in minuti e x il carico in centinaia di richieste giornaliere; la stima è y = 2 + 0,5x. Un aumento di 100 richieste è associato a **0,5 minuti**, non a 0,5%, di attesa in più; con x = 10 la previsione è 7 minuti.

Se l'errore standard di β è 0,2, un intervallo al 95% con approssimazione normale è 0,5 ± 1,96 × 0,2, cioè **[0,108; 0,892]**. L'intervallo descrive l'incertezza della procedura sotto le ipotesi del modello; non attribuisce una probabilità del 95% al singolo parametro fisso. Né l'esclusione dello zero dimostra causalità o grande rilevanza pratica. Personale, complessità delle pratiche e stagionalità possono confondere la relazione: una variabile omessa correlata con x può distorcere β. Servono specificazione, controlli, qualità del campione e un disegno adeguato alla domanda.

### Controfattuale con una differenza delle differenze

Un programma sperimentale interessa il gruppo T; il gruppo C è un confronto non coinvolto. Sono percentuali di pratiche oltre lo standard, su popolazioni comparabili e con la stessa definizione:

| Gruppo | Prima | Dopo |
| --- | --- | --- |
| T: interessato dalla misura | 20% | 12% |
| C: confronto | 15% | 13% |

La variazione T è −8 punti percentuali; C migliora di −2 punti. La differenza delle differenze è (12 − 20) − (13 − 15) = **−6 punti percentuali**. Il controfattuale T, se avesse seguito l'andamento C, sarebbe 18%; la distanza da 12% è sei punti. Non sono −6% relativi e non sono automaticamente tutti gli otto punti prima/dopo.

Per leggerlo causalmente occorre che, senza intervento, i gruppi avrebbero seguito andamenti paralleli; vanno considerate composizione stabile, assenza di anticipazione, altri interventi e ricadute sul controllo. Serie precedenti aiutano a discutere l'ipotesi, senza dimostrarla definitivamente. Con i soli quattro numeri il risultato è un esercizio di calcolo, non una prova empirica conclusiva.

### RAB, WACC e costi comuni

La **RAB** è la base patrimoniale riconosciuta ai fini regolatori: dipende da investimenti ammissibili, ammortamenti, dismissioni e criteri della disciplina; non coincide necessariamente con capitale sociale o valore di borsa. Il **WACC** è il costo medio ponderato del capitale. In una formula didattica nominale dopo imposte: WACC = [E/(D+E)] × Ke + [D/(D+E)] × Kd × (1 − t). E e D indicano capitale proprio e debito secondo i pesi adottati; Ke e Kd i relativi costi; t l'aliquota convenzionale.

Con E = 60, D = 40, Ke = 8%, Kd = 4% e t = 25%, WACC = 0,6 × 8% + 0,4 × 4% × 0,75 = **6%**. È un esempio, non il tasso ARERA corrente. Non si combina un tasso nominale con flussi reali senza conversione né un tasso dopo imposte con una base fiscale incompatibile.

Per mostrare le componenti, si assuma una disciplina didattica coerente con questi valori: RAB 1.000.000 euro, costi operativi riconosciuti 200.000 e ammortamenti 50.000. Ricavo riconosciuto semplificato = 200.000 + 50.000 + 6% × 1.000.000 = **310.000 euro**. La remunerazione di 60.000 non è il ricavo totale; gli ammortamenti e gli interessi non si sommano una seconda volta se già considerati secondo il metodo. Con 10.000 unità il corrispettivo medio illustrativo è 31 euro, prima degli ulteriori elementi eventualmente previsti da un metodo reale.

**Allocazione verificabile.** Un centro di assistenza costa 300.000 euro e serve attività regolata R e commerciale C. Le ore documentate sono 6.000 per R e 4.000 per C: il driver attribuisce 60% a R, quindi 180.000, e 40% a C, quindi 120.000. I due importi si riconciliano al totale. Imputare tutti i 300.000 a R sovraccaricherebbe il settore regolato di 120.000, a beneficio di C. Prima del riparto si attribuiscono direttamente i costi identificabili; per quelli comuni si dimostra che le ore esprimano davvero l'uso del servizio e che il criterio sia consentito e stabile. Il caso non autorizza a recuperare in tariffa ogni costo contabilmente allocato.

'''+s[pos:]
a=s.index('### Laboratorio di qualificazione');s=s[:a]+'''### ▣ Verifica ragionata

**Quesito 1.** P0 = 100 euro, inflazione 3%, X = 1%. Qual è il price cap didattico e quanti ricavi consente a 11 unità?

**Risposta corretta:** prezzo 102 euro; ricavi 1.122. Un revenue cap di 1.020 euro darebbe invece prezzo medio 92,73 circa: il vincolo agisce su una variabile diversa.

**Quesito 2.** Nella domanda Q = 200 − 2P, con P = 50, l'elasticità è −2?

**Risposta corretta:** no. −2 è la pendenza in unità per euro. Q è 100 e l'elasticità puntuale è −2 × 50/100 = −1, rapporto privo di unità fra variazioni percentuali.

**Quesito 3.** β = 0,5 e SE = 0,2: che cosa dice l'intervallo normale approssimativo e che cosa non dimostra?

**Risposta corretta:** 0,5 ± 0,392, quindi [0,108; 0,892]. Esclude zero sotto le ipotesi del modello, ma non elimina variabili omesse, selezione del campione o altre ragioni per cui il coefficiente non sia causale.

**Quesito 4.** Nel caso T 20%→12% e C 15%→13%, qual è la differenza delle differenze?

**Risposta corretta:** −8 − (−2) = −6 punti percentuali. Interpretarla come effetto richiede, fra l'altro, andamenti paralleli in assenza di trattamento e assenza di fattori differenziali non considerati.

**Quesito 5.** Con RAB di un milione e WACC 6%, il ricavo complessivo riconosciuto è sempre 60.000 euro?

**Risposta corretta:** no. 60.000 è la componente di remunerazione nel modello. Nell'esempio si aggiungono costi operativi riconosciuti 200.000 e ammortamenti 50.000: totale 310.000, senza doppi conteggi.

**Quesito 6.** Costi comuni 300.000 e ore R/C 6.000/4.000. Quale riparto segue il driver e quale controllo resta?

**Risposta corretta:** R 180.000, C 120.000. Occorre verificare ore, causalità del driver, ammissibilità del costo e riconciliazione; il risultato aritmetico non autorizza da solo il recupero tariffario.

### Caso ragionato di chiusura

**Traccia.** Il regolatore riceve questa nota: «Il prezzo massimo sale da 100 a 102, quindi anche i ricavi restano 1.020 qualunque sia il volume. Il gruppo trattato migliora di otto punti, tutti causati dalla misura. I costi comuni di 300.000 vanno tutti sulla rete regolata perché il gruppo è proprietario della rete». Usa i dati del capitolo per correggerla.

**Soluzione.** A 11 unità e prezzo 102 i ricavi sono 1.122: 1.020 sarebbe un diverso tetto ai ricavi. Il confronto disponibile suggerisce una differenza delle differenze di −6 punti, condizionata alle ipotesi: non prova da solo un effetto causale di otto punti. Il driver documentato 60/40 attribuisce 180.000 alla rete regolata e 120.000 all'altra attività; la proprietà non sostituisce il criterio di uso e i requisiti regolatori. La proposta deve esporre separatamente calcolo, ipotesi e conclusione consentita.

**Autovalutazione:** un punto per ciascuno dei tre risultati corretti e un punto per aver dichiarato i limiti del confronto causale e dell'ammissibilità tariffaria.

**Riferimenti metodologici e professionali.** Commissione europea, comunicazione sul mercato rilevante C/2024/1645; [JRC, metodi di valutazione microeconomica](https://knowledge4policy.ec.europa.eu/microeconomic-evaluation/policy-impact-evaluation-methods-data_en); ARERA, TIROSS 2024–2031 e disciplina settoriale dei conti separati; AGCOM, contabilità regolatoria delle reti fisse e mobili. Tutti i parametri e dataset numerici del capitolo sono didattici: i coefficienti effettivi richiedono il metodo settoriale applicabile. Calcoli verificati il 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/vol-05-economia-esempi-verifica-2026-10-03.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/vol-05-economia-esempi-verifica-2026-10-03.md", "wiki/topics/authority-rettifiche-2026.md", ',1)
p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,8));d['chaptersReadThisCycle']=list(range(1,8));d['findingsFullyApplied']+=['V05-12','V05-13'];f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][6]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('Applied chapter 7; all arithmetic assertions and calculation artifact produced.')
