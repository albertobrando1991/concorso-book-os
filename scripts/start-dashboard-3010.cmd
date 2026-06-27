@echo off
cd /d "%~dp0.."
echo Starting ConcorsoBook OS dashboard on http://localhost:3010
echo Keep this window open while using the dashboard.
if not exist artifacts mkdir artifacts
echo [%date% %time%] Starting dashboard on port 3010 > artifacts\dashboard-3010.log
call node_modules\.bin\next.cmd dev --port 3010 >> artifacts\dashboard-3010.log 2>&1
echo [%date% %time%] Next exited with code %ERRORLEVEL% >> artifacts\dashboard-3010.log
type artifacts\dashboard-3010.log
pause
