sorteados = []
for i in range(1,16):
    x = int(input(f'Informar o {i}o. numero -> '))
    if x > 0 and x <= 25:
        if sorteados.count(x) <= 15:
            sorteados.append(x)
            i += 1            
        else:
            print('Numero ja existe...')
    else:
        print('Numero fora da faixa !')

print(f'O total de numeros na lista -> {len(sorteados)}')

print(f'Numero mais baixo -> {min(sorteados)} mais alto -> {max(sorteados)}')

print(f'Numeros sorteados -> {set(sorteados)}')