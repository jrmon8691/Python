# web scrapping
from typing import Any
import requests as rq
from bs4 import BeautifulSoup as bs 

#homepage
url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'
pagina = rq.get(url)
status = pagina.status_code

#BS4
soup = bs(pagina.text, 'html.parser')
soup.findAll('td rowspan="1"')
#Print
print('Status da pagina -> ', status,'\r')
print(soup.getText)