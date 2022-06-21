nome = input('=> Digite seu nome : \t').title()
peso = float(input('=> Digite o peso : \t'))
altura = float(input('=> Digite a altura : \t'))

#calculo IMC
def imc(p, a):
    return p/(a**2)
    
print(f'\n\033[32mOla {nome}.\nSeu peso ideal = {imc(peso, altura):.2f}\n\033[m')