'''
prg055 - Escreva um programa que leia 800 pesquisas. Para cada pesquisa pergunta-se a
idade, se tem internet em casa, caso tenha pergunte a velocidade da internet, se tem celular
com acesso a internet, se tem computador e se tem tablet. 
Seu programa ao final deve informar:
a média da idade das pessoas pesquisadas,
o percentual de pessoas que tem internet em casa,
a média de velocidade dessa internet,
o percentual de pessoas que tem celular,
o percentual que tem computador,
e o percentual que tem tablet.
'''
tid = 0
tnet = 0
tvel = 0
tcel = 0
tpc = 0
ttab = 0
y = 3
for x in range(800):
    print("Registro %d"%(x+1))
    tid += int(input("Idade: "))
    net = int(input("Acesso à internet (0-Não/1-Sim): "))
    if net==1:
        tnet +=1
        tvel += int(input("Velocidade: "))
        cel = int(input("Celular (0/1): "))
        if cel == 1:
            tcel +=1
        pc = int(input("Computador (0/1): "))
        if pc == 1:
            tpc +=1
        tab = int(input("Tablet (0/1): "))
        if tab == 1:
            ttab +=1
print(f"Média das idades: {tid/y:.0f}")
print(f"{tnet*100/y:.0f}% tem internet em casa.")
print(f"A velocidade média é de {tvel/tnet:.1f} Megas")
print(f"{tcel*100/y:.0f}% tem celular.")
print(f"{tpc*100/y:.0f}% tem computador.")
print(f"{ttab*100/y:.0f}% tem tablet.")