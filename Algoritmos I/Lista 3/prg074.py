'''
prg074.py - Escreva um programa que leia um CPF e informe se é um CPF válido ou não.
Caso não seja um CPF válido informe este fato ao usuário e pergunte se quer finalizar ou tentar novamente.
'''
continua = 1
while continua==1:
    valido = True
    cpf = input("Digite seu CPF: (apenas digitos)\n")
    tam = len(cpf)
    if tam != 11:
        valido = False
        print("Digitos inválidos. CPF tem 11 dígitos.")
    else:
        mult1 = 10
        mult2 = 11
        soma1 = 0
        soma2 = 0
        char1 = cpf[0]
        cont = 0
        #CHECA SE TODOS OS DIGITOS SÃO IGUAIS
        for x in range(tam):
            if char1 == cpf[x]:
                cont+=1
        if cont==tam:
            valido = False
        else:
            #PRIMEIRO DIGITO VERIICADOR
            for x in range(tam-2):
                soma1 += ((int(cpf[x])*mult1)) 
                mult1-=1
            dv = 11-(soma1%11)
            #se for maior que 10 o dígito verificador será 0
            if dv>=10:
                dv=0
            if (dv)==(int(cpf[9])):
                #SEGUNDO DIGITO VERIFICADOR
                for x in range(tam-1):
                    soma2 += ((int(cpf[x])*mult2))
                    mult2-=1
                dv = 11-(soma2%11)
                if dv>=10:
                    dv=0
                if (dv)==(int(cpf[10])):
                    valido = True
                else:
                    valido = False
            else:
                valido = False
    if valido:
        print("CPF válido!")
        break
    else:
        print("CPF inválido.")
        continua = int(input("Gostaria de continuar? (1 - Sim/ 0 - Não)\n"))