'''
prg075 - Faça um programa parecido com o anterior, mas agora com a validação do CNPJ
'''
continua = 1
while continua == 1:
    valido = True
    cnpj = input("Digite seu CNPJ (apenas números):\n")
    tam = len(cnpj)
    jpnc = [0]*14
    mult = 2
    soma = 0
    char1 = cnpj[0]
    cont = 0
    #Checa se todos os números são iguais
    for x in range(tam):
        if char1 == cnpj[x]:
            cont+=1
    if cont==tam:
            valido = False
    #Checa se tem 14 dígitos
    if tam != 14:
        valido = False
        print("Digitos inválidos. CNPJ tem 14 dígitos.")
    else:
        #Inverte os 12 primeiros numeros do cnpj
        for x in range(12):
            jpnc[x] = cnpj[11-x]
        #Calcula o dv1 
        for x in range(12):
            if mult<10:
                soma += int(jpnc[x])*mult
                mult+=1
            else:
                mult=2
                soma += int(jpnc[x])*mult
                mult+=1
        dv = 11 - (soma % 11)
        if dv>=10:
            dv = 0
        if dv == int(cnpj[12]):
            #Calcula dv2 se dv1 for valido
            #Inverte os 13 primeiros numeros do cnpj
            for x in range(13):
                jpnc[x] = cnpj[12-x]
            mult = 2
            soma = 0
            #Calcula dv2
            for x in range(13):
                if mult<10:
                    soma += int(jpnc[x])*mult
                    mult+=1
                else:
                    mult=2
                    soma += int(jpnc[x])*mult
                    mult+=1
            dv = 11 - (soma % 11)
            if dv>=10:
                dv = 0
            if dv == int(cnpj[13]):
                valido = True
            else:
                valido = False
        else:
            valido = False
    if valido:
        print("CNPJ válido!")
        break
    else:
        print("CNPJ inválido.")
        continua = int(input("Deseja continuar? (0 - Não/1 - Sim)\n"))
            
