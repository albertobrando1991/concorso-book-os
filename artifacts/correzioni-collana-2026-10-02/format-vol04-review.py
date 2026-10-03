from pathlib import Path
p=Path('wiki/reviews/pipeline/VOL-04/13-moduli-m-fc04-giustizia.md')
lines=p.read_text('utf-8').splitlines(); out=[]
for line in lines:
 if line.startswith('|ID|'):
  out.append('| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |')
 elif line=='|---|---|---|---|---|':out.append('|---|---|---|---|---|---|---|')
 elif line.startswith('|V04-'):
  cells=line.strip('|').split('|'); assert len(cells)==5
  out.append('| '+' | '.join([cells[0],cells[1],'Contenuto e didattica',cells[2],cells[3],cells[4],'Aperto'])+' |')
 else:out.append(line)
p.write_text('\n'.join(out)+'\n','utf-8')
