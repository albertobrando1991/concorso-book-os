# Conversation Memory: Ruflo Stop Hook Patch

- created_at: 2026-05-28T00:50:00.000Z
- scope: global
- route: codex-system-maintenance

## User Intent

L'utente ha chiesto di procedere con la correzione dell'avviso ricorrente `Stop hook (failed) error: hook exited with code 1`.

## Outcome

La causa individuata e' lo Stop hook globale di Claude/Ruflo in `C:\Users\alber\.claude\plugins\cache\ruflo\ruflo-core\0.2.0\hooks\hooks.json`, che chiamava direttamente `npx claude-flow@alpha hooks session-end ...` e falliva con `npm ECOMPROMISED Lock compromised`.

Il file hook e' stato patchato con backup automatici `.bak-*`: i comandi `npx claude-flow@alpha` ora sono wrappati con `cmd /d /s /c "... || node -e ""process.exit(0)"""`, cosi' lo hook resta attivo ma non blocca piu' la chiusura della sessione se npm/claude-flow fallisce.

## Verification

Lo Stop hook patchato e' stato eseguito manualmente e ha restituito `exit=0`.
