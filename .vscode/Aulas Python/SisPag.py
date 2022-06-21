##Tabela Price e SAC
# m, n, juros, prest,sd, amort,

m=float(input('Digite o valor do emprrestimo =>'))
n=int(input('Digite o numero de tempo =>'))
j=float(input('Digite a taxa de juros =>'))
p=str.upper(input('Digite o periodo <A-M-D> =>'))

def taxadejuros(a, b):
#recebe o juros e periodo
    if p == 'D':
        tx = (1+a)**(b/365)
    elif p == 'A':
        tx = (1+a)**(b/12)
    else:
        tx = (1+a)**(b/30)
    return tx

z = taxadejuros(j, n)    
print('Taxa de juros \033[32m{:.6f}\033[m no periodo de \033[32m{}\033[m'.format(z,p))