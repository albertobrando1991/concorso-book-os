from pathlib import Path
import re
p=Path('wiki/books/moduli/m-ir03-enti-ricerca/chapters/12-laboratorio-quattro-profili.md');t=p.read_text(encoding='utf8')
old=t.split('## Caso comune del laboratorio\n',1)[1].split('\n### ',1)[0]
new='''Un EPR partecipa a un progetto con partner. L'attrezzatura doveva arrivare il 1° giugno e arriva il 15. Il progetto termina il 30 settembre; il deliverable sperimentale è dovuto il 31 luglio. Servono due settimane di installazione e verifica, poi quattro di misure e una di analisi. Il contratto ammette costi effettivi per attività svolte entro il termine, con possibilità di fatture successive per debiti già sorti nel periodo. La variazione della scadenza del deliverable richiede approvazione del finanziatore; non è ancora concessa.

Sono assegnati tre costi, tutti pertinenti e documentalmente regolari salvo il requisito temporale da valutare: servizio A da 5.000 euro completato il 28 settembre e fatturato il 5 ottobre; servizio B da 3.000 eseguito il 10 ottobre; fornitura C da 20.000 consegnata e accettata il 30 giugno. Il partner può accedere ai risultati preliminari solo dopo validazione e autorizzazione del responsabile di progetto, secondo l'accordo fornito. Non vi sono dati personali. Per il collaudo si usa il requisito del capitolo 8: 1.000 record, 980 validi e 20 incompleti, massimo 60 secondi e nessuna perdita di validi.

Queste clausole e cifre sono dati della simulazione, non regole universali di finanziamento. Produci quattro elaborati distinti usando gli stessi fatti. Quando la traccia assegna una condizione, applicala; quando manca, dichiara il limite senza inventare un atto già adottato.
'''
t=t.replace(old,new)
blocks={
2:'''**Elaborato A — Piano scientifico, 20 minuti, massimo 250 parole.** Pianifica attività, output e rischio del ritardo senza modificare autonomamente il contratto.

**Soluzione svolta.** Installazione e verifica: 15–28 giugno; misure: 29 giugno–26 luglio; analisi: 27 luglio–2 agosto. Con le durate assegnate, l'esito completo arriva dopo il 31 luglio: la consegna del deliverable non è assicurata. Si verifica se una preparazione documentale parallela possa recuperare tempo senza ridurre qualità e si segnala subito al responsabile del progetto il bisogno di chiedere la modifica prevista. Non si dichiara già autorizzato il 2 agosto. Il piano conserva disegno, criteri di qualità e registro dei dati; se si propone un metodo alternativo, ne motiva equivalenza e limiti prima di usarlo. I risultati preliminari restano interni fino alla validazione e all'autorizzazione richiesta per l'accesso del partner.

**Evidenza da consegnare:** calendario con dipendenze, nota sullo scostamento e criterio di riesame. È un errore critico retrodatare le misure o presentare come ottenuto un risultato soltanto atteso.
''',
3:'''**Elaborato B — Verbale tecnico, 20 minuti.** Il test dura 48 secondi: importa 978 record validi e respinge 22 record, due dei quali erano validi. Valuta l'esito e indica la prova successiva.

**Soluzione svolta.** La soglia temporale è rispettata, ma il requisito di completezza fallisce: mancano due validi. Il verbale registra configurazione, versione, input, conteggi, durata e identificativi dei due scarti errati. Si apre un'anomalia sul parser, si conserva il log e si propone la correzione; dopo il cambiamento si ripete l'intero set, verificando 980 accettati, 20 respinti motivatamente e durata entro 60 secondi. Non basta rieseguire i due record errati: il cambiamento può compromettere casi precedentemente corretti. Il verbale propone esito non conforme nel perimetro del requisito, senza decidere da solo penalità contrattuali.

**Evidenza da consegnare:** tabella requisito–risultato–esito e sequenza di correzione/riprova. Definire «collaudo positivo» perché 48 è minore di 60 è un errore critico.
''',
4:'''**Elaborato C — Nota istruttoria, 20 minuti, massimo 180 parole.** Esamina i tre costi per il requisito temporale e prepara la proposta al soggetto competente.

**Soluzione svolta.** «A riguarda un servizio completato il 28 settembre: il contratto consente fattura successiva per debito sorto nel periodo, quindi i 5.000 euro superano il requisito temporale. B riguarda attività del 10 ottobre, successiva al 30 settembre: i 3.000 euro sono esclusi in base alla clausola data. C, consegnata e accettata il 30 giugno, supera il controllo temporale per 20.000 euro. Le altre condizioni sono dichiarate regolari nella traccia. Si propone pertanto ammissione di 25.000 euro ed esclusione di 3.000, con prospetto e documenti a supporto, rimettendo la decisione al soggetto competente». La data della fattura A non basta per escluderla; il pagamento di B non renderebbe ammissibile un'attività fuori periodo.

**Evidenza da consegnare:** tre righe di riconciliazione, clausola applicata, motivazione e proposta. Nessuna data viene corretta per far rientrare il servizio B.
''',
5:'''**Elaborato D — Scheda grant, 20 minuti.** Collega ritardo, scadenza, costi e accesso ai risultati in una richiesta di decisione.

**Soluzione svolta.** Scostamento: disponibilità completa dei risultati il 2 agosto rispetto al 31 luglio. Azione: informare il responsabile di progetto e predisporre richiesta motivata di modifica al finanziatore, con cronoprogramma e conseguenze; stato della modifica: non approvata. Budget/rendiconto: 25.000 euro superano il controllo assegnato, 3.000 restano esclusi; la modifica del deliverable non proroga automaticamente il termine del progetto né sana il costo B. Accesso partner: predisporre pacchetto validato e chiedere autorizzazione prevista; nessun invio anticipato solo perché il partner partecipa al progetto. Rischio residuo: mancata approvazione o impossibilità di recupero; mantenere il confronto sulle opzioni consentite senza aggiornare silenziosamente l'accordo.

**Griglia comune, 10 punti per elaborato.** Uso corretto dei fatti 2; applicazione delle clausole e rispetto del ruolo 3; calcoli o ragionamento tecnico 2; evidenze e rischi 2; chiarezza 1. Obiettivo didattico almeno 7 punti, con correzione obbligatoria degli errori critici: falso esito di collaudo, retrodatazione, costo estraneo al periodo o diffusione non autorizzata. La soglia appartiene a questa simulazione e non a un bando reale. Confronta le quattro soluzioni: stessi fatti, documenti diversi, decisioni coordinate.
'''}
for n,b in blocks.items():t=re.sub(rf'(^### N-IR03-12-{n:02}[^\n]*\n)',lambda m:m[1]+'\n'+b+'\n',t,count=1,flags=re.M)
t=t.replace('Se una colonna resta vuota, non la riempie con ipotesi: la segnala come dato da acquisire.','Se una colonna riguarda un fatto non noto, lo segnala come dato da acquisire; una scelta proposta può invece essere formulata come ipotesi esplicita e motivata.')
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M).replace('draft_stage: text_frozen','draft_stage: correction-in-progress').replace('review_required: false','review_required: true');p.write_text(t,encoding='utf8')
print('IR03 laboratorio quattro elaborati applicato')
