import os
import time
import pyautogui
from config.scripts_configurations import MICROSOFT_TEAMS_POWERSHELL_START_APP_ID

def start_teams():
    command = f"explorer shell:appsfolder\{MICROSOFT_TEAMS_POWERSHELL_START_APP_ID}"
    os.system(command)

def keep_online():
    pyautogui.moveTo(1000, 600)
    pyautogui.leftClick()

    while True:
        pyautogui.moveTo(100, 100, duration = 1)
        pyautogui.moveTo(100, 600, duration = 1)
        pyautogui.moveTo(1000, 600, duration = 1)
        pyautogui.moveTo(1000, 100, duration = 1)

if __name__ == "__main__":
    start_teams()
    time.sleep(4)
    keep_online()