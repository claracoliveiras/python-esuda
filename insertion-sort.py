lista = [42, 34, 24, 13, 7]

def insertionSort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        buraco = i

        while buraco > 0 and lista[buraco - 1] > valor:
            lista[buraco] = lista[buraco - 1]
            buraco -= 1
        lista[buraco] = valor

insertionSort(lista)
print(lista)

