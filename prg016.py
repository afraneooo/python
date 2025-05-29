'''
Escreva um programa que leia o custo de fábrica de um carro e imprima o custo ao
consumidor. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a
percentagem do distribuidor seja de 28% e os impostos de 45%.
'''
fab = float(input("Custo de fábrica: "))
final = fab+(fab*0.28)+(fab*0.45)
print("Custo final: R$ %.2f"%final)