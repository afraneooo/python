'''
prg008 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
'''
valor = float(input("Preço: "))
desc = float(input(f"% do Desconto: "))
valor = valor-valor*(desc/100)
print(f"Porcentagem do Desconto: {desc}%")
print("Preço a pagar: R$ %.2f"%valor)