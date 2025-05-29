'''
prg059 - Escreva um programa que leia o nome e o peso em kg que diversos atletas estão
levantando em uma competição. Seu programa deve finalizar quando o nome “fim” for
digitado no nome e informar o nome do medalhista de ouro.
'''
maior=0
nome = input("Nome do atleta:\n")
while nome!="fim":
    peso = float(input("Peso levantado:\n"))
    if peso>=maior:
        maior = peso
        ganhador = nome
    nome = input("Nome do atleta:\n")    
print("O ganhador foi o grandioso %s carregando incríveis %.1f Kg"%(ganhador,maior))