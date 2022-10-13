# Lendo arquivos de qualquer tipo e que fecha automaticamente para não corromper.
'''
with open('codigo.txt') as file_object:
    conteudo = file_object.read()
    print(conteudo)
'''
# Ler arquivo de outra forma 'utf-8' significa que o arquivo está lendo em PT-Br.
'''arquivo = open('codigo.txt', encoding='utf-8').read();
print(arquivo)
'''
# Ler arquivo de outra forma.
'''
arquivo = open('codigo.txt', encoding='utf-8').readlines();
for linha in arquivo:
    print(linha.strip())
'''
# ler um arquivo fora da mesma pasta. '../' significa voltar para pasta anterior.
'''
arquivo = open('../MATHIASKW_CODING/texto.txt', encoding='utf-8').readlines();
for linha in arquivo:
    print(linha)
'''
# Existem parametros para usar quando chamar um arquivo exemplo 'w' ele cria um arquivo, caso já tenha ele deleta tudo que tiver no arquivo.
'''
lista = ['banana', 'goiaba']
arquivo2 = open('text4.txt', "w")
i = 0
while i != '0':
    i = input('Digite algo, digite 0 para parar: ')
    if i != '0':
        arquivo2.write(i + '\n')
'''
# Escreva um programa para ler as n primeiras linhas de um arquivo.
'''
programa = open('boletim.txt', encoding='utf-8').readlines()
n = int(input('Até qual linha você quer ler? '))
if n > len(programa):
    print('O n não pode ser maior que o número de linhas do arquivo')
else:
    for x in range(0, n):
        print(programa[x].rstrip())
'''
# Escreva um programa que vai ler um arquivo, mostrar o conteúdo na tela e depois copiar n linhas para outro arquivo.
'''
arquivo5 = open('boletim.txt', encoding='utf-8').readlines()
for linhas in arquivo5:
    print(linhas.rstrip())

linha = int(input('Digite a quantia de linhas para copiar: '))
arquivoDeCopia = open('text4.txt', "w", encoding='utf-8')
if linha > len(arquivo5):
    print('A quantidade de linhas pedida é superior a quantidade de linhas no arquivo.')
else:
    for x in range(0, linha):
        arquivoDeCopia.write(arquivo5[x])
arquivoDeCopia.close()
'''
# Escreva um programa para combinar cada linha do primeiro arquivo com a linha correspondente no segundo arquivo e no fim montar um string nova com as linhas criadas.
arquivo1 = open('boletim.txt', encoding='utf-8').read().split('\n')
arquivo2 = open('text4.txt', encoding='utf-8').read().split('\n')
stringNova = ""
if len(arquivo1) != len(arquivo2):
    print("Os arquivos precisam ter o mesmo número de linhas")
else:
    for x in range(len(arquivo1)):
        stringNova += arquivo1[x] + "" + arquivo2[x] + " "
print(stringNova) 