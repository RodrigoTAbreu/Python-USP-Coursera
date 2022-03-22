import time
import math


def main():#função principal do programa solicitando a entrada de dados do usuário
    print("##" * 15)
    print("Formula de Bascara")
    print("##" * 15)
    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))
    print("Efetuando calculo na formula de Bhaskara")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("Calculando Delta")
    time.sleep(1)
    print("Delta Calculado...")
    time.sleep(1)
    imprime_raizes(a,b,c)

def delta(a,b,c): # calcula o DELTA
    return b**2-4*a*c

def imprime_raizes(a,b,c): #calcula as raizes com base no DELTA
    d = delta(a,b,c)
    if d > 0:
        print("Delta é maior que 0 temos duas raizes")
        print("--"*15)
        time.sleep(1)
        x1 = (-b + math.sqrt(d))/ (2*a)
        print("O valor de X1 é {:.1f}".format(x1))
        time.sleep(1)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("O valor de X2 é {:.1f}".format(x2))

    elif d == 0:
        print("A equação apresentará uma raiz real")
        time.sleep(1)
        x1 = (-b + math.sqrt(d)) / 2 * a
        print("O valor de X1 é {:.1f}".format(x1))
        time.sleep(1)
    elif d <0:
        print("A equação não possui raízes reais")

    print("O valor de Delta é {}".format(d))
    print("--"*15)
    print("Fim de Programa.")
    print("--"*15)

main() #invocando a função principal