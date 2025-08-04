'''
prg106 - Crie uma função sorteio_nomes(lista_nomes, n) que recebe uma lista de nomes e um
número n, e retorna n nomes aleatórios sem repetição (use random.randint).
'''
from random import randint

def sorteio_nomes(lista_nomes, n):
  sorteados = []
  tam = len(lista_nomes)
  for x in range(n):
    sorteado = randint(0,tam-1)
    while lista_nomes[sorteado] in sorteados:
      sorteado = randint(0,tam-1)
    sorteados.append(lista_nomes[sorteado])
  return(sorteados)

lista = ["carlos", "alberto", "afranio", "camila", "joao", "gilberto", "murilo", "antonio", "moisés"]
print(sorteio_nomes(lista,3))