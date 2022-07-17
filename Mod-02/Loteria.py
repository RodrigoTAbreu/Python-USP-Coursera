
class Megasena:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def consulta_jogo(self, meu_jogo):
        saiu = [self.a, self.b, self.c, self.d, self.e, self.f]
        saiu.sort()
        #meu_jogo = [self.a, self.b, self.c, self.d, self.e]
        cont =0
        for i in range(len(saiu)):
            if saiu[i] == meu_jogo:
                print('saiu esse numero')
                cont +=1
        print(f'Você jogou {meu_jogo} e ele saiu {cont} vezes.')
        print(saiu)

jogo = Megasena(51,27,58,40,58,1)
jogo.consulta_jogo(58)
