# Estudo de listas
lista = list(range(1,101))
pares = []
impares = []

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print('=-='*35)
print(f'\033[32m{len(pares)} Numeros Pares\n{pares}\n', end='\033[m')
print('=-='*35)
print(f'\033[33m{len(impares)} Numeros Impares\n{impares}\n', end='\033[m')
print('=-='*35)