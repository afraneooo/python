'''
prg022 - Escreva um programa que peça um valor e mostre na tela se o valor é positivo ou
negativo.
'''
num = float(input("Digite um número: "))
if num>0:
    print("Esse número é positivo")
else:
    if num==0:
        print("O número é zero!")
    else:
        print("O número é negativo!")