'''
prg079 - Escreva um programa que leia um endereço de email e verifique se é um endereço 
de e-mail válido. Um endereço de email válido deve conter pelo menos 10 caracteres, sendo 1 
deles  um  ponto  e  um  arrouba.  Este  arrouba  e  este  ponto  não  podem  estar  nem  no  início  e 
nem no final da cadeia lida.  Além disso só pode ter 1 arrouba. Use uma função para executar 
essa ação respondendo True ou False.
'''
def emailValido(email):
    tamanho = len(email)
    if tamanho<10:
        return False
    else:
        if email[0]=="@" or email[0]==".":
            return False
        else:
            if email[tamanho-1]=="@" or email[tamanho-1]==".":
                return False
            else:
                contA = 0
                contP = 0
                for x in range(tamanho):
                    if email[x]=="@":
                        contA+=1
                    if email[x]==".":
                        contP+=1
    if contA!=1 or contP<1:
        return False
    else:
        return True
    
print("Validador de E-mail")
email = input("Insira o e-mail:\n")
if emailValido(email):
    print("E-mail válido!")
else:
    print("E-mail inválido.")