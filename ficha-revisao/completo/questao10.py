MATRIZ = [[1, 2, 3], [1, 2, 3]]

for x in range(len(MATRIZ)):
    for y in range(len(MATRIZ[0])):
        if MATRIZ[x][y] % 2 > 0:
            MATRIZ[x][y] = 1
        else:
            MATRIZ[x][y] = 0

print(MATRIZ)