class Combustivel:
  def __init__(self,posto=None,etanol=None,gasolina=None):
    self.__posto = posto
    self.__etanol = etanol
    self.__gasolina = gasolina*0.7

  def getPosto(self):
    return self.__posto
  def setPosto(self,posto):
    self.__posto = posto
  def getEtanol(self):
    return self.__etanol
  def setEtanol(self,etanol):
    self.__etanol = etanol
  def getGasolina(self):
    return self.__gasolina
  def setGasolina(self,gasolina):
    self.__gasolina = gasolina

  def decideCombustivel(self):
    if self.__gasolina > self.__etanol:
      return "Etanol"
    elif self.__gasolina == self.__etanol:
      return "Tanto faz"
    else:
      return "Gasolina"
    
  def __str__(self):
    return f"Posto: {self.__posto}\nGasolina: R${self.__gasolina:.2f}\nEtanol: R${self.__etanol:.2f}\nO mais rentável é: {self.decideCombustivel()}"