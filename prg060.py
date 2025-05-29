'''
prg060 - Escreva um programa que leia um número e informe a tabuada deste número no
seguinte formato: 2 x 1 = 2 e etc.
'''
num = int(input("Digite um número:\n"))
tabuada = 1
while tabuada <= 10:
    print(f"{num} x {tabuada} = {num*tabuada}")
    tabuada += 1