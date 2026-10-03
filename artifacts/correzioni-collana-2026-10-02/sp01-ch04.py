from pathlib import Path
import re,shutil
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/04-accertamenti-preparazione.md');t=p.read_text(encoding='utf-8');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp01-04.md');assert not a.exists();shutil.copyfile(p,a)
t=t.replace("resta una fonte rilevante per l'idoneità psichica e attitudinale, mentre è stato superato soltanto il requisito di statura", "conserva nel proprio ambito Polizia di Stato requisiti fisici e sanitari, psichici e attitudinali; la riforma della statura non abroga tutto il regolamento")
t=t.replace("resta fonte per i requisiti di idoneità psichica e attitudinale per l'accesso ai ruoli della Polizia di Stato", "conserva gli altri requisiti fisici e sanitari oltre a quelli psichici e attitudinali per la Polizia di Stato")
t=t.replace("resta rilevante per idoneità psichica e attitudinale", "conserva anche altri requisiti fisici e sanitari, psichici e attitudinali della Polizia di Stato")
t=t.replace("in particolare per idoneità psichica e attitudinale", "compresi gli altri requisiti fisici e sanitari della Polizia di Stato")
t=t.replace("Il d.m. Interno 30 giugno 2003, n. 198, resta rilevante anche per questa area", "Per la Polizia di Stato il d.m. Interno 30 giugno 2003, n. 198, resta rilevante anche per questa area")
t=t.replace("Il d.m. 198/2003 resta rilevante per l'idoneità attitudinale.", "Il d.m. 198/2003 riguarda la Polizia di Stato; gli altri corpi applicano la propria disciplina.")
start=t.index('La distinzione più importante è tra struttura');end=t.index('Il doppio binario base/ispettivo',start)
t=t[:start]+'''La struttura indica quali esercizi svolgere e quali conseguenze produce il mancato superamento; la tabella tecnica specifica soglie, sesso, tentativi e modalità. Entrambe servono. Un esempio completo, nel binario ispettivo, è il bando GdF per **983 allievi marescialli del 2026**, articolo 14 e allegato 4. Il candidato deve scegliere il proprio contingente: una differenza negli obbligatori cambia ciò che deve superare per proseguire.

| Contingente | Obbligatori | Una facoltativa, scelta in domanda |
| --- | --- | --- |
| Ordinario | Salto in alto, corsa 1.000 metri, piegamenti sulle braccia | Corsa 100 metri oppure nuoto 25 metri stile libero |
| Mare | Salto in alto, corsa 1.000 metri, nuoto 25 metri stile libero | Corsa 100 metri oppure piegamenti sulle braccia |

**Regola dell’esempio, verificata il 3 ottobre 2026.** Un solo obbligatorio sotto il minimo determina inidoneità ed esclusione. Il mancato minimo nella facoltativa non elimina l’idoneità già conseguita. Non si sceglie liberamente una facoltativa il giorno della prova: la richiesta deve essere stata formulata nella domanda. Soglie e modalità esecutive si leggono nell’allegato 4 di questo bando, non in quello di un concorso per ufficiali.

I punti delle prestazioni non entrano nella graduatoria senza conversione. L’articolo 14 prevede queste fasce: 1–2 punti danno 0,05; 2,5–3,5 danno 0,10; 4–5 danno 0,15; 5,5–6,5 danno 0,20; 7–8 danno 0,25; 8,5–9,5 danno 0,30; 10–11 danno 0,35; 11,5–12 danno 0,40. Non si interpola un valore fra le fasce e non si somma direttamente il punteggio sportivo al voto culturale.

**Caso risolto.** Marco, contingente ordinario, supera tutti e tre gli obbligatori e raggiunge 7 punti complessivi secondo le tabelle. Non supera la facoltativa richiesta. Conserva l’idoneità e, sui dati del caso, riceve 0,25 di maggiorazione. Se invece fallisce il minimo in un obbligatorio, non può compensare con i 7 punti ottenuti altrove: viene escluso. L’obbligatorio è una condizione, il bonus una componente di punteggio.

''' +t[end:]
needle='**Caso ragionato.** Elena riceve la convocazione'
pos=t.index(needle)
t=t[:pos]+'''### Due esempi di documentazione

Nel bando GdF 983 del 2026, art. 14, serve un certificato in corso di validità di idoneità all’attività sportiva agonistica per l’atletica leggera o altro sport della tabella B del D.M. 18 febbraio 1982, rilasciato da specialista in medicina dello sport abilitato. Non è equivalente un generico certificato non agonistico. L’articolo disciplina originale, copia conforme e alternative di consegna: una scansione inviata informalmente non sostituisce quelle modalità.

Per le candidate il medesimo bando richiede il test di gravidanza effettuato non prima di cinque giorni dall’effettivo svolgimento delle prove e prevede una specifica disciplina di rinvio in caso di gravidanza. Non si può dedurre da questa disposizione un generale diritto a rinviare qualsiasi prova per qualsiasi impedimento.

Nel bando Carabinieri 898 del 2026, art. 10, il certificato agonistico per atletica leggera va presentato valido, in originale e con fotocopia; il referto di gravidanza deve rispettare il periodo di cinque giorni antecedenti, escludendo dal conteggio il giorno di presentazione. Il testo collega determinate irregolarità all’esclusione: le regole non vanno ricopiate dalla procedura GdF.

**Controllo applicato.** Convocazione ipotetica il 15 ottobre e certificato con validità terminata il 14: la data di emissione corretta non basta, perché alla prova il certificato non è più valido. Il candidato deve ottenere una certificazione conforme entro il momento richiesto e secondo i canali ammessi. Una prenotazione medica non è un certificato e non costituisce, da sola, una proroga del termine.

''' +t[pos:]
t=t.replace("C. Resta fonte per idoneità psichica e attitudinale, mentre è stato superato il requisito di statura.","C. Conserva altri requisiti fisici, psichici e attitudinali della Polizia di Stato, nel proprio ambito.")
t=t.replace("La riforma ha superato il requisito di statura, ma non ha cancellato l'intero impianto relativo all'idoneità psichica e attitudinale.","La riforma della statura non abroga il regolamento né lo estende agli altri corpi. A e B cancellano erroneamente l’intero atto; D confonde salute e prestazione sportiva.")
start=t.index('4. Perché un allegato tecnico acquisito');end=t.index('5. Qual è',start)
t=t[:start]+'''4. Nel bando GdF 983 del 2026, Marco supera tutti gli obbligatori e consegue 7 punti fisici. Fallisce la facoltativa. Quale esito segue, sui dati indicati?

A. Esclusione automatica per la facoltativa.
B. Sette punti aggiunti direttamente alla graduatoria.
C. Idoneità conservata e maggiorazione di 0,25.
D. Obbligo di scegliere una seconda facoltativa sul posto.

**Risposta corretta: C.** La fascia 7–8 converte il punteggio in 0,25. A tratta la facoltativa come obbligatoria; B omette la conversione; D inventa una scelta non consentita dall’articolo 14.

''' +t[end:]
pos=t.index('## ▣ Verifica 04.B')
t=t[:pos]+'''7. Un certificato agonistico scade il giorno precedente alla prova che lo richiede in corso di validità. La prenotazione di una nuova visita è sufficiente?

A. Sì, perché prova l’intenzione di regolarizzarsi.
B. No: serve il documento valido secondo tempi e modalità della procedura.
C. Sì, purché la prova scritta sia stata superata.
D. Il certificato non è necessario per chi si allena regolarmente.

**Risposta corretta: B.** La prenotazione non dimostra idoneità agonistica e non proroga il termine. A confonde intenzione e adempimento; C e D attribuiscono effetti estranei al requisito documentale.

''' +t[pos:]
t=t.replace('- Bandi, allegati tecnici, procedure e disposizioni ufficiali delle specifiche tornate concorsuali di Polizia di Stato, Arma dei Carabinieri e Guardia di Finanza.','- Bando GdF 983 allievi marescialli 2026, art. 14 e allegato 4; bando Carabinieri 898 allievi marescialli 2026, art. 10. Esempi datati, da confrontare con la propria procedura.')
p.write_text(t,encoding='utf-8');print('SP01/04: protocollo ispettivo, certificati, casi e quiz')
