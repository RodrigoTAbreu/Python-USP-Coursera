def main(l,a):
    if a == l:
        largura_altura(l,a)
    else:
        desenho(l,a)

def largura_altura(l,a):
    cont = 0
    while cont < a:
        print("#" * l)
        cont += 1


def desenho(l,a):
    cont = 0
    while cont < a:
        print("#" * l)
        cont += 1
        while cont == 1:
            print("#",end='')
            print(" " * (l - 3),end=' ')
            print("#")
            cont += 1

l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
main(l,a)