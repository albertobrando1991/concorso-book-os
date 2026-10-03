from pathlib import Path
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters')
repl={
'non elenca tutte le prestazioni e non pretende di aggiornare dati che cambiano nel tempo':'seleziona le principali prestazioni e distingue le regole strutturali dai dati riferiti al 2026',
'l’uso del mezzo privato deve essere necessitato nei termini previsti.':'l’uso del mezzo privato deve essere necessitato nei termini previsti. Per il velocipede la legge considera l’uso sempre necessitato, fermi gli altri presupposti della tutela.',
'l\'uso del mezzo privato deve essere necessitato nei termini previsti.':'l’uso del mezzo privato deve essere necessitato nei termini previsti. Per il velocipede la legge considera l’uso sempre necessitato, fermi gli altri presupposti della tutela.',
'"topics/epne-previdenza-assicurazione-rettifiche-2026.md"':'"epne-previdenza-assicurazione-rettifiche-2026"',
}
for p in B.glob('*.md'):
 s=p.read_text(encoding='utf8')
 for a,b in repl.items():s=s.replace(a,b)
 p.write_text(s,encoding='utf8')
source=Path('wiki/sources/epne-previdenza-assicurazione-rettifiche-2026-10-03.md');s=source.read_text(encoding='utf8')
s+='''
## Riscontri integrativi del riesame

- [Testo art. 13 richiamato in Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2016-09-24%3B185~art5=): trenta giorni per sanare e quindici per il pagamento agevolato dopo la scadenza, nel regime generale; non estendere a violazioni con disciplina speciale.
- [DPR 1124/1965, art. 2](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Apresidente.repubblica%3Adecreto%3A1965-06-30%3B1124~art2=), con il riscontro istituzionale [ISPRA sulla mobilità in bicicletta](https://www.isprambiente.gov.it/it/servizi/mobilita-sostenibile/mobilita-in-bicicletta): l'uso del velocipede è sempre considerato necessitato; non elimina gli altri presupposti dell'in itinere.
- [DL 92/2024, art. 9](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=9&atto.articolo.sottoArticolo=1&atto.articolo.tipoArticolo=0&atto.codiceRedazionale=24G00111&atto.dataPubblicazioneGazzetta=2024-07-04): fonte dell'art. 314-bis. Le proposte parlamentari del 2026 individuate nel controllo non sono trattate come legge approvata.

## Copie acquisite

Tre documenti ufficiali sono conservati immutabili in `wiki/raw/correzioni-fc03-2026-10-03/`: `inl-circolare-6-2020.pdf`, `ccnq-2025-2027.pdf`, `inps-preventivo-2026.pdf`. Il manifest con hash è negli artefatti di correzione. Lettura puntuale: circolare INL quattro pagine; CCNQ elenchi del comparto; preventivo INPS frontespizio, basi legali e competenze. Non è dichiarata una lettura integrale delle tavole economiche del preventivo.
'''
source.write_text(s,encoding='utf8')
raw=[]
for p in Path('wiki/raw/correzioni-fc03-2026-10-03').glob('*.pdf'):raw.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':p.stat().st_size})
(A/'FC03-raw-manifest.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2),encoding='utf8')
for name in ['m-fc03-dossier-redazionale-enti-pubblici-non-economici.md','m-fc03-fonti-ufficiali-enti-epne-2026.md','m-fc03-inl-vigilanza-lavoro-previdenziale.md']:
 p=Path('wiki/sources')/name;s=p.read_text(encoding='utf8')
 s+='\n## Rettifica puntuale del 3 ottobre 2026\n\nPer natura degli enti, comparti, organi, contabilità, prestazioni e vigilanza prevalgono i riscontri specifici di [[sources/epne-previdenza-assicurazione-rettifiche-2026-10-03]] e il topic [[topics/epne-previdenza-assicurazione-rettifiche-2026]]. Le precedenti pagine indice documentavano i canali, non tutte le nozioni sostanziali. CRI è associazione privata dal 2016; ISTAT, ENEA e ASI mantengono Istruzione e Ricerca anche nei profili amministrativi. Per vigilanza leggere il d.lgs. 149/2015 con le modifiche del 2024 e la diffida accertativa riformata nel 2020. La raccolta storica è conservata per tracciabilità, senza attribuirle conferme non svolte.\n'
 p.write_text(s,encoding='utf8')
extract=[]
for p in sorted(B.glob('*.md')):
 for i,line in enumerate(p.read_text(encoding='utf8').splitlines(),1):
  if re.search(r'67 anni|71 anni|tredici settimane|meno di un terzo|314-bis|323|velocipede|6%|16%|20 anni|2025–2027|CIV|articolo 13|sessanta giorni|trenta giorni|legge 222|445-bis|21 ottobre|CONI richiama|Istruzione e Ricerca',line):extract.append(f'{p.name}:{i}: {line}')
(A/'FC03-claims-extract.txt').write_text('\n'.join(extract),encoding='utf8')
print(len(extract),'righe di riscontro; manifest raw e rettifiche fonti scritti.')
