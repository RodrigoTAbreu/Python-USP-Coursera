i = 0
while i < 3:
  j = 0
  while j < 3:
    print(3 * i + j + 1, end=" ")
    j = j + 1
  i = i + 1
#################################################
  tab = 1
  while tab <= 10:
      i = 1
      while i <= 10:
          print(tab, "x", i, "=", tab * i)
          i = i + 1
      print()
      tab = tab + 1

#####################################################

x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        print(f"Valor de Y{y} | Valor de X {x}")
        y = y + 1
    x = x + 1

########################################################
x = 2
cont = 0
while x >= 0:
    y = 0
    while y >= 4:
        print("Olá")
        y = y + 1
    x = x - 1
####################################################

x = 2
cont = 0
while x >= 0:
    y = 0
    while y <= 4:
        print("Vamos")
        y = y - 1
    x = x - 1