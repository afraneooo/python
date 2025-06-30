'''
Escreva um programa que preencha um vetor de tamanho 10 com números inteiros 
aleatórios entre 1 e 99. Por fim exiba uma lista com os números que não foram sorteados.
'''
from random import randint

numeros = []
naoS = []
for x in range(10):
    numeros.append(randint(1,99))
print("Sorteados:",numeros)
for x in range(1,100):
    if not(x in numeros):
        naoS.append(x)
print("Não sorteados:",naoS)
