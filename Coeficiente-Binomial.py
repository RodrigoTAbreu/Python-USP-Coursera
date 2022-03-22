from math import factorial
def fatorial(n):
    return factorial(n)

#n = int(input("Informe o valor de N: "))
#print("O Fatorial de {} é {}.".format(n, fatorial(n)))

def numeroBinomial(n,k):
    return fatorial(n) / (fatorial(k)*fatorial(n-k))

n = int(input("Informe o numero de N: "))
k = int(input("Informe o numero de K: "))
print((numeroBinomial(n,k)))

# função de teste automático
def testa_Fatorial(): #função sem parametro
    #executa o teste logico para cada teste
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

#testa_Fatorial()