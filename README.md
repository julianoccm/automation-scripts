# Automation Scripts 🤖

Scripts to automate desktop processes, such as:
 - Start and connect to the VPN
 - Start antivirus
 - Start Microsoft Teams
 - Start Microsoft Outlook
 - Back up the work environment
 - Upload files to Google Drive

## How to set it up?

Create a folder inside the **utils** folder called **config**, and inside it create a file with the name: **scripts_configurations.py.** 

Inside this file put the following content, and change the information according to your environment:


```py
PATH_KASPERSKY_ENDPOINT_SECURITY = "" # System Path to Kaspersky Endpoint Security .exe file
PATH_CHECKPOINT_MOBILE_VPN = "" # System Path to Checkpoint Mobile VPN .exe file
PATH_CHROME = "" # System Path to Chrome .exe file

BACKUP_FILE_NAME_TEMPLATE="Backup-Workspace-YYYY-MM-DD" # File name template and date
PATH_TEMP="C:\\Temp" # Path to Temp folder to save .zip file
PATH_FOLDER_TO_BACKUP="E:\\" # Path Folder to backup
PATH_GOOGLE_DRIVE="G:\\" # Path to your Google Drive

MICROSOFT_TEAMS_POWERSHELL_START_APP_ID = "MSTeams_8wekyb3d8bbwe!MSTeams" # PowerSheell App Id for MS Teams
MICROSOFT_OUTLOOK_POWERSHELL_START_APP_ID = "Microsoft.Office.OUTLOOK.EXE.15" # PowerSheell App Id for MS Outlook

URL_PUNCH_CLOCK = "" # Punch Clock URL

PASSWORD_VPN = "" # VPN Password
PONTO_LOGIN = "" # Ponto Login
PONTO_SENHA = "" # Ponto Password
```

Acess [here](https://github.com/julianoccm/automation-scripts/blob/3e253203b3105dead4ecc5ac01e194f2099f7192/utils/config/scripts_configurations.py) the commit of this file.