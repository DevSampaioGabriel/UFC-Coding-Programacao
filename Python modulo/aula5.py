# For, While e Range() no python
#Treino básico 1:
'''lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)'''

#Treino básico 2:
'''n = int(input('Insira o número: '))
i = 0
while i <= n:
    print(i)
    i += 1 
'''
#Treino básico 3:
'''for x in range(2, 21, 2):
    print(x)'''

#Treino básico 4:
'''NumeroDeAlunos = int(input('Digite o número de alunos: '))
NotaDosAlunos = 0
for x in range(NumeroDeAlunos):
    NotaDosAlunos += int(input('Digite a nota dos alunos: '))

media = NotaDosAlunos / NumeroDeAlunos
print(media)'''

#Treino básico 5:
'''N = int(input('Digite um valor inteiro: '))
for N in range(1, N+1):
    print(N)
print('Parabuians')'''

#Treino básico 6:
'''num = int(input('Digite um número inteiro: '))
for num in range(2, num +2, 2):
    print(num)'''

#Treino básico 7:
'''N = int(input('Digite o valor de N: '))
X = int(input('Digite o valor de X: '))
for num in range(1, X+1):
    print(f''N * num)
'''
#Treino básico 8:
'''contador = 0
while (contador < 10):
    print(f'A variavel é: {contador}')
    contador += 1'''

#Treino básico 9:
'''N = int(input('Insira um valor: '))
variavel = 1
while (variavel <= N):
    print(variavel)
    variavel += 1'''

#Treino básico 10:
'''N = int(input('Digite um número: '))
print(N % 10)
print(N % 100)
print(N % 1000)
print(N % 10000)
print(N % 100000)
x1 = N % 10
x2 = (N%100 - N%10)/10 
x3 = (N%1000 - N%100)/100
x4 = (N%10000 - N%1000)/1000
x5 = (N%100000 - N%10000)/10000
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)'''

#Treino básico 11:
'''nun1 = int(input('Digite um valor para mostrar os algarismos: '))
i = 0
temp = nun1

while temp > 0:
    i += 1
    temp -= temp%(10**i)
    print(i)'''
#Treino complicado 11:
'''n = int(input('Digite um número: '))
temp = n
i = 0
cont = 0

while temp > 0:
    i += 1
    temp -= temp%(10**i)
    x = ((n%(10**i)) - ((n%(10**(i-1)))/(10**(i-1)))
    if x == 2:
        cont += 1

print('O número 2 aparece %d vezes' %cont)'''