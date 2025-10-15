from produto import Produto

p1 = Produto()
p2 = Produto("Lápis",1.55)
p1.setDesc("Borracha")
p1.setPreco(1.99)

print(p2.getDesc())
print(p2.getPreco())

print(p1)
print(p1.calcularPreco(20))