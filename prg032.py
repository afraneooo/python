'''
prg032 - Escreva um programa que receba o custo diário de transporte, o salário por dia de um
funcionário e a quantidade de dias que este trabalhou no mês. Seu programa deve calcular o
desconto do vale transporte considerando que este desconto seja o menor valor entre 6% do
seu salário ou o valor do vale transporte. Dica: Calcule o custo de transporte e o salário mensal
do funcionário para efetuar os cálculos do desconto do vale transporte.
'''
transporte = float(input("Valor da passagem: "))
sal = float(input("Salário diário: "))
dias = int(input("Dias trabalhados: "))
sal = sal*dias
transporte = transporte*dias*2
seis = sal*(6/100)
if seis < transporte:
    sal -= seis
    print("Salário s/ desconto: R$ %.2f"%(sal+seis))
    print("Desconto do VT: R$ %.2f"%seis)
    print("Salário: R$ %.2f"%sal)
else:
    sal -= transporte
    print("Salário s/ desconto: R$ %.2f"%(sal+transporte))
    print("Desconto do VT: R$ %.2f"%transporte)
    print("Salário: R$ %.2f"%sal)
