'''
prg073 - Escreva um programa que leia um endereço de email e verifique se é um endereço
de e-mail válido. Um endereço de email válido deve conter pelo menos 10 caracteres, sendo
somente um arrouba e pelo menos um ponto. Este arrouba e este ponto não podem estar nem
no início e nem no final da cadeia lida. Caso não seja um email válido informe este fato ao
usuário e pergunte se quer finalizar ou tentar novamente.
'''
continua=1
while continua == 1:
    valido = True
    email = input("Informe um email:\n")
    if len(email)<10:
        valido = False
    else:
        if email[0]=="." or email[0]=="@" or email[len(email)-1]=="." or email[len(email)-1]=="@":
            valido = False
        else:
            cont=0
            for x in range(len(email)):
                if email[x]=="@":
                    cont+=1
            if cont!=1:
                valido = False
    if valido:
        print("Email válido!")
        break
    else:
        print("Email inválido.")
        continua = int(input("Continuar? (0-Não/1-Sim)"))