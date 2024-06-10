import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from config.scripts_configurations import URL_PUNCH_CLOCK, PONTO_LOGIN, PONTO_SENHA

def bater_ponto():
    browser = Chrome()
    browser.get(URL_PUNCH_CLOCK)
    
    time.sleep(1)
    input_cpf = browser.find_element('name', 'ctl00$ContentPlaceHolderMasterPage$textBoxID')
    input_senha = browser.find_element('name', 'ctl00$ContentPlaceHolderMasterPage$txtPassword')
    time.sleep(1)

    input_cpf.send_keys(PONTO_LOGIN)
    input_senha.send_keys(PONTO_SENHA)
    input_senha.send_keys(Keys.ENTER)

    time.sleep(4)

    button_entrada = browser.find_element('name', 'ctl00$ContentPlaceHolderMasterPage$imageButtonGetin')
    button_entrada.click()

def iniciar_intervalo():
    browser = Chrome()
    browser.get(URL_PUNCH_CLOCK)
    
    time.sleep(1)
    input_cpf = browser.find_element('name', 'ctl00$ContentPlaceHolderMasterPage$textBoxID')
    input_senha = browser.find_element('name', 'ctl00$ContentPlaceHolderMasterPage$txtPassword')
    time.sleep(1)

    input_cpf.send_keys(PONTO_LOGIN)
    input_senha.send_keys(PONTO_SENHA)
    input_senha.send_keys(Keys.ENTER)

    time.sleep(4)

    button_entrada = browser.find_element('name', 'ctl00$ContentPlaceHolderMasterPage$imageButtonPauseStart')
    button_entrada.click()
    time.sleep(10)

if __name__ == "__main__":
    iniciar_intervalo()