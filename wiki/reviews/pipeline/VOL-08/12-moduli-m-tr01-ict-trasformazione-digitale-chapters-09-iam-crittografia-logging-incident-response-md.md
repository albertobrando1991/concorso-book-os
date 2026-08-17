# Report editoriale — M-TR01, Capitolo 09: IAM, crittografia, logging e incident response

## 1. Sintesi editoriale
- Genere: capitolo specialistico/workbook per concorsi pubblici ICT.
- Lettore: candidato che studia senza wiki, dashboard o note interne.
- Perimetro: capitolo 09, matrice Format 2, confini con VOL-01 e capitoli 7, 8 e 10.
- Esito: sei nuclei autosufficienti collegano identità, privilegi, chiavi, log e risposta a un incidente; caso, timeline e sei quiz consentono una prima verifica autonoma.

## 2. Punti applicati della checklist
Applicati i controlli 1-5 su struttura e gerarchia, 6-15 su coerenza, completezza, definizioni, contenuto tecnico, tabelle e fonti, 16-21 su frase, chiarezza, tono e ripetizioni, 22-26 e 28-30 su lingua, uniformità e leggibilità. Il punto 27 resta non applicabile: non è disponibile il PDF impaginato. Eseguiti il test dello studente e la verifica v4: nessuna promessa formativa richiede accesso a strumenti o collegamenti interni.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | N-TR01-09-01 | Copertura didattica | Media | Il testo legacy distingueva account e identità ma non sviluppava ciclo joiner-mover-leaver, account tecnici e riesame. | Nucleo ampliato con ruoli, evidenze, federazione e caso di cambio ufficio. | Applicato |
| E02 | N-TR01-09-02 | Accuratezza e applicazione | Media | Autenticazione, autorizzazione e privilegi erano compressi e non offrivano criteri per RBAC, ABAC e ACL. | Inseriti modelli, deny by default, verifica lato servizio, accesso temporaneo e caso PA. | Applicato |
| E03 | N-TR01-09-03 | Completezza tecnica | Media | Crittografia e gestione delle chiavi non separavano con sufficiente chiarezza funzioni, ciclo, rotazione e revoca. | Inserite distinzioni, inventario, responsabilità, compromissione e caso di secret esposto. | Applicato |
| E04 | N-TR01-09-04 e 09-05 | Struttura didattica | Media | Logging, triage e incident response non disponevano di una verifica autonoma e di una timeline compilabile. | Inseriti caso guidato, playbook, timeline e sei risposte commentate. | Applicato |
| V01 | N-TR01-09-01 e 09-02 | Quadro tecnico mobile | Media | Terminologia e configurazioni IAM/PAM richiedono controllo specialistico al cut-off. | Riesaminare fonti primarie e confini applicativi nello step 15. | Da verificare allo step 15 |
| V02 | N-TR01-09-03 | Quadro tecnico mobile | Media | Il ciclo delle chiavi è spiegato a livello concettuale; policy e dettagli architetturali richiedono audit specialistico. | Rieseguire audit key management nello step 15. | Da verificare allo step 15 |
| V03 | N-TR01-09-04 e 09-05 | Quadro tecnico mobile | Media | Log management, triage e incident response dipendono da fonti e procedure da verificare al cut-off. | Rieseguire audit SOC/incident response nello step 15. | Da verificare allo step 15 |
| V04 | N-TR01-09-06 | Contenuto normativo mobile | Media | Il testo evita termini, soglie e canali non consolidati, ma atti ACN/CSIRT, platea NIS2 e privacy vanno verificati sul caso concreto. | Rieseguire audit ACN/NIS2/privacy nello step 15. | Da verificare allo step 15 |

## 4. Osservazioni per capitolo
### Capitolo 09
- Punti di forza: progressione chiara dall'identità al recupero; distinzioni tecniche esplicite; caso credibile; prudenza nel raccordo normativo; confini con continuità, rischio e governance del dato non invasivi.
- Copertura: sei nuclei superano la soglia Format 2, il capitolo contiene un blocco `▣ Verifica`, sei risposte commentate e un caso ragionato. La matrice contiene gli stessi sei Nucleo ID con checklist dimensionale completa.
- Debiti: V01-V04 sono audit specialistici automatici da chiudere negli step 13-18 e non equivalgono a una revisione umana simulata.

## 5. Coerenza globale
La terminologia distingue identità/account, autenticazione/autorizzazione, hash/cifratura, evento/log/alert/incidente e incidente cyber/data breach. VOL-01 resta un prerequisito; i capitoli 7, 8 e 10 sono confini di materia, non rinvii sostitutivi della spiegazione. Le promesse di apertura risultano mantenute nel testo reader-facing.

## 6. Contenuto da verificare
- Fonti IAM/PAM e key management al cut-off del text freeze.
- Indicazioni ufficiali NIST su log management e incident response, senza convertirle in obblighi italiani generali.
- Testo vigente del d.lgs. 138/2024, atti ACN/CSIRT pertinenti e valutazione distinta della protezione dei dati personali.

## 7. Suggerimenti facoltativi
- In impaginazione, mantenere playbook e timeline su pagine con larghezza sufficiente per la compilazione manuale.

## 8. Priorità degli interventi
1. Chiudere V01-V04 mediante gli audit automatici specialistici previsti dagli step 13-18.
2. Riesaminare le fonti mobili al cut-off prima del text freeze.
3. Eseguire audit visivo KDP quando esisterà il PDF impaginato.

## 9. Giudizio di pubblicabilità
Pubblicabile con correzioni minori.

Il capitolo supera i controlli di struttura, densità, copertura e citazioni; non restano errori gravi aperti nel testo. Il giudizio non sostituisce gli audit specialistici, i gate successivi o la conferma umana obbligatoria dello step 24.

## 10. Limiti della revisione
La revisione ha esaminato Markdown, matrice e fonti già consolidate. Non ha verificato un PDF, non ha simulato revisione umana e non ha dichiarato chiusi gli audit specialistici successivi.