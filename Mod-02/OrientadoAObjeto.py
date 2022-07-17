'''class Carro:
    pass

meu_carro = Carro()


carro_do_ime = Carro()

meu_carro.ano = 1968
meu_carro.modelo = 'fusca'
meu_carro.cor = 'azul'


print(meu_carro.cor)

carro_do_ime.ano = 1981
carro_do_ime.modelo = 'brasilia'
carro_do_ime.cor = 'amarelo'

print(carro_do_ime.modelo)'''


class Lista:
    def append(self, elemento):
        return "Oops! Este objeto não é uma lista"


lista = []

a = Lista()
b = a.append(7)

lista.append(b)

print(lista)