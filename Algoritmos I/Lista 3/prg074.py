'''
prg074.py - Escreva um programa que leia um CPF e informe se é um CPF válido ou não.
Caso não seja um CPF válido informe este fato ao usuário e pergunte se quer finalizar ou tentar novamente.
'''
valido = 0
while valido==0:
    cpf = input("Digite seu CPF: (apenas digitos)\n")
    tam = len(cpf) #FALTA AJUSTAR QUANDO TODOS OS NUMEROS FOREM IGUAIS
    mult1 = 10
    mult2 = 11
    soma1 = 0
    soma2 = 0 
    for x in range(tam-2):
        soma1 += ((int(cpf[x])*mult1)) 
        mult1-=1
    if (11-(soma1%11)==(int(cpf[9]))): #FALTA AJUSTAR CASO SEJA MAIOR QUE 10
        print("Primeiro é valido!")
        for x in range(tam-1):
            soma2 += ((int(cpf[x])*mult2))
            mult2-=1
        if (11-(soma2%11)==(int(cpf[10]))):
            print("Segundo é valido!")
            print("CPF válido!")
            valido=1
        else:
            print("Segundo é inválido.")
    if valido==0:
        print("CPF inválido.")
        valido = int(input("Gostaria de continuar? (0 - Sim/ 1 - Não)\n"))
#FALTAM AJUSTES