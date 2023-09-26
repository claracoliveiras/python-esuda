MATRIZ = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
numeroMult = 2

def multiplicarMatriz(matriz, numero):
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            matriz[x][y] *= numero
    
    return matriz

print(multiplicarMatriz(MATRIZ, numeroMult))