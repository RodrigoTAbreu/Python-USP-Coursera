def computador_escolhe_jogada(n,m):
    print("Computador começa!")
    retirar = 1
    while retirar != m:
        if (n - retirar) % (m + 1) == 0:
            return retirar
        else:
            retirar +=1
    return retirar


def usuario_escolhe_jogada(n,m):

    print("Você começa!")
    # jogador_retira = int(input("Quantas peças vai retirar? "))
    play = False
    while not play:
        jogador_retira = int(input("Quantas peças vai retirar? "))
        if jogador_retira <1 or jogador_retira > m:
            print("Ops ! Jogada inválida. Tente novamente.")
        else:
            play = True
        return jogador_retira

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogador? "))
    compu = False
    if n % (m + 1) == 0:

        usuario_escolhe_jogada(n, m)
    else:
        computador_escolhe_jogada(n, m)
        compu = True
    while n > 0:
        if compu:
            saida = computador_escolhe_jogada(n,m)
            n -= saida
            if saida == 1:
                print("\nComputador removeu uma peça.")
            else:
                print(f"\nComputador removeu {saida} peças")
            compu = False
        else:
            saida = usuario_escolhe_jogada(n,m)
            n -= saida
            if saida == 1:
                print("\nVocê removeu uma peça")
            else:
                print(f"\nVocê removeu {saida} peças")
            compu = True
        if n == 1:
            print("\nAgora uma peça foi permanece do tabuleiro.")
        elif n != 0 :
            print(f"\nAgora {n} peças permanecem no tabuleiro ")
    print("Game Over ! Computador vence")

def campeonato():
    jogo = 1
    while jogo <= 3:
        print(f"\n**** Jogo {jogo} ****")
        partida()
        jogo += 1
    print("*** Final de Campeonato ****")
    print(f"\nPlacar: Você 0 x 3 Computador")

print(" Bem-vindo ao jogo do NIM! Escolha:\n")
print('1 - para jogar uma partida isolada.\n')
escolha = (int(input('2 - para jogar um campeonato.\n')))

if escolha == 1:
    partida()
elif escolha == 2:
    print("Você escolheu campeonato")
    campeonato()
