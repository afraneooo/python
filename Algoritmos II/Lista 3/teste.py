from retangulo import Retangulo
from desenho import Desenho


r1 = Retangulo(3, 4)

print(r1)

print(f"Área={r1.calcula_area()}")
print(f"Perímetro={r1.calcula_perimetro()}")

r2 = Retangulo(5, 8)

d1 = Desenho()

d1.adiciona_figura(r1)
d1.adiciona_figura(r2)

print("Cenario 1:")
print(d1.listar_figuras())

d1.remove_figura(r1)

print("Cenario 2:")
print(d1.listar_figuras())