'''
prg012 - Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que
um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante
perderá. Exiba o total em dias.
'''
cigarros = int(input("Cigarros por dia: "))
anos = int(input("Anos fumando: "))
perda = round((((cigarros*10)/60)/24)*(365*anos))
print("Essa pessoa já perdeu %d dias de vida..."%perda)