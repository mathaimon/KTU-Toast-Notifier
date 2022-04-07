import os, sys
import subprocess
from datetime import datetime

from pick import pick


def main():
    header = """
    KTU Notifier : Task Scheduler
    -----------------------------
        """
    description = """Follow steps in the setup to create a new \n'Windows Task Schedule' automatically.
    """
    print(header)
    print(description)

    input("Press Enter to start setup..... ")

def select_task_frequency() -> tuple[str, str]:
    """Select how frequent to run the program and the time period

    Returns ->
    0 : Run Daily
    1 : Run Repeatedly"""
    # Selecting how often to run the program
    title1 = "How often do you want to run the program :"
    options = ['Once Daily', 'Repeatedly at specified time intervals']

    option, index = pick(options, title1, indicator='->')

    print(f"\n[+] Selected option : {option}\n")
    # Run if once daily option is selected
    if index == 0:
        time = input("Enter the time you want to run the program (0-24) : ")
        time = run_once_daily(time)
        return index, time

    # Run if run repeatedly is selected
    if index == 1:
        interval = input("Enter the time interval for running the program (1-24) : ")
        time = run_repeatedly(interval)
        return index, time
        

def run_once_daily(time: str) -> str:
    # Check if the time is valid
    if int(time) > 24 or int(time) < 0:
        time = input("\n[-] Invalid Time : Enter time between 1-24 : ")
        run_once_daily(time)
    else:
        #covert time to 00:00AM format
        time = datetime.strptime(time, "%H")
        time = time.strftime("%I:%M%p")

        print(f"\n[+] The program will execute daily at {time}")
    return time


def run_repeatedly(time: str) -> str:
    # Check if the time is valid
    if int(time) > 24 or int(time) < 0:
        time = input("\n[X] Invalid Time : Enter time interval between 1-24 : ")
        run_repeatedly(time)
    else:
        print(f"\n[+] The program will execute every {time} Hrs")
    return time


def construct_command(selection: str, time: str) -> tuple[str, str]:
    """Construct the command to run.
    Takes the selection index and time as input"""
    application = "pythonw.exe"
    argument = "./main.py"
    directory = os.getcwd()

    task_action = f"""$taskaction = New-ScheduledTaskAction `
    -Execute "{application}" `
    -Argument "{argument}" `
    -WorkingDirectory "{directory}" """

    # If selection is daily
    if selection == 0:
        trig_time = time
        task_trigger = f"""$tasktrigger = New-ScheduledTaskTrigger `
        -Daily `
        -At {trig_time}"""
    # If selection is to run periodically
    elif selection == 1:
        interval_time = time
        task_trigger = f"""$tasktrigger = New-ScheduledTaskTrigger `
        -Once `
        -At (Get-Date) `
        -RepetitionInterval (New-TimeSpan -Hours {interval_time})`
        -RepetitionDuration ([System.TimeSpan]::MaxValue)"""
    return task_action, task_trigger
    

def create_script(task_action: str, task_trigger: str):
    """Create powershell file with preffered settings, action and trigger"""
    settings = f"""$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -DontStopIfGoingOnBatteries `
    -AllowStartIfOnBatteries `
    -RunOnlyIfNetworkAvailable"""

    user = '$user = "NT AUTHORITY\SYSTEM"'

    register_task = """Register-ScheduledTask `
    -TaskName "KTU Notification" `
    -Action $taskaction `
    -Trigger $tasktrigger `
    -User $user `
    -RunLevel Highest `
    -Settings $settings"""

    with open("./task_scheduler/ktu-notifier-scheduler.ps1", "w") as f:
            f.writelines([
                task_action+'\n',
                task_trigger+'\n',
                settings+'\n',
                user+'\n',
                register_task
            ])


def confirm_action():
    """Confirm wheather to continue with the settings or exit"""
    check = input("\nAre you sure with the options (y/n) : ")
    
    if check == 'n':
        sys.exit()
    elif check == 'y':
        pass
    else:
        print("\n[X] Invalid input")
        confirm_action()


if __name__ == "__main__":
    main()
    index, time = select_task_frequency()
    task_action, task_trigger = construct_command(index, time)
    
    confirm_action()
    create_script(task_action, task_trigger)

    script_path =  os.path.join(os.getcwd(), 'task_scheduler\ktu-notifier-scheduler.ps1')
    subprocess.Popen(['powershell.exe', script_path])