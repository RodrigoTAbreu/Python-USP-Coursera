conta_letras = 'programamos em python'

vogais = ['a','e','i','o','u']
qtd = 0
count = len(conta_letras)

while len(conta_letras) > count:
    conta_letras[qtd].find(vogais[qtd])
    count -= 1
    qtd +=1

print(qtd)