MATRIZ = [[1, 2, 3], [1, 2, 3]]
MATRIZ2 = [[1, 2, 3], [1, 2, 3]]

def saoIguais(matriz1, matriz2):
    flag = True
    for x in range(len(matriz1)):
        for y in range(len(matriz2)):
            if matriz1[x] != matriz2[y]:
                flag = False
                break
    return flag

print(saoIguais(MATRIZ, MATRIZ2))