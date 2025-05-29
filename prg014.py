'''
Escreva um programa que leia as 3 notas de um aluno e calcule a média final deste
aluno. Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.
'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = ((n1*2)+(n2*3)+(n3*5))/10
print("Média final: %.2f"%media)