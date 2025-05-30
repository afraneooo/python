'''
prg009 - Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a
distância a percorrer e a velocidade média esperada para a viagem.
'''
dist = float(input("Distância (Km): "))
vel = float(input("Velocidade média (km/h): "))
tempo = dist/vel
print("O tempo da viagem será de %.2f horas"%tempo)