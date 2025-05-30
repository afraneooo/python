'''
prg038 - Escreva um programa que leia uma idade (número inteiro) e se é brasileiro (True ou
False). Ao final deve informar:
• Idade de 18 a 70 anos e brasileiro........................................... : Voto obrigatório
• Idade de 16 a 17 ou acima de 70 anos e brasileiro.................. : Voto não obrigatório
• Abaixo de 16 anos ou não brasileira........................................ : Voto não permitido
'''
idade = int(input("Idade: "))
br = input("Brasileiro (true/false): ")
if br=="True":
    if idade>=18 and idade<=70:
        print("Voto obrigatório!")
    else:
        if idade<16:
            print("Voto não permitido!")
        else:
            print("Voto não obrigatório!")
else:
    print("Gringo")