# Analise de venda para compra de produto 
# com simulacao de preco compra abaixo.
def tela(n = 25):
    print('\033[35m=-=-\033[m'*n)

tela()
x=int(input('Digite a quantidade a ser comprada => '))
y=float(input('Digite o preco praticado => '))
z=float(input('Valor de desconto($0.1 a $0.5) => '))

qv = lambda qc,pc:(qc*pc)/(y-z)
qtdevendida = round(qv(x,y))

print(f'Qtde. a ser comprada \033[32m{x}\033[m ao preco de \033[32m${y}\033[m\nQtde. a ser vendida \033[34m{qtdevendida}\033[m ao preco de \033[34m${y-z:.1f}\033[m')

tela()