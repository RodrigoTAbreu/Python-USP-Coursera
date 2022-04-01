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

print(f"Lista de numeros {numeros}")
for i in range(len(numeros)):
    numeros[i] = numeros[i]**3

print(f"Lista de numeros ao cubo {numeros}")