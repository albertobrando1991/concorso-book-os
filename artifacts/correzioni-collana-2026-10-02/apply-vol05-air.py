from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti')
source=Path('wiki/sources/vol-05-air-verifica-2026-10-03.md')
source.write_text('''---
id: source-vol-05-air-verifica-2026-10-03
type: source
title: "VOL-05 — AIR ARERA e caso quantitativo: verifica del 3 ottobre 2026"
status: consolidated
domain: regolazione amministrativa
topics: ["consultazione", "air", "vir"]
entities: ["ARERA"]
source_refs: ["sources/ciclo-regolatorio-consultazione-air-vir-authority-2026-07-24.md", "sources/air-vir-qualita-regolazione-dpcm-169-2017.md"]
book_refs: ["m-fc05-authority-indipendenti", "vol-05-authority-regolazione"]
confidence: 0.97
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["vol-05", "correzioni", "fonti-primarie"]
source_type: official_resolution
source_date: 2025-06-18
source_url: https://www.arera.it/fileadmin/allegati/docs/25/255-25.pdf
authority_level: primary_official
---

# AIR: verifica mirata

La deliberazione ARERA **18 giugno 2025, 255/2025/A** adotta il regolamento AIR (Allegato A e annessi 1–2), efficace dalla pubblicazione, e abroga GOP 46/08. La motivazione, pp. 5–9, conferma selezione caso per caso degli atti rilevanti, proporzionalità, discrezionalità e metodologia adeguata a dati, effetti e risorse. Non stabilisce un obbligo generale di AIR per ogni atto né il primato necessario dell'analisi costi-benefici. Distingue monitoraggio e successiva selezione dei provvedimenti per VIR.

Riscontro: PDF ufficiale salvato immutabilmente in `wiki/raw/correzioni-vol05-2026-10-03/arera-air-255-2025.pdf`; testo in `artifacts/correzioni-collana-2026-10-02/norme-vol05/arera-air-255-2025.txt`, manifest documenti con URL e hash. Letti titolo, dispositivo e motivazione pertinente pp. 5–9; questa verifica non dichiara lettura degli allegati separati. Il DPCM 169/2017 resta rinviato alla source consolidata specifica: art. 1 esclude le autorità indipendenti dall'ambito soggettivo.

Il caso numerico del capitolo è interamente didattico: 10.000 contratti, 2.000 errori iniziali, alternative A e B, valore convenzionale di 30 euro per errore evitato. Non sono dati ARERA o una stima empirica. Benefici incrementali rispetto all'opzione zero; rimborsi e indennizzi non aggiunti automaticamente al beneficio sociale perché possono essere trasferimenti. Orizzonte di un anno, tutti i costi inclusi convenzionalmente nel periodo, nessun tasso di sconto necessario. Sensibilità B a 1.000 errori residui e differenziale B/A verificati aritmeticamente.

Collegamenti: [[topics/authority-rettifiche-2026]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/04-ciclo-regolatorio-consultazione-air-vir]].
''',encoding='utf8')
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## AIR e confronto quantitativo\n\n[[sources/vol-05-air-verifica-2026-10-03]] consolida data e natura della disciplina ARERA 255/2025/A. Il capitolo 4 integra una mini-AIR con ipotesi, costi, benefici incrementali e sensibilità: il calcolo sostiene, ma non sostituisce, la decisione motivata.\n',encoding='utf8')
p=B/'chapters/04-ciclo-regolatorio-consultazione-air-vir.md';s=p.read_text(encoding='utf8')
s=s.replace("l'Autorità ha inoltre aggiornato nel 2025 la propria disciplina AIR dopo un processo di consultazione.","l'Autorità ha adottato il regolamento AIR con deliberazione **18 giugno 2025, 255/2025/A**, dopo consultazione, abrogando la precedente guida GOP 46/08. L'analisi riguarda gli atti individuati dall'Autorità secondo rilevanza, discrezionalità e proporzionalità; metodo quantitativo, qualitativo o misto dipendono dal caso, dai dati e dalle risorse.")
a=s.index('### Laboratorio di qualificazione');s=s[:a]+'''### Mini-AIR compilata: contratti comprensibili

**Dati esclusivamente didattici.** In un anno vengono sottoscritti 10.000 contratti; un'indagine campionaria stima 2.000 errori di comprensione. Si assume, da validare in consultazione, un costo sociale medio di 30 euro per errore, espresso in tempo perso e risorse impiegate. Non si sommano automaticamente indennizzi o rimborsi: il trasferimento di denaro fra soggetti non equivale di per sé a un ulteriore costo sociale. L'obiettivo è ridurre gli errori mantenendo accessibile il servizio agli utenti vulnerabili.

L'opzione zero conserva le condizioni attuali. A introduce una scheda sintetica; B aggiunge una verifica assistita della comprensione. I costi sono incrementali annui complessivi, inclusi adeguamento, personale e monitoraggio per il periodo considerato; nessun costo viene nascosto in un esercizio successivo. Il valore di 30 euro e gli effetti attesi sono ipotesi del caso, non risultati accertati.

| Opzione | Errori residui / evitati rispetto a zero | Costi, benefici e saldo annui |
| --- | --- | --- |
| Zero: disciplina attuale | 2.000 / 0 | Costi incrementali 0; benefici incrementali 0; saldo 0 euro |
| A: scheda sintetica | 1.400 / 600 | Costo 12.000; beneficio 600 × 30 = 18.000; saldo +6.000 euro |
| B: scheda e verifica assistita | 600 / 1.400 | Costo 35.000; beneficio 1.400 × 30 = 42.000; saldo +7.000 euro |

B ha il saldo monetario maggiore nello scenario centrale, ma supera A di appena 1.000 euro. La maggiore riduzione degli errori costa 23.000 euro e produce 800 errori evitati in più: 28,75 euro per errore aggiuntivo evitato. Occorre quindi sostenere con dati l'ipotesi di un beneficio di 30 euro; il margine è piccolo. Se B lascia 1.000 errori anziché 600, evita 1.000 errori, produce 30.000 euro di beneficio e un saldo di **−5.000 euro**: A diventerebbe preferibile sul solo criterio monetario.

**Consultazione mirata.** Chiedere agli operatori tempi e costi di assistenza separati per canale; alle associazioni dei consumatori evidenze sugli errori e sulle barriere per utenti fragili. Specificare campione, periodo, definizione di errore e trattamento dei dati. La numerosità dei contributi favorevoli non sostituisce la qualità delle evidenze.

**Scelta provvisoria e verifica.** B è candidata soltanto se l'effetto atteso regge alle verifiche e non esclude gli utenti fragili. In caso contrario si può scegliere A, motivando efficacia e oneri. Registrare prima dell'avvio il tasso di errore, con campioni confrontabili, costi effettivi e differenze fra gruppi. Dopo dodici mesi, una VIR confronterà risultati, costi ed effetti inattesi con le alternative. Un semplice confronto prima/dopo non prova causalità: possono incidere campagne informative o cambiamenti nella clientela. Un progetto pilota con gruppo comparabile rafforza la valutazione.

## N-MF05-04-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Il DPCM 169/2017 obbliga direttamente ogni autorità indipendente a seguire la procedura AIR governativa?

**Risposta corretta:** no. Il suo ambito soggettivo esclude le autorità indipendenti. Per ARERA si consulta la disciplina dell'ente, inclusa la deliberazione 255/2025/A; la somiglianza metodologica non estende la competenza di una fonte.

**Quesito 2.** Nell'esempio, qual è il beneficio incrementale di A e quale il suo saldo netto?

**Risposta corretta:** A evita 600 errori; 600 × 30 = 18.000 euro di beneficio. Sottraendo 12.000 euro di costo, il saldo è +6.000. Usare 1.400 × 30 monetizzerebbe gli errori residui, non quelli evitati.

**Quesito 3.** Se B lascia 1.000 errori, quale opzione ha il maggiore saldo monetario fra zero, A e B?

**Risposta corretta:** A, con +6.000 euro. B vale (2.000 − 1.000) × 30 − 35.000 = −5.000 euro; zero vale zero. Il risultato dipende dalle ipotesi e non chiude la valutazione sugli effetti non monetizzati.

**Quesito 4.** Ottanta contributi contrari e venti favorevoli impediscono di adottare B?

**Risposta corretta:** no. La consultazione raccoglie evidenze e argomenti; non decide a maggioranza. L'autorità deve affrontare costi documentati, alternative e barriere segnalate, motivando secondo la propria disciplina.

**Quesito 5.** Un rapporto mensile registra errori e reclami: è già una VIR completa?

**Risposta corretta:** no. È monitoraggio. La VIR valuta efficacia, efficienza, utilità ed effetti inattesi, anche confrontando risultati con obiettivi e alternative. Una serie di conteggi costituisce la base della valutazione, non la sua conclusione.

**Quesito 6.** La disciplina ARERA del 2025 rende sempre obbligatoria l'analisi costi-benefici monetaria?

**Risposta corretta:** no. La scelta metodologica deve essere proporzionata e adeguata al caso. Se mancano dati attendibili, si espongono limiti e criteri qualitativi, senza inventare valori per completare una tabella.

### Caso ragionato di chiusura

**Traccia.** Un collega propone B perché «42.000 è maggiore di 18.000» e sostiene che dopo un anno basterà contare i reclami per dimostrare il successo. Correggi il ragionamento con due calcoli e due verifiche.

**Soluzione.** Confrontare i saldi: B 42.000 − 35.000 = 7.000; A 18.000 − 12.000 = 6.000 euro. Il vantaggio di B è soltanto 1.000 euro ed è sensibile all'effetto stimato: con 1.000 errori residui il saldo B diventa −5.000. Verificare sia i costi e l'efficacia dichiarati sia accessibilità e distribuzione degli effetti. Il numero di reclami può cambiare anche perché gli utenti conoscono meglio il canale: occorrono tasso di errore misurato in modo confrontabile, costi effettivi e analisi di fattori esterni. Non si confonde correlazione temporale con effetto causale.

**Autovalutazione:** un punto per saldi corretti, sensibilità, effetti distributivi e limite causale; quattro punti su quattro richiedono tutti i passaggi, non solo l'opzione scelta.

**Riferimenti normativi e professionali.** DPCM 15 settembre 2017, n. 169, art. 1; ARERA, [deliberazione 18 giugno 2025, 255/2025/A](https://www.arera.it/fileadmin/allegati/docs/25/255-25.pdf), regolamento AIR e motivazione sulla selezione degli atti e sulle metodologie. Verifica mirata del 3 ottobre 2026. Tutti i dati della mini-AIR sono convenzionali e didattici.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/vol-05-air-verifica-2026-10-03.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/vol-05-air-verifica-2026-10-03.md", "wiki/topics/authority-rettifiche-2026.md", ',1)
p.write_text(s,encoding='utf8')
assert 600*30-12000==6000 and 1400*30-35000==7000 and 1000*30-35000==-5000 and 23000/800==28.75
f=Path('artifacts/correzioni-collana-2026-10-02/VOL-05-progress.json');d=json.loads(f.read_text(encoding='utf8'));d['chaptersReadThisCycle']=[1,2,3,4,5];d['chaptersApplied']=[1,2,4];d['findingsFullyApplied']+=['V05-08'];d['findingsPartiallyApplied']['V05-02']='Capitoli 1, 2 e 4: sei quesiti e un caso specifici ciascuno';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=Path('artifacts/correzioni-collana-2026-10-02/VOL-05-reading-checkpoint.json');d=json.loads(f.read_text(encoding='utf8'));d['files'][4]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('Applied chapter 4 AIR; calculations verified; source/topic and checkpoints updated.')
