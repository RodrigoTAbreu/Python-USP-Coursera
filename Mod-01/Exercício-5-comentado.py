# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas
num = int(input("Digite um número inteiro: "))
resto = num %100 #calcula o resto de uma divisão com o % por 100 porque precisamos extrair a dezena dele
result = resto // 10 #calcula a divisão inteira por 10 que é a dezena a ser procurada

print(resto)
print(result)