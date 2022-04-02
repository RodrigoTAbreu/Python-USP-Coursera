n = [ 4,5,6,8,9,3,2,4,1,7,6,3,1,2,]
b = ["vermelho","verde","azul"]
a = b[:] # faz um clone da lista e ambas ficam independentes
print(f"Valores da Lista A {a}")
print(f"Valores da Lista B {b}")
a[1] = "amarelo"
print(f"Lista A modificada {a}")
print(f"Lista B original{b}")
print("**"*20)
if "blue" in b:
    print("Sim")
else:
    print("Não")

print("**"*20)

c = a + b
print(f"Lista A modificada {a}")
print(f"Lista B original{b}")
print(f"Lista C{c}")
print(f"Reverso {c}")

print("**"*20)

print(f"Triplicando listas {len(a*3)} itens")

print("**"*20)

print(f"Lista B {b}")
del b[1]
print(f"Lista B indice 1 deletado {b}")

print("**"*20)

