'''
prg089 - Escreva um programa que gere 10 cartelas de bingo com 25 números não repetidos 
entre 1 e 75. Imprima os números de cada cartela na tela.
'''
from random import randint

cartelas = []
cartela = []

for x in range(10):
    for y in range(25):
        num = randint(1,75)
        while num in cartela:
            num = randint(1,75)
        cartela.append(num)
    cartelas.append(cartela)
    cartela = []

for x in range(10):
    print(f"Cartela {x+1}:",cartelas[x])