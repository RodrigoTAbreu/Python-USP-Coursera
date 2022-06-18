# frutas = ["maça","banana","pessego","uva"]
#
# for fruta in frutas:
#     print(f"Eu gosto de {fruta}")
#

numeros = [50,10,15,35,30,20,5,1,2]
#
# for x in numeros:
#     print(f"O numero {x} elevado ao quadrado é : {x*x}")

# for n in range(1,15):
#     print(f"Apresentando o valor  {n}")
#
# for n in range(1,50,5): # inicia em 1 finaliza em 50 pulando de 5 em cino
#     print(f"Contando o número {n}")

# numeros = range(100,0,-5) #forma retroativa do range
#
# for x in numeros:
#      print(x)

# print(f"Lista de numeros {numeros}")
# for i in range(len(numeros)):
#     numeros[i] = numeros[i]**3
#
# print(f"Lista de numeros ao cubo {numeros}")

# animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
#
# for x in range(len(animais)):
#     print("--> ", x)


# #pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# for i in range(0, 50, 5):
# 	print(i)

valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)

print(valores)

print("*"*20)

# valores = []
# for i in range(0, 10, 2):
#     valores.append(i)
#
# print(valores)

# valores = []
# for i in range(2, 10, 2):
#     valores.append(i)
#
# print(valores)

# valores = []
# for i in range(1, 10, 2):
#     valores.append(i)
#
# print(valores)

#
# animais = ["gato", "cachorro", "papagaio",
# "arara", "jacaré"]
#
# #animais[2] = "piriquito"
# #animais[2] = animais.append("piriquito")
# animais[-3] = "LEAO"

# print(animais)

# for i in range(0, 50, 5):
#     print(i)

# pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# for x in range(5, 10):
#     print(pares[x])

# pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# for x in range(len(pares)):
#     print(x)

# pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# for x in range(len(pares)):
#     print(pares[x])

# for i in range(16,4,-3):
# 	print(i)

# alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#
# letras = alfabeto[1:10]
# print(letras)
# print(len(letras))
# print(alfabeto[0:13])
# print(len(alfabeto))
# print(alfabeto[13:])

#
# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = carnes
# carnes2.append("ponta de alcatra")
# print(carnes)
# print(carnes2)

# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = []
# for cns in carnes:
#     carnes2.append(cns)
# carnes2.append("ponta de alcatra")
#
# print(carnes)
# print(carnes2)

# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = carnes[:]
# carnes2.append("ponta de alcatra")
#
# print(carnes)
# print(carnes2)

# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
# if "ponta de alcatra" in carnes:
#     print("XXX")
# else:
#     if "ponta de alcatra" in carnes2:
#         print("YYY")
#     else:
#         print("ZZZ")

# carnes1 = ["picanha", "alcatra"]
# carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
# carnes3 = carnes2 + carnes1
#
# print(f"Valores de Carnes1 {carnes1}")
# print(f"Valores de carnes2 {carnes2}")
# print(f"Valores de carnes3 {carnes3}")

# pares = [2, 4, 6, 8, 10]
# x = pares * 3
# print(x)
#
# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# x = carnes
# del (x[-1])
#
# print(carnes)
# print(x)