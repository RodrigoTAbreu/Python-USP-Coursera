import random
import time

import ordenandolista


class ContaTempos:
    def lista_aleatoria(self,n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista
        #ou da forma logo abaixo
       #for i in range(n):
        #    lista[i] = random.randrange(1000)
        #return lista

    def lista_quase_ordenada(self,n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self,n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenandolista.Ordenador()

        print("Comparando com listas aleatorias")
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'Bolha curta {depois-antes} segundos')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'Selecao direta demorou {depois - antes} segundos')

        print("\nComparando com listas quase ordenadas")
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]

        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'Bolha curta {depois - antes} segundos')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'Selecao direta demorou {depois - antes} segundos')



melhoria = ContaTempos()
melhoria.compara(5000)
