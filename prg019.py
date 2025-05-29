'''
Escreva um programa que receba o ano de nascimento de uma pessoa e o ano atual,
calcule e mostre:
- a idade dessa pessoa em anos;
- a idade dessa pessoa em meses;
- a idade dessa pessoa em dias;
- a idade dessa pessoa em semanas.
'''
nasc = int(input("Nascimento: "))
atual = int(input("Ano atual: "))
idA = atual - nasc
idM = idA * 12
idS = idM * 4
idD = idS * 7
print("Idade em anos:",idA)
print("Idade em meses:",idM)
print("Idade em dias:",idD)
print("Idade em semanas:",idS)