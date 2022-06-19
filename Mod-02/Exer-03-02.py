#Imprime Matriz

def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        #Utilizando o metodo UNPACK
        #O operador * em Python pode ser usado para descompactar objetos.
        # Ele descompacta todos os elementos de uma lista e os imprime sem os colchetes
        print(*minha_matriz[i], sep=' ')

minha_matriz = [[1, 2, 3]]
imprime_matriz(minha_matriz)