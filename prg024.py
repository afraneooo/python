'''
prg024 - Escreva um programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input("Digite uma letra em minúsculo: ")
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("É uma vogal!")
else:
    print("É uma consoante!")