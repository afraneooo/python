'''
prg006 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do
usuário. Calcule o total em segundos.
'''
dias = int(input("Dias: "))
horas = int(input("Horas: "))
min = int(input("Minutos: "))
seg = int(input("Segundos: "))
total = seg+(min*60)+(horas*3600)+(dias*86400)
print("O total é de %d segundos"%total)
