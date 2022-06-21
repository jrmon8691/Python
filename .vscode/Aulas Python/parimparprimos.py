# numeros pares/impares ou primos.
#lista primos, pares e impares
class Primospares:

    def __init__(self, primo, parimpar):
        self.primo = primo
        self.parimpar = parimpar

    def primos(self):
        if self.primo % 2 != 0 and self.primo > 1:
            print(f'{self.primo} é numero primo.')
        else:
            print(f'{self.primo} não é numero primo.')
    

    def pares(self):
        if self.parimpar % 2 == 0:
            print(f'{self.parimpar} é numero par.')
        else:
            print(f'{self.parimpar} é numero ímpar.')    