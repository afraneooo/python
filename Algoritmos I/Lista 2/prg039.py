'''
prg039 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a
pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da
prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
'''
casa = float(input("Valor da casa: "))
sal = float(input("Salário: "))
anos = int(input("Anos a pagar: "))
prestacao = casa/(anos*12)
limite = sal*0.3
if prestacao < limite:
    print("Aprovado!\nValor da prestação: R$ %.2f"%prestacao)
else:
    print("Não aprovado.")