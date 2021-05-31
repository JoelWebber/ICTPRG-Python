stringInput = input ("Please input a random set of characters: ")
stringList = list(stringInput)

if (len(stringList) > 7):
    while (len(stringList) > 3):
        stringList.pop(0)
        if (len(stringList) > 3):
            stringList.pop(-1)
    for i in range(len(stringList)):
        if stringList[i] != stringList[-1]:
            print(stringList[i], end = ', ')
        else:
            print(stringList[i], end = '')
else:
    print("The string was less than 8 characters")
