# VOL-07 M-SA02 — Design del lotto setting-ready

**Data:** 2026-07-29
**Ambito:** pipeline VOL-07, modulo `M-SA02`, step 07
**Stato iniziale:** gate bloccato da 8 righe `parziale`

## Obiettivo

Ridurre i residui documentali ancora preparabili internamente senza simulare firme, prove pratiche o procedure del setting reale e senza avviare gli step a valle.

## Uscite

1. Un pacchetto di esercizi PICO/GRADE/applicabilità con tracce, chiavi editoriali e campi di review separati.
2. Un campione regionale ufficiale su accesso ai servizi, continuità ospedale-territorio e PDTA della persona fragile, da usare come modello organizzativo e non come procedura universale.
3. Un lotto TPALL su emissioni convogliate, BAT-AEL, sicurezza del campionamento e repertori metodologici ufficiali.
4. Aggiornamenti coerenti a source notes, matrice, audit e dossier delle review esterne.

## Vincoli di sicurezza editoriale

- Nessun esercizio clinico o tecnico diventa istruzione esecutiva.
- La chiave editoriale valuta il ragionamento, non prescrive decisioni sul singolo caso.
- Le fonti regionali sono esempi contestuali; non sostituiscono procedure aziendali, modulistica o flussi locali.
- Le norme tecniche UNI/EN/ISO non vengono ricostruite da elenchi pubblici né riprodotte senza il testo applicabile.
- Identità, esiti e firme dei revisori restano vuoti fino a review indipendente reale.
- `pipeline/VOL-07/run-state.json` resta di proprietà del CLI.

## Criteri di accettazione

- Fonti raw scaricate da domini istituzionali, con byte e SHA-256 registrati.
- PDF leggibili e metadati coerenti con le pagine ufficiali.
- Esercizi collegati a fonti consolidate, con sezione “limiti e applicabilità”.
- Matrice e audit descrivono soltanto gap effettivamente ridotti.
- Il gate viene rieseguito senza `--accept`; un esito ancora bloccato è corretto se dipende da review o setting esterni.

## Decisione operativa

Si adotta il lotto unico sopra descritto. La richiesta ripetuta dell’utente di procedere costituisce approvazione della direzione conservativa già concordata; non vengono richieste ulteriori scelte perché non modificano il perimetro né autorizzano operazioni esterne irreversibili.
