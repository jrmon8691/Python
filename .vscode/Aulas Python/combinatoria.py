#combinatória
from math import factorial

p = int(input('Digite o nro. elementos no conjunto -> '))
n = int(input('Digite o nro. de elementos de cada combinacao -> '))

def combinar(a,b):
    z = factorial(b)/(factorial(a)*factorial(b-a))
    return z
    

x = combinar(n,p)

print(f'A combinacao de {p} elementos no universo de {n} tem como resultado \
\033[33m{int(x):,}\033[m apostas.\nO total do custo das apostas sera de \
\033[33mR${x*2.5:.2f}\033[m')