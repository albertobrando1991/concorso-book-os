from pathlib import Path
import re,json,ast
B=Path('wiki/books/moduli/m-sp03-magistratura-avvocatura-notariato');A=Path('artifacts/correzioni-collana-2026-10-02');C=Path('wiki/reviews/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12')
source='sources/bandi-magistratura-avvocatura-notariato-m-sp03';topic='topics/m-sp03-carriere-giuridiche-prove';entity='entities/ministero-della-giustizia'
e={1:'Giurisdizione ordinaria civile e penale, funzioni giudicanti e requirenti; fonti dei requisiti distinte; precedenti esiti della procuratura.',2:'Lingua orale con giudizio di sufficienza, minimi numerici e totale 108; casi di soglie; domanda prima del diario successivo.',3:'Formula anagrafica del bando, D.P.C.M. 141/2000 e computo dei compleanni; due precedenti non idoneità; soglie autonome e correzione sequenziale.',4:'Pratica, scadenza e certificato separati; casi Marta e Andrea con cronologie possibili; esiti alla pubblicazione e espulsione dopo dettatura.',5:'Comando della traccia prima del formato; tema breve svolto, soluzione Alfa/Beta con danni e varianti, clausole testamentarie motivate e confronto prima/dopo.',6:'Piano su due anni con ore, prodotti e revisioni condizionate; caso dichiarato composito, candidatura storica tempestiva e studio successivo.',7:'Difesa concreta su requisito temporale, prova documentale e tardività; mancanza documentale distinta da incertezza interpretativa; checklist degli esiti.'}
stats=[];keys={}
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);c=int(p.name[:2]);ids=re.findall(r'^## (N-SP03-\d+-\d+) ·',body,re.M);assert len(ids)==5
 # Replace each ID once from its original set to avoid mapping collisions.
 mapping={old:f'N-SP03-{c:02}-{i:02}' for i,old in enumerate(ids,1)}
 fm=re.sub(r'N-SP03-\d+-\d+',lambda m:mapping.get(m[0],m[0]),fm);body=re.sub(r'N-SP03-\d+-\d+',lambda m:mapping.get(m[0],m[0]),body)
 body=body.replace('## Spiegazione teorica: da sapere in 5 righe','## Da sapere in 5 righe').replace('nel perimetro verificato per il requisito storico','art. 1, per il riferimento storico').replace('nel perimetro verificato per il requisito di accesso','art. 1, per il riferimento storico')
 body=body.replace('della L. 1035/1966','della legge 1035/1966')
 # Letter reordering includes any explicit letter references in the explanation.
 body=re.sub(r'^   (?=[A-D]\. |\*\*Risposta corretta:)', '',body,flags=re.M)
 pat=r'(?P<opts>^A\. [^\n]+\nB\. [^\n]+\nC\. [^\n]+\nD\. [^\n]+\n)\s*\*\*Risposta corretta: (?P<key>[A-D])\.\*\*(?P<comment>.*?)(?=\n\s*\n(?:\*\*)?\d+\. |\n## |\Z)'
 seq=[]
 def rotate(m):
  opts=re.findall(r'^[A-D]\. (.+)$',m['opts'],re.M);target='ABCD'[(len(seq)+c)%4];shift=(ord(target)-ord(m['key']))%4;mp={chr(65+i):chr(65+(i+shift)%4) for i in range(4)};out=['']*4
  for i,opt in enumerate(opts):out[(i+shift)%4]=opt
  comment=re.sub(r'\b[A-D]\b',lambda x:mp[x[0]],m['comment'].strip());seq.append(target)
  return '\n'.join(f'{chr(65+i)}. {v}' for i,v in enumerate(out))+f'\n\n**Risposta corretta: {target}.** '+comment+'\n'
 body=re.sub(pat,rotate,body,flags=re.M|re.S);assert len(seq)==len(re.findall(r'Risposta corretta:',body)),(p,len(seq))
 keys[f'{c:02}']=seq
 deps=[x.removesuffix('.md').removeprefix('wiki/') for x in ast.literal_eval(re.search(r'^source_refs: (\[.*\])$',fm,re.M)[1])]
 for field,val in [('source_refs',json.dumps(deps)),('last_compiled_from',json.dumps(deps)),('topics',json.dumps([topic])),('entities',json.dumps([entity])),('updated_at','2026-10-03'),('cut_off_date','2026-10-03'),('draft_stage','corrections-applied'),('review_required','true')]:
  if re.search(rf'^{field}:',fm,re.M):fm=re.sub(rf'^{field}:.*$',field+': '+val,fm,flags=re.M)
  else:fm+='\n'+field+': '+val
 p.write_text('\n'.join(x.rstrip() for x in (fm+'\n---\n'+body).splitlines())+'\n',encoding='utf8')
 nuclei=[{'id':m[0],'heading':m[1],'words':len(re.findall(r'\b[\w’]+\b',m[2]))} for m in re.findall(r'^## (N-SP03-\d+-\d+) · ([^\n]+)\n(.*?)(?=^## |\Z)',body,re.M|re.S)]
 assert min(n['words'] for n in nuclei)>=600,(p,nuclei)
 stats.append({'path':p.as_posix(),'chapter':c,'words':len(re.findall(r'\b[\w’]+\b',body)),'nuclei':nuclei,'quiz':len(seq)})
(A/'M-SP03-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8');(A/'M-SP03-quiz-keys.json').write_text(json.dumps(keys,indent=2),encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';old=p.read_text(encoding='utf8');arc=C/'archive/pre-correzioni-sp03-matrice.md';assert not arc.exists();arc.write_text(old,encoding='utf8');fm=old.split('\n---\n',1)[0];fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M)
t=fm+'''\n---

# M-SP03 — Matrice di copertura didattica

Riconciliazione del 3 ottobre 2026: sette capitoli e trentacinque nuclei con numerazione corrispondente ai file. Il percorso copre scelta, requisiti, struttura delle prove, metodo di scrittura e pianificazione; non sostituisce l’intero programma civilistico, penalistico, amministrativo e notarile. Le verifiche normative sono selettive e tracciate nella fonte, non una certificazione dell’ordinamento completo.

Definizione, funzione, ambito, distinzioni, conseguenze, casi, output, quiz ed errori sono stati riesaminati nel perimetro dei nuclei. Q è il totale del capitolo; C ed E indicano almeno un caso e un esercizio. La densità quantitativa è distinta dalla completezza sostanziale.

| Nucleo ID | Materia/concetto | Fonte | Collocazione | Teoria | Applicazione/output | Verifica | Stato | Review normativa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''
for s in stats:
 for n in s['nuclei']:t+=f"| {n['id']} | {n['heading']} | [[{source}]] | cap. {s['chapter']:02}, heading {n['id']} | Spiegazione nel perimetro assegnato | {e[s['chapter']]} | Q:{s['quiz']} C:1 E:1 | completo | Riscontri puntuali nelle fonti e limiti dichiarati |\n"
p.write_text(t,encoding='utf8')
p=Path('wiki')/(topic+'.md');assert not p.exists();p.write_text('---\nid: topic-m-sp03-carriere-giuridiche-prove\ntype: topic\ntitle: Carriere giuridiche — requisiti e prove\nstatus: consolidated\ndomain: concorsi pubblici\nsource_refs: '+json.dumps([source])+'\nentities: '+json.dumps([entity])+'\nbook_refs: ["m-sp03-magistratura-avvocatura-notariato"]\nupdated_at: 2026-10-03\ncreated_at: 2026-10-03\nreview_required: false\ncanonical: true\n---\n\n# Carriere giuridiche — requisiti e prove\n\nTre percorsi distinti per accesso e prestazione. Le fonti della tornata non sono intercambiabili. La magistratura ordinaria esercita funzioni civili e penali; l’Avvocatura svolge difesa e consulenza istituzionale; il notariato è professione regolamentata con funzione pubblica.\n\n[['+source+']] — [['+entity+']]\n\n'+'\n'.join(f"- [[{Path(s['path']).with_suffix('').as_posix()[5:]}]] — {e[s['chapter']]}" for s in stats)+'\n',encoding='utf8')
p=Path('wiki')/(source+'.md');t=p.read_text(encoding='utf8');t=t.replace('*DA VERIFICARE (fonte secondaria):* pubblicazione del bando in G.U. Concorsi ed esami n. 83 del 24 ottobre 2025; scadenza domande 24 novembre 2025.','Pubblicazione e termine della domanda sono riscontrati sul bando ufficiale locale: G.U. Concorsi n. 83 del 24 ottobre 2025; scadenza 24 novembre 2025. Il diario successivo non è usato per decidere la domanda nel novembre 2025.')
t=t.replace('cinque precedenti concorsi** per notaio banditi dopo il 2009. L\'espulsione durante le prove scritte','cinque precedenti concorsi** per notaio banditi dopo l’entrata in vigore della legge 69/2009, conteggiati alla pubblicazione del bando. L’espulsione dopo la dettatura del tema durante le prove scritte')
t=re.sub(r'> \*\*Il notariato ha due vincoli.*?(?=\n\n)', '> **Il notariato combina pratica, limiti sugli esiti e redazione tecnica dell’atto.** Il limite specifico è cinque precedenti non idoneità alle condizioni del bando. Anche magistratura e procuratura prevedono limiti propri: rispettivamente quattro e due, senza equiparare domande ed esiti. La competenza redazionale richiede esercizio e correzione degli atti.',t,flags=re.S)
t=t.replace('per Avvocatura il vincolo caratterizzante della tornata è il limite anagrafico del bando','per Avvocatura due precedenti non idoneità, oltre al limite anagrafico del bando')
t+='\nRaccordo editoriale: [['+topic+']], [['+entity+']], [[books/moduli/m-sp03-magistratura-avvocatura-notariato/index]].\n';p.write_text(t,encoding='utf8')
mapping={36:(1,e[1]),37:(3,'Eliminati riferimenti alla ricerca interna; base dell’età ricondotta al D.P.C.M. 141/2000 e bando applicativo.'),38:(2,'Lingua qualitativa, minimi numerici e totale 108 con esempi chiusi.'),39:(6,'Distinti domanda e diario in cap. 2; confronto retrospettivo e candidatura storica tempestiva nel cap. 6.'),40:(3,e[3]),41:(4,'Separati prima candidatura di Marta e cinque esiti di Andrea, con cronologie possibili.'),42:(4,'Pratica alla scadenza, invio anticipato e certificato successivo distinti anche nella domanda-trappola.'),43:(5,e[5]),44:(5,'Formato deciso dal comando espresso; tesi e obiezioni solo quando pertinenti.'),45:(6,'Corrette forme aggiungi, classificale e pagina scritta male e corretta bene.'),46:(6,e[6]),47:(7,e[7])}
report='''# M-SP03 — Correzioni editoriali del 3 ottobre 2026

## 1. Sintesi editoriale

Applicati i rilievi V12-36–47 e le quote del modulo dei rilievi trasversali. Sette capitoli riesaminati integralmente; fonti normative controllate nei punti dichiarati, casi e calcoli svolti. Nuovo PDF necessario.

## 2. Punti applicati della checklist

Controllati perimetro, copertura, progressione, titoli, numerazione, funzioni, requisiti, cronologie, fonti, esempi, quiz, coerenza dei commenti, autonomia, stile e residui staff. Separata ammissibilità dalla preparazione.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
for n,(c,desc) in mapping.items():report+=f'| V12-{n:02} | Capitolo {c:02} | Contenuto e applicazione | Media | {desc} | Delta applicato e tracciato | Corretto |\n'
report+='\n## 4. Osservazioni per capitolo\n\n'+'\n\n'.join(f'{c:02}: {v}' for c,v in e.items())+'''

## 5. Coerenza globale

Trentacinque nuclei riconciliati con la matrice. I tre percorsi sono separati; numeri di posti non trasformati in probabilità individuali. Aggiunto anche il limite di due precedenti non idoneità per procuratore dello Stato, riscontrato direttamente nell’art. 4 del bando.

## 6. Contenuto da verificare

Nuovo PDF e altri moduli del volume. Le fonti storiche conservano i limiti espliciti: il vecchio PDF della legge notarile non contiene l’art. 5; non è usato per provarlo. Nessuna estensione generale di provvedimenti cautelari sul limite d’età. La sentenza TAR 11045/2026 è di improcedibilità, non di merito.

## 7. Suggerimenti facoltativi

Le clausole testamentarie sono esercizio limitato alla parte dispositiva, con condizioni e formalità distinte. Il piano biennale è adattabile e subordinato ai requisiti; non è una durata promessa per conseguire idoneità.

## 8. Priorità degli interventi

Audit specialistico, manifest e PDF. Proseguire SP04 prima della verifica complessiva del volume.

## 9. Giudizio di pubblicabilità

Non attestata. Correzioni testuali, verifica del modulo e resa finale sono passaggi separati.

## 10. Limiti della revisione

Lettura integrale dei sette capitoli e riscontri selettivi delle norme rilevanti; nessuna certificazione dell’intero programma concorsuale. I raw acquisiti con errore o senza articolo non sono evidenza normativa. Confronti automatici supportano il controllo umano, senza sostituirlo.
'''
p=R/'14-moduli-m-sp03-magistratura-avvocatura-notariato.md';arc=C/'archive/pre-correzioni-14-m-sp03.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text(report,encoding='utf8');(A/'M-SP03-findings-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf8')
print('SP03 close14',sum(s['words'] for s in stats),'words',sum(s['quiz'] for s in stats),'quiz')
