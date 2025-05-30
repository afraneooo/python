'''
Escreva um programa que leia um número inteiro qualquer com 3 algarismos e o
informe de traz pra frente.
'''
num = int(input("Digite um número de 3 algarismos: "))
c1 = num // 100
c2 = num % 100 // 10
c3 = num % 100 % 10
num = (c3*100)+(c2*10)+c1
print("Invertido: %d"%num)
