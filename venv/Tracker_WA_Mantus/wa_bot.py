#App_Tracker_WA_Mantus
#By Rodolfo - 2022

from datetime import datetime as dt
from time import sleep
from selenium import webdriver
from selenium.webdriver import Chrome                       #controlador do navegado
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys             #usar o teclado
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located


#entrada site


#espera side-bar_WA
def localiza_sidebar(webdriver):
    print('\n\033[35:1mLocalizando contato ....\r\033[m')
    elementos = webdriver.find_elements_by_css_selector(f'span[title="{cliente}"]')
    return bool(elementos)
    
#condicao online
def online():    
    while driver.find_element(locator).is_enabled():
        print(f'TRACKING | <\033[2:32monline\033[m>  -  {dt.now()}\n')
    else:
        offline()

#condicao offline
def offline():
    wdw_1 = WebDriverWait(driver, timer, poll_frequency=0.5)
    wdw_1.until(presence_of_element_located(locator), 'VALIDACAO DE TRACKING')
    tracking()

#tracking 
def tracking():
    temporizador = timer
    print(
        f'Start tracking | cliente = {cliente} | tempo = {timer}s | Status <\033[31moffline\033[m>  -  {dt.now()}\r'
        )
    while temporizador > 0:
        online()
        sleep(1)
        temporizador -= 1
        print(f'Timer = {temporizador}s\r')
    else:
        print(f'Termino do tracking | cliente = {cliente} | Status <\033[31moffline\033[m>  -  {dt.now()}')
        offline()


cliente = input('\033[34mDigite o nome/telefone do cliente : \033[m')
timer = int(input('\033[34mDigite o tempo de tracking [seg] : \033[m'))            
locator = (By.CSS_SELECTOR, '#main > header > div._24-Ff > div.zzgSd._3e6xi > span[title="online"]')
    
driver = webdriver.Chrome(executable_path = r'C:\Users\DX\Documents\Python\chromedriver.exe')
driver.get('https://web.whatsapp.com/')       
wdw = WebDriverWait(driver, 200, poll_frequency=1)

loc_side = wdw.until(localiza_sidebar)
if loc_side == True:
    driver.find_element_by_css_selector(f'span[title="{cliente}"]').click()    
    print('\033[33mContato localizado ....\n\033[m\r')
    tracking()
else:
    print('\033[31mLista de contatos nao localizada.\033[m')


print('Processo de trackeamento interrompido.\n')
sleep(5)
print('\033[31mAdios muchacho !\033[m')
driver.quit()