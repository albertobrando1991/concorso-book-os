from pathlib import Path
import json
A=Path(__file__).parent;p=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-01-schemi-nativi.md')
s=p.read_text(encoding='utf8');m=json.loads((A/'VOL-01-native-pdf-map.json').read_text(encoding='utf8'));f=json.loads((A/'VOL-01-native-layout-findings.json').read_text(encoding='utf8'))
s=s.replace('La verifica della nuova impaginazione è in corso.','Sono state esaminate 194 pagine selezionate della terza prova, distribuite in 49 tavole: coprono tutti i 133 schemi e tutte le 19 figure. La leggibilità è adeguata; restano 20 raccordi tra titolo e corpo dello schema da correggere nel motore di impaginazione.')
lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('| F'):
  ident=line.split('|')[1].strip();r=next(x for x in m['native'] if x['id']==ident)
  evidence='PDF 670 pagine, pp. '+', '.join(map(str,r['pages']))+'; lettura visiva completata.'
  outcome='Applicato e leggibile; raccordo titolo-corpo pendente.' if r['layoutFinding'] else 'Applicato; verifica visiva superata.'
  lines[i]=line.replace('Originale e semantica verificati; impaginato in verifica.',evidence).replace('Applicato; PDF pendente.',outcome)
s='\n'.join(lines)+'\n'
s=s.replace('Completare la verifica visiva del PDF rigenerato su tutte le sostituzioni e sulle 19 immagini conservate. Ricontrollare il raccordo tra mini-esercizio e griglia nel capitolo 19.','Correggere i 20 raccordi titolo-corpo elencati sotto, rigenerare la prova e controllare le pagine interessate. Il mini-esercizio del capitolo 19 è ora completo di titolo, introduzione e griglia a pagina 459. Il rinvio «Le percentuali dell’esempio precedente» è verificato a pagina 478. Due domande isolate sono state corrette con «Perché» iniziale dopo questa prova e richiedono il nuovo export.\n\n| Apparato | Pagina del titolo | Pagina del corpo | Stato |\n|---|---|---|---|\n'+'\n'.join('| '+', '.join(r['ids'])+' | '+str(r['page'])+' | '+str(r['nextPage'])+' | Raccordo pendente nel renderer. |' for r in f['findings'])+'\n\nSono stati osservati anche raccordi analoghi, preesistenti, alle pagine 394, 462, 476, 492 e 537. Non si rilevano tagli o sovrapposizioni nelle 194 pagine esaminate.')
s=s.replace('Non è ancora attestata la qualità della nuova impaginazione;','Leggibilità, integrità dei contenuti degli apparati e conservazione delle 19 immagini sono verificate nella prova esaminata. I raccordi residui impediscono di chiudere la revisione grafica;')
s=s.replace('I controlli DOM e il PDF hanno mostrato una differenza di paginazione: la mappa degli apparati viene quindi costruita sul PDF effettivo, non sulle sole metriche del browser.','La terza prova conta 670 pagine sia nel DOM sia nel PDF. La mappa deriva dal PDF effettivo. La copertura visiva è di 194 pagine mirate, non una rilettura integrale delle 670 pagine. Il registro delle tavole e la mappa indicano esattamente la copertura. I raccordi residui sono in `VOL-01-native-layout-findings.json`, con hash della prova. Le due correzioni di maiuscole successive non sono ancora presenti in questo PDF.')
p.write_text(s,encoding='utf8');print(p)
