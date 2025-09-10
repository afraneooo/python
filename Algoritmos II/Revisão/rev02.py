'''
2) Desenvolver um algoritmo que leia a altura de 15 pessoas.
Este programa deverá calcular e mostrar:
- A menor altura do grupo
- A maior altura do grupo
'''
for x in range(15):
  altura = float(input("Digite a altura: "))
  if x == 0 or altura>maior:
    maior = altura
  if x == 0 or altura<menor:
    menor = altura
print(f"Maior altura: {maior:.2f} m")
print(f"Menor altura: {menor:.2f} m")