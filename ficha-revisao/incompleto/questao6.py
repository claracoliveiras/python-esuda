MATRIZ = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
position1 = 0
position2 = 0
flag = True
flag0 = False

while position1 < 3:
    print(position1, position2)
    if flag == True:
        if MATRIZ[position1][position2] == 1:
            position1 += 1
            position2 += 1
            flag = True
            

        else:
            for i in range(position2+1, 3):
                if MATRIZ[position1][i] == 0:
                    flag0 = True
                    break
                else: 
                    flag0 = False
    else:
        print("A matriz não tem 1 em todas as suas diagonais")
        break



print (flag0)