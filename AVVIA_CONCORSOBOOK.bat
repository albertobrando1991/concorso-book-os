@echo off
setlocal
cd /d "%~dp0"

set AGENT_MEMORY_ENABLED=true
set AGENT_MEMORY_ROOT=wiki\memory\agent

echo ============================================
echo ConcorsoBook OS
echo ============================================
echo.
echo Questa finestra deve restare aperta mentre usi la dashboard.
echo Quando compare "Ready", apri:
echo.
echo   http://127.0.0.1:3000
echo.
echo Memoria agentica locale: attiva
echo.

where codex >nul 2>nul
if errorlevel 1 (
  echo ATTENZIONE: Codex CLI non trovato. Il Manual Writer usera' il fallback locale.
  echo.
) else (
  codex login status >nul 2>nul
  if errorlevel 1 (
    echo ATTENZIONE: Codex CLI non e' autenticato.
    echo Per usare il Manual Writer con il tuo account Codex, apri un nuovo terminale qui ed esegui:
    echo.
    echo   codex login --device-auth
    echo.
  )
)

if not exist node_modules (
  echo Dipendenze non trovate. Eseguo npm install...
  npm install
  if errorlevel 1 (
    echo.
    echo ERRORE: npm install non riuscito.
    pause
    exit /b 1
  )
)

npm run dev -- -H 127.0.0.1 -p 3000

echo.
echo Il server si e' fermato.
pause
