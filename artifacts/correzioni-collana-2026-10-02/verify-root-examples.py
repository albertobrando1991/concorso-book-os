from pathlib import Path
import sqlite3,re,json,math,hashlib
from datetime import datetime,timedelta
base=Path('wiki/books/il-metodo-bando/chapters');t=(base/'informatica-pa-digitale-competenze-digitali.md').read_text(encoding='utf8')
query=next(x.strip() for x in re.findall(r'```sql\n(.*?)```',t,re.S) if 'JOIN Uffici' in x)
c=sqlite3.connect(':memory:');c.execute('PRAGMA foreign_keys=ON')
c.executescript('CREATE TABLE Uffici(IdUfficio INTEGER PRIMARY KEY,NomeUfficio TEXT); CREATE TABLE Dipendenti(IdDipendente INTEGER PRIMARY KEY,Cognome TEXT,IdUfficio INTEGER REFERENCES Uffici(IdUfficio)); INSERT INTO Uffici VALUES(10,\'Anagrafe\'),(20,\'Tributi\'); INSERT INTO Dipendenti VALUES(1,\'Verdi\',10),(2,\'Bianchi\',10),(3,\'Neri\',20);')
result=c.execute(query).fetchall();assert result==[('Bianchi','Anagrafe'),('Verdi','Anagrafe')]
try:c.execute('INSERT INTO Dipendenti VALUES(4,\'Rossi\',99)');raise AssertionError('FK assente')
except sqlite3.IntegrityError:pass
cells=[10,20,30];assert [x*.1 for x in cells]==[1,2,3]
assert [sum(cells),sum(cells)/len(cells),min(cells),max(cells),len(cells)]==[60,20,10,30,3]
assert ['Sì' if x>=20 else 'No' for x in cells[:2]]==['No','Sì']
assert 120+80-50-30==120 and 120-45-40-10==25 and 120-80-40-10==-10
assert 100-60==40 and 100-40==60 and 100*.3==30
assert 36-12*.25==33 and 36/50*100==72 and 36/48*100==75
assert math.isclose(.25*1-.75*.25,.0625) and math.isclose(.25-.75*.5,-.125) and math.isclose(.5-.5*.5,.25)
assert math.isclose(.25/1.25,.2)
assert datetime(2026,10,5,10)+timedelta(hours=72)==datetime(2026,10,8,10)
out={'status':'passed','checks':['SQL eseguito dal blocco del capitolo: JOIN, filtro, ordine e rifiuto chiave esterna inesistente','Esempi foglio: 1/2/3, somma/media/min/max/conteggio e condizione','Risultato amministrazione, quote e parte disponibile negativa','Residuo Stato, FPV e FCDE del caso','Marta: punteggio e denominatori distinti','Quiz: valori attesi e soglia di convenienza','Breach: 72 ore lunedì-giovedì'],'sqlOutput':result,'limits':'Verifica dei casi numerici e informatici indicati; non sostituisce revisione normativa, linguistica o PDF','chapterHashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in base.glob('*.md') if p.name in ['informatica-pa-digitale-competenze-digitali.md','contabilita-pubblica-essenziale.md','diario-degli-errori.md','la-prova-a-quiz.md','trasparenza-anticorruzione-privacy.md']}}
Path(__file__).with_name('vol01-esempi-verificati.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(out,ensure_ascii=False))
