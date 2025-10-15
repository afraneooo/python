class Bebida:
    def __init__(self, desc = None, preco = None, composicao = None, adulterado = False):
        self.__desc = desc
        self.__preco = preco
        self.__composicao = composicao
        self.__adulterado = adulterado
    
    def setComposicao(self, comp):
        self.__composicao = comp
    def getComposicao(self):
        return self.__composicao
    
    def adulterarBebida(self,composto):
        self.__composicao.append(composto)
        self.__adulterado = True

    def __str__(self):
        return f"Composição: {self.__composicao}\nAdulterado: {self.__adulterado}"

#programa principal

vodka = Bebida()
vodka.setComposicao(["agua","alcool"])

print(vodka)

print("\nAdicionando composto...\n")

vodka.adulterarBebida("metanol")

print(vodka)