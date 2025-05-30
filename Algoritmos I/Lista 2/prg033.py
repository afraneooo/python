'''
prg033 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso
ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
'''
vel = float(input("Velocidade em km/h: "))
if vel > 80:
    print("MULTA!")
    multa = (vel-80)*5
    print("Valor a pagar: R$ %.2f"%multa)
else:
    print("Tá tranquilo...")