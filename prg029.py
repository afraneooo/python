'''
prg029 - Escreva um programa que 3 números inteiros quaisquer. Seu programa deve informar
estes números em ordem crescente.
'''
n1 = float(input("Número 1:"))
n2 = float(input("Número 2:"))
n3 = float(input("Número 3:"))
# '''JEITO DIFICIL:'''
# if n1 > n2 and n1 > n3:
#     if n2 > n3:
#         print("Em ordem: %.1f,%.1f,%.1f"%(n3,n2,n1))
#     else:
#         print("Em ordem: %.1f,%.1f,%.1f"%(n2,n3,n1))
# else:
#     if n2 > n1 and n2 > n3:
#         if n1 > n3:
#             print("Em ordem: %.1f,%.1f,%.1f"%(n3,n1,n2))
#         else:
#             print("Em ordem: %.1f,%.1f,%.1f"%(n1,n3,n2))
#     else:
#         if n3 > n1 and n3 > n2:
#             if n2 > n1:
#                 print("Em ordem: %.1f,%.1f,%.1f"%(n1,n2,n3))
#             else:
#                 print("Em ordem: %.1f,%.1f,%.1f"%(n2,n1,n3))
# '''JEITO DIFICIL 2:'''
# if n1>n2:
#     if n1>n3:
#         if n2>n3:
#             print("Em ordem:\n%.1f\n%.1f\n%.1f"%(n3,n2,n1))
#         else:
#             print("Em ordem:\n%.1f\n%.1f\n%.1f"%(n2,n3,n1))
#     else:
#         print("Em ordem:\n%.1f\n%.1f\n%.1f"%(n2,n1,n3))
# else:
#     if n1>n3:
#         print("Em ordem:\n%.1f\n%.1f\n%.1f"%(n3,n1,n2))
#     else:
#         if n2>n3:
#             print("Em ordem:\n%.1f\n%.1f\n%.1f"%(n1,n3,n2))
#         else:
#             print("Em ordem:\n%.1f\n%.1f\n%.1f"%(n1,n2,n3))
'''JEITO FÁCIL:'''
if n2<n1:
    n2, n1 = n1, n2
if n3<n2:
    n3,n2 = n2, n3
if n2<n1:
    n2, n1 = n1, n2
print("Em ordem:\n%.1f\n%.1f\n%.1f"%(n1,n2,n3))