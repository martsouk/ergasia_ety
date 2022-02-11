import random

tries = 0
for game in range(100):
    notwin = True
    rows, cols = (3, 3)
    square = []
    for i in range(rows) :
        col = []
        for j in range(cols):
            col.append(0)
        square.append(col)
    rings = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
    random.shuffle(rings)
    help = []
    for i in range(3) :
        help.append(i)
    count = 0
    while notwin :
        tries = tries + 1
        if count != 27 :
            random.shuffle(help)
            x = help[1]
            random.shuffle(help)
            y = help[1]
            if square[x][y] == 0 :
                square[x][y] = rings[count]
            elif  square[x][y] <= 3 :
                if square[x][y] == 1 :
                    if rings[count] == 2 :
                        square[x][y] = 12
                    if rings[count] == 3 :
                        square[x][y] = 13
                elif square[x][y] == 2 :
                    if rings[count] == 1 :
                        square[x][y] = 12
                    if rings[count] == 3 :
                        square[x][y] = 23
                elif square[x][y] == 3 :
                    if rings[count] == 1 :
                        square[x][y] = 13
                    if rings[count] == 2 :
                        square[x][y] = 23
            else :
                if square[x][y] == 12 :
                    if rings[count] == 3 :
                        square[x][y] = 123
                if square[x][y] == 13 :
                    if rings[count] == 2:
                        square[x][y] =123
                if square[x][y] == 23 :
                    if rings[count] == 1 :
                        square[x][y] = 123

            if count >= 3 :
                for i in range(1,4) :
                    for j in range(3) :
                        if i == 1 :
                            k = 12
                            l = 13
                        if i == 2 :
                            k = 12
                            l = 23
                        if i == 3 :
                            k = 13
                            l = 23
                        if (square[j][0] == i or square[j][0] == 123 or square[j][0] == k or square[j][0] == l) and (square[j][1] == i or square[j][1] == 123 or square[j][1] == k or square[j][1] == l) and (square[j][2] == i or square[j][2] == 123 or square[j][2] == k or square[j][2] == l):
                            notwin = False
                            i = 10
                            j = 10
                if notwin == True :
                    for i in range(1,4) :
                        for j in range(3) :
                            if i == 1 :
                                k = 12
                                l = 13
                            if i == 2 :
                                k = 12
                                l = 23
                            if i == 3 :
                                k = 13
                                l = 23
                            if (square[0][j] == i or square[0][j] == 123 or square[0][j] == k or square[0][j] == l) and (square[1][j] == i or square[1][j] == 123 or square[1][j] == k or square[1][j] == l) and (square[2][j] == i or square[2][j] == 123 or square[2][j] == k or square[2][j] == l):
                                notwin = False
                                i = 10
                                j = 10
                if notwin == True :
                    for i in range(1,4) :
                        if i == 1 :
                            k = 12
                            l = 13
                        if i == 2 :
                            k = 12
                            l = 23
                        if i == 3 :
                            k = 13
                            l = 23
                        if (square[0][0] == i or square[0][0] == 123 or square[0][0] == k or square[0][0] == l) and (square[1][1] == i or square[1][1] == 123 or square[1][1] == k or square[1][1] == l) and (square[2][2] == i or square[2][2] == 123 or square[2][2] == k or square[2][2] == l):
                            notwin = False
                            i = 10
                            j = 10
                        if (square[0][2] == i or square[0][2] == 123 or square[0][2] == k or square[0][2] == l) and (square[1][1] == i or square[1][1] == 123 or square[1][1] == k or square[1][1] == l) and (square[2][0] == i or square[2][0] == 123 or square[2][0] == k or square[2][0] == l):
                            notwin = False
                            i = 10
                            j = 10
                if notwin == True :
                    for i in range(1,4) :
                        for j in range(3) :
                            if (square[j][0] == 1 or square[j][0] == 123 or square[j][0] == 12 or square[j][0] == 13) and (square[j][1] == 2 or square[j][1] == 123 or square[j][1] == 12 or square[j][1] == 23) and (square[j][2] == 3 or square[j][2] == 123 or square[j][2] == 13 or square[j][2] == 23):
                                notwin = False
                                i = 10
                                j = 10
                if notwin == True :
                    for i in range(1,4) :
                        for j in range(3) :
                            if (square[0][j] == 1 or square[0][j] == 123 or square[0][j] == 12 or square[0][j] == 13) and (square[1][j] == 2 or square[1][j] == 123 or square[1][j] == 12 or square[1][j] == 23) and (square[2][j] == 3 or square[2][j] == 123 or square[2][j] == 13 or square[2][j] == 23):
                                notwin = False
                                i = 10
                                j = 10
                if notwin == True :
                        if (square[0][0] == 1 or square[0][0] == 123 or square[0][0] == 12 or square[0][0] == 13) and (square[1][1] == 2 or square[1][1] == 123 or square[1][1] == 12 or square[1][1] == 23) and (square[2][2] == 3 or square[2][2] == 123 or square[2][2] == 23 or square[2][2] == 13):
                            notwin = False
                            i = 10
                            j = 10
                        if (square[0][2] == 3 or square[0][2] == 123 or square[0][2] == 13 or square[0][2] == 23) and (square[1][1] == 2 or square[1][1] == 123 or square[1][1] == 12 or square[1][1] == 23) and (square[2][0] == 1 or square[2][0] == 123 or square[2][0] == 12 or square[2][0] == 13):
                            notwin = False
                            i = 10
                            j = 10
            count = count + 1
        else:
            notwin = False
mo = tries/100
print("Ο μέσος όρος κινήσεων για τον τερματισμό 100 παιχνιδιών: ", mo)
