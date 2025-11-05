class FiguraGeometrica:
  def __init__(self, base=None):
    self.__base = base
  
  def get_base(self):
    return self.__base
  
  def set_base(self, base):
    self.__base = base

  def __str__(self):
    return f"base={self.__base}"
