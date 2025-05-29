'''
prg061 - Escreva um programa que leia um número e verifique e informe se ele é ou não
primo:
'''
num = int(input("Digite um número:\n"))
br = 0
for x in range(2,num):
    if (num%x)==0:
        print("Não é primo!")
        br = 1
        break
if br==0:
    print("É primo!")