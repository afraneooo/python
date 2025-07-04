'''
prg090 - Escreva um programa que leia 3 números inteiros N, I e F. Sendo N, a quantidade de 
números a serem sorteados, e I e F o intervalo de números do sorteio. Por fim exiba os números 
sorteados.  
'''
from random import randint

sorteados = []
entrada = input().split()
n = int(entrada[0])
i = int(entrada[1])
f = int(entrada[2])
if i>f:
    i,f = f,i
for x in range(n):
    sorteados.append(randint(i,f))
print(sorteados)
