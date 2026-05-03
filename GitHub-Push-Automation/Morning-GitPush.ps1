# Once per calendar day (first successful run): git pull, commit+push if needed.
# If no worktree changes: append "." to bump file at repo root, then commit+push.
# If commits exist but not pushed: git push only.
# Run from Task Scheduler at log on (see Install-MorningPushSchedule.ps1).

$ErrorActionPreference = "Stop"
$ConfigPath = Join-Path $PSScriptRoot "MorningPush.Config.ps1"
$ExamplePath = Join-Path $PSScriptRoot "MorningPush.Config.example.ps1"
$StatePath = Join-Path $PSScriptRoot "last-daily-git-push.txt"
$LogDir = Join-Path $PSScriptRoot "logs"
$null = New-Item -ItemType Directory -Force -Path $LogDir
$LogFile = Join-Path $LogDir ("daily-git-{0:yyyy-MM-dd}.log" -f (Get-Date))

function Write-Log {
    param([string]$Message)
    $line = "{0:yyyy-MM-dd HH:mm:ss}  {1}" -f (Get-Date), $Message
    Add-Content -Path $LogFile -Value $line -Encoding utf8
    Write-Host $line
}

if (-not (Test-Path -LiteralPath $ConfigPath)) {
    if (Test-Path -LiteralPath $ExamplePath) {
        Copy-Item -LiteralPath $ExamplePath -Destination $ConfigPath -Force
        Write-Log "Created MorningPush.Config.ps1 from example. Edit if needed."
    }
    else {
        Write-Log "ERROR: Missing MorningPush.Config.ps1 and example."
        exit 1
    }
}

. $ConfigPath

if ([string]::IsNullOrWhiteSpace($RepoPath)) {
    $RepoPath = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
}

if ([string]::IsNullOrWhiteSpace($DailyBumpFileName)) {
    $DailyBumpFileName = "daily-fullstop.txt"
}

$gitDir = Join-Path $RepoPath ".git"
if (-not (Test-Path -LiteralPath $gitDir)) {
    Write-Log "ERROR: Not a git repo: $RepoPath"
    exit 1
}

$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git) {
    Write-Log "ERROR: git not found in PATH."
    exit 1
}

$today = (Get-Date).ToString("yyyy-MM-dd")
if (Test-Path -LiteralPath $StatePath) {
    $last = (Get-Content -LiteralPath $StatePath -Raw -ErrorAction SilentlyContinue).Trim()
    if ($last -eq $today) {
        Write-Log "Already completed daily push for $today; exiting."
        exit 0
    }
}

function Invoke-Git {
    param([string[]]$Arguments)
    $prev = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        & git @Arguments 2>&1 | ForEach-Object { Write-Log "$_" }
        if ($LASTEXITCODE -ne 0) {
            throw "git $($Arguments -join ' ') exited with $LASTEXITCODE"
        }
    }
    finally {
        $ErrorActionPreference = $prev
    }
}

function Set-LastPushDay {
    Set-Content -LiteralPath $StatePath -Value $today -Encoding utf8 -NoNewline
}

Push-Location $RepoPath
try {
    Write-Log "Repo: $RepoPath"
    Write-Log "git pull"
    Invoke-Git @("pull")

    $porcelain = git status --porcelain 2>&1
    if ($LASTEXITCODE -ne 0) { throw "git status failed" }

    $hasWorktreeChanges = -not [string]::IsNullOrWhiteSpace($porcelain)

    $ahead = 0
    $upstream = git rev-parse --abbrev-ref "@{u}" 2>$null
    if ($LASTEXITCODE -eq 0 -and $upstream) {
        $countOut = git rev-list --count "${upstream}..HEAD" 2>&1
        if ($LASTEXITCODE -eq 0 -and $countOut -match '^\d+$') { $ahead = [int]$countOut }
    }

    if ($hasWorktreeChanges) {
        Write-Log "Local changes detected; committing and pushing."
        Invoke-Git @("add", "-A")
        $msg = "chore: sync {0:yyyy-MM-dd}" -f (Get-Date)
        Invoke-Git @("commit", "-m", $msg)
        Invoke-Git @("push")
    }
    elseif ($ahead -gt 0) {
        Write-Log "Branch is ahead by $ahead commit(s); pushing only."
        Invoke-Git @("push")
    }
    else {
        $bumpPath = Join-Path $RepoPath $DailyBumpFileName
        Write-Log "No local changes; appending '.' to $DailyBumpFileName"
        [System.IO.File]::AppendAllText($bumpPath, ".")
        Invoke-Git @("add", "--", $DailyBumpFileName)
        $msg = "chore: daily mark {0:yyyy-MM-dd}" -f (Get-Date)
        Invoke-Git @("commit", "-m", $msg)
        Invoke-Git @("push")
    }

    Set-LastPushDay
    Write-Log "Done."
    exit 0
}
catch {
    Write-Log "ERROR: $($_.Exception.Message)"
    exit 1
}
finally {
    Pop-Location
}
