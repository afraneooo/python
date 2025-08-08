'''
prg109 - Use um arquivo palavras.txt com uma palavra por linha. Leia o arquivo
e escolha uma palavra aleatória. Crie uma função jogar_forca(palavra) que
gerencia o jogo (chances limitadas, exibe letras acertadas). 
'''
from random import randint

def jogar_forca(palavra):
  tamanho = len(palavra)-1
  erros, acertos = 0, 0
  letras, morte = [], []
  while erros < 5:
    print("Vidas:",5-erros)
    for x in range(tamanho):
      if palavra[x] not in letras:
        print("_",end=" ")
      else:
        print(palavra[x],end=" ")
    if acertos == tamanho:
      print("\nParabéns! Você ganhou!")
      break
    letra = input("\nDigite uma letra: ")
    if letra in palavra:
      if letra in letras:
        print("Epa! Letra já usada!")
      else:
        letras.append(letra)
        for x in range(tamanho):
          if palavra[x] == letra:
            acertos+=1
    else:
      if letra in morte:
        print("Epa! Letra já usada!")
      else:
        morte.append(letra)
        erros+=1
        if erros<5:
          print("\nVocê errou!")
          print("Letras já usadas:",morte)
        else:
          print("Você errou x.x")
          print("\n-=[GAME OVER]=-\n")

arquivo = open("palavras.txt", "r")
sorte = randint(1,10)
l = arquivo.readline()
cont = 1
while cont != sorte:
  l = arquivo.readline()
  cont+=1
jogar_forca(l)
arquivo.close()