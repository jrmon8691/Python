#Indice de massa corporal
from tkinter import *
import tkinter

#calculo IMC
def imc(p, a):
    mc = p/(a**2)
    return mc

#janela
janela = Tk()
#janela.geometry('300x300')
janela.title('IMC - indice de massa corporal'.title())
janela.config(padx=10, pady=10)

l1 = Label(janela, text='Nome:   ').grid(column=0, row=0)
l2 = Label(janela, text='Peso:   ').grid(column=0, row=2)
l3 = Label(janela, text='Altura: ').grid(column=0, row=4)
l4 = Label(janela, text='Resultado:').grid(column=0, row=6 )

nome = Entry(janela, background='#fff').grid(column=1, row=0)
peso = Entry(janela, background='#fff').grid(column=1, row=2)
altura = Entry(janela, background='#fff').grid(column=1, row=4)

n = nome.get()
p = peso.get()
a = altura.get()

btn_click = Button(janela, text='Click', command=imc(p,a)).grid(column=1, row=10)
btn_sair = Button(janela, text='Sair', command=janela.destroy).grid(column=0, row=10)

janela.mainloop()

#nome = input('=> Digite o nome : ')
#peso = float(input('=> Digite o peso : '))
#altura = float(input('=> Digite a altura : '))

#calculo peso ideal
def pesoideal(c):
    pesoi = 25*(c**2)
    return pesoi

massa_corporal = imc(p, a)
tela = '\033[32m=-\033[m'*40
print(tela, f'\n\033[39mPaciente\t{n}\nPeso atual\t{p:.1f}kg\nAltura\t\t{a:.2f}m\nIMC\t\t{massa_corporal:.2f}\n')

if massa_corporal >= 18.5 and massa_corporal <=24.999:
    print(f'\033[32m{nome}, voce esta com IMC Normal.')
elif massa_corporal >= 25 and massa_corporal <= 29.999:
    print(f'\033[33m{nome}, seu IMC tem condicao de Sobrepeso. Seu peso ideal e {pesoideal(altura):.1f}kg\nVoce tem que perder {peso-pesoideal(altura):.4}kg.')
elif massa_corporal >= 30 and massa_corporal <= 34.999:
    print(f'\033[31m{nome}, seu IMC tem condicao de Obesidade Grau I. Seu peso ideal e {pesoideal(altura):.1f}kg\nVoce tem que perder {peso-pesoideal(altura):.4}kg.')
elif massa_corporal >= 35 and massa_corporal <= 39.999:
    print(f'\033[31m{nome}, seu IMC tem condicao de Obesidade Grau II. Seu peso ideal e {pesoideal(altura):.1f}kg\nVoce tem que perder {peso-pesoideal(altura):.4}kg.')
elif massa_corporal >= 40:
    print(f'\033[31m{nome}, seu IMC tem condicao de Obesidade Grau III ou Morbidez. Seu peso ideal e {pesoideal(altura):.1f}kg\nVoce tem que perder {peso-pesoideal(altura):.4}kg.')
else:
    print(f'\033[29m{nome}, seu IMC esta abaixo do normal.')
print(tela)    