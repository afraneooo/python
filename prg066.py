'''
prg066 - Dado um país A, com 5 milhões de habitantes e uma taxa
de natalidade de 3% ao ano, e um país B, com 7 milhões de habitantes
e uma taxa de 2% ao ano, calcular e imprimir o tempo necessário para
que a população do país A ultrapasse a populaçao do país B.
'''
def calc(a, b):
    t = 0
    while a < b:
        a *= 1.03
        b *= 1.02
        t += 1
    return t    
#prog
pA = 5000000
pB = 7000000
print("Foi necessário %d anos"%(calc(pA,pB)))