MATRIZ = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
MATRIZ2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
MULT = []

def multCheck(MATRIZ, MATRIZ2, MULT):
    if len(MATRIZ2[0]) == len(MATRIZ[0]) and len(MATRIZ) == len(MATRIZ2):
        for x in range(len(MATRIZ)):
            for y in range(len(MATRIZ)):
                MULT += [MATRIZ[x][y] * MATRIZ[x][y]]
        return MULT
    else:
        return "O tamanho das matrizes é diferente"
    
print(multCheck(MATRIZ, MATRIZ2, MULT))