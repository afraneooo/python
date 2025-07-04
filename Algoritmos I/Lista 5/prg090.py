'''
prg090 - Escreva um programa que leia 3 números inteiros N, I e F. Sendo N, a quantidade de 
números a serem sorteados, e I e F o intervalo de números do sorteio. Por fim exiba os números 
sorteados.  
'''
from random import randint

sorteados = []
n = int(input("Números a serem sorteados: "))
i = int(input("Intervalo inicial: "))
f = int(input("Intervalo final: "))
for x in range(n):
    sorteados.append(randint(i,f))
print(sorteados)
