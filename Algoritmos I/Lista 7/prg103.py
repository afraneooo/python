'''
prg103 - Crie  uma  função  maior_menor(lista)  que  recebe  uma  lista  de  números  e  retorna  o 
maior e o menor valor (em uma tupla). Exemplo de entrada: [5, 2, 9, 1] → Saída: (9, 1).
'''

def maior_menor(lista):
  tam = len(lista)
  for x in range(tam):
    if x==0 or lista[x]>maior:
      maior = lista[x]
    if x==0 or lista[x]<menor:
      menor = lista[x]
  tupla = (maior,menor)
  return (tupla)

lista = [5,2,9,1]
print(maior_menor(lista))
