from pathlib import Path
import re,json,shutil,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');delta=[]
def change(p,fn):
 t=p.read_text('utf-8');n=fn(t)
 if t==n:return
 b=A/'before-text/VOL-04/propagation'/p.relative_to('wiki');b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copyfile(p,b)
 before=hashlib.sha256(p.read_bytes()).hexdigest();p.write_text(n,'utf-8')
 delta.append(dict(path=p.as_posix(),before=before,after=hashlib.sha256(p.read_bytes()).hexdigest()))
s='vol-04-organizzazione-upp-verifica-2026-10-03'
p=Path('wiki/sources/ordinamento-giudiziario-upp-riforme-processuali-m-fc04.md')
def ord(t):
 t=t.replace("D.L. 12 giugno 2026, n. 100, non convertito entro la scadenza dell'11 agosto 2026 risultante dagli atti parlamentari consultati.","D.L. 12 giugno 2026, n. 100, convertito senza modificazioni dalla L. 7 agosto 2026, n. 145.")
 t=re.sub(r'Aggiornamento web ufficiale 2026-08-18:.*?(?=\n\n)',f'Rettifica 2026-10-03: il DL100/2026 è convertito dalla L.145/2026, GU8agosto, in vigore9agosto. La precedente conclusione di decadenza era errata; backup conservato. Prevale [[sources/{s}]], anche per DL144art7 e UPP coordinato.',t,flags=re.S)
 return t
change(p,ord)
p=Path('wiki/sources/ministero-giustizia-organizzazione-dipartimenti-m-fc04.md')
change(p,lambda t:t.replace('La DGSIA va collocata come struttura tecnico-amministrativa, non come dipartimento alternativo al DIT.','DGSIA è denominazione storica; il DIT comprende DGSAP, DGINFRA, DGSTAT e DGCOE.').replace('Richiamare la DGSIA per specifiche e servizi informatici quando pertinente,','Qualificare storicamente la DGSIA nelle specifiche pregresse,')+f'\n\n## Rettifica del 3 ottobre 2026\n\nOrganigramma verificato e competenze: [[sources/{s}]].\n')
root=Path('wiki/books/vol-04-giustizia-upp')
p=root/'planning/01-indice-dettagliato-volume-moduli-v4.md'
change(p,lambda t:t.replace("Verifica chiusa il 18 agosto 2026: non risulta conversione del D.L. 100/2026 entro la scadenza dell'11 agosto 2026.","Rettifica verificata il 3 ottobre 2026: DL100/2026 convertito dalla L.145/2026; leggere UPP coordinato anche dopo DL144/2026 art.7."))
p=root/'front-matter/06-indice.md'
change(p,lambda t:t.replace('DIT, DGSIA e supporto digitale','DIT e direzioni del digitale').replace('Stabilizzazione, nuova fase PNRR e caso del D.L. 100/2026 non convertito','Stabilizzazione, PNRR e aggiornamenti: DL 100/2026 convertito dalla L. 145/2026'))
p=next(Path('wiki/books/moduli/m-fc04-giustizia/chapters').glob('17-*.md'))
addition='''
## Ordinamento e Ufficio per il processo

- R.D. 30 gennaio 1941, n. 12, ordinamento giudiziario: artt. 42, 48, 56, 65, 70 e 73, da leggere con le disposizioni transitorie.
- D.Lgs. 25 luglio 2006, n. 240, artt. 1–4: capo dell'ufficio, dirigente amministrativo, risorse e programma annuale.
- D.Lgs. 10 ottobre 2022, n. 151, artt. 1–9: sedi, progetto, composizione e compiti degli UPP.
- L. 7 agosto 2026, n. 145, conversione senza modificazioni del DL 100/2026, GU n. 183 dell'8 agosto; in vigore il 9 agosto: https://www.gazzettaufficiale.it/eli/id/2026/08/08/26G00164/SG
- DL 7 agosto 2026, n. 144, art. 7: ulteriore modifica dei compiti del personale UPP. Consultare il testo coordinato e l'esito della conversione alla data della prova.
- Ministero della giustizia, organigramma corrente: https://www.giustizia.it/giustizia/page/it/articolazione_degli_uffici

La scheda parlamentare documenta l'iter, ma non sostituisce la pubblicazione in Gazzetta Ufficiale. Il DL 100/2026 non è decaduto; la sua conversione era già intervenuta prima del 18 agosto 2026.

'''
change(p,lambda t:t.replace('## Fonti normative e parlamentari ad alta mobilità',addition+'## Fonti normative e parlamentari ad alta mobilità'))
p=next(Path('wiki/books/moduli/m-fc04-giustizia/chapters').glob('12-*.md'))
change(p,lambda t:t.replace('| DIT e strutture tecniche, inclusa DGSIA | Innovazione, infrastrutture, specifiche, servizi e supporto tecnico-istituzionale |','| DIT: DGSAP, DGINFRA, DGSTAT e DGCOE | Servizi applicativi, infrastrutture e assistenza, statistica e analisi, coordinamento delle politiche di coesione. DGSIA è denominazione storica nelle specifiche pregresse. |'))
(A/'VOL-04-org-propagation-delta.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps({'files':len(delta),'note':'Cut-off globale non ancora chiuso; ch12 e17 parziali'}))
