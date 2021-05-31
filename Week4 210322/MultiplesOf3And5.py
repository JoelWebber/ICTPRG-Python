total = 0
maxValue = 20

for i in range (0, 20):
    if ((i % 3) == 0 or (i % 5) == 0):
        total += i
        print(total)

    
