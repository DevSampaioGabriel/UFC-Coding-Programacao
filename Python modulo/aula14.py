#Aula sobre CSV
import csv

#Escrever no arquivo csv. 'csv.writer' é o comando para escrever no arquivo csv. '.writerow()' para escrever uma lista em cada linha.
'''
arquivo = open('./teste.csv', 'a', encoding='utf-8')
arquivoEscrevivel = csv.writer(arquivo)

novasPessoas = [
    ["Matue", "5", "Orégano"],
    ["Pica Pau", "4", "Bolo de murango"],
    ["He-man", "3", "Esqueleto"]
]

for pessoa in novasPessoas:
    arquivoEscrevivel.writerow(pessoa)

'''

#Escrever as informações do arquivo txt no arquivo csv.

with open('texto.txt', 'r', encoding='utf-8') as arquivoDeNotas:
    arquivoCsvDeNotas = open('aluno.csv', 'a', newline='', encoding='utf-8')
    arquNotasEscrevivel = csv.writer(arquivoCsvDeNotas)
    linhasDoArquivoDeNotas = arquivoDeNotas.readlines()
    arquNotasEscrevivel.writerow(['nome do aluno', 'nota'])
    for linha in linhasDoArquivoDeNotas:
        linhaSplitada = linha.split(',')
        arquNotasEscrevivel.writerow([linhaSplitada[0], linhaSplitada[1].strip()])
    arquivoCsvDeNotas.close()

