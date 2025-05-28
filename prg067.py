'''
prg067 - Escreva um programa que controle o saldo bancário de um cliente.
O programa lê o valor do saldo anterior e, em seguida, lê as operações
realizadas na conta. As operações podem ser as seguintes:
- Saque em dinheiro (código 10);
- Depósito (código 11);
- Pagamento de cheque (código 4, tarifa de R$ 0,50 por operação)
O programa lê o código das operações e realiza as atualizações na conta,
imprimindo uma mensagem ao usuário caso a saída esteja negativo.
O programa deve continuar a leitura até que o código de operação seja 0.
Códigos diferentes dos definidos devem ser ignorados. Ao final do
processamento o programa deve imprimir o saldo atual do cliente.
'''
saldo = float(input("Saldo anterior:\n"))
print("10 - Saque em dinheiro")
print("11 - Depósito")
print(" 4 - Pagamento de cheque")
print(" 0 - Sair")
cod = int(input("Digite a operação desejada: "))
while cod!=0:
    if cod == 10:
        saldo -= (float(input("Valor para o saque: ")))
    else:
        if cod == 11:
            saldo += (float(input("Valor para depósito: ")))
        else:
            if cod == 4:
                saldo -= (0.5+(float(input("Valor do cheque: "))))
	    else:
		print("Código inválido. Operação ignorada.")
    if saldo < 0:
        print("\n!!SALDO NEGATIVO!!")
    print("\nNovo Saldo: R$ %.2f"%saldo)
    print("10 - Saque em dinheiro")
    print("11 - Depósito")
    print(" 4 - Pagamento de cheque")
    cod = int(input("Digite a operação desejada: "))
print("Saldo final: R$ %.2f"%saldo)
