'''
prg088 - Escreva um programa que preencha um vetor com os nomes fornecidos pelo usuário. 
Ao final, quando o usuário digitar o usuário de nome 'fim', sorteie um nome que vencerá uma 
rifa.
'''
from random import choice
'''nomes = []
nome = input("Digite o nome:\n")
if nome!="fim":
    nomes.append(nome)
while nome!="fim":
    nome = input("Digite o nome:\n")
    if nome!="fim":
        nomes.append(nome)
print(choice(nomes))'''

nomes = []
while not("fim" in nomes):
    nomes.append(input("Digite o nome:\n"))
del nomes[len(nomes)-1]
print(choice(nomes))


