n = int(input("Informe o numero: "))

cont = 0

for count in range(2,n):
    count += 1
    if count == 2 :
        cont = 1
        #print(f"{n} é primo.")
    else:
        if n % 2 == 0:
            #print(f"{n} não é primo.")
            cont +=1
        else:
            #print(f"{n} é primo.")
            cont += 1
#print(count)
print(cont)

