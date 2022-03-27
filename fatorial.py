
def fatorial(n):
    while n >= 0 :
        fatorial = 1
        while n > 1:
            fatorial = fatorial * n
            n = n - 1
        print(f"Fatorial: {fatorial}")

def valor():
    n = int(input("Informe um numero inteiro positivo: "))
    if n <0:
        print("Fim da execução")
    else:
        fatorial(n)

valor()
