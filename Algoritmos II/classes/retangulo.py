class Retangulo:
  def __init__(self, base=None, altura=None):
    self.__base = base
    self.__altura = altura
  
  def get_base(self):
    return self.__base
  def get_altura(self):
    return self.__altura
  def set_base(self, base):
    self.__base = base
  def set_altura(self, altura):
    self.__altura = altura

  def calcular_area(self):
    return self.__base * self.__altura
  
  def calcular_perimetro(self):
    return 2*self.__base + 2*self.__altura
  
  def __str__(self):
    return f"Retângulo: base={self.__base} altura={self.__altura} área={self.calcular_area()} perímetro={self.calcular_perimetro()}"

#programa principal
r1 = Retangulo()
r2 = Retangulo(3, 4)

r1.set_base(5)
r1.set_altura(6)

print(r1)
print("Área:", r1.calcular_area())
print("Perímetro:", r1.calcular_perimetro())

print(r2)
print("Área:", r2.calcular_area())
print("Perímetro:", r2.calcular_perimetro())