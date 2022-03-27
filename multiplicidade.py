n = int(input("Digite um número inteiro maior que 1: "))

fator = 2
multiplo = 0

while n > 1:
    while n % fator == 0:
        multiplo = multiplo + 1
        n = n / fator
    if multiplo > 0:
        print(f"Fator {fator} é multiplo por {multiplo}")
    fator = fator + 1
    multiplo = 0

mult = 0
for count in range(2,n):
    if (n%count == 0):
        print(f"Multiplo de {count}")
        mult +=1
if mult == 0:
    print(f"{n} É primo")
else:
    print(f"Tem {mult} multiplos acima de 2 e baixo de {n}")