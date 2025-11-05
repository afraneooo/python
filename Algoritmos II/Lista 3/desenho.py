from retangulo import Retangulo

class Desenho:
  def __init__(self):
    self.__desenho = []

  def adiciona_figura(self, figura):
    self.__desenho.append(figura)
  
  def remove_figura(self, figura):
    self.__desenho.remove(figura)

  def listar_figuras(self):
    lista_str = ""
    for d in self.__desenho:
      lista_str += f"{d}\n"
    return lista_str
  