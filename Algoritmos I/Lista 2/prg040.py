'''
prg040 - Escreva um programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
• Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
• Triângulo Equilátero ..................................: três lados iguais;
• Triângulo Isósceles.....................................: quaisquer dois lados iguais;
• Triângulo Escaleno.....................................: três lados diferentes;
'''
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
if (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b and b==c:
        print("Triângulo equilátero!")
    else:
        if a==b or b==c or a==c:
            print("Triângulo Isósceles!")
        else:
            print("Triângulo Escaleno!")
else:
    print("As medidas não formam um triângulo.")