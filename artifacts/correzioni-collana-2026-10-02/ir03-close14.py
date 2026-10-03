from pathlib import Path
import re,json,hashlib,shutil
B=Path('wiki/books/moduli/m-ir03-enti-ricerca');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-06');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
raw=Path('wiki/raw/correzioni-collana-2026-10-02/cnr-380-2-tec-usrg-2026.pdf')
if not raw.exists():shutil.copyfile(A/raw.name,raw)
p=Path('wiki/sources/fonti-ufficiali-m-ir03-enti-ricerca-2026-07-24.md');t=p.read_text(encoding='utf8').replace('[[https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32018R1046|Reg. UE 2018/1046]]','[[https://eur-lex.europa.eu/eli/reg/2024/2509/oj|Reg. UE, Euratom 2024/2509]]').replace('La lacuna del grant manager EPR autonomo resta aperta.','La funzione grant è documentata dal caso CNR 380.2 del 2026 qui sotto; non è presentata come profilo contrattuale nazionale autonomo.').replace('[[entities/consiglio-nazionale-ricerche]]','[[entities/ministero-universita-ricerca]]')
t+='''
## Bando EPR per supporto a progetti — acquisizione del 3 ottobre 2026

CNR, bando n. 380.2 TEC URSG (questa è la sigla nell’intestazione; ufficio USRG), firmato il 23 marzo 2026: https://www.urp.cnr.it/system/files?file=2026-03%2FBando-380.2-TEC-USRG_signed.pdf . Letti pagine PDF 1, 3–6 e 9–11 nei punti pertinenti; non dichiarata lettura integrale delle restanti pagine. Art. 1: un tecnologo di III livello a tempo determinato per collaborazione al Project Management Office presso l’Ufficio Supporto alla Ricerca e Grant. Art. 2, lettera g: organizzazione, monitoraggio, gestione finanziaria e rendicontazione di programmi regionali/nazionali/europei, con richiamo agli strumenti informatici. Art. 8: selezione per titoli e colloquio collegato alle attività/esperienze e conoscenze richieste. L’esempio chiude l’assenza di un riscontro di selezione EPR sulla funzione grant; non inventa un quarto profilo contrattuale e non trasferisce requisiti, punteggi o scadenze a tutti i bandi.
'''+f'\nRaw `{raw.as_posix()}`, SHA256 {hashlib.sha256(raw.read_bytes()).hexdigest()}.\n'
p.write_text(t,encoding='utf8')
# Read consolidated source before injecting its delimited factual example.
assert 'Art. 1: un tecnologo' in p.read_text(encoding='utf8')
p=next((B/'chapters').glob('11-*.md'));t=p.read_text(encoding='utf8');needle=re.search(r'^### N-IR03-11-01[^\n]*\n',t,re.M)
t=t[:needle.end()]+'''\n**Un bando reale sulla funzione di supporto.** Il CNR, bando n. 380.2 del marzo 2026 presso l'Ufficio Supporto alla Ricerca e Grant, ha selezionato un tecnologo di III livello a tempo determinato per collaborazione al Project Management Office. Le attività richiamate comprendono organizzazione, monitoraggio, gestione finanziaria e rendicontazione di programmi di finanziamento regionali, nazionali ed europei. La selezione per titoli e colloquio collega la prova alle esperienze e conoscenze della posizione. Il caso mostra perché «supporto grant» descriva una funzione che può essere assegnata a un profilo formale di tecnologo: non autorizza a dedurre che ogni ufficio progetti abbia lo stesso inquadramento o che tutti i concorsi richiedano gli stessi titoli.\n\n'''+t[needle.end():];p.write_text(t,encoding='utf8')
repls={'consultarei':'consulterei','presumererei':'presumerei','altriarticolazioni':'altre articolazioni','deposizioni e accordi':'depositi e accordi','Equivalere open science':'Equiparare open science','Nel corpus esaminato':'Nei bandi esaminati',"Si'":'Sì',"si'":'sì',"perche'":'perché',"Perche'":'Perché',"puo'":'può',"cosi'":'così',"qualita'":'qualità',"attivita'":'attività',"responsabilita'":'responsabilità',"contabilita'":'contabilità',"proprieta'":'proprietà',"pubblicita'":'pubblicità',"e'":'è'}
stats=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1)
 for a,b in repls.items():body=body.replace(a,b)
 if p.name.startswith('05-'):
  dup='In sede di prova, questa conclusione va sempre collegata alla verifica della fonte interna vigente e alla distinzione tra chi propone, chi controlla e chi decide.'
  first=body.find(dup);body=body[:first+len(dup)]+body[first+len(dup):].replace('\n'+dup,'')
  body=body.replace('### N-IR03-05-02 · Audit: evidenze, pianificazione, rilievi, azioni correttive e follow-up\n','''### N-IR03-05-02 · Audit: evidenze, pianificazione, rilievi, azioni correttive e follow-up

**Esempio di follow-up.** L'audit rileva che tre fascicoli su venti controllati non contengono la prova di consegna richiesta. L'azione correttiva assegna all'ufficio responsabile il recupero dei documenti e introduce un controllo prima della liquidazione. Nel riesame non basta trovare una nuova procedura firmata: si verificano i tre fascicoli e un nuovo insieme di pratiche, registrando l'effettivo uso del controllo. La chiusura del rilievo richiede evidenza dell'azione svolta e del suo esito; la sola promessa non chiude la non conformità. Il campione didattico non autorizza a stimare automaticamente la frequenza dell'errore in tutte le pratiche dell'ente.
''')
  body+='\nPer il quadro generale degli strumenti di acquisto: [[books/il-metodo-bando/chapters/contratti-pubblici-essenziali#16. Consip, Acquisti in Rete, MEPA, convenzioni e accordi quadro]]. Qui resta il delta proprio degli EPR.\n'
 if '## Riferimenti essenziali' not in body:
  body+='\n## Riferimenti essenziali\n\nD.Lgs. 213/2009, art. 1; D.Lgs. 218/2016, artt. 1–3 e 10; statuti CNR e ISTAT nei passaggi illustrati; CCNL Istruzione e ricerca 2022–2024; regolamento CNR di amministrazione, contabilità e finanza n. 201/2024. Per il progetto si applicano bando, accordo e regolamenti pertinenti.\n'
 if p.name.startswith('09-'):body=body.replace('nella versione vigente da verificare per il caso concreto.','articoli 45–49 e 65, nel perimetro illustrato; testo dell’articolo 65 verificato il 3 ottobre 2026.')
 sources=['sources/fonti-ufficiali-m-ir03-enti-ricerca-2026-07-24']
 if p.name.startswith(('05-',)):sources+=['sources/d-p-r-16-aprile-2013-n-62-codice-comportamento-dipendenti-pubblici','sources/vol-09-consip-strumenti-obblighi-2026-10-03']
 if p.name.startswith(('07-',)):sources+=['sources/integrita-pubblicazioni-ricerca-2026-08-22']
 if p.name.startswith(('09-',)):sources+=['sources/proprieta-intellettuale-trasferimento-2026-08-22']
 if p.name.startswith(('10-',)):sources+=['sources/open-science-fair-dati-2026-08-22']
 if p.name.startswith(('11-','12-')):sources+=['sources/grant-management-horizon-pnrr-2026-08-23']
 for field in ['source_refs','last_compiled_from']:
  m=re.search(rf'^{field}: (\[.*\])$',fm,re.M);existing=json.loads(m[1]) if m else []
  line=field+': '+json.dumps(list(dict.fromkeys(existing+sources)),ensure_ascii=False)
  fm=re.sub(rf'^{field}:.*$',lambda m:line,fm,flags=re.M) if m else fm+'\n'+line
 fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M);fm=re.sub(r'^draft_stage:.*$','draft_stage: corrections-applied',fm,flags=re.M);fm=re.sub(r'^review_required:.*$','review_required: true',fm,flags=re.M)
 t=fm+'\n---\n'+body;t='\n'.join(l.rstrip() for l in t.splitlines())+'\n';p.write_text(t,encoding='utf8')
 nuclei=[{'id':a.split(' · ')[0],'words':len(re.findall(r'\b[\w’]+\b',c.split('\n## ')[0]))} for a,c in re.findall(r'^### (N-[^\n]+)\n(.*?)(?=^### N-|\Z)',body,re.M|re.S)]
 q=len(re.findall(r'\*\*Quiz \d+',body));assert q==6 and len(nuclei)==5 and min(x['words'] for x in nuclei)>=600,p
 assert not re.search(r'\[\[(sources|topics|entities|planning|reviews|raw)/',body),p
 stats.append({'path':p.as_posix(),'words':len(re.findall(r'\b[\w’]+\b',body)),'nuclei':nuclei,'quiz':q})
(A/'M-IR03-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8')
e={1:'Quadro EPR e regolamento finanziario 2024/2509; decoder professionale.',2:'Ambiti 213/218, libertà e responsabilità; confronto documentato CNR/ISTAT.',3:'Profili e livelli I–III; declaratorie funzionali, grant come funzione.',4:'CNR 2025: budget/consuntivo, assestamenti; caso quadrato a 101.000.',5:'Conflitto/astensione, deroga acquisti delimitata; missione saldo 90, audit e follow-up.',6:'Mini-proposta 600 record, otto settimane, scelte e fatti distinti, rubrica.',7:'h-index 4 calcolato; limiti, contributi, integrità e correzioni.',8:'Piano tecnico 980/20 record e 60 secondi; verifica, validazione e regressione.',9:'CPI art. 65, tempi deposito, terzi; requisiti brevettuali, licenza/cessione.',10:'FAIR e protocolli; DMP compilato con oggetti, ruoli, formati, tempi e diritti.',11:'Bando CNR 380.2 reale; forme AGA, calcoli, DNSH obbligatorio e target 190/200.',12:'Quattro elaborati risolti: calendario, collaudo, rendiconto 25.000/3.000, modifica e rubrica.'}
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8').split('## Totali e blocker')[0];t=t.replace('`Completo` indica una progettazione con teoria, applicazione e verifica collocate in un capitolo; non equivale a testo scritto o pubblicabile.','La matrice è riconciliata con il testo effettivo al 3 ottobre 2026. La tabella delle evidenze collega i nuclei a teoria, casi e verifiche; non certifica ogni bando né il nuovo PDF.').replace('Alta: manca bando EPR grant autonomo; call mobili','Bando CNR 380.2/2026 acquisito; funzione grant distinta da profilo; call mobili')
t+='\n## Evidenze sui nuclei effettivi\n\n| Capitolo e nuclei | Teoria e applicazione osservate | Verifica |\n| --- | --- | --- |\n'+'\n'.join(f'| {n:02}, N-IR03-{n:02}-01–05 | {s} | Q:6 C:1 E:1 |' for n,s in e.items())
t+='''

Definizione, funzione, fonti, elementi, distinzioni, conseguenze, esempio, prova, errore e verifica sono distribuiti nei cinque nuclei e nei casi indicati. Il caso contabile distingue cassa/competenza e quadratura; le simulazioni scientifiche dichiarano assunzioni e limiti; la verifica copre le nuove nozioni. Fonti aggiuntive: [[sources/proprieta-intellettuale-trasferimento-2026-08-22]], [[sources/integrita-pubblicazioni-ricerca-2026-08-22]], [[sources/open-science-fair-dati-2026-08-22]], [[sources/grant-management-horizon-pnrr-2026-08-23]]. Resta da controllare il PDF rigenerato. Nessun regolamento locale non esaminato è certificato e nessuna specialità scientifica è sostituita dal metodo generale.
''';t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M).replace('status: planned_complete','status: coverage_reconciled');p.write_text(t,encoding='utf8')
p=Path('wiki/topics/m-ir03-enti-ricerca-fonti-e-profili.md');p.write_text('''---
id: topic-m-ir03-enti-ricerca-fonti-e-profili
type: topic
title: "Enti di ricerca: fonti, profili e casi"
status: consolidated
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
source_refs: ["sources/fonti-ufficiali-m-ir03-enti-ricerca-2026-07-24", "sources/proprieta-intellettuale-trasferimento-2026-08-22", "sources/grant-management-horizon-pnrr-2026-08-23"]
---

# Enti di ricerca: fonti, profili e casi

L'ordinamento distingue ambiti dei D.Lgs. 213/2009 e 218/2016; statuti CNR/ISTAT mostrano assetti differenti. CNR applica dal 2025 il nuovo regolamento contabile. I livelli di ricercatori/tecnologi non coincidono con la funzione trasversale di supporto grant, documentata dal bando CNR 380.2/2026. CPI art. 65 disciplina le invenzioni nel proprio perimetro; open science e contratti non cancellano titolarità e vincoli. DNSH è obbligatorio nelle misure RRF.

Fonti: [[sources/fonti-ufficiali-m-ir03-enti-ricerca-2026-07-24]], [[sources/proprieta-intellettuale-trasferimento-2026-08-22]], [[sources/integrita-pubblicazioni-ricerca-2026-08-22]], [[sources/open-science-fair-dati-2026-08-22]], [[sources/grant-management-horizon-pnrr-2026-08-23]], [[entities/ministero-universita-ricerca]].

Capitoli e matrice: [[books/moduli/m-ir03-enti-ricerca/index]], [[books/moduli/m-ir03-enti-ricerca/planning/02-matrice-copertura-didattica]]. I casi sono originali e numericamente chiusi; esempi locali distinti dalla disciplina generale. Riscontri esterni selettivi nelle parti indicate dalle note, non certificazione di tutti gli atti degli EPR.
''',encoding='utf8')
p=B/'index.md';t=p.read_text(encoding='utf8').replace('M-IR03 -','M-IR03 —').replace('text_frozen','corrections-applied').replace('module_status: text_freeze','module_status: editorial_revision').replace('revisione editoriale trasversale completata; in attesa di audit specialistico e text freeze.','correzioni del 3 ottobre applicate; audit specialistico e nuovo PDF da completare.');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
p=Path('wiki/books/volumi/vol-06-scuola-universita-ricerca-cultura/planning/01-indice-analitico.md');t=p.read_text(encoding='utf8');t=re.sub(r'(##[^\n]*M-IR03.*?)(?=\n## |\Z)',lambda m:m[0].replace('Appendici:', 'Apparati progettuali storici, ora sviluppati nei capitoli 04–12:'),t,flags=re.S);p.write_text(t,encoding='utf8')
p=R/'14-moduli-m-ir03-enti-ricerca.md';a=C/'archive/pre-correzioni-14-m-ir03.md'
if not a.exists():a.write_bytes(p.read_bytes())
rows=[('V06-17','01','Regolamento finanziario sostituito'),('V06-18','02–03','Autonomia, due statuti e livelli spiegati'),('V06-10 quota IR03','04/11','Contabilità e forme di finanziamento con calcoli'),('V06-19','05','Duplicati rimossi, conflitto/acquisti/missione integrati'),('V06-20','06','Scelta progettuale distinta da fatto inventato'),('V06-21','07–08','h-index e piano tecnico misurabile'),('V06-22','09','Art. 65 CPI, brevetto, licenza e cessione'),('V06-23','11','DNSH obbligatorio'),('V06-24','10/12','DMP e quattro prove con dati e soluzioni'),('V06-33/35/36 quota IR03','Tutti','Superficie, fonti, matrice e 72 quiz disciplinari')]
p.write_text('''# M-IR03 — Correzioni del 3 ottobre 2026

## 1. Sintesi editoriale

Applicati i rilievi del modulo e le quote IR03 dei rilievi trasversali. Nessuna pubblicabilità attestata prima dei nuovi PDF.

## 2. Checklist

Copertura teorica, autonomia, esattezza dei riferimenti, ipotesi dichiarate, calcoli, quiz, soluzioni, ruoli, stile e superficie. Impaginazione da controllare separatamente.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(f'| {i} | {pos} | Testo e didattica | Media | {s} | Delta applicato e raccordato | Corretto |' for i,pos,s in rows)+'''

## 4. Osservazioni per capitolo

'''+ '\n\n'.join(f'{n:02}: {s}' for n,s in e.items())+'''

## 5. Coerenza globale

Matrice sui 60 nuclei effettivi, sei quiz per capitolo; vecchi quiz archiviati fuori dal testo. Grant è funzione documentata da bando, non profilo contrattuale uniforme. Rinvio al capitolo base degli acquisti con heading esistente.

## 6. Fonti

Consolidati articoli selezionati dei D.Lgs. 213/218; due statuti, CCNL e declaratorie funzionali; regolamento CNR 201/2024 nei passaggi dichiarati; CPI 65 e requisiti UIBM; definizione Hirsch; AGA e RRF già consolidati. Bando CNR 380.2/2026 acquisito e usato soltanto per funzione/profilo e tipo di prova. Tentativi di acquisizione falliti esclusi dalle evidenze valide.

## 7. Suggerimenti facoltativi

Nessun ampliamento del dominio scientifico oltre il perimetro dei rilievi.

## 8. Priorità

Audit specialistico, text freeze e nuovo PDF.

## 9. Pubblicabilità

Non attestata. Testo corretto nel perimetro indicato; restano gli altri moduli e l'impaginato del volume.

## 10. Limiti

Lettura integrale baseline precedente, ora riesame dei delta e raccordi. Verifiche normative selettive e originali didattici esplicitamente ipotetici; nessuna certificazione di ogni regolamento, bando o manuale tecnico. Non effettuata una nuova lettura integrale dichiarata delle parti invariate.
''',encoding='utf8')
(A/'M-IR03-chapter-evidence.json').write_text(json.dumps(e,ensure_ascii=False,indent=2),encoding='utf8')
print('IR03 raccordi completati:',sum(x['words'] for x in stats),'parole, 72 quiz, 60 nuclei')
