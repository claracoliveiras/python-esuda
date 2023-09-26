#5. Crie uma função que receba uma matriz como entrada e retorne o maior valor encontrado na matriz.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
maiorValor = 0

for x in range(len(matriz)):
    for y in range(len(matriz)):
        if matriz[x][y] > maiorValor:
            maiorValor = matriz[x][y]

print(maiorValor)