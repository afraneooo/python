from contabancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
  def __init__(self, nome=None, conta=None):
    super().__init__(nome, conta)

  def calcularJuros(self):
    pass