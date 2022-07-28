from random import choices, sample


def lista_grande(n):

    tamanho = n
    valores = range(1,50)
    resp = choices(valores, k = tamanho)
    resp.sort()
    return resp

    #print('=='*20)
    #print('Usando Sample')
    #print(resp)
    #print('=='*20)
    #print('Lista Ordenada')
    #resp.sort()
    #print(resp)

def ordena(lista):
    lista.sort()
    return lista


#lista_grande(n = int(input('Insira o valor: ')))
lista = [10,5,8,9,15,25,-1]
ordena(lista)

'''print('Usando Sample')
print(sample(valores, k= tamanho))
print('=='*25)
'''