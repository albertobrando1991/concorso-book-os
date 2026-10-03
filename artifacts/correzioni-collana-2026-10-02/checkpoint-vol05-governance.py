from pathlib import Path
import json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');N=A/'norme-vol05'
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
p=N/'manifest.json';d=json.loads(p.read_text(encoding='utf8'))
full={('agcm',10),('consob',1),('privacy',153),('privacy',156),('risparmio',19),('civit',13),('ivass',13)}
partial={'arera':'Art. 2, commi 1–32; non articolo intero','agcom':'Art. 1, commi 1–5 e 9–12; comma 13 letto solo in parte','collegi':'Art. 23, commi 1–2-ter','anac':'Art. 19, commi 1–4'}
for r in d:
 if (r['name'],r['article']) in full:r.update(readComplete=True,readScope='Articolo intero; coordina norme successive esterne')
 elif r['name'] in partial:r.update(readComplete=False,readScope=partial[r['name']])
save(p,d)
p=N/'manifest-governance-extra.json';d=json.loads(p.read_text(encoding='utf8'))
for r in d:
 if r['name'] in ('consob-durata','personale'):r.update(readComplete=True,readScope='Articolo intero')
 else:r.update(readComplete=False,usableForClaim=False,readScope='Estratto art. 1 non contiene comma 528; escluso come prova di tale comma. Usata pagina ufficiale ARERA corrente.')
save(p,d)
p=N/'manifest-docs.json';d=json.loads(p.read_text(encoding='utf8'))
scopes={'statuto-ivass.pdf':'Lettura visiva pagine PDF 6–7: articoli 9, 11 e 12; non statuto intero','statuto-banca.pdf':'Passaggi artt. 18–23 tramite testo web primario; art. 19 solo passaggi pertinenti','ptpct-banca-2026.pdf':'Pagina PDF 12, aggiornamenti incompatibilità e investimenti; non piano intero','arera-chi-siamo.html':'Pagina istituzionale corrente: composizione, nomina e mandato; lettura web','anac-personale-art52quater.html':'Articolo 52-quater intero','banca-art29ter.html':'Articolo 29-ter intero','banca-art29quater.html':'Articolo 29-quater intero'}
for r in d:
 name=Path(r['path']).name
 if name in scopes:r.update(readScope=scopes[name],readComplete=name in ['anac-personale-art52quater.html','banca-art29ter.html','banca-art29quater.html'])
 if name in ['banca-art19bis.html','banca-art19ter.html']:r.update(usableForClaim=False,readComplete=False,readScope='URN non valido: restituisce art. 1; escluso dalle prove')
save(p,d)
p=A/'VOL-05-progress.json';save(p,dict(date='2026-10-03',chaptersReadThisCycle=[1,2,3,4],chaptersApplied=[2],findingsFullyApplied=['V05-05','V05-06'],findingsPartiallyApplied={'V05-02':'Capitolo 2: sei quesiti e un caso riscritti; altri capitoli da fare','V05-33':'Capitolo 2 repertorio introdotto; resto da fare'},pending=['Fonti e integrazioni capitoli 1, 3–15','90 quesiti / 15 casi complessivi e 10 simulazioni','Matrice, indici, rinvii','Audit e freeze tramite CLI','Figure e PDF coordinatore'],limitations=['Nessuna conclusione di pubblicabilità; capitoli in revisione','Articoli solo acquisiti non equiparati a lettura/verifica']))
print('Checkpoint VOL05 saved; chapter 2 applied, remaining work recorded.')
