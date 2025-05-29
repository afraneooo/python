'''
prg005 - Escreva um programa que leia o radio de uma esfera e informe o seu volume. Considere
para seu cálculo o valor de π = 3,14159
V = 4/3.pi.r³
'''
import math
r = float(input("Insira o raio: "))
v = (4/3)*math.pi*(r**3)
print("O volume da ésfera é: %.2f"%v)