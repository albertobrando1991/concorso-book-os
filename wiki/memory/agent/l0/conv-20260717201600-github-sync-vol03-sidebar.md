# Sincronizzazione GitHub e allineamento VOL-03

- Data: 2026-07-17
- Richiesta: integrare l'ultimo commit GitHub senza perdere i contenuti locali e correggere la discordanza tra volume selezionato e sidebar capitoli.
- Protezione dati: creato commit locale di salvaguardia `018743b`; mantenuto `stash@{0}` come copia di sicurezza; ripristinati 125 file non tracciati.
- Sincronizzazione: integrato `origin/main` (`d71db22`) nel merge locale `408934d`.
- Diagnosi: il catalogo VOL-03 includeva ancora M-FC01, mentre il volume ricostruito comprende M-FC02 e M-FC03.
- Correzione: catalogo e test allineati nel commit `21744b0`; suite completa 32/32 e typecheck superato.
- Preferenza operativa confermata: durante gli aggiornamenti Git preservare sempre bozze, fonti e contenuti editoriali locali, mantenendo una copia di sicurezza verificabile.
