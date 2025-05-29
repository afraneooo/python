'''
prg035 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do
aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os
inferiores ou iguais, de 15%.
'''
sal = float(input("Salário: "))
if sal > 1250:
    sal += sal*(10/100)
else:
    sal += sal*(15/100)
print("Novo salário: R$ %.2f"%sal)