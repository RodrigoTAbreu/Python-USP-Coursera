n = int(input("Infome o valor a ser buscado: "))
lista = [-100,0,20,30,50,100,3000,5000]


for i in range(len(lista)):
    if lista[i] == n:
        print(lista[i])
        #print(f'Encontrei o valor informado {n}. E está na posição {i}')
        break
    else:
        print(f'{i}')

