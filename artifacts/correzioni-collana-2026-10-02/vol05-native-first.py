from pathlib import Path
import json,re,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');p=next(Path('wiki/books/moduli/m-fc05-authority-indipendenti/chapters').glob('01-*.md'))
original=p.read_text(encoding='utf8');snap=A/'vol05-native-snapshots'/p.name
assert not snap.exists();snap.write_text(original,encoding='utf8')
data={
1:('Dal bando alla prima prova','Passaggio|Decisione da prendere',[
('B — Bando','Ente, profilo, programma e formato della prova.'),('A — Aree','Base comune nel VOL-01 e contenuti specialistici pertinenti.'),('N — Nuclei','Fonte, interesse protetto, potere e procedura.'),('D — Diario','Errore preciso, rinvio e azione di recupero.'),('O — Output','Quiz, memo, caso o risposta orale previsti dal bando.')], 'Il percorso parte dal programma effettivo: non dalla notorietà dell’ente.'),
2:('Dall’ente al problema','Ente|Problema da riconoscere',[
('AGCM','Concorrenza e correttezza delle pratiche verso il consumatore.'),('ARERA','Qualità, tariffe e tutela nei servizi regolati.'),('AGCOM','Comunicazioni, media, utenti e piattaforme nei rispettivi regimi.'),('Consob','Mercati, informazione e condotta verso l’investitore.'),('Banca d’Italia / IVASS','Rischi prudenziali e tutele nei settori bancario e assicurativo.'),('Garante privacy','Dati personali, poteri correttivi e cooperazione.'),('ANAC','Prevenzione, trasparenza, vigilanza e whistleblowing.')], 'Settore e interesse orientano lo studio; il singolo potere richiede sempre la propria fonte.'),
3:('Tre percorsi, tre prodotti','Percorso|Prodotto da allenare',[
('G — Giuridico','Ricostruzione del procedimento con fonte, garanzia e rimedio.'),('E — Economico-regolatorio','Calcolo o analisi con dati, ipotesi, risultato e limite.'),('P — Giuridico-economico','Memo che collega norma, mercato, evidenza e decisione.')], 'La base è comune. Cambiano peso delle materie e forma dell’allenamento; nessun percorso autorizza a ignorare il programma.'),
4:('Decoder da compilare','Campo|Il tuo bando',[
('Ente, settore e codice del concorso','________________________________'),('Profilo e percorso prevalente','________________________________'),('Scadenza della domanda','________________________________'),('Prove, durata e soglia','________________________________'),('Materie comuni da richiamare','________________________________'),('Capitoli specialistici prioritari','________________________________'),('Nuclei più deboli e rischio principale','________________________________'),('Output e data del primo tentativo','________________________________')], 'Compila da bando e allegati. Se un dato manca, annota che cosa verificare: non inventarlo. L’esempio compilato segue nel caso guidato.'),
5:('Collegare base e specializzazione','Livello|Uso nella risposta',[
('Categoria generale','Richiama dal VOL-01 il principio o l’istituto necessario.'),('Applicazione settoriale','Identifica interesse, fonte, potere e procedimento dell’autorità.'),('Richiesta della prova','Usa questi elementi per concludere il caso o produrre l’output richiesto.')], 'Una risposta utile unisce i tre livelli: non ripete soltanto una definizione né elenca sigle.')}
ledger=json.loads((A/'VOL-05-native-schemes.json').read_text(encoding='utf8'))
def repl(m):
 n=int(m[1]);title,cols,rows,note=data[n];left,right=cols.split('|')
 native=f'#### Schema 1.{n} — {title}\n\n| {left} | {right} |\n|---|---|\n'+'\n'.join('| '+a+' | '+b+' |' for a,b in rows)+'\n\n'+note
 image=m[2];raw=(p.parent/image).resolve()
 ledger['records'].append({'file':p.as_posix(),'schema':f'1.{n}','originalImage':image,'originalSHA256':hashlib.sha256(raw.read_bytes()).hexdigest(),'nativeText':native,'sourceEvidence':'Capitolo 01 corretto e prova PDF iniziale pagine 11,15,17,18,20','sha256Before':hashlib.sha256(snap.read_bytes()).hexdigest()})
 return native
s=re.sub(r'!\[Figura 1\.(\d+)[^\n]*\]\(([^\n)]+)\)',repl,original)
s=re.sub(r'^\*Figura 1\.\d+[^\n]*\*\s*\n','',s,flags=re.M)
s=re.sub(r'asset_refs:\n(?:  - .*\n)+','asset_refs: []\n',s);p.write_text(s,encoding='utf8')
for r in ledger['records']:
 if r['file']==p.as_posix():r['sha256After']=hashlib.sha256(p.read_bytes()).hexdigest()
ledger['count']=75;ledger['additionalFiveReason']='PDF iniziale: etichette raster minute e Decoder non praticabile su carta.'
(A/'VOL-05-native-schemes.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
print('Five first-chapter images replaced; total 75 native schemes.')
