n = int(input("Valor de N:"))
m = int(input("Valor de M:"))




def comp(n,m):
    retira = n
    print(f"Retirando {m} peças do tabuleiro")
    #while retira > 0:
    retira -= m
    n = retira
    return print(n)

comp(n,m)




