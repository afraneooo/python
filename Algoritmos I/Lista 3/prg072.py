'''
prg072 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,
13,21,34,55,... Faça um programa que gere até que
o valor seja maior que 500.
'''
print("Fibonacci!")
n1 = 0
n2 = 1
print(n1)
print(n2)
while n2<500:
    nn = n1+n2
    n1 = n2
    n2 = nn
    print(n2)