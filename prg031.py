'''
prg031 - Escreva um programa que leia os valores da gasolina e do etanol de um determinado
posto de abastecimento de combustível. Seu programa deve verificar e informar qual
combustível é mais vantajoso para o cliente, considerando que o etanol rende 30% menos que
a gasolina.
'''
etanol = float(input("Preço da Etanol: "))
gasolina = float(input("Preço da Gasolina: "))
etanol += etanol*(30/100)
if gasolina > etanol:
    print("Vale mais abastecer com Etanol!")
else:
    if gasolina == etanol:
        print("Qualquer um vale a pena!")
    else:
        print("Vale mais abastecer com Gasolina!")