'''
prg073 - Escreva um programa que leia um endereço de email e verifique se é um endereço
de e-mail válido. Um endereço de email válido deve conter pelo menos 10 caracteres, sendo 1
deles (somente um) um ponto e um arrouba. Este arrouba e este ponto não podem estar nem
no início e nem no final da cadeia lida. Caso não seja um email válido informe este fato ao
usuário e pergunte se quer finalizar ou tentar novamente.
'''
valido=1
while valido==1:
    email = input("Email:\n")
    tam = len(email)
    contA=0
    contP=0
    if tam>=10:
        for x in range(tam):
            char=email[x]
            if x==0 and (char=="@" or char=="."):
                valido=0
                print("@ ou . no ínicio")
            else:
                if char=="@":
                    contA+=1
                else:
                    if char==".":
                        contP+=1
            if x==(tam-1) and (char=="@" or char=="."):
                valido=0
                print("@ ou . no final.")
        if valido==1:
            if contA>1 or contA<1:
                valido=0
                print("Quantidade de @ inválido.")
            if contP>1 or contP<1:
                valido=0
                print("Quantidade de . inválido.")
    else:
        valido=0
        print("Caracteres insuficientes.")
    if valido==0:
        print("Email inválido!")
        valido = int(input("Continuar? (0-Não/1-Sim)\n"))
    else:
        print("Email válido!")
        valido=0