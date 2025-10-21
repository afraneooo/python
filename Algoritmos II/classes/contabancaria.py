class ContaBancaria:
  def __init__(self,nome=None,conta=None):
    self.__nome = nome
    self.__conta = conta
    self.__saldo = 0

  @property
  def nome(self):
    return self.__nome
  @nome.setter
  def nome(self,nome):
    self.__nome = nome

  @property
  def conta(self):
    return self.__conta
  @conta.setter
  def conta(self,conta):
    self.__conta = conta

  @property
  def saldo(self):
    return self.__saldo
  @saldo.setter
  def saldo(self,saldo):
    self.__saldo = saldo

  def depositar(self,deposito):
    self.__saldo += deposito
    print("Novo saldo: R$",self.__saldo)
  def sacar(self,saque):
    self.__saldo -= saque
    print("Novo saldo: R$",self.__saldo)
  def imprimirSaldo(self):
    print("Saldo: R$",self.__saldo)
  
  def __str__(self):
    return f"Proprietário: {self.__nome}\nConta: {self.__conta}\nSaldo: R$ {self.__saldo:.2f}"
  
# programa

conta = ContaBancaria()
conta.nome = "Frederico"
conta.conta = "12312-3"
print(conta)
conta.depositar(5000)
conta.sacar(1500)
print(conta)