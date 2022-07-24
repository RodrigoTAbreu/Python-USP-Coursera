class Ordenador:
     def selecao_direta(self, lista):
         fim = len(lista)

         for i in range(fim - 1):
            #incialmente o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range( i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            #Coloca o menor elemento encontrado no início da sub-lista
            #Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

     def bolha(self, lista):
         fim = len(lista) #tamanho da lista

         for i in range(fim-1,0,-1): #para cada i no range de TAMANHO DA LISTA -1
                                    #ou seja do final para o inicio
                                    # até o 0 pulando de -1 em -1
             for j in range(i): #para cada J no range do i

                 if lista[j] > lista[j+1]: # se a posição j for maior que a posição de j + 1
                     lista[j], lista[j+1] = lista[j+1], lista[j]#trocando de posições os elementos

     def bolha_curta(self, lista):
         fim = len(lista) #tamanho da lista

         for i in range(fim-1,0,-1): #para cada i no range de TAMANHO DA LISTA -1
                                    #ou seja do final para o inicio
                                    # até o 0 pulando de -1 em -1
             for j in range(i): #para cada J no range do i
                 trocou = False

                 if lista[j] > lista[j+1]: # se a posição j for maior que a posição de j + 1
                     lista[j], lista[j+1] = lista[j+1], lista[j]#trocando de posições os elementos
                     trocou = True

             if not trocou:
                  return




#lista = [10,3,8,-10,200,17,32]
#o = Ordenador()
#o.selecao_direta(lista)
#print(lista)

#print(lista)
#o = Ordenador()
#o.bolha(lista)
#print(lista)


"""
def ordenada(lista):
    next = 0
    for i in range(len(lista)):
        next = i + 1
        if next < len(lista):
            if lista[i] > lista[next]:
                return False
    return True
"""
