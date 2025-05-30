'''
prg063 - Escreva um programa que leia um número e calcule
e informe o fatorial deste número
'''
num = int(input("Digite um número:\n"))
fat = 1
for x in range(1,num+1):
    fat *= x
print(fat)