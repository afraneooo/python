from figura_geometrica import FiguraGeometrica

class Retangulo(FiguraGeometrica):
  def __init__(self, base=None, altura=None):
    super().__init__(base)
    self.__altura = altura
  
  def get_altura(self):
    return self.__altura

  def set_altura(self, altura):
    self.__altura = altura
  
  def calcula_area(self):
    return self.__altura * self.get_base()
  
  def calcula_perimetro(self):
    return 2*self.__altura + 2*self.get_base()

  def __str__(self):
    return f"Retângulo " + super().__str__() + f" altura={self.__altura}"