from cores import vermelho
from random import choice
 # verifica se o número está no nível de dificuldade ou não se encaixa, ex: (str)
def verify(escolhas):
        while True:
            try:
                user = int(input('Escolha: '))
                if user in escolhas:
                        return user
                print(f'{vermelho}Não tem esse número na lista, escolha outro:\033[m')
            except:
                print(f'{vermelho}Um número entre 1 e 4 por gentileza!\033[m')
        
        
def dificuldade(usuario, lista):
    '''while True:
        try:
            base = 0
            if usuario == 1:
                while len(lista) < 50:
                    base = base + 1
                    lista.append(base)
                return lista
            elif usuario == 2:
                while len(lista) < 100:
                    base += 1
                    lista.append(base)
                return lista
            elif usuario == 3:
                while len(lista) < 150:
                    base += 1
                    lista.append(base)
                return lista
            elif usuario == 4:
                while len(lista) < 200:
                    base += 1
                    lista.append(base)
                return lista
            elif usuario not in [1, 2, 3, 4]:
                while len(lista) < usuario:
                    base += 1
                    lista.append(base)
                return(lista)
        except ValueError:
            print('Um número por gentileza!')'''
    try:
        tamanhos = {1: 50, 2: 100, 3: 150, 4: 200}
        limite = tamanhos.get(usuario, usuario)
        listad.extend(range(1, limite+1))
        return listad
    except ValueError:
        print('Um número por gentileza!')
    return lista

def escolher_Numero(numero):
    choic = choice(numero)
    return choic

def escolha(opc):
    while True:
        try:
            opc = int(input(f"Escolha um número de 1 a {intervalo}: "))
            return opc
        except:
            print('Número Inválido!')

def personalizado(pers):
    while True:
        try:
            pers = int(input('Escolha a quantidade de números de chutes:'))
            return pers
        except:
            print('Valor Inválido')

listad = []
personalizado_ou_pronto = int(input('Você quer um número personalizado ou pronto? \n1-Pronto \n2-Personalizado:'))
try:
    if personalizado_ou_pronto == 1:
        opcoes = [1, 2, 3, 4]
        user = verify(opcoes)
        dificuldade(user, listad)
    elif personalizado_ou_pronto == 2:
        numero_user = []
        personalizado_usuario = personalizado(numero_user)
        dificuldade(personalizado_usuario, listad)
    else:
        print('Inválido')
except:
    print('Inválido')


intervalo = len(listad)
numero_escolhido = escolher_Numero(listad)
