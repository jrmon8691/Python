class pessoa:
    ano_atual = 2022
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def imprime(self):
        print("Meu nome eh " + self.name + "\nTenho " + self.age + " anos.")

    def get_ano_nascimento(self):
        print('\nVoce nasceu no ano de ' + self.ano_atual - self.age)
        
