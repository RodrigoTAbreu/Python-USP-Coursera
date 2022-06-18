import math
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta = b**2-4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta))/ (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("as raízes da equação são {} e {}".format(x1,x2))

elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    print("a raiz desta equação é {}".format(x1))

elif delta <0:
    print("esta equação não possui raízes reais")

print("Fim de Programa.")



