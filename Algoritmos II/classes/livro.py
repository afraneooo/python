class Livro:
  def __init__(self,isbn=None,titulo=None,autor=None,preco=None,qtd=None):
    self.__isbn = isbn
    self.__titulo = titulo
    self.__autor = autor
    self.__preco = preco
    self.__qtd = qtd

  def getIsbn(self):
    return self.__isbn
  def setIsbn(self,isbn):
    self.__isbn = isbn
  def getTitulo(self):
    return self.__titulo
  def setTitulo(self,titulo):
    self.__titulo = titulo
  def getAutor(self):
    return self.__autor
  def setAutor(self,autor):
    self.__autor = autor
  def getPreco(self):
    return self.__preco
  def setPreco(self,preco):
    self.__preco = preco
  def getQtd(self):
    return self.__qtd
  def setQtd(self,qtd):
    self.__qtd = qtd

  def comprarLivros(self,compra):
    self.__qtd += compra
  def venderLivros(self,venda):
    self.__qtd -= venda

  def ajustarPreco(self,ajuste):
    self.__preco += self.__preco*(ajuste/100)

  def __str__(self):
    return f"ISBN: {self.__isbn}\nTítulo: {self.__titulo}\nAutor: {self.__autor}\nPreço: R${self.__preco:.2f}\nQuantidade em estoque: {self.__qtd}"

# programa principal

livro1 = Livro("501","As aventuras de Ysalana","Ysalana Gomes",59.90,60)
print(livro1)  
livro1.comprarLivros(40)
print(livro1)
livro1.venderLivros(20)
livro1.ajustarPreco(-80)
print(livro1)