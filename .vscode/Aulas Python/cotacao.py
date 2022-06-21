import requests
from datetime import datetime

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic['USDBRL']['bid']
cotacao_euro  = requisicao_dic['EURBRL']['bid']
cotacao_btc   = requisicao_dic['BTCBRL']['bid']

print(f'\n* Cotacoes de Moedas *\n\nDolar\t=> {cotacao_dolar}\n\
Euro\t=> {cotacao_euro}\nBTC\t=> {cotacao_btc}\n\nAtualizado:{datetime.now()}')