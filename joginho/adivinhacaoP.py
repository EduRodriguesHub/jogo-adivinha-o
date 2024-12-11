from tela_inicio import titulo, subtitulo, lista_de_dificuldade
from cores import azul_claro, amarelo
from dificuldades import listad, numero_escolhido, escolha
from versus_maquina import tentativa_pc, apagarNumeros
from time import sleep
from random import choice
titulo
sleep(0.5)
subtitulo
sleep(0.5)
lista_de_dificuldade()
contador = 1
maquina_lista_escolha = listad.copy()
intervalo = len(listad)
tentativa = escolha('')
computador_tentativa = ''
while True:
    # Checa se o jogador acertou
    if tentativa == numero_escolhido:
        sleep(0.5)
        print(f"{azul_claro}Parabéns! Você acertou o número {amarelo}{numero_escolhido}\033[m {azul_claro}em {contador} tentativas!\033[m")
        break

    # Feedback para o jogador
    if tentativa < numero_escolhido:
        sleep(0.5)
        print("Jogador chutou baixo!")
    else:
        sleep(0.5)
        print("Jogador chutou alto!")

    # Jogada do computador
    if computador_tentativa == '':
        computador_tentativa = choice(listad)
    sleep(0.5)
    print(f"{amarelo}COMPUTADOR\033[m: eu escolhi {computador_tentativa}")

    # Checa se o computador acertou
    if computador_tentativa == numero_escolhido:
        sleep(0.5)
        print(f"{azul_claro}O computador acertou o número {amarelo}{numero_escolhido}\033[m {azul_claro}em {contador} tentativas!\033[m")
        break

    # Feedback para o computador
    if computador_tentativa < numero_escolhido:
        sleep(0.5)
        print("Computador chutou baixo!")
    else:
        sleep(0.5)
        print("Computador chutou alto!")
    sleep(0.5)
    maquina_lista_escolha = apagarNumeros(computador_tentativa, numero_escolhido, maquina_lista_escolha)
    print(maquina_lista_escolha)
    tentativa = escolha(tentativa)
    computador_tentativa = tentativa_pc(maquina_lista_escolha)
    contador += 1