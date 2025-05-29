'''
prg004 - Escreva um programa que leia o raio de um círculo e informe a sua área. Considere para
seu cálculo o valor de π = 3,14159
A = pi.r²
'''
import math
r = float(input("Insira o raio: "))
a = math.pi*(r**2)
print("O área o círculo é: %.2f"%a)