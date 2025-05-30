'''
prg071 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,
13,21,34,55,... Faça um programa que seja capaz de gerar até
o enésimo termo.
'''
print("Fibonacci!")
termo = int(input("Gostaria até que termo? "))
n1 = 1
n2 = 1
if termo>2:
    for x in range(2,termo):
        nn = n1+n2
        n1 = n2
        n2 = nn
    print(nn)
else:
    print(1)