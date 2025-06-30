'''
prg085 - Escreva um programa que gere um jogo de 6 dezenas da megasena com números de 
1 a 60. Aprimore o programa anterior não permitindo números repetidos.
'''
from random import randint

numeros = []
for x in range(6):
    numero = randint(1,60)
    while numero in numeros:
        numero = randint(1,60)
    numeros.append(numero)
    if x<5:
        print(numeros[x], end=" - ")
    else:
        print(numeros[x])
