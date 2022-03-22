import math
x1 = int(input("Informe o Primeiro Valor: "))
x2 = int(input("Informe o Segundo Valor: "))
y1 = int(input("Informe o Terceiro Valor: "))
y2 = int(input("Informe o Quarto Valor: "))

distancia = math.sqrt((x1-x2)**2+(y1-y2)**2)

if distancia >=10:
    print("longe")
else:
    print("perto")
