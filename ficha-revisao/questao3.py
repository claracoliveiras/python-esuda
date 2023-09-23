#3. Implemente uma função que calcule a transposta de uma matriz (troque linhas por colunas).

MATRIZ = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
TRANSPOSTA = [[0 for j in range(3)] for i in range(3)]

for x in range(3):
    for y in range(3):
        TRANSPOSTA[x][y] = MATRIZ[y][x]

print(TRANSPOSTA)