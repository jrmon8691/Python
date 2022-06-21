import math

a = int(input('Digite o nro de elementos da aposta -> '))
print(f'Voce escolheu \033[32;1m{a}\033[m elementos')

lista = []

cont=1
while cont <= a: 
    b = int(input(f'Escolha o \033[33m{cont}o.\033[m numero -> '))
    if lista.count(b):
        print(f'\033[31mNumero {b} ja esta na lista!\033[m')
    elif b > 0 and b < 26:
            lista.append(b)
            cont += 1
    else:
        print(f'\033[31mNumero {b} esta fora do conjunto de numeros validos!\033[m')         
                    
print('Sua lista -> ',set(lista))
lstpares = [numero for numero in lista if numero % 2 == 0]
lstimpares = [numero for numero in lista if numero % 2 != 0]
lstprimos = [numero for numero in lista if numero % 2 != 0 and numero > 1]
print('Numeros Pares -> ', lstpares)
print('Numeros Impares -> ', lstimpares)
print('Numeros Primos -> ', lstprimos)