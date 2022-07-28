from random import randint, choices
class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1 ):
            #inicialmente o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            #coloca o menor elemento encontrado no início da sub-lista
            #Para isso, troca de ugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    def lista_grande(self, n):
        listas = choices(n, k = n)
        return listas


lista = Ordenador()
lista.lista_grande(15)

'''
lista = [2,6,8,9,10,63,3,1,4,5]
print(f'Sequência da lista atual=  {lista}')

o = Ordenador()
o.selecao_direta(lista)
print(f'Lista após execução do código=  {lista}')
'''