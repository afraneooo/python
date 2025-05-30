'''
prg056 - Escreva um programa que leia números até que um número negativo seja lido. Seu
programa ao final do processamento deve exibir a soma, a quantidade e a média dos números
lidos.
'''
x=0
cont=0
soma=0
x = float(input("Digite um número:\n"))
while x>=0:
    soma += x
    cont += 1
    x = float(input("Digite um número:\n"))
print("Soma dos números: %.1f"%soma)
print("Quantidade lida: %d"%cont)
print("Média dos números: %.1f"%(soma/cont))
