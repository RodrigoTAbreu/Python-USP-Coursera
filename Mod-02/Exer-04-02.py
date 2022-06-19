#Matrizes multiplicáveis

'''def sao_multiplicaveis(m1,m2):
    countLinha = countColuna = 0
    for i in range(len(m1)):
        #print(f'valor de i {i}')
        countLinha += 1
    #print(f'Total de linha: {countLinha}')

    for i in range(len(m2)):
        for x in m2[i]:
            #print(f'valor de x {x}')
            countColuna += 1
    #print(f'Total de Coluna: {countColuna}')

    if countLinha % countColuna == 0:
        print('Multiplicaveis')
        #return True
    else:
        #return False
        print('Não Multiplicaveis')

m1 = [[1]]
m2 = [[2, 3, 4]]
sao_multiplicaveis(m1,m2)'''


def sao_multiplicaveis(m1, m2):
    '''Recebe duas matrizes como parâmetros e devolve True se as matrizes forem multiplicáveis (número de colunas
    da primeira é igual ao número de linhs da segunda). False se não forem
    '''

    if len(m1) == len(m2[0]):
        return True
    else:
        return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
sao_multiplicaveis(m1, m2)