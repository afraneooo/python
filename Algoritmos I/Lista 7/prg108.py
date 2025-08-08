'''
prg108 - Crie um programa que gera 10 números aleatórios (entre 1 e 100) usando randint e os 
salva  em  um  arquivo  numeros.txt  (um  por  linha).  Depois,  leia  o  arquivo  e  exiba  a  soma  dos 
números. 
'''
from random import randint

def criar_arquivo():
  arquivo = open("numeros.txt","w")
  for x in range(10):
    num = randint(1,100)
    arquivo.write(str(num)+"\n")
  arquivo.close()

def ler_e_somar():
  arquivo = open("numeros.txt","r")
  soma = 0
  for l in arquivo:
    soma += int(l)
  print("Soma:", soma)
  arquivo.close()

criar_arquivo()
ler_e_somar()