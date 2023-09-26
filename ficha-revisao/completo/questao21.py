lista = [1, 2, 3, 4, 5, 6]

def temDuplicata(lista):
    lista2 = []
    for i in range(len(lista)):
        if lista[i] not in lista2:
            lista2 += [lista[i]]
    if len(lista) != len(lista2):
        return "Tem duplicatas"
    return "N tem duplicata"

print(temDuplicata(lista))