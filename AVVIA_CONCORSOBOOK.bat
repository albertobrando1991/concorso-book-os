@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo ConcorsoBook OS
echo ============================================
echo.
echo Questa finestra deve restare aperta mentre usi la dashboard.
echo Quando compare "Ready", apri:
echo.
echo   http://127.0.0.1:3000
echo.

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

