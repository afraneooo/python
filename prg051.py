'''
prg051 - Escreva um programa que leia a temperatura inicial de um motor e quantos graus ela
ganha a cada leitura de 10 segundos, por fim calcule e informe quantos graus ela terá após 16
leituras.
'''
temp = float(input("Temperatura:"))
ganho = float(input("Quantos graus aumenta a cada 10s? "))
for x in range (16):
    temp += ganho
print("Após 16 leituras terá: %.1f"%temp)