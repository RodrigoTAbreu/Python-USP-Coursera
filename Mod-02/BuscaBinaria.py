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
        primeiro = 0
        ultimo = len(lista) - 1
        while primeiro <= ultimo:
            i  = int((primeiro + ultimo)/2)
            print(i)
            if lista[i] == elemento:
                return i
            elif lista[i] > elemento:
                ultimo = i -1
            elif lista[i] < elemento:
                primeiro = i + 1
            else:
                return False
