inputValue = ""
numberList = []
while (inputValue != 'x'):
    inputValue = input("Please enter numbers. If you enter x you will be shown all the numbers you have entered that repeat themselves ")
    if (inputValue != 'x'):
        numberList.append(inputValue)
repeatedNumbers = []
x = 0
for i in range(len(numberList)):
    for x in range(i, len(numberList)):
        if (i != x):
            if (numberList[int(i)] == numberList[x]):
                repeatedNumbers.append(numberList[i])
                break


print(repeatedNumbers)
