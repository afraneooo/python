'''
prg102  -  Crie  uma  função eh_palindromo(texto)  que recebe  uma  string e  retorna  True  se  for 
um palíndromo (ex: "arara") ou False caso contrário.
'''

def eh_palindromo(texto):
  tam = len(texto)
  for x in range(tam):
      if texto[x] != texto[tam-1-x]:
          return False
  return True

print("Verificador de palíndromo.")

texto = input("Digite a palavra:\n")
if eh_palindromo(texto):
   print("É palíndromo")
else:
   print("Não é palíndromo")