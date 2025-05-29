'''
prg053 – Escreva um programa que leia a descrição, o preço e a quantidade de 4 itens de um
supermercado. Seu programa deve calcular e informar para cada item o seu subtotal ( preço x
quantidade ). Seu programa por fim deve informar o total a pagar e ler o valor que o cliente
deu para pagar. Para finalizar seu programa deve informar o troco.
'''
total = 0
for x in range(4):
    desc = input("Descrição: ")
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade: "))
    subtotal = preco * qtd
    print("Subtotal: %.2f"%subtotal)
    total += subtotal
print("Total: %.2f"%total)