'''
prg084 - Escreva um programa que gere um jogo de 6 dezenas da megasena com números de 
1 a 60. Ao final imprima os números sorteados no seguinte formato: 10 - 19 - 7 - 54 - 2 - 18
'''
from random import randint

numeros = []
for x in range(6):
    numeros.append(randint(1,60))
    if x<5:
        print(numeros[x], end=" - ")
    else:
        print(numeros[x])