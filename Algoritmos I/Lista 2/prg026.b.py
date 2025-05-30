'''
prg026 - Escreva um programa para a leitura de duas notas de um aluno. O programa deve
calcular a média alcançada pelo aluno e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;
• A mensagem "Reprovado", se a média for menor do que três;
• A mensagem "Recuperação", se a média for maior ou igual a três e menor do que seis;
'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1+n2)/2
print("Média: %.1f"%media)
if media>=6:
    print("Aprovado")
else:
    if media<3:
        print("Reprovado")
    else:
        print("Recuperação")