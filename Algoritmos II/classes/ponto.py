class Ponto:
  def __init__(self,x=None,y=None):
    self.__x = x
    self.__y = y
  
  def getX(self):
    return self.__x
  def setX(self,x):
    self.__x = x
  def getY(self):
    return self.__y
  def setY(self,y):
    self.__y = y

  def novaPosicao(self,x,y):
    self.__x = x
    self.__y = y

  def calcularDistancia(self,ponto):
    return (((ponto.getX()-self.__x)**2)+((ponto.getY()-self.__y)**2))**(1/2)
  
  def __str__(self):
    return f"({self.__x},{self.__y})"

#programa principal

p1 = Ponto(2,2)
print(p1)
print(p1.calcularDistancia(p1))
p2 = Ponto()
p2.setX(4)
p2.setY(8)
print(p2)
print(p2.calcularDistancia(p1))