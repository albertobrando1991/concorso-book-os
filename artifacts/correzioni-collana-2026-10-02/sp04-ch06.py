from pathlib import Path
import shutil
p=next(Path('wiki/books/moduli/m-sp04-prefettizia-diplomatica/chapters').glob('06-*.md'));a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp04-06.md');assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
t=t.replace('Le scadenze esterne impongono retromarcia.','Le scadenze esterne richiedono una pianificazione a ritroso.')
t=t.replace('quattro prove scritte portate a termine senza successo','quattro serie di prove scritte portate a termine senza superarle').replace('lo stesso limite dei quattro scritti completati','lo stesso limite delle quattro serie di scritti completate e non superate')
t=t.replace('costo strategico dei tentativi scritti completati','costo strategico delle serie di scritti completate e non superate')
t=t.replace('protegge anche i tentativi scritti completati','controlla anche il numero delle serie di scritti completate e non superate')
t=t.replace('Un orizzonte di sei-dodici mesi è soltanto un minimo operativo condizionato','Un orizzonte di sei-dodici mesi è uno scenario didattico condizionato').replace('Sei-dodici mesi possono rappresentare un minimo di pianificazione','Sei-dodici mesi possono rappresentare un orizzonte di pianificazione').replace('È un minimo operativo condizionato, da adattare.','È uno scenario didattico condizionato, da adattare.')
anchor='## N-SP04-11-04'
s=t.index(anchor)
t=t[:s]+'''### Due settimane realmente distribuibili

Gli esempi partono da candidati già in possesso delle basi disciplinari e dei requisiti. Non promettono di costruire da zero tutte le materie. Le ore sono nette di studio: riposo, pasti e spostamenti non sono inclusi né soppressi. Il margine resta disponibile per correzioni e imprevisti.

**Profilo A: prefettizia, 12 ore settimanali.**

| Giorno | Attività | Ore |
| --- | --- | ---: |
| lunedì | amministrativo/costituzionale: recupero e scaletta | 1,5 |
| martedì | lingua: testo e revisione | 1 |
| mercoledì | civile o storia, a rotazione, con domanda orale | 1,5 |
| giovedì | quiz nelle sei aree e analisi del punteggio | 1 |
| venerdì | lingua: recupero lessicale e conversazione | 1 |
| sabato | caso o elaborato parziale, alternati | 3 |
| domenica | correzione e retest | 1 |
| domenica | integrazioni orali e aggiornamento del piano | 1 |
| margine non assegnato | ritardo o approfondimento motivato | 1 |

Totale: 12 ore, di cui 11 assegnate. La rotazione deve coprire civile e storia in ogni ciclo di due settimane; l’amministrativo non assorbe tutte le tracce. Le tre ore del sabato producono un output parziale, non una simulazione da otto ore. Una volta ogni quattro settimane prepara una settimana speciale: riserva una finestra di otto ore a un elaborato completo, un’ora alla lingua, un’ora alla correzione, un’ora ai quiz/recupero e un’ora al margine. Totale ancora 12. Nel ciclo successivo sostituisci l’elaborato con un caso da sette ore e usa l’ora liberata per la correzione. Se non puoi mai ricavare una finestra completa, il limite è operativo e va risolto prima di dichiarare prontezza.

**Profilo B: diplomatica, 20 ore settimanali.**

| Giorno | Attività | Ore |
| --- | --- | ---: |
| lunedì | storia: recupero, tesi e fonti | 2 |
| martedì | diritto internazionale/UE | 2 |
| mercoledì | economia, secondo l’intero programma | 2 |
| giovedì | inglese: scritto e revisione | 2 |
| venerdì | seconda lingua: scritto e revisione | 2 |
| sabato | elaborato completo da cinque ore, a rotazione | 5 |
| domenica | correzione dell’elaborato | 1,5 |
| sessioni distribuite | ascolto e conversazione: 30 minuti per lingua | 1 |
| sessioni distribuite | attitudinale e logica con debrief | 1 |
| margine non assegnato | imprevisti o retest | 1,5 |

Totale: 20 ore, di cui 18,5 assegnate. Ogni terza settimana sostituisci il blocco da cinque ore con uno scritto linguistico da tre ore e due ore di integrazioni orali. Alterna inglese e seconda lingua; non usare la lingua forte per evitare la più debole. Le due ore delle sessioni ordinarie non simulano lo scritto ufficiale da tre ore: ne preparano e correggono i passaggi.

### Un orizzonte di sei o dodici mesi con verifiche

Per rendere il piano controllabile, usa cicli di quattro settimane; “sei mesi” indica qui circa 26 settimane, “dodici mesi” circa 52. Nel profilo A il budget nominale a 12 ore è 312 ore in 26 settimane; nel profilo B a 20 ore è 520. Non sono soglie di riuscita: assenze e qualità del lavoro modificano il risultato. In dodici mesi i budget nominali raddoppiano, ma il progresso non è automaticamente proporzionale.

**Settimane 1–2:** verifica requisiti, scadenze e opzioni linguistiche; acquisisci un campione per ogni formato e misura le ore realmente sostenibili. **Settimane 3–8:** costruisci le aree deboli, produci scalette e sezioni, mantieni entrambe le lingue nel profilo B e caso più lingua nel profilo A. Al controllo della settimana 8 devono esistere campioni corretti, non solo letture. **Settimane 9–16:** aumenta le prove intere, ruota le materie e chiudi il feedback entro il ciclo seguente. Alla settimana 16 individua la prova peggiore e verifica se il difetto si trasferisce anche a tracce nuove. **Settimane 17–22:** accosta due prove complete in giorni vicini, se sostenibile, e campiona l’orale con lingua e pratica informatica. **Settimane 23–26:** consolida e valuta la partecipazione con i minimi individuali; riduci il nuovo materiale soltanto se il calendario ufficiale rende prossima la prova.

Per dodici mesi aggiungi, dopo la diagnosi, circa sei cicli di quattro settimane dedicati ai fondamenti e alla produzione progressiva, senza rinviare lingue e primi scritti. Ripeti il controllo ogni quattro settimane: se le ore effettive restano sotto l’80% del budget per tre settimane, ricalcola il carico; se tre campioni nuovi ripetono lo stesso errore, cambia intervento o feedback. Queste soglie sono regole personali di gestione, non criteri ministeriali. Una data d’esame anticipata non autorizza a comprimere sei cicli in uno: richiede una nuova decisione sul rischio.

**Settimana minima per imprevisti:** nel profilo A quattro ore, una per lingua, una per recupero, una per un pezzo di caso e una per correzione/avvisi; nel profilo B sei ore, una per ciascuna lingua, due per contenuti e produzione breve, una per recupero, una per correzione/avvisi. Mantiene continuità per poco tempo, senza pretendere di mantenere il ritmo del piano normale. Dopo due settimane minime consecutive, rifai il calendario sulle disponibilità reali.

'''+t[s:]
p.write_text(t,encoding='utf8')
