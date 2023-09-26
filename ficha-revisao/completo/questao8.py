tamanhoLinhas = int(input("Insira a quantidade de linhas da primeira matriz "))
colunasMatriz = int(input("Insira as colunas da primeira matriz: "))
MATRIZ = [[0] * tamanhoLinhas] * colunasMatriz

tamanhoLinhas2 = int(input("Insira a quantidade de linhas da segunda matriz "))
colunasMatriz2 = int(input("Insira as colunas da segunda matriz: "))
MATRIZ2 = [[0] * tamanhoLinhas] * colunasMatriz
MATRIZMULT = [[0] * tamanhoLinhas] * colunasMatriz


if tamanhoLinhas == tamanhoLinhas2 and colunasMatriz == colunasMatriz2:
    #Preenchendo matriz 1
    for x in range(len(MATRIZ)):
        for y in range(len(MATRIZ)):
            MATRIZ[x][y] = int(input("Preencha a matriz 1:"))
    
    #Preenchendo matriz 2
    for x in range(len(MATRIZ)):
        for y in range(len(MATRIZ)):
            MATRIZ2[x][y] = int(input("Preencha a matriz 2:"))
            
    print("ok")
    for x in range(len(MATRIZ)):
        for y in range(len(MATRIZ)):
            MATRIZMULT[x][y] = MATRIZ[x][y] * MATRIZ2[x][y]
else:
    print("meh")

print(MATRIZMULT)
