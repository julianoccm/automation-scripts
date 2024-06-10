import os
import time
import win32com
import win32com.client
from config.scripts_configurations import MICROSOFT_OUTLOOK_POWERSHELL_START_APP_ID

def start_desktop_outlook():
    command = f"explorer shell:appsfolder\{MICROSOFT_OUTLOOK_POWERSHELL_START_APP_ID}"
    os.system(command)

def get_token_checkpoint():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # "6" refers to the inbox
    messages = inbox.Items
    message = messages.GetLast()
    print(message.Subject)
    token = str.replace(message.Subject, "Token code: ", "")
    
    return token

if __name__ == "__main__":
    start_desktop_outlook()
    time.sleep(5)
    get_token_checkpoint()