# data 
import numpy as np

lista1 = '4	23	8	2	13	12	17	9	6	7	1	25	21	10	11'.replace(' ', ',')
lista2 = '8	5	21	14	22	15	18	10	11	24	1	7	16	13	2'.replace(' ', ',')

arr1 = np.array(lista1)
arr2 = np.array(lista2)
newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(f'Lista1 => {lista1}\nLista2 => {lista2}\nLista Join => {newarr}')