'''
prg061-a - Escreva um programa que verifique e informe quais os
100 primeiros números primos.
'''
num,cont2=0,2
while cont2<100:
    cont=0
    for x in range(1,num+1):
        if (num%x)==0:
            cont+=1
    if cont==2:
        cont2+=1
        print(f"Número {cont2}: ",num)
    num+=1