'''def fazAlgo(string):
    pos = 0
    string1 = ""
    while pos < len(string):
        if string[pos] != " ":
            string1 = string1 + string[pos]
        pos = pos + 1
        string1 = string1.capitalize()
    return string1

print(fazAlgo("É UM TESTE"))
print("**"*20)

#Atribuição de lista de valores
a, b, c = 1, 2 , 3
print(a)
print(b)
print(c)
print("**"*20)

def pagto_semanal(vlr_hora, num_horas = 40):
    resultado = 0
    assert vlr_hora >=0  and num_horas >= 0
    resultado = vlr_hora * num_horas
    print(resultado)


pagto_semanal(100,41)

print("**"*20)
x = 10
x += 10
x /= 2
x //= 3
x %= 2
x *= 9
print(x)

print("**"*20)
def calculo(x, y = 10, z = 5):
    return x + y * z
print(calculo(7))
print("**"*20)


def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s
print(horario_em_segundos (1,33,50))
'''

"""def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False

numeros = [55,33,0,900,-432,10,77,123,11]"""

"""def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return -1
    return i
"""

def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            print("True")
    print("False")

numeros = [55,33,0,900,-432,10,77,123,11]