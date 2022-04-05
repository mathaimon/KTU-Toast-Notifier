# Running the program on Schedule

The program can be scheduled to run in the background using periodically **Windows Task Scheduler**.

The task can be scheduled in two ways :
- Manually
- Scheduling using script

## Manually scheduling task
- Open Task Scheduler

## TODO
Time intervals:
- Once every day
    - Specific time
- Run repeatedly
    - Every {specified time} hours

**Commands**
```powershell
$taskaction = New-ScheduledTaskAction
    -Execute "pythonw.exe"
    -Argument "path_to_script/main.py"
    -WorkingDirectory "path_to_working_directory"

$tasktrigger = New-ScheduledTaskTrigger
    -At 
    -Daily

$user = "NT AUTHORITY\SYSTEM"

Register-ScheduledTask
    -TaskName "KTU Notification"
    -Action $taskaction
    -Trigger $tasktrigger
    -User $user
    -RunLevel Highest
    -Force
```