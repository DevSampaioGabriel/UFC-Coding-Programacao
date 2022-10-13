#Funções - parte 2
#Treino 1 - dois jeitos de fazer, um atribui o for dentro da função.
'''
string_a_ser_cortada = str(input('Digite uma palavra: '))

def cortadorDePalavras (string):
    stringCortada = []
    for letra in string:
        stringCortada.append(letra)
    return stringCortada


def cortadorDePalavras (string):
    for palavra in string:
        stringCortada = []
        for letra in string:
            stringCortada.append(letra)
        print(string_a_ser_cortada)

cortadorDePalavras(range(0, 2))
cortadorDePalavras(string_a_ser_cortada[1])
cortadorDePalavras(string_a_ser_cortada[2])

for palavra in string_a_ser_cortada:
    print(cortadorDePalavras(palavra))
print('\n')
for palavra in range(0, 3):
    print(cortadorDePalavras(string_a_ser_cortada[palavra]))
'''
#Treino 2 - Podemos utilizar o def com if, else, elif para remover coisas de uma lista.
'''
listaDePessoas = ['Rafael', 'Yasser', 'Gabriel', 'Elias']

def apagarPessoaDaLista(nomeDaPessoa, listaDePessoas):
    if nomeDaPessoa in listaDePessoas:
        listaDePessoas.remove(nomeDaPessoa)
    else:
        print('Pessoa não encontrada')
apagarPessoaDaLista('Rafael', listaDePessoas)
print(listaDePessoas)
apagarPessoaDaLista('Thiago', listaDePessoas)
'''
#Treino 3 - '*' utiliza o asterisco para indicar que vai receber vários argumentos.
'''
def printarIngredientes(*ingredientes):
    print('A pizza será feita com os seguintes ingredientes: ')
    for ingrediente in ingredientes:
        print(ingrediente)


printarIngredientes('Tomate', 'carne', 'Peperone', 'queijo', 'bacon')
'''
#Treino 4 - '**' utiliza dois asteriscos para atribuir uma chave e um valor.
'''
def ingredientesDaPizza(numeroDoPedido, **ingredientes):
    print(f'Ingredientes do pedido {numeroDoPedido}')
    for chave, valor in ingredientes.items():
        print(f'{chave}: {valor}')


ingredientesDaPizza(12, sabor_carne =  'carne', sabor_peperone = 'Peperone', sabor_queijo = '4 queijos', borda = 'recheada', com_cebola = 'Sim' )
'''
#Treino 5 - A função 'lambda' não precisa usar 'def exemplo():'.
'''
porcentagem = lambda preço: preço*0.3
#Básicamente declaramos uma função dentro de uma váriavel sem usar 'def'.
print(porcentagem(10))
#Podemos utilizar uma função 'def' com 'lambda'
def porcentagem (preco)

'''



