'''
prg057 - Atualize o seu programa anterior para exibir o maior e o menor número lido.
'''
x=0
cont=0
soma=0
maior=0
menor=0
while True:
    x = float(input("Digite um número:\n"))
    if x<0:
        break
    soma += x
    cont += 1
    if x>=maior or cont==1:
        maior = x
    if x<=menor or cont==1:
        menor = x
print("Soma dos números: %.1f"%soma)
print("Quantidade lida: %d"%cont)
print("Média dos números: %.1f"%(soma/cont))
print("Maior número lido: %.1f"%maior)
print("Menor número lido: %.1f"%menor) 