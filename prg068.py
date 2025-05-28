'''
prg068 - Escreva um programa que ajude o DETRAN a saber o total de
recursos que serão arrecadados com a aplicação de multas de trânsito.
O programa deve ler, para cada motorista, as seguintes informações:
- O número da carteira de motorista
- O número de multas
- O valor de cada uma das multas
Deve ser impresso o valor da dívida para cada motorista, e no final
da leitura, o total de recursos arrecadados (somatório das multas).
O programa deve imprimir também o número da carteira do motorista que
obteve o maior número de multas. O programa termina ao ler a carteira
do motorista de valor 0.
'''
soma = 0
maior = 0
maiorC = 0
cart = int(input("Número da carteira: "))
while cart!=0:
    totalM = 0
    multas = int(input("Número de multas: "))
    for x in range(multas):
        valor = float(input("Valor da multa %d:"%(x+1)))
        totalM += valor
    print("Valor da dívida: R$ %.2f"%totalM)
    if soma==0 or multas>maior:
        maior = multas
        maiorC = cart
    soma += totalM
    cart = int(input("Número da carteira: "))
print("Total arrecadado: R$ %.2f"%soma)
print("Motorista com mais multas foi o CNH: %d"%maiorC)