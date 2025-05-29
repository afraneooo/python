'''
prg050 - Escreva um programa que leia o nome e a as três notas de 6 alunos. Seu programa
deve calcular e informar a média ponderada, onde as notas têm os pesos 2, 3 e 5
respectivamente. Seu programa também deve informar o grau do aluno, aprovado para notas
maiores ou iguais a 6 e em recuperação para as notas menores que 6.
'''
for x in range(6):
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    media = ((2*nota1)+(3*nota2)+(5*nota3))/10
    print("Média: %.2f"%media)
    if media>=6:
        print("Aprovado!")
    else:
        print("Recuperação.")