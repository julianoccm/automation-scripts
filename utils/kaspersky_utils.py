import os
import time
import pyautogui
from config.scripts_configurations import PATH_KASPERSKY_ENDPOINT_SECURITY

def start_kaspersky():
    os.startfile(PATH_KASPERSKY_ENDPOINT_SECURITY)

def close_kaspersky_window():
    pyautogui.moveTo(1429, 191)
    pyautogui.leftClick()

if __name__ == "__main__":
    start_kaspersky()
    time.sleep(15)
    close_kaspersky_window()