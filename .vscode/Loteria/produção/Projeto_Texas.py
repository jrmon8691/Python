import math

vl_jogos = {15:2.5, 16:40,17:340, 18:2040, 19:9690, 20:38760}
#Valor dos premios pagos
vl_premios = {11:5 ,12:10 ,13:25 ,14:'verifique' ,15:'verifique'}

loto = list(range(1,26))
loto = set(loto)
sorte ={{3, 6, 7, 9, 10, 11, 12, 14, 16, 17, 19, 20, 23, 24, 25}, {}, {}}
oposi = loto ^ sorte(0)
print(f'Sorteados #{len(sorte)} {sorte}\nOpositores #{len(oposi)} {oposi}')

#recupera jogos do arquivo.txt
with open(arquivo.txt, 'a+') as arq:
    

#cadastramento de jogos
conc = int(input('Concurso Lotofacil # '))
n=1
while n<=15:
    numero = int(input(f'Digite os nros. sorteados(15 numeros) {n} -> '))
    if jogo.count(n):
        print(f'\033[31mNumero {numero} ja esta na lista!\033[m')
    elif numero > 0 and numero < 26:
        jogo.append(numero)
        n += 1
    else:
        print(f'\033[31mNumero {numero} esta fora do conjunto de numeros validos!\033[m')         
                        
print(f'Lotofacil # {conc}',set(jogo))
lstpares = [numero for numero in jogo if numero % 2 == 0]
lstimpares = [numero for numero in jogo if numero % 2 != 0]
print('Numeros Pares -> ', lstpares)
print('Numeros Impares -> ', lstimpares)

jogos[conc] = jogo

n = input('Deseja incluir no aquivo de dados? <S/N> = ').casefold()
if n == 'S':
    arquivo.write(jogos)    
elif n == 'N':
    print('Jogo NAO incluido no arquivo de dados!')
else:
    print('Sua escolha esta fora do padrao...')

print(f'Lista de jogos -> {jogos}')
arquivo.close()

def imp_arquivo():
    pass

def par_impar():
    pass

def primos():
    pass

def analise():
    pass