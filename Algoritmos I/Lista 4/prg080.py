'''
prg080 - Escreva um programa que leia um CPF e informe se é um CPF válido ou não. Caso não 
seja  um  CPF  válido  informe  este  fato  ao  usuário  e  pergunte  se  quer  finalizar  ou  tentar 
novamente. Faça uma função para executar essa ação respondendo True ou False.
'''
def cpfValido(cpf):
    tam = len(cpf)

    if tam != 11:
        print("Digitos inválidos. CPF tem 11 dígitos.")
        return False
    
    mult1 = 10
    mult2 = 11
    soma1 = 0
    soma2 = 0
    cont = 0
    for x in range(tam):
        if cpf[x] == cpf[0]:
            cont+=1
    if cont==tam:
        return False
    
    for x in range(tam-2):
        soma1 += ((int(cpf[x])*mult1)) 
        mult1-=1
    dv = 11-(soma1%11)
    if dv>=10:
        dv=0
    if (dv)==(int(cpf[9])):
        for x in range(tam-1):
            soma2 += ((int(cpf[x])*mult2))
            mult2-=1
        dv = 11-(soma2%11)
        if dv>=10:
            dv=0
        if (dv)==(int(cpf[10])):
            return True
        else:
            return False
    else:
        return False

print("Verificador de CPF")
cpf = input("Digite o CPF (apenas números):\n")
if cpfValido(cpf):
    print("CPF válido!")
else:
    print("CPF inválido.")