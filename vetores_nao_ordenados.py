from random import randint

ULTIMA_POSICAO = 0
vetor = [-1] * 100
TAMANHO_MAX = len(vetor) - 1


def adicionar_vetor(lista, adicionar_numero):
    global ULTIMA_POSICAO
    if ULTIMA_POSICAO != len(lista):
        lista[ULTIMA_POSICAO] = adicionar_numero
        ULTIMA_POSICAO += 1


def pesquisar_vetor(lista, pesquisar_numero):
    for i, numero in enumerate(lista):
        if pesquisar_numero == numero:
            return i
        return False


def excluir_vetor(lista, excluir_numero):
    i = 0
    excluiu = False
    while i < len(lista):
        if lista[i] == excluir_numero:
            lista[i] = lista[i + 1]
            excluiu = True
        elif excluiu and i < (len(lista) - 1):
            lista[i] = lista[i + 1]
        elif i == (len(lista) - 1):
            lista[i] = None

        i += 1

    return lista


listaaa = [1, 2, 3, 4]
print(excluir_vetor(listaaa, 2))

# Comentar essa linha caso queira testar o método de adicionar
# for i in range(len(vetor)):
#    adicionar_vetor(vetor, randint(1, 100))

# print(vetor)
# print(pesquisar_vetor(vetor, 12))
