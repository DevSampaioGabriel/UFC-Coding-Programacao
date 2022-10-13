#Aula 8 revisão de tudo que já vimos
#Exercício 1
'''
import math
cateOpo = float(input('Insira o cateto oposto: '))
cateAdj = float(input('Insira o cateto adjacente: '))

hipote = math.sqrt((cateOpo**2) + (cateAdj**2))
print(f'A hipotenusa tem o comprimento de {hipote:.2f}')
'''
#Exercício 2
'''
compra_total = float(input('Digite o valor total da compora: $'))
desconto = 0.07
taxa = 1 - desconto
valor_descontado = compra_total * taxa
print(f'A compra total foi: ${compra_total}\nA compra total com desconto é de: ${valor_descontado:.2f}')
'''
#Exercício 3
'''
custo_show = float(input('Quanto custa fazer um show do Tirulipa? $')) 
ingresso = float(input('Quanto vai ser o ingresso para o show? $'))
ingressos_custo = custo_show / ingresso
lucro_ingresso = (custo_show*1.23) / ingresso 
print(f'A quantidade de ingressos para alcançar o custo do show é: {ingressos_custo:.0f}\nA quantidade de ingressos para obter lucro de 23% é: {lucro_ingresso:.0f}')
'''
#Exercício 4
'''
menor_ate_agora = int(input("Insira um número: "))
maior_ate_agora = menor_ate_agora
for i in range(4):
    valores = int(input('Insira um número: '))
    if valores < menor_ate_agora:
        menor_ate_agora = valores
    
    if valores > maior_ate_agora:
        maior_ate_agora = valores
print(f'O maior número é: {maior_ate_agora}')
print(f'O menor até agora é: {menor_ate_agora}')
'''
#Exercício 5
'''
primeiro_elemento = int(input('Digite o primeiro elemento: '))
razao = int(input('Digite a razão da P.A: '))
N = int(input('Quantos elementos exibir: '))
print(primeiro_elemento)
for i in range(N-1):
    primeiro_elemento += razao
    print(primeiro_elemento)
'''

#Exercício 6
'''
primeiro_elemento = int(input('Digite o primeiro elemento: '))
razao = int(input('Digite a razão da P.G: '))
N = int(input('Quantos elementos exibir: '))
print(primeiro_elemento)
for i in range(N-1):
    primeiro_elemento *= razao
    print(primeiro_elemento)
'''
#Exercício 7
'''
opcao = input('Insira uma das opções de média:\na)Geométrica\nb)Ponderada\nc)Harmônica\nd)Aritmética\nEscolha a opção: ')
x = int(input('Digite o primeiro número: '))
y= int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))
if opcao == 'a' or opcao == 'A':
    media = (x*y*z)**(1/3)
elif opcao == 'b' or opcao == 'B':
    media = (x + 2*z + 3*y)/6

elif opcao == 'c' or opcao == 'C':
    media = 1/((1/x)+(1/y)+(1/z))
else:
    media = (x+y+z)/3
print(f'A media da opção {opcao} é {media:.1f}')
'''
