from pathlib import Path
import shutil,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/raw/correzioni-collana-2026-10-02')
p=Path('wiki/sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02.md');t=p.read_text(encoding='utf8');t+='''

## Prevenzione incendi: funzione e procedimenti — 3 ottobre 2026

Normattiva, testi correnti acquisiti e letti integralmente per gli articoli indicati:

- D.Lgs. 139/2006, art. 13: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2006-03-08;139~art13!vig= . Funzione pubblica che previene insorgenza e limita conseguenze, per vita, persone, beni e ambiente; criteri uniformi e competenze concorrenti di altre amministrazioni preservate. Evitare equivalenza fra prevenzione e sola estinzione.
- D.P.R. 151/2011, art. 3: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2011-08-01;151~art3!vig= . Attività soggette categorie B/C: valutazione progetti nuovi e modifiche con aggravio; integrazioni entro 30 giorni; pronuncia entro 60 dalla documentazione completa.
- Art. 4 dello stesso decreto: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2011-08-01;151~art4!vig= . SCIA prima dell’esercizio per attività dell’allegato I; ricevuta dopo verifica formale, non collaudo materiale. A/B: controlli anche a campione entro 60 giorni; C: visite entro 60, CPI entro 15 dalla visita positiva. In carenza: divieto motivato e rimozione effetti, salvo conformazione possibile entro 45 giorni. Comma 6: modifiche rilevanti impongono nuovo avvio, fermo art. 3 per aggravio. Questi sono procedimenti distinti: non basta avere un progetto esaminato per omettere SCIA, né basta ricevuta per escludere controlli.

La lezione è una mappa istituzionale e procedurale per il programma direttivo, non un progetto antincendio eseguibile né un manuale completo di tutte le regole tecniche. La scelta della regola tecnica, dei dati e delle soluzioni resta dipendente da attività, progetto e disciplina specifica.
'''
for n in ['dl139-art13-current.html','dpr151-art3-current.html','dpr151-art4-current.html']:
 assert 'art_text_in_comma' in (A/n).read_text(encoding='utf8')
 if not (R/n).exists():shutil.copyfile(A/n,R/n)
 t+=f'\nRaw `{(R/n).as_posix()}`, SHA256 `{hashlib.sha256((R/n).read_bytes()).hexdigest()}`.\n'
p.write_text(t,encoding='utf8');print('Prevenzione consolidata')
