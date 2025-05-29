'''
prg036 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer
em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km,
e R$ 0,45 para viagens mais longas.
'''
dist = float(input("Distância desejada em Km: "))
if dist<=200:
    preco = dist*0.5
else:
    preco = dist*0.45
print("Preço da viagem: R$ %.2f"%preco)