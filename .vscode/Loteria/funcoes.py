#classe loteria
#by Rodolfo Montemurro - 2022-03-08
#
class Loteria:
    def __init__(self):
        self.nros = set()
        for x in range(1,26):
            self.nros.add(x)

    def imprime_cartao(self):
        print(self.nros)