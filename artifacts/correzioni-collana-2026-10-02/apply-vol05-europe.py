from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti')
Path('wiki/sources/vol-05-reti-ue-verifica-2026-10-03.md').write_text('''---
id: source-vol-05-reti-ue-verifica-2026-10-03
type: source
title: "VOL-05 — Atti UE e organismi di cooperazione: verifica del 3 ottobre 2026"
status: consolidated
domain: diritto europeo della regolazione
topics: ["regolazione europea", "cooperazione", "reti delle autorità"]
entities: ["Commissione europea", "ECN", "BEREC", "ACER", "EDPB", "EBA", "ESMA", "EIOPA"]
source_refs: ["sources/regolazione-ue-multilivello-reti-authority-2026-07-24.md"]
book_refs: ["m-fc05-authority-indipendenti", "vol-05-authority-regolazione"]
confidence: 0.96
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["vol-05", "correzioni", "fonti-primarie"]
source_type: official_eu_legislation_and_institutional_pages
source_date: 2026-10-03
authority_level: primary_official
---

# Atti e organismi: riscontri puntuali

- TFUE artt. 288–291 letti nel testo ufficiale del Consiglio già acquisito: `wiki/raw/constitutional-law/04-eu-international/consilium-tue-tfue-carta-op-2012.epub`; estratto di lavoro `norme-vol05/tfue-epub.txt`. Riscontro istituzionale corrente nel [Parlamento europeo, fonti del diritto UE](https://www.europarl.europa.eu/factsheets/it/sheet/6/subsidiarity), paragrafi su gerarchia e tipologia degli atti. Decisioni vincolanti; delega sugli elementi non essenziali; esecuzione uniforme. Non si confondono RTS/ITS adottati con bozze delle autorità.
- [Commissione, ECN](https://competition-policy.ec.europa.eu/antitrust-and-cartels/european-competition-network_en): rete della Commissione e delle autorità nazionali, non organo sanzionatore ulteriore. Reg. 1/2003, cooperazione artt. 11–12; la pagina conferma casi, scambio probatorio e coordinamento.
- [Reg. 2018/1971, artt. 1–4](https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX%3A32018R1971): testo indicizzato ufficiale verificato su istituzione, personalità giuridica del BEREC Office e massima considerazione di orientamenti/pareri BEREC. Non dichiarata lettura integrale del regolamento; acquisizione diretta EUR-Lex respinta dal sito, registrata nel manifest.
- [ACER, REMIT investigations](https://acer.europa.eu/remit/remit-investigations): poteri investigativi transfrontalieri, informazioni, ispezioni e dichiarazioni; rapporto conclusivo e misure delle autorità nazionali. Reg. 2019/942 e REMIT 1227/2011 modificato da 2024/1106. Non confondere sanzione per violazione sostanziale e penalità per mancata cooperazione. Nessun richiamo a una data di avvio operativo delle indagini nel manuale.
- GDPR artt. 55–56, 65 e 68 letti integralmente dal PDF ufficiale Garante già acquisito, `wiki/raw/chapter-7-trasparenza-anticorruzione-privacy/garante-gdpr-regolamento-ue-2016-679.pdf`; estratto `norme-vol05/gdpr-local.txt`. EDPB organismo UE con personalità; decisioni vincolanti nei casi art. 65; esclusione sportello unico per art. 55(2).
- [EBA, compliance](https://www.eba.europa.eu/about-us/legal-and-policy-framework/compliance-eba-regulatory-products): art. 16 reg. 1093/2010 e obbligo di comunicare conformità/intenzione o motivi; due mesi dalla pubblicazione multilingue. [EIOPA, strumenti di convergenza](https://www.eiopa.europa.eu/browse/supervisory-convergence/supervisory-convergence-tools_en): art. 16 reg. 1094/2010. [ESMA, tabella di conformità MiCA](https://www.esma.europa.eu/sites/default/files/2025-07/ESMA35-24871704-2591_Compliance_table_on_MiCA_crypto-asset_transfer_Guidelines.pdf): art. 16 reg. 1095/2010. Queste pagine confermano natura e processo degli orientamenti; non si dichiara lettura integrale dei tre regolamenti istitutivi.
- Per RTS/ITS: [EBA, consultazione sui collegi](https://eba.europa.eu/sites/default/files/document_library/Publications/Consultations/2023/Consultation%20on%20RTS%20and%20ITS%20on%20supervisory%20colleges%20under%20CRD/1055870/CP%20with%20RTS-ITS%20on%20colleges.pdf) è un esempio del processo, non norma definitiva: i progetti vengono sottoposti alla Commissione; efficacia dell'atto adottato distinto dal progetto. Il capitolo non applica prescrizioni della consultazione.

Raw delle pagine ECN, EBA, EIOPA e ACER salvate in `wiki/raw/correzioni-vol05-2026-10-03/`; URL/hash e fallimenti distinti in `artifacts/correzioni-collana-2026-10-02/norme-vol05/eu-institutional-manifest.json`. Nessun file vuoto trattato come testo verificato.

Collegamenti: [[topics/authority-rettifiche-2026]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/03-regolazione-europea-multilivello-reti-autorita]].
''',encoding='utf8')
t=Path('wiki/topics/authority-rettifiche-2026.md')
if '## Fonti UE e organismi' not in t.read_text(encoding='utf8'):t.write_text(t.read_text(encoding='utf8')+'\n\n## Fonti UE e organismi\n\n[[sources/vol-05-reti-ue-verifica-2026-10-03]] distingue decisione vincolante, soft law e norme tecniche adottate; confronta ECN, BEREC, ACER, EDPB e autorità finanziarie senza attribuire alla rete poteri propri degli enti partecipanti.\n',encoding='utf8')
p=B/'chapters/03-regolazione-europea-multilivello-reti-autorita.md';s=p.read_text(encoding='utf8')
a=s.index('Le **decisioni**');b=s.index('\n\nLa regolazione multilivello',a)
s=s[:a]+'''La **decisione** è vincolante in tutti i suoi elementi; se individua destinatari, vincola soltanto questi. Raccomandazioni e pareri non sono vincolanti ai sensi dell'art. 288. Non si può quindi collocare una decisione nella stessa categoria di una raccomandazione soltanto perché entrambe provengono da un soggetto europeo.

Gli **atti delegati**, art. 290 TFUE, sono atti non legislativi generali con cui la Commissione integra o modifica elementi non essenziali dell'atto legislativo, entro la delega e i controlli fissati dal legislatore. Gli **atti di esecuzione**, art. 291, assicurano condizioni uniformi di applicazione: sono adottati di regola dalla Commissione, dal Consiglio nei casi specifici previsti. «Delegato» e «di esecuzione» indicano funzione e procedimento, non sinonimi di linea guida.

Nel settore finanziario, EBA, ESMA ed EIOPA elaborano progetti di norme tecniche: gli **RTS** diventano norme tecniche di regolamentazione mediante atti delegati della Commissione, gli **ITS** norme tecniche di attuazione mediante atti di esecuzione, secondo la fonte che conferisce il potere. Una bozza consultiva non è ancora diritto vincolante. Gli orientamenti dell'art. 16 dei regolamenti istitutivi seguono invece il meccanismo **comply or explain**: le autorità nazionali comunicano conformità o intenzione di conformarsi, oppure i motivi del mancato adeguamento. Per EBA il periodo ordinario di comunicazione è di due mesi dalla pubblicazione nelle lingue ufficiali. L'orientamento non diventa per questo un regolamento, ma non è neppure un documento da ignorare senza confronto.''' + s[b:]
a=s.index('Nel settore energetico, **ACER**');b=s.index('\n\n## N-MF05-03-03',a)
s=s[:a]+'''Nel settore energetico, **ACER** è un'agenzia dell'Unione che coordina i regolatori nazionali ed esercita anche poteri decisori e investigativi attribuiti dalla disciplina settoriale. Nel REMIT riformato può svolgere indagini transfrontaliere, acquisire informazioni e compiere ispezioni; l'autorità nazionale conserva il ruolo di accertamento della violazione sostanziale e di enforcement descritto più avanti. Ridurla a una sede di scambio di dati nasconderebbe la riforma del 2024.''' +s[b:]
s=s.replace('Nei casi transfrontalieri, il GDPR prevede il meccanismo dello sportello unico:',"Nei trattamenti transfrontalieri cui si applica l'art. 56 GDPR opera lo sportello unico:")
needle='![Figura 3.4'
pos=s.index(needle)
s=s[:pos]+'''Lo sportello unico non si estende ai trattamenti delle autorità pubbliche e degli organismi privati che agiscono nei casi dell'art. 55, paragrafo 2, GDPR: resta competente l'autorità dello Stato interessato. Un fornitore estero non trasferisce automaticamente il procedimento sulla pubblica amministrazione al regolatore del proprio Stato. Ruolo del fornitore e relativi trattamenti vanno qualificati separatamente.

### Organismo, base e limite del potere

| Soggetto e natura | Fonte essenziale | Potere e limite da ricordare |
| --- | --- | --- |
| ECN: rete fra Commissione e autorità nazionali della concorrenza | Reg. CE 1/2003, artt. 11–12 | Coordina casi e scambi informativi; non emette una sanzione a nome della rete |
| BEREC: organismo dei regolatori delle comunicazioni | Reg. UE 2018/1971, artt. 1–4 | Orientamenti, pareri e convergenza; autorità nazionali e Commissione ne tengono massima considerazione. Distinto dal BEREC Office, agenzia di supporto dotata di personalità giuridica |
| ACER: agenzia UE per la cooperazione dei regolatori dell'energia | Reg. UE 2019/942; REMIT 1227/2011 e riforma 2024/1106 | Anche decisioni nelle materie attribuite e indagini REMIT transfrontaliere; non assorbe ogni potere ARERA |
| EDPB: organismo UE con personalità giuridica | GDPR, artt. 65, 68 e 70 | Orientamenti e decisioni vincolanti nei casi di coerenza/controversia previsti; la decisione finale dell'autorità si conforma alla decisione art. 65 |
| EBA, ESMA, EIOPA: tre autorità europee di vigilanza con personalità giuridica | Reg. UE 1093, 1095 e 1094/2010, rispettivamente | Norme tecniche in progetto, orientamenti e poteri specifici; non costituiscono una sola rete né sostituiscono indistintamente i vigilanti nazionali |

**Esempio finanziario.** Un final report EBA contenente un progetto RTS non basta per imporre all'intermediario un requisito: si cerca l'atto adottato dalla Commissione, la data di applicazione e l'ambito. Per una guideline si controllano invece destinatari, decorrenza e posizione dell'autorità competente. Il controllo del tipo di atto precede il controllo del contenuto.

'''+s[pos:]
a=s.index("### Checklist per una nota d'ufficio")
s=s[:a]+'''## N-MF05-03-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Una decisione UE individua la società Alfa quale destinataria. È soltanto un consiglio perché non è un regolamento?

**Risposta corretta:** no. L'art. 288 rende la decisione vincolante in tutti i suoi elementi; se designa destinatari, vincola questi. L'assenza di portata generale non equivale ad assenza di obbligatorietà.

**Quesito 2.** Un testo EBA reca «draft regulatory technical standards». È già un regolamento delegato applicabile alla banca?

**Risposta corretta:** no. Si tratta di un progetto. Occorre verificare l'adozione da parte della Commissione e l'applicazione dell'atto finale. RTS, ITS e orientamenti seguono procedimenti ed effetti differenti.

**Quesito 3.** AGCM e Commissione scambiano elementi su un'intesa transfrontaliera. Chi sanziona: ECN o l'autorità competente?

**Risposta corretta:** il soggetto competente secondo il regolamento e il procedimento. ECN è la rete di cooperazione, non un ulteriore collegio che adotta una sanzione propria. Lo scambio deve rispettare base legale e limiti d'uso.

**Quesito 4.** ACER rileva una possibile manipolazione REMIT transfrontaliera. Può soltanto inoltrare un messaggio ad ARERA?

**Risposta corretta:** no. Nei presupposti della disciplina riformata ha poteri investigativi propri. Il rapporto investigativo non coincide con la sanzione nazionale per la violazione sostanziale. Non vanno confuse con questa le penalità per mancata cooperazione previste a livello europeo.

**Quesito 5.** Un dissenso rilevante fra autorità privacy può essere risolto da una decisione EDPB obbligatoria?

**Risposta corretta:** sì, nei casi dell'art. 65 GDPR. L'autorità capofila o quella competente adotta poi la decisione definitiva conforme. EDPB non produce soltanto pareri facoltativi e non sostituisce sempre il provvedimento nazionale.

**Quesito 6.** Un ente pubblico italiano utilizza un fornitore cloud stabilito in un altro Stato UE. Lo sportello unico si applica automaticamente al trattamento dell'ente?

**Risposta corretta:** no. L'art. 55, paragrafo 2, esclude l'art. 56 per i trattamenti indicati. Si distingue il ruolo del fornitore dalla responsabilità dell'ente e si individua la competenza per ciascun trattamento.

### Caso ragionato di chiusura

**Traccia.** Una nota d'ufficio conclude: «BEREC sanziona l'operatore italiano; il progetto RTS EBA vincola già tutte le banche; EDPB può solo consigliare; ACER non ha poteri istruttori». Correggi le quattro proposizioni senza aggiungere dati non presenti.

**Soluzione.** BEREC favorisce convergenza, ma la sanzione richiede il potere dell'autorità competente e la sua procedura; la rete non lo attribuisce. Il progetto RTS deve completare il processo di adozione e applicazione dell'atto della Commissione. EDPB adotta anche decisioni vincolanti nei casi dell'art. 65. ACER dispone dei poteri investigativi REMIT previsti per i casi transfrontalieri; occorre ancora verificare i presupposti del caso concreto. Per ciascun atto si annotano fonte, titolare, destinatari e rimedio; una sigla europea da sola non risolve il fascicolo.

**Autovalutazione:** quattro punti, uno per correzione accompagnata da potere e limite; nessun punto per sostituire semplicemente una sigla con un'altra.

**Riferimenti normativi e professionali.** TFUE, artt. 288–291; reg. CE 1/2003, artt. 11–12; reg. UE 2018/1971; reg. UE 2019/942; REMIT, reg. UE 1227/2011 come modificato da 2024/1106; GDPR, artt. 55–56, 65 e 68; regolamenti istitutivi EBA 1093/2010, EIOPA 1094/2010 ed ESMA 1095/2010. Pagine istituzionali: [ECN](https://competition-policy.ec.europa.eu/antitrust-and-cartels/european-competition-network_en), [indagini REMIT ACER](https://acer.europa.eu/remit/remit-investigations), [conformità agli orientamenti EBA](https://www.eba.europa.eu/about-us/legal-and-policy-framework/compliance-eba-regulatory-products). Verifica mirata del 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/vol-05-reti-ue-verifica-2026-10-03.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/vol-05-reti-ue-verifica-2026-10-03.md", "wiki/topics/authority-rettifiche-2026.md", ',1)
p.write_text(s,encoding='utf8')
f=Path('artifacts/correzioni-collana-2026-10-02/VOL-05-progress.json');d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=[1,2,3,4];d['findingsFullyApplied']+=['V05-07'];f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('Applied chapter 3: acts, comparative bodies, six questions and solved case.')
