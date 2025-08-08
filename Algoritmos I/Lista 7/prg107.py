'''
prg107 - Crie uma função contar_linhas(arquivo.txt) que lê um arquivo .txt e retorna o número
de linhas. Teste com um arquivo criado por você.
'''
#r = ler
#w = criar
#a = adicionar no final

def contar_linhas(nomearq):
  arquivo = open(nomearq,"r")
  cont = 0
  l = arquivo.readline()
  while l!="":
    cont+=1
    l = arquivo.readline()
  # for l in arquivo:
  #   cont += 1
  arquivo.close()
  return cont

arq = input("Informe o nome do arquivo: ")
print("Número de linhas:", contar_linhas(arq))
