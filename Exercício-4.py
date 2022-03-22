# entrada = int(input("Por favor, entre com o número de segundos que deseja converter:"))
# totalsegundos = entrada % 3600
#
# minutos = (totalsegundos // 60)
# hora = (entrada // 3600)
# dia  = (entrada / 86400)
#
# print("{:.0f} dias, {:.0f} horas, {:.0f} minutos, {:.0f} segundos".format(dia, hora, minutos, totalsegundos))
#
# print(totalsegundos)
conversao = (86400, 3600, 60) #segundos por: dia, hora, minuto - criada a lista

entradaUsuario = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horasRestantes = (entradaUsuario % conversao[0]) # o resto da divisão da ENTRADA pela POSIÇÃO NA LISTA
minutosRestantes = (horasRestantes % conversao[1])

dias = entradaUsuario // conversao[0]
horas = horasRestantes // conversao[1]
minutos = minutosRestantes // conversao[2]
segundos = minutosRestantes % conversao[2]

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))