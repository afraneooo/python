'''
prg027 - Escreva um programa baseado no prg026, mas inclua na leitura o percentual de
frequência do aluno. Se o aluno obtiver um percentual menor que 75, estará reprovado não
importando a sua média.
'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
freq = int(input("Frequência: "))
media = (n1+n2)/2
if freq>=75:   
    print("A média do aluno é %.1f"%media)
    if media>=6:
        if media==10:
            print("Aprovado com Distinção")
        else:
            print("Aprovado")
    else:
        print("Reprovado")
else:
    print("Reprovado")