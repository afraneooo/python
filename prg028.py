'''
prg028 - Escreva um programa que leia o nome, gênero e estado civil de uma pessoa. Caso a
pessoa seja casada e do gênero “F”, peça também o tempo do casamento em anos.
'''
nome = input("Nome: ")
gen = input("Gênero: ")
estCivil = input("Estado civil: ")
if gen=="f" and estCivil=="c":
    casamento = input("Tempo do casamento em anos: ")