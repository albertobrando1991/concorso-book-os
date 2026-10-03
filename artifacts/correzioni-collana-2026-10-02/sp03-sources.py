from pathlib import Path
import re,shutil
p=Path('wiki/sources/bandi-magistratura-avvocatura-notariato-m-sp03.md');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-source-sp03.md');assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
t=re.sub(r'^checked_at:.*$','checked_at: 2026-10-03',t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
t=t.replace('non meno di **6/10 in ciascuna materia della prova orale** e votazione complessiva non inferiore a **108 punti** per l\'idoneità.','non meno di **6/10 nelle materie orali valutate numericamente**, giudizio di sufficienza nel colloquio di lingua straniera e votazione complessiva nelle due prove non inferiore a **108 punti**; frazioni non ammesse. Art. 8, PDF p. 10, riletto il 3 ottobre 2026.')
t=t.replace('Trentacinque anni non compiuti.','Formula del bando: non aver superato il trentacinquesimo anno, alla scadenza. D.P.C.M. 141/2000, art. 1, modificato nel 2011: trentacinque. Computo ed eventuali elevazioni vanno tenuti distinti; vedere il riscontro sotto.')
t=t.replace('### 3. Le date rendono i binari mutuamente esclusivi nello stesso anno','### 3. Date ravvicinate e sostenibilità personale')
t=t.replace('sostenerle entrambe nella stessa tornata non è una strategia: è una scelta che compromette entrambe.','sostenerle entrambe richiede una verifica concreta di preparazione, recupero e logistica. Non sono date coincidenti e non ne deriva un divieto né una compromissione inevitabile.')
t=t.replace('Il binario B è di due ordini di grandezza più piccolo degli altri due.','Il binario B ha circa un sessantaquattresimo dei posti del campione magistratura e un cinquantasettesimo di quello notarile.')
t+='''

## Riscontri e correzioni del 3 ottobre 2026

### Accesso e valutazione

- Magistratura 450: art. 8 del bando, PDF locale p. 10, letto nel testo integrale del passaggio. Scritti: 12/20 ciascuno. Orale: 6/10 per materia valutata numericamente, lingua con giudizio di sufficienza. Totale delle due prove almeno 108, senza frazioni. Il totale non compensa una singola insufficienza. Bando art. 7 già indica finestra 22–26 giugno; diario 24 febbraio pubblicato 10 marzo 2026 distingue identificazione e tre scritti. Una scelta di domanda a novembre 2025 non può usare dettagli pubblicati dopo.
- Avvocatura 7: D.A.G. 114/2025, pp. 3–7 rilette, artt. 2–5. Requisiti alla scadenza; domanda digitale e ultima inviata valida; diritto di segreteria 15 euro. **Art. 4: non ammessi coloro che per due volte non abbiano conseguito l’idoneità in precedenti esami di concorso a procuratore dello Stato.** Non descrivere il percorso come privo di limiti ai tentativi. Il conteggio riguarda l’esito giuridico degli esami, non il solo invio della domanda.
- Notariato 400: artt. 2–4 letti nel PDF locale pp. 7–8. Requisiti sostanziali alla scadenza; limite delle cinque non idoneità valutato alla pubblicazione del bando e riferito ai concorsi successivi all’entrata in vigore della L. 69/2009. Espulsione dopo dettatura e annullamento equivalenti. Pratica entro termine utile, dichiarazione con periodo e Consiglio; certificato nella successiva fase dell’art. 11. I casi su durata della pratica e cinque inidoneità devono avere cronologie separate e possibili.

### Età per procuratore dello Stato

[D.P.C.M. 141/2000, art. 1 vigente](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=000G0191&atto.dataPubblicazioneGazzetta=2000-06-05&tipoDettaglio=multivigenza): testo corrente letto e acquisito in `wiki/raw/correzioni-collana-2026-10-02/dpcm141-2000-art1-20261003.html`. Dal 15 ottobre 2011 il limite è trentacinque, non i quaranta del testo originario. Il bando 2025 richiama il regolamento, non ricava il limite dal solo art. 1 della L. 1035/1966.

La [rassegna ufficiale di Giustizia amministrativa relativa all’ordinanza 8154/2019](https://www.giustizia-amministrativa.it/documents/20142/371980/Cons-St-sez-IV-ord-28-11-2019-n8154-2.pdf/2675497f-f33a-a0e2-1232-b29b3c6c7aa4), p. 5, lettera j, riporta l’indirizzo derivante da Adunanza plenaria 21/2011: superamento dal giorno successivo al compleanno, senza estendere il limite fino al compleanno seguente in ragione della sola formulazione. Non inferire un anno in più da “non superato”. Esempio senza benefici e con scadenza 12 agosto: compleanno il 12 rientra nel giorno limite; compleanno l’11 comporta superamento alla scadenza. La stessa rassegna, lettera i, tratta elevazione per effettivo servizio militare fino a tre anni, con rinvio all’art. 2049 D.Lgs. 66/2010. Non attribuire tre anni automatici a tutti né trasferire benefici di altre carriere. I casi del libro dichiarano assenza di elevazioni; una posizione individuale con beneficio richiede verifica della norma applicabile e della documentazione.

Acquisita inoltre la sentenza TAR Lazio I, 15 giugno 2026, n. 11045, sul bando 2025: [originale ufficiale](https://mdp.giustizia-amministrativa.it/visualizza/?nodeRef=&schema=tar_rm&nrg=202509114&nomeFile=202611045_01.html&subDir=Provvedimenti), raw `tar-lazio-11045-2026.html`. Letta integralmente: improcedibilità per sopravvenuta carenza di interesse dopo mancata consegna degli elaborati; **non è annullamento generale del limite né decisione di merito sul suo computo**. Il libro non attribuisce alla cautelare un diritto generalizzato.

### Confini della funzione

La magistratura ordinaria esercita giurisdizione civile e penale; lo studio del diritto amministrativo nel concorso non significa che il giudice ordinario abbia la generale giurisdizione del giudice amministrativo. Restano le attribuzioni e le questioni incidentali previste dalla legge. I giudici amministrativi come percorso professionale sono fuori perimetro. I calendari ravvicinati misurano un carico, non un’incompatibilità giuridica.

Questi riscontri prevalgono sulle formulazioni storiche incompatibili della nota; il materiale non riesaminato resta tale. L’acquisizione HTML art. 2049 interrotta per reset di rete non è usata come testo completo.
'''
p.write_text(t,encoding='utf8');print('SP03 source consolidated')
