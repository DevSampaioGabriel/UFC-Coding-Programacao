# Funções - Parte 1
# Exemplo 1. Cortador de palavras definindo uma função.
'''
string_a_ser_cortada = input('Digite uma palavra: ')

def cortadorDePalavras (string):
    stringCortada = []
    for letra in string:
        stringCortada.append(letra)
    return stringCortada

print(cortadorDePalavras(string_a_ser_cortada))
'''
# Exemplo 2. A ordem é importante.
'''
nomeDoCliente = str(input('Digite seu nome: '))
divida = float(input('Digite o valor da divida em doláres: '))

def valorEmReais (cliente, valorDivida):
    valorDaDividaEmReais = valorDivida*5
    print(f'O valor a ser pago em reais pelo cliente {cliente} é {valorDaDividaEmReais:.2f}')

valorEmReais(nomeDoCliente, divida)
'''
# Exemplo 3. Não importa a ordem.
'''
nomeDoCliente = 'Gabriel'
divida = float(input('Digite o valor da divida em doláres: '))

def valorEmReais (cliente, valorDivida, valor = 4.77):
    valorDaDividaEmReais = valorDivida*valor
    print(f'O valor a ser pago em reais pelo cliente {cliente} é {valorDaDividaEmReais:.2f}')

valorEmReais(cliente = nomeDoCliente, valorDivida = divida)
'''
# Exemplo 3. sem usar o return
'''
PrimeiroNome = 'Ronaldinho'
SegundoNome = 'Gaucho'

def qualquer (Nome, Sobrenome):
    NomeCompleto = Nome + ' ' + Sobrenome
    return NomeCompleto

NomeCompleto = (PrimeiroNome, SegundoNome)

print(NomeCompleto) //alguma coisa errada
'''
# Exemplo 4. Declarar uma váriavel global ou local.
'''
c6_Bank = 0

def Brasil ():
    global c6_Bank
    c6_Bank += 1
    print(c6_Bank)
    nuBank = 0

Brasil()
'''
# Exercícios
# Exercício 1. Faça uma função que torne a frase em maiúscula
'''
Receba1 = input('Digite qualquer frase: ')

def Receba2 (string):
    return string.upper()
print(Receba2(Receba1))
'''
# Dois jeitos diferentes de fazer.
'''
frase1 = str(input('Digite qualquer frase: '))

def frase2 (maiuscula):
    fraseMaiuscula = maiuscula.upper()
    return fraseMaiuscula
print(frase2(frase1))
'''
# Exercício 2.Utilizando a função def faça um programa que leia a largua e comprimento e mostrar a area.
'''
def area (largura, comprimento):
    area = largura * comprimento
    print(area)
area(largura, comprimento)
# Outro modo.
def recebe_1_c():
    largura = float(input('Digite a largura: '))
    comprimento = float(input('Digite o comprimento: '))
    area = largura*comprimento
    print(area)
recebe_1_c()
'''
# Exercício 3.Utilizando a função def faça um programa que leia sua idade e diga se seu voto é obrigatório ou opcional
'''
def voto (idade):  
    if (idade < 16):
        print('Voto Negado')
    elif ((idade >=16 and idade < 18) or (idade >70)):
        print('Voto opcional')
    else:
        print('Voto obrigatório')
idade_exemplo = int(input('Digite sua idade: '))
voto(idade_exemplo)
'''
# Exercício 4.Utilizando def informe a quantidade de digítos de um determinado número inteiro informado.
'''
def qtd_dig(n):
    n_string = str(n)
    print(len(n_string))
qtd_dig(int(input('Digite um número: ')))
'''
# Exercício 5. Faça um programa para imprimir para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''
def triangulo(n):
    i = 1
    while (i != n+1):
        for x in range(i):
            print(i, end = ' ')
        print('')
        i +=1

triangulo(int(input('Digite um número: ')))
'''

