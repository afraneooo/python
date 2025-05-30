'''
prg058 - Escreva um programa que faça orçamentos de um determinado produto. Leia o
nome da loja e o preço do produto de diversos orçamentos. Faça seu programa perguntar se
deseja continuar ou finalizar após ler cada orçamento. Por fim deve informe o nome da loja
onde o produto seja mais barato e preço praticado.
'''
ler=1
barato=0
while ler==1:
    loja = input("Nome da loja:\n")
    preco = float(input("Preço do produto:\n"))
    if preco<=barato or barato==0:
        barato = preco
    ler = int(input("Deseja continuar? (0/1)\n"))
print("O produto mais barato é da loja %s por apenas R$ %.2f"%(loja,barato))