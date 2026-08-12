# VOL-08 Atomic Q/C/E Gate Design

## Obiettivo

Rendere coerente il gate Format 2: una riga `completo` deve dichiarare `Q:<n> C:<n> E:<n>`, ma tali conteggi sono accettabili soltanto quando derivano dal mapping atomico già registrato in `verificationAttestations` e verificato contro l'apparato del capitolo.

## Decisione

Il validatore calcola per ogni nucleo i conteggi attesi classificando il target attestato come quiz, caso o esercizio in base all'unità reader-visible alla quale punta. Confronta quindi i conteggi dichiarati nella matrice con quelli derivati. Un valore numerico senza mapping, impossibile o discordante resta bloccante.

La promozione a `completo` avviene soltanto dopo che teoria, applicazione, output concorsuale, verifica, fonti e checklist dimensionale sono tutti chiusi. Applicazione e output usano le attestazioni letterali già presenti nel manifest. La checklist dimensionale registra esito verificato e posizione, senza inventare nuove evidenze.

## Alternative escluse

- Lasciare `parziale`: impedisce la pubblicabilità nonostante le attestazioni complete.
- Accettare qualsiasi Q/C/E quando esiste almeno un mapping: non verifica la cardinalità e indebolisce il comportamento fail-closed.
- Rimuovere il requisito Q/C/E: contraddice lo schema Format 2 canonico.

## Error handling

Il gate fallisce quando manca un'attestazione, il target non è reader-visible, la classificazione è ambigua, oppure i conteggi dichiarati non coincidono con quelli derivati. Nessun fallback trasforma automaticamente un errore in warning.

## Verifica

TDD con due casi minimi: un Q/C/E coerente deve passare; un conteggio alterato deve fallire. Seguono suite completa dell'audit, audit reale, typecheck e `git diff --check`.
