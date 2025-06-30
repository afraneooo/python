'''
prg082 - Escreva  um  programa  que  leia  o  nome  e  as  duas  notas  de  20  alunos.  Após  o 
processamento  de  todos  os  alunos,  informe  o  nome  e  a  média  dos  aprovados.  Os  aprovados 
têm média maior ou igual a 6. 
'''
alunos = []
media = []

for x in range(20):
    nome = input("Nome do aluno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    alunos.append(nome)
    media.append(float((n1+n2)/2))

print("Alunos aprovados:")
for x in range(len(alunos)):
    if media[x]>=6:
        print(f"{alunos[x]} com média {media[x]:.1f}")





    