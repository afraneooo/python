'''
prg101 - Crie uma função soma_numeros(a, b, c) que recebe três números como parâmetros e
retorna a soma deles. Peça ao usuário para inserir os valores e exiba o resultado.
'''

def soma_numeros(a, b, c):
  return(c+b+a)

print("Soma de 3 números.")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

print(soma_numeros(n1,n2,n3))