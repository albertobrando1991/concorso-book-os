$projectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $projectRoot

if (-not (Test-Path "artifacts")) {
  New-Item -ItemType Directory -Path "artifacts" | Out-Null
}

$logPath = Join-Path $projectRoot "artifacts\dashboard-3010.log"
"[$(Get-Date -Format o)] Starting dashboard on port 3010" | Set-Content -Path $logPath -Encoding utf8
Write-Host "Starting ConcorsoBook OS dashboard on http://localhost:3010"
Write-Host "Keep this window open while using the dashboard."

& ".\node_modules\.bin\next.cmd" dev --port 3010 *>&1 | Tee-Object -FilePath $logPath -Append
