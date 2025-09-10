'''
3) Desenvolver um algoritmo que leia 20 números inteiros e calcule e escreva
a média aritmética dos valores lidos, a quantidade de valores positivos,
a quantidade de valores negativos e o percentual de valores negativos e positivos.
'''
soma, contPos, contNeg = 0,0,0
for x in range(20):
  num = int(input("Digite um número: "))
  soma += num
  if num >0:
    contPos +=1
  elif num <0:
    contNeg +=1
print("Média:",soma/20)
print("Total positivos:",contPos)
print("Total negativos:",contNeg)
print(f"{(contPos*100)/20}% são positivos e {(contNeg*100)/20}% negativos")