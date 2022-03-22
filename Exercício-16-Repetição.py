#compara os numeros digitados com o antecedente apenas e não com todo o numero.
n = int(input("Digite um número inteiro: "))
cond = True

while cond:
    x1 = n % 10 # pega o ultimo numero digitado dividindo pelo resto de 10
    print("O valor de X1 {}".format(x1))
    x = n // 10 #X recebe a divisão inteira de 10
    x2 = x % 10# pega o penultimo numero digitado dividindo pelo resto de 10
    print("O valor de X2 {}".format(x2))
    if n <= 10: # se o valor informado for menor que duas casas decimais
        print('não')
        cond = False #cond recebe FALSE e fecha o while
    elif n > 10 and x1 == x2: # se N tiver dois algarismos e X1 igual a X2
        print('sim')
        cond = False
    else: # Se não atender as condições anteriores
        n = n//10 #N recebe a divisão inteira por 10 e segue no While
