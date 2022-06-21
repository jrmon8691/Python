#Selenium Webdriver
#Navegador Chrome
from time import sleep
from webbrowser import Chrome
from selenium import webdriver #controlador do navegador
from selenium.webdriver.common.keys import Keys #usar o teclado
from selenium.webdriver.common.by import By # localizar o item no navegador
from selenium.webdriver.chrome.options import Options 

#criar o navegador
chrome_options = Options
#chrome_options.add_argument('--headless') #roda bot em segundo plano
navegador = webdriver.Chrome(executable_path = r'C:\Users\DX\Documents\Python\chromedriver.exe')    

#entrada no site 
navegador.get('https://www.google.com/')
sleep(1)
#busca elemento de pesquisa do Google
navegador.find_element(By.XPATH, r'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
sleep(1)

#acionando a busca 
navegador.find_element(By.XPATH, r'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#busca valor da cotacao e data/hora
cotacao_dolar = navegador.find_element(By.XPATH, r'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
data_hora = navegador.find_element(By.XPATH, r'//*[@id="knowledge-currency__updatable-data-column"]/div[2]/span').text

print(f'\033[32m| USD Quote {cotacao_dolar} | {data_hora} |\033[m')

navegador.quit()