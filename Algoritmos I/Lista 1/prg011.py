'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule
o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''
km = float(input("Km percorrido: "))
dias = float(input("Dias alugados: "))
valor = (dias*60) + (km*0.15)
print("Valor total a ser pago: R$ %.2f"%valor)