'''
prg043 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I
para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
'''
kw = float(input("kWh consumido: "))
tipo = input("Tipo de instalação (R/C/I): ")
if tipo != "R" and tipo != "C" and tipo != "I":
    print("Tipo de instalação informado é inválido.")
else:
    if tipo == "R":
        if kw<500:
            preco = 0.4
        else:
            preco = 0.65
    else:
        if tipo == "C":
            if kw<1000:
                preco = 0.55
            else:
                preco = 0.60
        else:
            if tipo == "I":
                if kw<5000:
                    preco = 0.55
                else:
                    preco = 0.60
    print(f"Preço a pagar: R$ {(kw*preco):.2f}")