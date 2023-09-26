MATRIZ = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
flag = True
flag0 = True

for x in range (len(MATRIZ)):
    for y in range(len(MATRIZ)):
        if MATRIZ[x][x] != 1:
            flag = False
            
        if x != y and MATRIZ[x][y] != 0:
            flag0 = False
        