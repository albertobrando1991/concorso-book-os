from pathlib import Path
import json,re
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-07')
p=Path('wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/10-procurement-farmaci-dispositivi-magazzino.md');t=p.read_text(encoding='utf8');ref='sources/vol-09-consip-strumenti-obblighi-2026-10-03'
for key in ['source_refs','last_compiled_from']:
 t=re.sub(r'^'+key+r': \[(.*?)\]',lambda m:key+': ['+m.group(1)+', "'+ref+'"]',t,count=1,flags=re.M)
anchor='**Esempio:** il servizio acquisti rileva un fabbisogno annuale di medicinali.'
assert anchor in t
t=t.replace(anchor,'''Il **D.P.C.M. 11 febbraio 2026**, pubblicato il 16 aprile 2026, aggiorna le categorie e le soglie del regime dei soggetti aggregatori, sostituendo il decreto del 2018. Per esempio, per farmaci e vaccini la soglia è 40.000 euro; altre categorie seguono la soglia europea prevista per le amministrazioni subcentrali. Non applicare un solo importo a tutti gli acquisti sanitari. L’art. 1, comma 2, considera l’importo massimo annuo per categoria e, per gare pluriennali, l’intero periodo. Il mancato rilascio del CIG previsto per questo regime decorre dall’attivazione del contratto del soggetto aggregatore: categoria, importo e stato dello strumento vanno quindi verificati insieme. Questo aggiornamento non elimina gli altri obblighi di acquisto centralizzato.

'''+anchor,1);p.write_text(t,encoding='utf8')
p=R/'14-moduli-m-sa04-tecnici-sanitari-prevenzione.md';t=p.read_text(encoding='utf8');t=t.replace('Grafico QC richiesto al coordinatore per V07-35; testo e dati pronti.','Grafico QC inserito nel capitolo 02; resa del nuovo PDF da controllare.').replace('Specifica pronta; inserimento a cura del coordinatore | Aperto','Due apparati inseriti con didascalie, domande e soluzioni; originali verificati dal coordinatore, PDF pendente | Applicato')
a=t.index('Restano da documentare esplicitamente');b=t.index('\n\n## 7.',a)
t=t[:a]+'Accesso Normattiva risolto: artt. 146 e 166 del D.Lgs. 101/2020 acquisiti e letti nel consolidato. I tre apparati V07-35/39 sono inseriti nei capitoli; rimane da verificarne la composizione nel nuovo PDF.'+t[b:];p.write_text(t,encoding='utf8')
print('Aggiornamento procurement 2026 inserito e report14 SA04 allineato.')
