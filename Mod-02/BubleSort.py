def bubble_sort(list: list) -> list:
    """Ordena uma lista utilizando o algoritmo: Ordenação da Bolha."""
    list = list[:]

    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list)

    print(list)

list = [-1,3,8,6,17,4,10,-5,50,45,15,9]
nome = bubble_sort(list)