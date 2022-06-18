def dimensoes(matriz):
    print(f'{len(matriz)}X', end="")

    if len(matriz) >= 1:
        print(len(matriz[0]))


matriz = []
dimensoes(matriz)
