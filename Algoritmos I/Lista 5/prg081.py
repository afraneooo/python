'''
prg081 - Escreva um programa que  leia 10 números inteiros e calcule a média aritmética. Ao 
final informe quantos números estão acima da média. 
'''
numeros = []
soma = 0
cont = 0
for i in range(10):
    n = int(input("Informe um número: "))
    numeros.append(n)
    soma+=n
media = soma / 10
print("Média:",media)
for n in numeros:
    if n>media:
        cont+=1
print(cont,"estão acima da média")