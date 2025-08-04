'''
prg105 - Use random.randint(1, 100) para gerar um número aleatório. O usuário deve adivinhar
o número, e o programa informa se o chute foi alto, baixo ou correto (use funções).
'''
from random import randint

def testar_chute(sorteado,chute):
  if chute==sorteado:
    print("Parabéns! Você acertou!")
    return(True)
  else:
    if chute>sorteado:
      print("Opa, chute alto!")
      return(False)
    else:
      print("Eita, chute baixo!")
      return(False)

print("GANBA!\nAdivinhe o número de 1 a 100!")

sorteado = randint(1,100)
acerto = False
while not acerto:
  chute = int(input("Chute um número: "))
  acerto = testar_chute(sorteado,chute)