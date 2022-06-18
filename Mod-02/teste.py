def cria_matriz(nlinhas, ncolunas):
    matriz = []

    for i in range(nlinhas):
        #cria a linha i
        linha = []
        for j in range (ncolunas):
            valor = int(input(f'Digite o elemento [{i}][{j}]'))
            linha.append(valor)

        #adiciona a linha a matriz
        matriz.append(linha)

    print(matriz)

def le_matriz():
    lin = int(input('Digite o numero de linhas da matriz: '))
    col = int(input('Digite o numero de colunas da matriz: '))
    return cria_matriz(lin,col)
