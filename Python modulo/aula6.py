# Arrays no python
'''
lista1 = ['Banana', 'Maçã', 'manga', 'Abacate']
'''

# Treino 1
'''
listaa = ["Banana", "Maçã", 56, False]
print(listaa[3, -1, 0, 0:2, :6, 0:, 1:-1])
'''

# Treino 2
'''
lista = ['Banana', 'Maçã', 'manga', 'Abacate']
i = int(input('Insira um indice para percorrer a lista de alimentos: '))
print(lista[i])
'''

# Treino 3
'''
lista = ['Banana', 'Maçã', 'manga', 'Abacate']
print(lista[0] in lista) print("Banana" in lista)
'''

# Treino 4
'''
lista = ['Banana', 'Maçã', 'manga', 'Abacate']
lista[1:3] = ['Kiwi', 'Coco']
print(lista)
'''

# Treino 5
# '.insert(', "Romã")' // Insere um item no índice expecificado 
'''
lista = ['Banana', 'Maçã', 'manga', 'Abacate']
lista.insert(1, 'Romã')
print(lista)
'''

# Treino 6. 
# '.append("maracuja")' // Insere um elemento no final da lista
'''
lista = ['Banana', 'Maçã', 'manga', 'Abacate']
lista.append('maracuja')
print(lista)
'''

# Treino 7.
# '.extend' // Extende a primeira linha com a segunda
'''
lista2 = ['Banana', 'Maçã']
lista2.extend(lista2)  
print(lista2)
'''

# Treino 8.
# '.remove('', 1:3)' // Remove a parte expecificada da lista.
'''
lista = ['Banana', 'Maçã', 'manga', 'Abacate']
lista.remove('Banana') #lista.remove
print(lista)
'''

# Treino 9.
# '.pop(1)' // Remove e retorna um item de determinado índice .
# Neste caso, vamos guardar esse valor retornado numa variável 'x'
# porém, nem sempre isso é necessário.
'''
x = lista1.pop(1)
print(lista1)
print(x)
'''

# Treino 10.
# 'del lista[0]' // só remove o item de determinado índice.
'''
del lista1[0]
print(lista1)
'''

# Treino 11.
# lista1 declarada Array, lista2 declarada como Array vazia // com '.append()' vai inserir um índice da lista1 com o '.pop(índice)'
'''
lista2 = []
lista2.append(lista1.pop(1))
print(lista2)
print(lista1)
'''

# Treino 12.
# '.clear' // limpa a lista deixando ela vázia, mas a variável ainda existe.
'''
lista1.clear()
print(lista1)
'''

# Treino 13.
# a função 'len()' // Retorna o número de elementos da lista
'''
tamanho = len(lista1)
print(tamanho)
'''

# Treino 14.
# Utilizar 'for' para percorrer a lista com a variável expecificada 'x'.
'''
lista = [1, 3, 5, 7, 9]
for x in lista:
    print(x)
'''

# Treino 15.
# Percorrer todos os elementos da lista utilizando o 'for', 'range()'
# e o 'len()'
'''
lista = [1, 3, 5, 7, 9]
for i in range(len(lista)):
    print(lista[i])

'''
# Treino 16.
# Percorrendo só os índices pares com o 'for'.
'''
lista = [1, 3, 5, 7, 9]
for i in range(len(lista)):
    if i%2 == 0:
        print(lista[i])
'''
# Treino 17.
# Percorrendo toda a lista printando os elementos utilizando o 'while'
'''
lista = ['banana', 'maçã', 'cereja']
i = 0
while i < len(lista):
    print(lista[i])
    i+=1
'''

# Exercício 1.
'''
lista1 = []
x = 0
while x != -1:
    x = int(input('Digite um número natural, até -1: '))
    if x != -1:
        lista1.append(x)
numero = int(input('Digite um número para ver se está presente na lista: '))
if numero in lista1:
    print(f'O número {numero} está presente!')
else:
    print(f'O número {numero} não está presente.')
'''
# Exercício 2.
'''
lista1 = []
x = 0
while x != -1:
    x = int(input('Digite um número natural, até -1: '))
    if x != -1:
        lista1.append(x)
numero = int(input('Digite um número para ver se está presente na lista: '))
print(f'A lista original é: {lista1}')
if numero in lista1:
    lista1.remove(numero)
else:
    print(f'O número {numero} não está presente.')
print(lista1)
'''
# Exercício 3.
'''num = input('Digite um número para ser invertido: ')
novaN = ''
for i in range(len(num)-1, -1, -1):
    novaN += num[i]
    print(novaN)'''
