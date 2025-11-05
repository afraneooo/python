from figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
  def __init__(self, base=None):
    super().__init__(base)

  def calcular_altura(self):
    return self.get_base() * (3**0.5) / 2
  
  def calcular_area(self):
    return self.get_base() * self.calcular_altura / 2
  
  def calcular_perimetro(self):
    return 3 * self.get_base()
  
  def __str__(self):
    return 