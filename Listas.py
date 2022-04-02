
def remove_repetidos(lista):
    lista_b = []
    for i in lista:
        if i not in lista_b:
            lista_b.append(i)
    lista_b.sort()
    return lista_b

def soma_elementos(lista):
    return sum(lista)
    #print(sum(lista))

def maior_elemento(lista):
    #max(lista)
    print(max(lista))



lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]
lista = remove_repetidos(lista)
print(lista)
soma_elementos(lista)
maior_elemento(lista)