'''
prg064 - Escreva um programa que leia o depósito inicial e a taxa
de juros de uma poupança. Exiba os valores mês a mês para os próximos
24 meses. Escreva o total ganho com juros no período.
'''
def calcula_juros(d, j):
    mensal = d
    for x in range(24):
        mensal += mensal*(j/100)
        print(f"Mês {x+1}: R$ {mensal:.2f}")
    print("Ganhos: R$ %.2f"%(mensal-d))

depo = float(input("Depósito inicial:\n"))
juros = int(input("Taxa de juros:\n"))
calcula_juros(depo, juros)