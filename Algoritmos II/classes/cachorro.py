class Cachorro:
  #método construtor
  def __init__(self, nome, raca, porte):
    self.__nome = nome
    self.__raca = raca
    self.__porte = porte

  def latir(self):
    print(f"{self.__nome}: Au! Au!")

  def get_nome(self):
    return self.__nome
  def set_nome(self, nome):
    self.__nome = nome

# principal

cachorro1 = Cachorro("Bob","pitbull","pequeno")
cachorro1.latir()
cachorro1.set_nome("Roberto")
cachorro1.latir()