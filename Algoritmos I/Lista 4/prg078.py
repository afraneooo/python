'''
prg078  -  Escreva  um  programa  que  receba  uma  cadeia  de  caracteres  e  responda  se  a  cadeia 
informada é palíndromo ou não. Crie uma função que verifique se a cadeia recebia é 
palíndromo respondendo True ou False.
'''
def palindromo(palavra):
    tamanho = len(palavra)
    for x in range(tamanho-1):
        if palavra[x] != palavra[tamanho-1-x]:
            return False
    return True

print("!-Verificador de PALÍNDROMO-!")
palavra = input("Informe a palavra: ")
if palindromo(palavra):
    print("É um palindromo!")
else:
    print("Não é um palindromo.")
