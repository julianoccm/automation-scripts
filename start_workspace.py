import time
import utils.chrome_utils
import utils.kaspersky_utils
import utils.checkpoint_utils
import utils.punch_clock_utils
import utils.microsoft_teams_utils
import utils.microsoft_outlook_utils

def start_workspace():
    # Microsoft Outlook
    utils.microsoft_outlook_utils.start_desktop_outlook()

    # Kaspersky Endpoint Security
    print("Starting Kaspersky Endpoint Security.")
    utils.kaspersky_utils.start_kaspersky()
    time.sleep(15)
    utils.kaspersky_utils.close_kaspersky_window()
    print("Starting Kaspersky Endpoint Started.")

    # Checkpoint Mobile VPN
    print("Starting Checkpoint Mobile VPN.")
    utils.checkpoint_utils.start_checkpoint()
    time.sleep(5)
    utils.checkpoint_utils.write_vpn_password()
    utils.checkpoint_utils.click_on_connect()
    
    # Outlook Get Token VPN
    print("Waiting For Token")
    time.sleep(60)
    token = utils.microsoft_outlook_utils.get_token_checkpoint()

    # Write token to Checkpoint
    utils.checkpoint_utils.write_token(token)
    utils.checkpoint_utils.click_on_connect()
    print("Checkpoint Mobile VPN Connected.")

    # Puch Clock 
    print("Starting Punch Clock Scrapping")
    time.sleep(5)
    utils.punch_clock_utils.bater_ponto()

    # Starting Google Chrome
    utils.chrome_utils.start_chrome_hypeone()

    # Microsoft Teams
    print("Starting Microsoft Teams")
    utils.microsoft_teams_utils.start_teams()
    time.sleep(5)

    print("Keep Online Microsoft Teams")
    utils.microsoft_teams_utils.keep_online()

if __name__ == "__main__":
    print("Starting Workspace Environment")
    start_workspace()
