import requests as rq
import time
import datetime as dt

#conversao de data e hora
d = dt.datetime.now()
data = f'{d.day}/{d.month}/{d.year}'
hora = f'{d.hour}:{d.minute}:{d.second}'

requisicao = rq.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic['USDBRL']['bid']
cotacao_euro  = requisicao_dic['EURBRL']['bid']
cotacao_btc   = requisicao_dic['BTCBRL']['bid']
    
print(f'\n* Cotação de Moedas *\n\nDolar\t=> R${cotacao_dolar}\n\
Euro\t=> R${cotacao_euro}\nBitcoin\t=> R${cotacao_btc}\n\nUpdated:\n{data} | {hora}')