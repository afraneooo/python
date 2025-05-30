'''
prg007 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do
salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
'''
sal = float(input("Salário: "))
aumento = float(input("'%' do aumento: "))
sal = sal+(sal*(aumento/100))
print(f"Porcentagem do aumento: {aumento}%")
print("Novo salário: R$ %.2f"%sal)