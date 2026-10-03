from pathlib import Path
import json
R=Path('wiki/reviews/pipeline/VOL-07');state=json.loads(Path('artifacts/correzioni-collana-2026-10-02/VOL-07-changes.json').read_text(encoding='utf8'))['changes']
modules=[('M-SA02','m-sa02-professioni-sanitarie',list(range(14,28))+[29]),('M-SA03','m-sa03-dirigenza-medica-sanitaria',list(range(28,35))+[41]),('M-SA04','m-sa04-tecnici-sanitari-prevenzione',[28,29]+list(range(35,42)))]
for code,m,ids in modules:
 p=R/f'14-moduli-{m}.md';a=R/'archive'/('pre-correzioni-'+p.name)
 if p.exists() and not a.exists():a.write_bytes(p.read_bytes())
 rows=[]
 for n in ids:
  key=f'V07-{n:02}';x=state.get(key,{})
  rows.append('| '+' | '.join([key,', '.join(Path(f).name for f in x.get('files',[])) or 'SA04/03','Correzione dell’audit','Media' if n==39 else 'Come audit storico',x.get('change','Due apparati originali con domanda e soluzione'),x.get('evidence','Specifica pronta; inserimento a cura del coordinatore'), 'Aperto' if n==39 else 'Applicato'])+' |')
 text=f'''# {code} — Correzioni dopo l’audit integrale

## 1. Sintesi editoriale

Applicate le correzioni testuali autorizzate del modulo, con definizioni, distinzioni, esempi e soluzioni effettivamente presenti. La lettura integrale diagnostica precedente resta documentata nell’audit del 2 ottobre; questa revisione riguarda i delta e i raccordi. Non viene dichiarata una nuova lettura integrale del testo invariato.

## 2. Punti applicati della checklist

Riesame dei punti 1–26 e 28–30 pertinenti alle modifiche: destinatario, copertura, autonomia, definizioni, coerenza normativa, esempi, casi, quiz, lingua, fonti e rinvii. Punto 27 da verificare sui nuovi PDF. Controllo Humanizer e micro-revisione eseguiti sui delta: frasi concrete, responsabilità esplicite, dati didattici separati dagli standard, nessuna istruzione interna aggiunta alla prosa pubblica.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+f'''

## 4. Osservazioni per capitolo

Il dettaglio per capitolo, con file e hash, è nel [[reviews/correzioni-collana-2026-10-02/VOL-07|registro correzioni]]. Le nuove verifiche hanno soluzione; i calcoli didattici sono stati rieseguiti. Per SA02 sono distinti casi clinici non esecutivi e procedure giuridiche; per SA03 obbligo generale e modalità del concorso; per SA04 indicatori, dosi, rischio e competenze.

## 5. Coerenza globale

Raccordati frontmatter, topic e matrice. Le attestazioni precedenti nelle matrici sono esplicitamente storicizzate rispetto ai delta correnti. Il totale del volume è 45 righe: 12 SA01, 15 SA02, 9 SA03 e 9 SA04. Il conteggio non attesta completezza. Preservate le integrazioni INT e i ruoli distinti dei profili.

## 6. Contenuto da verificare

Lo step 15 riesamina i claim specialistici modificati e le parti mobili. Gli errori delle fonti risolti comprendono codice CNOP e copia NSG valida. Le risposte challenge non sono classificate come fonti. Restano da documentare esplicitamente i limiti dei consolidati Normattiva non accessibili; i riscontri alternativi sono indicati nelle source. {'Per SA04 restano aperti V07-39 e il grafico QC di V07-35: testo, dati, domanda e soluzione sono pronti nella specifica apparati, ma nessuna immagine è simulata come presente.' if code=='M-SA04' else 'Nessun errore testuale noto viene rinviato a una futura persona; il prossimo passaggio è l’audit automatico specialistico.'}

## 7. Suggerimenti facoltativi

Non applicati ampliamenti estranei ai rilievi obbligatori.

## 8. Priorità degli interventi

Riesame specialistico, eventuali correzioni conseguenti, apparati, nuovo freeze, PDF e controllo visivo. La conferma conclusiva umana resta allo step 24.

## 9. Giudizio di pubblicabilità

Correzioni testuali applicate. Nessuna dichiarazione di pubblicabilità del modulo o del volume prima degli audit e dei nuovi PDF. Il gate formale del report non certifica norme, pratica clinica o resa tipografica.

## 10. Limiti di questa revisione

Riscontri normativi e scientifici selettivi sui claim effettivamente insegnati; nessuna validazione di procedure aziendali, pazienti o apparecchiature reali. Revisioni storiche immutate e copie dei report precedenti archiviate. Stato analitico nel registro correzioni; stato operativo esclusivamente nel CLI.
'''
 p.write_text(text,encoding='utf8')
print('Report 14 dei tre moduli scritti, SA04 con apparati esplicitamente aperti.')
