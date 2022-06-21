#App que ativa botao de sorteio no Hypnobox
import time
import pyautogui as pg  

def tempo(t=3):
    time.sleep(t)

pg.pause = 0.1
pg.alert('Sistema Knob esta controlando seu terminal !\nNao mexa em nada !')
print('Iniciando....')
pg.hotkey('winleft')
tempo()
pg.write('Google Chrome', interval=0.2)
tempo()
pg.press('enter')
tempo(5)
try:
    print('Abrindo a homepage....')
    pg.write('http://tegravendas.hypnobox.com.br', interval=0.2)
    tempo()
    pg.press('enter')
except:
    print('Homepage sem acesso....')

#btn_sorteio = pg.locateOnScreen('a#bt-sorteio-automatico.botao')
#print('Localizacao botao ->', btn_sorteio)
