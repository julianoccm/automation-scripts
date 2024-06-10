import os
import time
import pyautogui
from config.scripts_configurations import PATH_CHECKPOINT_MOBILE_VPN, PASSWORD_VPN

def start_checkpoint():
    os.startfile(PATH_CHECKPOINT_MOBILE_VPN)

def write_vpn_password():
    pyautogui.moveTo(805, 554)
    pyautogui.leftClick()
    pyautogui.write(PASSWORD_VPN)

def click_on_connect():
    pyautogui.moveTo(704, 650)
    pyautogui.leftClick()

def write_token(token): 
    pyautogui.moveTo(796, 608)
    pyautogui.leftClick()
    pyautogui.write(token)

if __name__ == "__main__":
    start_checkpoint()
    time.sleep(5)
    write_vpn_password()
    click_on_connect()


