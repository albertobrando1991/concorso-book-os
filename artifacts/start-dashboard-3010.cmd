@echo off
cd /d "C:\Users\alber\Desktop\LIBRO EDITORE CONCORSI PUBBLICI"
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy Bypass -File ".\artifacts\start-dashboard-3010.ps1" > ".\artifacts\dashboard-3010-start.out" 2> ".\artifacts\dashboard-3010-start.err"
