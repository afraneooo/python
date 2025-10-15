'''
Crie uma classe chama Triangulo que represente um triangulo equilátero.
O atributo de classe deve ser a base. A classe deve ter métodos para calcular a altura, a área e o perímetro.
Encapsule a base e crie um método para receber o valor.
'''
class Triangulo:
  def __init__(self,base=None):
    self.__base = base

  def getBase(self):
    return self.__base
  def setBase(self, base):
    self.__base = base

  def altura(self):
    return (self.__base*(3**(1/2)))/2
  
  def area(self):
    return (self.__base*self.altura())/2
  
  def perimetro(self):
    return self.__base*3
  
  def __str__(self):
    return f"Base: {self.__base}\nAltura: {self.altura():.2f}\nÁrea: {self.area():.2f}\nPerímetro: {self.perimetro()}"

# programa principal
t1 = Triangulo()
t1.setBase(5)
print(t1)
t2 = Triangulo(7)
print(t2)


