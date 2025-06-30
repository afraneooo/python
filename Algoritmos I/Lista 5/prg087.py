'''
prg087 - Escreva  um  programa  que  preencha  um  vetor  com  números  aleatórios  até  que  o 
número 1 seja sorteado. Ao final informe quantos números foram sorteados excetuando-se o 1.
'''
from random import randint

numeros = []
while not(1 in numeros):
    numeros.append(randint(1,100))
del numeros[len(numeros)-1]
print(numeros)
