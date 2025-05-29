'''
prg030 - Escreva um programa que leia o nome e o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
p1Nome = input("Nome produto 1: ")
p1Preco = float(input("Preço produto 1: "))
p2Nome = input("Nome produto 2: ")
p2Preco = float(input("Preço produto 2: "))
p3Nome = input("Nome produto 3: ")
p3Preco = float(input("Preço produto 3: "))
if p1Preco < p2Preco and p1Preco < p3Preco:
    print(f"Compra o {p1Nome} fio!")
else:
    if p2Preco < p3Preco:
        print(f"Compra o {p2Nome} fio!")
    else:
        print(f"Compra o {p3Nome} fio!")