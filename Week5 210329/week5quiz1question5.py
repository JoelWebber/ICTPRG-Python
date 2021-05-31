inputValue = ""
numberList = []
while (inputValue != 'x'):
    inputValue = input("Please enter numbers. If you enter x you will be shown all the numbers you have entered ")
    if (inputValue != 'x'):
        numberList.append(inputValue)

print(numberList)