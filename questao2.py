lista = [" "] * 10
ultimaPosOcupada = -1

def adicionarString(palavra, lista, ultimaPos):
    if ultimaPos < len(lista) - 1:
        for i in range(len(lista)):
            


    return ultimaPos

def removerString(palavra, lista, ultimaPos):
    if palavra in lista:
        for i in range(len(lista)):
            if lista[i] == palavra:
                j = i
                while j != len(lista) - 1:
                    lista[j] = lista[j + 1]
                    j += 1
                ultimaPos -= 1
        return ultimaPos
    else:
        print("Não há o que remover.")

def exibirLista(lista):
    for nome in lista:
        print(nome)