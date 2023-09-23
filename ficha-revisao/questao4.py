#4. Escreva um programa que leia duas matrizes do mesmo tamanho do usuário e exiba a soma das duas matrizes.
tamanhoLinhas = int(input("Insira a quantidade de linhas da matriz "))
colunasMatriz = int(input("Insira as colunas da matriz: "))
MATRIZ = [[-1] * tamanhoLinhas] * colunasMatriz
MATRIZ2 = [[-1] * tamanhoLinhas] * colunasMatriz
SOMA = [[0] * tamanhoLinhas] * colunasMatriz

print("Matriz 1")
for x in range(len(MATRIZ)):
    for y in range(len(MATRIZ)):
        MATRIZ[x][y] = int(input(f"Insira os numeros da linha {x}: "))

print("Matriz 2")
for x in range(len(MATRIZ)):
    for y in range(len(MATRIZ)):
        MATRIZ2[x][y] = int(input(f"Insira os numeros da linha {x}: "))

for x in range(len(MATRIZ)):
    for y in range(len(MATRIZ)):
        SOMA[x][y] = MATRIZ[x][y] + MATRIZ2[x][y]

print(SOMA)