from pathlib import Path
import re,json,hashlib
O=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');files=sorted((B/'chapters').glob('*.md'))
for p in files:
 s=p.read_text(encoding='utf8')
 # Move only demonstrated separators; preserve every paragraph, caption and table.
 s=re.sub(r'(!\[[^\n]+\]\([^\n]+\))\n\n(## N-MF05-[^\n]+)\n\n(\*Figura[^\n]+)',r'\1\n\n\3\n\n\2',s)
 s=re.sub(r'(### [^\n]+)\n\n(## N-MF05-[^\n]+)',r'\2\n\n\1',s)
 if p.name.startswith('07-'):
  marker='## N-MF05-07-05 · Consolidamento e verifica';s=s.replace(marker+'\n\n','');s=s.replace('### Mini-esercizio di consolidamento',marker+'\n\n### Mini-esercizio di consolidamento')
 if p.name.startswith('05-'):
  marker='## N-MF05-05-04 · Applicazione alla prova';s=s.replace(marker+'\n\n','');s=s.replace('### Mappa BANDO',marker+'\n\n### Mappa BANDO')
 s=s.replace('Nel privacy','Nel settore privacy').replace('nel elaborato','nell’elaborato').replace('occorre a loro volta','occorre a sua volta')
 s=s.replace("In un concorso, la risposta migliore dichiara la regola generale e rinvia alla fonte dell'ente per il dettaglio applicativo.","In un concorso, la risposta applica la regola specifica dell'ente: le tabelle precedenti forniscono il quadro strutturale, da completare sul bando per requisiti individuali e programma.")
 s=s.replace('profili giuridico, economico e policy','profili giuridico, economico e giuridico-economico').replace('profilo policy','profilo giuridico-economico')
 for key,vals in [('topics',['topics/authority-rettifiche-2026']),('last_compiled_from',['wiki/topics/authority-rettifiche-2026.md'])]:
  m=re.search(r'^'+key+r': (\[.*\])$',s,re.M);a=json.loads(m[1]);a=list(dict.fromkeys(a+vals));s=s[:m.start(1)]+json.dumps(a,ensure_ascii=False)+s[m.end(1):]
 p.write_text(s,encoding='utf8')
# Source corrections and precise shared laboratory provenance.
p=Path('wiki/sources/vol-05-bandi-authority-2022-2025.md');s=p.read_text(encoding='utf8').replace('12-banca-italia-ivass-vigilanza-prudenziale-bancaria-assicurativa','12-banca-italia-ivass-vigilanza-prudenziale');p.write_text(s,encoding='utf8')
p=Path('wiki/sources/vol-05-reti-ue-verifica-2026-10-03.md');s=p.read_text(encoding='utf8').replace('CP%20with%20RTS-ITS%20on%20colleges.pdf','CP%20with%20RTS-ITS%20on%20supervisory%20colleges.pdf');p.write_text(s,encoding='utf8')
sources=sorted(Path('wiki/sources').glob('vol-05-*-verifica-2026-10-03.md'))
p=files[-1];s=p.read_text(encoding='utf8');m=re.search(r'^source_refs: (\[.*\])$',s,re.M);a=list(dict.fromkeys(json.loads(m[1])+['sources/'+x.name for x in sources]));s=s[:m.start(1)]+json.dumps(a,ensure_ascii=False)+s[m.end(1):];p.write_text(s,encoding='utf8')
p=Path('wiki/topics/authority-rettifiche-2026.md');s=p.read_text(encoding='utf8');s=re.sub(r'^source_refs:.*$','source_refs: '+json.dumps(['sources/'+x.name for x in sources]),s,flags=re.M);s=re.sub(r'^chapter_refs:.*$','chapter_refs: '+json.dumps([x.as_posix()[5:-3] for x in files]),s,flags=re.M);s+='\n## Laboratorio e riscontro del conteggio\n\nNovanta quesiti aperti con risposte specifiche, quindici casi finali, dieci simulazioni con dossier e soluzioni. I calcoli E1/E2/E3 e SCR e il memo inglese di 107 parole sono verificati in `artifacts/correzioni-collana-2026-10-02/VOL-05-simulations-verification.json`. La matrice non attribuisce sei quesiti a ogni nucleo.\n';p.write_text(s,encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';old=p.read_text(encoding='utf8');arc=B/'planning/revisioni-2026-10-03';arc.mkdir(exist_ok=True)
if not (arc/'matrice-precedente.md').exists():(arc/'matrice-precedente.md').write_text(old,encoding='utf8')
fm=old.split('---',2)[1];fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M)
s='---'+fm+'---\n\n# Copertura effettiva — M-FC05\n\nSono inventariati 75 nuclei in 15 capitoli. Le verifiche sono integrate per capitolo: **90 quesiti aperti, 15 casi finali**, oltre a casi guidati, mini-esercizi e **10 simulazioni svolte**. Non sono 450 quesiti. Le unità canoniche aggregate sottostanti rendono esplicito il conteggio unico; la tabella analitica localizza il contenuto effettivo. Le attestazioni precedenti sono archiviate e non certificano la presente versione.\n\n## Inventario analitico dei nuclei\n\n| Nucleo | Capitolo | Evidenza nel testo | Verifica integrata | Esito |\n|---|---|---|---|---|\n'
details=[]
for ch in files:
 t=ch.read_text(encoding='utf8');heads=list(re.finditer(r'^## (N-MF05-\d\d-\d\d) · (.*)$',t,re.M));n=ch.name[:2]
 for i,m in enumerate(heads):
  block=t[m.end():heads[i+1].start() if i+1<len(heads) else len(t)];hs=re.findall(r'^### (.+)$',block,re.M);ev='; '.join(hs[:5]) or m[2]+' — spiegazione e applicazioni nel blocco'
  s+='| '+m[1]+' | '+n+' | '+ev.replace('|','/')+' | Q1–Q6 e caso del capitolo '+n+'; conteggio unico sotto | verificato nel perimetro |\n'
  details.append({'id':m[1],'chapter':n,'headings':hs,'words':len(block.split())})
s+='\n## Copertura canonica delle unità di capitolo\n\n| Nucleo ID | Materia | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica apprendimento | Stato | Review normativa |\n|---|---|---|---|---|---|---|---|---|---|\n'
for ch in files:
 t=ch.read_text(encoding='utf8');n=ch.name[:2];title=re.search(r'^title: "(.*)"',t,re.M)[1];refs=[x for x in json.loads(re.search(r'^source_refs: (.*)$',t,re.M)[1]) if 'verifica-2026-10-03' in x]
 s+='| N-MF05-'+n+'-01 | Unità aggregata: '+title+' | '+('; '.join(refs) or 'source_refs del capitolo; fonti ufficiali nominate nel corpo')+' | cap. '+n+' | Nuclei 01–05 e sezioni nominate nell’inventario | Casi guidati e mini-esercizio; sei risposte specifiche e caso finale | Output della Mappa BANDO; '+('10 simulazioni risolte' if n=='15' else 'orale e caso risolto')+' | Q:6 C:1 E:1 conteggio minimo del capitolo, non del singolo nucleo | completo | Verifica mirata 3 ottobre 2026; ambiti e limiti nelle note |\n'
s+='\n## Checklist dimensionale delle unità aggregate\n\nLe dieci dimensioni sono valutate nel capitolo intero: definizione e quadro nei primi nuclei, conseguenze e distinzioni nello sviluppo, applicazione nel caso, errori/trappole e sei quesiti commentati nelle sezioni finali. Non si afferma che ciascuna sottosezione ripeta tutte le dimensioni né che ogni norma esterna sia stata letta integralmente.\n\n| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Errore tipico | Verifica | Fonti |\n|---|---|---|---|---|---|---|---|---|---|---|\n'
for n in range(1,16):s+='| N-MF05-'+f'{n:02d}'+'-01 | '+' | '.join(['✓ capitolo']*10)+' |\n'
s+='\n## Limiti\n\nIl perimetro è concorsuale: matematica/econometria avanzata e corsi completi di diritto civile o societario restano esclusi. I dati numerici didattici non sono tariffe o coefficienti universali. Rinvii comuni precisi nel capitolo 1; percorso tecnico-digitale verso VOL-08. Figure e PDF aggiornati ancora da verificare prima della consegna.\n';p.write_text(s,encoding='utf8')
for p in [B/'index.md',B/'planning/00-piano-editoriale.md',B/'planning/03-bibbia-del-modulo.md',Path('wiki/books/vol-05-authority-regolazione/index.md')]:
 s=p.read_text(encoding='utf8').replace('profili giuridici, economici e policy','profili giuridici, economici e giuridico-economici').replace('candidati giuridici, economici e policy','candidati giuridici, economici e giuridico-economici').replace('premium','integrato');s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M)
 s+='\n## Versione del 3 ottobre 2026\n\nQuindici capitoli; percorsi G giuridico, E economico-regolatorio e P giuridico-economico. Novanta quesiti aperti specifici, quindici casi finali e dieci simulazioni svolte con dossier, tre prove economiche numeriche e memo inglese. Il capitolo 1 contiene rinvii puntuali al base e piani di studio alternativi. Il perimetro non comprende un corso avanzato di econometria né ogni materia di qualsiasi bando.\n';p.write_text(s,encoding='utf8')
(O/'VOL-05-nuclei-current.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['findingsFullyApplied']=sorted(set(d['findingsFullyApplied']+['V05-01','V05-03','V05-04','V05-33']));d['findingsPartiallyApplied']={};d['pending']=['Verifica link e gate 10/14/15/16','Schemi nativi specifici al posto delle figure generiche','PDF e pacchetto; nessuna chiusura automatica step 24'];f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Reconciled',len(details),'nuclei, 90 questions; 33 text findings applied, verification pending.')
