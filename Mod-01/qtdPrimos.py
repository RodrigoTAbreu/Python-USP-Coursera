def n_primos(n):
    count = 0
    cont = 0
    if n == 2:
        cont = 1

    for count in range(2,n):
        count += 1
        if n % 2 == 0:
            #print(f"{n} não é primo.")
            cont +=1
        else:
            #print(f"{n} é primo.")
            cont += 1

    print(cont)

n = int(input("Informe o numero: "))
n_primos(n)