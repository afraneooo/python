'''
prg076 - Escreva um programa que receba um número e responda se o mesmo é ou não é
primo. Use uma função para verificar se o número é primo.
'''
def ehprimo(n):
    cont = 0
    for x in range(1,n+1):
        if (n%x)==0:
            cont+=1
    if cont==2 and n!=1:
        return True
    else:
        return False
    
for x in range(0,1000):
    if ehprimo(x):
        print(x)