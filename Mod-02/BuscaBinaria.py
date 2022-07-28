class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self,lista,x):
        primeiro = 0
        ultimo = len(lista)-1
        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:

                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio-1
                else:
                    primeiro = meio+1

        return -1


    def busca(self, lista, elemento):
        first = 0
        last = len(lista) - 1

        while first <= last:
            i = int((first + last) / 2)
            print(i)
            if lista[i] == elemento:
                print(i)
                #return i
            elif lista[i] > elemento:
                last = i - 1
            elif lista[i] < elemento:
                first = i + 1
            else:
                print('False')
                #return False

        print('False')
        #return False

a = Buscador()
lista = [1,3,2,5,6,9,87]
a.busca(lista, 5)