'''
prg042 - Escreva um programa que receba o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
• salários até R$ 280,00 (incluindo)...................: aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 .............: aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 ...........: aumento de 10%
• salários de R$ 1500,00 em diante...................: aumento de 5%
Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento.
'''
sal = float(input("Salário: "))
aumento = 20
if sal > 280:
    if sal > 700:
        if sal > 1500:
            aumento = 5
        else:
            aumento = 10
    else:
        aumento = 15
print(f"Salário antigo: R$ {sal:.2f}")
print(f"Percentual do aumento: {aumento}%")
print(f"Valor do aumento: R$ {(sal*(aumento/100)):.2f}")
print(f"Salário novo: R$ {(sal+(sal*(aumento/100))):.2f}")
