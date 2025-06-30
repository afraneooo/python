'''
prg083 - Escreva um programa que simule o sorteio de dois dados 15 vezes. Ao final imprima a 
lista de números sorteados.
'''
from random import randint

numeros = []
for x in range(15):
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    numeros.append(n1+n2)

print("Números sorteados:",numeros)