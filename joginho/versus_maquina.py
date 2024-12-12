#criar uma maquina que jogue com o jogador revezando entre eles, quem acertar primeiro ganha.

#importar a listad
#robô escolher um número de acordo com a dificuldade do jogo
#fazer jogador e maquina revezarem 
#verificar se o jogador e a máquina acertaram

from dificuldades import listad, numero_escolhido
from random import choice


def apagarNumeros(maquina_Tentativa, numero_escolhido, lista):
    novaLista = []
    if maquina_Tentativa > numero_escolhido:
        for n in lista:
            if n < maquina_Tentativa:
                novaLista.append(n)
        return novaLista
    elif maquina_Tentativa < numero_escolhido:
        for n in lista:
            if n > maquina_Tentativa:
                novaLista.append(n)
        return novaLista

maquina_lista_escolha = listad.copy()
