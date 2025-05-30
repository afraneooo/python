'''
prg052 – Escreva um programa que leia 10 números reais e por fim informe a soma dos
números lidos.
'''
print("Cálculo de soma!")
soma = 0
for x in range(10):
    soma += float(input("Insira um número: "))
print("Soma: %.1f"%soma)