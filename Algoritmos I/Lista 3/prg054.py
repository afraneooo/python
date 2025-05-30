'''
prg054 - Escreva um programa que leia a quantidade de votos a serem lidos. Para cada voto o
usuário digita 0 para branco, 1 para o candidato Bráulio e 2 para a candidata Theresa. Se
digitar qualquer número diferente deve computar como nulo. Seu programa deve informar ao
final a quantidade de votos e o percentual de cada um. (Branco, Nulos, Bráulio e Thereza)
'''
qtd = int(input("Votos: "))
branco = 0
braulio = 0
theresa = 0
nulo = 0
for x in range(qtd):
    voto = int(input("Digite o candidato: "))
    if voto == 0:
        branco+=1
    else:
        if voto ==1:
            braulio+=1
        else:
            if voto==2:
                theresa+=1
            else:
                nulo+=1
print(f"Branco: {branco} votos | {100*branco/qtd:.0f}%")
print(f"Braulio: {braulio} votos | {100*braulio/qtd:.0f}%")
print(f"Theresa: {theresa} votos | {100*theresa/qtd:.0f}%")
print(f"Nulo: {nulo} votos | {100*nulo/qtd:.0f}%")