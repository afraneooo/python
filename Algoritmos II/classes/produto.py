class Produto:
    def __init__(self, desc = None, preco = None):
        self.__desc = desc
        self.__preco = preco
    
    def getDesc(self):
        return self.__desc
    def setDesc(self, desc):
        self.__desc = desc
    def getPreco(self):
        return self.__preco
    def setPreco(self, preco):
        self.__preco = preco
    
    def calcularPreco(self,qtd):
        return self.__preco * qtd
    
    def __str__(self):
        return f"Descrição: {self.__desc}\nPreço: {self.__preco}"
