from pathlib import Path
import importlib.util,json,re
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.REF='sources/vol-01-procedimento-correzioni-2026-10-03.md'
slug='diritto-amministrativo-per-candidati';t=u.read(slug)
t=u.replace(t,'Individuati nei modi dei commi 3 e 5;','Individuati nei modi del comma 3;')
anchor='La frase da memorizzare è: prima qualifico il procedimento, poi valuto il regime del silenzio. Dire automaticamente “silenzio-assenso” è un errore da concorso.'
t=u.replace(t,anchor,anchor+'\n\n**Silenzio-assenso e attestazione nel quadro del 2026.** Nell’ambito dei procedimenti soggetti all’art. 20 della legge 241/1990, la domanda deve essere ricevuta dall’amministrazione competente e contenere gli elementi indispensabili per individuare oggetto e ragioni del provvedimento richiesto. Restano le esclusioni del comma 4: questa regola non rende soggetti al silenzio-assenso tutti i procedimenti, per esempio quelli in materia di tutela ambientale o salute. La facoltà di chiedere informazioni o integrazioni si coordina con l’art. 2, comma 7; una richiesta non determina una proroga indefinita.\n\nUna volta formato il silenzio-assenso, l’attestazione è rilasciata in via telematica e automatica. Nei procedimenti non ancora telematizzati l’amministrazione la invia d’ufficio alla PEC o all’indirizzo ordinario indicato nell’istanza entro dieci giorni dalla formazione. Se tale termine decorre inutilmente, l’attestazione è sostituita dalla dichiarazione del privato ai sensi dell’art. 47 del DPR 445/2000, oppure del progettista abilitato. L’attestazione documenta l’effetto già prodotto: non è un ulteriore titolo necessario perché il silenzio si formi.')
u.save(slug,t,['V01-10'],u.REF);u.record()
u.REF='sources/vol-01-esempi-logica-inglese-metodo-2026-10-02.md';u.changes={}
slug='diario-degli-errori';t=u.read(slug)
t=u.replace(t,'Il tasso di secondo tentativo è `errori corretti al controllo / errori ricontrollati × 100`.','Il tasso di secondo tentativo è `errori corretti al controllo / errori ricontrollati × 100`. Se il denominatore è zero, segna “non calcolabile”: nessun quiz svolto o nessun errore ricontrollato non equivale a una prestazione dello 0%.')
u.save(slug,t,['V01-42'],u.REF);u.record()
u.changes={}
archive=[]
for row in json.loads(Path(__file__).with_name('baseline.json').read_text(encoding='utf8')):
 p=Path(row['file'])
 if 'il-metodo-bando' not in p.parts:continue
 t=p.read_text(encoding='utf8');original=t
 # Remove only entirely internal reference sections; keep reader content and source metadata.
 pattern=r'(?m)^## (?:Fonti consolidate|Riferimenti consolidati)\s*\n([\s\S]*?)(?=^## |\Z)'
 def remove(m):
  lines=[l.strip() for l in m[1].splitlines() if l.strip()]
  if all(re.fullmatch(r'- \[\[(?:sources|topics|entities)/[^\]]+\]\]',l) for l in lines):
   archive.append({'file':p.as_posix(),'removed':m[0]});return ''
  return m[0]
 t=re.sub(pattern,remove,t)
 if p.stem=='introduzione':t=u.replace(t,'Questo è il punto commerciale e didattico del libro:','Il percorso del libro segue questa logica:')
 if p.stem=='il-metodo-bando':
  t=u.replace(t,'## Perché il metodo è il prodotto','## Dal materiale di studio al lavoro quotidiano')
  t=u.replace(t,'La concorrenza spesso offre tre cose: un manuale più grande, una raccolta di quiz più lunga o un corso più fitto. Tutte possono essere utili, ma nessuna risolve da sola il problema principale: decidere che cosa fare con il tempo che hai.','Manuali, raccolte di quiz e corsi possono aiutarti a prepararti. Per usarli bene devi però decidere quali argomenti affrontare, con quali esercizi e in quanto tempo. Il metodo collega il materiale disponibile alle attività della tua settimana.')
 if p.stem in ['casi-pratici-problem-solving-amministrativo','anatomia-del-bando','bando-decoder','appendice-c-template-bando-decoder']:
  t=re.sub(r'\b(legge|comma|Capitolo|DPR|art\.)\s*(?=\d)',r'\1 ',t)
  t=t.replace('a140.000','a 140.000')
 if t!=original:u.save(p.stem,t.rstrip()+'\n',['V01-49'],u.REF)
Path(__file__).with_name('vol01-riferimenti-interni-rimossi.json').write_text(json.dumps(archive,ensure_ascii=False,indent=2),encoding='utf8')
u.record()
