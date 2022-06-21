from pessoa import pessoa as p

nome = input('Digite o nome : ')
idade = str(input('Digite a idade : '))
p1 = p(nome,idade)
p1.imprime()
p1.get_ano_nascimento()