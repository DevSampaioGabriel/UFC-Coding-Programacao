#Tupla e introdução a Matrizes
#Exemplo Lista comprehension
'''
lista = [item**2 for item in range(10)]
for item in lista:
    print(item)
    '''
#Exemplo lista comprehension
'''
lista1 = [1,2,3,4,5,6,7,8]
lista2 = [item for item in lista1 if item % 2 == 1]
print(lista2)
'''
#Exemplo lista comprehension
'''
lista3 = [numero for numero in range(1, 100) if numero % 5 == 0  or numero % 6 == 0]
for n in lista3:
    print(n)
'''
#Exemplo lista comprehension
'''
resultado = ['i' if numero % 5== 0 else '0' for numero in range(10) ]
print(resultado)
'''
#Exemplo lista comprehension
'''
lista4 = [item for item in range(1, 1001)if item % 6 == 0]
print(lista4)
'''
#Usando List comprehension, escreva um programa que encontre os números de 1 a 1000 que contém o número 6
'''
lista4 = [item for item in range(1, 5) if '6' in str(item)]
print(lista4)
'''
#Usando List Comprehension, escreva um programa que conta o número de espaços em uma String.
'''
tamanho_da_frase = [caractere for caractere in str(input('Digite uma frase: ')) if caractere == ' ']
print(len(tamanho_da_frase))
'''
#Tuplas
#Exemplo
'''time = ('Palmeiras', ['campeonato brasileiro', 'Paulista', 'libertadores'])

if ('mundial' in time[1]):
    print(f'{time[0]} tem mundial')
else:
    print(f'{time[0]} não tem mundial')
'''
#Treino
'''
vogais = ('a', 'e', 'i', 'o', 'u')
listaDePalavras = []
novaPalavra = '1'
string = ''

while novaPalavra != '-1':
    novaPalavra = input('Digite uma palavra, só para se digitar -1: ')
    if novaPalavra != '-1':
        listaDePalavras.append(novaPalavra)
tuplaDePalavras = tuple(listaDePalavras)

for palavras in tuplaDePalavras:
    for letra in vogais:
        if letra in palavras:
            string += letra + ' '
    print(palavras, 'possui as seguintes vogais: ', string)
    string = ''   
'''
