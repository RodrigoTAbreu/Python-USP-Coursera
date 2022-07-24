'''Mede o tempo de execução de um progama'''
import random
import time
import ordenandolista

class ContaTempo:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)] #gera uma lista de 0 até o N informado
        for i in range(n):
            lista[i] = random.randrange(1000) # gera valores aleatorios entre 0 e 999
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #cria uma segunda lista de conteudo igual (clone)

        o = ordenandolista.Ordenador() #chama a classe Ordenador

        antes = time.time() #inicia o tempo
        o.bolha_curta(lista1) #chama a função bolha
        depois = time.time() #finaliza o tempo
        print(f'A Bolha Curta Demorou {depois - antes}segundos. ') #imprime o resultado

        o = ordenandolista.Ordenador()
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'A Seleção Direta Demorou {depois - antes}segundos. ')

        print("Comparando com listas quase ordenadas.")

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]

        antes = time.time()  # inicia o tempo
        o.bolha_curta(lista1)  # chama a função bolha
        depois = time.time()  # finaliza o tempo
        print(f'A Bolha Curta Demorou {depois - antes}segundos. ')  # imprime o resultado


        o = ordenandolista.Ordenador()
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'A Seleção Direta Demorou {depois - antes}segundos. ')


tempo = ContaTempo()
tempo.compara(5000)
