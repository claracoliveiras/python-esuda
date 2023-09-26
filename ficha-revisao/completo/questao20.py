somaK = 4
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
paresElementos = []

for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x] + lista[y] == somaK:
            paresElementos += [(lista[x], lista[y])]

print(paresElementos)

