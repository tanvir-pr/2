# Registers "At log on" task for Morning-GitPush.ps1 in this folder.
param(
    [string]$TaskName = "Automation-DailyPushOnLogon"
)

$scriptPath = Join-Path $PSScriptRoot "Morning-GitPush.ps1"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    Write-Error "Missing Morning-GitPush.ps1 at $scriptPath"
    exit 1
}

$pwshCmd = Get-Command pwsh -ErrorAction SilentlyContinue
$powershell = if ($pwshCmd) { $pwshCmd.Source } else { "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" }

$argList = @(
    "-NoProfile"
    "-ExecutionPolicy Bypass"
    "-File"
    $scriptPath
)

$action = New-ScheduledTaskAction -Execute $powershell -Argument ($argList -join " ")
$userId = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $userId
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$principal = New-ScheduledTaskPrincipal -UserId $userId -LogonType Interactive -RunLevel Limited

foreach ($old in @("Automation-MorningGitPush", $TaskName)) {
    $existing = Get-ScheduledTask -TaskName $old -ErrorAction SilentlyContinue
    if ($existing) {
        Unregister-ScheduledTask -TaskName $old -Confirm:$false
    }
}

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Daily git push on logon (see $PSScriptRoot)" | Out-Null

Write-Host "Task '$TaskName' registered: runs at log on."
Write-Host "Script path: $scriptPath"
