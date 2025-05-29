'''
prg021 - Escreva um programa que peça dois números e imprima o maior deles.
'''
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
if n1>n2:
    print(n1,"é o maior!")
else:
    if n1==n2:
        print("Eles são iguais!")
    else:
        print(n2,"é o maior!")