'''
prg026 - Escreva um programa para a leitura de duas notas de um aluno. O programa deve
calcular a média alcançada pelo aluno e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;
• A mensagem "Reprovado", se a média for menor do que seis;
• A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1+n2)/2
print("A média do aluno é %.1f"%media)
if media>=6:
    if media==10:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")