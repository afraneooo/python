'''
prg048 - Escreva um programa que leia dois números e imprima todos os números entre eles.
'''
n1 = int(input("N1: "))
n2 = int(input("N2: "))
for x in range(n1+1,n2):
    print(x)