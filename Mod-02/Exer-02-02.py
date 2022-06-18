
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

if len(m1) == len(m2):
    tam1 = len(m1)
    tam2 = len(m2)
    for i in range(tam1):
        for j in range(tam2):
            elemento1 = m1[i][j] + m2[i][j]
            print(elemento1)