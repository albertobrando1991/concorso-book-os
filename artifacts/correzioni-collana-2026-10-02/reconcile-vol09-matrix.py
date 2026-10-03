from pathlib import Path
import re,json,shutil
B=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue');A=Path(__file__).parent
titles={
1:['Profili, perimetro e lettura del bando','Ciclo contrattuale e specialista appalti','Procurement, PNRR e project management','Confini di materia e caso integrato','Classificazione del bando e allenamento'],
2:['Governance e separazione delle funzioni','Nomina del RUP e responsabili di fase','Qualificazione e matrice RACI','Competenze mancanti e scelta organizzativa','Verifica dei ruoli e costruzione della RACI'],
3:['Fabbisogno, dati e nota istruttoria','Programmazione e scelta dei lotti','Valore stimato, opzioni e strategia','Confronto delle opzioni e priorità','KPI, decisione e nota di fabbisogno'],
4:['Decisione di contrarre e documenti','Requisiti, esclusioni, RTI e avvalimento','Criteri, soccorso e specifiche tecniche','Proporzionalità: correggere il caso','Controllo del fascicolo e matrice requisiti'],
5:['Soglie europee e percorsi nazionali','Procedure, rotazione e casi di confine','Motivazione e controlli dei requisiti','Istruttoria e scelta nel caso concreto','Errori, verifiche e riepilogo operativo'],
6:['Funzioni del ciclo digitale','PAD, banche dati e pubblicità','Qualità del dato e continuità operativa','Gestione degli errori e verifiche','Ricostruire il flusso del fascicolo'],
7:['Obblighi, categorie e deroghe','Convenzioni, accordi quadro e MePA','Negoziazioni, SDA e gare in ASP','Scelta dello strumento nel caso concreto','Esercizi e verifica degli strumenti'],
8:['Avvio della fase esecutiva','Documenti e controlli della prestazione','Subappalto, modifiche e sospensioni','Prezzi, pagamenti e chiusura','Decisioni e rimedi nel caso concreto','Allenamento sui controlli esecutivi'],
9:['Qualificazione del problema e accesso','Precontenzioso e parere ANAC','Rimedi esecutivi, ricorso e divieti di stipula','Caso di aggiudicazione contestata','Timeline e scelta del rimedio'],
10:['Architettura del Piano e responsabilità','Risultati, indicatori e identificativi','ReGiS, dati e validazione','Controlli, ritardi e chiusura 2026','Report di avanzamento e allenamento'],
11:['Fasi della spesa e identificativi','Tracciabilità e condizioni di pagamento','Fascicolo, conflitti e controlli antifrode','Ammissibilità, duplicazioni e rettifiche','Riconciliazione e verifiche conclusive'],
12:['DNSH: obiettivi e regimi','CAM: obblighi minimi e criteri premianti','Verifica ambientale e caso notebook','Fascicolo ambientale e non conformità','Caso arredi e allenamento conclusivo'],
13:['Charter, output e benefici','Pianificazione, dipendenze e rischi','Modifiche, report e chiusura','Decisioni sul progetto in ritardo','WBS e calendario: soluzione completa','Laboratorio di verifica del progetto'],
14:['Lettura dei fatti e metodo di risposta','Simulazioni di programmazione e affidamento','Simulazioni di esecuzione, rimedi e PNRR','Recupero del ritardo e decisioni','Autovalutazione, diario e piano di studio','Kit cartaceo per atti e aggiornamenti']}
sources={1:'vol-09-bandi-specialistici-verificati-2026-10-03',2:'vol-09-governance-contratti-verifica-2026-10-03',3:'vol-09-programmazione-sottosoglia-verifica-2026-10-03',4:'vol-09-gara-requisiti-verifica-2026-10-03',5:'vol-09-programmazione-sottosoglia-verifica-2026-10-03',6:'vol-09-ciclo-digitale-verifica-2026-10-03',7:'vol-09-consip-strumenti-obblighi-2026-10-03',8:'vol-09-esecuzione-verifica-2026-10-03',9:'vol-09-accesso-rimedi-verifica-2026-10-03',10:'vol-09-pnrr-architettura-chiusura-regis-2026-10-03',11:'vol-09-tracciabilita-antifrode-spesa-2026-10-03',12:'vol-09-dnsh-cam-casi-verificati-2026-10-03',13:'vol-09-project-management-esempi-2026-10-03',14:'vol-09-laboratorio-soluzioni-verificate-2026-10-03'}
theory={1:'profili editoriali e incarico RUP; ciclo; output/outcome; confini delle famiglie',2:'nomina, requisiti e responsabilità; art.15 e I.2; art.62–63 e II.4; DEC; RACI',3:'fabbisogno e programmazione triennale; CUI; opzioni e lotti; KPI',4:'art.17; artt.94–101,108; requisiti, rimedi e motivazione; qualità/prezzo',5:'artt.48–52; soglie2026; interesse transfrontaliero; deroghe cumulative; controlli',6:'PAD/PCP/BDNCP/FVOE; certificazione; CIG per lotto; pubblicità UE e nazionale; trasparenza',7:'obblighi soggettivi e merceologici; DPCM2026; AQart59 e SDAart32; MePA e ASP',8:'artt.60,116,119–126,215; subappalto e varianti; prezzi e anticipazione; collaudo/CCT',9:'artt.18,35–36,210–213,220; accesso e segreti; standstill e CPA120',10:'RRF e PNRR; missioni e CID; milestone/target; ReGiS; chiusura2026',11:'L136/2010; CUP e fatture; art22RRF e art61reg2024/2509; titolare effettivo; spesa',12:'art17reg2020/852; Regimi1/2; scheda3DNSH; art57; DM254/2022arredi',13:'PM²3.1; output/outcome; WBS; dipendenze e margini; risk/issue/change; report',14:'applicazione delle regole dei capitoli1–13; nessuna norma introdotta solo nella soluzione'}
case={1:'Caso ragionato',2:'Caso ragionato: servizio digitale e competenza mancante',3:'Caso ragionato: servizio ricorrente e investimento PNRR',4:'Caso ragionato: servizio digitale e requisito sproporzionato',5:'Caso ragionato',6:'Caso svolto: la gara del Comune Alfa nel ciclo digitale',7:'Caso ragionato: materiale informatico, assistenza e servizio tecnico',8:'Caso ragionato',9:'Soluzione guidata',10:'Caso ragionato: milestone a rischio',11:'Calcolo risolto della quota rendicontabile',12:'Caso DNSH: venti notebook nuovi',13:'Soluzione completa: sportello digitale in nove giorni',14:'Simulazione 1 - Dal fabbisogno alla programmazione'}
output={1:'decoder e classificazione del bando',2:'matrice RACI e scelta del soggetto qualificato',3:'nota fabbisogno e valore stimato',4:'decisione e matrice requisiti-prove',5:'proposta motivata di affidamento',6:'flusso dati e nota di rettifica',7:'scelta motivata dello strumento',8:'verbale, calcolo penale e revisione',9:'timeline e nota sul rimedio',10:'status report e scheda avanzamento',11:'prospetto di spesa e riconciliazione',12:'clausola e matrice requisito-prova',13:'WBS, Gantt e richiesta decisionale',14:'elaborati delle dieci simulazioni e schede compilate'}
matrix=B/'planning/02-matrice-copertura-didattica.md';backup=A/'before-text/VOL-09';backup.mkdir(parents=True,exist_ok=True)
for p in [matrix,B/'index.md']:
 if not (backup/p.name).exists():shutil.copy2(p,backup/p.name)
rows=[];chapters=[]
for p in sorted((B/'chapters').glob('*.md')):
 n=int(p.name[:2]);t=p.read_text(encoding='utf8')
 t=re.sub(r'\b(M-[A-Z]{2})\s+(\d{2})\b',r'\1\2',t)
 for i,title in enumerate(titles[n],1):t=re.sub(rf'^## N-TR02-{n:02}-{i:02} · .+$',f'## N-TR02-{n:02}-{i:02} · {title}',t,flags=re.M)
 if n==13:t=t.replace('▣ Verifica N-TR02-13-02 -','▣ Verifica 1 -').replace('▣ Verifica N-TR02-13-04 -','▣ Verifica 2 -')
 p.write_text(t,encoding='utf8')
 assert (Path('wiki/sources')/(sources[n]+'.md')).exists(),sources[n]
 assert case[n] in t,(n,case[n])
 body=t.split('---',2)[2];matches=list(re.finditer(r'^## (N-TR02-\d{2}-\d{2}) · (.+)$',body,re.M))
 # Counts describe the shared apparatus of the chapter, not independent copies per nucleus.
 q=len(re.findall('Risposta corretta\s*:',body,re.I));c=len(re.findall(r'Caso (?:ragionato|guidato)\b',body,re.I));e=len(re.findall(r'^#{2,4} (?:Mini-esercizio|Esercizio:|Simulazione \d)',body,re.M))
 assert q>=6 and c>=1
 chTitle=re.search(r'^# (.+)$',body,re.M)[1];chapters.append({'number':f'{n:02}','file':p.name,'title':chTitle,'nuclei':len(matches),'qce':{'quizzes':q,'cases':c,'exercises':e}})
 for i,m in enumerate(matches):
  section=body[m.end():matches[i+1].start() if i+1<len(matches) else len(body)]
  headings=re.findall(r'^#{3,4} (.+)$',section,re.M)
  # Store real text for review, never manufacture an evidence quotation.
  paragraphs=[x.strip() for x in section.split('\n\n') if len(x.strip())>100 and not x.lstrip().startswith(('#','|','!['))]
  quote=paragraphs[0] if paragraphs else section.strip()[:500]
  rows.append({'id':m[1],'title':m[2],'chapter':n,'file':p.name,'sections':headings,'evidenceQuote':quote,'source':sources[n],'q':q,'c':c,'e':e,'case':case[n]})
def cell(s):return re.sub(r'\s+',' ',s.replace('|','/').replace('`','')).strip()
front='''---
id: matrix-m-tr02-appalti-pnrr-fondi-ue-copertura-didattica
type: coverage_matrix
title: "Matrice di copertura effettiva — M-TR02"
status: reviewed_text
updated_at: 2026-10-03
review_required: true
canonical: true
book_refs: ["m-tr02-appalti-pnrr-fondi-ue"]
---

# Matrice di copertura effettiva — M-TR02

La matrice del 29 luglio descriveva intenzioni progettuali e citava titoli non più esistenti. È archiviata in artifacts/correzioni-collana-2026-10-02/before-text/VOL-09. Questa versione mappa 73 nuclei realmente presenti in 14 capitoli, dopo le correzioni dell'audit integrale.

`completo` indica la copertura testuale del perimetro, non il via libera alla pubblicazione. Restano PDF corrente, controlli di produzione e approvazione finale. Le source note contengono URL, raw, disposizioni lette e limiti del riscontro; gli esempi sono originali.

**Conteggi Q/C/E:** apparato condiviso dell'intero capitolo, richiamato da più nuclei. Non sommare le righe per stimare il numero di esercizi del libro; i totali univoci sono nel manifest. Il caso e l'output possono integrare più nuclei, mentre teoria e collocazione identificano la sezione specifica. La checklist dimensionale è qualitativa: i laboratori applicano definizioni e regole già insegnate nel capitolo o nei capitoli richiamati, senza ripeterle come nuova teoria.

| Nucleo ID | Famiglia/profilo | Materia | Concetto/sotto-concetti | Frequenza/peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa | Destinazione rinvio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''
for r in rows:
 n=r['chapter'];dest=f"[[books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters/{Path(r['file']).stem}#{r['id'].lower()}]]"
 sections='; '.join(r['sections'][:6]) or r['title']
 vals=[r['id'],'M-TR02 / appalti, procurement, PNRR, PM',chapters[n-1]['title'],r['title'],'Da ponderare sul bando; campione qualitativo',f"[[sources/{r['source']}]]",f'cap. {n:02}; {dest}',sections,f"cap. {n:02} § {r['case']}",output[n],f"Q:{r['q']} C:{r['c']} E:{r['e']} — apparato condiviso cap. {n:02}; verifiche commentate e caso",'completo',f"3 ottobre 2026: {theory[n]}",'—']
 front+='| '+' | '.join(cell(v) for v in vals)+' |\n'
front+='''
## Checklist dimensionale e rintracciabilità

Le citazioni di riscontro sono nel manifest, copiate dal testo attuale; non costituiscono attestazioni di verità normativa autonome. Le dimensioni richiamano le sezioni della riga principale e, per applicazione/verifica, l'apparato condiviso dichiarato.

| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Errore tipico | Verifica | Fonti |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''
for r in rows:
 n=r['chapter'];applied=n==14 or 'Allenamento' in r['title'] or 'allenamento' in r['title'] or 'Laboratorio' in r['title']
 vals=[r['id'],('N/A: applicazione delle nozioni dei cap.1–13' if n==14 else '✓ '+r['title']), '✓ '+output[n], '✓ '+theory[n], '✓ sezioni analitiche della riga', '✓ regola/caso e limiti nel testo', '✓ esiti e commenti delle verifiche', '✓ '+r['case'], '✓ Errori tipici e commenti nel capitolo',f"✓ apparato cap. {n:02}, conteggi condivisi",'✓ '+r['source']]
 front+='| '+' | '.join(cell(v) for v in vals)+' |\n'
front+='\n## Confini e produzione\n\nIl B-PA resta nel VOL-01, le discipline di ente nei volumi di famiglia. Le ex appendici A–E sono sostituite da strumenti reali nei capitoli e dalla tavola del kit cartaceo del capitolo14; nessuna unità inesistente viene promessa. Il campione bandi aggiuntivo documenta appalti specialistici e strumenti digitali, senza inferenze statistiche nazionali. La matrice va riaperta se cambia il testo dopo il freeze.\n'
matrix.write_text(front,encoding='utf8')
(B/'planning/10-manifest-nuclei-format-2.json').write_text(json.dumps({'volume':'VOL-09','module':'M-TR02','updatedAt':'2026-10-03','status':'text-reviewed-pdf-pending','countingPolicy':'Q/C/E shared per chapter; do not sum nucleus rows','chapters':chapters,'nuclei':rows},ensure_ascii=False,indent=2),encoding='utf8')
index=B/'index.md';s=index.read_text(encoding='utf8');s=re.sub(r'^status:.*$','status: editorial_review',s,flags=re.M);s=re.sub(r'^module_status:.*$','module_status: editorial_review',s,flags=re.M);s=re.sub(r'^draft_stage:.*$','draft_stage: editorial-review',s,flags=re.M);s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M)
s=s[:s.index('## Capitoli di lavoro')]+'''## Indice dei capitoli

'''+''.join(f"- [[books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters/{Path(c['file']).stem}|Capitolo {c['number']} — {c['title']}]]\n" for c in chapters)
s=s.replace('M-TR02 - Appalti','M-TR02 — Appalti').replace('- Stato: indice e matrice pronti; fonti ufficiali e redazione dei capitoli da consolidare.','- Stato: correzioni testuali applicate; audit e PDF corrente da completare.')
s+='\n## Piano editoriale staff\n\n- [[books/moduli/m-tr02-appalti-pnrr-fondi-ue/planning/01-indice-analitico-vol-09]]\n- [[books/moduli/m-tr02-appalti-pnrr-fondi-ue/planning/02-matrice-copertura-didattica]]\n\n## Mappa analitica dei nuclei\n\n'
for r in rows:s+=f"- {r['id']} — [[books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters/{Path(r['file']).stem}#{r['id'].lower()}|{r['title']}]]\n"
index.write_text(s,encoding='utf8')
print({'chapters':len(chapters),'nuclei':len(rows),'quizSharedUnique':sum(c['qce']['quizzes'] for c in chapters)})
