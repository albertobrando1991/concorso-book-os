from pathlib import Path
import re,json,hashlib,shutil
A=Path(__file__).parent;W=Path('wiki/reviews/correzioni-collana-2026-10-02')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=W/'VOL-01.md';t=p.read_text('utf8');backup=A/'VOL-01-report-before-production-close.md'
if not backup.exists():shutil.copy2(p,backup)
t=re.sub(r'## 8\. Priorità degli interventi.*?(?=## 9\.)','## 8. Priorità degli interventi\n\nAudit specialistico e freeze conclusi; nuovo PDF di 686 pagine verificato con 437 rimandi, 43 tavole panoramiche e 14 dettagli finali. Resta completare i dati reali di V01-50/51 e collaudare l’attivazione promessa. Report di produzione: [PDF-VOL-01](PDF-VOL-01.md).\n\n',t,flags=re.S)
t=re.sub(r'## 9\. Giudizio di pubblicabilità.*?(?=## 10\.)','## 9. Giudizio di pubblicabilità\n\n**Non pubblicabile allo stato attuale per i preliminari V01-50 e V01-51.** I 49 rilievi dei capitoli e i 12 di produzione sono verificati nel perimetro dichiarato. Condizioni del servizio digitale, canale errata e dati editoriali effettivi restano da consolidare. Nessuna pubblicazione o conferma conclusiva.\n\n',t,flags=re.S)
t=t.replace('Il precedente PDF non rappresenta i manoscritti correnti.','I PDF storici non rappresentano i manoscritti correnti; il candidato da usare è identificato nel pacchetto del 3 ottobre 2026.')
p.write_text(t,'utf8')
for v,mod in [('01','il-metodo-bando'),('04','moduli-m-fc04-giustizia')]:
 p=Path(f'wiki/reviews/pipeline/VOL-{v}/16-{mod}.md');s=p.read_text('utf8');marker='\n## Riscontro conclusivo della produzione, 3 ottobre 2026\n'
 if marker not in s:s+=marker+f'\nLa tabella storica sopra conserva il freeze iniziale. Il manifest corrente M-{"PA01" if v=="01" else "FC04"}-freeze.json registra i delta controllati e gli hash finali. Il pacchetto delivery/VOL-{v}/candidate-2026-10-03 conserva il candidato verificato, le sorgenti e le evidenze. Per giudizio e limiti prevale il rapporto PDF-VOL-{v} del presente ciclo; nessuna conferma 24.\n'
 p.write_text(s,'utf8')
p=W/'README.md';b=A/'review-README-before-consegna.md'
if p.exists() and not b.exists():shutil.copy2(p,b)
p.write_text('''# Correzioni e integrazioni della collana — esito del 3 ottobre 2026

I dodici pacchetti locali sono raccolti nell'[indice di consegna](../../../delivery/COLLANA-REVISIONATA-2026-10-03.md). Il volume 2 comprende due tomi. Usare i PDF identificati dai manifest correnti: i candidati precedenti restano storici.

Il [registro consolidato](registro-applicazione-consolidato-2026-10-03.md) conserva i 582 rilievi iniziali: 577 verificati, quattro parziali e uno aperto non bloccante. I 13 rilievi aggiuntivi sono separati, senza alterare il conteggio originario. Rapporti VOL-01–12 e PDF-VOL-01–12 distinguono contenuti, produzione, copertura dei controlli e limiti.

**Nessun via libera complessivo alla pubblicazione.** Restano dati e condizioni dei servizi digitali, recapito errata e dati editoriali reali, prova fisica di compilazione, copertine e confezione finale. Giustizia ha superato la revisione 21; il suo preflight è registrato separatamente. Nessuno step 24 è stato eseguito.

Audit iniziale immutato in ../audit-integrale-2026-10-02; baseline, snapshot e registri precedenti restano negli artefatti. Non sono stati effettuati pubblicazione, commit o push.
''','utf8')
for v in ['01','04']:
 D=Path(f'delivery/VOL-{v}/candidate-2026-10-03')
 for p in [W/f'VOL-{v}.md',W/f'PDF-VOL-{v}.md',Path(f'wiki/reviews/pipeline/VOL-{v}/21-vol-{v}.md')]:shutil.copy2(p,D/'reports'/p.name)
 if v=='04':
  for p in [A/'VOL-04-text-verifica.json',A/'VOL-04-preflight-source-check.json',Path('wiki/reviews/pipeline/VOL-04/16-moduli-m-fc04-giustizia.md')]:shutil.copy2(p,D/'reports'/p.name)
 p=D/'package-manifest.json';d=json.loads(p.read_text('utf8'));d['files']=[dict(path=f.relative_to(D).as_posix(),bytes=f.stat().st_size,sha256=sha(f)) for f in sorted(D.rglob('*')) if f.is_file() and f.name!='package-manifest.json'];p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
print('Report aggiornati e manifest01/04 riallineati')
