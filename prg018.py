'''
Escreva um programa que receba o salário fixo de um funcionário e o valor de suas
vendas, calcule e mostre a comissão e o salário final do funcionário. Um funcionário recebe um
salário fixo mais 4% de comissão sobre as vendas. 
'''
sal = float(input("Salário: "))
vendas = float(input("Vendas: "))
comissao = vendas*0.04
total = sal+comissao
print("Comissão: R$ %.2f"%comissao)
print("Salário final: R$ %.2f"%total)
