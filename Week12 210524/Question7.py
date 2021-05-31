


def PrintBoxByWidth(columns):
    rows = 5
    
    for i in range(rows):
        for x in range(columns):
            if (x == 0 or x == columns - 1) or (i == 0 or i == rows - 1 ):
                print("x", end='')
            elif(i == (rows - 1) / 2):
                print("o", end = '')
            else:
                print(" ", end='')
        print("")

    

PrintBoxByWidth(60)
