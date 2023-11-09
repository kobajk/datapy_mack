import random as rd
import matplotlib.pyplot as plt

def dado():
    return rd.randrange(1,6)

def jogo():
    print('\n Jogador ',i)
    entrada = [1,4,9,17,21,28,51,54,62,64,72,80,87,93,94,98]
    saida = [38,14,31,7,42,84,67,34,19,60,91,99,36,73,75,79]
    pos = 0
    rodada = 0
    listaposicao = []
    listarodada = []
    while pos < 100:
        listaposicao.append(pos)
        listarodada.append(rodada + 1)
        pos += dado()
        rodada += 1
        if pos in entrada:
            x = entrada.index(pos)
            pos = saida[x]
    print(f' A quantidade de rodadas para o Jogador {i} foi {rodada}')
    plt.plot(listarodada, listaposicao)
    plt.ylabel(' Posição ')
    plt.xlabel(' Rodada ')
    plt.legend(jogadores)
    return sum(listarodada)



nj = int(input(' Informe a quantidade de jogadores que irão jogar: '))

jogadores = [1]
ganhador = []
for i in range(1,nj+1):
    ganhador.append(jogo())
    jogadores.append(i+1)

print(f'\n O vencedor do jogo foi o Jogador n°: {ganhador.index(min(ganhador)) + 1}')


