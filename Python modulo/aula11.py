# Função Recursiva.
# Exemplo 1
'''
def listSum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listSum(numlist[1:])
print(listSum([1, 3, 5, 7, 9]))
'''
# Exemplo 2
'''
def mult_lista(lista):
    if len(lista) == 1:
        return lista [0]
    else:
        return lista[0] * mult_lista(lista[1:])
print(mult_lista([2, 3, 4]))
'''
# Exemplo 3
'''
def soma(n):
    if n == 0:
        return 0
    else:
        return n + soma(n-1)
print(soma(5))
'''
# Exemplo 4
'''
def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)
print(fatorial(5))
'''
# Exercício 1
'''
def calculo(base, exponente):
    if exponente < 1:
        return 1
    else:
        return base * calculo(base, exponente - 1)
print(calculo(2, 10))
'''
# Exercício 2
'''
def listSum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] * listSum(numlist[1:])
print(listSum([1, 3, 5, 7, 9]))
'''
# Exercício 3
'''
def mais_Sig(n):
    if n < 10:
        return n
    else:
        return mais_Sig(n//10)
print(mais_Sig(6564845189))
'''
# Exercício 4
'''
def primo (numPrimo, divisor = 2):
    if divisor == numPrimo:
        return True
    elif numPrimo % divisor > 0:
        return primo(numPrimo, divisor + 1)
    else:
        return False
print(primo(9))
'''
# Exercício 5
'''
def div (divisor, dividendo):
    if dividendo < divisor:
        return 0
    else:
        return 1 + div(divisor, dividendo - divisor)
print(div(3,7))
'''
# Exercício 6
'''
def cont (numero, n, rest = 0):
    rest = numero%10
    if numero == 0:
        return 0
    else:
        if rest == 0:
            return 1 + cont(numero//10, n, rest)
        else:
            return 0 + cont(numero//10, n, rest)
print(cont(2222239759856222,2))
'''

