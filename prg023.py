'''
prg023 - Escreva um programa que leia uma letra e caso a letra seja C, imprima “Casado”, caso
seja “S” imprima “Solteiro” e caso não seja nenhuma das duas, imprima “Estado Civil não
encontrado”.
'''
letra = input("Qual sua situação civil? (digite a primeita letra da situação ex: 'S' para Solteiro)\n")
if letra=="C":
    print("Casado")
else:
    if letra=="S":
        print("Solteiro")
    else:
        print("Estado Civil não encontrado")