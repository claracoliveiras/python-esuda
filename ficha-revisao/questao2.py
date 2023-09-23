#2. Crie uma função que receba uma matriz como entrada e retorne a soma de todos os elementos da matriz.
MATRIZ = [[0] * 3] * 3

def somaMatriz(matriz):
    soma = 0;
    for i in range(len(matriz)):
        for x in range(len(matriz)):
            soma = soma + matriz[i][x]
    return soma

print(somaMatriz(MATRIZ))