#criar uma maquina que jogue com o jogador revezando entre eles, quem acertar primeiro ganha.

#importar a listad
#robô escolher um número de acordo com a dificuldade do jogo
#fazer jogador e maquina revezarem 
#verificar se o jogador e a máquina acertaram

from dificuldades import listad, numero_escolhido
from random import choice



def tentativa_pc(maquina):
    maquina = choice(maquina)
    return maquina

def apagarNumeros(maquina_Tentativa, numero_escolhido, lista):
    if maquina_Tentativa > numero_escolhido:
        lista = [n for n in lista if n < maquina_Tentativa]
    elif maquina_Tentativa < numero_escolhido:
        lista = [n for n in lista if n > maquina_Tentativa]
    return lista


contador = 0

maquina_lista_escolha = listad.copy()


