'''
prg049 - Escreva um programa que execute 5 operações de soma. Para cada operação o
programa deve pedir dois números e informar a soma com o seguinte formato: Soma 1 = 10,
onde o 1 do exemplo representa o número da soma e o 10 o resultado da adição dos dois
números informados.
'''
for x in range(5):
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    print(f"Soma {x+1}: {n1+n2:.1f}")