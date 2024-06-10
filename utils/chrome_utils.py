import time
import pyautogui

def start_chrome_hypeone(): 
    pyautogui.moveTo(92, 1068)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.hotkey('ctrl', '1') # Go to the First tab

if __name__ == "__main__":
    start_chrome_hypeone()