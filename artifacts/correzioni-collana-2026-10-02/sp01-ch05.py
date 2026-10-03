from pathlib import Path
import shutil
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/05-prova-orale-titoli-lingua.md');t=p.read_text(encoding='utf-8');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp01-05.md');assert not a.exists();shutil.copyfile(p,a)
t=t.replace('Inglese è più competitivo, ma lei riesce già a rispondere con frasi complete.','Nelle simulazioni di inglese riesce già a rispondere con frasi complete; il numero di altri candidati che scelgono la lingua non dimostra da solo un vantaggio o uno svantaggio.')
t=t.replace('Luca prepara un concorso del binario ispettivo. Ha già superato le prove precedenti e deve organizzare la fase finale.','Luca prepara un concorso del binario ispettivo prima della scadenza della domanda. Legge subito anche le regole delle fasi finali, perché alcune scelte e dichiarazioni devono essere effettuate ora.')
t=t.replace('Corregge la domanda e conserva la documentazione.','Il titolo è già posseduto alla data richiesta. Luca corregge la domanda entro il termine, con annullamento e nuovo invio se questa è la modalità prevista, e salva la ricevuta definitiva. Non attende di superare le prove per dichiararlo.')
t=t.replace('La lezione del caso è chiara: la fase finale non si improvvisa. Si governa con tre schede separate, una per il colloquio, una per i titoli e una per la lingua.','Dopo il superamento delle prove Luca aggiorna il calendario dell’orale e produce i documenti eventualmente richiesti, senza supporre di poter aggiungere retroattivamente titoli o cambiare lingua. Possesso, dichiarazione e documentazione hanno scadenze distinte: un documento rilasciato dopo può provare un fatto già esistente, ma non crea retroattivamente il titolo mancante.')
pos=t.index('La seconda regola è distinguere tra lingua obbligatoria')
t=t[:pos]+'''Un confronto concreto evita equivoci. Nel bando PS 1.000 vice ispettori del 2026, art. 8, l’orale comprende l’accertamento obbligatorio dell’inglese, con traduzione dall’inglese all’italiano senza dizionario e conversazione, oltre all’informatica. Non puoi rinunciarvi perché preferisci un’altra lingua. Il bando GdF 983 marescialli distingue invece l’orale dalla prova facoltativa di lingua, con opzioni inglese, francese, tedesco e spagnolo. Prima di usare una regola di convenienza, verifica dunque se esista davvero una scelta.

''' +t[pos:]
t=t.replace('Se il corpus di una procedura documenta lingue','Se il bando di una procedura prevede lingue').replace('Quando il corpus documenta opzioni','Quando il bando prevede opzioni')
pos=t.index('## ▣ Verifica 05.B')
t=t[:pos]+'''7. Luca ha già superato lo scritto e scopre di non aver dichiarato un titolo che il bando richiedeva di indicare entro la scadenza. Può presumere di aggiungerlo ora?

A. Sì, ogni documento è sempre integrabile dopo le prove.
B. Sì, se il titolo appare prestigioso.
C. No: deve distinguere dichiarazione omessa e successiva prova documentale e verificare la disciplina applicabile.
D. Sì, basta modificare una copia locale della domanda.

**Risposta corretta: C.** La documentazione successiva non equivale automaticamente a una nuova dichiarazione tempestiva. A cancella la scadenza; B sostituisce il bando con una valutazione personale; D non produce un invio valido.

''' +t[pos:]
p.write_text(t,encoding='utf-8');print('SP01/05 corretto')
