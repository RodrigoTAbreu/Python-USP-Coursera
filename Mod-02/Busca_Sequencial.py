class Musica:
    def __init__(self, titulo, compositor, ano):
        self.titulo = titulo
        self.compositor = compositor
        self.ano= ano

class Buscador:
    def busca_por_titulo(self, playlist, titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo:
                return i
        return -1

    def vamos_buscar(self):
        playlist = [Musica("Ponta de Areia","Milton", 1957),
                    Musica("Podres Poderes","Caetano", 1984),
                    Musica("Baby","Gal Costa",1969)]

        onde_achou = self.busca_por_titulo(playlist, "Baby")

        if onde_achou == -1:
            print("A musica buscada não foi encontrada.")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.compositor, preferida.ano, sep = ', ')

b = Buscador()
b.vamos_buscar()
