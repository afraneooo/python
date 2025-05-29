'''
prg034 - Escreva um programa que leia três números e que imprima o maior e o menor.
'''
n1 = float(input("Número 1:"))
n2 = float(input("Número 2:"))
n3 = float(input("Número 3:"))

if n2<n1:
    n2, n1 = n1, n2
if n3<n2:
    n3,n2 = n2, n3
if n2<n1:
    n2, n1 = n1, n2
    
print(f"Menor: {n1}\nMaior: {n3}")