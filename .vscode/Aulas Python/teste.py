#igualdade de listas
linha = '02 03 05 07 10 12 13 14 18 20 21 22 23 24 25'
linha1 = '01 05 09 10 13 14 15 16 17 18 20 21 22 24 25'
linha2 = '01 03 05 06 07 08 09 10 13 14 16 18 19 21 24'
linha3 = '01 02 04 06 08 09 10 11 13 14 16 17 19 23 25'
print(type(linha))
l1 = linha1.split()
print(type(l1))
l2 = linha2.split()
print(type(l2))
l3 = l1.copy()

for k in l2:
    if l1.count(k) == True:
        print(f'Numero {k} de l2 esta em l1 na posicao {l1.index(k)}')
    else:
        print(f'\033[31mNumero {k} de l2 NAO esta em l1.\033[m')
        l3.append(k)
        l3.sort()

print('Lista 1 - Original', l1)
print('Lista 2 - Original', l2)    
print('Nova lista l3', l3)