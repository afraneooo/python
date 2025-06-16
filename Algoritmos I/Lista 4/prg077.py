'''
prg077 - Escreva um programa que receba um número inteiro n qualquer e responda com a
impressão dos n número da sequência de Fibonacci, que é formada pela sequência 1, 1, 2, 3, 5,
8, 13, 21, 34, 55, ... Use uma função em sua solução.
'''
def fibonacci(n):
    n1 = 1
    n2 = 1
    if n<1:
        print("Termo inválido.")
    else:
        if n==1:
            print(n1)
        else:
            if n==2:
                print(n1)
                print(n2)
            else:
                print(n1)
                print(n2)
                for x in range(n-2):
                    nn = n1 + n2
                    n1 = n2
                    n2 = nn
                    print(nn)
print("Sequência de Fibonacci!")
n = int(input("Gostaria de calcular até que termo? "))
fibonacci(n)
        
