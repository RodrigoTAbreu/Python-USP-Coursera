class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


    def perimetro(self):
        self.p = self.a + self.b + self.c
        return self.p

    def tipo_lado(self):
        #dois lados iguais apenas
        if self.a == self.b and self.a != self.c or self.b == self.c and self.b != self.a or self.c == self.a and self.c != self.b:
            print('isósceles')
            return 'isósceles'

        #todos lados diferentes
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            print('escaleno')
            return 'escaleno'

        #todos lados iguais
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            print('equilatero')
            return 'equilátero'

    def retangulo(self):

        if self.a > self.b and self.a > self.c:
            hipot = self.a
            calc = (self.b^2) + (self.c^2)
            if calc == (hipot^2):
                #print('é triangulo retangulo')
                return True
            else:
                return False
                #print('Não é retangulo')
        elif self.b> self.a and self.b > self.c:
            hipot = self.b
            calc = (self.c ^ 2) + (self.a ^ 2)
            if calc == (hipot^2):
                #print('é triangulo retangulo')
                return True
            else:
                #print('Não é retangulo')
                return False
        elif self.c > self.a and self.c > self.b:
            hipot = self.c
            calc = (self.b ^ 2) + (self.a ^ 2)
            if calc == (hipot^2):
                #print('é triangulo retangulo')
                return True
            else:
                #print('Não é retangulo')
                return False
        else:
            #print('Não é retangulo')
            return False

    def semelhantes(self, triangulo_2):
        triangulo_1 = [self.a, self.b, self.c]
        triangulo_2 = [self.a, self.b, self.c]
        pos0 = float(triangulo_1[0] / triangulo_2[0])
        pos1 = float(triangulo_1[1] / triangulo_2[1])
        pos2 = float(triangulo_1[2] / triangulo_2[2])

        if pos0 == pos1 and pos0 == pos2:
            print('São semelhantes')
            print(f'Posição 0:{pos0:.2f}, Posição 1:{pos1:.2f} e Posição 2:{pos2:.2f}')
            return True
        else:
            print('Não são semelhantes')
            print(f'Posição 0:{pos0}, Posição 1:{pos1} e Posição 2:{pos2}')
            return False


triangulo_1 = Triangulo(3,3,3)
triangulo_2 = Triangulo(3,4,5)
triangulo_1.semelhantes(triangulo_2)

