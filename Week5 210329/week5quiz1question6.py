inputValue = int(input("Please enter a large number and all of it's digits will be added together "))
digits = str(inputValue)
digitList = []
i = 0
while (i < len(digits)):
    digitList.append(digits[i])
    i += 1
for i in range(0, len(digitList)):
    digitList[i] = int(digitList[i])
total = sum(digitList)
print (total)