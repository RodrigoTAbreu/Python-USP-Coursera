n = int(input("Digite um número: ")) # entrada do número
soma = 0 #definida a variável para soma
while n > 0: # enquanto o n for maior que 0
    soma += n % 10 # incrementa na variavel soma, o resto da divisão por 10 que é sempre o último digito
    n = int(n/10) # n recebe apenas a parte inteira da divisão por 10
print(soma)