n = int(input("Digite um numero [0] para sair: "))

def primo(x):
    fator = 2
    if x == 2:
        return True
    while x  % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

while n > 0 :
    if primo(n):
        print(f"{n} É primo")
    else:
        print(f"{n} Não é primo")
    n = int(input("Digite um numero [0] para sair: "))

