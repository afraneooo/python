'''
prg106 - Crie uma função sorteio_nomes(lista_nomes, n) que recebe uma lista de nomes e um
número n, e retorna n nomes aleatórios sem repetição (use random.randint).
'''
from random import choice

def sorteio_nomes(lista_nomes, n):
  if n>len(lista_nomes):
    return None

  sorteados = []
  tam = len(lista_nomes)
  for x in range(n):
    sorteado = choice(lista_nomes)
    while sorteado in sorteados:
      sorteado = choice(lista_nomes)
    sorteados.append(sorteado)
  return(sorteados)

lista = ["carlos", "alberto", "afranio", "camila", "joao", "gilberto", "murilo", "antonio", "moisés"]
print("Sorteados:",sorteio_nomes(lista,3))