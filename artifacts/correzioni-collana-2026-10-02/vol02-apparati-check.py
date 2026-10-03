from pathlib import Path
import re,json,random,hashlib
art=Path('artifacts/correzioni-collana-2026-10-02');vol=Path('wiki/books/vol-02-enti-locali-polizia-locale');p=vol/'chapters/50-simulazione-finale-vol-02.md';t=p.read_text(encoding='utf-8')
# Keep correct answer text unchanged; balance locations without cyclic answer pattern.
oldkeys={int(n):k for n,k in re.findall(r'^\| (\d+) \| ([A-D]) \|',t,re.M)};letters=list('ABCD'*5);rng=random.Random(530);rng.shuffle(letters);newkeys={};correct={}
def rotate(m):
 n=int(m[2]);opts=re.findall(r'^([A-D])\. (.*)$',m[3],re.M);answer=next(x[1] for x in opts if x[0]==oldkeys[n]);wrong=[x[1] for x in opts if x[0]!=oldkeys[n]];rng.shuffle(wrong);pos='ABCD'.index(letters[n-1]);wrong.insert(pos,answer);newkeys[n]='ABCD'[pos];correct[n]=answer
 return m[1]+''.join('ABCD'[i]+'. '+x+'\n\n' for i,x in enumerate(wrong))
t=re.sub(r'(\*\*(\d+)\..*?\*\*\n\n)((?:[A-D]\. [^\n]+\n\n){4})',rotate,t);assert len(newkeys)==20
t=re.sub(r'^(\| (\d+) \| )([A-D])( \|)',lambda m:m[1]+newkeys[int(m[2])]+m[4],t,flags=re.M)
t=t.replace('Art.23:', 'Art. 23:').replace('spesa.3 ottobre','spesa. 3 ottobre')
t=t.replace('Il dossier non contiene ancora', 'Il dossier non contiene ancora')
t=t.replace('L\'importo proposto è 900 euro complessivi; il dossier non contiene ancora', 'La scheda di fabbisogno allegata alla traccia indica 900 euro complessivi e il prospetto finanziario riporta la disponibilità di 1.000 euro; il dossier non contiene ancora')
t=t.replace('Gli agenti annotano i dati visibili del veicolo.', 'Gli agenti annotano i dati visibili del veicolo.')
t=t.replace('gli agenti annotano i dati visibili del veicolo. Nessuna dichiarazione', 'gli agenti annotano i dati visibili del veicolo nella scheda V1 e localizzano il punto nella scheda dei luoghi. Queste schede sono gli allegati didattici della traccia, senza nominativi o targhe reali. Nessuna dichiarazione')
old='Per il caso assegna fino a due punti per la qualificazione corretta, due per la sequenza e tre per i controlli decisivi del percorso: nel Comune, differenza 100 e assenza di liquidazione; nella Provincia, competenza scolastica e diagnosi non acquisita; nella Camera, separazione delle istanze e istruttoria dell\'interesse; nella PL, ramo penale e CNR anche contro ignoti. Dai un punto solo parziale quando un elemento è nominato senza applicazione.'
new='''Per il caso assegna fino a due punti per la qualificazione corretta e due per la sequenza: zero se errate, uno se incomplete, due se corrette e applicate. Gli altri tre punti sono attribuiti, uno ciascuno, ai controlli seguenti.

| Percorso | Controllo 1 | Controllo 2 | Controllo 3 |
|---|---|---|---|
| Comune | Calcolo 100 euro residui, dichiarato teorico | Istruttoria dell'acquisto e controlli mancanti | Nessun pagamento prima delle fasi necessarie |
| Provincia | Competenza sull'edificio scolastico nel dossier | Diagnosi tecnica non ancora acquisita | Raccordo tecnico/scuola senza urgenza o spesa inventata |
| Camera | Visura distinta dall'accesso al fascicolo | Istruttoria del collegamento all'interesse documentale | Valutazione di controinteressati e limiti, senza esito automatico |
| Polizia locale | Art. 255, comma 1, di natura penale | CNR anche contro ignoti | Ripristino e PG distinti; nessun sequestro inventato |

Il punto si assegna quando il controllo è applicato ai dati, non soltanto nominato.'''
assert old in t;t=t.replace(old,new);p.write_text(t,encoding='utf-8')
keyfile=art/'VOL-02-simulazione-key.json';keydata=json.loads(keyfile.read_text(encoding='utf-8'));keydata['keys']=newkeys;keydata['correctTexts']=correct;keydata['distribution']={l:letters.count(l) for l in 'ABCD'};keyfile.write_text(json.dumps(keydata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
mods=[Path('wiki/books/moduli')/x for x in ['m-fl01-comuni-unioni','m-fl02-regioni-province-citta-metropolitane','m-fl03-camere-commercio','m-fl04-polizia-locale']]
chapters=sorted((vol/'chapters').glob('0[123]-*.md'))+[p for m in mods for p in sorted((m/'chapters').glob('*.md'))]+sorted((vol/'chapters').glob('5[01]-*.md'))
assert len(chapters)==51
refs=[];invalid=[];internal=[];numbers=[]
for p in chapters+list((vol/'front-matter').glob('*.md'))+list((vol/'modules').glob('*.md')):
 text=p.read_text(encoding='utf-8');body=text.split('---',2)[-1]
 if re.search(r'\[\[(?:sources|topics|entities|raw|planning|reviews)/',body):internal.append(p.as_posix())
 for m in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',text):
  target,_,anchor=m[1].partition('#');dest=Path('wiki')/target
  if dest.suffix!='.md':dest=dest.with_suffix('.md')
  refs.append(m[1])
  if not dest.exists():invalid.append({'file':p.as_posix(),'target':m[1],'issue':'missing-file'})
  elif anchor and anchor not in re.findall(r'^#{1,6}\s+(.+?)\s*$',dest.read_text(encoding='utf-8'),re.M):invalid.append({'file':p.as_posix(),'target':m[1],'issue':'missing-heading'})
for i,p in enumerate(chapters,1):
 t=p.read_text(encoding='utf-8');m=re.search(r'^volume_chapter:\s*(\d+)',t,re.M)
 if m and int(m[1])!=i:numbers.append({'file':p.as_posix(),'expected':i,'actual':int(m[1])})
index=(vol/'front-matter/06-indice.md').read_text(encoding='utf-8');seq=[int(x) for x in re.findall(r'^(\d+)\. \*\*',index,re.M)];assert seq==list(range(1,52)),seq
words={m.name:sum(len(re.findall(r'\S+',p.read_text(encoding='utf-8').split('---',2)[-1])) for p in (m/'chapters').glob('*.md')) for m in mods}
result={'chapters':51,'internalLinksInBody':internal,'linksChecked':len(refs),'invalidLinks':invalid,'volumeNumbersMismatch':numbers,'sourceIndexContinuous':True,'wordsByModuleApprox':words,'simulation':{'questions':20,'distribution':keydata['distribution'],'points':30,'minutes':70,'fourSolvedPaths':True},'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in chapters],'limits':['PDF corrente non ancora generato; nessuna prova di pagine/layout da questi controlli','Servizi digitali e dati editoriali richiedono allineamento comune con coordinatore']}
(art/'VOL-02-text-handoff.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='files'},ensure_ascii=False))
