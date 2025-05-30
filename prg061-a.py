'''
prg061-a - Escreva um programa que verifique e informe se um número é primo
ou não até 1000.
'''
cont = 0
for num in range(2,1000):
    for x in range(1,num+1):
        if (num%x)==0:
            cont+=1
        if cont==2:
            print(num)