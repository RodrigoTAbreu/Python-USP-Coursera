n = int(input("Digite um número inteiro: "))
total = 0

for count in range(1, n +1): # para COUNT na range de 1 até o N informado mais 1
     if n % count == 0: #resto da divisão de N pelo contador COUNT for igual a zero
         total += 1 #incrementa mais 1 ao total
# fim do laço for
if total == 2 :  # se a variável total for igual a 2 significa que o numero informado foi divisivel por 2 numeros apenas
    print("primo")
else:
    print("não primo")
