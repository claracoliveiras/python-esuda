MATRIZ = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def ehDiagonal(MATRIZ):
    flag = True
    
    for x in range (len(MATRIZ)):
        for y in range(len(MATRIZ)):
            if x != y and MATRIZ[x][y] != 0:
                flag = False
    
    return flag

print(ehDiagonal(MATRIZ))