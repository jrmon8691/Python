arquivo = open('arquivo.txt', '+')
arquivo.write('Testando gravação de arquivos em Python  Acrescentando conteúdo')
print(f'lendo arquivo....', arquivo.read())
arquivo.close()