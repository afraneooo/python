'''
prg037 - Escreva um programa que leia dois números e que pergunte qual operação você
deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada.
'''
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
opera = input("Operação (+,-,*,/): ")
if opera == "+":
    print("Resultado: %.2f"%(n1+n2))
else:
    if opera == "-":
        print("Resultado: %.2f"%(n1-n2))
    else:
        if opera == "*":
            print("Resultado: %.2f"%(n1*n2))
        else:
            if opera == "/":
                print("Resultado: %.2f"%(n1/n2))
            else:
                print("Operador inválido!")
