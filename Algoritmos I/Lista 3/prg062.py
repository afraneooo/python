'''
prg062 - Crie um programa para verificar se um termo é palíndromo.
'''
termo = input("Digite um termo:\n")
tam = len(termo)
pali = True
for x in range(tam):
    if termo[x]!=termo[tam-x-1]:
        print("Não é palindromo.")
        pali = False
        break
if pali:
    print("É palindromo.")