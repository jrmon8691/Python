from rich import print
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bf4

url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'
      
req = rq.get(url)
zebra = req.status_code

if req.status_code == 200:
  print(f'[white]Connection OK ![/]\nCode {zebra}\n')
else:
  print(f'[blue, bold]Connection Failed ![/]\nCode {zebra}\n')

print(req.text)