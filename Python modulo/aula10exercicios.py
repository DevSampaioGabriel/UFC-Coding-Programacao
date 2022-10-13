#Faça um programa utilizando uma função que receba números e multiplique todos eles.
''' Com erro
def numeros ():
    lista1 = []
    x = 0
    resultado = 1
    while x != -1:
     x = int(input('Digite um número natural, até -1: '))
    if x != -1:
        lista1.append(x)
    for numero in lista1:
        resultado *= numero 
     
    return(resultado)
    

print(numeros(resultado))
'''
'''
def produto_lista(lista):
    produto = 1
    for i in lista:
        produto *= i
    return produto

print(produto_lista([2, 3, 4]))
'''
#Crie uma função fatorial que receba dois parâmetros.
'''
def fatorial (numero, show = False):
    n_fatorial = 1
    for i in range(1, numero+1):
        copia_n_fatorial = n_fatorial
        n_fatorial *= i
    if show:
        print(copia_n_fatorial, 'x', i, '=', n_fatorial)
    return n_fatorial

print(fatorial(5, True))
'''
#Faça uma função que desenhe um retangulo que receba o número de linhas
def retangulo (n_linhas = 5, n_colunas = 5):
    for i in range(n_linhas+2):
        if i == 0 or i == n_linhas+1:
            for j in range(n_colunas+2):
                print(' - ', end = '')
            print('')
        else: 
            for j in range(n_colunas+2):
                if j == 0 or j == n_colunas+1:
                    print(' | ', )
            