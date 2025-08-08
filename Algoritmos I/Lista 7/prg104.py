'''
prg104 - Crie uma função inverter_lista(lista) que recebe uma lista e retorna uma nova lista com
os elementos invertidos (sem usar [::-1] ou métodos prontos).
'''
def inverter_lista(lista):
  tam = len(lista)
  invertida = []
  for x in range(tam-1,-1,-1):
    invertida.append(lista[x])
  return(invertida)

lista = [1,2,3,4,5,6]
print(inverter_lista(lista))
