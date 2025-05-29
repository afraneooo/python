'''
Escreva um programa que leia 2 pontos quaisquer no plano, P(x1, y1) e P(x2, y2), e
escreva a distância entre eles.
'''
import math
print("Ponto 1:")
x1 = float(input("X: "))
y1 = float(input("Y: "))
print("Ponto 2:")
x2 = float(input("X: "))
y2 = float(input("Y: "))
d = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
print("A distância entre os pontos é: %.2f"%d)