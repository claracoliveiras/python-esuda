MATRIZ1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
MATRIZ2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

def comparaMatriz(MATRIZ1, MATRIZ2):
    for i in range(len(MATRIZ1)):
        if MATRIZ1[i] != MATRIZ2[i]:
            return False
    return True

print(comparaMatriz(MATRIZ1, MATRIZ2))
