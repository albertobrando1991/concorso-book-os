param(
  [string]$ManifestPath = "artifacts\informatica-download-manifest.tsv",
  [string]$LogPath = "artifacts\informatica-download-log.csv"
)

$ErrorActionPreference = "Stop"

$root = (Resolve-Path ".").Path
$manifest = Import-Csv -Delimiter "`t" -Path $ManifestPath
$rows = @()

foreach ($item in $manifest) {
  $dest = Join-Path $root $item.dest
  $destDir = Split-Path -Parent $dest
  New-Item -ItemType Directory -Force -Path $destDir | Out-Null

  $status = "ok"
  $message = ""
  $bytes = 0

  try {
    if ($item.url -match "^[A-Za-z]:\\") {
      Copy-Item -LiteralPath $item.url -Destination $dest -Force
    } else {
      $tmp = "$dest.part"
      if (Test-Path -LiteralPath $tmp) {
        Remove-Item -LiteralPath $tmp -Force
      }
      & curl.exe -L --fail --retry 2 --connect-timeout 30 --max-time 180 --output $tmp $item.url
      if ($LASTEXITCODE -ne 0) {
        throw "curl exit code $LASTEXITCODE"
      }
      Move-Item -LiteralPath $tmp -Destination $dest -Force
    }

    $file = Get-Item -LiteralPath $dest
    $bytes = $file.Length
    if ($bytes -le 0) {
      $status = "empty"
      $message = "downloaded file is empty"
    }
  } catch {
    $status = "failed"
    $message = $_.Exception.Message
  }

  $rows += [pscustomobject]@{
    area = $item.area
    slug = $item.slug
    title = $item.title
    url = $item.url
    dest = $item.dest
    status = $status
    bytes = $bytes
    message = $message
  }

  Write-Host "$status`t$($item.slug)`t$bytes"
}

$rows | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $LogPath

$ok = ($rows | Where-Object { $_.status -eq "ok" }).Count
$failed = ($rows | Where-Object { $_.status -eq "failed" }).Count
$empty = ($rows | Where-Object { $_.status -eq "empty" }).Count
Write-Host "summary`t ok=$ok failed=$failed empty=$empty log=$LogPath"
