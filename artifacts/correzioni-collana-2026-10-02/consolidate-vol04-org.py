from pathlib import Path
import re,shutil
A=Path('artifacts/correzioni-collana-2026-10-02')
source='vol-04-organizzazione-upp-verifica-2026-10-03'
p=Path('wiki/sources/vol-04-aggiornamento-normativo-2026-08-18.md')
b=A/'before-text/VOL-04/sources'/p.name;b.parent.mkdir(parents=True,exist_ok=True)
if not b.exists():shutil.copyfile(p,b)
t=p.read_text('utf-8')
t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true')
t=re.sub(r'## Organizzazione del Ministero\n.*?(?=## Copie esecutive)', '''## Rettifica documentata del 3 ottobre 2026

La versione precedente conteneva un errore sulla conversione del DL 100/2026 e un organigramma non aggiornato. Copia storica conservata nell'artefatto di correzione; prevale [[sources/vol-04-organizzazione-upp-verifica-2026-10-03]].

## Organizzazione del Ministero

Cinque dipartimenti: DAG, DOG, DIT, DAP e DGMC. Il DIT comprende DGSAP, DGINFRA, DGSTAT e DGCOE. DGSIA è una denominazione storica, tuttora presente in documentazione tecnica pregressa e recapiti, non una direzione attuale aggiuntiva.

## D.L. 12 giugno 2026, n. 100

Convertito senza modificazioni dalla L. 7 agosto 2026, n. 145, pubblicata nella GU n. 183 dell'8 agosto, in vigore dal 9 agosto. Era dunque già convertito al precedente cut-off del 18 agosto. L'assenza di aggiornamento di una scheda parlamentare non provava la decadenza. Per i compiti UPP occorre inoltre leggere la novella dell'art. 7 DL 144/2026 nel testo coordinato degli artt. 5–6 D.Lgs. 151/2022.

**Esito: errore storico rettificato con fonte ufficiale GU.**

''',t,flags=re.S)
p.write_text(t,'utf-8')
delta='''
## Aggiornamento verificato al 3 ottobre 2026

Fonte prevalente per questi punti: [[sources/vol-04-organizzazione-upp-verifica-2026-10-03]]. Il DL 100/2026 è convertito dalla L. 145/2026; non è decaduto. Gli UPP sono strutture con più figure professionali, distinte dai singoli addetti. Artt. 1–4 D.Lgs. 151/2022 disciplinano sedi, progetto, coordinamento e composizione. Non esiste per questa sola norma un UPP ordinario in ogni Procura: la Procura generale della Cassazione ha specifiche strutture previste dall'art. 1.

Il personale dell'art. 4, comma 1, lettera f svolge i compiti previsti dagli artt. 5–6 e dal contratto e, secondo il testo vigente dall'8 agosto 2026, anche attività di cancelleria in via residuale. La decisione resta del magistrato competente. La conversione del DL 144/2026 richiede controllo conclusivo al freeze, senza dedurre decadenza da iter incompleti.

Il DIT comprende DGSAP, DGINFRA, DGSTAT e DGCOE; DGSIA va qualificata storicamente. Capo magistrato e dirigente amministrativo hanno responsabilità distinte secondo D.Lgs. 240/2006 e concordano il programma annuale. Funzione giudiziaria comprende funzioni giudicanti e requirenti, da distinguere dalla gestione dei servizi ministeriali.

Capitoli impattati: [[books/moduli/m-fc04-giustizia/chapters/01-sistema-giustizia-visto-dal-candidato]], [[books/moduli/m-fc04-giustizia/chapters/02-ministero-dipartimenti-amministrazioni-giustizia]], [[books/moduli/m-fc04-giustizia/chapters/03-uffici-giudiziari-ordinamento-lavoro-ufficio]], [[books/moduli/m-fc04-giustizia/chapters/04-ufficio-per-il-processo-struttura-progetto-flussi]].
'''
for file in ['wiki/topics/giustizia-e-upp.md','wiki/entities/ufficio-per-il-processo.md','wiki/entities/ministero-della-giustizia.md']:
 p=Path(file);t=p.read_text('utf-8')
 if source not in t:
  t=t.replace('source_refs: [',f'source_refs: ["sources/{source}.md", ',1)
  t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1)
  p.write_text(t+delta,'utf-8')
p=Path('wiki/index.md');t=p.read_text('utf-8')
if source not in t:p.write_text(t+f'\n- [[sources/{source}]] — rettifica conversione, UPP e organigramma Giustizia; verifica normativa 3 ottobre 2026.\n','utf-8')
with Path('wiki/log.md').open('a',encoding='utf-8') as f:f.write('\n\n## 2026-10-03 — Rettifica normativa Giustizia e figure VOL-01\n\nConsolidati conversione DL100/L145, UPP D.Lgs.151 coordinato, DL144 art.7, D.Lgs.240 e organigramma DIT. Rettificata fonte errata del 18 agosto con backup; collegati topic ed entità. VOL04 in correzione, gate13 ancora aperto. Installate tutte le19 figure VOL01 con etichette grandi; manifest e delta controllati aggiornati. Nuovo PDF necessario: nessuna pubblicabilità attestata.\n')
print('Fonti, topic, entità, indice e log aggiornati')
