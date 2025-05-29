'''
prg041 - Escreva um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.
Desconto do IR:
• Salário Bruto até 900 (inclusive)................: isento
• Salário Bruto até 1500 (inclusive)..............: desconto de 5%
• Salário Bruto até 2500 (inclusive)..............: desconto de 10%
• Salário Bruto acima de 2500......................: desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da
hora é R$ 50,00 e a quantidade de horas é 200.
• Salário Bruto: (50 * 200)..: R$ 10.000,00
• (-) IR (20%) .......................: R$ 2.000,00
• (-) Sindicato (3%)..............: R$ 300,00
• FGTS (11%).......................: R$ 1.100,00
• Total de descontos...........: R$ 2.300,00
• Salário Líquido..................: R$ 7.700,00
'''
valor = float(input("Valor por hora: "))
horas = int(input("Horas trabalhadas: "))
salB = valor*horas
desconto = int(0)
sind = salB*0.03
fgts = salB*0.11
if salB>900:
    if salB>1500:
        if salB>2500:
            desconto = 20
        else:
            desconto = 10
    else:
        desconto = 5
ir = salB*(desconto/100)
descontos = ir+sind
print("• Salário Bruto: (%.0f*%d)..........: R$ %.2f"%(valor,horas,salB))
if desconto > 0:
    print(f"• (-) IR ({desconto}%) .....................: R$ {ir:.2f}")
print(f"• (-) Sindicato (3%)...............: R$ {sind:.2f}")
print(f"• FGTS (11%).......................: R$ {fgts:.2f}")
print("• Total de descontos...............: R$ %.2f"%(descontos))
print("• Salário Líquido..................: R$ %.2f"%(salB-descontos))
