'''
Escreva um programa que receba o valor dos catetos de um triângulo, calcule e mostre
o valor da hipotenusa.
'''
import math
a = float(input("Cateto A: "))
b = float(input("Cateto B: "))
c = math.sqrt((a**2)+(b**2))
print("Hipotenusa: %.2f"%c)
